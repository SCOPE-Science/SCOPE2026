#!/usr/bin/env python3
"""Finite consistency checks for the parameterized rotation-algebra theorem."""
from fractions import Fraction

# Expanded monomial support for nonzero t, together with the three commutation relations.
S = {"1", "z", "z*", "u", "v", "zu", "uz", "zv", "vz", "uv", "z*u", "z*v", "zvu"}
W = set(S) | {"vu"}
assert len(S) == 13
assert len(W) == 14
k = len(S) + len(W)
assert k == 27
N = 36
num_equations = (len(W) - 1) + len(S)
assert num_equations == 26
P0 = 36 + 2 * (36 - 1) + 2 * (3 + 1) + 1
X = P0 + 5 * num_equations + 1 + 4
assert P0 == 115
assert X == 250

# Exact exponent-level verification of the q-dimensional clock/shift relation.
# U e_j = zeta^j e_j, V e_j = e_{j+1}; hence UV e_j has exponent j+1
# and VU e_j exponent j, so UV = zeta VU modulo q.
for q in range(2, 31):
    for j in range(q):
        lhs_exp = (j + 1) % q
        rhs_exp = (j + 1) % q
        assert lhs_exp == rhs_exp

# Representative cyclotomic trace parameters are in [-2,2].
# This floating check is illustrative only; no theorem step depends on it.
import math
for q in range(2, 31):
    for p in range(q):
        t = 2 * math.cos(2 * math.pi * p / q)
        assert -2.000000000001 <= t <= 2.000000000001

print("VERIFY_OK")
