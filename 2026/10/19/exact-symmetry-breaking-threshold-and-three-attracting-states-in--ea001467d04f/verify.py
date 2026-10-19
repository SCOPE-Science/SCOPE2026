"""Exact reproduction of the two-person stationary-state and stability certificates.
Requires Python 3 and SymPy. No network access or external data are used.
"""
import sympy as s

x, z, u, v, w = s.symbols('x z u v w')
a = s.Integer(1)
alpha = s.Rational(1, 4)
beta = s.Rational(1, 100)
rho = alpha / beta
h = s.sqrt(5)
field = s.Matrix([
    -(1-u)*(x-z)-u*(x-a),
    (1-v)*(x-z)-v*(z+a),
    alpha*(1-u)*x*x-beta*u*(x-z)**2,
    alpha*(1-v)*z*z-beta*v*(x-z)**2
])
J = field.jacobian((x,z,u,v))

def canonical(expr):
    return s.simplify(s.radsimp(s.expand(expr)))

def test_state(name, state, expected):
    sub = dict(zip((x,z,u,v), state))
    residuals = [canonical(f.subs(sub)) for f in field]
    assert all(r == 0 for r in residuals), (name, residuals)
    assert all(abs(float(e)) < 1.0000000001 for e in state[:2])
    assert all(0 < float(e) < 1 for e in state[2:])
    poly = J.subs(sub).charpoly(w).as_expr().expand()
    assert canonical(poly - expected) == 0, (name, canonical(poly - expected))
    return [canonical(k) for k in s.Poly(poly,w).all_coeffs()]

sym = (s.Rational(25,33), -s.Rational(25,33), s.Rational(25,29), s.Rational(25,29))
same_plus = (s.Rational(5,12)+h/4, -s.Rational(5,12)+h/4,
             s.Rational(85,122)+15*h/122, s.Rational(85,122)-15*h/122)
same_minus = (-same_plus[1], -same_plus[0], same_plus[3], same_plus[2])
cross_plus = (s.Rational(5,8)+h/8, -s.Rational(5,8)+h/8,
              s.Rational(65,82)+5*h/82, s.Rational(65,82)-5*h/82)
cross_minus = (-cross_plus[1], -cross_plus[0], cross_plus[3], cross_plus[2])
P_pol = (29*w+33)*(4356*w+725)*(126324*w*w+129925*w+6525)/s.Integer(15957752976)
P_same = w**4+s.Rational(325,144)*w**3+s.Rational(2020873,1264896)*w**2+s.Rational(78161,210816)*w+s.Rational(5,192)
P_cross = w**4+s.Rational(145,64)*w**3+s.Rational(238993,167936)*w**2+s.Rational(12923,83968)*w-s.Rational(5,512)
for name, state, target in (
        ('polarized', sym, P_pol), ('same +', same_plus, P_same),
        ('same -', same_minus, P_same),
        ('cross +', cross_plus, P_cross), ('cross -', cross_minus, P_cross)):
    test_state(name, state, target)

cc = s.Poly(P_same,w).all_coeffs()
_, c1,c2,c3,c4=cc
assert all(c > 0 for c in (c1,c2,c3,c4))
assert c1*c2-c3 == s.Rational(589252621,182145024)
assert c1*c2*c3-c3*c3-c1*c1*c4 == s.Rational(40962897209981,38399085379584)
assert s.Poly(P_cross,w).coeff_monomial(1) == -s.Rational(5,512)
assert all(k>0 for k in s.Poly(P_pol,w).all_coeffs())
# Full-sector determinant identity, independently symbolic in the ratio.
rr, bb, aa=s.symbols('rr bb aa',positive=True)
r=aa*rr/(rr+8); y=rr/(rr+4)
B=s.Matrix([[-y,aa+r],[2*rr*bb*(1-y)*r,-(rr+4)*bb*r*r]])
assert s.simplify(B.det()-bb*aa**2*rr**2*(rr-16)/(rr+8)**2)==0
# Direct verification of the branch-reduction identity using the two root relations.
ss,pp,qq=s.symbols('ss pp qq')
assert s.expand((a-pp)*pp**2-(a-qq)*qq**2-(pp-qq)*(a*(pp+qq)-(pp**2+pp*qq+qq**2))) == 0
print('PASS: five nonzero equilibria, exact spectra and quartic Routh certificates; symmetric threshold identity.')
