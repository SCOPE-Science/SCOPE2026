#!/usr/bin/env python3
"""Reproduce exact Gaussian tensor-train prefix-sharing variance identities.

Requires NumPy >= 1.24. No external files, network access, or random state
from an earlier computation are used. Monte Carlo supports, but does not prove,
the universal and asymptotic theorems.
"""
from fractions import Fraction
from math import exp
import numpy as np


def exact_variance(d: int, r: int, k: int, probes: int) -> Fraction:
    assert d >= 2 and r >= 1 and 0 <= k < d and probes >= 1
    base = Fraction(r + 2, r)
    return ((3 * base ** (d - 1) - 1)
            + (probes - 1) * (base ** k - 1)) / probes


def trace_rank_one_samples(d, r, k, probes, batches, rng):
    """Each physical dimension has at least one unit basis vector;
    contractions against that vector use one Gaussian slice per core.

    The first k slices are identically reused across all probes. The rest
    are independent among probes. This is exactly the rank-one target law.
    """
    vec = np.ones((batches, probes, 1), dtype=float)
    for j in range(d):
        left = 1 if j == 0 else r
        right = 1 if j == d - 1 else r
        if j < k:
            g = rng.normal(size=(batches, 1, left, right))
        else:
            g = rng.normal(size=(batches, probes, left, right))
        vec = np.einsum('bpi,bpij->bpj', vec, g, optimize=True)
    z = vec[:, :, 0] / (r ** ((d - 1) / 2))
    return z * z


def validation():
    assertions = 0
    # Rational checks: zero shared prefix recovers 1/L decay. Single probe
    # cannot depend on the shared-prefix length. Infinite-probe floor rises.
    for d in range(2, 9):
        for r in range(1, 8):
            base = Fraction(r + 2, r)
            for k in range(d):
                previous = Fraction(0)
                for probes in range(1, 19):
                    got = exact_variance(d, r, k, probes)
                    target = (3 * base ** (d - 1) - 1) / probes + (
                        Fraction(probes - 1, probes) * (base ** k - 1))
                    assert got == target
                    assertions += 1
                    if k == 0:
                        assert got * probes == 3 * base ** (d - 1) - 1
                        assertions += 1
                    if probes == 1:
                        assert got == 3 * base ** (d - 1) - 1
                        assertions += 1
                    if previous:
                        assert got < previous
                        assertions += 1
                    previous = got
    # For every finite r, any nonzero shared prefix gives a positive floor.
    for d in range(2, 11):
        for r in range(1, 21):
            for k in range(1, d):
                floor = Fraction(r + 2, r) ** k - 1
                assert floor > 0
                assert exact_variance(d, r, k, 10000) > floor
                assertions += 2
    # Critical fraction limit of exact worst-case variance.
    for alpha, theta in [(1.0, 1.0), (2.0, 0.5), (0.8, 0.25)]:
        target = exp(2 * theta / alpha) - 1
        for d in [400, 1600, 6400]:
            r = round(alpha * d)
            k = min(d - 1, round(theta * d))
            expected = float(exact_variance(d, r, k, d ** 2))
            assert abs(expected - target) < (0.09 if d == 400 else 0.04)
            assertions += 1
    rng = np.random.default_rng(1748831)
    # Covariance decomposition of the shared-core estimator, direct
    # TT-core contractions: E Z_1^2 Z_2^2 - 1 = ((r+2)/r)^k - 1.
    tests = [(3, 4, 0, 5), (3, 4, 1, 5), (3, 4, 2, 5), (4, 4, 2, 6)]
    for d, r, k, probes in tests:
        count = 200000
        first = second = cross = second_mean = 0.0
        for _ in range(count // 10000):
            ys = trace_rank_one_samples(d, r, k, probes, 10000, rng)
            avg = np.mean(ys, axis=1)
            first += float(np.sum(ys[:, 0]))
            second += float(np.sum(ys[:, 0] ** 2))
            cross += float(np.sum(ys[:, 0] * ys[:, 1]))
            second_mean += float(np.sum(avg ** 2))
        mean = first / count
        fourth = second / count
        e_cross = cross / count
        e_avg2 = second_mean / count
        exact_e4 = float(3 * Fraction(r + 2, r) ** (d - 1))
        exact_cross = float(Fraction(r + 2, r) ** k)
        exact_est_var = float(exact_variance(d, r, k, probes))
        # Bounded, deterministic Monte Carlo tolerances, not a theorem.
        assert abs(mean - 1) < 0.04, (d,r,k,mean)
        assert abs(fourth - exact_e4) < 0.14 * exact_e4, (d,r,k,fourth,exact_e4)
        assert abs(e_cross - exact_cross) < 0.14 * exact_cross, (d,r,k,e_cross,exact_cross)
        assert abs(e_avg2 - 1 - exact_est_var) < 0.14 * exact_est_var, (d,r,k,e_avg2,exact_est_var)
        assertions += 4
        print(f'd={d} r={r} k={k} L={probes}: '
              f'estimator variance {e_avg2 - mean ** 2:.5f}, '
              f'exact {exact_est_var:.5f}; '
              f'cross moment {e_cross:.5f}, exact {exact_cross:.5f}')
    # Nonseparable u in (R^2) tensor (R^2) gives strict worst-case bound.
    B = 250000
    n, r, probes = 2, 3, 5
    e2 = e12 = 0.0
    for _ in range(B // 10000):
        g1 = rng.normal(size=(10000, n, r))
        g2 = rng.normal(size=(10000, probes, r, n))
        u = np.eye(2) / 2 ** 0.5
        z = np.einsum('bir,blrs,is->bl', g1, g2, u, optimize=True) / r ** 0.5
        sq = z ** 2
        e2 += float(np.sum(np.mean(sq, axis=1) ** 2))
        e12 += float(np.sum(sq[:, 0] * sq[:, 1]))
    mean_square = e2 / B
    cross = e12 / B
    bound = float(exact_variance(2, r, 1, probes))
    assert mean_square - 1 < bound + 0.10
    assert cross - 1 < 2 / r + 0.08
    assertions += 2
    print(f'nonseparable target variance {mean_square - 1:.5f}; '
          f'sharp separable upper bound {bound:.5f}')
    print(f'PASS: {assertions} exact algebraic/asymptotic and supporting Monte Carlo checks')


if __name__ == '__main__':
    validation()
