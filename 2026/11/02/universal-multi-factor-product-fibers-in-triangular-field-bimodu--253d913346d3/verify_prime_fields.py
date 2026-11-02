#!/usr/bin/env python3
"""Exact k-fold product-fiber distribution for two-by-two upper triangular matrices."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod

def multiply(x,y,q):
    a,b,c=x;d,e,f=y
    return (a*d%q,(a*e+b*f)%q,c*f%q)

def check(q,k):
    assert q in (2,3,5)
    R=list(product(range(q),repeat=3))
    hist=Counter(R)
    for _ in range(2,k+1):
        out=Counter()
        for a,count in hist.items():
            for b in R:out[multiply(a,b,q)]+=count
        hist=out
    p=Fraction(1,q);t=1-p;s=t**k;u=1-s;r=s/(q-1)
    E=1-k*t**(k-1)+(k-1)*t**k
    for a,b,c in R:
        if a==c==0:
            v=(u*u-E)/q+(E if b==0 else 0)
        elif a==0 or c==0:
            v=u*r/q
        else:v=r*r/q
        if Fraction(hist.get((a,b,c),0),q**(3*k))!=v:
            raise AssertionError((q,k,(a,b,c),hist.get((a,b,c),0),v))
    assert sum(hist.values())==q**(3*k)
    print('CHECK',q,k,'zero',hist[(0,0,0)],'nonzero_squarezero',(q-1)*hist[(0,1,0)],'total',q**(3*k))

if __name__=='__main__':
    for q in (2,3):
        for k in range(1,6):check(q,k)
    for k in range(1,4):check(5,k)
    print('VERIFY_OK')
