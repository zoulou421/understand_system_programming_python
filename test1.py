"""
There are three standard flows:
----Standard input: it is called when you use input. This is what is used to request information
to the user. By default, standard input is your keyboard.
----Standard output: as we have seen, this is what is used to display messages. By default, it redirects to
the screen.
-----The standard error: it is used in particular when Python shows you the traceback of an exception. By default,
it also redirects to your screen.

We can access the objects representing these standard flows.The sys module
offers several functions and variables
allowing you to interact with the system.
"""
import sys
import os

#standard input
sys.stdin

#standard output
sys.stdout

#standard error
sys.stderr

sys.stdout.write("a test")
sys.stdout.write("a test\n")

file = open('output-file.txt', 'w')
sys.stdout = file
print("My first test file...")
"""
A small subtlety: if you try to call getcwd directly, the result will not be displayed on the screen...it will be
written to the file. To revert to the old standard output, type the line:
"""
sys.stdout = sys.__stdout__
#Now you can do:
os.getcwd() #file output-file.txt is created

"""
If you modified the standard flows and are looking for the original objects, those redirecting to the keyboard (for input) and
to the screen (for outputs), you can find them in sys.__stdin__, sys.__stdout__ and sys.__stderr__.
The Python documentation nevertheless advises us to preferably keep the original objects on hand rather than
to look for them in sys.__stdin__, sys.__stdout__ and sys.__stderr__
"""


















