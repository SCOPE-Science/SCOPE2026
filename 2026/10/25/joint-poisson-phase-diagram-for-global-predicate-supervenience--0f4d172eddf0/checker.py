"""Finite checks for the collision/supervenience theorem.

Usage: python3 checker.py
No third-party packages are required.
"""
from itertools import combinations, product
from fractions import Fraction


def masks(r):
    return tuple(range(1 << r))


def project(row, mask):
    return tuple(row[j] for j in range(len(row)) if mask & (1 << j))


def collision_count(rows, mask):
    return sum(project(rows[i], mask) == project(rows[j], mask)
               for i, j in combinations(range(len(rows)), 2))


def dependence(rows, antecedent, consequent):
    return all(project(rows[i], antecedent) != project(rows[j], antecedent)
               or project(rows[i], consequent) == project(rows[j], consequent)
               for i, j in combinations(range(len(rows)), 2))


def classified(rows, a):
    r = len(rows[0]); masks_ = masks(r)
    critical = [A for A in masks_ if A.bit_count() == a]
    good = True
    for A in masks_:
        if A.bit_count() > a and collision_count(rows, A):
            good = False
        if A.bit_count() == a:
            for j in range(r):
                if not (A & (1 << j)) and collision_count(rows, A | (1 << j)):
                    good = False
        if A.bit_count() < a:
            for j in range(r):
                if not (A & (1 << j)) and dependence(rows, A, 1 << j):
                    good = False
    if good:
        for A in masks_:
            for B in masks_:
                expected = (B & ~A == 0 or A.bit_count() > a
                            or (A.bit_count() == a and collision_count(rows, A) == 0))
                assert dependence(rows, A, B) == expected
    return good, tuple(collision_count(rows, A) for A in critical)


def exact_exhaustion(q, r, m, a):
    vectors = tuple(product(range(q), repeat=r))
    patterns = {}; n_good = 0; total = 0
    for rows in product(vectors, repeat=m):
        good, counts = classified(rows, a)
        total += 1
        n_good += good
        patterns[counts] = patterns.get(counts, 0) + 1
    assert sum(patterns.values()) == total == q ** (r * m)
    # Check exact first and cross second moments, including overlapping pairs.
    n_pairs = m * (m - 1) // 2
    subsets = [A for A in masks(r) if A.bit_count() == a]
    for i, A in enumerate(subsets):
        expect = Fraction(n_pairs, q ** a)
        observed = Fraction(sum(freq * c[i] for c, freq in patterns.items()), total)
        assert observed == expect, (q, r, m, a, A)
        for j, B in enumerate(subsets):
            if i == j:
                continue
            pair_prob = Fraction(1, q ** ((A | B).bit_count()))
            prediction = n_pairs * pair_prob + n_pairs * (n_pairs - 1) * Fraction(1, q ** (2*a))
            observed2 = Fraction(sum(freq * c[i] * c[j] for c, freq in patterns.items()), total)
            assert observed2 == prediction, (A, B, observed2, prediction)
    print(f'PASS q={q} r={r} m={m} a={a}: {total} world tables, {n_good} satisfying exact profile preconditions')


if __name__ == '__main__':
    for args in ((2, 2, 2, 1), (2, 2, 3, 1), (3, 2, 3, 1),
                 (2, 3, 3, 1), (2, 3, 3, 2), (2, 3, 4, 1),
                 (2, 3, 4, 2), (3, 3, 3, 1), (3, 3, 3, 2)):
        exact_exhaustion(*args)
    print('ALL_CHECKS_OK')
