#!/usr/bin/env python3
"""Finite checks for union-generated team families and phase-distribution weights.

This script tests small finite cases. It is not a proof of the asymptotic result.
"""
import math
from itertools import combinations


def family(generators):
    f = {0}
    for g in generators:
        f = f | {x | g for x in f}
    return frozenset(f)


def profile_by_enumeration(n):
    choices = [(1 << i) for i in range(n)]
    choices += [(1 << i) | (1 << j) for i, j in combinations(range(n), 2)]
    seen = set()
    profile = [0] * (n + 1)
    for mask in range(1 << len(choices)):
        gens = [choices[k] for k in range(len(choices)) if (mask >> k) & 1]
        f = family(gens)
        if f not in seen:
            seen.add(f)
            profile[sum((1 << i) in f for i in range(n))] += 1
    return profile


def theoretical_profile(n):
    return [math.comb(n, s) * 2 ** (math.comb(n, 2) - math.comb(s, 2))
            for s in range(n + 1)]


def root(n):
    lo, hi = 0.0, math.log2(n) + 1
    for _ in range(80):
        q = (lo + hi) / 2
        if math.log(q + 1) + q * math.log(2) < math.log(n):
            lo = q
        else:
            hi = q
    return (lo + hi) / 2


def phase_accuracy(n):
    q = root(n)
    m = math.floor(q)
    theta = q - m
    js = range(-m, n - m + 1)
    logs = [math.lgamma(n + 1) - math.lgamma(m + j + 1)
            - math.lgamma(n - m - j + 1)
            - (m + j) * (m + j - 1) * math.log(2) / 2 for j in js]
    mx = max(logs)
    unnormalized = [math.exp(v - mx) for v in logs]
    z = sum(unnormalized)
    exact = dict(zip(js, (x / z for x in unnormalized)))
    f = lambda j: j * theta - j * (j - 1) / 2
    candidates = range(-80, 81)
    tilts = [f(j) * math.log(2) for j in candidates]
    mx = max(tilts)
    weights = [math.exp(t - mx) for t in tilts]
    z = sum(weights)
    base = {j: v / z for j, v in zip(candidates, weights)}
    mu = sum(f(j) * p for j, p in base.items())
    corrected = {j: p * (1 + (f(j) - mu) / (m + 1))
                 for j, p in base.items()}
    support = set(exact) | set(base)
    zero_err = sum(abs(exact.get(j, 0) - base.get(j, 0)) for j in support)
    one_err = sum(abs(exact.get(j, 0) - corrected.get(j, 0)) for j in support)
    return m, theta, zero_err, one_err


if __name__ == '__main__':
    for n in range(5):
        got = profile_by_enumeration(n)
        expected = theoretical_profile(n)
        assert got == expected, (n, got, expected)
        print('ENUM', n, expected)
    for n in (32, 128, 512, 2048, 10000, 100000):
        m, theta, leading_error, corrected_error = phase_accuracy(n)
        assert corrected_error < leading_error
        print('PHASE', n, m, f'{theta:.9f}',
              f'{leading_error:.9f}', f'{corrected_error:.9f}')
    print('VERIFY_OK')
