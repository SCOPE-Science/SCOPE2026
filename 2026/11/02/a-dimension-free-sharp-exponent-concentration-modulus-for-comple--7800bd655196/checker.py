#!/usr/bin/env python3
"""Reproducible finite stress tests for the explicit quadratic concentration law.

No numerical sampling is used to justify the infinite-dimensional theorem.
Only Python's standard library is required.
"""
import cmath
import math
import random

checks = 0
K = math.e ** 4 + 2 * math.e ** 2 + 0.5
assert 69 < K < 70
checks += 1
C = 8 * math.sqrt(K)
assert 66 < C < 67
checks += 1

# The optimum of cos(theta)+2*b*sin(theta) is sqrt(1+4*b*b).
# The chosen trigonometric phase gives an exact boundary extremizer.
for b in [1 / 1024, 1 / 256, 1 / 64, 1 / 16, 1 / 4, 1 / 2, 1, 2]:
    norm = math.sqrt(1 + 4 * b * b)
    theta = math.atan(2 * b)
    z1, z2 = cmath.exp(1j * theta), cmath.exp(-1j * theta)
    principal = 0.5 * z1 * (z1 + z2)
    mixed = b * (z1 - z2)
    z3 = cmath.exp(1j * (cmath.phase(principal) - cmath.phase(mixed)))
    assert math.isclose(abs(principal + mixed * z3), norm, rel_tol=2e-13)
    checks += 1
    restricted = 1 / norm
    deficit = 1 - restricted
    tail = 2 * b / norm
    assert math.isclose(tail ** 2 / deficit, 1 + restricted, rel_tol=1e-9)
    checks += 1
    assert tail <= C * math.sqrt(deficit) + deficit
    checks += 1
    for j in range(257):
        th = math.pi * j / 512
        assert math.cos(th) + 2*b*math.sin(th) <= norm + 1e-12
        checks += 1

# Real-sign selection gives a dimension-independent domination inequality.
rng = random.Random(2068)
for _ in range(2048):
    n = rng.randint(1, 24)
    cs = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(n)]
    signed_max_lower = max(sum(abs(z.real) for z in cs), sum(abs(z.imag) for z in cs))
    assert sum(abs(z) for z in cs) <= 2 * signed_max_lower + 1e-12
    checks += 1

print(f"PASS: {checks} finite checks; K={K:.12f}, coefficient={C:.12f}")
