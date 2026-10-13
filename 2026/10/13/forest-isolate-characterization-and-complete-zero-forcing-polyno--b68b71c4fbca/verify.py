#!/usr/bin/env python3
"""Exhaustive, direct small-instance checks for zero forcing sets of L(K_n)."""
from collections import Counter
from itertools import combinations
from math import comb


def tree_number(k):
    return 1 if k == 1 else k ** (k - 2)


def forest_distribution(n):
    """Counts labelled simple spanning forests by number of edges via component containing 0."""
    f = [{0: 1}]
    for m in range(1, n + 1):
        d = Counter()
        for k in range(1, m + 1):
            coeff = comb(m - 1, k - 1) * tree_number(k)
            for e, count in f[m-k].items():
                d[e+k-1] += coeff * count
        f.append(dict(d))
    return f


def expected_white(n):
    f = forest_distribution(n)
    d = Counter()
    for j in range(1, n+1):
        sign = 1 if (j & 1) else -1
        for e, count in f[n-j].items():
            d[e] += sign * comb(n, j) * count
    return {e: count for e,count in d.items() if count}


def structurally_forceable(n, edges, white_mask):
    parent = list(range(n))
    deg = [0] * n
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i, (a,b) in enumerate(edges):
        if (white_mask >> i) & 1:
            deg[a] += 1
            deg[b] += 1
            ra, rb = root(a), root(b)
            if ra == rb:
                return False
            parent[ra] = rb
    return 0 in deg


def directly_forceable(n, edges, white_mask):
    N = len(edges)
    neighbors = [0]*N
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            if i != j and (a==c or a==d or b==c or b==d):
                neighbors[i] |= 1<<j
    remaining = white_mask
    while remaining:
        black = ((1<<N)-1) ^ remaining
        forced = False
        while black:
            bit = black & -black
            i = bit.bit_length()-1
            white_neighbors = neighbors[i] & remaining
            if white_neighbors and (white_neighbors & (white_neighbors-1)) == 0:
                remaining ^= white_neighbors
                forced = True
                break
            black ^= bit
        if not forced:
            return False
    return True


def run():
    total_subsets = 0
    for n in range(3,7):
        edges = list(combinations(range(n),2))
        counter = Counter()
        for white in range(1<<len(edges)):
            actual = directly_forceable(n,edges,white)
            expected = structurally_forceable(n,edges,white)
            assert actual == expected, (n, white, actual, expected)
            if actual:
                counter[white.bit_count()] += 1
            total_subsets += 1
        formula = expected_white(n)
        assert dict(counter) == formula, (n,counter,formula)
        min_white = max(counter)
        assert min_white == n-2
        assert counter[min_white] == n*(n-1)**(n-3)
        max_failed_white_edge_min = min(3,(n+1)//2)
        assert max_failed_white_edge_min == min([w.bit_count() for w in range(1<<len(edges)) if not structurally_forceable(n,edges,w)])
        print('n=',n,'white_forest_isolated_coefficients=',dict(sorted(counter.items())), 'minimum_zero_forcing_size=',len(edges)-min_white)
    print('VERIFY_OK orders=3..6 all_subsets=',total_subsets,'forest_EGF_recurrence_checked=4')

if __name__=='__main__':
    run()
