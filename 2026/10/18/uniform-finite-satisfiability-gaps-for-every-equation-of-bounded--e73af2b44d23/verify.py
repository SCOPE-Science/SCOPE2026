#!/usr/bin/env python3
"""Reproduce exact finite-chain checks accompanying the quantitative uniform-gap theorem."""
from itertools import product
from fractions import Fraction

def sub(a,b):
    return max(Fraction(0),a-b)

def evaluate_positive_implicativity(x,y):
    return sub(sub(x,y),y),sub(x,y)

def degree(n):
    assert n>=2
    grid=[Fraction(j,n-1) for j in range(n)]
    failures=[(x,y) for x,y in product(grid,repeat=2) if (lambda r: r[0]!=r[1])(evaluate_positive_implicativity(x,y))]
    return len(failures),Fraction(len(failures),n*n)

# The smallest violating chain is the three-point standard MV/BCK chain.
assert degree(2)[0]==0
assert degree(3)==(1,Fraction(1,9))
# There are five variable occurrences in the two sides of the example equation.
# Witness chain n0=3, k=2 -> theorem lower bound (16*2*5)^(-2).
eps=Fraction(1,(16*2*5)**2)
for n in range(2,51):
    fails,frac=degree(n)
    assert fails==0 or frac>=eps, (n,fails,eps)
    assert fails >=0
print('VERIFY_OK chains=49 smallest_witness=3 witness_failures=1 witness_probability=1/9 uniform_gap_lower_bound=',eps)
