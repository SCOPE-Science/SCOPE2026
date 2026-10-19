"""Self-contained finite cross-check for block-reversal images of three-marker words."""
from math import comb
from itertools import product

def reversal_set(word):
    n = len(word)
    found = set()
    for mask in range(1 << (n - 1)):
        start = 0
        pieces = []
        for i in range(n - 1):
            if (mask >> i) & 1:
                pieces.append(word[start:i + 1])
                start = i + 1
        pieces.append(word[start:])
        found.add(''.join(pieces[::-1]))
    return found

def predicted_set(a, b):
    length = a + b
    result = set()
    for p in range(b + 1):
        for s in range(a + 1):
            for q in range(length - p - s + 1):
                r = length - p - s - q
                result.add('0'*p+'1'+'0'*q+'1'+'0'*r+'1'+'0'*s)
    return result

def check():
    count=0
    for a,b in ((m,m) for m in range(8)):
        w='1'+'0'*a+'1'+'0'*b+'1'
        actual=reversal_set(w)
        expected=predicted_set(a,b)
        formula=(a+1)*(b+1)*(a+b+2)//2
        assert actual==expected,(a,b,len(actual),len(expected),next(iter(actual^expected)))
        assert len(actual)==formula,(a,b,len(actual),formula)
        count+=1
    print(f'PASS {count} source words (a=b=m, 0<=m<=7), exact image equality, cardinality')

if __name__=='__main__':check()
