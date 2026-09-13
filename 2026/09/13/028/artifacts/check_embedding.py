"""Full lattice embedding data for lane-1568.

L = U^3 + E8(-1)^2 + <-2>  (K3^[2] lattice, rank 23, signature (3,20)).
j0: U -> L, first summand.  NS generators F1=e1, F2=f1.
delta = F1 - F2. Checks (exact integer arithmetic):
 - q(delta) = -2, delta primitive in L, div_L(delta) = 1.
 - Reflection R_delta integral isometry, swaps F1<->F2, fixes T pointwise.
 - E8 Cartan determinant = 1 (unimodularity sanity), L signature (3,20).
Writes output/artifacts/embedding.json
"""
import json
from fractions import Fraction

# E8 Cartan matrix, Bourbaki labeling:
# chain 1-3-4-5-6-7-8 with extra node 2 attached to 4.
n = 8
C = [[0]*n for _ in range(n)]
edges = [(0,2),(2,3),(3,4),(4,5),(5,6),(6,7),(1,3)]
for i in range(n):
    C[i][i] = 2
for (i,j) in edges:
    C[i][j] = C[j][i] = -1

def det_int(M):
    m = len(M)
    A = [[Fraction(M[i][j]) for j in range(m)] for i in range(m)]
    d = Fraction(1)
    for k in range(m):
        piv = next((i for i in range(k, m) if A[i][k] != 0), None)
        assert piv is not None, "singular"
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
            d = -d
        d *= A[k][k]
        for i in range(k+1, m):
            f = A[i][k]/A[k][k]
            for j in range(k, m):
                A[i][j] -= f*A[k][j]
    return d

assert det_int(C) == 1, det_int(C)

# Block-diagonal Gram of L in basis
# [e1,f1, e2,f2, e3,f3, E8a x8, E8b x8, d]
def gram_L():
    G = [[0]*23 for _ in range(23)]
    U = [[0,1],[1,0]]
    for b in range(3):
        o = 2*b
        for i in range(2):
            for j in range(2):
                G[o+i][o+j] = U[i][j]
    for blk in range(2):
        o = 6 + 8*blk
        for i in range(8):
            for j in range(8):
                G[o+i][o+j] = -C[i][j]  # E8(-1)
    G[22][22] = -2
    return G

G = gram_L()
# signature via Sylvester: leading principal minors nonzero pattern is messy for
# block diag; instead check each block: U has signature (1,1) (det -1, trace 0),
# -C has signature (0,8) (C positive definite: all leading minors > 0), [-2] (0,1).
def leading_minors_pos(M):
    ms = []
    for k in range(1, len(M)+1):
        sub = [row[:k] for row in M[:k]]
        ms.append(det_int(sub))
    return ms
assert leading_minors_pos(C) == [2,3,4,5,6,7,8,1] or all(
    v > 0 for v in leading_minors_pos(C)), leading_minors_pos(C)
# U block: det = -1, trace 0 -> (1,1). -C negative definite -> (0,8). [-2] -> (0,1).
assert G[0][1] == 1 and G[0][0] == 0 and G[22][22] == -2
signature = (3, 20)  # 3x(1,1) + 2x(0,8) + (0,1)

def pair(v, w):
    return sum(v[i]*G[i][j]*w[j] for i in range(23) for j in range(23))

def q(v):
    return pair(v, v)

e = lambda i: tuple(1 if k == i else 0 for k in range(23))
F1, F2 = e(0), e(1)
assert q(F1) == 0 and q(F2) == 0 and pair(F1, F2) == 1
delta = tuple(F1[i]-F2[i] for i in range(23))
assert q(delta) == -2
import math
assert math.gcd(*[c for c in delta if c != 0]) == 1  # primitive in L
divs = sorted({abs(pair(delta, e(i))) for i in range(23) if pair(delta, e(i)) != 0})
div = 0
for d_ in divs:
    div = math.gcd(div, d_)
assert div == 1, divs  # divisibility 1 (pairings +-1 with e1,f1)
assert pair(delta, F1) == -1 and pair(delta, F2) == 1

# Reflection R(x) = x + (x,delta) delta  [since (d,d)=-2: x - 2(x,d)/(d,d) d]
def R(v):
    c = pair(v, delta)
    return tuple(v[i] + c*delta[i] for i in range(23))
assert R(F1) == F2 and R(F2) == F1
# fixes T = U^perp pointwise: test basis of T (all basis vecs except e1,f1)
for i in range(2, 23):
    assert R(e(i)) == e(i), i
# isometry + involution on samples
import random
random.seed(7)
for _ in range(300):
    v = tuple(random.randint(-3,3) for _ in range(23))
    w = tuple(random.randint(-3,3) for _ in range(23))
    assert pair(R(v), R(w)) == pair(v, w)
    assert R(R(v)) == v

# h = F1+F2: q=2 (projectivity witness); wall midpoint
h = tuple(F1[i]+F2[i] for i in range(23))
assert q(h) == 2 and pair(h, delta) == 0

out = {
    "L": "U^3 + E8(-1)^2 + <-2>, rank 23, signature [3, 20]",
    "E8_Cartan_det": 1,
    "j0": "U isometrically as first summand; NS = span{e1, f1}",
    "F1": list(F1), "F2": list(F2),
    "delta": list(delta),
    "q_delta": -2,
    "delta_primitive_in_L": True,
    "div_L_delta": 1,
    "pair_delta_F1": -1,
    "pair_delta_F2": 1,
    "R_swaps_F1_F2": True,
    "R_fixes_T_pointwise": True,
    "R_isometry_involution": True,
    "h_F1pF2": list(h),
    "q_h": 2,
    "conclusion": "delta is a primitive (-2, div 1) class in L; R_delta is an "
                  "integral Hodge-monodromy involution exchanging the two "
                  "isotropic rays and fixing the transcendental lattice.",
}
with open("output/artifacts/embedding.json", "w") as fh:
    json.dump(out, fh, indent=2)
print(json.dumps({k: v for k, v in out.items() if not isinstance(v, list)}, indent=2))
print("ALL EMBEDDING CHECKS PASSED")
