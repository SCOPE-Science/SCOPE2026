#!/usr/bin/env python3
"""Reproduce the exact moment identities and sharp-transition certificate.

Requires Python 3 and SymPy. All finite probabilities are exact Fractions.
"""
from collections import defaultdict
from fractions import Fraction as F
import sympy as sp

q=sp.symbols('q',integer=True,positive=True)
for k,sgn in ((4,1),(5,-1)):
    m=9*q+k
    ratio=(sp.prod(2*(m+s)/(2*(m+s)-1) for s in range(1,10))
           *(2*q+1)/(2*q+2)
           *(12*q+12+k)/(9*q+9+k)
           *(9*q+k)/(12*q+k))
    num,den=sp.fraction(sp.cancel(ratio-1))
    assert sp.Poly(num,q).all_coeffs() and sp.Poly(den,q).all_coeffs()
    assert all(int(c)*sgn>0 for c in sp.Poly(num,q).all_coeffs())
    assert all(int(c)>0 for c in sp.Poly(sp.expand(den),q).all_coeffs())

# The independent exact birth-time signs for q=1.
r=[F(1)]
for i in range(1,16):r.append(r[-1]*F(2*i,2*i-1))
assert r[13]/r[1]*F(16,52)==F(16777216,16900975)
assert r[14]/r[1]*F(17,56)==F(2097152,2064825)
print('POLYNOMIAL_CERTIFICATE_PASS')

def leaves_at_birth(j):
    d={1:F(1)}
    for n in range(2,j):
        g=2*n-1
        nd=defaultdict(F)
        for leaf,p in d.items():
            nd[leaf]+=p*F(leaf,g)
            nd[leaf+1]+=p*(1-F(leaf,g))
        d=nd
    return d

def advance(states,n):
    g=2*n-1
    new=defaultdict(F)
    for (L,W,B),p in states.items():
        assert 0<=B<=1 and 1<=W<=g and L>=B
        marked=F(W,g)
        other_leaf=F(L-B,g)
        other_internal=1-marked-other_leaf
        assert other_internal>=0
        new[(L+1-B,W+1,0)]+=p*marked
        new[(L,W,B)]+=p*other_leaf
        new[(L+1,W,B)]+=p*other_internal
    return new

checks=0
for j in range(2,10):
    states={(l,1,1):p for l,p in leaves_at_birth(j).items()}
    a=b=F(1)
    for n in range(j,min(j+16,26)):
        assert sum(states.values(),F(0))==1
        EW=sum((p*w for (l,w,t),p in states.items()),F(0))
        EL=sum((p*l for (l,w,t),p in states.items()),F(0))
        EWL=sum((p*w*l for (l,w,t),p in states.items()),F(0))
        EB=sum((p*t for (l,w,t),p in states.items()),F(0))
        assert EW==a and EB==b and EL==F(2*n-1,3)
        assert EWL-EW*EL==(a-1)/3+b-1
        checks+=4
        if n<min(j+16,26)-1:
            states=advance(states,n)
            a*=F(2*n,2*n-1)
            b*=F(2*n-2,2*n-1)
print('JOINT_PORT_DP_PASS', checks, 'exact assertions')

for j in range(2,100):
    a=b=F(1)
    for n in range(j,9*j-1):
        c=(a-1)/3+b-1
        if n==j:assert c==0
        elif n<=9*j-4:assert c<0,(j,n,c)
        else:assert c>0,(j,n,c)
        a*=F(2*n,2*n-1)
        b*=F(2*n-2,2*n-1)
print('EXACT_BIRTH_HORIZON_99_PASS')
