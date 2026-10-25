#!/usr/bin/env python3
"""Exact rational-chain check for one ordered two-particle graph configuration space.

Uses only the Python standard library. The finite cubical model D(G,2) has
0-cells (v,w), v != w; 1-cells (e,v) and (v,e), v not incident to e;
and 2-cells (e,f), ordered disjoint edges. Its cellular boundaries are built
from the product boundary formula.
"""
from fractions import Fraction
from itertools import combinations


def rank_over_Q(matrix):
    """Exact Gaussian-elimination rank over Q for a rectangular integer matrix."""
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        for i in range(r + 1, m):
            if not a[i][c]:
                continue
            q = a[i][c] / p
            for j in range(c, n):
                a[i][j] -= q * a[r][j]
        r += 1
        if r == m:
            break
    return r


def main():
    # K_5 on 0,1,2,3,4, plus two new vertices 5,6 each adjacent to 0 and 1.
    vertices = list(range(7))
    edges = list(combinations(range(5), 2)) + [(0, 5), (1, 5), (0, 6), (1, 6)]
    edge_index = {e: i for i, e in enumerate(edges)}

    # Ordered configurations of distinct vertices.
    c0 = [(u, v) for u in vertices for v in vertices if u != v]
    c0_index = {cell: i for i, cell in enumerate(c0)}

    # Ordered 1-cells: first coordinate moves along an edge, or second does.
    c1 = []
    for ei, (u, v) in enumerate(edges):
        for w in vertices:
            if w not in (u, v):
                c1.append(("e_v", ei, w))
    for ei, (u, v) in enumerate(edges):
        for w in vertices:
            if w not in (u, v):
                c1.append(("v_e", w, ei))
    c1_index = {cell: i for i, cell in enumerate(c1)}

    # Ordered 2-cells e x f, where the closed edges have disjoint endpoints.
    c2 = []
    for i, (u, v) in enumerate(edges):
        for j, (x, y) in enumerate(edges):
            if i != j and len({u, v, x, y}) == 4:
                c2.append((i, j))

    d1 = [[0 for _ in c1] for _ in c0]
    for j, cell in enumerate(c1):
        typ, a, b = cell
        if typ == "e_v":
            u, v = edges[a]
            w = b
            d1[c0_index[(v, w)]][j] += 1
            d1[c0_index[(u, w)]][j] -= 1
        else:
            w, ei = a, b
            u, v = edges[ei]
            d1[c0_index[(w, v)]][j] += 1
            d1[c0_index[(w, u)]][j] -= 1

    d2 = [[0 for _ in c2] for _ in c1]
    for col, (i, j) in enumerate(c2):
        u, v = edges[i]
        x, y = edges[j]
        # d(e_i x e_j) = (v,e_j) - (u,e_j) - (e_i,y) + (e_i,x).
        d2[c1_index[("v_e", v, j)]][col] += 1
        d2[c1_index[("v_e", u, j)]][col] -= 1
        d2[c1_index[("e_v", i, y)]][col] -= 1
        d2[c1_index[("e_v", i, x)]][col] += 1

    r1 = rank_over_Q(d1)
    r2 = rank_over_Q(d2)
    assert r1 == len(c0) - 1, "the 1-skeleton should be connected"
    # Chain condition d1*d2 = 0, checked columnwise without external libraries.
    for col in range(len(c2)):
        for row in range(len(c0)):
            value = sum(d1[row][k] * d2[k][col] for k in range(len(c1)))
            assert value == 0, "boundary-of-boundary check failed"

    beta1_graph = len(edges) - len(vertices) + 1
    b1_config = len(c1) - r1 - r2
    target_rank = 2 * beta1_graph
    kernel_rank = b1_config - target_rank  # inclusion is onto for connected G != S^1

    print(f"|V|={len(vertices)}, |E|={len(edges)}, beta_1(G)={beta1_graph}")
    print(f"cell counts (C0,C1,C2)=({len(c0)},{len(c1)},{len(c2)})")
    print(f"ranks (d1,d2)=({r1},{r2})")
    print(f"dim_Q H1(F(G,2))={b1_config}")
    print(f"dim_Q H1(G x G)={target_rank}")
    print(f"dim_Q ker(H1(F(G,2))->H1(G x G))={kernel_rank}")
    assert (len(c0), len(c1), len(c2), r1, r2, b1_config, target_rank, kernel_rank) == (42, 140, 82, 41, 77, 22, 16, 6)


if __name__ == "__main__":
    main()
