#!/usr/bin/env python3
"""Independent finite checks for fixed-cardinality edge-incidence traces.
Standard library only. Run: python verify.py
"""
from itertools import combinations
from math import comb


def edge_list(n):
    return list(combinations(range(n), 2))


def predicted(edges, mask, n, r):
    if mask == 0:
        return True
    degrees = [0] * n
    support = 0
    selected = []
    for j, (a, b) in enumerate(edges):
        if (mask >> j) & 1:
            degrees[a] += 1
            degrees[b] += 1
            support |= (1 << a) | (1 << b)
            selected.append((a, b))
    if n - support.bit_count() < r:
        return False
    # Each edge must have a degree-one endpoint; components are stars.
    if any(degrees[a] > 1 and degrees[b] > 1 for a, b in selected):
        return False
    seen = set()
    weight = 0
    for a, b in selected:
        if degrees[a] == 1 and degrees[b] == 1:
            key = ('e', min(a, b), max(a, b))
            w = 1
        else:
            hub = a if degrees[a] > 1 else b
            key = ('h', hub)
            w = max(1, degrees[hub] - 1)
        if key not in seen:
            seen.add(key)
            weight += w
    return weight <= r


def actual(edges, mask, cover_masks):
    # Incidence vector of each r-vertex set on all edges.
    if mask == 0:
        return True
    if 1 << mask.bit_count() > len(cover_masks):
        return False
    trace = {x & mask for x in cover_masks}
    return len(trace) == 1 << mask.bit_count()


def check(n, max_size=None):
    edges = edge_list(n)
    N = len(edges)
    for r in range(1, n + 1):
        covers = [sum(1 << j for j, (a, b) in enumerate(edges) if a in U or b in U)
                  for U in combinations(range(n), r)]
        masks = range(1 << N) if max_size is None else (
            sum(1 << j for j in I)
            for k in range(max_size + 1)
            for I in combinations(range(N), k))
        tested = 0
        maximum = 0
        for F in masks:
            got = actual(edges, F, covers)
            want = predicted(edges, F, n, r)
            assert got == want, (n, r, F, got, want)
            tested += 1
            if got:
                maximum = max(maximum, F.bit_count())
        expected_vc = max(0, min(2 * r, n - r - 1, n // 2))
        if max_size is None or max_size >= expected_vc:
            assert maximum == expected_vc, (n, r, maximum, expected_vc)
        print('CHECK', n, r, 'tested', tested, 'VC', maximum, 'PASS', flush=True)

for n in range(2, 7):
    check(n)
check(7, 4)
check(8, 4)
# Closed-neighborhood J(n,2) shattered-set count polynomial, from types.
for n in range(3, 9):
    edges = edge_list(n)
    covers = [sum(1 << j for j, (a, b) in enumerate(edges) if a in U or b in U)
              for U in combinations(range(n), 2)]
    counts = [0] * 5
    for k in range(5):
        for I in combinations(range(len(edges)), k):
            mask = sum(1 << i for i in I)
            counts[k] += actual(edges, mask, covers)
    target = [1,
              comb(n, 2) if n >= 4 else 0,
              3*comb(n,3)*(n>=5) + 3*comb(n,4)*(n>=6),
              4*comb(n,4)*(n>=6) + 30*comb(n,5)*(n>=7),
              90*comb(n,6)*(n>=8)]
    assert counts == target, (n, counts, target)
    print('TRIANGULAR', n, 'counts', counts, 'PASS', flush=True)
print('VERIFY_OK uniform_starforest=PASS exact_vc=PASS triangular_enumeration=PASS')
