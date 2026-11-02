#!/usr/bin/env python3
"""Exact finite checks for a weighted biclique random-walk Kemeny identity."""
from fractions import Fraction as F


def inverse(matrix):
    n = len(matrix)
    work = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if work[i][j])
        work[j], work[pivot] = work[pivot], work[j]
        divisor = work[j][j]
        work[j] = [v / divisor for v in work[j]]
        for i in range(n):
            if i == j:
                continue
            scale = work[i][j]
            if scale:
                work[i] = [u - scale * v for u, v in zip(work[i], work[j])]
    return [row[n:] for row in work]


def kemeny_direct(a, b, t):
    n = a + b
    w = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(a):
        for j in range(a, n):
            w[i][j] = w[j][i] = F(1)
    w[0][1] = w[1][0] = t
    d = [sum(row) for row in w]
    pi = [v / sum(d) for v in d]
    p = [[w[i][j] / d[i] for j in range(n)] for i in range(n)]
    m = [[F(i == j) - p[i][j] + pi[j] for j in range(n)] for i in range(n)]
    z = inverse(m)
    return sum(z[i][i] for i in range(n)) - 1


def difference(a, b, t):
    return t * (4 * (a - 2) * t - 3 * b) / (2 * (b + 2 * t) * (a * b + t))


def derivative_sign(a, x):
    return (8 * a * a - 12 * a - 2) * x * x + 8 * a * (a - 2) * x - 3 * a


def run():
    tests = 0
    strengths = [F(0), F(1, 3), F(1), F(5, 2), F(10)]
    for a in range(2, 8):
        for b in range(1, 9):
            for t in strengths:
                actual = kemeny_direct(a, b, t)
                expected = F(a + b) - F(3, 2) + difference(a, b, t)
                assert actual == expected, (a, b, t, actual, expected)
                tests += 1
                assert difference(a, b, t) >= -F(1, 6)
                tests += 1
    for b in range(1, 13):
        assert difference(2, b, F(b)) == -F(1, 6)
        tests += 1
        for a in range(3, 13):
            assert difference(a, b, F(b)) > -F(1, 6)
            tests += 1
    for n in range(2, 19):
        sign = (difference(n, n, F(1)) > 0) - (difference(n, n, F(1)) < 0)
        assert sign == ((n > 8) - (n < 8))
        tests += 1
    for a in range(2, 25):
        # Unique derivative sign crossing brackets for the positive root.
        assert derivative_sign(a, F(0)) < 0
        assert derivative_sign(a, F(100)) > 0
        tests += 2
        for x in [F(1, 10000), F(1, 100), F(1), F(10), F(100)]:
            # Dependence on b occurs only through x=t/b.
            assert difference(a, 5, 5 * x) == difference(a, 7, 7 * x)
            tests += 1
    print('PASS', tests, 'exact assertions')


if __name__ == '__main__':
    run()
