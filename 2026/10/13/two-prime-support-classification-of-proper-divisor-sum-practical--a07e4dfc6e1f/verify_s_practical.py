#!/usr/bin/env python3
"""Exact arithmetic checks for the two-prime s-practical classification.

Uses only the Python standard library. Finite checks test critical identities
and boundary certificates; the accompanying written inequalities prove the
unbounded exponent ranges.
"""
from math import isqrt


def aliquot(p, i, j):
    assert i >= 0 and j >= 0 and p >= 3
    value = ((p + 1) * (2 ** i) - p) * p ** j - (2 ** (i + 1) - 1)
    assert value % (p - 1) == 0
    return value // (p - 1)


def proper_divisor_sum(n):
    total = 0
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            e = n // d
            if d < n:
                total += d
            if e != d and e < n:
                total += e
    return total


def greedy(p, a, b):
    weights = sorted(aliquot(p, i, j)
                     for i in range(a + 1) for j in range(b + 1))
    reach = 0
    for w in weights:
        if w > reach + 1:
            return False, reach + 1, weights, reach
        reach += w
    return True, reach, weights, reach


def total(p, a, b):
    return sum(aliquot(p, i, j)
               for i in range(a + 1) for j in range(b + 1))


def row_gap(p, a, b):
    return aliquot(p, a + 1, b) - sum(
        aliquot(p, a + 1, j) for j in range(b))


def col_gap(p, a, b):
    return aliquot(p, a, b + 1) - sum(
        aliquot(p, i, b + 1) for i in range(a))


def margins(p, a, b):
    s = total(p, a, b)
    return s + 1 - row_gap(p, a, b), s + 1 - col_gap(p, a, b)


def theorem(p, a, b):
    return ((p == 3 and ((a >= 4 and b >= 1) or
                         (a >= 3 and b >= 2) or
                         (a >= 2 and b >= 3))) or
            (p == 5 and ((a >= 4 and b >= 2) or
                         (a >= 3 and b >= 3))))


def run():
    direct_checks = 0
    for p in (3, 5, 7):
        for i in range(6):
            for j in range(5):
                n = 2 ** i * p ** j
                assert aliquot(p, i, j) == proper_divisor_sum(n), (p, i, j)
                direct_checks += 1

    certified = {
        (3, 2, 3): (358, (141, 77)),
        (3, 3, 2): (273, (106, 141)),
        (3, 4, 1): (161, (37, 106)),
        (5, 3, 3): (2704, (551, 206)),
        (5, 4, 2): (1205, (302, 551)),
    }
    for (p, a, b), (s, mr) in certified.items():
        yes, reach, _, _ = greedy(p, a, b)
        assert yes and reach == s == total(p, a, b)
        assert margins(p, a, b) == mr

    failures = {
        (3, 1, 1): 3,
        (3, 2, 1): 12,
        (3, 2, 2): 53,
        (3, 3, 1): 35,
        (5, 1, 1): 3,
        (5, 2, 2): 20,
        (5, 3, 2): 259,
        (5, 4, 1): 6,
        (7, 2, 1): 6,
    }
    for (p, a, b), k in failures.items():
        good, least, _, _ = greedy(p, a, b)
        assert not good and least == k

    classification_checks = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29):
        for a in range(1, 11):
            for b in range(1, 9):
                yes, reach, _, _ = greedy(p, a, b)
                assert yes == theorem(p, a, b), (p, a, b, reach)
                classification_checks += 1

    delta_checks = 0
    for p in (3, 5):
        for a in range(2, 12):
            for b in range(1, 11):
                U = 2 ** (a + 1) - 1
                drow = (p ** b * (2 * (p + 1) * U - (a + 1) * p ** 2
                                - (p - 2)) - (4 * U - a))
                dcol = (p ** (b + 1) * ((p + 1) * U - a * p ** 2
                                      - 2 * p + 1) - (2 * U - a - 1))
                assert drow % (p - 1) == dcol % (p - 1) == 0
                mr, mc = margins(p, a, b)
                mr_b, mc_b = margins(p, a, b + 1)
                assert mr_b - mr == drow // (p - 1)
                assert mc_b - mc == dcol // (p - 1)
                delta_checks += 2

    print('VERIFY_OK direct_aliquot=%s five_base_certificates=yes '
          'nine_exclusion_witnesses=yes rectangular_cases=%s '
          'delta_identity_checks=%s infinite_proof=written_inequalities'
          % (direct_checks, classification_checks, delta_checks))


if __name__ == '__main__':
    run()
