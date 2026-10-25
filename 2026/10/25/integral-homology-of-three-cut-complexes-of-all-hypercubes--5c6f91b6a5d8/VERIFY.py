"""Reproduce the low-dimensional Alexander-dual computation for cube 3-cut complexes.

Run: python VERIFY.py (Python >=3.9; sympy required for integer Smith forms).
The infinite-dimensional claim rests on the separate combinatorial proof.
"""
from itertools import combinations
from math import comb
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def faces(d):
    vertices = range(1 << d)
    edges = list(combinations(vertices, 2))
    triangles = [t for t in combinations(vertices, 3)
                 if sum((u ^ v).bit_count() == 1 for u, v in combinations(t, 2)) == 2]
    tetrahedra = [t for t in combinations(vertices, 4)
                  if all(sum((u ^ v).bit_count() == 1
                             for u, v in combinations(tri, 2)) == 2
                         for tri in combinations(t, 3))]
    return edges, triangles, tetrahedra


def boundary(lower, higher):
    position = {s: i for i, s in enumerate(lower)}
    entries = {}
    for j, face in enumerate(higher):
        for k in range(len(face)):
            subface = face[:k] + face[k+1:]
            entries[(position[subface], j)] = (-1) ** k
    return SparseMatrix(len(lower), len(higher), entries)


def smith_units(B):
    D = smith_normal_form(B, domain=ZZ)
    diagonal = [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i] != 0]
    assert set(diagonal) <= {1}, ('unexpected integral invariant factors', diagonal)
    return len(diagonal)


def mod2_rank_columns(edge_count, triangles, edge_indices):
    pivot = {}
    for triangle in triangles:
        a, b, c = triangle
        v = (1 << edge_indices[(a,b)]) ^ (1 << edge_indices[(a,c)]) ^ (1 << edge_indices[(b,c)])
        while v:
            high = v.bit_length() - 1
            if high not in pivot:
                pivot[high] = v
                break
            v ^= pivot[high]
    return len(pivot)


def verify(d):
    n = 1 << d
    edges, tris, tets = faces(d)
    square_count = (1 << (d-2)) * comb(d, 2)
    assert len(tris) == 4 * square_count
    assert len(tets) == square_count
    far = (1 << (d-1)) * (n - 1 - d - comb(d, 2))
    beta2 = (1 << (d-2)) * (4 - 2*d + comb(d,2)) - 1
    assert len(edges) - ((1 << (d-1)) * (d + comb(d,2))) == far
    if d <= 4:
        verts = [(v,) for v in range(n)]
        B1 = boundary(verts, edges)
        B2 = boundary(edges, tris)
        B3 = boundary(tris, tets)
        assert B1 * B2 == SparseMatrix(n, len(tris), {})
        assert B2 * B3 == SparseMatrix(len(edges), len(tets), {})
        r1, r2, r3 = smith_units(B1), smith_units(B2), smith_units(B3)
        assert (r1, r2, r3) == (n-1, len(tris)-len(tets)-beta2, len(tets))
        assert (len(edges)-r1-r2, len(tris)-r2-r3) == (far, beta2)
        print(f'd={d}: n={n}, (vertices,edges,triangles,tetrahedra)={(n,len(edges),len(tris),len(tets))};'
              f' ranks=(d1:{r1},d2:{r2},d3:{r3}); H1=Z^{far}, H2=Z^{beta2}; SNF unit-only')
    else:
        ranks2 = mod2_rank_columns(len(edges), tris, {e:i for i,e in enumerate(edges)})
        assert ranks2 == len(tris)-len(tets)-beta2
        print(f'd={d}: n={n}, (vertices,edges,triangles,tetrahedra)={(n,len(edges),len(tris),len(tets))};'
              f' boundary2 rank modulo 2={ranks2}; expected H1 rank={far}, H2 rank={beta2}')


if __name__ == '__main__':
    for d in (3, 4, 5):
        verify(d)
    print('All finite checks passed. General case follows from cubical 2-skeleton proof.')
