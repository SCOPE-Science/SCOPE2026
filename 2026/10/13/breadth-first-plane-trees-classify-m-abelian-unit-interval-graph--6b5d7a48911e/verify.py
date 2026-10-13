#!/usr/bin/env python3
"""Independent finite checks for a structural count of naturally labeled unit interval graphs."""
from collections import Counter
from math import comb

def parent_lists(n):
    # Area-sequence equivalents: 0=p(1)<=p(2)<=...<=p(n), p(i)<i.
    def rec(i, parents):
        if i > n:
            yield (0,) + tuple(parents)
            return
        for par in range(parents[-1] if parents else 0, i):
            yield from rec(i + 1, parents + [par])
    yield from rec(1, [])

def graph(n, p):
    adj = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(p[i] + 1, i):
            adj[i] |= 1 << (j - 1)
            adj[j] |= 1 << (i - 1)
    return adj

def independent_number_brute(n, adj):
    best = 0
    for subset in range(1 << n):
        if subset.bit_count() <= best:
            continue
        ok = True
        for v in range(1, n + 1):
            if subset & (1 << (v - 1)) and adj[v] & subset:
                ok = False
                break
        if ok:
            best = subset.bit_count()
    return best

def clique_cover_brute(n, adj):
    # Check existence of consecutive clique blocks by independent DP (not tree recursion).
    d = [n + 1] * (n + 1)
    d[0] = 0
    for hi in range(1, n + 1):
        for lo in range(1, hi + 1):
            if all(adj[v] & (1 << (u - 1))
                   for v in range(lo + 1, hi + 1) for u in range(lo, v)):
                d[hi] = min(d[hi], d[lo - 1] + 1)
    return d[n]

def dyck_with_max_height(n, h):
    # Independent walk recursion, not using graph enumeration/tree construction.
    states = {0: 1}
    for _ in range(2 * n):
        after = {}
        for altitude, count in states.items():
            if altitude + 1 <= h:
                after[altitude + 1] = after.get(altitude + 1, 0) + count
            if altitude > 0:
                after[altitude - 1] = after.get(altitude - 1, 0) + count
        states = after
    return states.get(0, 0)

def rational_coefficient_q(h, nmax):
    # F_0=1; F_h =1/(1-z F_{h-1}), by composition of plane trees.
    s = [1] + [0] * nmax
    for _ in range(h):
        nxt = [0] * (nmax + 1)
        nxt[0] = 1
        for n in range(1, nmax + 1):
            nxt[n] = sum(s[j] * nxt[n-1-j] for j in range(n))
        s = nxt
    return s

def main():
    totals = {}
    max_n = 9
    for n in range(1, max_n + 1):
        alpha_distribution = Counter()
        tested = 0
        for p in parent_lists(n):
            assert len(p) == n + 1
            assert p[1] == 0
            assert all(0 <= p[i] < i for i in range(1, n + 1))
            assert all(p[i] <= p[i+1] for i in range(1, n))
            depths = [0] * (n + 1)
            for i in range(1, n + 1):
                depths[i] = depths[p[i]] + 1
            h = max(depths)
            assert h == depths[n]
            edges = graph(n, p)
            alpha = independent_number_brute(n, edges)
            cover = clique_cover_brute(n, edges)
            assert alpha == cover == h, (n, p, h, alpha, cover)
            # Breadth-first child listing reconstructs the same parent labels.
            kids = [[i for i in range(1, n + 1) if p[i] == j] for j in range(n + 1)]
            bfs = [0]
            for v in bfs:
                bfs.extend(kids[v])
            assert bfs == list(range(n + 1)), (n, p, bfs)
            alpha_distribution[h] += 1
            tested += 1
        assert tested == comb(2*n, n) // (n + 1)
        assert sum(alpha_distribution.values()) == tested
        for h in range(1, n + 1):
            summed = sum(c for depth,c in alpha_distribution.items() if depth <= h)
            assert summed == dyck_with_max_height(n, h)
        for m in range(1, n + 1):
            summed = sum(c for depth,c in alpha_distribution.items() if depth <= m+1)
            assert summed == rational_coefficient_q(m+1, n)[n]
            if m == 1:
                assert summed == 2 ** (n-1)
            if m == 2:
                f0,f1=0,1
                for _ in range(2*n-1):
                    f0,f1=f1,f0+f1
                assert summed == f0
            if m == 3:
                assert summed == (3 ** (n-1) + 1) // 2
        totals[n] = (tested, [alpha_distribution[h] for h in range(1, n + 1)])
    print('Graph-to-tree and converse BFS reconstruction: PASS')
    print('Brute-force graph independent number: PASS')
    print('Independent contiguous-clique dynamic program: PASS')
    print('Bounded Dyck excursions and continued fraction coefficient: PASS')
    print('Closed formulas at m=1,2,3: PASS')
    print('n  Catalan_n  counts at exact independence number 1..n')
    for n,(total,distribution) in totals.items():
        print(n, total, *distribution)

if __name__ == '__main__':
    main()
