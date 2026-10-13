#!/usr/bin/env python3
import math
import random


def rhs(N, R):
    return 2.0*N*(R-1.0)**2/(R*(2.0*N-R))


def lhs_reduced(N, R):
    return 1.0/R + (2.0*N-1.0)**2/(2.0*N-R) - 2.0*N

for N in range(1, 9):
    for j in range(1, 100):
        R = 1.0 + (2.0*N-1.0)*j/101.0
        assert abs(lhs_reduced(N, R)-rhs(N, R)) < 1e-10

rng = random.Random(20261006)
for N in range(1, 8):
    d = 2*N
    for _ in range(500):
        raw = [rng.expovariate(1.0) for _ in range(d)]
        scale = d/sum(raw)
        x = [v*scale for v in raw]
        R = max(x)
        # The average is one, so R >= 1 and positivity gives R < d.
        assert R >= 1.0 - 1e-12
        assert R < d + 1e-12
        recip = sum(1.0/v for v in x)
        bound = 1.0/R + (d-1.0)**2/(d-R)
        assert recip + 1e-9*max(1.0, abs(recip), abs(bound)) >= bound

# Check the extensive asymptotic coefficient numerically.
nu = 1.3
A = 0.5*math.log((2*nu+1)/(2*nu-1))
for rho in (0.2, 0.7, 1.3, 1.8):
    target = 2*rho*nu*A/(2-rho)
    vals=[]
    for N in (1000, 3000, 10000):
        R=rho*N
        vals.append(2*N*nu*A*(R-1)**2/(R*(2*N-R))/N)
    assert abs(vals[-1]-target) < 2e-3

print('VERIFY_OK')
