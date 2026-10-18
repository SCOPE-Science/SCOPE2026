#!/usr/bin/env python3
"""Exact finite-state and formula checks for a root-doubling tree size limit.

All infinite and ergodic assertions are proved analytically in RESULT.md, not by this checker.
"""
from fractions import Fraction
from math import prod

states={0:Fraction(1)}
checks=0
moments=[]
for n in range(1,13):
    nxt={}
    for b,p in states.items():
        assert b>=0 and p>0
        ordinary=Fraction(b,b+1)
        doubling=Fraction(1,b+1)
        assert ordinary+doubling==1
        checks+=1
        for v,q in ((b+1,ordinary),(2*b+2,doubling)):
            if q:
                nxt[v]=nxt.get(v,Fraction(0))+p*q
    states=nxt
    assert sum(states.values())==1
    mean=sum(Fraction(b)*p for b,p in states.items())
    second=sum(Fraction(b*b)*p for b,p in states.items())
    assert mean==2*n,(n,mean)
    assert second==5*n*n-n,(n,second)
    moments.append((n,mean,second))
    checks+=3
for n in range(1,51):
    for b in range(n,4*n+1):
        x=Fraction(b,n)
        phi=Fraction(b+1,n+1)
        exact_p=Fraction(1,b+1)
        assert Fraction(1,n)*Fraction(1,x)/ (1+Fraction(1,n)*Fraction(1,x))==exact_p
        assert 2*phi==Fraction(2*b+2,n+1)
        checks+=2
for k in range(1,10):
    mk=prod(Fraction(j-1+2**j,j) for j in range(1,k+1))
    mprev=prod(Fraction(j-1+2**j,j) for j in range(1,k))
    assert k*mk==(k-1+2**k)*mprev
    checks+=1
for z_num in range(1,20):
    z=Fraction(z_num,40)
    for u_num in range(1,20):
        u=Fraction(u_num,20)
        h=1/z
        y=h/(u+h*(1-u))
        z_next=Fraction(1,2*y)
        assert z_next==(1-u+u*z)/2
        checks+=1
print('PASS:',checks,'exact rational identities; finite n up to 12; moment recursion through k=9')
print('Finite exact moments:',moments)
print('No claim of computer proof for the weak limit.')
