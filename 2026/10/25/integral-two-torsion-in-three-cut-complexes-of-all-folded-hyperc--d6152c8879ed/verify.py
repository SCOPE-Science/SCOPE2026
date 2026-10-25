#!/usr/bin/env python3
"""Standalone finite checks for 3-cut Alexander duals of folded cubes.

No external dependencies. The infinite-family theorem uses the written
cubical-collapse and projective-space argument, not extrapolation.
"""
from itertools import combinations
from math import comb


def ranks_mod_p(columns, p):
    """Rank of sparse integer columns modulo the prime p."""
    pivots = {}
    for original in columns:
        v = {k: c % p for k, c in original.items() if c % p}
        while v:
            j = min(v)
            if j not in pivots:
                unit = pow(v[j], -1, p)
                pivots[j] = {k: (c * unit) % p for k, c in v.items()}
                break
            fac = v[j]
            for k, c in pivots[j].items():
                val = (v.get(k, 0) - fac * c) % p
                if val:
                    v[k] = val
                else:
                    v.pop(k, None)
    return len(pivots)


def verify(n):
    assert 5 <= n <= 7
    mask = (1 << n) - 1
    rep = lambda z: min(z, z ^ mask)
    verts = sorted({rep(x) for x in range(1 << n)})
    N = 1 << (n-1)
    assert len(verts) == N
    pos = {v: i for i, v in enumerate(verts)}
    adj = [set() for _ in verts]
    for i, v in enumerate(verts):
        for bit in range(n):
            adj[i].add(pos[rep(v ^ (1 << bit))])
    assert all(len(a) == n for a in adj)
    assert all(i in adj[j] for i, ns in enumerate(adj) for j in ns)
    edges_graph = {tuple(sorted((i,j))) for i, ns in enumerate(adj) for j in ns}
    assert len(edges_graph) == N*n//2
    dist2 = {}
    for i, j in combinations(range(N), 2):
        common = adj[i] & adj[j]
        if j in adj[i]:
            assert not common, 'triangle detected'
        elif common:
            assert len(common) == 2, 'non-unique square pair'
            dist2[(i,j)] = tuple(sorted(common))
    assert len(dist2) == N*comb(n,2)//2
    squares = {tuple(sorted((i,j,a,b))) for (i,j),(a,b) in dist2.items()}
    q = N*comb(n,2)//4
    assert len(squares) == q
    # All two-path triples, exactly one square tetrahedron per triple.
    triangles = {tuple(sorted((a,v,b))) for v in range(N) for a,b in combinations(sorted(adj[v]),2)}
    assert len(triangles) == N*comb(n,2)
    tetra = {}
    for sq in squares:
        for tri in combinations(sq,3):
            assert tri in triangles
            tetra.setdefault(tri, []).append(sq)
    assert len(tetra) == len(triangles)
    assert all(len(ls)==1 for ls in tetra.values())
    # Every four-face must be such a square (the criterion is checked
    # directly for the n=5/6 cases; for 7, the exhaustive same test also fits).
    for quad in combinations(range(N),4):
        if all(tri in triangles for tri in combinations(quad,3)):
            assert quad in squares
    full_edges = set(combinations(range(N),2))
    remaining_edges = full_edges.copy()
    remaining_triangles = triangles.copy()
    remaining_tetra = squares.copy()
    # Two certified free-face collapses per square. All tests below are
    # performed on the changing simplicial complex itself.
    for sq in sorted(squares):
        diagonals = [edge for edge in combinations(sq,2) if edge not in edges_graph]
        assert len(diagonals) == 2
        diag = diagonals[0]
        ends = [v for v in sq if v not in diag]
        t = tuple(sorted((*diag, ends[0])))
        t2 = tuple(sorted((*diag, ends[1])))
        assert t in remaining_triangles
        assert sum(t in combinations(other,3) for other in remaining_tetra) == 1
        remaining_tetra.remove(sq)
        remaining_triangles.remove(t)
        assert diag in remaining_edges and t2 in remaining_triangles
        assert sum(set(diag).issubset(tri) for tri in remaining_triangles) == 1
        remaining_triangles.remove(t2)
        remaining_edges.remove(diag)
    assert not remaining_tetra
    assert len(remaining_triangles)==2*q
    far = len(full_edges)-len(edges_graph)-len(dist2)
    assert len(remaining_edges)==len(edges_graph)+q+far
    assert all(any(edge in edges_graph for edge in combinations(tri,2)) for tri in remaining_triangles)
    # Check integral proof's necessary finite-dimensional predictions over
    # two characteristics (one detects order-2 torsion).
    edge_index = {edge: i for i,edge in enumerate(sorted(full_edges))}
    columns = []
    for a,b,c in sorted(triangles):
        columns.append({edge_index[(a,b)]:1, edge_index[(a,c)]:-1, edge_index[(b,c)]:1})
    h = N - (N*n)//2 + q - 1
    assert h == (1 << (n-4))*(n*n-5*n+8)-1
    for p in (2,3):
        rank2 = ranks_mod_p(columns,p)
        hom1 = (len(full_edges)-N+1)-rank2
        hom2 = len(triangles)-rank2-q
        assert (hom1,hom2)==(far+(p==2),h+(p==2)), (n,p,hom1,hom2,far,h)
    print(f'n={n} N={N} f=( {N}, {len(full_edges)}, {len(triangles)}, {q} ) '
          f'far_edges={far} integral_H2_free_rank={h} verified')


if __name__ == '__main__':
    for n in (5,6,7):
        verify(n)
    print('VERIFY_OK')
