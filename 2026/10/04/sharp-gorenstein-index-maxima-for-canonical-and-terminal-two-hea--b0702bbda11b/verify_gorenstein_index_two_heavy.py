#!/usr/bin/env python3
from math import gcd, lcm

def index(r,a,b):
    L=lcm(a,b)
    S=r+a+b
    return L//gcd(L,S)

def canonical(r,a,b):
    d=b-a
    return 0 <= d <= r and 1 <= a <= r+d

def terminal(r,a,b):
    d=b-a
    return 0 <= d < r and 1 <= a < r+d

for r in range(2,201):
    C = 6 if r==2 else (2*r-3)*(3*r-4)
    expected = (2,3) if r==2 else (2*r-3,3*r-4)
    cmax=-1; cb=[]; tmax=-1; tb=[]
    for d in range(r+1):
        for a in range(1,r+d+1):
            b=a+d
            q=index(r,a,b)
            if canonical(r,a,b):
                if q>cmax: cmax=q; cb=[(a,b)]
                elif q==cmax: cb.append((a,b))
            if terminal(r,a,b):
                if q>tmax: tmax=q; tb=[(a,b)]
                elif q==tmax: tb.append((a,b))
    assert cmax==C and cb==[expected], (r,cmax,cb,C,expected)
    assert tmax==C and tb==[expected], (r,tmax,tb,C,expected)
    a,b=expected
    assert terminal(r,a,b)
print('VERIFY_OK r=2..200; canonical and terminal maxima, equality cases, and terminality of the maximizer agree')
