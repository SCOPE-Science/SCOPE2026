import sympy as sp

x = sp.symbols("x", positive=True)
r = sp.sqrt(1 + x**2) - 1
F = sp.simplify(r / (1 + r - r**2))

leading = sp.limit(F / x**2, x, 0)
quartic = sp.limit((F - x**2 / 2) / x**4, x, 0)
duration = sp.limit((1 / F - 1 / x) * x**2, x, 0)

assert leading == sp.Rational(1, 2), leading
assert quartic == -sp.Rational(3, 8), quartic
assert duration == 2, duration

print("F_over_x2_limit=1/2")
print("quartic_coefficient=-3/8")
print("tau_times_x2_limit=2")
print("VERIFY_OK")
