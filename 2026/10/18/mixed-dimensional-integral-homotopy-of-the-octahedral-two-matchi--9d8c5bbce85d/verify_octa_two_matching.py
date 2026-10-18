#!/usr/bin/env python3
"""Reproducible finite verification of the octahedral degree-two matching complex.
Only Python's standard library is required. All face incidence signs are exact integers.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

VERTICES = tuple(range(6))
EDGES = tuple((a, b) for a in VERTICES for b in range(a + 1, 6) if a // 2 != b // 2)
assert len(EDGES) == 12


def legal(mask):
    degree = [0] * 6
    for i, (a, b) in enumerate(EDGES):
        if mask & (1 << i):
            degree[a] += 1
            degree[b] += 1
            if degree[a] > 2 or degree[b] > 2:
                return False
    return True


FACES = tuple(mask for mask in range(1 << 12) if legal(mask))
FACESET = set(FACES)
assert len(FACES) == 772
assert Counter(mask.bit_count() - 1 for mask in FACES if mask) == {0: 12, 1: 66, 2: 196, 3: 297, 4: 180, 5: 20}
assert all((mask & ~(1 << i)) in FACESET for mask in FACES for i in range(12) if mask & (1 << i))
FACETS = tuple(mask for mask in FACES if not any((mask | (1 << i)) in FACESET for i in range(12) if not mask & (1 << i)))
assert Counter(mask.bit_count() - 1 for mask in FACETS) == {3:3,4:60,5:20}


def boundary(mask):
    return tuple((mask ^ (1 << i), (-1) ** j)
                 for j, i in enumerate(i for i in range(12) if mask & (1 << i))
                 if (mask ^ (1 << i)) != 0)


# Successive matching by the smallest available edge-index.
# The empty face is excluded so one critical vertex remains.
ACTIVE = set(FACES) - {0}
PAIRS = []
for i in range(12):
    bit = 1 << i
    for lo in sorted(ACTIVE):
        hi = lo | bit
        if not (lo & bit) and hi in ACTIVE:
            assert lo in ACTIVE
            ACTIVE.remove(lo)
            ACTIVE.remove(hi)
            PAIRS.append((lo, hi))
LOWER_TO_UPPER = dict(PAIRS)
UPPER_TO_LOWER = {b: a for a, b in PAIRS}
CRITICAL = set(ACTIVE)
assert len(PAIRS) == 377
assert len(CRITICAL) == 17
assert Counter(mask.bit_count() - 1 for mask in CRITICAL) == {0: 1, 3: 6, 4: 10}

# Exact topological sort of the matched Hasse digraph.
# Reverse only the 377 matched face incidences.
OUT = {x: [] for x in FACESET if x != 0}
INDEG = {x: 0 for x in OUT}
covers = 0
for upper in OUT:
    for lower, sg in boundary(upper):
        assert lower in FACESET
        covers += 1
        if LOWER_TO_UPPER.get(lower) == upper:
            src, dst = lower, upper
        else:
            src, dst = upper, lower
        OUT[src].append(dst)
        INDEG[dst] += 1
q = deque(x for x, d in INDEG.items() if d == 0)
visited = 0
while q:
    x = q.popleft()
    visited += 1
    for y in OUT[x]:
        INDEG[y] -= 1
        if INDEG[y] == 0:
            q.append(y)
assert visited == len(OUT) == 771

# Morse chain-projection reduction over Z: eliminate an upper matched
# generator; replace its lower matched boundary face by the remaining
# boundary of the matched upper cell, with the correct incidence sign.
@lru_cache(None)
def project(mask):
    if mask in CRITICAL:
        return {mask: 1}
    if mask in UPPER_TO_LOWER:
        return {}
    upper = LOWER_TO_UPPER[mask]
    incidence = dict(boundary(upper))[mask]
    result = {}
    for face, coefficient in boundary(upper):
        if face == mask:
            continue
        for cface, val in project(face).items():
            result[cface] = result.get(cface, 0) - incidence * coefficient * val
    return {key: val for key, val in result.items() if val}

C3 = sorted(m for m in CRITICAL if m.bit_count() == 4)
C4 = sorted(m for m in CRITICAL if m.bit_count() == 5)
M = [[0 for _ in C4] for _ in C3]
for j, upper in enumerate(C4):
    result = {}
    for face, coefficient in boundary(upper):
        for cface, val in project(face).items():
            result[cface] = result.get(cface, 0) + coefficient * val
    for i, target in enumerate(C3):
        M[i][j] = result.get(target, 0)
assert M == [
    [0, 0, 0, 0, -1, -1, 0, 1, 0, 1],
    [0, -1, 1, 1, 1, 0, 1, 0, 1, 0],
    [-1, 0, -1, 0, 0, 1, -1, -1, 0, -1],
    [1, 1, 0, -1, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def rank_mod_p(matrix, p):
    if not matrix or not matrix[0]:
        return 0
    a = [[int(v) % p for v in row] for row in matrix]
    r, ncol = 0, len(a[0])
    for col in range(ncol):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(inv * v) % p for v in a[r]]
        for j in range(r + 1, len(a)):
            if a[j][col]:
                factor = a[j][col]
                a[j] = [(v - factor * w) % p for v, w in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r


# Check exact integer rank =3: all 4x4 minors vanish (since last two rows
# are zero, enough to check the 4 active rows), and exhibit unit 3x3 minor.
assert rank_mod_p(M, 2) == rank_mod_p(M, 3) == rank_mod_p(M, 101) == 3

def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

minor = next(((rows, cols, determinant3([[M[r][c] for c in cols] for r in rows]))
              for rows in combinations(range(6), 3)
              for cols in combinations(range(10), 3)
              if abs(determinant3([[M[r][c] for c in cols] for r in rows])) == 1), None)
assert minor is not None
assert all(M[3][j] == -M[0][j] - M[1][j] - M[2][j] for j in range(10))
# Deterministic rational elimination to bound rank exactly.
from fractions import Fraction

def rank_Q(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for col in range(len(a[0])):
        pivot = next((k for k in range(r, len(a)) if a[k][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = a[r][col]
        for j in range(col, len(a[0])):
            a[r][j] /= inv
        for i in range(r+1, len(a)):
            t = a[i][col]
            for j in range(col, len(a[0])):
                a[i][j] -= t*a[r][j]
        r += 1
        if r == len(a):
            break
    return r
assert rank_Q(M) == 3

# Independent simplicial homology over F2 and F3, computed using all faces.
B = {}
for k in range(1, 6):
    src = [m for m in FACES if m.bit_count() == k+1]
    dst = [m for m in FACES if m.bit_count() == k]
    imap = {m: i for i, m in enumerate(dst)}
    mat = [[0] * len(src) for _ in dst]
    for j, m in enumerate(src):
        for f,sgn in boundary(m):
            mat[imap[f]][j] = sgn
    B[k] = mat
for p in (2,3):
    r = {k: rank_mod_p(B[k],p) for k in B}
    counts = Counter(m.bit_count() - 1 for m in FACES if m)
    betti = {k: counts[k] - r.get(k,0) - r.get(k+1,0)
             for k in range(1,6)}
    assert betti == {1:0, 2:0, 3:3, 4:7, 5:0},(p,r,betti)
print('OCTAHEDRON_TWO_MATCHING_INTEGRAL_HOMOTOPY_CHECKS_OK')
print('face_vector',(12,66,196,297,180,20),'facets_by_dimension',{3:3,4:60,5:20})
print('morse_pairs',len(PAIRS),'critical_by_dimension',{0:1,3:6,4:10},'hasse_covers',covers)
print('morse_d4_rank',rank_Q(M),'unit_minor',minor)
print('homotopy','3*S^3 wedge 7*S^4')
