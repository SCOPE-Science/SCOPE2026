import sympy as sp

x, y = sp.symbols("x y", nonzero=True)
a, b, c = sp.symbols("a b c")
A, B, C = sp.symbols("A B C")
alpha, delta = sp.symbols("alpha delta")

# Holling type-II model.
alpha_H = alpha + y/(1-x**4) * (A/(B+x) - a/(b+x))
delta_H = delta + x * (C/(B+x) - c/(b+x))

old_x_H = alpha*x*(1-x**4) - a*x*y/(b+x)
old_y_H = c*x*y/(b+x) - delta*y
new_x_H = alpha_H*x*(1-x**4) - A*x*y/(B+x)
new_y_H = C*x*y/(B+x) - delta_H*y

holling_x_residual = sp.factor(sp.simplify(new_x_H - old_x_H))
holling_y_residual = sp.factor(sp.simplify(new_y_H - old_y_H))

# Ratio-dependent model.
alpha_R = alpha + y/(1-x**4) * (A/(B*y+x) - a/(b*y+x))
delta_R = delta + x * (C/(B*y+x) - c/(b*y+x))

old_x_R = alpha*x*(1-x**4) - a*x*y/(b*y+x)
old_y_R = c*x*y/(b*y+x) - delta*y
new_x_R = alpha_R*x*(1-x**4) - A*x*y/(B*y+x)
new_y_R = C*x*y/(B*y+x) - delta_R*y

ratio_x_residual = sp.factor(sp.simplify(new_x_R - old_x_R))
ratio_y_residual = sp.factor(sp.simplify(new_y_R - old_y_R))

# Algebra behind a simple identifiability repair when alpha(t) is known.
r_H = a/(b+x)
repair_H = sp.factor(sp.simplify(1/r_H - (x/a + b/a)))

r_R = a/(b*y+x)
repair_R = sp.factor(sp.simplify(1/r_R - (x/a + b*y/a)))

checks = {
    "holling_x_residual": holling_x_residual,
    "holling_y_residual": holling_y_residual,
    "ratio_x_residual": ratio_x_residual,
    "ratio_y_residual": ratio_y_residual,
    "known_alpha_holling_affine_identity": repair_H,
    "known_alpha_ratio_affine_identity": repair_R,
}
for name, value in checks.items():
    print(f"{name} = {value}")

passed = all(value == 0 for value in checks.values())
print(f"all_symbolic_checks_passed = {passed}")
if not passed:
    raise SystemExit(1)
