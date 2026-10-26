#!/usr/bin/env python3
"""Independent numeric sanity checks for a Dirichlet kernel zero threshold.

Diagnostic samples only: the general classification is established analytically.
"""
import cmath
import math

Q_STAR = 1.0 - math.log(2.0)
TAU_STAR = Q_STAR / (1.0 - 2.0 * Q_STAR)

def kernel(m, q, t):
    return 1.0 - cmath.log(1.0 - t) - q * t**m

def negative_root(q):
    assert Q_STAR < q < 0.5
    lo, hi = 0.0, 1.0
    for _ in range(90):
        mid = (lo + hi) / 2
        if (1.0 - math.log1p(mid) - q * mid * mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

assert abs(Q_STAR - 0.3068528194400547) < 2e-15
assert abs(TAU_STAR - 0.7943497247810449) < 2e-15
assert (911.0/243.0) > (2.0 + math.sqrt(3.0))
for m in (1, 3, 4, 5, 8):
    q = 1.0 / m
    samples = [cmath.exp(1j * (2*math.pi*(k+0.5)/20000)) for k in range(20000)]
    minimum = min(kernel(m, q, z).real for z in samples)
    print(f'order={m} sampled boundary minimum real part={minimum:.12f}')
    assert minimum > 0.0
for q in (0.32, 0.40, 0.49):
    r = negative_root(q)
    assert abs(kernel(2, q, -r)) < 2e-13
    print(f'quadratic perturbation q={q:.2f}, unique negative zero t={-r:.14f}')
print('q_star=', Q_STAR)
print('tau_star=', TAU_STAR)
print('All diagnostics passed. Analytic argument is required for global conclusions.')
