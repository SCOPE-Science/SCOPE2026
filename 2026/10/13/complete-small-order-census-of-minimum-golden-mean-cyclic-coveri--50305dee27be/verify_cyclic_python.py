#!/usr/bin/env python3
"""Independent exhaustive shortest cyclic-cover census for no-adjacent-one binary language."""
from itertools import product
from collections import Counter

def fib(t):
    a,b=0,1
    for _ in range(t):a,b=b,a+b
    return a

def shifts(w):
    for i in range(len(w)):
        yield w[i:]+w[:i]

def canon(w):
    return min((*shifts(w), *shifts(w[::-1])))

def classify(n):
    length=fib(n+2)+fib(n)-1
    legal={''.join(bits) for bits in product('01',repeat=n) if '11' not in ''.join(bits)}
    cnt=Counter()
    # Full finite recursion prunes exactly the sequences with internal 11.
    def visit(prefix):
        if len(prefix)==length:
            if prefix[0]==prefix[-1]=='1':return
            blocks={''.join(prefix[(j+k)%length] for k in range(n)) for j in range(length)}
            if blocks==legal:
                cnt[canon(prefix)]+=1
            return
        visit(prefix+'0')
        if not prefix or prefix[-1]=='0':visit(prefix+'1')
    visit('')
    return length,cnt

def main():
    actual=[]
    for n in range(2,7):
        length,cat=classify(n)
        labelled=sum(cat.values())
        hist=Counter(cat.values())
        print(f'{n}\t{length}\t{labelled}\t{len(cat)}\t{sorted(hist.items())}')
        actual.append((labelled,len(cat),sorted(hist.items())))
    expect=[(3,1,[(3,1)]),(6,1,[(6,1)]),(20,1,[(20,1)]),
            (102,3,[(34,3)]),(2352,42,[(56,42)])]
    assert actual==expect,(actual,expect)
    print('PYTHON_CYCLIC_ENUMERATION_VERIFIED')
if __name__=='__main__':main()
