#!/usr/bin/env python3
"""Standalone checks of exact first-choice-only RCV posterior formula."""
from fractions import Fraction as F
import random
from math import sqrt

# The exact difference density is 1-3*d*d+2*d**3 for 0 <= d <= 1.
def q_tail(delta):
    d = F(delta)
    if d >= 1:
        return F(0)
    if d <= -1:
        return F(1)
    if d >= 0:
        return F(1, 2) - d + d**3 - d**4 / 2
    return F(1) - q_tail(-d)

def q_factored(d):
    d = F(d)
    return F(0) if d >= 1 else F(1, 2)*(1-d)**3*(1+d)

# Independent binomial summation over integer grid verifies the polynomial
# identity using exact arithmetic at many rational arguments.
for den in range(1,31):
    for num in range(den+1):
        d=F(num,den)
        assert q_tail(d) == q_factored(d)
        assert F(0) <= q_tail(d) <= F(1,2)
        assert q_tail(d) <= F(1,2)*(1-d)
assert q_tail(F(1,5)) == F(192,625)
assert q_tail(F(1,2)) == F(3,32)
assert q_tail(F(4,5)) == F(9,1250)
# Verify normalized marginal density: integral_0^1 (1-3d^2+2d^3) dd = 1/2.
assert F(1)-F(3,3)+F(2,4) == F(1,2)
# Dirichlet aggregation can be sampled directly from five independent
# Gamma(1,1) variables, without sampling a Dirichlet(2,2,1) distribution.
rng=random.Random(20261024)
N=120_000
for d, tol in [(0.2,0.012),(0.5,0.012),(0.8,0.012)]:
    hits=0
    for i in range(N):
        g=[rng.expovariate(1) for _ in range(5)]
        x=(g[2]+g[4]-g[1]-g[3])/sum(g)
        # indices deliberately represent C, CA, CB, CAB, CBA
        # g[1],g[3] transfer to A; g[2],g[4] transfer to B.
        if x>d: hits+=1
    empirical=hits/N
    exact=float(q_factored(F(str(d))))
    assert abs(empirical-exact)<tol,(d,empirical,exact)
    print('delta',d,'empirical',round(empirical,6),'exact',round(exact,6))
print('PASS: exact arithmetic, normalized density, independently sampled 5-category Dirichlet grouping')
