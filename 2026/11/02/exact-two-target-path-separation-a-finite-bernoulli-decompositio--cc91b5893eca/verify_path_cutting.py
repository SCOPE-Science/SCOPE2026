#!/usr/bin/env python3
"""Exact finite checks of the two-target path-separation identity.
The asymptotic theorems are mathematical statements, not consequences of finite tests.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import factorial, log


def convolution(p, q):
    result = defaultdict(F)
    for i, x in p.items():
        for j, y in q.items():
            result[i + j] += x * y
    return dict(result)


def bernoulli_sum(low, high):
    """Generating polynomial for independent successes with probabilities 1/(k+1)."""
    out = {0: F(1)}
    for k in range(low, high + 1):
        out = convolution(out, {0: F(k, k + 1), 1: F(1, k + 1)})
    return out


def proposed(a, b):
    n = a + b + 1
    left = bernoulli_sum(a + 1, n - 1)
    right = bernoulli_sum(b + 1, n - 1)
    out = defaultdict(F)
    for j, p in left.items():
        out[j + 1] += p
    for j, p in right.items():
        out[j + 1] += p
    out[1] -= 1
    return dict(out), left, right


@lru_cache(None)
def independent_markov(ell, rr, still_left, still_right):
    """Solve all transitions by conditioning on a uniformly chosen vertex.

    The state stores surviving arm sizes and whether the *original* endpoint
    remains attached. This recurrence never uses the proposed pgf.
    """
    if not (still_left or still_right):
        return {0: F(1)}
    n = ell + rr + 1
    out = defaultdict(F)
    out[1] += F(1, n)  # source removed
    for j in range(1, ell + 1):
        for k, p in independent_markov(j - 1, rr, False, still_right).items():
            out[k + 1] += p / n
    for j in range(1, rr + 1):
        for k, p in independent_markov(ell, j - 1, still_left, False).items():
            out[k + 1] += p / n
    return dict(out)


def check():
    assertions = 0
    pairs = 0
    for n in range(3, 13):
        for a in range(1, n - 1):
            b = n - 1 - a
            law, A, B = proposed(a, b)
            independent = independent_markov(a, b, True, True)
            for k in set(law) | set(independent):
                assert law.get(k, 0) == independent.get(k, 0), (a, b, k)
                assertions += 1
            assert sum(law.values()) == 1
            assertions += 1
            assert law[1] == F(1, n)
            assertions += 1
            assert sum(k * v for k, v in law.items()) == F(1) + sum(F(1, k + 1) for k in range(a + 1, n)) + sum(F(1, k + 1) for k in range(b + 1, n))
            assertions += 1
            # TV between S-1 and the Bernoulli sum associated with the other arm.
            tvA = sum(abs(law.get(j + 1, 0) - A.get(j, 0)) for j in set(A) | {k - 1 for k in law}) / 2
            tvB = sum(abs(law.get(j + 1, 0) - B.get(j, 0)) for j in set(B) | {k - 1 for k in law}) / 2
            assert tvA == F(a, n), (a, b, tvA)
            assert tvB == F(b, n), (a, b, tvB)
            assertions += 2
            for j in range(1, max(a, b) + 1):
                assert law.get(j + 1, F(0)) == A.get(j, F(0)) + B.get(j, F(0))
                assertions += 1
            pairs += 1
    # Local sanity probes for the continuous interior and endpoint limits.
    for a, b in [(100, 100), (100, 300), (2, 500), (1, 1000)]:
        n = a + b + 1
        A = bernoulli_sum(a + 1, n - 1)
        B = bernoulli_sum(b + 1, n - 1)
        # Exact finite formulas and a numerical comparison only, not a limit proof.
        mean_from_product = float(sum(j * p for j, p in A.items()) + sum(j * p for j, p in B.items())) + 1
        mean_from_harmonics = 1 + sum(1 / (k + 1) for k in range(a + 1, n)) + sum(1 / (k + 1) for k in range(b + 1, n))
        assert abs(mean_from_product - mean_from_harmonics) < 1e-11
        assertions += 1
    print(f'PASS: {pairs} exact finite path instances; {assertions} assertions; independent Markov recursion; exact TV identities; finite moment checks.')


if __name__ == '__main__':
    check()
