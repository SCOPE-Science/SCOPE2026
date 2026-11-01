"""Reconstruct signed boundary chains of clique complexes of stable cycle powers.

Requires Python 3 and sympy. This finite checker is supplementary to the proof.
"""
from collections import defaultdict
from itertools import combinations
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def invariant(n, m):
    assert m >= 3 and n >= 3*m + 1
    maximal = [frozenset((j + i) % n for i in range(m+1)) for j in range(n)]
    assert len(set(maximal)) == n
    degree = defaultdict(int)
    for facet in maximal:
        for rid in combinations(sorted(facet), m):
            degree[frozenset(rid)] += 1
    assert set(degree.values()) <= {1, 2}
    boundary = [tuple(sorted(s)) for s, count in degree.items() if count == 1]
    faces = {
        k: sorted({small for face in boundary
                   for small in combinations(face, k+1)})
        for k in range(m)
    }
    boundary_maps = {}
    for k in range(1, m):
        row_index = {face: i for i, face in enumerate(faces[k-1])}
        entries = {}
        for col, face in enumerate(faces[k]):
            for i in range(k+1):
                subface = face[:i] + face[i+1:]
                entries[(row_index[subface], col)] = (-1)**i
        boundary_maps[k] = SparseMatrix(len(faces[k-1]), len(faces[k]), entries)
    for k in range(2, m):
        assert boundary_maps[k-1] * boundary_maps[k] == SparseMatrix.zeros(
            len(faces[k-2]), len(faces[k]))
    ranks = {k: B.rank() for k, B in boundary_maps.items()}
    reduced_betti = tuple(len(faces[k]) - ranks.get(k, 0) - ranks.get(k+1, 0)
                          - (1 if k == 0 else 0) for k in range(m))
    top = boundary_maps[m-1]
    normal = smith_normal_form(top, domain=ZZ)
    top_nonunits = tuple(sorted(abs(int(normal[i, i]))
                                for i in range(min(normal.shape))
                                if abs(normal[i, i]) > 1))
    return len(boundary), reduced_betti, top_nonunits


EXPECTED = {
    (10, 3): (20, (0, 2, 1), ()),
    (11, 3): (22, (0, 2, 1), ()),
    (13, 4): (39, (0, 1, 0, 0), (2,)),
    (14, 4): (42, (0, 1, 1, 1), ()),
    (16, 5): (64, (0, 1, 0, 1, 1), ()),
}


if __name__ == "__main__":
    for case, expected in EXPECTED.items():
        actual = invariant(*case)
        assert actual == expected, (case, expected, actual)
        print("PASS n={}, m={}, boundary_facets={}, reduced_betti={}, top_nonunits={}".format(
            *case, *actual))
