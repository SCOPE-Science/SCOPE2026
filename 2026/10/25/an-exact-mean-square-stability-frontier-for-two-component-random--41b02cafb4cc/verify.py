#!/usr/bin/env python3
"""Symbolic checks for the two-component random-reshuffling stability formula.
Requires Python 3 and SymPy. The proof in RESULT.md supplies the analytic argument.
"""
import sympy as sp

alpha, beta, eta, c, s, x = sp.symbols(
    "alpha beta eta c s x", positive=True, real=True
)
a, b, d = sp.symbols("a b d", real=True)

# One component step in each of two rank-one directions.
B1 = sp.Matrix([[1 - alpha * eta, 0], [0, 1]])
B2 = sp.Matrix([
    [1 - beta * eta * c**2, -beta * eta * c * s],
    [-beta * eta * c * s, 1 - beta * eta * s**2],
])
M = B2 * B1
X = sp.Matrix([[a, d], [d, b]])
Y = (M * X * M.T + M.T * X * M) / 2
T = sp.Matrix([Y[0, 0], Y[1, 1], Y[0, 1]]).jacobian([a, b, d])
det_general = sp.factor((sp.eye(3) - T).det())

F1 = 2 * alpha * beta * eta - 2 * (alpha + beta) - alpha**2 * beta**2 * x * (1 - x) * eta**3
F2 = (
    alpha**2 * beta**2 * x * eta**4
    - alpha * beta * (alpha + beta) * x * eta**3
    - 2 * alpha * beta * eta**2
    + 4 * (alpha + beta) * eta
    - 8
)
expected = alpha * beta * eta**3 * (1 - x) * F1 * F2 / 4
assert sp.simplify(
    det_general.subs({c: sp.sqrt(x), s: sp.sqrt(1 - x)}) - expected
) == 0

# Exact illustrative specialization: alpha=2, beta=1, x=1/2.
z = sp.Symbol("z")
p = 2*z**4 - 3*z**3 - 4*z**2 + 12*z - 8
F1_example = -z**3 + 4*z - 6
critical = 2 / sp.sqrt(3)
assert sp.simplify(F1_example.subs(z, critical) - (16 / (3 * sp.sqrt(3)) - 6)) == 0
assert sp.simplify(16 / (3 * sp.sqrt(3)) - 6) < 0
assert p.subs(z, 1) == -1
assert p.subs(z, sp.Rational(3, 2)) == 1

# Sturm's theorem certifies exactly one positive real root of p.
sequence = sp.sturm(p, z)
def sign_at_zero(poly):
    return sp.sign(sp.simplify(poly.subs(z, 0)))
def sign_at_plus_infinity(poly):
    return sp.sign(sp.Poly(poly, z).LC())
def variations(signs):
    signs = [int(v) for v in signs if v != 0]
    return sum(signs[i] != signs[i-1] for i in range(1, len(signs)))
V0 = variations([sign_at_zero(q) for q in sequence])
Vinf = variations([sign_at_plus_infinity(q) for q in sequence])
assert V0 - Vinf == 1

root = [r for r in sp.nroots(p, maxsteps=200) if abs(sp.im(r)) < 1e-12 and sp.re(r) > 0]
assert len(root) == 1
assert 1 < float(sp.re(root[0])) < 1.5
print("PASS: exact determinant factorization")
print("PASS: example F1 has no positive root")
print("PASS: Sturm count gives one positive F2 root in (1, 3/2)")
print("PASS: numerical root approximation =", float(sp.re(root[0])))
