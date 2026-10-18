#!/usr/bin/env python3
"""Finite checks for open rook-graph neighborhood first homology.

No external dependencies. Computational checks supplement an all-parameter proof.
"""
from itertools import combinations


def rank_mod(triangles, edge_index, p):
    pivots = {}
    for a, b, c in triangles:
        col = {edge_index[(b, c)]: 1, edge_index[(a, c)]: p - 1,
               edge_index[(a, b)]: 1}
        while col:
            lead = max(col)
            if lead not in pivots:
                inv = pow(col[lead], -1, p)
                pivots[lead] = {k: (v * inv) % p for k, v in col.items()}
                break
            factor = col[lead]
            for k, v in pivots[lead].items():
                rem = (col.get(k, 0) - factor * v) % p
                if rem:
                    col[k] = rem
                else:
                    col.pop(k, None)
    return len(pivots)


def check(m, n):
    facets = []
    for i in range(m):
        for j in range(n):
            row = [i*n+t for t in range(n) if t != j]
            col = [s*n+j for s in range(m) if s != i]
            facets.append(sorted(row + col))
    edges, triangles = set(), set()
    for f in facets:
        edges.update(combinations(f, 2))
        triangles.update(combinations(f, 3))
    edges = sorted(edges)
    triangles = sorted(triangles)
    assert len(edges) == m*n*(m*n-1)//2
    edge_index = {edge: k for k, edge in enumerate(edges)}
    diagonal = lambda u, v: int(u//n != v//n and u % n != v % n)
    for a, b, c in triangles:
        assert (diagonal(a,b)+diagonal(a,c)+diagonal(b,c))%2 == 0
    loop = (0, 1, n+1)
    assert (diagonal(loop[0],loop[1])+diagonal(loop[1],loop[2])+
            diagonal(loop[2],loop[0]))%2 == 1
    betti = []
    for p in (2,3,5):
        betti.append(len(edges)-(m*n-1)-rank_mod(triangles,edge_index,p))
    assert betti == [1,0,0], (m,n,betti)
    print(f'{m}x{n}: edges={len(edges)}, triangles={len(triangles)}, H1 mod (2,3,5)={betti}')


if __name__ == '__main__':
    for dims in [(4,4), (4,5), (5,5), (5,6), (6,6)]:
        check(*dims)
    print('VERIFY_OK')
