from fractions import Fraction
from itertools import combinations

def rank_integer(mat):
    if not mat:
        return 0
    a = [[Fraction(x) for x in row] for row in mat]
    m = len(a)
    n = len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def face_basis(n, I):
    I = sorted(I)
    p = I[0]
    cols = []
    for i in I[1:]:
        v = [0] * (n + 1)
        v[i] = 1
        v[p] = -1
        cols.append(v)
    return cols

def col_matrix(cols):
    if not cols:
        return []
    d = len(cols[0])
    return [[cols[j][i] for j in range(len(cols))] for i in range(d)]

def intersection_dim(n, I, J):
    BI = face_basis(n, I)
    BJ = face_basis(n, J)
    RI = rank_integer(col_matrix(BI))
    RJ = rank_integer(col_matrix(BJ))
    R = rank_integer(col_matrix(BI + BJ))
    return RI + RJ - R

# Exhaustive actual-face rank check in small dimensions.
for n in range(2, 7):
    vertices = range(n + 1)
    faces = []
    for k in range(2, n + 1):
        faces.extend(combinations(vertices, k))
    for I in faces:
        for J in faces:
            ov = len(set(I) & set(J))
            d = intersection_dim(n, I, J)
            assert (d == 0) == (ov <= 1)

# Exact all-combinatorial-type optimization over a broad finite window.
# This checks the formula algebraically; the proof in RESULT.md is all-dimensional.
for n in range(2, 101):
    best = Fraction(-1)
    best_types = set()
    for r in range(1, n):
        for s in range(1, n):
            if r + s > n:
                continue
            val = Fraction(r * s, (r + 1) * (s + 1))
            if val > best:
                best = val
                best_types = {(r, s)}
            elif val == best:
                best_types.add((r, s))
    r0 = n // 2
    s0 = n - r0
    target = Fraction(r0 * s0, (r0 + 1) * (s0 + 1))
    assert best == target
    assert best_types == {(r0, s0), (s0, r0)}
    assert Fraction(1) - target == Fraction(n + 1, (r0 + 1) * (s0 + 1))

print("VERIFY_OK")
print("actual_face_rank_exhaustive=n=2..6")
print("combinatorial_type_optimization=n=2..100 exact_rational")
print("maximizer=balanced_shared_vertex_full_union")
