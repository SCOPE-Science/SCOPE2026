#!/usr/bin/env python3
"""Finite exact sanity tests for the geometric block argument; not an infinite proof."""
from fractions import Fraction
from math import factorial

def near_geometric(m,n,J):
    x = Fraction(0)
    for j in range(J+1): x += Fraction((-m)**j,(n+1)**(j+1))
    actual=Fraction(1,m+n+1)
    return abs(x-actual) <= actual * Fraction(m,n+1)**(J+1)

def far_geometric(m,n,J):
    x = sum((Fraction((-n)**j,(m+1)**(j+1)) for j in range(J+1)),Fraction(0))
    actual=Fraction(1,m+n+1)
    return abs(x-actual) <= actual * Fraction(n,m+1)**(J+1)

def nuclear_upper_bound(n):
    # Explicit rank-one decomposition by repeated upper-right rectangular blocks.
    assert n>0 and n&(n-1)==0
    if n==1: return 1
    return 2*nuclear_upper_bound(n//2)+n//2

for l in range(1,5):
    for k in range(l+2,l+5):
        for m in (2**l,2**(l+1)-1):
            for n in (2**k,2**(k+1)-1):
                assert near_geometric(m,n,16)
for k in range(1,5):
    for l in range(k+2,k+5):
        for m in (2**l,2**(l+1)-1):
            for n in (2**k,2**(k+1)-1):
                assert far_geometric(m,n,16)
for h in range(9):
    n=1<<h
    assert nuclear_upper_bound(n)==n*(1+h/2)
print('CHECK_OK: rational geometric expansions and triangular nuclear recursion')
