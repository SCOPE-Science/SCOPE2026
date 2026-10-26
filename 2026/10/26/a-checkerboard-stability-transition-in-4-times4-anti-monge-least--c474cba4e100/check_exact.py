#!/usr/bin/env python3
"""Exact rational verification of square anti-Monge projection constants.

Pure Python 3, no external libraries. Run: python3 check_exact.py
"""
from fractions import Fraction as Q


def difference_matrix(n):
    D = []
    for i in range(n - 1):
        for j in range(n - 1):
            row = [Q(0)] * (n * n)
            for r, c, s in ((i, j, 1), (i + 1, j + 1, 1),
                            (i + 1, j, -1), (i, j + 1, -1)):
                row[r * n + c] = Q(s)
            D.append(row)
    return D


def invert(M):
    n = len(M)
    T = [[Q(M[i][j]) for j in range(n)] +
         [Q(i == j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if T[r][c]), None)
        assert p is not None, "independence failure"
        T[c], T[p] = T[p], T[c]
        inv = 1 / T[c][c]
        T[c] = [v * inv for v in T[c]]
        for r in range(n):
            if r != c and T[r][c]:
                factor = T[r][c]
                T[r] = [u - factor * v for u, v in zip(T[r], T[c])]
    return [row[n:] for row in T]


def projector(D, mask):
    N = len(D[0]); active = [k for k in range(len(D)) if mask >> k & 1]
    B = [D[k] for k in active]; m = len(B)
    if not m:
        return [[Q(i == j) for j in range(N)] for i in range(N)], [], []
    gram = [[sum(B[i][h] * B[j][h] for h in range(N))
             for j in range(m)] for i in range(m)]
    inv = invert(gram)
    V = [[sum(inv[i][j] * B[j][h] for j in range(m))
          for h in range(N)] for i in range(m)]
    P = [[Q(i == j) - sum(B[k][i] * V[k][j] for k in range(m))
          for j in range(N)] for i in range(N)]
    return P, B, inv


def mat_vec(M, v):
    return [sum(a * b for a, b in zip(row, v)) for row in M]


def certify(n, expected, expected_mask, expected_by_count):
    D = difference_matrix(n)
    m = (n-1)*(n-1)
    per_count = {k: [Q(-1), []] for k in range(m+1)}
    global_best = Q(-1); best_masks = []
    for mask in range(1 << m):
        P, B, inverse = projector(D, mask)
        # Exact symmetry, idempotence, annihilation; all active faces checked.
        assert all(P[i][j] == P[j][i] for i in range(n*n) for j in range(n*n))
        assert all(sum(row[h] * P[h][j] for h in range(n*n)) == P[i][j]
                   for i, row in enumerate(P) for j in range(n*n))
        assert all(sum(b[h] * P[h][j] for h in range(n*n)) == 0
                   for b in B for j in range(n*n))
        peak = max(sum(abs(a) for a in row) for row in P)
        count = mask.bit_count()
        if peak > per_count[count][0]:per_count[count] = [peak, [mask]]
        elif peak == per_count[count][0]:per_count[count][1].append(mask)
        if peak > global_best:global_best, best_masks = peak, [mask]
        elif peak == global_best:best_masks.append(mask)
    assert global_best == Q(*expected)
    assert best_masks == [expected_mask]
    assert {k:v[0] for k,v in per_count.items()} == {
        k:Q(*p) for k,p in enumerate(expected_by_count)}
    print("size",n,"checked",1<<m,"active subsets; peak",global_best,
          "unique winning mask",best_masks[0])
    print("peak by active-set size:", [str(per_count[k][0]) for k in range(m+1)])
    return D


D2 = certify(2, (3,2), 1, [(1,1), (3,2)])
D3 = certify(3, (17,9), 15, [(1,1),(3,2),(9,5),(11,6),(17,9)])
D4 = certify(4, (9,4), 341, [(1,1),(3,2),(9,5),(27,14),(21,10),
                              (9,4),(43,20),(17,8),(19,9),(17,8)])
# Exact active-face witness with strict multipliers and inactive slacks.
mask = 341; P, B, G = projector(D4,mask)
z = [Q(x) for x in (0,0,0,0, 0,0,1,1, 0,1,2,3, 0,1,3,4)]
y = [Q(x) for x in (-1,1,-1,1, 1,-2,3,0, -1,3,0,4, 1,0,4,3)]
v = [Q(x) for x in (-1,1,1,-1, 1,1,1,1, 1,1,-1,-1, -1,1,-1,1)]
assert mat_vec(D4,z) == [Q(int(k not in (0,2,4,6,8))) for k in range(9)]
assert [z[i]-y[i] for i in range(16)] == [sum(b[i] for b in B) for i in range(16)]
assert sum(abs(t) for t in P[5]) == Q(9,4)
assert v == [Q(1 if r >= 0 else -1) for r in P[5]]
eps = Q(1,100)
G_B_v = mat_vec(G, mat_vec(B,v))
new_lambda = [Q(1)-eps*x for x in G_B_v]
new_z = [z[i]+eps*x for i,x in enumerate(mat_vec(P,v))]
slacks = mat_vec(D4,new_z)
assert min(new_lambda) == Q(397,400)
assert min(slacks[j] for j in (1,3,5,7)) == Q(99,100)
assert all(slacks[j] == 0 for j in (0,2,4,6,8))
assert mat_vec(P,v)[5] == Q(9,4)
assert max(abs(x) for x in v) == Q(1)
print('strict finite-pair witness verified; norm ratio', Q(9,4),
      'minimum multiplier', min(new_lambda),
      'minimum inactive slack', min(slacks[j] for j in (1,3,5,7)))
