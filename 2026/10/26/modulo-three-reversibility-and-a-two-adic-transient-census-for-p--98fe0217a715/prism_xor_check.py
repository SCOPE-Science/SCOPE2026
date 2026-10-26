#!/usr/bin/env python3
"""Reproducible checks for open-neighbor XOR on C_n Cartesian K_2.

The matrix and the polynomial predictions are implemented separately.
These finite computations are checks, not a substitute for the general proof.
"""
from collections import Counter
from functools import reduce


def degree(x):
    return x.bit_length() - 1


def polynomial_remainder(a, b):
    assert b
    while a and degree(a) >= degree(b):
        a ^= b << (degree(a) - degree(b))
    return a


def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_remainder(a, b)
    return a


def polynomial_product(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result


def polynomial_power(a, m):
    result = 1
    while m:
        if m & 1:
            result = polynomial_product(result, a)
        a = polynomial_product(a, a)
        m >>= 1
    return result


def dimension_of_fixed_points(n, m):
    g = (1 << n) | 1
    p = 0b111
    h = polynomial_power(p, m) ^ (1 << m)
    if m % 2:
        return degree(polynomial_gcd(g, polynomial_product(h, h)))
    return 2 * degree(polynomial_gcd(g, h))


def rows_of_prism_adjacency(n):
    assert n >= 3
    rows = []
    for side in range(2):
        for position in range(n):
            neighbors = (
                side * n + (position - 1) % n,
                side * n + (position + 1) % n,
                (1 - side) * n + position,
            )
            assert len(set(neighbors)) == 3
            rows.append(sum(1 << j for j in neighbors))
    return rows


def matrix_compose(left, right):
    width = len(left)
    out = []
    for row in left:
        result = 0
        for j in range(width):
            if (row >> j) & 1:
                result ^= right[j]
        out.append(result)
    return out


def matrix_power(a, m):
    result = [1 << j for j in range(len(a))]
    while m:
        if m & 1:
            result = matrix_compose(result, a)
        a = matrix_compose(a, a)
        m >>= 1
    return result


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = degree(row)
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def nilpotent_depth(n):
    if n % 3:
        return 0
    k = n & -n
    return 2 if k == 1 else k


def kernel_dimension(n, t):
    if n % 3:
        return 0
    k = n & -n
    return 2 * min(t, 2) if k == 1 else 4 * min(t, k)


def eventual_dimension(n):
    return 2 * n if n % 3 else 2 * n - 4 * (n & -n)


def update(rows, state):
    value = 0
    for j, row in enumerate(rows):
        value |= ((row & state).bit_count() & 1) << j
    return value


def test_matrix_and_polynomial_formulas():
    tests = 0
    for n in range(3, 25):
        a = rows_of_prism_adjacency(n)
        for t in range(0, max(nilpotent_depth(n) + 2, 13)):
            observed = len(a) - rank(matrix_power(a, t))
            assert observed == kernel_dimension(n, t), (n, t, observed)
            tests += 1
        for m in range(1, 21):
            power = matrix_power(a, m)
            fixed_equations = [row ^ (1 << j) for j, row in enumerate(power)]
            observed = 2*n - rank(fixed_equations)
            predicted = dimension_of_fixed_points(n, m)
            assert observed == predicted, (n, m, observed, predicted)
            tests += 1
    return tests


def test_all_labelled_states():
    count = 0
    for n in range(3, 9):
        rows = rows_of_prism_adjacency(n)
        distribution = Counter()
        T = nilpotent_depth(n)
        for start in range(1 << (2*n)):
            first_seen = {}
            x = start
            while x not in first_seen:
                first_seen[x] = len(first_seen)
                x = update(rows, x)
            arrival = first_seen[x]
            assert arrival <= T, (n, start, arrival)
            distribution[arrival] += 1
            count += 1
        base = eventual_dimension(n)
        assert distribution[0] == (1 << base), (n, distribution[0])
        for t in range(1, T+1):
            cumulative = 1 << (base + kernel_dimension(n, t))
            previous = 1 << (base + kernel_dimension(n, t-1))
            assert distribution[t] == cumulative - previous, (n, t, distribution[t])
        assert sum(distribution.values()) == 1 << (2*n)
    return count


if __name__ == '__main__':
    checks = test_matrix_and_polynomial_formulas()
    states = test_all_labelled_states()
    print('VERIFY_OK matrix_rank_checks=%d labelled_states=%d' % (checks, states))
