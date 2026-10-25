#!/usr/bin/env python3
"""Exact exhaustive certificate for a four-car weighted parking counterexample."""
from collections import defaultdict
from itertools import product
from fractions import Fraction

def cells(n, weights):
    assert len(weights) == n and all(type(v) is int and v > 0 for v in weights)
    tab = defaultdict(int)
    histogram = defaultdict(lambda: defaultdict(int))
    support = set()
    success_total = 0
    for a in product(range(1, n + 1), repeat=n):
        free = set(range(1, n + 1))
        lucky = displacement = 0
        for pref in a:
            free_after = [j for j in range(pref, n + 1) if j in free]
            if not free_after:
                break
            site = free_after[0]
            free.remove(site)
            lucky += int(pref == site)
            displacement += site - pref
        else:
            mult = 1
            for pref in a:
                mult *= weights[pref - 1]
            key = (lucky, displacement)
            tab[key] += mult
            success_total += mult
            support.add(key)
            histogram[key][tuple(a.count(j) for j in range(1, n + 1))] += 1
    return tab, support, success_total, histogram

expected_support = {
    1: {(1, 0)},
    2: {(1, 1), (2, 0)},
    3: {(1, 2), (1, 3), (2, 1), (2, 2), (3, 0)},
}
for n in (1, 2, 3):
    for weights in (tuple(1 for _ in range(n)), tuple(j+1 for j in range(n)), tuple(2 if j%2==0 else 1 for j in range(n))):
        t, support, total, _ = cells(n, weights)
        assert support == expected_support[n], (n, weights, support)
        for l in range(1, n+1):
            for lp in range(l+1, n+1):
                for d in range(n*(n-1)//2+1):
                    for dp in range(d+1, n*(n-1)//2+1):
                        assert t[l,d] * t[lp,dp] <= t[l,dp] * t[lp,d]

t, support, total, histories = cells(4, (2,1,2,1))
assert total == 776
expect = {(2,2):128, (2,3):80, (3,2):64, (3,3):48}
assert {key:t[key] for key in expect} == expect
expected_histograms = {
    (2,2): {(1,2,1,0):4, (2,0,2,0):6, (2,1,0,1):4},
    (2,3): {(1,3,0,0):4, (2,1,1,0):5, (3,0,0,1):4},
    (3,2): {(1,2,1,0):8, (2,1,0,1):8},
    (3,3): {(2,1,1,0):6},
}
for key, expected in expected_histograms.items():
    assert dict(histories[key]) == expected, (key, histories[key])
determinant = t[2,2] * t[3,3] - t[2,3] * t[3,2]
assert determinant == 1024
assert Fraction(t[3,3], t[2,3]) == Fraction(3, 5)
assert Fraction(t[3,2], t[2,2]) == Fraction(1, 2)
print('PASS: all n<=3 supports, exact four-car histograms, 776 total weight, positive determinant 1024')
