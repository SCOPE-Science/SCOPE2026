"""Finite exact checks for a binary-factor tensor sketch and occupancy spectrum.

Uses Python standard library only. These tests do not replace asymptotic proofs.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, log1p
from random import Random


def hadamard(d):
    n = 1 << d
    return [[1 if ((u & s).bit_count() % 2 == 0) else -1
             for s in range(n)] for u in range(n)]


def kronecker_column(factors):
    w = [1]
    for a, b in factors:
        w = [z * v for z in w for v in (a, b)]
    return w


def stirling2(m, n):
    a = [0] * (n + 1)
    a[0] = 1
    for _ in range(m):
        b = [0] * (n + 1)
        for j in range(1, n + 1):
            b[j] = j * a[j] + a[j - 1]
        a = b
    return a[n]


def coverage_probability(n, m):
    return Fraction(factorial(n) * stirling2(m, n), n ** m)


def inclusion_exclusion(n, m):
    return sum(((-1) ** j * Fraction(comb(n, j) * (n-j) ** m, n ** m)
                for j in range(n + 1)), Fraction(0))


def check():
    checks = 0
    rng = Random(3141592653)
    for d in range(1, 6):
        n = 1 << d
        h = hadamard(d)
        for a in range(n):
            for b in range(n):
                assert sum(h[u][a] * h[u][b] for u in range(n)) == n * (a == b)
                checks += 1
        for _ in range(9):
            m = rng.randrange(1, n + 11)
            categories = []
            vectors = []
            for _ in range(m):
                factors = [(rng.choice((-1, 1)), rng.choice((-1, 1)))
                           for _ in range(d)]
                w = kronecker_column(factors)
                matches = [j for j in range(n)
                           if all(w[i] == h[i][j] for i in range(n)) or
                           all(w[i] == -h[i][j] for i in range(n))]
                assert len(matches) == 1
                categories.append(matches[0])
                vectors.append(w)
                checks += 1
            counts = Counter(categories)
            # The (unscaled) Gram matrix has the Walsh vectors as exact eigenvectors.
            gram = [[sum(w[u] * w[v] for w in vectors) for v in range(n)]
                    for u in range(n)]
            for s in range(n):
                eigenvalue_times_m = n * counts[s]
                for u in range(n):
                    assert sum(gram[u][v] * h[v][s] for v in range(n)) == eigenvalue_times_m * h[u][s]
                    checks += 1
            assert len(counts) == sum(counts[s] > 0 for s in range(n))
    for n in range(2, 8):
        for m in range(1, n + 9):
            p = coverage_probability(n, m)
            assert p == inclusion_exclusion(n, m)
            assert p == 0 if m < n else p > 0
            checks += 1
    for n, m in [(2, 6), (3, 7), (4, 6)]:
        totals = n ** m
        successes = sum(len(set(tup)) == n for tup in product(range(n), repeat=m))
        assert Fraction(successes, totals) == coverage_probability(n, m)
        checks += 1
    for eps in (0.1, 0.25, 0.5, 0.8):
        upper = (1 + eps) * log1p(eps) - eps
        lower = eps + (1 - eps) * log1p(-eps)
        assert 0 < upper < lower
        checks += 1
    print(f"PASS: {checks} exact/finite checks; no asymptotic certification claimed")


if __name__ == '__main__':
    check()
