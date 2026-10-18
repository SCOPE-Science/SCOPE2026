#!/usr/bin/env python3
"""Exact rational diagnostics for stated examples; not an infinite-dimensional proof."""
from fractions import Fraction as F

def diagonal_error_squared(n):
    # T=diag(1,-1,1/2,3/4), x=(1,2,3,4), so δ_*²=3²+4²=25.
    return (2 * (F(-1) ** n - 1))**2 + (3*(F(1,2)**n-1))**2 + (4*(F(3,4)**n-1))**2

assert diagonal_error_squared(2) == F(65,8)
assert F(24) < diagonal_error_squared(100) < F(25)
assert F(40) < diagonal_error_squared(101) < F(41)
# Forward shift S e_0=e_1 gives disjoint unit basis vectors for every n>=1.
assert F(1)+F(1) == F(2)
# B e_0=0, while weighted forward S_w e_0=(1/2)e_1 for n>=1.
assert F(1) == F(1)
assert F(1)+F(1,2)**2 == F(5,4)
# A on e_0 has weight-product squared 1/4, agreeing with δ_*²=5/4.
assert F(1)+F(1,4) == F(5,4)
print('All exact rational sample diagnostics passed (not an infinite-dimensional proof).')
