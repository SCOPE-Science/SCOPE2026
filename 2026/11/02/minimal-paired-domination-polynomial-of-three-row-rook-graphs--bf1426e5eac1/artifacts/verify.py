#!/usr/bin/env python3
"""Independent graph-level verification of the minimal paired-domination enumerator.

Only Python 3 standard library is needed. The graph is built from its
rook adjacency, and perfect matchings are tested by backtracking.
"""
from collections import Counter
from functools import lru_cache
from math import comb


def expected(n):
    assert n >= 3
    counts = Counter()
    counts[4] += 3 * n * (n - 1) * (n + 2) // 2
    if n >= 6:
        counts[6] += comb(n, 2) * comb(n - 2, 2) * comb(n - 4, 2)
    if n % 2:
        counts[n + 1] += 3 * n * 2 ** (n - 1)
    else:
        counts[n] += 3 * (2 ** (n - 1) - 1)
    return counts


def graph_count(n):
    order = 3*n
    adj = [0] * order
    for u in range(order):
        r, c = divmod(u, n)
        for v in range(order):
            if u != v and (r == v//n or c == v%n):
                adj[u] |= 1 << v

    @lru_cache(None)
    def perfect(mask):
        if mask == 0:
            return True
        u = (mask & -mask).bit_length()-1
        possible = adj[u] & mask
        while possible:
            vbit = possible & -possible
            if perfect(mask ^ (1 << u) ^ vbit):
                return True
            possible ^= vbit
        return False

    def dominates(mask):
        for u in range(order):
            if not (mask >> u & 1) and not (adj[u] & mask):
                return False
        return True

    def shape_check(mask):
        if n == 2:
            return mask.bit_count() == 2
        row_sets = []
        for r in range(3):
            row_sets.append({c for c in range(n) if (mask >> (r*n+c)) & 1})
        occupied = sum(bool(x) for x in row_sets)
        if occupied == 3:
            if mask.bit_count() == 4:
                return True
            if mask.bit_count() == 6:
                return (all(len(x) == 2 for x in row_sets)
                        and sum(len(x) for x in row_sets) == len(set.union(*row_sets)))
            return False
        colcounts = [sum(c in x for x in row_sets) for c in range(n)]
        if any(t == 0 for t in colcounts):
            return False
        if n % 2 == 0:
            return (all(t == 1 for t in colcounts)
                    and all(len(x) % 2 == 0 for x in row_sets))
        return sorted(colcounts) == [1] * (n-1) + [2]

    seen = bytearray(1 << order)
    counts = Counter()
    tested = 0
    for mask in range(1, 1 << order):
        tested += 1
        subvalid = False
        rest = mask
        while rest:
            bit = rest & -rest
            if seen[mask ^ bit]:
                subvalid = True
                break
            rest ^= bit
        is_valid = mask.bit_count() % 2 == 0 and dominates(mask) and perfect(mask)
        if is_valid and not subvalid:
            assert shape_check(mask), (n, mask, 'unexpected minimal shape')
            counts[mask.bit_count()] += 1
        seen[mask] = subvalid or is_valid
    target = Counter({2: 3}) if n == 2 else expected(n)
    assert counts == target, (n, dict(counts), dict(target))
    return tested, dict(sorted(counts.items()))


def main():
    subsets = 0
    for n in range(2, 8):
        tested, counts = graph_count(n)
        subsets += tested
        print('n=%d subsets=%d minimal_counts=%s' % (n, tested, counts))
    for n in range(3, 101):
        counts = expected(n)
        assert sum(counts.values()) > 0
        if n >= 7:
            assert sorted(counts) == sorted(set((4, 6, 2 * ((n+1)//2))))
    print('VERIFY_OK graph_orders=6 direct_vertex_subsets=%d arithmetic_orders=98' % subsets)

if __name__ == '__main__':
    main()
