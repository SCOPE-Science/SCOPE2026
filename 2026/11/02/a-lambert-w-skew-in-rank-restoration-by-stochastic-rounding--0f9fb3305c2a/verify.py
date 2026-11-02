#!/usr/bin/env python3
"""Independent, exact finite-case checks for a Bernoulli rank-restoration theorem.

Standard library only. Exhaustive checks corroborate finite special cases;
the general fixed-width asymptotic statement relies on the written proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, exp, isclose, log


def real_rank(rows):
    """Exact rational row reduction of a finite integer matrix."""
    a = [[Fraction(v) for v in row] for row in rows]
    n, d = len(a), len(a[0])
    r = 0
    for j in range(d):
        k = next((i for i in range(r, n) if a[i][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        pivot = a[r][j]
        for i in range(r + 1, n):
            if a[i][j]:
                mult = a[i][j] / pivot
                for t in range(j, d):
                    a[i][t] -= mult * a[r][t]
        r += 1
        if r == d:
            break
    return r


def failure_count_by_ones(n, d):
    counts = Counter()
    for bits in product((0, 1), repeat=n * d):
        rows = [bits[i * d:(i + 1) * d] for i in range(n)]
        if real_rank(rows) < d:
            counts[sum(bits)] += 1
    return counts


def failure_exact(n, d, p, counts=None):
    counts = counts if counts is not None else failure_count_by_ones(n, d)
    q = 1 - p
    return sum((count * p ** k * q ** (n * d - k)
                for k, count in counts.items()), Fraction())


def two_column_failure(n, p):
    q = 1 - p
    s = p * p + q * q
    return s ** n + 2 * q ** n - 2 * q ** (2 * n)


def two_column_stationarity(n, p):
    q = 1 - p
    s = p * p + q * q
    return (2 * p - 1) * s ** (n - 1) - q ** (n - 1) * (1 - 2 * q ** n)


def root_2column(n):
    lo, hi = 0.5, 1.0
    for _ in range(120):
        md = (lo + hi) / 2
        if two_column_stationarity(n, md) < 0:
            lo = md
        else:
            hi = md
    return (lo + hi) / 2


def lambert_w_positive(x):
    w = log(1 + x)
    for _ in range(50):
        e = exp(w)
        nxt = w - (w * e - x) / (e * (1 + w))
        if abs(nxt - w) < 1e-13:
            return nxt
        w = nxt
    raise AssertionError('Lambert W Newton iteration failed')


def hyperplane_maximal_test(d):
    """Inspect all small-integer normal vectors; general classification is proved."""
    cube = list(product((0, 1), repeat=d))
    tested = 0
    for normal in product(range(-2, 3), repeat=d):
        if not any(normal):
            continue
        tested += 1
        hits = sum(sum(x * v for x, v in zip(normal, vertex)) == 0
                   for vertex in cube)
        assert hits <= 2 ** (d - 1)
        if hits == 2 ** (d - 1):
            support = [(i, x) for i, x in enumerate(normal) if x]
            assert len(support) == 1 or (
                len(support) == 2 and support[0][1] == -support[1][1]
            )
    return tested


def main():
    checks = 0
    for d in (2, 3, 4, 5):
        checks += hyperplane_maximal_test(d)

    for n in range(2, 7):
        counts = failure_count_by_ones(n, 2)
        assert sum(counts.values()) < 2 ** (2 * n)
        checks += 1
        for p in (Fraction(1, 4), Fraction(1, 3), Fraction(1, 2),
                  Fraction(2, 3), Fraction(3, 4)):
            assert failure_exact(n, 2, p, counts) == two_column_failure(n, p)
            checks += 1

    for n, d, target in ((3, 3, (1, 9, 36, 78, 90, 54, 42, 18, 9, 1)),
                         (4, 3, (1, 12, 66, 196, 315, 288, 264, 144,
                                  135, 52, 30, 12, 1))):
        counts = failure_count_by_ones(n, d)
        assert tuple(counts[k] for k in range(n * d + 1)) == target
        checks += n * d + 1
        assert failure_exact(n, d, Fraction(1, 2), counts) == Fraction(sum(target), 2 ** (n * d))
        checks += 1
        for p in (Fraction(1, 3), Fraction(2, 3)):
            assert Fraction(0) < failure_exact(n, d, p, counts) < Fraction(1)
            checks += 1

    assert two_column_failure(2, Fraction(1, 2)) == Fraction(5, 8)
    checks += 1
    assert isclose(root_2column(2), 2 ** -0.5, abs_tol=1e-13)
    checks += 1
    assert isclose(two_column_failure(2, root_2column(2)), 0.5, abs_tol=1e-13)
    checks += 1
    assert isclose(root_2column(3), 2 / 3, abs_tol=1e-13)
    checks += 1

    for n in (3, 4, 5, 10, 20, 50, 100, 200, 500):
        r = root_2column(n)
        assert 0.5 < r < 1.0
        assert two_column_stationarity(n, 0.5) < 0
        assert two_column_stationarity(n, 1.0) > 0
        assert two_column_failure(n, r) < two_column_failure(n, 0.5)
        checks += 4
        for shift in (0.0001, 0.001, 0.01):
            if r - shift > 0:
                assert two_column_failure(n, r) <= two_column_failure(n, r - shift) + 1e-25
                checks += 1
            if r + shift < 1:
                assert two_column_failure(n, r) <= two_column_failure(n, r + shift) + 1e-25
                checks += 1
        if n >= 50:
            approx = 0.5 + lambert_w_positive(n) / (2 * n)
            assert abs(r - approx) < 3 * log(n) ** 2 / (n ** 2)
            checks += 1

    # The third-column, four-row case provides a finite-dimensional
    # orientation check on the direction of the optimum shift.
    t = failure_count_by_ones(4, 3)
    assert failure_exact(4, 3, Fraction(3, 5), t) < failure_exact(4, 3, Fraction(1, 2), t)
    checks += 1
    print(f'PASS: {checks} assertions/finite enumerations; exact rational tests, '
          'hypercube hyperplane checks and Lambert-W diagnostics')


if __name__ == '__main__':
    main()
