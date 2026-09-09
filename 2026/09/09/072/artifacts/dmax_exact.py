"""Exact d=0 proof via lattice-max formula (no analysis, no floats).
Dai Thm 2.9: d(Y) = max_{x in L} (|G| + k'(x)^2)/4, k'(x) = K + 2Mx, pairing via M^{-1}.
Key identity: k'(x)^2 = K^2 - 8 chi(x), so d = -2 min chi.
Square identity: chi(x) = chi(xs) - q/2, q = (x-xs)^T M (x-xs), M xs = -K/2.
Since M neg-def (exact Sylvester), q <= 0; chi(xs) = -5/8 exactly;
chi integer-valued (K characteristic) => min chi = 0 (attained at x=0).
Hence d = 0 exactly.
"""
from fractions import Fraction

M = [[-1,1,1,1,0],[1,-2,0,0,0],[1,0,-3,0,0],[1,0,0,-7,1],[0,0,0,1,-2]]
K = [-1,0,1,5,0]
n = 5

def det(A):
    m = len(A); B = [[Fraction(A[i][j]) for j in range(m)] for i in range(m)]
    d = Fraction(1)
    for i in range(m):
        p = next(r for r in range(i, m) if B[r][i] != 0)
        if p != i:
            B[i], B[p] = B[p], B[i]; d = -d
        d *= B[i][i]; piv = B[i][i]
        for r in range(i + 1, m):
            f = B[r][i] / piv
            for c in range(i, m):
                B[r][c] -= f * B[i][c]
    return d

# 1. exact negative-definiteness via Sylvester on -M
N = [[-M[i][j] for j in range(n)] for i in range(n)]
minors = [det([row[:k] for row in N[:k]]) for k in range(1, n + 1)]
print("leading principal minors of -M:", minors)
assert all(m > 0 for m in minors), "Sylvester failed"
print("PASS -M positive definite (exact Sylvester)")

# 2. det, K characteristic
print("det M =", det(M))
assert det(M) == -1
assert all((K[v] - M[v][v]) % 2 == 0 for v in range(n))
print("PASS det=-1, K characteristic (exact)")

# 3. xs = -M^{-1}K/2 = (4,2,3/2,1,1/2); verify M xs = -K/2 exactly
xs = [Fraction(4), Fraction(2), Fraction(3, 2), Fraction(1), Fraction(1, 2)]
Mxs = [sum(M[i][j] * xs[j] for j in range(n)) for i in range(n)]
assert Mxs == [Fraction(-K[i], 2) for i in range(n)]
print("PASS M xs = -K/2 (exact)")

# 4. chi(xs) = -5/8 exactly
def chi(t):
    Mt = [sum(M[i][j] * t[j] for j in range(n)) for i in range(n)]
    return Fraction(-(sum(K[i] * t[i] for i in range(n)) + sum(t[i] * Mt[i] for i in range(n))), 2)
print("chi(xs) =", chi(xs))
assert chi(xs) == Fraction(-5, 8)

# 5. square identity on samples: chi(t) = chi(xs) - q/2
import random
random.seed(7)
for _ in range(200):
    t = [random.randint(-15, 15) for _ in range(n)]
    d = [Fraction(t[i]) - xs[i] for i in range(n)]
    Md = [sum(M[i][j] * d[j] for j in range(n)) for i in range(n)]
    q = sum(d[i] * Md[i] for i in range(n))
    assert chi(t) == chi(xs) - q / 2
print("PASS square identity chi(x)=chi(xs)-q/2 on 200 exact samples")

# 6. conclude: q<=0 (neg-def) => chi(x) >= -5/8; chi integer => chi >= 0; chi(0)=0.
assert chi([0]*n) == 0
print("PASS chi(0)=0; hence min chi = 0 and d = -2 min chi = 0 (exact)")
print("CONCLUSION d(+Sigma(2,3,13)) = 0, exact rational proof.")
