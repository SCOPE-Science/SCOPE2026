#!/usr/bin/env python3
"""Independent finite checks for alternating-spoke directed wheels.
Uses direct subset testing and GF(2) boundary elimination (not the proof).
"""
from collections import Counter, defaultdict
from itertools import combinations


def arcs(n):
    # Rim vertices 0,...,n-1; hub n.  n must be positive and even.
    return [(i, (i+1) % n) for i in range(n)] + [
        ((i, n) if i % 2 == 0 else (n, i)) for i in range(n)]


def is_multipath(mask, edges, n):
    outgoing = [-1] * (n + 1)
    incoming = [-1] * (n + 1)
    for k, (u, v) in enumerate(edges):
        if not ((mask >> k) & 1):
            continue
        if outgoing[u] != -1 or incoming[v] != -1:
            return False
        outgoing[u] = v
        incoming[v] = u
    for start in range(n + 1):
        seen = set()
        x = start
        while x != -1:
            if x in seen:
                return False
            seen.add(x)
            x = outgoing[x]
    return True


def all_faces(n):
    es = arcs(n)
    return es, {mask for mask in range(1 << len(es)) if is_multipath(mask, es, n)}


def link_expected(n, i, j, rim_mask):
    assert i % 2 == 0 and j % 2 == 1
    # Arc v_i -> hub, then hub -> v_j.
    forbidden = (1 << i) | (1 << ((j - 1) % n))
    if rim_mask & forbidden:
        return False
    t = j
    path_mask = 0
    while t != i:
        path_mask |= (1 << t)
        t = (t + 1) % n
    return rim_mask & path_mask != path_mask


def betti_mod2(faces):
    levels = defaultdict(list)
    for s in faces:
        levels[s.bit_count() - 1].append(s)
    ranks = defaultdict(int)
    for d in sorted(levels):
        if d <= 0:
            continue
        rows = {s: k for k, s in enumerate(levels[d - 1])}
        pivots = {}
        for simplex in levels[d]:
            boundary = 0
            b = simplex
            while b:
                low = b & -b
                b ^= low
                boundary ^= 1 << rows[simplex ^ low]
            while boundary:
                k = boundary.bit_length() - 1
                if k not in pivots:
                    pivots[k] = boundary
                    break
                boundary ^= pivots[k]
        ranks[d] = len(pivots)
    return {d: len(levels[d]) - ranks[d] - ranks[d + 1]
            for d in sorted(levels) if d >= 0}


def check(n):
    es, fs = all_faces(n)
    rim_full = (1 << n) - 1
    assert rim_full not in fs
    # One-spoke links are simplices missing their unique forbidden even edge.
    for i in range(n):
        spoke_bit = 1 << (n + i)
        miss = i if i % 2 == 0 else (i - 1)
        for rim in range(1 << n):
            assert ((rim | spoke_bit) in fs) == (rim & (1 << miss) == 0)
    # Two-spoke links: degree constraints and the unique possible directed cycle.
    special = 0
    for i in range(0, n, 2):
        for j in range(1, n, 2):
            pair = (1 << (n + i)) | (1 << (n + j))
            for rim in range(1 << n):
                assert ((rim | pair) in fs) == link_expected(n, i, j, rim)
            if j == (i + 1) % n:
                special += 1
    assert special == n // 2
    # The simplicial retraction fixes rim arcs, sends all spokes to e_1.
    for s in fs:
        if s & ~rim_full:
            image = (s & rim_full) | (1 << 1)
        else:
            image = s
        assert image in fs and image <= rim_full
    assert all(sum(1 for i in range(n) if (s >> (n + i)) & 1) <= 2 for s in fs)
    # Homology calculated independently from a full, exact GF(2) boundary matrix.
    betti = betti_mod2(fs)
    assert betti.get(0) == 1
    expected = {n - 2: 1, n - 1: n // 2}
    assert {d:r for d,r in betti.items() if d >= 1 and r} == expected, (n, betti)
    ordinary_euler = sum((-1)**(s.bit_count()-1) for s in fs if s)
    assert ordinary_euler == 2 - n // 2
    print('PASS',n,'arcs',len(es),'faces',len(fs)-1,'reduced_betti',expected,'Euler',ordinary_euler)

if __name__ == '__main__':
    for n in (4, 6, 8, 10):
        check(n)
