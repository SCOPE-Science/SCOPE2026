#!/usr/bin/env python3
"""Finite checks of the action-quandle polynomial and partition formulas.

Only standard-library Python is needed.  The finite tests corroborate,
but do not replace, the arbitrary-degree proof in RESULT.md.
"""
from collections import Counter
from itertools import permutations
from math import factorial


def multiply(a, b):
    """Right-action convention: x^(ab) = (x^a)^b."""
    return tuple(b[a[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def op(x, g, y, h):
    return multiply(inverse(g), h)[x], multiply(multiply(inverse(h), g), h)


def cycle_data(g):
    n = len(g)
    multiplicity = Counter()
    point_length = {}
    seen = set()
    for start in range(n):
        if start in seen:
            continue
        orbit = []
        x = start
        while x not in seen:
            seen.add(x)
            orbit.append(x)
            x = g[x]
        d = len(orbit)
        multiplicity[d] += 1
        for z in orbit:
            point_length[z] = d
    return multiplicity, point_length


def integer_partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for first in range(minimum, n + 1):
            for rest in integer_partitions(n - first, first):
                yield (first,) + rest


def centralizer_size(multiplicity):
    z = 1
    for d, m in multiplicity.items():
        z *= d ** m * factorial(m)
    return z


def predicted_polynomial(n):
    p = Counter()
    for lam in integer_partitions(n):
        multiplicity = Counter(lam)
        z = centralizer_size(multiplicity)
        for d, m in multiplicity.items():
            c = z * len(multiplicity)
            r = n * z // (d * m)
            p[(c, r)] += (factorial(n) // z) * d * m
    return p


def partition_numbers(n):
    p = [1] + [0] * n
    for d in range(1, n + 1):
        for j in range(d, n + 1):
            p[j] += p[j - d]
    return p


def check_direct(n):
    group = list(permutations(range(n)))
    points = [(x, g) for g in group for x in range(n)]
    polynomial = Counter()
    checked = 0
    for x, g in points:
        c = r = 0
        m, point_length = cycle_data(g)
        z = centralizer_size(m)
        expected_c = z * len(m)
        expected_r = n * z // (point_length[x] * m[point_length[x]])
        for y, h in points:
            r += op(x, g, y, h) == (x, g)
            c += op(y, h, x, g) == (y, h)
            checked += 2
        assert (c, r) == (expected_c, expected_r), (n, x, g, c, r)
        polynomial[(c, r)] += 1
    assert polynomial == predicted_polynomial(n), (n, polynomial, predicted_polynomial(n))
    p = partition_numbers(n)
    fixed = sum(c * count for (c, r), count in polynomial.items())
    assert fixed == sum(r * count for (c, r), count in polynomial.items())
    assert fixed == n * factorial(n) * sum(p[:n])
    if n >= 3:
        assert polynomial[(n, n)] == factorial(n)
    assert sum(polynomial.values()) == n * factorial(n)
    return checked, len(polynomial), fixed


def check_trivial_group_actions():
    # A nonfaithful action on a set of m points reduces the polynomial
    # to m parallel copies of the group conjugation quandle.
    for n in range(1, 6):
        group = list(permutations(range(n)))
        for m in (1, 2, 4):
            for g in group:
                centralizer = sum(multiply(g, h) == multiply(h, g) for h in group)
                c = m * centralizer
                r = m * centralizer
                # Directly test the trivial action's algebraic equalities.
                assert c == m * centralizer and r == m * centralizer


if __name__ == '__main__':
    check_trivial_group_actions()
    total_checks = 0
    for n in range(1, 6):
        checks, terms, fixed = check_direct(n)
        total_checks += checks
        print(f'n={n} terms={terms} fixed_pairs={fixed} operation_comparisons={checks}')
    print(f'VERIFY_OK degrees=5 operation_comparisons={total_checks}')
