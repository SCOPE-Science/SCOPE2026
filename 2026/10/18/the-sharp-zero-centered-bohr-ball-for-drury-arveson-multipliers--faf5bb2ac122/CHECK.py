"""Exact finite arithmetic diagnostics for the zero-centered Drury--Arveson Bohr theorem.

The proof is analytic. This script checks finitely many multinomial identities and
sampled consequences, not any claim of exhaustive verification.
"""
from fractions import Fraction as Q
from math import comb, sqrt

u2, v2 = Q(9, 25), Q(16, 25)
assert u2 + v2 == 1
count = 0
for degree in range(1, 41):
    s = sum(Q(comb(degree, k)) * u2**k * v2**(degree-k)
            for k in range(degree+1))
    assert s == 1
    count += 1
    # At the boundary radius a=1/sqrt(2), both the degree-n coefficient
    # majorant and the H^2_d norm-squared contribution equal 2^{-n}.
    degree_mass = sum(Q(comb(degree, k), 2**degree) * u2**k * v2**(degree-k)
                      for k in range(degree+1))
    assert degree_mass == Q(1, 2**degree)
    count += 1

r0 = 1/sqrt(2)
def lower(r):
    return r0*r/(1-r0*r)
def upper(r):
    return r/sqrt(1-r*r)
assert abs(lower(r0)-1) < 1e-13
assert abs(upper(r0)-1) < 1e-13
count += 2
for r in (.1, .25, .5, .65, .70, r0, .72, .80, .9):
    assert lower(r) <= upper(r) + 1e-12
    assert (lower(r) > 1) == (r > r0)
    count += 2
h = 1e-5
for bound in (lower, upper):
    slope = (bound(r0+h)-bound(r0-h))/(2*h)
    assert abs(slope-2*sqrt(2)) < 1e-7
    count += 1
print(f'PASS: {count} exact and finite numeric diagnostic assertions')
