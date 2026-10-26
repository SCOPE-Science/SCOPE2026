#!/usr/bin/env python3
"""Independent finite checks of directed successor-order collision identities.

Python 3 standard library only. Enumerates labelled linear orders and exact
joint moments; no stochastic simulation is used to certify identities.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def compatible(arcs):
    out, inc = {}, {}
    for u, v in arcs:
        if u == v or (u in out and out[u] != v) or (v in inc and inc[v] != u):
            return False
        out[u] = v
        inc[v] = u
    for source in out:
        seen = set()
        u = source
        while u in out:
            if u in seen:
                return False
            seen.add(u)
            u = out[u]
    return True


def test_prescribed_arcs():
    tested = 0
    for n in range(2, 6):
        permutations_n = list(permutations(range(n)))
        arc_sets = [{(perm[i], perm[i+1]) for i in range(n-1)}
                    for perm in permutations_n]
        arcs = [(u, v) for u in range(n) for v in range(n) if u != v]
        for k in range(1, min(3, len(arcs)) + 1):
            for sample in combinations(arcs, k):
                count = sum(set(sample).issubset(a) for a in arc_sets)
                predicted = factorial(n-k) if compatible(sample) else 0
                assert count == predicted, (n, sample, count, predicted)
                tested += 1
    return tested


def expected_moments(n, r):
    # Y counts (ordered arc, unordered triple of orders) incidents.
    mu = Fraction(n * (n-1) * choose(r, 3), n**3)
    a = [choose(r, 3) * choose(3, s) * choose(r-3, 3-s)
         for s in range(4)]
    same_arc = n * (n-1) * sum((Fraction(a[s], n**(6-s)) for s in range(3)), Fraction())
    other_arcs = n * (n-1)**2 * (n-2) * sum(
        (Fraction(a[s], n**(6-s) * (n-1)**s) for s in range(4)), Fraction())
    return mu, same_arc + other_arcs


def test_joint_distributions():
    checked = []
    for n, r in [(3, 3), (3, 4), (4, 3), (4, 4)]:
        perms = list(permutations(range(n)))
        events = [{(p[i], p[i+1]) for i in range(n-1)} for p in perms]
        total = 0
        ysum = 0
        y2sum = 0
        for state in product(range(len(perms)), repeat=r):
            counts = Counter(e for j in state for e in events[j])
            y = sum(choose(v, 3) for v in counts.values())
            z = sum(v >= 3 for v in counts.values())
            assert (y > 0) == (z > 0)
            total += 1
            ysum += y
            y2sum += y*(y-1)
        expected_first, expected_second = expected_moments(n, r)
        assert Fraction(ysum, total) == expected_first
        assert Fraction(y2sum, total) == expected_second
        checked.append((n, r, total, str(expected_first), str(expected_second)))
    return checked


if __name__ == '__main__':
    count = test_prescribed_arcs()
    print('ORDER_ARC_CONTRACTION_CHECK_OK', count)
    for row in test_joint_distributions():
        print('TRIPLE_COLLISION_EXACT_MOMENTS_OK', *row)
    print('TRIPLE_SUCCESSOR_CHECK_OK')
