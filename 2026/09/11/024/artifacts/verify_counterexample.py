#!/usr/bin/env python3
"""Exact verification of the numeric certificates for the lane-709 TARGET disproof.

Target (FALSE): every origin-symmetric C^2 strictly convex K in R^3 with
d_BM(K,P) >= 1.1 satisfies |K||K^polar| >= 32/3 + 1e-3 (P = parallelepiped class).

Counterexample: K = {x : f(x) <= 1}, f(x) = sum_i sqrt(x_i^2+delta^2), delta = 1e-6.
Put r = 1 - 3*delta = 999997/10^6. The proof uses:
  (A) averaging identity m(a) = (1/8) sum_{s in {+-1}^3} |a.s|
      = max(|a|_1/2, |a|_inf), checked on a grid + random points
      (the DRAFT gives the analytic case-split proof; this is a sanity replay);
  (B) distance transfer (3/2)*r >= 1.1 as exact integers: 3*999997 >= 2200000;
  (C) product violation (32/3)/r^3 < 32/3 + 1e-3 as exact integers:
      32003*999997^3 > 32000*10^18;
  (D) sandwich sanity |x|_1 <= f(x) <= |x|_1 + 3*delta on random samples.
"""
import itertools
import random

# ---- (A) averaging identity ----
def m(a):
    return sum(abs(a[0]*s[0] + a[1]*s[1] + a[2]*s[2])
               for s in itertools.product((-1, 1), repeat=3)) / 8.0

random.seed(709)
pts = [tuple(v / 4.0 for v in t)
       for t in itertools.product(range(-12, 13), repeat=3)]
pts += [(random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(-3, 3))
        for _ in range(3000)]
worst = 0.0
for a in pts:
    lhs = m(a)
    rhs = max(sum(abs(v) for v in a) / 2.0, max(abs(v) for v in a))
    worst = max(worst, abs(lhs - rhs))
    assert abs(lhs - rhs) < 1e-9, (a, lhs, rhs)
print("A ok: averaging identity holds, max deviation =", worst)

# ---- (B) distance transfer: (3/2)*(999997/10^6) >= 11/10 ----
assert 3 * 999997 >= 2200000
print("B ok: (3/2)*(1-3e-6) >= 1.1, margin =", 3 * 999997 - 2200000)

# ---- (C) product violation ----
assert 32003 * 999997**3 > 32000 * 10**18
print("C ok: product-excess margin =", 32003 * 999997**3 - 32000 * 10**18)
print("    excess value (float) =", (32.0 / 3.0) * ((10**6 / 999997.0)**3 - 1.0))

# ---- (D) sandwich sanity ----
delta = 1e-6
for _ in range(20000):
    x = [random.uniform(-1.5, 1.5) for _ in range(3)]
    l1 = sum(abs(v) for v in x)
    f = sum((v * v + delta * delta) ** 0.5 for v in x)
    assert f >= l1 - 1e-12 and f <= l1 + 3 * delta + 1e-12, (x, l1, f)
print("D ok: |x|_1 <= f(x) <= |x|_1 + 3*delta on 20000 samples")

print("VERIFY_OK")
