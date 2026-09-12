"""Exact (stdlib-only) verification that the admitted P8->X9 non-extendability claim is FALSE.

Q_P8 = E6-type (rank 6, disc 3), Q_X9 = E7-type (rank 7, disc 2), with the
distinguished Dolgachev-exchange vertex-deletion inclusion sigma (delete the end
of the long arm of E7). Shows Phi = coordinate inclusion J IS a primitive
isometric embedding extending j, with explicit Nikulin rank-1 gluing and exact
Seifert-divisibility preservation. Sign convention (positive Cartan G vs -G) is
immaterial: every check below is invariant under an overall sign flip.

Prints VERIFY_OK on success; asserts everything.
"""
from fractions import Fraction
from math import gcd
from functools import reduce


def zeros(r, c):
    return [[0] * c for _ in range(r)]


def mat_mul(A, B):
    r, m, c = len(A), len(B), len(B[0])
    assert len(A[0]) == m
    C = zeros(r, c)
    for i in range(r):
        for k in range(m):
            if A[i][k]:
                for j in range(c):
                    C[i][j] += A[i][k] * B[k][j]
    return C


def mat_T(A):
    return [list(row) for row in zip(*A)]


def mat_eq(A, B):
    return (len(A) == len(B) and len(A[0]) == len(B[0])
            and all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0]))))


def bareiss_det(M):
    n = len(M)
    A = [row[:] for row in M]
    if n == 0:
        return 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:  # pivot swap (track sign)
            s = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if s is None:
                return 0
            A[k], A[s] = A[s], A[k]
            prev = -prev
        piv = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * piv - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = piv
    return A[n - 1][n - 1]


def cartan(n, edges):
    G = zeros(n, n)
    for i in range(n):
        G[i][i] = 2
    for (u, v) in edges:
        G[u][v] = G[v][u] = -1
    return G


# ---- 1. E6 / E7 Cartan Grams (branch at index 2 in both conventions) ----
E6_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (2, 5)]
E7_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (2, 6)]
G6 = cartan(6, E6_edges)
G7 = cartan(7, E7_edges)
assert bareiss_det(G6) == 3, bareiss_det(G6)     # disc(Q_P8) = 3
assert bareiss_det(G7) == 2, bareiss_det(G7)     # disc(Q_X9) = 2

# ---- 2. Distinguished inclusion: E6 = E7 minus long-arm end vertex (index 5) ----
sigma = [0, 1, 2, 3, 4, 6]
J = zeros(7, 6)
for j, s in enumerate(sigma):
    J[s][j] = 1
assert mat_eq(mat_mul(mat_mul(mat_T(J), G7), J), G6), "J must be an isometry"
print("isometry J^T G7 J == G6: OK")

# ---- 3. Primitivity via explicit splitting (coordinate projection is a left inverse) ----
R = zeros(6, 7)
for j, s in enumerate(sigma):
    R[j][s] = 1
I6 = [[1 if i == j else 0 for j in range(6)] for i in range(6)]
assert mat_eq(mat_mul(R, J), I6), "R J = I_6 missing: J not split"
print("primitivity (split mono, coker = Z): OK")

# ---- 4. Rank-1 orthogonal complement + Nikulin gluing ----
w = [2, 4, 6, 5, 4, 3, 3]
Gw = [sum(G7[i][j] * w[j] for j in range(7)) for i in range(7)]
assert all(Gw[s] == 0 for s in sigma), Gw          # w orthogonal to image
assert reduce(gcd, w) == 1, "w must be primitive"   # => S^perp = Z w (ranks match)
nrm = sum(w[i] * Gw[i] for i in range(7))
assert nrm == 6, nrm                                # disc(complement) = 6
glue_index = abs(w[5])
assert glue_index == 3, glue_index                  # [T : S + Z w] = |w_5| = 3
assert 3 * 6 == 2 * 3 * 3, "disc relation 3*dK = 2*d^2"
print("complement <w>=6, glue index 3, 3*6 = 2*3^2: OK")

