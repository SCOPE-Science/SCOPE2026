#!/usr/bin/env python3
"""Independent finite checks for minimal obstructions to disjunctive constancy.

Uses only Python's standard library. This is not a proof of the all-domain bound.
"""
from itertools import product
from collections import Counter


def check_finite(q: int, m: int):
    points = list(product(range(q), repeat=m))
    n = len(points)
    masks = []
    for a in product(range(q), repeat=m):
        mask = 0
        for j, t in enumerate(points):
            if any(t[i] == a[i] for i in range(m)):
                mask |= 1 << j
        masks.append(mask)

    def coverable(team):
        return any(team & ~mask == 0 for mask in masks)

    bad, minimal = 0, Counter()
    for team in range(1 << n):
        if coverable(team):
            continue
        bad += 1
        if all(coverable(team & ~(1 << j))
               for j in range(n) if team >> j & 1):
            size = team.bit_count()
            minimal[size] += 1
            assert size <= (1 << m), (q, m, size)

    if q == 2:
        full = (1 << n) - 1
        assert not coverable(full)
        assert all(coverable(full & ~(1 << j)) for j in range(n))
        assert minimal[1 << m] >= 1
    print(f'finite q={q} m={m} teams={1<<n} bad={bad} minimal={dict(sorted(minimal.items()))}')
    return minimal


def check_rank_cube(m: int):
    points = list(product((0, 1), repeat=m))
    n = len(points)
    # For every deleted point t, the complement a is a cover of all other points.
    # H[s,t] = product_i(a_i - s_i) is diagonal and nonzero.
    for t in points:
        a = tuple(1-v for v in t)
        for s in points:
            product_value = 1
            for i in range(m):
                product_value *= a[i] - s[i]
            assert (product_value != 0) == (s == t)
    # Every such column is multilinear in the m coordinates, with at most 2**m monomials.
    print(f'rank-witness cube m={m}: {n} diagonal nonzero evaluations')


if __name__ == '__main__':
    for q, m in [(2, 1), (3, 1), (2, 2), (3, 2), (2, 3), (2, 4)]:
        check_finite(q, m)
    for m in range(1, 7):
        check_rank_cube(m)
    print('ALL_CHECKS_OK')
