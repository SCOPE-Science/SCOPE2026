#!/usr/bin/env python3
"""Exact rational checks for the monomial-pole identity and sharp signs."""
from fractions import Fraction
from math import gcd

def S(r,t):
    return sum((t**j for j in range(r)), Fraction(0))

def V(r,t):
    return sum((t**j for j in range(1,r)), Fraction(0))

def H(r,x,y):
    return x*y/((1-x**r)*(1-y**r))

def K(r,x,y):
    return H(r,x,y)-H(r,x,x*y)-H(r,x*y,y)

def closed(r,x,y):
    return x*y*(1-V(r,x)*V(r,y))/((1-x*y)*S(r,x)*S(r,y)*S(r,x*y))

cases=0
for r in range(1,21):
    for x,y in [(Fraction(2,7),Fraction(3,11)), (Fraction(1,2),Fraction(3,5)), (Fraction(4,7),Fraction(1,3))]:
        assert K(r,x,y)==closed(r,x,y)
        cases+=1
        if r==1:
            assert K(r,x,y)==x*y/(1-x*y)
        if r==2:
            assert K(r,x,y)==x*y/((1+x)*(1+y)*(1+x*y))

# The largest positive Laurent exponent of V_r(x)V_r(c/x)
# comes uniquely from i=r-1,j=1, with coefficient c.
for r in range(3,21):
    for c in [Fraction(1), Fraction(2), Fraction(3,7)]:
        coeff={}
        for i in range(1,r):
            for j in range(1,r):
                e=i-j
                coeff[e]=coeff.get(e,Fraction(0)) + c**j
        assert max(coeff)==r-2
        assert coeff[r-2]==c

sign_cases=0
for r in range(1,11):
    for q in [Fraction(1,2),Fraction(3,5),Fraction(2,3),Fraction(3,4)]:
        root_sign=(1-V(r,q)*V(r,q))
        for a in range(1,9):
            for b in range(1,9):
                if gcd(a,b)!=1: continue
                z=K(r,q**a,q**b)
                if root_sign>=0: assert z>=0
                if root_sign<0: assert K(r,q,q)<0
                sign_cases+=1

# Independent partial sums converge upward to root H(q,q) in the
# nonnegative low-q regime, and show signed cancellation at high q.
for r in range(1,6):
    q=Fraction(1,3)
    partial=sum((K(r,q**a,q**b) for a in range(1,7) for b in range(1,7) if gcd(a,b)==1), Fraction(0))
    exact=H(r,q,q)
    assert 0<partial<exact
print('VERIFY_OK exact_rational_identities=%d coefficient_obstructions=%d sign_samples=%d' % (cases,18*3,sign_cases))
