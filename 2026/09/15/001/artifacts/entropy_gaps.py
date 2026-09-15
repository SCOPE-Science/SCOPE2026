"""Reproducible verification of entropy-gap numerics for lane-20111.

Checks (mpmath, 80 digits):
1. nu_cyl(3) = log 2 - 1 exactly (closed form for S^2_{sqrt(2)} x R).
2. eps_3 = 0.2 separates the cylinder from every other 3D noncompact shrinker
   entropy value: R^3-type (-log|G|) and cylinder-quotient-type (log2-1-log|G|).
3. Context table of product entropies nu(S^k) for general n (shows why the
   classification route does not extend: nearest-product gaps shrink with n,
   and non-product families are unaccounted for).
"""
import mpmath as mp

mp.mp.dps = 80

def nu_sphere(k):
    k = int(k)
    if k == 0:
        return mp.mpf(0)
    r = mp.sqrt(2 * (k - 1))
    vol_unit = 2 * (mp.pi ** (mp.mpf(k + 1) / 2)) / mp.gamma(mp.mpf(k + 1) / 2)
    return mp.log(vol_unit * (r ** k) / ((4 * mp.pi) ** (mp.mpf(k) / 2))) - mp.mpf(k) / 2

# 1. closed form
val = nu_sphere(2)
assert abs(val - (mp.log(2) - 1)) < mp.mpf(10) ** (-70), (val, mp.log(2) - 1)
print("nu_cyl(3) =", val)
print("log2 - 1  =", mp.log(2) - 1, " MATCH")

# 2. eps_3 = 0.2 validity: competitor distances
eps = mp.mpf("0.2")
cyl = mp.log(2) - 1
d_gauss = abs(mp.mpf(0) - cyl)          # R^3
d_cylquot = mp.log(2)                   # |(cyl - log|G|) - cyl|, |G|>=2 minimal
d_gaussquot = mp.log(2) - abs(cyl)      # |-log|G| - cyl|, |G|>=2 minimal
print("dist(R^3) =", d_gauss)
print("dist(cyl quotients,|G|>=2) >=", d_cylquot)
print("dist(Gauss quotients,|G|>=2) >=", d_gaussquot)
assert d_gauss > eps and d_cylquot > eps and d_gaussquot > eps
print("eps_3 = 0.2 VALID: all competitor distances exceed 0.2")

# 3. context table
print("\n n | nu_cyl(n) | nearest-product gap | Gauss gap")
for n in [3, 4, 5, 6, 7, 8]:
    c = nu_sphere(n - 1)
    pg = min([abs(nu_sphere(k) - c) for k in range(2, n - 1)], default=None)
    print(f" {n} | {float(c):+.8f} | {('%.6f' % float(pg)) if pg is not None else 'none-only-cylinder'} | {float(-c):.6f}")
print("\nALL CHECKS PASSED")
