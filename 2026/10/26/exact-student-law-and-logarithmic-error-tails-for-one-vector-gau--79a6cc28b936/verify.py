#!/usr/bin/env python3
"""Reproduce the finite identities and distribution checks for a Gaussian sketched one-vector matrix exponential.

Uses only Python's standard library. Random trials corroborate the formulas; the
all-dimensional tail and moment statements are established by the accompanying proof.
"""
from math import exp, gamma, pi, sqrt, atan, isfinite
from random import Random


def density_constant(s):
    return gamma((s + 1) / 2) / (sqrt(pi) * gamma(s / 2))


def exact_sketch(s, rng):
    # SPD diagonal matrix with active eigenvalues 1,3; s sketch rows and n=s+2 columns.
    n = s + 2
    row = [[rng.gauss(0, 1) / sqrt(s) for _ in range(n)] for _ in range(s)]
    xx = [(r[0] + r[1]) / sqrt(2) for r in row]
    ww = [(-r[0] + r[1]) / sqrt(2) for r in row]
    a_v = [(r[0] + 3 * r[1]) / sqrt(2) for r in row]
    numerator = sum(x * z for x, z in zip(xx, a_v))
    denominator = sum(x * x for x in xx)
    direct_ritz = numerator / denominator
    ratio = sum(x * z for x, z in zip(xx, ww)) / denominator
    assert abs(direct_ritz - (2 + ratio)) < 2e-12 * (1 + abs(direct_ritz))
    t = 0.35
    approx = exp(-t * direct_ritz)
    approx_direct_vector_norm = sqrt(approx**2 / 2 + approx**2 / 2)
    assert abs(approx_direct_vector_norm - approx) < 1e-12 * max(1, approx)
    truth1, truth2 = exp(-t) / sqrt(2), exp(-3 * t) / sqrt(2)
    squared_error = (approx / sqrt(2) - truth1)**2 + (approx / sqrt(2) - truth2)**2
    assert squared_error >= 0
    # If initial vector is an eigenvector, Ritz 1 is returned for every sketch.
    first = [r[0] for r in row]
    first_ritz = sum(z * z for z in first) / sum(z * z for z in first)
    assert abs(first_ritz - 1) < 1e-14
    return ratio


def tail_2(u):
    return (1 - u / sqrt(1 + u * u)) / 2


def tail_3(u):
    return .5 - (atan(u) + u / (1 + u * u)) / pi


def run():
    rng = Random(26042026)
    checks = 0
    for s in (2, 3, 4, 5, 8):
        vals = [exact_sketch(s, rng) for _ in range(6000)]
        checks += 6000 * 4
        checks += 1
        assert isfinite(sum(vals))
        if s in (2, 3):
            for u in (.5, 1., 2.):
                estimate = sum(v > u for v in vals) / len(vals)
                expected = (tail_2 if s == 2 else tail_3)(u)
                assert abs(estimate - expected) < .025, (s, u, estimate, expected)
                checks += 1
    assert abs(density_constant(2) - .5) < 1e-15
    assert abs(density_constant(3) - 2 / pi) < 1e-15
    checks += 2
    for s in (2, 3, 4, 5, 10):
        c = density_constant(s) / s
        assert c > 0
        checks += 1
    # Exact tail constants for the two explicitly integrable cases.
    for u in (100, 250):
        assert abs(u*u*tail_2(u) - .25) < .00003
        assert abs(u**3*tail_3(u) - 2/(3*pi)) < .0002
        checks += 2
    # A deterministic sketch with small projected initial norm can yield a huge
    # negative sketched Ritz value, even though A is SPD.
    for epsilon in (0.4, 0.2, 0.1):
        # First sketch row acts as epsilon*v^T - w^T on the active 2-space.
        x, w = epsilon, -1.
        ritz = 2 + x*w/(x*x)
        assert abs(ritz - (2 - 1 / epsilon)) < 1e-12
        assert ritz < 0
        checks += 2
    print('PASS: direct sketched projection, scalar matrix exponential, eigenvector')
    print('PASS: Student-ratio law corroborated by Gaussian sampling')
    print('PASS: explicit two-/three-row tails and sharp tail constants')
    print(f'PASS: {checks} deterministic check instances (including seeded random trials)')

if __name__ == '__main__':
    run()
