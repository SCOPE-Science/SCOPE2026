#!/usr/bin/env python3
"""Finite rational checks for a model ell-one column norm identity."""
from fractions import Fraction as Q

def one_column(n):
    # Column u/2+b_n/2; exact geometric tail after N entries.
    N=n+5
    values=[Q(1,2**(j+1)) for j in range(1,N+1)]
    values[n]+=Q(1,4)
    values[n+1]-=Q(1,4)
    infinite_tail=Q(1,2**(N+1))
    return sum(map(abs,values))+infinite_tail

for n in range(1,61):
    assert one_column(n)==Q(1)-Q(1,2**(n+2)),n
assert sum(Q(1,2**j) for j in range(1,101))==Q(1)-Q(1,2**100)
print("C0_SECOND_ADJOINT_EXACT_COLUMN_CHECK_OK")
