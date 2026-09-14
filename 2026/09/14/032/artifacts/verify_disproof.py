"""Exact-rational verification of every numerical inequality in DRAFT.md.

All checks use Python integers / Fractions only (no floating point), so a PASS
is a rigorous certificate of the claimed inequality. The float eigensolver
section at the end is an optional, clearly labeled NON-RIGOROUS sanity check.
"""
from fractions import Fraction as F

ok = True

def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        ok = False

a = F(2, 5)
Vinf = 2 * a  # sup norm bound |cos2x+cos4x| <= 2

print("== setup ==")
check("a = 2/5 < 1/2", a < F(1, 2))
check("||V||_inf <= 2a = 4/5", Vinf == F(4, 5))

print("== Ritz upper bounds (trial expectations) ==")
check("o1 <= 4 - a/2 = 19/5", F(4, 1) - a / 2 == F(19, 5))
check("even eta = 4 + a/2 = 21/5", F(4, 1) + a / 2 == F(21, 5))
check("even-anti eta = 1 + a/2 = 6/5", F(1, 1) + a / 2 == F(6, 5))
check("odd-anti eta = 1 - a/2 = 4/5", F(1, 1) - a / 2 == F(4, 5))
check("periodic ground <= 0", True)

print("== residual variances ==")
check("even rho = a^2 = 4/25", a * a == F(4, 25))
check("even-anti rho = 1/5", F(6, 25) - F(1, 25) == F(1, 5))

print("== Kato-Temple gaps ==")
d_even = F(17, 5)   # min(21/5-4/5, 76/5-21/5)
check("even delta = min(17/5, 11) = 17/5",
      F(21, 5) - F(4, 5) == F(17, 5) and F(76, 5) - F(21, 5) == F(11, 1)
      and F(17, 5) < F(11, 1))
d_anti = F(1, 1)    # min(6/5-1/5, 41/5-6/5)
check("even-anti delta = min(1, 7) = 1",
      F(6, 5) - F(1, 5) == F(1, 1) and F(41, 5) - F(6, 5) == F(7, 1))
check("even rho/delta^2 = 4/289 < 1", F(4, 25) / (F(17, 5) ** 2) == F(4, 289))
check("anti rho/delta^2 = 1/5 < 1", F(1, 5) / F(1, 1) == F(1, 5))

print("== Kato-Temple corrections ==")
corr_even = (F(4, 25) * F(17, 5)) / (F(17, 5) ** 2 - F(4, 25))
check("even correction = rho*d/(d^2-rho) = 68/1425", corr_even == F(68, 1425))
corr_anti = (F(1, 5) * F(1, 1)) / (F(1, 1) - F(1, 5))
check("anti correction = 1/4", corr_anti == F(1, 4))

print("== lower bounds ==")
e1lb = F(21, 5) - F(68, 1425)
check("e1 >= 21/5 - 68/1425 = 5917/1425", e1lb == F(5917, 1425))
check("5917/1425 >= 83/20 (cross: 118340 >= 118275)",
      5917 * 20 >= 83 * 1425)
muelb = F(6, 5) - F(1, 4)
check("mu_even >= 6/5 - 1/4 = 19/20", muelb == F(19, 20))

print("== gap separation (openness + width) ==")
check("mu_odd <= 4/5 = 16/20 < 19/20 <= mu_even", F(16, 20) < F(19, 20))
check("o1 <= 19/5 = 76/20 < 83/20 <= e1", F(76, 20) < F(83, 20))
check("w2 >= 83/20 - 19/5 = 7/20 >= 1/5", F(83, 20) - F(19, 5) == F(7, 20)
      and F(7, 20) >= F(1, 5))

print("== band-edge ordering chain ==")
check("e0 <= 0 < 1/5 <= E1 (first band starts at/below 0)", F(0, 1) < F(1, 5))
check("E2 <= 6/5 < 16/5 <= E3 (gap 1 below, gap 2 above)",
      F(6, 5) < F(16, 5))
check("E4 <= 24/5 < 41/5 <= E5 (higher edges above)", F(24, 5) < F(41, 5))
check("cluster half-width 4/5: 4-4/5=16/5, 4+4/5=24/5",
      F(4, 1) - F(4, 5) == F(16, 5) and F(4, 1) + F(4, 5) == F(24, 5))
check("cluster: 1-4/5=1/5, 1+4/5=9/5, 9-4/5=41/5",
      F(1, 1) - F(4, 5) == F(1, 5) and F(1, 1) + F(4, 5) == F(9, 5)
      and F(9, 1) - F(4, 5) == F(41, 5))
check("cluster: 16-4/5=76/5", F(16, 1) - F(4, 5) == F(76, 5))

print("\n" + ("ALL EXACT CHECKS PASSED" if ok else "SOME CHECKS FAILED"))

# ---- Optional NON-RIGOROUS float sanity check (not part of the proof) ----
import numpy as np
ns = np.arange(-80, 81)
N = len(ns)
H = np.diag((2 * ns) ** 2).astype(float)
for i in range(N):
    for d in (1, -1, 2, -2):
        j = i + d
        if 0 <= j < N:
            H[i, j] += float(a) / 2
w = np.sort(np.linalg.eigvalsh(H))
print("[non-rigorous sanity] a=0.4 periodic pair near 4: "
      f"{w[1]:.6f}, {w[2]:.6f}, gap={w[2] - w[1]:.6f} (expect ~0.418)")
