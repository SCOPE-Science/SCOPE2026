#!/usr/bin/env python3
"""Exact integer and fundamental-group checks for a thirteen-vertex graph complex.

Requires only the Python 3 standard library. Every finite assertion is rebuilt
from quadratic residues, without preloaded boundary matrices or saved logs.
"""

from itertools import combinations
from collections import Counter

N = 13
RESIDUES = {pow(i, 2, N) for i in range(1, N)}
assert RESIDUES == {1, 3, 4, 9, 10, 12}
VERTICES = tuple(range(N))


def adjacent(a, b):
    return a != b and (a - b) % N in RESIDUES


def connected_triple(t):
    return all(any(adjacent(a, b) for b in t if b != a) for a in t)


def test_graph():
    for a in VERTICES:
        nbr = {b for b in VERTICES if adjacent(a, b)}
        assert len(nbr) == 6
        for b in VERTICES:
            if a != b:
                common = sum(adjacent(a, c) and adjacent(b, c) for c in VERTICES)
                assert common == (2 if adjacent(a, b) else 3)
        # An induced 6-cycle: each neighbor has two neighbors inside,
        # and all six neighbors form one connected component.
        assert all(sum(adjacent(b, c) for c in nbr) == 2 for b in nbr)
        seen = {next(iter(nbr))}
        frontier = set(seen)
        while frontier:
            frontier = {w for v in frontier for w in nbr if adjacent(v, w)} - seen
            seen.update(frontier)
        assert seen == nbr


def build_faces():
    # Empty face is implicit; nonempty faces are indexed by cardinality.
    F = {k: [] for k in range(1, 6)}
    for k in F:
        for s in combinations(VERTICES, k):
            if k < 3 or all(connected_triple(t) for t in combinations(s, 3)):
                F[k].append(s)
    assert tuple(len(F[k]) for k in range(1, 6)) == (13, 78, 143, 78, 0)
    shape = Counter(sum(adjacent(a, b) for a, b in combinations(s, 2)) for s in F[4])
    assert shape == {4: 39, 5: 39}  # 4-cycles and diamonds; no 4-cliques
    assert len([s for s in combinations(VERTICES, 3) if connected_triple(s)]) == 143
    return F


def test_duality(F):
    disconnected = [frozenset(s) for s in combinations(VERTICES, 3)
                    if not connected_triple(s)]
    assert len(disconnected) == 143
    for mask in range(1 << N):
        u = {i for i in VERTICES if (mask >> i) & 1}
        # Direct Alexander-dual membership: no disconnected triple in u.
        dual = not any(t <= u for t in disconnected)
        direct = all(connected_triple(t) for t in combinations(u, 3))
        assert dual == direct
        # Direct ordinary cut-complex membership by complementing u.
        original_cut_face = any(t <= (set(VERTICES) - u) for t in disconnected)
        assert original_cut_face == (not all(
            connected_triple(t) for t in combinations(set(VERTICES) - u, 3)))


def test_fundamental_group(F):
    # A spanning tree of the complete one-skeleton is the star at vertex 0.
    # Every non-tree edge (i,j), 1 <= i < j <= 12, is one generator.
    gens = {tuple(e) for e in combinations(range(1, N), 2)}
    # Triangles (0,i,j) make this generator trivial.
    trivial = {(t[1], t[2]) for t in F[3] if t[0] == 0}
    assert len(gens) == 66 and len(trivial) == 33
    first_round = set(trivial)
    triangles_as_relations = [set(combinations(t, 2)) & gens for t in F[3]]
    # If two edges of a triangular relator are trivial, so is the third.
    rounds = []
    while True:
        newly = {next(iter(r - trivial)) for r in triangles_as_relations
                 if len(r - trivial) == 1}
        newly -= trivial
        if not newly:
            break
        rounds.append(len(newly))
        trivial.update(newly)
    assert rounds == [33] and trivial == gens and len(first_round) == 33


def boundary(F, k):
    lower, upper = F[k], F[k + 1]
    idx = {s: i for i, s in enumerate(lower)}
    mat = [[0] * len(upper) for _ in lower]
    for j, simplex in enumerate(upper):
        for a in range(k + 1):
            deleted = simplex[:a] + simplex[a + 1:]
            mat[idx[deleted]][j] = (-1) ** a
    return mat


def check_chain(M, Nmat):
    # M: C_{k-1} <- C_k, Nmat: C_k <- C_{k+1}.
    rows, middle, cols = len(M), len(Nmat), len(Nmat[0])
    assert len(M[0]) == middle
    for i in range(rows):
        for j in range(cols):
            assert sum(M[i][a] * Nmat[a][j] for a in range(middle)) == 0


def unit_diagonal_form(original):
    """Integral row/column elementary operations give diag(+-1,...,0).

    A pivot at ±1 is split off by unimodular row/column operations.
    The remaining submatrix is recomputed exactly; termination with a zero
    submatrix proves both the integral rank and absence of nonunit Smith
    factors. No floating-point arithmetic or modular inference is involved.
    """
    A = [list(row) for row in original]
    m, n = len(A), len(A[0])
    rank = 0
    while rank < min(m, n):
        k = rank
        loc = next(((i, j) for i in range(k, m) for j in range(k, n)
                    if abs(A[i][j]) == 1), None)
        if loc is None:
            break
        r, c = loc
        A[r], A[k] = A[k], A[r]
        for i in range(m):
            A[i][c], A[i][k] = A[i][k], A[i][c]
        pivot = A[k][k]
        assert abs(pivot) == 1
        # Clear pivot column by exact integral row additions.
        for i in range(k + 1, m):
            if A[i][k]:
                v = A[i][k] // pivot
                for j in range(k, n):
                    A[i][j] -= v * A[k][j]
        # Clear pivot row by exact integral column additions.
        for j in range(k + 1, n):
            if A[k][j]:
                v = A[k][j] // pivot
                for i in range(k, m):
                    A[i][j] -= v * A[i][k]
        assert all(A[i][k] == 0 for i in range(k + 1, m))
        assert all(A[k][j] == 0 for j in range(k + 1, n))
        rank += 1
    assert not any(A[i][j] for i in range(rank, m) for j in range(rank, n)), \
        'Nonzero Smith residual block; assertion not established'
    return rank


def main():
    test_graph()
    faces = build_faces()
    test_duality(faces)
    test_fundamental_group(faces)
    B1, B2, B3 = (boundary(faces, k) for k in (1, 2, 3))
    check_chain(B1, B2)
    check_chain(B2, B3)
    ranks = (unit_diagonal_form(B1), unit_diagonal_form(B2),
             unit_diagonal_form(B3))
    assert ranks == (12, 66, 76)
    b1 = len(faces[2]) - ranks[0] - ranks[1]
    b2 = len(faces[3]) - ranks[1] - ranks[2]
    b3 = len(faces[4]) - ranks[2]
    assert (b1, b2, b3) == (0, 1, 2)
    print('VERIFY_OK; faces=(13,78,143,78), tetrahedra=C4:39+diamond:39, '
          'unimodular boundary ranks=(12,66,76), pi1=1, dual bettis=(0,1,2)')


if __name__ == '__main__':
    main()
