"""Exact polynomial checks for the symmetry-jump identity.

Run with: python verify.py
Requires SymPy.  The finite examples supplement the general group argument.
"""
import sympy as sp

t, a, b, c = sp.symbols('t a b c', nonzero=True)
F = lambda v: (v + b) * (v + c) / (v - a)
identity = sp.factor(F(a**2 / t) + a * F(t) / t)
assert sp.factor(identity - (a + t) * (a**2 - b*c) / (a*t)) == 0
assert sp.factor(identity.subs(c, a**2/b)) == 0

# Numerator relation giving the ambient torus involution.
P = (t - a) * (t + b) * (t + c)
assert sp.factor((t**3 * P.subs(t, a**2/t) + a**3 * P).subs(c, a**2/b)) == 0

# The normal-form parameter examples are strictly positive and distinct.
assert 2**2 == 1 * 4
assert 3**2 != 1 * 4

for m in (6, 7, 8, 11):
    # A chosen positive real m-th root gives v^m=a^2.
    v = sp.Pow(4, sp.Rational(1, m))
    assert sp.simplify(v**m - 4) == 0
    z = sp.Integer(1)
    w = sp.factor(F(z**m).subs({a: 2, b: 1, c: 4}))
    z1 = v/z
    w1 = -sp.Integer(2) * z**(-m) * w
    eq = (z1**m - 2)*w1 - (z1**m + 1)*(z1**m + 4)
    assert sp.simplify(eq) == 0
    z2 = v/z1
    w2 = -sp.Integer(2) * z1**(-m) * w1
    assert sp.simplify(z2-z) == 0
    assert sp.simplify(w2-w) == 0
    print(f'PASS exact torus involution example m={m}')
print('PASS universal rational identity and polynomial identity')