# Explicit overlattice (isotropic gluing) lift: u in T with 3u = s + w, s in S.
s = [1, 2, 0, 1, 2, 0, 0]
assert s[5] == 0, "s must lie in the image S"
u = [1, 2, 2, 2, 2, 1, 1]
assert [s[i] + w[i] for i in range(7)] == [3 * u[i] for i in range(7)]
Gu = [sum(G7[i][j] * u[j] for j in range(7)) for i in range(7)]
assert sum(u[i] * Gu[i] for i in range(7)) % 2 == 0, "T is even"
# Discriminant classes a=[s/3] in A_S, b=[w/3] in A_K: order 3, isotropic sum.
# sS = S-coordinates of s (drop the zero slot 5); q(a) = (s,s)_S/9.
sS = [s[i] for i in [0, 1, 2, 3, 4]] + [s[6]]
srow = [sum(sS[i] * G6[i][j] for i in range(6)) for j in range(6)]
assert all(c % 3 == 0 for c in srow), srow          # s/3 in S^*
assert any(c % 3 != 0 for c in sS)                  # [s/3] != 0, order 3
normS = sum(sS[i] * sum(G6[i][j] * sS[j] for j in range(6)) for i in range(6))
qS = Fraction(normS, 9)
qK = Fraction(nrm, 9)
assert normS + nrm == 9 * sum(u[i] * Gu[i] for i in range(7)), "qS+qK must equal (u,u)"
assert (qS + qK) % 2 == 0, (qS, qK)                 # isotropic: qS+qK in 2Z
print("isotropic order-3 gluing lift (qS=%s, qK=%s, sum=%s): OK" % (qS, qK, qS + qK))

# ---- 5. Seifert data: explicit compatible unimodular pair, divisibility preserved ----
# Gabrielov/Seifert normalization: L + L^T = -G (G = positive Cartan Gram), det L = +-1.
# Correct choice: diag -1, strict-upper part = strict-upper part of -G (orientation by
# vertex order). (Naive "-G upper triangle" wrongly puts -2 on the diagonal.)
def seifert_upper(G):
    n = len(G)
    L = zeros(n, n)
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][j] = -1
            elif j > i:
                L[i][j] = -G[i][j]
    return L

LS, LT = seifert_upper(G6), seifert_upper(G7)
assert bareiss_det(LS) in (1, -1), "LS unimodular"
assert bareiss_det(LT) in (1, -1), "LT unimodular"
assert mat_eq([[LS[i][j] + LS[j][i] for j in range(6)] for i in range(6)],
              [[-G6[i][j] for j in range(6)] for i in range(6)]), "LS+LS^T == -G6"
assert mat_eq([[LT[i][j] + LT[j][i] for j in range(7)] for i in range(7)],
              [[-G7[i][j] for j in range(7)] for i in range(7)]), "LT+LT^T == -G7"
assert mat_eq(mat_mul(mat_mul(mat_T(J), LT), J), LS), "Seifert compatibility"
print("Seifert compatibility J^T LT J == LS, det = +-1: OK")


def div_of(L, x):
    n = len(L)
    row = [sum(x[i] * L[i][j] for i in range(n)) for j in range(n)]
    if all(c == 0 for c in row):
        return 0
    return reduce(gcd, [abs(c) for c in row if c != 0])


for i in range(6):  # distinguished basis vectors: divisibility 1 on both sides
    e = [1 if k == i else 0 for k in range(6)]
    Je = [J[r][i] for r in range(7)]
    assert div_of(LS, e) == 1 and div_of(LT, Je) == 1, (i, div_of(LS, e), div_of(LT, Je))
# Unimodularity => every primitive vector has divisibility 1, on both sides, hence
# div_T(Phi x) = 1 = div_S(x) for ALL primitive x (lemma in DRAFT.md).
print("Seifert divisibility 1 = 1 on distinguished bases (hence all primitives): OK")

print("VERIFY_OK")
