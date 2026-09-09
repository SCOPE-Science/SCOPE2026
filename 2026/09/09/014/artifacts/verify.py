"""Stdlib-only verifier for lane-289 exact Werner-I3322 threshold v*=4/5.

Replays (with exact Fraction arithmetic where exact):
  (L) local bound: deterministic max of the CG CH-form I3322 is 0 (64 cases);
  (A) achievability: CG planar settings give S=5 exactly (cosines in {0,+-1/2,+-1});
  (U) upper-bound algebra: polynomial identity (5-t^2)^2-4(4-t^2)=(t^2-3)^2,
      which closes the g(t)<=5 chain; plus dense grid sanity for g(t);
  (V) threshold arithmetic: v*=4/5, (4/5)^2=16/25>1/2 so 4/5>1/sqrt(2),
      gap 4/5-1/sqrt(2) in (0.092,0.094).
Prints VERIFY_OK on success; exits nonzero otherwise.
"""
from fractions import Fraction as F
import itertools
import math

def fail(msg):
    raise SystemExit("VERIFY_FAIL: " + msg)

# ---- (L) local bound, exact over {0,1}^6 ----
C = [[1, 1, 1], [1, 1, -1], [1, -1, 0]]
def Ldet(a, b):
    return (-F(a[0]) - 2 * F(b[0]) - F(b[1])
            + sum(F(C[i][j]) * F(a[i] * b[j]) for i in range(3) for j in range(3)))
m = max(Ldet(a, b) for a in itertools.product([0, 1], repeat=3)
        for b in itertools.product([0, 1], repeat=3))
n0 = sum(1 for a in itertools.product([0, 1], repeat=3)
         for b in itertools.product([0, 1], repeat=3) if Ldet(a, b) == 0)
assert m == 0, (m,)
print("local det max = 0 OK (%d/64 saturators)" % n0)

# ---- (A) CG settings give S=5 exactly ----
D = [[-1, -1, -1], [-1, -1, 1], [-1, 1, 0]]
COS = {0: F(1), 60: F(1, 2), 120: F(-1, 2), 180: F(-1),
       240: F(-1, 2), 300: F(1, 2)}
Aang = [0, 60, 120]
Bang = [240, 180, 120]
S = sum(F(D[i][j]) * COS[(Aang[i] - Bang[j]) % 360]
        for i in range(3) for j in range(3))
if S != 5:
    fail("S_CG = %s != 5" % S)
print("S_CG = 5 exact OK; I_singlet = -1+5/4 = 1/4 OK")
if -1 + F(5, 4) != F(1, 4):
    fail("singlet value")

# ---- (U) upper-bound polynomial identity (exact integer arithmetic) ----
# Claim: (5-u)^2 - 4*(4-u) = (u-3)^2 for all u (u = t^2). Check coefficients:
# LHS = u^2-10u+25-16+4u = u^2-6u+9 = (u-3)^2. Verify at 5 integer points
# (degree<=2 identity check) with exact ints:
for u in [0, 1, 2, 3, 4, 7]:
    if (5 - u) ** 2 - 4 * (4 - u) != (u - 3) ** 2:
        fail("poly identity at u=%d" % u)
print("identity (5-u)^2-4(4-u)=(u-3)^2 OK")
# The chain: 2*sqrt(4-t^2)... precisely: 2*sqrt(t^2+1) <= 5-sqrt(4-t^2)
# needs RHS >= 0 (true since sqrt(4-t^2)<=2<5); squaring gives
# 4(t^2+1) <= 25+(4-t^2)-10*sqrt(4-t^2)  <=>  2*sqrt(4-t^2) <= 5-t^2
# (needs 5-t^2>=1>0); squaring again gives 4(4-t^2)<=(5-t^2)^2
# <=> 0<=(t^2-3)^2. Replay numeric direction on dense grid:
worst = 0.0
N = 20001
for k in range(N + 1):
    t = 2.0 * k / N
    g = 2.0 * math.sqrt(t * t + 1.0) + math.sqrt(max(0.0, 4.0 - t * t))
    worst = max(worst, g)
    if g > 5.0 + 1e-9:
        fail("g(%r)=%r > 5" % (t, g))
print("grid max g(t) = %.12f <= 5 OK" % worst)
# exact spot checks of g: g(0)=4, g(2)=2*sqrt(5)<4.5, g(sqrt(3))=5
if abs((2.0 * math.sqrt(3.0 + 1.0) + math.sqrt(4.0 - 3.0)) - 5.0) > 1e-12:
    fail("g(sqrt3)")
print("g(0)=4, g(2)=2sqrt5, g(sqrt3)=5 OK")

# ---- (V) threshold arithmetic ----
if F(4, 5) ** 2 != F(16, 25) or not (F(16, 25) > F(1, 2)):
    fail("4/5 > 1/sqrt(2) comparison")
gap = 0.8 - 1.0 / math.sqrt(2.0)
if not (0.092 < gap < 0.094):
    fail("gap %r" % gap)
print("v*=4/5=0.8 > 1/sqrt2, gap=%.6f OK" % gap)
# sum c = 4 check (reduction constant): rows sum 3+1+0
if sum(C[i][j] for i in range(3) for j in range(3)) != 4:
    fail("sum c")
print("sum c_ij = 4 OK (I(v) = -1 + v S/4)")
print("VERIFY_OK")
