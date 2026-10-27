#!/usr/bin/env python3
"""Independent finite checks for stable-extension diversity on leaf-paired symmetric attacks.

Run: python3 checker.py. Uses Python standard library only.
"""
from collections import Counter
from itertools import combinations
import random


def edge_masks(n, mask):
    edges = list(combinations(range(n), 2))
    return {e for bit, e in enumerate(edges) if (mask >> bit) & 1}


def independent(mask, edges):
    return all(not ((mask >> u) & 1 and (mask >> v) & 1) for u, v in edges)


def stable_extensions(n, edges):
    # In an undirected graph with symmetric attacks, stable means
    # independent and every excluded vertex has an included neighbor.
    N = 2*n
    adj = [0]*N
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for u in range(n):
        v = n+u
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    out = []
    for M in range(1 << N):
        if any((M >> v) & 1 and (adj[v] & M) for v in range(N)):
            continue
        if any(not ((M >> v) & 1) and not (adj[v] & M) for v in range(N)):
            continue
        out.append(M)
    return out


def center_to_full(n, C):
    return C | (sum(1 << (n+v) for v in range(n) if not ((C >> v) & 1)))


def direct_polynomial(n, edges):
    sts = stable_extensions(n, edges)
    return Counter((a ^ b).bit_count() for a in sts for b in sts), sts


def formula_polynomial(n, edges):
    out = Counter()
    full = (1 << n) - 1
    for S in range(1 << n):
        # Count proper 2-colorings of the induced subgraph; zero if nonbipartite.
        colors = [-1] * n
        comp = 0
        bip = True
        neighbors = [set() for _ in range(n)]
        for u, v in edges:
            if (S >> u) & 1 and (S >> v) & 1:
                neighbors[u].add(v)
                neighbors[v].add(u)
        for u in range(n):
            if ((S >> u) & 1) and colors[u] == -1:
                comp += 1
                colors[u] = 0
                stack = [u]
                while stack:
                    v = stack.pop()
                    for w in neighbors[v]:
                        if colors[w] == -1:
                            colors[w] = 1 - colors[v]
                            stack.append(w)
                        elif colors[w] == colors[v]:
                            bip = False
        if not bip:
            continue
        adjacent = 0
        for u, v in edges:
            if ((S >> u) & 1) and not ((S >> v) & 1):
                adjacent |= 1 << v
            if ((S >> v) & 1) and not ((S >> u) & 1):
                adjacent |= 1 << u
        T_universe = full & ~(S | adjacent)
        T = T_universe
        count = 0
        while True:
            if independent(T, edges):
                count += 1
            if T == 0:
                break
            T = (T-1) & T_universe
        out[2*S.bit_count()] += (2**comp)*count
    return out


def expected_leading(n, edges):
    # Exhaustive independent verification of the OCT expression.
    best = -1
    factor = 0
    for S in range(1 << n):
        # Independently enumerate 2-colourings.
        c = 0
        for I in range(1 << n):
            if I & ~S:
                continue
            J = S ^ I
            if independent(I, edges) and independent(J, edges):
                c += 1
        if c:
            s = S.bit_count()
            if s > best:
                best, factor = s, c
            elif s == best:
                factor += c
    return 2*best, factor


def check_graph(n, edges):
    actual, sets = direct_polynomial(n, edges)
    centers = {center_to_full(n, I) for I in range(1 << n) if independent(I, edges)}
    assert centers == set(sets), ('normal form failed', n, edges)
    predicted = formula_polynomial(n, edges)
    assert actual == predicted, ('distance polynomial failed', n, edges, actual, predicted)
    top_deg, top_coeff = expected_leading(n, edges)
    assert max(actual) == top_deg and actual[top_deg] == top_coeff, ('leading term failed', n, edges)
    assert actual[0] == len(sets)
    assert set(actual) <= set(range(0, 2*n+1, 2))
    return len(sets)


def main():
    ngraphs = 0
    for n in range(1, 6):
        total = 1 << (n*(n-1)//2)
        for mask in range(total):
            check_graph(n, edge_masks(n, mask))
        ngraphs += total
        print(f'all labelled graphs on {n} vertices: {total} checked')
    rng = random.Random(201626)
    edges6 = list(combinations(range(6),2))
    for _ in range(20):
        e = {edge for edge in edges6 if rng.randrange(2)}
        check_graph(6, e)
    print(f'20 extra six-vertex tests; {ngraphs+20} graphs checked in total')


if __name__ == '__main__':
    main()
