#!/usr/bin/env python3
"""Reproduce finite instances of the crown-graph negative-type spectrum.

Uses only Python's standard library. Numerical checks are not an infinite proof.
"""
import math


def metric(n, i, j):
    if i == j:
        return 0
    side_i, idx_i = divmod(i, n)
    side_j, idx_j = divmod(j, n)
    if side_i == side_j:
        return 2
    return 3 if idx_i == idx_j else 1


def apply(n, power, vec):
    size = 2 * n
    return [sum((metric(n, i, j) ** power if i != j else 0.0) * vec[j]
                for j in range(size)) for i in range(size)]


def eigenpairs(n, power):
    two, three = 2.0 ** power, 3.0 ** power
    u = [1.0] * (2 * n)
    v = [1.0] * n + [-1.0] * n
    result = [(u, (n - 1) * (two + 1) + three),
              (v, (n - 1) * (two - 1) - three)]
    for i in range(n - 1):
        x = [0.0] * n
        x[i], x[-1] = 1.0, -1.0
        result.append((x + x, three - two - 1))
        result.append((x + [-r for r in x], 1 - two - three))
    return result


def critical(n):
    if n <= 4:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(72):
        mid = (lo + hi) / 2
        if (n - 1) * (2.0 ** mid - 1.0) <= 3.0 ** mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def verify():
    tests = 0
    for n in range(3, 26):
        for p in (0.0, 0.125, 0.4, 0.9, 1.0, 1.1, 1.5, 2.0):
            for vec, ev in eigenpairs(n, p):
                lhs = apply(n, p, vec)
                err = max(abs(x - ev * y) for x, y in zip(lhs, vec))
                assert err < 2e-10 * (1 + abs(ev)), (n, p, err)
                tests += 1
        beta = critical(n)
        eigen = [pair[1] for pair in eigenpairs(n, beta)[1:]]
        assert max(eigen) < 1e-12, (n, beta, max(eigen))
        if n >= 5:
            assert abs((n - 1) * (2.0 ** beta - 1.0) - 3.0 ** beta) < 1e-12
            assert max(pair[1] for pair in eigenpairs(n, beta + 1e-3)[1:]) > 0
    # Match the analytic expansion only at genuinely large orders.
    a, b = math.log(2), math.log(3)
    for n in (100, 1000, 10000):
        N = n - 1
        approx = 1/(a*N) + (b/a**2 - 1/(2*a))/N**2
        assert abs(critical(n) - approx) < 4.0/N**3, (n, approx)
    print('CHECK_OK', tests, 'explicit vector/eigenvalue tests; 23 boundary tests; 3 asymptotic tests')


if __name__ == '__main__':
    verify()
