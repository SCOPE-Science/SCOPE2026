"""Exact finite classification of permutation-memory Fibonacci scalar collapse.

Run with: python3 verify.py
Uses only Python's standard library and exact integer arithmetic.

The finite window is logically exhaustive by Cayley-Hamilton and the
invertible stable-image lemma proved in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations


def fibonacci_memory(pattern, length):
    period = len(pattern)
    values = [0, 1]
    for n in range(2, length):
        order = pattern[n % period]
        values.append(sum(values[n - j] for j in range(1, min(n, order) + 1)))
    return values


def transition(order, size):
    return [[int(j < order) for j in range(size)]] + [
        [int(j == i - 1) for j in range(size)]
        for i in range(1, size)
    ]


def matmul(a, b):
    size = len(a)
    return [[sum(a[i][h] * b[h][j] for h in range(size))
             for j in range(size)] for i in range(size)]


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def scalar_collapse(pattern):
    """An exact criterion for eventual *single-scalar* k-step collapse."""
    k = len(pattern)
    d = k + 1
    # Q=2d guarantees d completed blocks after an already valid state.
    # This removes all nilpotent transients before the exact test.
    Q = 2 * d
    terms = fibonacci_memory(pattern, (Q + d + 2) * k + d + 2)
    multiplier = Fraction(terms[(Q + 1) * k], terms[Q * k])
    works = all(
        terms[(q + 1) * k + r] * multiplier.denominator
        == terms[q * k + r] * multiplier.numerator
        for q in range(Q, Q + d) for r in range(k)
    )
    # Independent state-space evaluation of one full period, testing the
    # second implementation of the recurrence at d+1 successive blocks.
    matrix = [[int(i == j) for j in range(d)] for i in range(d)]
    for n in range(Q * k + 1, (Q + 1) * k + 1):
        matrix = matmul(transition(pattern[n % k], d), matrix)
    vector = [terms[Q * k - j] for j in range(d)]
    for q in range(Q, Q + d + 1):
        expected = [terms[q * k - j] for j in range(d)]
        if vector != expected:
            raise AssertionError(('matrix-disagreement', pattern, q))
        vector = matvec(matrix, vector)
    return multiplier, works


def rotations(pattern):
    return {pattern[j:] + pattern[:j] for j in range(len(pattern))}


def main():
    total = 0
    counts = []
    for k in range(2, 6):
        good = set()
        for pattern in permutations(range(2, k + 2)):
            total += 1
            multiplier, works = scalar_collapse(pattern)
            if works:
                if multiplier != 3 * 2 ** (k - 2):
                    raise AssertionError(('wrong-multiplier', pattern, multiplier))
                good.add(pattern)
        ascending = tuple(range(2, k + 2))
        expected = rotations(ascending)
        if k == 5:
            exceptional = (2, 4, 5, 6, 3)
            expected |= rotations(exceptional)
        if good != expected:
            raise AssertionError(('wrong-classification', k, good ^ expected))
        counts.append(len(good))
    pattern = (2, 4, 5, 6, 3)
    values = fibonacci_memory(pattern, 51)
    if values[6:11] != [13, 26, 52, 91, 143]:
        raise AssertionError('incorrect-base-values')
    if values[11:16] != [312, 624, 1248, 2184, 3432]:
        raise AssertionError('incorrect-five-checks')
    for n in range(6, 46):
        if values[n + 5] != 24 * values[n]:
            raise AssertionError(('noncyclic-witness', n))
    if total != 152 or counts != [2, 3, 4, 10]:
        raise AssertionError(('unexpected-counts', total, counts))
    print('VERIFY_OK permutations=152 counts=2,3,4,10 noncyclic_first=5 multiplier=24 matrix_checked=yes')


if __name__ == '__main__':
    main()
