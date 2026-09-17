import sympy as sp

k = sp.symbols("k", positive=True)
A = sp.diag(1, k)
g0 = sp.Matrix([1, 1 / k])
x0 = A.inv() * g0

def f(x):
    return sp.simplify((x.T * A * x)[0] / 2)

# Exact first steepest-descent / CG step.
d0 = -g0
alpha0 = sp.simplify(g0.dot(g0) / g0.dot(A * g0))
x1 = sp.simplify(x0 + alpha0 * d0)
g1 = sp.simplify(A * x1)
y0 = sp.simplify(g1 - g0)
s0 = sp.simplify(x1 - x0)

# Dai--Yuan direction.
beta = sp.simplify(g1.dot(g1) / d0.dot(y0))
d1 = sp.simplify(-g1 + beta * d0)

# AOS model matrix from the source definition.
c = sp.simplify(y0.dot(y0) / s0.dot(y0))
Bbar = sp.simplify(
    c * sp.eye(2)
    - c * (s0 * s0.T) / s0.dot(s0)
    + (y0 * y0.T) / s0.dot(y0)
)

alpha_exact = sp.simplify(-g1.dot(d1) / d1.dot(A * d1))
alpha_aos = sp.simplify(-g1.dot(d1) / d1.dot(Bbar * d1))
r = sp.factor(alpha_aos / alpha_exact)
x2 = sp.simplify(x1 + alpha_aos * d1)

expected_r = (k**2 + 1) / (2 * k)
expected_f1_f0 = k * (k - 1) ** 2 / ((k + 1) * (k**3 + 1))
expected_f2_f1 = (k - 1) ** 4 / (4 * k**2)
expected_f2_f0 = (k - 1) ** 6 / (4 * k * (k + 1) * (k**3 + 1))

assert sp.simplify(alpha0 - (k**2 + 1) / (k * (k + 1))) == 0
assert sp.simplify(r - expected_r) == 0
assert sp.simplify(f(x1) / f(x0) - expected_f1_f0) == 0
assert sp.simplify(f(x2) / f(x1) - expected_f2_f1) == 0
assert sp.simplify(f(x2) / f(x0) - expected_f2_f0) == 0
assert sp.limit((f(x2) / f(x0)) / k, k, sp.oo) == sp.Rational(1, 4)

print("alpha0 =", sp.factor(alpha0))
print("alpha_aos / alpha_exact =", r)
print("f1 / f0 =", sp.factor(f(x1) / f(x0)))
print("f2 / f1 =", sp.factor(f(x2) / f(x1)))
print("f2 / f0 =", sp.factor(f(x2) / f(x0)))
print("k=10: f2/f0 =", sp.N((f(x2) / f(x0)).subs(k, 10), 15))
print("lim_{k->infinity} (f2/f0)/k =", sp.Rational(1, 4))
