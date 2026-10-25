#!/usr/bin/env python3
"""Independent finite numerical checks of sharp two-direction cosine brightness."""
import math
import random

PS = [0.02, 0.13, 0.3, 0.6, 0.85, 1.0, 1.2, 1.51, 1.8, 1.97, 1.999]
N = 4096
TOL = 4e-5
random.seed(139810)
checks = 0
for p in PS:
    c = math.gamma((p + 1) / 2) / (math.sqrt(math.pi) * math.gamma(1 + p / 2))
    lower = (c - .5) / 2
    assert c > .5 and lower > 0
    hi = 2 ** (-p / 2)
    assert hi - c <= c - .5 + 1e-14, (p, c, hi)
    vals = [0.5 * (abs(math.cos(math.pi*j/N))**p + abs(math.sin(math.pi*j/N))**p)
            for j in range(N)]
    assert abs(min(vals)-.5)<1e-12
    assert abs(max(vals)-hi)<1e-12
    q = .5 * max(abs(min(vals)-c),abs(max(vals)-c))
    assert abs(q-lower)<1e-12
    # Midpoint of each angular cell: convergent numerical quadrature only.
    avg = sum(abs(math.cos(math.pi*(j+.5)/N))**p for j in range(N))/N
    assert abs(avg-c) < TOL,(p,avg,c)
    checks += 4
    for _ in range(200):
        w = random.random()
        phi = math.pi*random.random()
        s = abs(math.sin(phi))
        candidate_lower = .5*(c-min(w,1-w)*s**p)
        assert candidate_lower >= lower - 1e-12
        if candidate_lower <= lower+.01:
            eps = candidate_lower-lower
            assert abs(w-.5) <= 2*eps+1e-12
            assert abs(math.cos(phi)) <= math.sqrt(max(0,1-(1-4*eps)**(2/p)))+1e-10
        checks += 1
print('SUBQUADRATIC_TWO_VIEW_OK exponents=',len(PS),'finite_checks=',checks)
