#!/usr/bin/env python3
"""Self-contained algebraic checks for the cubic global-center period formulas.

Python 3 + sympy. Analytic estimates for the infinite-amplitude limit
are proved in RESULT.md; symbolic identities alone do not prove them.
"""
import sympy as s

v, w, alpha, kappa = s.symbols('v w alpha kappa', real=True)
p = 1-alpha*v+kappa*v**2
assert s.simplify(s.diff(p, v) + alpha-2*kappa*v) == 0
# The primitive is (log(p) + alpha*int(dv/p))/(2*kappa).
# Therefore its exact derivative is v/p.
assert s.simplify(((s.diff(p, v)+alpha)/(2*kappa*p))-v/p) == 0

# Invert the analytic K(v) coordinate through cubic order.
K = s.integrate(s.series(v/p, v, 0, 5).removeO(), v)
w_of_v = s.series(v*s.sqrt(s.cancel(2*K/v**2)), v, 0, 4).removeO()
B, C = s.symbols('B C')
v_of_w = w+B*w**2+C*w**3
composition = s.series(w_of_v.subs(v, v_of_w), w, 0, 4).removeO().expand()
coeff = s.solve([composition.coeff(w, 2), composition.coeff(w, 3)], [B, C])
assert s.simplify(coeff[B]+alpha/3) == 0
assert s.simplify(coeff[C]-alpha**2/36-kappa/4) == 0
reciprocal = s.series(w/v_of_w.subs(coeff), w, 0, 3).removeO()
assert s.simplify(reciprocal.coeff(w, 1)-alpha/3) == 0
assert s.simplify(reciprocal.coeff(w, 2)-(alpha**2-3*kappa)/12) == 0
# Average sin^2 across one physical revolution = 1/2.
assert s.simplify(reciprocal.coeff(w, 2)/2-(alpha**2-3*kappa)/24)==0

# Angle transform: dv/p = (2/sqrt(Delta)) d theta.
D = s.symbols('D', positive=True, real=True)
angle = s.symbols('theta', real=True)
vs = (alpha+s.sqrt(D)*s.tan(angle))/(2*kappa)
ps = s.simplify(p.subs(v, vs))
ps = s.simplify(ps.subs(alpha**2, 4*kappa-D))
assert s.trigsimp(ps-D/(4*kappa*s.cos(angle)**2)) == 0
# I0=2*pi/sqrt(D); I1/I0=C after integral(log cos)=-pi*log 2.
z = s.symbols('z', real=True)
scaled_C = s.log(2)-s.log(1+z**2)/2+z*s.atan(z)
assert s.simplify(s.diff(scaled_C, z)-s.atan(z)) == 0
assert scaled_C.subs(z, 0)==s.log(2)
# Extreme velocity constants differ by alpha*pi/(kappa*sqrt(D)).
# Hence their ratio is exp(-pi*alpha/sqrt(D)).
angle_gap = s.pi
assert s.simplify(-kappa*(alpha*angle_gap/(kappa*s.sqrt(D))) + s.pi*alpha/s.sqrt(D)) == 0
print('CHECK_OK')
