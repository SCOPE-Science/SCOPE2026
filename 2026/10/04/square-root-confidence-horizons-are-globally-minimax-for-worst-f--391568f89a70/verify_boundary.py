#!/usr/bin/env python3
"""Deterministic sanity checks for the square-root boundary minimax algebra.

This script does not certify Brownian crossing probabilities.  It only checks the
pointwise envelope and relative-width identities used in the analytic proof.
"""
import math

def ratio(g, s, z=1.0):
    return g(s)/(z*math.sqrt(s))

def check_shape(g, grid):
    K=max(ratio(g,s) for s in grid)
    for s in grid:
        assert g(s) <= K*math.sqrt(s) + 1e-12
    return K

D=9.0
grid=[1.0 + (D-1.0)*i/4000 for i in range(4001)]

# Square-root shape has constant relative width.
c=2.7
gstar=lambda s: c*math.sqrt(s)
K=check_shape(gstar,grid)
assert abs(K-c) < 1e-12
assert max(abs(ratio(gstar,s)-c) for s in grid) < 1e-12

# Representative power boundaries have endpoint-driven worst relative width.
for q in (-0.5,0.0,0.5,1.0,1.5):
    cq=1.9
    g=lambda s,q=q: cq*s**(1.0-q)
    K=check_shape(g,grid)
    expected=cq*max(1.0,D**(0.5-q))
    assert abs(K-expected) < 2e-6

# A non-power oscillating boundary is still dominated by its square-root envelope.
g=lambda s: math.sqrt(s)*(1.4 + 0.2*math.sin(math.log(s)*3.0))
K=check_shape(g,grid)
assert K <= 1.6000001
print('VERIFY_OK')
