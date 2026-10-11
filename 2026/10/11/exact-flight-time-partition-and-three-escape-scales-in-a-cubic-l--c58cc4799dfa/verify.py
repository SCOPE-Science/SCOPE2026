"""Reproduce exact polynomial identities for a cubic Lambda-Omega flow.

Run: python verify.py
Dependency: SymPy. Analytic integral and asymptotic proofs are in RESULT.md.
"""
import sympy as sp

x, y = sp.symbols("x y", real=True)
mu, k = sp.symbols("mu k", positive=True, real=True)
q = mu**2 + k
p = 1 + 2 * mu * y - k * y**2
P = -y * (1 + mu * y) + x * (mu * x - k * x * y)
Q = x * (1 + mu * y) + y * (mu * x - k * x * y)
H = (x**2 + y**2) / p
assert sp.cancel(sp.diff(H, x) * P + sp.diff(H, y) * Q) == 0
J = sp.Matrix([P, Q]).jacobian([x, y])
assert J.subs({x: 0, y: 0}) == sp.Matrix([[0, -1], [1, 0]])
assert sp.simplify(J.subs({x: 0, y: -1 / mu}) - sp.Matrix([[0, 1], [-q / mu**2, 0]])) == sp.zeros(2)
y_minus = -1 / (mu + sp.sqrt(q))
y_plus = 1 / (sp.sqrt(q) - mu)
for yi in (y_minus, y_plus):
    assert sp.simplify(p.subs(y, yi)) == 0
    assert sp.simplify(P.subs(y, yi) - (mu - k * yi) * (x**2 + yi**2)) == 0
assert sp.simplify(mu - k * y_minus - sp.sqrt(q)) == 0
assert sp.simplify(mu - k * y_plus + sp.sqrt(q)) == 0
b = -(k * x**2 + 1) / (2 * mu)
assert sp.simplify(k * (x**2 + b**2) + p.subs(y, b)) == 0
assert sp.simplify(P.subs(y, b) - ((1 + k * x**2)**2 + 4 * mu**2 * x**2) / (4 * mu)) == 0
assert sp.simplify(q * (x**2 + y**2) + p - (q * x**2 + (1 + mu * y)**2)) == 0
assert sp.simplify(k * (x**2 + y**2) + p - (k * x**2 + 1 + 2 * mu * y)) == 0
Fminus = sp.pi / (sp.sqrt(q) * abs(y_minus))
Fplus = sp.pi / (sp.sqrt(q) * abs(y_plus))
# Positivity permits rationalizing absolute values and evaluating the expressions directly.
Fminus = sp.pi * (mu + sp.sqrt(q)) / sp.sqrt(q)
Fplus = sp.pi * (sp.sqrt(q) - mu) / sp.sqrt(q)
assert sp.simplify(Fminus + Fplus - 2 * sp.pi) == 0
assert sp.simplify(Fminus - Fplus - 2 * sp.pi * mu / sp.sqrt(q)) == 0
print("CHECK_OK")
