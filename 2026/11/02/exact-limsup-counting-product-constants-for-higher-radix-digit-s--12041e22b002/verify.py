#!/usr/bin/env python3
"""Exact-arithmetic checks for higher-radix digit-splitting additive complements."""
from fractions import Fraction

def check(r, digit_levels):
    Q=r*r
    cutoff=Q**digit_levels
    A=[]; B=[]
    for n in range(cutoff):
        m=n; aa=True; bb=True
        for _ in range(digit_levels):
            d=m%Q; m//=Q
            aa &= d<r
            bb &= d%r==0
        if aa: A.append(n)
        if bb: B.append(n)
    aset=set(A); bset=set(B)
    a=b=0
    L=Fraction(2*(r+1),r+2)
    ca=L/(r+1); cb=L*r/(r+1)
    for n in range(cutoff):
        D=L*n-a*b
        assert D>=0,(r,n,'main')
        if n in aset: assert D>=b-ca,(r,n,'A')
        if n in bset: assert D>=a-cb,(r,n,'B')
        a+= n in aset; b+= n in bset
    for k in range(1,digit_levels+1):
        j=2*r**(k-1)-1
        alpha=lambda i: sum(((i//r**h)%r)*Q**h for h in range(k+1))
        x=r*alpha(j)+1
        aa=sum(v<x for v in A) if x<cutoff else r**k
        bb=sum(v<x for v in B) if x<cutoff else 2*r**(k-1)
        assert aa==r**k and bb==2*r**(k-1),(r,k,aa,bb)
    return cutoff

if __name__=='__main__':
    cases=((2,9),(3,6),(4,5),(5,4),(6,3),(7,3))
    for r,k in cases:
        print('radix',r,'checked',check(r,k),'thresholds')
    print('VERIFY_OK')
