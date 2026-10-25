#!/usr/bin/env python3
"""Exact integral 2-cycle and symmetry certificate for the deleted symmetric square of K6.

Run: python3 verify_k6_triangle_tori.py
Only the Python standard library is needed.
"""
from itertools import combinations, permutations

N = 6
E = list(combinations(range(N), 2))
edge_idx = {e: i for i, e in enumerate(E)}
C0 = list(combinations(range(N), 2))
c0_idx = {c: i for i, c in enumerate(C0)}
C1 = [(v, j) for j, e in enumerate(E) for v in range(N) if v not in e]
c1_idx = {c: i for i, c in enumerate(C1)}
C2 = [(i, j) for i, a in enumerate(E) for j, b in enumerate(E)
      if i < j and set(a).isdisjoint(b)]
c2_idx = {c: i for i, c in enumerate(C2)}

D1 = [[0] * len(C1) for _ in C0]
for j, (v, i) in enumerate(C1):
    a, b = E[i]
    D1[c0_idx[tuple(sorted((v, b)))]][j] += 1
    D1[c0_idx[tuple(sorted((v, a)))]][j] -= 1

D2 = [[0] * len(C2) for _ in C1]
for k, (i, j) in enumerate(C2):
    a, b = E[i]
    c, d = E[j]
    for row, sgn in (((b, j), 1), ((a, j), -1),
                     ((d, i), -1), ((c, i), 1)):
        D2[c1_idx[row]][k] += sgn

assert len(C0) == 15 and len(C1) == 60 and len(C2) == 45
for col in range(len(C2)):
    for row in range(len(C0)):
        assert sum(D1[row][mid] * D2[mid][col]
                   for mid in range(len(C1))) == 0

def cycle_of(triple):
    out = {}
    a, b, c = triple
    for x, y in ((a, b), (b, c), (c, a)):
        ee = tuple(sorted((x, y)))
        out[edge_idx[ee]] = 1 if (x, y) == ee else -1
    return out

PARTS = []
for x in combinations(range(N), 3):
    y = tuple(i for i in range(N) if i not in x)
    if x < y:
        PARTS.append((x, y))
assert len(PARTS) == 10
part_idx = {p: i for i, p in enumerate(PARTS)}
T = [[0] * len(PARTS) for _ in C2]
for k, (x, y) in enumerate(PARTS):
    for i, a in cycle_of(x).items():
        for j, b in cycle_of(y).items():
            pair = tuple(sorted((i, j)))
            T[c2_idx[pair]][k] += a*b*(1 if i < j else -1)
for col in range(len(PARTS)):
    for row in range(len(C1)):
        assert sum(D2[row][i]*T[i][col] for i in range(len(C2))) == 0

def perm_sign(vals):
    return -1 if sum(vals[i] > vals[j] for i in range(len(vals))
                     for j in range(i+1, len(vals))) % 2 else 1

REL = [perm_sign(x+y) for x, y in PARTS]
for row in T:
    assert sum(row[i] * REL[i] for i in range(10)) == 0
assert REL == [1, -1, 1, -1, 1, -1, 1, 1, -1, 1]

# The fixed unit minor for columns 0..8 certifies their saturated rank-nine lattice.
UNIT_ROWS = [0, 1, 3, 6, 7, 9, 12, 13, 18]

def det_bareiss(a):
    a = [list(row) for row in a]
    m = len(a)
    old = 1
    sgn = 1
    for k in range(m-1):
        if a[k][k] == 0:
            row = next((j for j in range(k+1, m) if a[j][k]), None)
            if row is None:
                return 0
            a[k], a[row] = a[row], a[k]
            sgn *= -1
        p = a[k][k]
        for i in range(k+1, m):
            for j in range(k+1, m):
                v = a[i][j]*p - a[i][k]*a[k][j]
                assert v % old == 0
                a[i][j] = v//old
            a[i][k] = 0
        old = p
    return sgn * (a[-1][-1] if m else 1)

unit_det = det_bareiss([[T[i][j] for j in range(9)] for i in UNIT_ROWS])
assert unit_det == 1

def rank_mod_p(A, p):
    a = [[v % p for v in row] for row in A]
    rows, cols = len(a), len(a[0])
    r = 0
    for col in range(cols):
        lead = next((i for i in range(r, rows) if a[i][col]), None)
        if lead is None:
            continue
        a[r], a[lead] = a[lead], a[r]
        inv = pow(a[r][col], -1, p)
        a[r][col:] = [(inv*v) % p for v in a[r][col:]]
        for i in range(r+1, rows):
            if a[i][col]:
                v = a[i][col]
                a[i][col:] = [(x-v*y)%p for x,y in zip(a[i][col:], a[r][col:])]
        r += 1
        if r == rows:
            break
    return r

assert rank_mod_p(D2, 101) == 36
assert rank_mod_p(D2, 2) == 35

# Verify all 720 S6 actions on the chain matrix and ten torus classes,
# including the action on the alternating relation.
for g in permutations(range(N)):
    sign_g = perm_sign(g)
    image_edge = []
    for (a, b) in E:
        u, v = g[a], g[b]
        image_edge.append((edge_idx[tuple(sorted((u, v)))], 1 if u<v else -1))
    image_c2 = []
    for i, j in C2:
        ni, si = image_edge[i]
        nj, sj = image_edge[j]
        a, b = sorted((ni, nj))
        image_c2.append((c2_idx[(a, b)], si*sj*(1 if ni<nj else -1)))
    for k, (x, y) in enumerate(PARTS):
        gx, gy = tuple(sorted(g[i] for i in x)), tuple(sorted(g[i] for i in y))
        ix = perm_sign([g[i] for i in x])
        iy = perm_sign([g[i] for i in y])
        if gx < gy:
            newpart = (gx, gy)
            swap = 1
        else:
            newpart = (gy, gx)
            swap = -1
        q = part_idx[newpart]
        factor = ix*iy*swap
        transformed = [0] * len(C2)
        for row, (target, sgn) in enumerate(image_c2):
            transformed[target] += sgn*T[row][k]
        assert transformed == [factor*T[row][q] for row in range(len(C2))]
        # Relation coefficient covariance under the total vertex-permutation sign.
        assert REL[k]*factor == sign_g*REL[q]

print('VERIFY_OK_K6_TEN_TRIANGLE_TORI_PRIMITIVE_ALTERNATING_RELATION')
print('CELL_RANKS', len(C0),len(C1),len(C2), 'D1D2_ZERO')
print('MOD_101_AND_MOD_2_D2_RANKS',rank_mod_p(D2,101),rank_mod_p(D2,2))
print('TRIANGLE_PAIR_TORI',len(PARTS),'ONE_INTEGER_RELATION',tuple(REL))
print('NINE_BY_NINE_UNIT_MINOR_ROWS',tuple(UNIT_ROWS),'DET',unit_det)
print('INTEGRAL_H2_RANK',9,'ANY_NINE_TRIANGLE_TORI_BASIS')
print('SIX_VERTEX_PERMUTATIONS_CHECKED',720, 'RELATION_SIGN_CHARACTER')
