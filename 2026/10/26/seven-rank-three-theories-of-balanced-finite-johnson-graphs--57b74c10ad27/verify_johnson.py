#!/usr/bin/env python3
"""Finite checks for the Johnson-graph three-round classification.
This program is a finite corroboration, not a proof of the infinite claim.
"""
from itertools import combinations
from collections import defaultdict


def profile(n, k):
    assert 1 <= k <= n // 2
    vertices = list(map(frozenset, combinations(range(n), k)))
    first = frozenset(range(k))
    edge_types, nonedge_types = set(), set()
    representatives = [frozenset(list(range(t)) + list(range(k,2*k-t)))
                       for t in range(max(0,2*k-n), k)]
    for second in representatives:
        is_edge = len(first & second) == k-1
        mask = 0
        for third in vertices:
            if third == first or third == second:
                continue
            u = int(len(third & first) == k-1)
            v = int(len(third & second) == k-1)
            mask |= 1 << (2*u+v)
        (edge_types if is_edge else nonedge_types).add(mask)
    return (tuple(sorted(edge_types)), tuple(sorted(nonedge_types)))


def predicted(n, k):
    if k == 1:
        return ((0,), ()) if n == 2 else ((8,), ())
    if k == 2:
        if n == 4: return ((14,), (8,))
        if n == 5: return ((15,), (14,))
        return ((15,), (15,))
    if (n,k) == (6,3): return ((15,), (6,15))
    return ((15,), (7,15))


def check():
    tested = 0
    by_type = defaultdict(list)
    for k in range(1,9):
        for n in range(2*k, min(2*k+5,19)):
            if k >= 7 and n > 2*k+1: continue
            got = profile(n,k)
            want = predicted(n,k)
            assert got == want, (n,k,got,want)
            tested += 1
            by_type[got].append((n,k))
    assert len(by_type) == 7, len(by_type)
    for idx, (code, pairs) in enumerate(sorted(by_type.items(), key=lambda v:v[1][0]),1):
        print(f'class {idx}: edge-masks={code[0]}, nonedge-masks={code[1]}; samples={pairs}')
    print(f'PASS: {tested} directly enumerated parameter pairs; 7 distinct rank-three profiles.')


if __name__ == '__main__':
    check()
