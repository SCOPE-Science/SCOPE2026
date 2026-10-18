#!/usr/bin/env python3
"""Exact finite census of minimum circular string attractors of Fibonacci words.

A position is zero-indexed. No external packages or downloaded data required.
"""
from collections import deque
from hashlib import sha256


def fibonacci_words(top):
    words = ['0', '01']
    while len(words) <= top:
        words.append(words[-1] + words[-2])
    return words


def exhaustive_edges(word):
    """Filter ALL position pairs by EVERY circular factor length 1..N.

    A factor length ell occurs at one of N cyclic start sites.  The bitset
    at position p records the distinct length-ell factors with at least one
    occurrence whose interval contains p modulo N.  A pair is admissible
    at length ell iff the bitwise union covers all factor IDs for ell.
    """
    n = len(word)
    periodic = word + word
    surviving = [(i, j) for i in range(n) for j in range(i + 1, n)]
    critical = []
    total_factors = 0
    for ell in range(1, n + 1):
        identifiers = {}
        for start in range(n):
            factor = periodic[start : start + ell]
            if factor not in identifiers:
                identifiers[factor] = len(identifiers)
        total_factors += len(identifiers)
        bits = [0] * n
        for start in range(n):
            bit = 1 << identifiers[periodic[start : start + ell]]
            end = start + ell
            for position in range(start, end):
                p = position if position < n else position - n
                bits[p] |= bit
        full = (1 << len(identifiers)) - 1
        before = len(surviving)
        surviving = [(i, j) for i, j in surviving if (bits[i] | bits[j]) == full]
        if len(surviving) < before:
            critical.append((ell, before - len(surviving)))
    return surviving, critical, total_factors


def complete_bipartite_partition(edges):
    neighbors = {}
    for i, j in edges:
        neighbors.setdefault(i, set()).add(j)
        neighbors.setdefault(j, set()).add(i)
    if not neighbors:
        return [], []
    color = {}
    for start in neighbors:
        if start in color:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in neighbors[u]:
                if v in color:
                    assert color[v] != color[u], 'nonbipartite graph'
                else:
                    color[v] = color[u] ^ 1
                    queue.append(v)
    assert len(color) == len(neighbors)
    A = sorted(p for p in color if color[p] == 0)
    B = sorted(p for p in color if color[p] == 1)
    assert len(edges) == len(A) * len(B), 'graph not complete bipartite'
    assert set(edges) == {(min(a, b), max(a, b)) for a in A for b in B}
    return A, B


def main():
    words = fibonacci_words(12)
    for level in range(1, 13):
        w = words[level]
        edges, critical, nfactor = exhaustive_edges(w)
        A, B = complete_bipartite_partition(edges)
        assert len(edges) == 1 << (level - 1), (level, len(edges))
        assert len(A) * len(B) == len(edges)
        assert sorted((len(A), len(B))) == sorted((1 << (level // 2), 1 << ((level - 1) // 2)))
        # The factor of length one enforces the two letter classes.
        assert {w[a] for a in A} == {'0'} or {w[a] for a in A} == {'1'}
        assert {w[b] for b in B} == {'0'} or {w[b] for b in B} == {'1'}
        assert w[A[0]] != w[B[0]]
        # Each length-ell circular factor is counted exactly once.
        if level >= 2:
            assert nfactor == len(w) * (len(w) + 1) // 2 + len(w) - 1
        # The stage values are constraints that really remove pairs,
        # NOT proof of a statement extending beyond the finite range.
        crit_lengths = [t for t, _ in critical]
        assert crit_lengths == [len(words[j]) for j in range(level - 1)], (level, crit_lengths)
        digest = sha256(';'.join(f'{i}:{j}' for i,j in edges).encode()).hexdigest()[:16]
        print('level=%d length=%d circular_factors=%d minima=%d parts=%d,%d critical=%s digest=%s' % (
            level, len(w), nfactor, len(edges), len(A), len(B), ','.join(map(str,crit_lengths)), digest))
        if level == 12:
            print('level12_part_A_0based=' + ','.join(map(str,A)))
            print('level12_part_B_0based=' + ','.join(map(str,B)))
    print('ALL FINITE ENUMERATIONS PASS')


if __name__ == '__main__':
    main()
