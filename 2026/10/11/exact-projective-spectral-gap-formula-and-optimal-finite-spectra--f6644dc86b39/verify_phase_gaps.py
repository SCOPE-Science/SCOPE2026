#!/usr/bin/env python3
"""Finite numerical cross-checks for the projective spectral-gap formula."""
import math
import random

PI = math.pi

def gaps(phases):
    p = sorted(a % PI for a in phases)
    assert p
    assert all(p[j + 1] - p[j] > 1e-10 for j in range(len(p) - 1))
    return [p[j + 1] - p[j] for j in range(len(p) - 1)] + [PI + p[0] - p[-1]]

def exact_square(phases):
    return 1.0 - math.fsum(g - math.sin(g) for g in gaps(phases)) / (2 * PI)

def quadrature_square(phases, steps=65536):
    acc = 0.0
    for j in range(steps):
        t = PI * (j + 0.5) / steps
        v = max(abs(math.cos(t - a)) for a in phases)
        acc += v * v
    return acc / steps

def run():
    rng = random.Random(20261004)
    for n in [1, 2, 3, 4, 7, 13]:
        phases = [j * PI / n for j in range(n)]
        expected = 0.5 + n * math.sin(PI / n) / (2 * PI)
        assert abs(exact_square(phases) - expected) < 2e-14
        assert abs(quadrature_square(phases) - expected) < 1.1e-8
    for n in [2, 3, 5, 9]:
        for _ in range(3):
            phases = sorted(rng.uniform(0, PI) for j in range(n))
            exact = exact_square(phases)
            numerical = quadrature_square(phases)
            bound = 0.5 + n * math.sin(PI / n) / (2 * PI)
            assert 0.5 - 1e-14 <= exact < bound + 1e-13 <= 1.0 + 1e-12
            assert abs(exact - numerical) < 1.1e-8, (n, exact, numerical)
    print('UNITARY_PROJECTIVE_SPECTRAL_GAP_OK')

if __name__ == '__main__':
    run()
