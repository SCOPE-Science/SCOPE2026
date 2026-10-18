#!/usr/bin/env python3
"""Exact small-network service-capacity test for pairwise-identical plant-failure laws."""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import comb


def connected(rows, b):
    # Alternating bipartite BFS, represented by exact integer bitsets.
    a = len(rows)
    seen_plants, seen_pollinators = 1, 0
    while True:
        new_poll = seen_pollinators
        for i, row in enumerate(rows):
            if seen_plants >> i & 1:
                new_poll |= row
        new_plants = seen_plants
        for i, row in enumerate(rows):
            if row & new_poll:
                new_plants |= 1 << i
        if (new_plants, new_poll) == (seen_plants, seen_pollinators):
            break
        seen_plants, seen_pollinators = new_plants, new_poll
    return seen_plants == (1 << a) - 1 and seen_pollinators == (1 << b) - 1


def signature(rows, b):
    deg = tuple(row.bit_count() for row in rows)
    pair = tuple((rows[i] & rows[j]).bit_count()
                 for i in range(len(rows)) for j in range(i+1, len(rows)))
    col = tuple(sorted(sum(bool(row & (1<<j)) for row in rows) for j in range(b)))
    return deg + pair + col


def matching(rows, survivors):
    # Independent DP on the set of pollinators already committed to service.
    possibilities = {0}
    for row in rows:
        options = list(possibilities)
        for used in possibilities:
            candidates = (row & survivors) & ~used
            while candidates:
                bit = candidates & -candidates
                options.append(used | bit)
                candidates -= bit
        possibilities = set(options)
    return max(used.bit_count() for used in possibilities)


def profile(rows, b):
    h = [0]*(b+1)
    for S in range(1<<b):
        h[S.bit_count()] += matching(rows, S)
    return tuple(h)


def check_all(a, b):
    previous = {}
    connected_count = 0
    compared = 0
    for rows in product(range(1, 1<<b), repeat=a):
        if not connected(rows, b):
            continue
        connected_count += 1
        key = signature(rows, b)
        h = profile(rows, b)
        if key in previous:
            compared += 1
            assert previous[key] == h, (a,b,key,previous[key],h,rows)
        else:
            previous[key] = h
    return connected_count,len(previous),compared


def main():
    for a in range(1, 8):
        for b in range(1, 9-a):
            if a+b > 8: continue
            n,g,c = check_all(a,b)
            print(f'plants={a} pollinators={b} connected={n} signatures={g} repeat_comparisons={c}')
    G = (25,6,5,3)
    H = (22,9,5,3)
    assert connected(G,5) and connected(H,5)
    assert signature(G,5) == signature(H,5)
    hG,hH=profile(G,5),profile(H,5)
    assert hG == (0,5,19,27,17,4),hG
    assert hH == (0,5,20,30,20,4),hH
    diffs=[]
    for S in range(32):
        d = matching(H,S)-matching(G,S)
        assert 0 <= d <= 1
        if d: diffs.append(tuple(i for i in range(5) if S>>i&1))
    assert len(diffs)==7, diffs
    assert sorted(diffs)==sorted([(3,4),(0,3,4),(1,3,4),(2,3,4),
                                      (0,1,3,4),(0,2,3,4),(1,2,3,4)])
    print('G: rowmasks',G,'H: rowmasks',H)
    print('G profile',hG,'H profile',hH)
    print('all seven strictly improved survival subsets:',diffs)
    print('difference polynomial = q*(1-q)^2*(3-3*q+q^2) > 0 on (0,1)')
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    main()
