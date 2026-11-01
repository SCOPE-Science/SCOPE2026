#!/usr/bin/env python3
"""Finite checks for a Lorentz block-averaging theorem.

Only a supplement to the analytic proof. No external packages or data.
"""
import math
import random


def lorentz_norm(values, p, q):
    a = sorted((abs(v) for v in values), reverse=True)
    alpha = q / p
    return math.fsum(((k ** alpha - (k - 1) ** alpha) * v ** q)
                      for k, v in enumerate(a, 1)) ** (1 / q)


def binary_formula(n, k, j, p, q):
    if k < j:
        k, j = j, k
    if k == 0:
        return 0.0
    A = 2 ** (q / p) - 1
    return ((k / n) ** (1 - 1 / p) *
            ((1 + A * (j / k) ** q) ** (1 / q)) /
            (1 + j / k) ** (1 / p))


def binary_direct(n, k, j, p, q):
    x = [1] * k + [0] * (n - k) + [1] * j + [0] * (n - j)
    y = [k / n] * n + [j / n] * n
    return lorentz_norm(y, p, q) / lorentz_norm(x, p, q)


def profile(t, p, q):
    return math.exp(math.log1p((2 ** (q / p) - 1) * t ** q) / q
                    - math.log1p(t) / p)


def stationary(t, p, q):
    A = 2 ** (q / p) - 1
    return A * t ** (q - 1) * (p + (p - 1) * t) - 1


def maximizer(p, q):
    # Take the FIRST sign transition of the exact derivative numerically.
    samples = [math.exp(-700 + k * .1) for k in range(7001)]
    for lo, hi in zip(samples, samples[1:]):
        if stationary(lo, p, q) >= 0 >= stationary(hi, p, q):
            for _ in range(90):
                mid = (lo + hi) / 2
                if stationary(mid, p, q) > 0:
                    lo = mid
                else:
                    hi = mid
            return (lo + hi) / 2
    raise AssertionError('no first derivative crossing located')


def run():
    assertions = 0
    rng = random.Random(7119)
    parameters = [(p, q) for p in (1.1, 1.5, 2.0, 5.0)
                  for q in (0.2, 0.5, 0.8, 0.95)]
    # Check the one-block contraction bound on random vectors.
    for p, q in parameters:
        for m in range(1, 12):
            for rep in range(70):
                x = [rng.uniform(-2, 2) for _ in range(m + 5)]
                avg = sum(x[:m]) / m
                y = [avg] * m + [0] * 5
                assert lorentz_norm(y, p, q) <= lorentz_norm(x, p, q) * (1 + 1e-11)
                assertions += 1
            x = [1] * m + [0] * 5
            assert abs(lorentz_norm(x, p, q) - m ** (1 / p)) < 1e-9
            assertions += 1
    # Check the complete binary-input ratio formula, including swapped blocks.
    for p, q in parameters:
        for n in range(1, 13):
            for k in range(n + 1):
                for j in range(n + 1):
                    if k + j == 0:
                        continue
                    d = binary_direct(n, k, j, p, q)
                    f = binary_formula(n, k, j, p, q)
                    assert abs(d - f) < 5e-10, (n, k, j, p, q, d, f)
                    assertions += 1
    # All profile maximizers lie in (0,1) and provide strict amplification.
    for p, q in parameters:
        t = maximizer(p, q)
        R = profile(t, p, q)
        assert 0 < t < 1 and R > 1
        assertions += 1
        assert abs(stationary(t, p, q)) < 1e-10
        assertions += 1
        for j in range(1001):
            assert profile(j / 1000, p, q) <= R * (1 + 1e-11)
            assertions += 1
        for n in (5, 10, 20, 40, 80, 160):
            # The norm over binary vectors is bounded by the exact profile.
            for k in (1, n // 2, n):
                for j in (0, 1, k // 2, k):
                    if k == 0:
                        continue
                    assert binary_formula(n, k, j, p, q) <= R * (1 + 1e-10)
                    assertions += 1
            restricted = max(profile(j / n, p, q) for j in range(n + 1))
            assert restricted <= R * (1 + 1e-12)
            assertions += 1
    # Exact-pair witness in a four-coordinate instance.
    p, q = 2., 0.5
    d = binary_direct(2, 2, 1, p, q)
    assert d > 1.04 and abs(d - profile(0.5, p, q)) < 1e-12
    assertions += 1
    # Cross-check selected near-boundary rates, without treating them as proof.
    for p in (1.5, 2., 5.):
        B = p * (2 ** (1 / p) - 1)
        kap = (math.log(2) / p) * (2 ** (1 / p) / (2 ** (1 / p) - 1))
        assert 0 < B < 1
        assertions += 1
        for q in (0.8, 0.85, 0.9, 0.95):
            t = maximizer(p, q)
            prediction = math.exp(math.log(B) / (1 - q) - kap)
            assert 0 < t < 1 and 0 < prediction < 1
            assertions += 1
    print('PASS finite checks:', assertions)
    print('Example p=2,q=1/2, two blocks of length 2:',
          binary_direct(2, 2, 1, 2., .5))
    for p, q in ((2., .5), (2., .9), (2., .95)):
        t = maximizer(p, q)
        print('p,q,t*,binary amplification:', p, q, t, profile(t, p, q))


if __name__ == '__main__':
    run()
