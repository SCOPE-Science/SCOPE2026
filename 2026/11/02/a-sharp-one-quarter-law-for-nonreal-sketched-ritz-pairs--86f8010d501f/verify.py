"""Exact identities and supplementary tests for the circular sketched Ritz law.

Run with Python 3 and SymPy. All probability and sharpness assertions
are proved analytically in RESULT.md; samples here are checks only.
"""
import math
import random
import sympy as sp

D, rho, tau, ph = sp.symbols('D rho tau ph', positive=True, real=True)
K = sp.diag(1, 1 + D)
r = sp.Matrix([rho / sp.sqrt(2), rho / sp.sqrt(2)])
g = sp.Matrix([tau * sp.cos(ph), tau * sp.sin(ph)])
H = K + g * r.T
disc = sp.expand(sp.trace(H)**2 - 4 * H.det())
expected = D**2 + rho**2 * tau**2 * sp.sin(ph + sp.pi / 4)**2 \
           - 2 * D * rho * tau * sp.cos(ph + sp.pi / 4)
assert sp.simplify(sp.trigsimp(disc - expected)) == 0

x = sp.symbols('x', positive=True, real=True)
h = (sp.sqrt(x**2 + 2) - 1) / x
assert sp.simplify(h.subs(x, sp.Rational(1, 2)) - 1) == 0
assert sp.simplify(h.subs(x, sp.sqrt(2)) - 1 / sp.sqrt(2)) == 0
assert sp.simplify(sp.diff(h, x) - (1 - 2 / sp.sqrt(x**2 + 2)) / x**2) == 0
assert sp.simplify((D**2 - 2*D*rho*tau).subs(tau, D/(2*rho))) == 0

z = sp.symbols('z', positive=True)
A = sp.Matrix([[1, 0, 1/sp.sqrt(2)],
               [0, 1 + z, 1/sp.sqrt(2)],
               [1/sp.sqrt(2), 1/sp.sqrt(2), 2]])
assert sp.simplify(A[:2, :2].det()) == 1 + z
assert sp.simplify(A.det() - (2 + 3*z)/2) == 0

rng = random.Random(4921)
checked = 0
for _ in range(4800):
    delta = sp.Rational(rng.randint(1, 20), rng.randint(22, 50))
    a, b = sp.Rational(rng.randint(1, 30), 20), sp.Rational(rng.randint(1, 30), 20)
    c, d = sp.Rational(rng.randint(1, 30), 20), sp.Rational(rng.randint(1, 30), 20)
    g1 = a if rng.randrange(2) else -a
    g2 = b if rng.randrange(2) else -b
    r1 = c
    r2 = d
    hmat = sp.Matrix([[1+g1*r1, g1*r2], [g2*r1,1+delta+g2*r2]])
    q = sp.factor(sp.trace(hmat)**2-4*hmat.det())
    q2 = (delta-g1*r1+g2*r2)**2+4*g1*g2*r1*r2
    assert sp.factor(q-q2)==0
    if q < 0:
        assert g1 > 0 and g2 < 0
    checked += 1

count = 0
n = 100000
for _ in range(n):
    angle = rng.random() * 2 * math.pi
    gg = math.sqrt(2) * math.cos(angle)
    hh = math.sqrt(2) * math.sin(angle)
    discval = (1 - gg/math.sqrt(2) + hh/math.sqrt(2))**2 + 2*gg*hh
    count += discval < -1e-12
assert abs(count / n - 0.25) < 0.007
print('PASS: symbolic identities, SPD determinant, 4800 exact cases, '
      f'{n} angular samples, observed rate {count/n:.6f}')
