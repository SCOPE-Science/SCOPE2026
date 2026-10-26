#!/usr/bin/env python3
"""Reproduce arithmetic checks of a base-uniform affine digit-reversal theorem."""
from math import isqrt

def digits(n,b):
    a=[]
    while n:
        a.append(n%b)
        n//=b
    return a

def rev(n,b):
    r=0
    for a in digits(n,b):
        r=r*b+a
    return r

def predicted(b,l):
    if b<10 or b%3!=1: return None
    n=((b+5)*b**(l-1)-(b-7))//3
    return n

def check_small():
    tests=0
    for b in range(4,15):
        for l in range(2,6):
            found=[]
            for n in range(b**(l-1),b**l):
                if n%b and rev(n,b)==2*n-4:
                    found.append(n)
            expected=[predicted(b,l)] if predicted(b,l) is not None else []
            assert found==expected, (b,l,found,expected)
            tests+=1
    return tests

def check_constructive():
    cases=0
    for b in range(10,1000,3):
        for l in [2,3,4,5,8,12]:
            n=predicted(b,l)
            d=digits(n,b)
            assert len(d)==l and d[0]==(2*b+7)//3 and d[-1]==(b+2)//3
            assert all(x==b-1 for x in d[1:-1]); assert rev(n,b)==2*n-4
            cases+=1
    return cases

def check_primes():
    for n in [107,109,1787,1789]:
        assert n>1 and all(n%d for d in range(2,isqrt(n)+1))
    for n,l in [(109,2),(1789,3)]:
        assert n==predicted(16,l)
        assert rev(n,16)==2*(n-2)
    return 4

if __name__=='__main__':
    print('VERIFIED',check_small(),'complete finite base/length domains;',check_constructive(),'constructed cases;',check_primes(),'trial-divided primes')
