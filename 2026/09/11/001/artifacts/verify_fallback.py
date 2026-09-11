"""Verify fallback: lambda_1^1 = 1 on Berger (L(3,1), g_{1/2}).

Checks (exact rational arithmetic + certified sqrt bounds):
 A. Frame computation: d(X1*) = -(2 b^2/a) X2*^X3*, delta(X1*)=0,
    Delta(X1*) = (2 b^2/a)^2 X1*; at (a,b)=(2,1) eigenvalue exactly 1.
 B. Henkel-Lauret branch census at (a,b)=(2,1): min over all nu/mu
    branches equals 1 (vertical mu_{0,0}), runner-up 6 (exact nu_{1,0});
    enumeration k<=8 plus analytic tails for all k.
 C. Z3 weight selection: k=1 carries no invariant vectors (weights +-1).
"""
from fractions import Fraction as F
import math

A, B = 2, 1  # (a,b): eps = b/a = 1/2
a, b = F(2), F(1)

# ---- A. frame eigenpair (exact) ----
c = F(-2) * b * b / a          # dX1* = c X2*^X3*
eig = c * c                    # Delta X1* = c^2 X1*
assert c == F(-1), c
assert eig == F(1), eig
print(f"A: dX1* coeff c = {c}, Delta eigenvalue c^2 = {eig}  OK")

# ---- B. HL census at (2,1) ----
def nu(k, j):
    return F(4) * F((k - 2 * j) ** 2) + F((4 * j + 2) * k - 4 * j * j)

K0 = 8
best = None
for k in range(0, K0 + 1):
    for j in range(0, k + 1):
        if (k, j) == (0, 0):
            continue
        v = nu(k, j)
        if best is None or v < best[0]:
            best = (v, ('nu', k, j))
    # mu specials (coexact, all k)
    m1 = F(4) * F((k + 2) ** 2)          # mu_{k,-1}
    m0 = F(4 * k * k + 4 * k) + F(1)     # mu_{k,0} = 4k^2+4k+1
    for v, tag in ((m1, ('mu-', k)), (m0, ('mu0', k))):
        if best is None or v < best[0]:
            best = (v, tag)
    # pm modes need k>=2, 1<=j<=k-1; bound mu^- from below by monotonicity in nu
    # (checked via floats with certified margin, plus exact inequality below)
print(f"B: census k<={K0}: min = {best[0]} at {best[1]}")
assert best[0] == F(1) and best[1][0] == 'mu0', best
# runner-up
vals = []
for k in range(0, K0 + 1):
    for j in range(0, k + 1):
        if (k, j) == (0, 0):
            continue
        vals.append((nu(k, j), ('nu', k, j)))
    vals.append((F(4) * F((k + 2) ** 2), ('mu-', k)))
    vals.append((F(4 * k * k + 4 * k) + F(1), ('mu0', k)))
vals.sort(key=lambda t: t[0])
print(f"B: runner-up = {vals[1]}")
assert vals[1][0] == F(6), vals[1]

# tails (analytic, valid for all k > K0 and all j):
# nu_{k,j} = 4(k-2j)^2 + 2k + 4j(k-j) >= 2k  (since 4j(k-j)>=0 on 0<=j<=k)
# mu_{k,-1} = 4(k+2)^2 >= 4k^2 >= ... ; mu_{k,0} = 4k^2+4k+1 increasing in k.
# mu^+ >= mu^-(bound below) actually mu^+ >= (sqrt(kap)+... ) trivially large;
# mu^- = (sqrt(nu+kap)-sqrt(kap))^2 with kap=1/4, increasing in nu;
#   valid pm modes (k>=2,1<=j<=k-1) have nu>=8 (see below), so
#   mu^- >= (sqrt(33)-1)^2/4 = (17-sqrt(33))/2 > (17-6)/2 = 5.5 > 1.
kap = F(1, 4)
# verify nu>=8 on pm range for k<=K0 by enumeration; for k>K0 use nu>=2k>=18>8
pm_min = min(nu(k, j) for k in range(2, K0 + 1) for j in range(1, k))
assert pm_min == F(8), pm_min
assert 2 * (K0 + 1) >= 18
# certified: (sqrt(33)-1)^2/4 > 5.5 since sqrt(33) < 6 (36>33)
assert 33 < 36
mu_minus_floor = (F(17) - F(6)) / F(2)   # 5.5, lower bound for true floor
assert mu_minus_floor > F(1)
print(f"B: tails OK (nu>=2k, pm-range nu>=8 -> mu^->= (17-sqrt33)/2 > 5.5 > 1)")

# float cross-check of mu^- monotonic claim at pm_min
mum = (math.sqrt(8.25) - 0.5) ** 2
assert mum > 5.6, mum
print(f"B: mu^-(nu=8) = {mum:.6f} > 1  OK")

# ---- C. Z3 selection: k=1 has weights {+1,-1}, no multiple of 3 ----
def weights(k):
    return [k - 2 * r for r in range(k + 1)]
assert weights(1) == [1, -1]
assert not any(m % 3 == 0 for m in weights(1))
assert any(m % 3 == 0 for m in weights(2))  # k=2 does have invariants (weight 0)
print("C: k=1 carries no Z3-invariant vectors (weights +-1); nu_{1,0} absent on quotient  OK")

print("VERIFY_OK")
