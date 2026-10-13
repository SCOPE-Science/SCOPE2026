from __future__ import annotations
import math
import sympy as sp

a, z, r = sp.symbols("a z r", positive=True)
x_plus = a + sp.sqrt(a) * z
x_minus = a - sp.sqrt(a) * z
ratio_geom = sp.simplify((x_plus / x_minus).subs(z, r * sp.sqrt(a)))
assert sp.simplify(ratio_geom - (1 + r) / (1 - r)) == 0

lhs = (a - 1) * sp.log((1 + r) / (1 - r)) - 2 * a * r
rhs = 2 * ((a - 1) * sp.atanh(r) - a * r)
diff = sp.simplify(lhs - rhs)
assert sp.simplify(sp.diff(diff, r)) == 0
assert sp.simplify(diff.subs(r, 0)) == 0

# Crossing expansion. Let e=1/a and s=kappa^2=3+c e+O(e^2).
e, c = sp.symbols("e c")
s = 3 + c * e
series_lhs = 1 + s * e / 3 + s**2 * e**2 / 5
series_rhs = 1 + e + e**2
coef_e2 = sp.expand(series_lhs - series_rhs).coeff(e, 2)
assert sp.solve(sp.Eq(coef_e2, 0), c) == [sp.Rational(-12, 5)]

def F(x: float) -> float:
    return math.atanh(x) / x

def crossing(alpha: float) -> float:
    lo, hi = 0.0, 1.0
    target = alpha / (alpha - 1.0)
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if F(mid) < target:
            lo = mid
        else:
            hi = mid
    return math.sqrt(alpha) * (lo + hi) / 2.0

for alpha in (1.1, 1.5, 2.0, 3.0, 10.0, 100.0, 1000.0):
    kappa = crossing(alpha)
    assert 1.0 < kappa < math.sqrt(3.0)
    approx = math.sqrt(3.0) * (1.0 - 2.0 / (5.0 * alpha))
    print(f"alpha={alpha:g} kappa={kappa:.12f} first_order={approx:.12f}")

print("VERIFY_OK")
