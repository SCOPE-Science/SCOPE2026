#!/usr/bin/env python3
"""Exact identities and independent random-sample checks for Gini/order-statistic correlation."""
from fractions import Fraction as F
from math import sqrt, log1p
from random import Random


def harmonic_diff(n, k, power=1):
    return sum((F(1, r ** power) for r in range(n - k + 1, n + 1)), F(0))


def closed(n, k):
    assert 2 <= n and 1 <= k <= n
    b = n * harmonic_diff(n, k) - k
    v = harmonic_diff(n, k, 2)
    vg = F(2 * (2 * n - 1), 3 * n * (n - 1))
    cov = F(2, n * (n - 1)) * b
    return cov, v, vg


def rank_cov(n, i, j):
    return harmonic_diff(n, min(i, j), 2)


def independent_matrix_check(n):
    # Evaluate a pairwise-rank expansion instead of the spacing formula.
    weights = {i: F(2 * (2 * i - n - 1), n * (n - 1)) for i in range(1, n + 1)}
    vg_matrix = sum((weights[i] * weights[j] * rank_cov(n, i, j)
                     for i in range(1, n + 1) for j in range(1, n + 1)), F(0))
    for k in range(1, n + 1):
        cov = sum((weights[i] * rank_cov(n, i, k) for i in range(1, n + 1)), F(0))
        c, v, vg = closed(n, k)
        assert cov == c and vg_matrix == vg and v == rank_cov(n, k, k)
    return n


def direct_sample_stats(xs, k):
    xs = sorted(xs)
    n = len(xs)
    gd = sum(abs(xs[i] - xs[j]) for i in range(n) for j in range(i + 1, n))
    gd *= 2 / (n * (n - 1))
    by_spacings = 0.0
    for j in range(2, n + 1):
        by_spacings += 2 * (j - 1) * (n - j + 1) * (xs[j - 1] - xs[j - 2]) / (n * (n - 1))
    assert abs(gd - by_spacings) < 1e-10 * (1 + abs(gd))
    return xs[k - 1], gd


def simulate(n, k, reps, seed):
    rng = Random(seed)
    sx = sg = sxx = sgg = sxg = 0.0
    for _ in range(reps):
        x, g = direct_sample_stats([rng.expovariate(1) for __ in range(n)], k)
        sx += x; sg += g; sxx += x * x; sgg += g * g; sxg += x * g
    vx = (sxx - sx * sx / reps) / reps
    vg = (sgg - sg * sg / reps) / reps
    cov = (sxg - sx * sg / reps) / reps
    obs = cov / sqrt(vx * vg)
    c, v, gvar = closed(n, k)
    theory = float(c) / sqrt(float(v * gvar))
    assert abs(obs - theory) < 0.025, (n, k, obs, theory)
    return n, k, round(obs, 5), round(theory, 5)


def r(n, k):
    c, v, g = closed(n, k)
    return float(c) / sqrt(float(v * g))


def main():
    total = 0
    for n in range(2, 46):
        independent_matrix_check(n)
        total += n
    print('Exact rank-matrix covariance and variance identities:', total)
    # Repeated nontrivial ranks: empirical input data, not synthesized using spacings.
    for n, k in ((4, 3), (8, 7), (25, 23), (80, 75)):
        print('Simulation (n, rank, empirical correlation, exact):', simulate(n, k, 18000, 1729+n))
    for n in (30, 50, 100, 300, 1000):
        k_star = max(range(1, n + 1), key=lambda k: r(n, k))
        print('Maximizing rank:', n, k_star, 'share:', round(k_star/n, 8), 'correlation:', round(r(n, k_star), 8))
    lo, hi = 0.8, 0.99
    for _ in range(70):
        p = (lo + hi) / 2
        if -log1p(-p) - p - 2*p*p < 0:
            lo = p
        else:
            hi = p
    p = (lo + hi) / 2
    c = 2*sqrt(3)*p**1.5*sqrt(1-p)
    assert 0.93005641444 < p < 0.93005641446
    assert 0.82172879836 < c < 0.82172879838
    print('Continuum optimal fraction:', p)
    print('Continuum maximal correlation:', c)
    print('PASS: exact arithmetic, independent matrix method, Monte Carlo, asymptotic numerics')


if __name__ == '__main__':
    main()
