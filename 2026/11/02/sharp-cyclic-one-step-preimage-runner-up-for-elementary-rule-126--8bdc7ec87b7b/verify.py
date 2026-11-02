#!/usr/bin/env python3
"""Exact finite checks for cyclic elementary cellular automaton Rule 126."""
from collections import Counter
from itertools import product


def rule126(x, n):
    y = 0
    for j in range(n):
        t = ((x >> ((j - 1) % n)) & 1) + ((x >> j) & 1) + ((x >> ((j + 1) % n)) & 1)
        if t == 1 or t == 2:
            y |= 1 << j
    return y


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def tau(a):
    return (1, 0, -1)[a % 3]


def formula(y, n):
    mask = (1 << n) - 1
    if y == mask:
        lucas = fib(n - 1) + fib(n + 1) if n >= 1 else 2
        return lucas + (2 if n % 3 == 0 else -1)
    zeros = [j for j in range(n) if ((y >> j) & 1) == 0]
    fs, ts = 1, 1
    for i, j in enumerate(zeros):
        k = zeros[(i + 1) % len(zeros)]
        gap = (k - j - 1) % n
        fs *= (1 if gap == 0 else fib(gap - 1))
        ts *= tau(gap)
    return fs + ts


def mult(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def verify_matrix_formula(n):
    states = ((0, 0), (0, 1), (1, 0), (1, 1))
    B0 = [[0] * 4 for _ in range(4)]
    B1 = [[0] * 4 for _ in range(4)]
    for i, (a, b) in enumerate(states):
        for c in (0, 1):
            j = states.index((b, c))
            T = B0 if a == b == c else B1
            T[i][j] = 1
    I = [[int(i == j) for j in range(4)] for i in range(4)]
    for nbits in range(1, n + 1):
        for y in range(1 << nbits):
            P = I
            for j in range(nbits):
                P = mult(P, B1 if ((y >> j) & 1) else B0)
            assert trace(P) == formula(y, nbits), ('matrix', nbits, y)


def run():
    # Matrix traces are independent from the direct forward-map enumeration.
    verify_matrix_formula(10)
    for n in range(1, 17):
        counts = Counter(rule126(x, n) for x in range(1 << n))
        assert sum(counts.values()) == (1 << n)
        for y in range(1 << n):
            assert counts[y] == formula(y, n), ('fiber', n, y, counts[y], formula(y, n))
        if n >= 7:
            top = (1 << n) - 1
            biggest = formula(top, n)
            second = fib(n - 2) + tau(n - 1)
            assert counts[top] == biggest
            assert max(counts[y] for y in range(1 << n) if y != top) == second
            winners = {y for y in range(1 << n) if y != top and counts[y] == second}
            expected = {top ^ (1 << i) for i in range(n)}
            assert winners == expected, ('runners', n, winners, expected)
            print(f'n={n} global={biggest} runner_up={second} count={len(winners)}')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
