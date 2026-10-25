"""Exact symbolic checks for the two-agent AdGT stability frontier.

Requires SymPy. This checks the characteristic polynomial and the exact
Schur/Jury inequalities used in RESULT.md; it is not an external certification.
"""
import sympy as sp

h1, h2, q, z = sp.symbols("h1 h2 q z", positive=True, real=True)
W = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)],
               [sp.Rational(1, 2), sp.Rational(1, 2)]])
H = sp.diag(h1, h2)
D = q * sp.diag(1 / h1, 1 / h2)
I2 = sp.eye(2)
T = sp.BlockMatrix([
    [W, -W * D],
    [H * (W - I2), W - H * W * D],
]).as_explicit()
xi = (h1 - h2) ** 2 / (4 * h1 * h2)
charpoly = sp.factor((z * sp.eye(4) - T).det())
expected = (z - 1) * z * (z**2 + (q - 1) * z + q * xi)
assert sp.simplify(charpoly - expected) == 0

# For r^2 + a*r + b, the real quadratic Schur conditions are
# |b| < 1, 1+a+b > 0, and 1-a+b > 0.
a = q - 1
b = q * xi
assert sp.simplify((1 + a + b) - q * (1 + xi)) == 0
assert sp.simplify((1 - a + b) - (2 - q * (1 - xi))) == 0

# Verify the two closed-form threshold branches at rational test points.
def xi_value(h1v, h2v):
    return (h1v - h2v) ** 2 / (4 * h1v * h2v)

def qcrit(x):
    if x <= sp.Rational(1, 3):
        return sp.Rational(2, 1) / (1 - x)
    return 1 / x

def roots_moduli(x, qv):
    poly = sp.Poly(z**2 + (qv - 1) * z + qv * x, z)
    return [complex(root.evalf()) for root in sp.nroots(poly)]

for h1v, h2v, qbelow, qabove in [
    (sp.Rational(2), sp.Rational(1), sp.Rational(11, 5), sp.Rational(23, 10)),
    (sp.Rational(5), sp.Rational(1), sp.Rational(6, 5), sp.Rational(13, 10)),
]:
    x = xi_value(h1v, h2v)
    threshold = qcrit(x)
    assert qbelow < threshold < qabove
    assert max(abs(v) for v in roots_moduli(x, qbelow)) < 1
    assert max(abs(v) for v in roots_moduli(x, qabove)) > 1

print("VERIFY_OK: characteristic polynomial, Jury identities, and two threshold tests")
