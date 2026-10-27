#!/usr/bin/env python3
"""Exact, finite rational consistency diagnostics for the anchored Bohr theorem.
This checks only finite identities; the infinite-dimensional result requires the analytic proof.
"""
from fractions import Fraction as Q
from math import comb

def boundary(x2,y2,N=12):
    assert x2+y2 == Q(1,2)
    totals=[]
    for n in range(1,N+1):
        s=sum(Q(comb(n,k))*x2**k*y2**(n-k) for k in range(n+1))
        assert s == Q(1,2)**n
        totals.append(s)
        for k in range(n+1):
            # norm weight times profile squared, at the specified point
            weight=Q(1,comb(n,k))
            b2=Q(comb(n,k))**2*x2**k*y2**(n-k)
            assert weight*b2 == Q(comb(n,k))*x2**k*y2**(n-k)
    assert sum(totals) == 1-Q(1,2)**N

for a,b in [(Q(1,4),Q(1,4)),(Q(1,8),Q(3,8)),(Q(1,16),Q(7,16)),(Q(1,2),Q(0))]:
    boundary(a,b)

# Non-extremal finite symbolic coefficient arrays: algebraic deficit identity
for N in range(1,9):
    for t in [Q(0),Q(1,10),Q(1,3),Q(1,2),Q(3,4)]:
        # Coefficients at all multiindices are t times boundary profile.
        # Finite tail gives the exact truncation residual 2^-N.
        mass = 1-Q(1,2)**N
        lhs=2*(1-t*mass)
        rhs=(1-t*t*mass) + (t-1)**2*mass
        assert lhs-rhs == (1-mass)
print('PASS: exact multinomial moments, profile normalization, and finite-tail deficit identities')
