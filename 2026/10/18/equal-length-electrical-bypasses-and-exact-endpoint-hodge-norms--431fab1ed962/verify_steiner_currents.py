#!/usr/bin/env python3
"""Exact, dependency-free checks of incidence-graph electrical-flow formulas.

Run: python3 steiner_projector_stdlib.py
Only uses Python's standard library. This tests finitely many designs;
the all-design theorem is established separately by an analytic argument.
"""
from fractions import Fraction as F
from itertools import combinations, product


def inverse_rational(A):
    n = len(A)
    work = [[F(x) for x in row] + [F(int(i == j)) for j in range(n)]
            for i, row in enumerate(A)]
    for col in range(n):
        piv = next((i for i in range(col, n) if work[i][col]), None)
        assert piv is not None, 'grounded graph Laplacian is singular'
        work[col], work[piv] = work[piv], work[col]
        d = work[col][col]
        work[col] = [z / d for z in work[col]]
        for i in range(n):
            if i == col or not work[i][col]:
                continue
            a = work[i][col]
            work[i] = [x - a * y for x, y in zip(work[i], work[col])]
    return [row[n:] for row in work]


def pairs(v):
    return v, [tuple(b) for b in combinations(range(v), 2)], 2


def affine(q):
    assert q in (2, 3, 5, 7)
    pts = list(product(range(q), repeat=2))
    blocks = []
    for slope in range(q):
        for t in range(q):
            blocks.append(tuple(i for i, (x, y) in enumerate(pts)
                                if (y - slope * x) % q == t))
    for t in range(q):
        blocks.append(tuple(i for i, (x, y) in enumerate(pts) if x == t))
    return len(pts), blocks, q


def projective(q):
    assert q in (2, 3, 5)
    def normal(a):
        a = tuple(z % q for z in a)
        s = next(z for z in a if z)
        inv = pow(s, -1, q)
        return tuple((inv * z) % q for z in a)
    pts = sorted({normal(a) for a in product(range(q), repeat=3) if any(a)})
    blocks = [tuple(i for i, a in enumerate(pts)
                    if sum(x * y for x, y in zip(a, l)) % q == 0)
              for l in pts]
    return len(pts), blocks, q + 1


def check(label, design):
    v, blocks, k = design
    r = F(v - 1, k - 1)
    assert r.denominator == 1
    assert all(len(block) == k for block in blocks)
    block_of_pair = {}
    for j, block in enumerate(blocks):
        for pair in combinations(block, 2):
            key = tuple(sorted(pair))
            assert key not in block_of_pair
            block_of_pair[key] = j
    assert len(block_of_pair) == v * (v - 1) // 2
    b = len(blocks)
    assert b * k == v * int(r)
    edges = [(p, v + j) for j, block in enumerate(blocks) for p in block]
    idx = {e: i for i, e in enumerate(edges)}
    m, nv = len(edges), v + b
    # Ground the last graph vertex and invert its Laplacian by exact fractions.
    L = [[0] * (nv - 1) for _ in range(nv - 1)]
    for u, w in edges:
        if u < nv - 1: L[u][u] += 1
        if w < nv - 1: L[w][w] += 1
        if u < nv - 1 and w < nv - 1:
            L[u][w] -= 1
            L[w][u] -= 1
    inv = inverse_rational(L)
    endpoints = [[(z, s) for z, s in ((u, 1), (w, -1)) if z < nv - 1]
                 for u, w in edges]
    P = [[sum(F(eps * eta) * inv[u][w]
              for u, eps in endpoints[i] for w, eta in endpoints[j])
          for j in range(m)] for i in range(m)]
    rho = F(k - 1, v) + F(1, k)
    qnorm, cnorm = 5 - 4 * rho, 6 * (1 - rho)
    assert all(P[i][j] == P[j][i] for i in range(m) for j in range(m))
    assert all(P[j][j] == rho for j in range(m))
    assert all(sum(abs(P[i][j]) for i in range(m)) == qnorm for j in range(m))
    assert all(sum(abs(F(int(i == j)) - P[i][j]) for i in range(m)) == cnorm
               for j in range(m))
    if m <= 52:
        for i in range(m):
            for j in range(m):
                assert sum(P[i][u] * P[u][j] for u in range(m)) == P[i][j]
    unit = F(1, k * v)
    paths_checked = 0
    for col, (src, root_v) in enumerate(edges):
        root = root_v - v
        flow = [F(0) for _ in range(m)]
        flow[col] += rho
        paths = 0
        for j, B1 in enumerate(blocks):
            if j == root or src not in B1: continue
            for x in B1:
                if x == src: continue
                assert x not in blocks[root]
                for y in blocks[root]:
                    if y == src: continue
                    j2 = block_of_pair[tuple(sorted((x, y)))]
                    assert j2 not in (root, j)
                    for e, sign in [((src, v + j), 1), ((x, v + j), -1),
                                    ((x, v + j2), 1), ((y, v + j2), -1),
                                    ((y, v + root), 1)]:
                        flow[idx[e]] += sign * unit
                    paths += 1
        assert paths == (v - k) * (k - 1)
        assert flow == [P[i][col] for i in range(m)]
        paths_checked += paths
    print('PASS', label, 'v', v, 'k', k, 'edges', m,
          'Q', qnorm, 'C', cnorm, 'current_paths', paths_checked)
    return m, paths_checked


if __name__ == '__main__':
    records = [('pair_5', pairs(5)), ('projective_2', projective(2)),
               ('affine_3', affine(3)), ('projective_3', projective(3)),
               ('affine_5', affine(5))]
    counts = [check(label, d) for label, d in records]
    print('VERIFIED', len(records), 'designs;', sum(n for n, _ in counts),
          'edge columns;', sum(z for _, z in counts), 'length-five bypass paths')
