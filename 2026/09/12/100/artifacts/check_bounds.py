"""Reproducible numeric check for the thinned-subfield disproof (TARGET route).

Majorant failure bound M(r) = 4*exp(-r^2/48) + 56/r^2 + 6*r^4*2^(-c*sqrt(r)),
c = 2^(-1/4), valid for r >= 6561 (all Chernoff bases <= 1/2 there).
M is decreasing for r >= 200, and M(6561) < 1 certifies existence of a good
sample for every r >= 6561 (hence an infinite capped family violating the
N^{3/2-1/20} bound for every absolute C).
All evaluations use log-space where magnitudes could under/overflow.
"""
import math

C_PRIME = 2 ** (-0.25)  # A(r) >= c'*sqrt(r) since Ndet >= r^2/2


def log2_term_last(r):
    # log2 of 6*r^4*2^(-c*sqrt(r))
    return math.log2(6) + 4 * math.log2(r) - C_PRIME * math.sqrt(r)


def M_total(r):
    t1 = 4 * math.exp(-r * r / 48.0) if r * r / 48.0 < 700 else 0.0
    t2 = 16.0 / r
    t3 = 2.0 ** log2_term_last(r)
    return t1 + t2 + t3, t1, t2, t3


def A_lower(r):
    return (r * r / 2.0) ** 0.25  # <= true A(r) = floor(3r^2/4)^{1/4}


r0 = 6561
print("c' =", C_PRIME)
print("A_lower(6561) =", A_lower(r0), " vs 2e(1+1/r) =", 2 * math.e * (1 + 1 / r0))
tot, t1, t2, t3 = M_total(r0)
print(f"M(6561) = {tot:.6e}  (size={t1:.2e}, cheb={t2:.3e}, cap={t3:.2e})")
assert A_lower(r0) > 2 * math.e * (1 + 1 / r0)
assert tot < 1.0
# monotonicity: d/ds [8 ln s - c s ln2] < 0 iff s > 8/(c ln2)
s_thresh = 8 / (C_PRIME * math.log(2))
print("cap-majorant decreasing for sqrt(r) >", s_thresh,
      "-> holds for all r >=", math.ceil(s_thresh ** 2))
assert math.ceil(s_thresh ** 2) <= r0
# other terms plainly decreasing in r; spot-check a larger value
for r in [r0, 3 ** 9, 3 ** 10, 3 ** 12]:
    tot, _, _, _ = M_total(r)
    print(f"r={r}: M={tot:.3e}")
# violation ratio r^{1/10}/(8C): r needed to beat given C
for C in [1, 10, 1000]:
    k = next(k for k in range(8, 300) if (3 ** k) ** 0.1 / (8 * C) > 1)
    print(f"C={C}: ratio>1 from k={k} (r=3^{k})")
# Ndet <= q^{3/2} sanity
assert (3 * r0 * r0) // 4 <= r0 ** 3
print("OK: existence certified for all r = 3^k >= 6561; Ndet <= q^{3/2}.")
