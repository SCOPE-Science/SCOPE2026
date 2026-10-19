#!/usr/bin/env python3
"""Exact finite tests of the complementary-branch Markov spectrum.
Requires Python 3 standard library only. Infinite-dimensional claims use the proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def multiply(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def cycles(q):
    seen = set()
    lengths = []
    for i in range(len(q)):
        if i in seen:
            continue
        j, ell = i, 0
        while j not in seen:
            seen.add(j)
            j = q[j]
            ell += 1
        lengths.append(ell)
    return lengths


def matrix_mul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def characteristic(a):
    """Exact characteristic coefficients via Newton's trace identities."""
    n = len(a)
    t, out, power = [Fraction(1)] + [Fraction(0)] * n, [], a
    for k in range(1, n + 1):
        tr = sum(power[i][i] for i in range(n))
        out.append(tr)
        t[k] = -sum(t[k-j] * out[j-1] for j in range(1, k+1)) / k
        power = matrix_mul(power, a)
    return t


def run():
    for n in (4, 5, 6, 7):
        m = n - 1
        r = tuple(m - i for i in range(n))
        a = [[int(j != r[i]) for j in range(n)] for i in range(n)]
        counts = [0] * (n + 1)
        for sigma in permutations(range(n)):
            q = multiply(sigma, r)
            # The unique zero of row i of AP is column sigma[r[i]].
            for i in range(n):
                for j in range(n):
                    assert a[i][sigma.index(j)] == int(j != q[i])
            ell = cycles(q)
            counts[1] += len(ell) > 1
            for d in range(2, n + 1):
                counts[d] += any(length % d == 0 for length in ell)
        for d in range(1, n + 1):
            if d == 1:
                expected = factorial(n) - factorial(n-1)
            else:
                avoid = Fraction(1)
                for j in range(1, n // d + 1):
                    avoid *= 1 - Fraction(1, d*j)
                expected = factorial(n) * (1 - avoid)
            assert counts[d] == expected, (n, d, counts[d], expected)
        print('n=', n, 'incidence=', counts[1:])
    sigma = (3, 0, 2, 1)
    n = 4
    r = tuple(n-1-i for i in range(n))
    a = [[int(j != r[i]) for j in range(n)] for i in range(n)]
    p = [[int(j == sigma[i]) for j in range(n)] for i in range(n)]
    b = matrix_mul(a, p)
    # (t-3)(t+1)(t^2-t+1) = t^4-3t^3+t-3.
    assert characteristic(b) == [1, -3, 0, 1, -3]
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
