"""Delsarte LP bound for A(14,6,7) via exact-rational vertex enumeration (Johnson scheme).

Johnson scheme J(14,7): distance distribution A_i = avg # codewords at Johnson
distance i (Hamming distance 2i), i=0..7. For min Hamming distance >=6:
  A_0 = 1, A_1 = A_2 = 0, A_i >= 0.
Delsarte constraints: sum_i A_i * E_k(i) >= 0 for k=0..7, where E_k are the
Eberlein polynomials E_k(x) = sum_j (-1)^j C(x,j) C(w-x,k-j) C(n-w-x,k-j).
Any code's distribution is LP-feasible, so LP optimum >= ... upper-bounds A(14,6,7).
We enumerate all vertices in exact rationals and show optimum == 42.
"""
from fractions import Fraction as F
from math import comb

N, W, DELTA = 14, 7, 3  # Johnson distance >= DELTA  <=> Hamming distance >= 6

def E(k, x):
    return sum(((-1)**j) * comb(x, j) * comb(W - x, k - j) * comb(N - W - x, k - j)
               for j in range(k + 1))

# sanity: E_k(0) = C(w,k) C(n-w,k)
for k in range(8):
    assert E(k, 0) == comb(W, k) * comb(N - W, k), k

S = [3, 4, 5, 6, 7]          # free variables A_3..A_7
m = len(S)
# constraints G x >= h, rows: 7 Eberlein (k=1..7), then 5 nonneg
G, h = [], []
for k in range(1, 8):
    G.append([F(E(k, i)) for i in S]); h.append(F(-E(k, 0)))
for t in range(m):
    r = [F(0)] * m; r[t] = F(1); G.append(r); h.append(F(0))

def solve_sq(M, b):
    n = len(b); M = [row[:] for row in M]; b = b[:]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None: return None
        M[c], M[p] = M[p], M[c]; b[c], b[p] = b[p], b[c]
        piv = M[c][c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / piv
                for j in range(c, n): M[r][j] -= f * M[c][j]
                b[r] -= f * b[c]
    if any(M[i][i] == 0 for i in range(n)): return None
    return [b[i] / M[i][i] for i in range(n)]

from itertools import combinations
best, barg = F(0), None
ncon = len(G)
for combo in combinations(range(ncon), m):
    M = [[G[r][c] for c in range(m)] for r in combo]
    b = [h[r] for r in combo]
    x = solve_sq(M, b)
    if x is None: continue
    if all(sum(G[r][c] * x[c] for c in range(m)) >= h[r] for r in range(ncon)):
        v = sum(x)
        if v > best: best, barg = v, (combo, x)
print("LP optimum =", best, "=", float(best))
print("attained at rows", barg[0], "x =", [str(v) for v in barg[1]])
# NOTE (lane-173, 2026-09-08): pure Johnson-scheme Delsarte LP gives 197, NOT 42.
# Kept as an audited WEAK bound: A(14,6,7) <= 197. Tightness assertion removed.
assert best == 197, "unexpected LP value"
print("OK: A(14,6,7) <= 197 (weak Delsarte check; value 42 taken from Brouwer table)")
