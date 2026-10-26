"""Finite exact checks for fixed-weight sparse binary path pattern moments.

The identities verified here are finite combinatorial consequences of uniform
sampling without replacement; the infinite Poisson and logical claims require
separate mathematical proofs.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def translations(n, pattern):
    return [frozenset(i + x for x in pattern) for i in range(n - pattern[-1])]


def falling(n, k):
    out = 1
    for x in range(k):
        out *= n - x
    return out


def hypergeom_probability(n, k, required):
    t = len(required)
    return Fraction(falling(k, t), falling(n, t)) if t <= k else Fraction(0)


def exhaustive_joint_moment(n, k, patterns, orders):
    all_trans = [translations(n, p) for p in patterns]
    total = 0
    for ones_tuple in combinations(range(n), k):
        ones = frozenset(ones_tuple)
        counts = [sum(t <= ones for t in trans) for trans in all_trans]
        product = 1
        for count, order in zip(counts, orders):
            product *= falling(count, order)
        total += product
    return Fraction(total, comb(n, k))


def exact_joint_moment(n, k, patterns, orders):
    from itertools import permutations, product
    selections = [list(permutations(translations(n, p), d)) for p, d in zip(patterns, orders)]
    total = Fraction(0)
    for selected_groups in product(*selections):
        union = set()
        for group in selected_groups:
            for t in group:
                union.update(t)
        total += hypergeom_probability(n, k, union)
    return total


def run():
    checks = 0
    cases = [
        (8, 3, [(0, 1), (0, 2), (0, 3)]),
        (9, 4, [(0, 1), (0, 2)]),
        (10, 4, [(0, 1), (0, 3)]),
        (9, 4, [(0, 1, 3), (0, 2, 3)]),
        (10, 5, [(0, 1, 3), (0, 2, 4)]),
    ]
    for n, k, patterns in cases:
        for p in patterns:
            for d in (1, 2):
                orders = [d]
                got = exhaustive_joint_moment(n, k, [p], orders)
                expected = exact_joint_moment(n, k, [p], orders)
                assert got == expected, (n, k, p, d, got, expected)
                checks += 1
        if len(patterns) >= 2:
            got = exhaustive_joint_moment(n, k, patterns[:2], [1, 1])
            expected = exact_joint_moment(n, k, patterns[:2], [1, 1])
            assert got == expected, (n, k, patterns, got, expected)
            checks += 1

    for r, pattern in [(2, (0, 2)), (3, (0, 2, 5)), (4, (0, 1, 3, 6))]:
        for n in (10**4, 10**5, 10**6):
            k = max(r, round(n ** (1 - 1 / r)))
            expectation = (n-pattern[-1]) * float(hypergeom_probability(n, k, pattern))
            assert abs(expectation - 1) < (0.14 if r == 4 else 0.075), (r, n, k, expectation)
            checks += 1
    print('SPARSE_FIXED_WEIGHT_PATH_EXACT_OK', checks, 'moment_checks', sum(2*len(p)+1 for _,_,p in cases), 'asymptotic_checks', 9)


if __name__ == '__main__':
    run()
