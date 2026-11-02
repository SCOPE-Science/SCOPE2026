"""Exact-integer checks for bipartite average-distance swapping.

Run: python check_biclique.py. No external packages required.
The code checks finite examples only; the paper's general proof is separate.
"""
from itertools import combinations, combinations_with_replacement
from math import comb


def inside_distance(points, group):
    return sum(abs(points[i] - points[j]) for i, j in combinations(group, 2))


def potential_scaled(points, left):
    n = len(points)
    a = len(left)
    b = n - a
    A = set(left)
    B = set(range(n)) - A
    return b * inside_distance(points, A) + a * inside_distance(points, B)


def crossed_costs_scaled(points, left, x, y):
    """Returns the two positive improvement numerators, scaled by ab."""
    A = set(left)
    B = set(range(len(points))) - A
    a, b = len(A), len(B)
    assert x in A and y in B
    old_x = sum(abs(points[x] - points[j]) for j in B)
    new_x = sum(abs(points[x] - points[j]) for j in (A - {x}) | {y})
    old_y = sum(abs(points[y] - points[j]) for j in A)
    new_y = sum(abs(points[y] - points[j]) for j in (B - {y}) | {x})
    return a * old_x - b * new_x, b * old_y - a * new_y


def rounded_partition(n, a):
    """Integer half-up rounding of ak/n, stable through all prefixes."""
    qprev = 0
    chosen = []
    for k in range(1, n + 1):
        q = (2 * a * k + n) // (2 * n)
        assert qprev <= q <= qprev + 1
        if q > qprev:
            chosen.append(k - 1)
        qprev = q
    assert len(chosen) == a
    return tuple(chosen)


def social_cross(points, left):
    A = set(left)
    B = set(range(len(points))) - A
    return sum(abs(points[i] - points[j]) for i in A for j in B)


def social_rounded_partition(n, a):
    """Clamp the nearest integer to (a-b+2*k)/4 at every rank prefix."""
    b = n - a
    prev = 0
    chosen = []
    for k in range(1, n + 1):
        lo = max(0, k - b)
        hi = min(a, k)
        nearest = (a - b + 2*k + 2) // 4
        q = max(lo, min(hi, nearest))
        assert prev <= q <= prev + 1
        if q > prev:
            chosen.append(k - 1)
        prev = q
    assert len(chosen) == a
    return tuple(chosen)


def is_stable(points, left):
    A = set(left)
    B = set(range(len(points))) - A
    return all(not (g1 > 0 and g2 > 0)
               for x in A for y in B
               for g1, g2 in [crossed_costs_scaled(points, left, x, y)])


def exhaustive():
    partitions = 0
    edges = 0
    families = 0
    roundings = 0
    social_roundings = 0
    for n in range(2, 9):
        for a in range(1, n):
            b = n - a
            candidates = list(combinations(range(n), a))
            choice = rounded_partition(n, a)
            social_choice = social_rounded_partition(n, a)
            for tup in combinations_with_replacement(range(4), n):
                points = list(tup)
                families += 1
                best = max(potential_scaled(points, A) for A in candidates)
                assert potential_scaled(points, choice) == best
                assert is_stable(points, choice)
                roundings += 1
                social_best = min(social_cross(points, A) for A in candidates)
                assert social_cross(points, social_choice) == social_best
                social_roundings += 1
                for A in candidates:
                    partitions += 1
                    v = potential_scaled(points, A)
                    SA = set(A)
                    B = set(range(n)) - SA
                    for x in SA:
                        for y in B:
                            g1, g2 = crossed_costs_scaled(points, A, x, y)
                            newA = tuple(sorted((SA - {x}) | {y}))
                            diff = potential_scaled(points, newA) - v
                            assert diff == g1 + g2
                            assert not (g1 > 0 and g2 > 0 and diff <= 0)
                            edges += 1
                    if a == 1:
                        x = A[0]
                        sums = [sum(abs(points[i] - points[j]) for j in range(n)) for i in range(n)]
                        opt = min(sums)
                        if opt:
                            assert sums[x] <= (n - 1) * opt
    for n in range(3, 51):
        types = [0] + [1] * (n - 1)
        worst = 0
        best = 1
        assert sum(abs(types[worst] - t) for t in types) == n - 1
        assert sum(abs(types[best] - t) for t in types) == 1
        assert is_stable(types, (0,))
    # Exact seven-agent instance where the best equilibrium is worse than
    # the global cost minimum. Zero-type multiplicities are interchangeable.
    points = [0, 0, 0, 0, 1, 3, 4]
    pairs = list(combinations(range(7), 2))
    assert min(social_cross(points, A) for A in pairs) == 15
    assert min(social_cross(points, A) for A in pairs
               if is_stable(points, A)) == 17
    assert {tuple(sorted(points[i] for i in A)) for A in pairs
            if is_stable(points, A)} == {(0,3),(0,4),(1,4)}
    print('PASS: exact potential identities, strict-improvement monotonicity,')
    print('quantile-ranked potential maximizers, every tested equilibrium,')
    print('star upper bound and its sharp example.')
    print('Type-multiset/part-size families:', families)
    print('Checked group partitions:', partitions)
    print('Checked cross-part swaps:', edges)
    print('Checked rounded equilibria:', roundings)
    print('Checked socially optimal rounded allocations:', social_roundings)
    print('Exact K_2,5 stability/optimum gap: 17/15 in pairwise crossing costs')
    print('Sharp star examples:', 48)


if __name__ == '__main__':
    exhaustive()
