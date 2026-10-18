"""Exact, standard-library singular-fan certificate for the triangular prism edge polytope.

Run: python3 verify_prism.py
No external libraries, downloaded datasets, or randomization are required.
"""
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd
from collections import Counter

# Edges of the triangular prism on vertices 0,...,5.
EDGES = ((0, 1), (1, 2), (0, 2),
         (3, 4), (4, 5), (3, 5),
         (0, 3), (1, 4), (2, 5))
POINTS = tuple(tuple(int(j in e) for j in range(5)) for e in EDGES)


def rank(rows):
    if not rows: return 0
    A = [list(map(Fraction, row)) for row in rows]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        i = next((i for i in range(r, m) if A[i][c]), None)
        if i is None: continue
        A[r], A[i] = A[i], A[r]
        z = A[r][c]
        A[r] = [a / z for a in A[r]]
        for j in range(r + 1, m):
            z = A[j][c]
            if z:
                A[j] = [a - z*b for a, b in zip(A[j], A[r])]
        r += 1
        if r == m: break
    return r


def det(rows):
    a = [list(row) for row in rows]
    n = len(a)
    assert all(len(row) == n for row in a)
    if not n: return 1
    d = 1
    for j in range(n - 1):
        if a[j][j] == 0:
            q = next((q for q in range(j+1, n) if a[q][j]), None)
            if q is None: return 0
            a[j], a[q] = a[q], a[j]
            d = -d
        pivot = a[j][j]
        for i in range(j + 1, n):
            for k in range(j + 1, n):
                a[i][k] = (a[i][k]*pivot - a[i][j]*a[j][k]) // (1 if j == 0 else a[j-1][j-1])
            a[i][j] = 0
    return d * a[-1][-1]


def norm(v):
    g = reduce(gcd, (abs(x) for x in v), 0)
    assert g
    return tuple(int(x//g) for x in v)


def facets():
    out = {}
    for choice in combinations(range(9), 5):
        a = POINTS[choice[0]]
        rows = [[POINTS[i][j] - a[j] for j in range(5)] for i in choice[1:]]
        n = tuple(((-1)**j)*det([[r[h] for h in range(5) if h != j]
                               for r in rows]) for j in range(5))
        if not any(n): continue
        n = norm(n)
        c = sum(x*y for x, y in zip(n, a))
        offsets = [sum(x*y for x, y in zip(n, p)) - c for p in POINTS]
        if min(offsets) < 0 and max(offsets) > 0: continue
        if min(offsets) < 0:
            n, c = tuple(-x for x in n), -c
            offsets = [-x for x in offsets]
        S = frozenset(i for i, x in enumerate(offsets) if x == 0)
        assert len(S) >= 5
        assert rank([[POINTS[i][j]-POINTS[min(S)][j] for j in range(5)]
                     for i in S if i != min(S)]) == 4
        if S in out: assert out[S] == (n, c)
        out[S] = (n, c)
    return out


def lattice_index(rows):
    k = rank(rows)
    if k == 0: return 1
    assert k == len(rows)
    n = len(rows[0])
    return reduce(gcd, (abs(det([[row[j] for j in J] for row in rows]))
                        for J in combinations(range(n), k)), 0)


def all_faces(F):
    current = {frozenset(range(9))}
    for S in F:
        current.update(T & S for T in tuple(current))
    current.discard(frozenset())
    assert len(current) == 135 # face counts: 9+30+47+36+12+1
    return current


def face_dim(S):
    p = POINTS[min(S)]
    return rank([[POINTS[i][j] - p[j] for j in range(5)]
                 for i in S if i != min(S)])


def nonsmooth(F, S):
    d = face_dim(S)
    if d == 5: return False, []
    N = [row[0] for T, row in F.items() if S <= T]
    assert rank(N) == 5-d
    if len(N) != 5-d: return True, N
    return lattice_index(N) != 1, N


def relation_four(N):
    # Primitive signed rank-one relation among four rank-three vectors in Z^5.
    assert len(N) == 4 and rank(N) == 3
    candidates = []
    for i in range(4):
        rest = [N[j] for j in range(4) if j != i]
        # Coefficient of row i is a signed 3x3 maximal minor of other rows.
        candidates.append(((-1)**i) * det([[N[j][h] for h in (0,1,2)]
                                             for j in range(4) if j != i]))
    if not any(candidates):
        for J in combinations(range(5), 3):
            candidates = [(-1)**i*det([[N[j][h] for h in J]
                                     for j in range(4) if j != i]) for i in range(4)]
            if any(candidates): break
    rel = norm(candidates)
    assert [sum(rel[i]*N[i][j] for i in range(4)) for j in range(5)] == [0]*5
    return rel


def run():
    # The edge-point differences span the full intrinsic sum-two lattice.
    diffs = [tuple(POINTS[i][j]-POINTS[0][j] for j in range(5))
             for i in range(1,9)]
    assert rank(diffs) == 5
    assert reduce(gcd, (abs(det([diffs[i] for i in I]))
                        for I in combinations(range(8),5)),0) == 1
    F = facets()
    assert len(F) == 12, len(F)
    faces = all_faces(F)
    dims = Counter(face_dim(S) for S in faces)
    assert dims == {0: 9, 1: 30, 2: 47, 3: 36, 4: 12, 5: 1}, dims
    singular = {}
    for S in faces:
        bad, N = nonsmooth(F, S)
        if bad: singular[S] = N
    sd = Counter(face_dim(S) for S in singular)
    assert sd == {0: 9, 1: 24, 2: 15}, sd
    maximum = {S: N for S, N in singular.items()
               if not any(S < T for T in singular)}
    assert len(maximum) == 15
    assert all(face_dim(S) == 2 for S in maximum)
    assert Counter(map(len, maximum)) == {3: 12, 4: 3}
    total_degree = 0
    for S, N in maximum.items():
        assert len(N) == 4 and rank(N) == 3
        rel = relation_four(N)
        assert sorted(rel) == [-1,-1,1,1], (S,rel)
        for I in combinations(range(4), 3):
            assert lattice_index([N[j] for j in I]) == 1, (S,I)
        p = POINTS[min(S)]
        diffs = [tuple(POINTS[i][j]-p[j] for j in range(5))
                 for i in S if i != min(S)]
        if len(S) == 3:
            assert lattice_index(diffs) == 1
            total_degree += 1
        else:
            assert rank(diffs) == 2
            # Among the four vertices one opposite-pair equality must hold.
            assert any(tuple(POINTS[I[0]][j]+POINTS[I[1]][j]
                             for j in range(5)) ==
                       tuple(POINTS[J[0]][j]+POINTS[J[1]][j]
                             for j in range(5))
                       for I in combinations(S, 2)
                       for J in combinations(S, 2) if not set(I)&set(J))
            assert any(lattice_index([a,b]) == 1 for a,b in combinations(diffs,2)
                       if rank([a,b]) == 2)
            total_degree += 2
    assert total_degree == 18
    print('VERIFY_OK facets=12 faces=135 singular_orbits=(9,24,15) '
          'components=(12_P2,3_P1xP1) degree=18 conifold_transversals=15')
    return maximum, F

if __name__ == '__main__':run()
