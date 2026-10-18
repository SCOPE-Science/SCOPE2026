#!/usr/bin/env python3
"""Exact finite checks for the beta-mixed environmental germination theorem.
Only Python standard library is required. This is not an infinite-parameter proof.
"""
from fractions import Fraction as F
from math import comb

def d(k, a, b, h):
    # a,b are positive integer beta shapes; exact beta-binomial masses.
    # B=4 and s=1 in the subcritical test.
    def rising(x, n):
        v=1
        for j in range(n):v*=x+j
        return v
    return sum((F(comb(k,j)*rising(a,j)*rising(b,k-j), rising(a+b,k))
                * F(k-4*j, k*h+4*j*(1-h)))
               for j in range(k+1))

def d_critical(k, h):
    # Beta(2,1), B=2, s=1, exact expectation of derivative.
    return sum(F(2*(j+1), (k+1)*(k+2))
               * F(k-2*j, k*h+2*j*(1-h))
               for j in range(k+1))

for k in range(1,101):
    h=F(2,k+2)
    assert d_critical(k,h)==0, (k,'critical')
for k in range(30,101):
    assert d(k,2,1,F(3,k*k))>0, (k,'lower bracket')
    assert d(k,2,1,F(5,k*k))<0, (k,'upper bracket')
for k in range(1,36):
    # Beta(1/2,1/2) has beta-binomial mass central(2j,j)*central(2(k-j),k-j)/4^k.
    D=sum(F(comb(2*j,j)*comb(2*(k-j),k-j),4**k)
          * F(3*(k-4*j),k+8*j) for j in range(k+1))
    assert D>0, (k,'arcsine finite optimum above 1/3')
assert F(4,1) == F(2,1) / (1-F(1,2))
print('PASS: 100 exact critical identities, 71 exact two-sided brackets, 35 arcsine signs')
