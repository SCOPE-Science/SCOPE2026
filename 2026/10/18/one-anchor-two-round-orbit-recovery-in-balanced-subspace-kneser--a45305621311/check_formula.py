#!/usr/bin/env python3
"""Independent exact arithmetic verification for q-Kneser rooted common-neighbor counts.
Uses Gaussian lattice Möbius inversion rather than complement graph parametrization.
"""
from functools import lru_cache
from math import prod
@lru_cache(None)
def gaussian(n,r,q):
    if r < 0 or r > n: return 0
    if r==0 or r==n: return 1
    return gaussian(n-1,r,q)+q**(n-r)*gaussian(n-1,r-1,q)

def mobius_common_neighbours(k,q,s):
    # Inclusion-exclusion over nonzero subspaces of the projected second anchor.
    # Number of complements with a fixed j-dimensional intersection constraint.
    r=k-s
    return sum((-1)**j*q**(j*(j-1)//2+s*j+k*(k-j))*gaussian(r,j,q) for j in range(r+1))

def graph_count(k,q,s):
    r=k-s
    # Graph matrices whose quotient restriction on r coordinates is invertible.
    return q**(k*k-r*(r+1)//2)*prod(q**j-1 for j in range(1,r+1))

def size_orbit(k,q,s):
    return q**((k-s)**2)*gaussian(k,s,q)**2

checked=0
for q in [2,3,4,5,7]:
    for k in range(2,9):
        vals=[graph_count(k,q,s) for s in range(k+1)]
        for s in range(k+1):
            v=mobius_common_neighbours(k,q,s)
            assert v==vals[s],(q,k,s,v,vals[s])
            checked+=1
        assert all(vals[s]<vals[s+1] for s in range(k))
        assert sum(size_orbit(k,q,s) for s in range(k+1))==gaussian(2*k,k,q)
        assert vals[k]==q**(k*k)
        assert vals[0]==prod(q**k-q**j for j in range(k))
print(f'MOBIUS_INVERSION_TESTS_OK configurations={5*7} common_neighbor_cases={checked}; all orbit totals and monotonicity verified')
