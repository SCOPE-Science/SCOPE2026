"""Exact monodromy and independent floating-point local-derivative checks.

Requires sympy. All identities central to the theorem use exact arithmetic.
The finite-difference tests are supplementary, not a proof of nonlinear stability.
"""
from fractions import Fraction
import sympy as sp

s = sp.symbols('s', real=True, positive=True)
t = sp.Rational(4, 5)
M = lambda r: sp.Matrix([[0, r], [-1, 2*r]])
P = sp.simplify(M(s) * M(t) * M(t))
P_expected = sp.Matrix([[-8*s/5, 44*s/25], [sp.Rational(4,5)-16*s/5, (88*s-32)/25]])
assert P == P_expected
assert M(t)**2 == sp.Matrix([[-t, 2*t*t], [-2*t, -t+4*t*t]])
assert sp.simplify(sp.trace(P)-(48*s-32)/25)==0
assert sp.simplify(P.det()-16*s/25)==0
assert sp.simplify((sp.eye(2)+P).det()-(64*s-7)/25)==0
assert sp.simplify((sp.eye(2)-P).det()-(57-32*s)/25)==0
assert sp.simplify(P*sp.ones(2,1)-sp.Matrix([4*s/25,(8*s-12)/25])) == sp.zeros(2,1)
assert sp.simplify(sp.det(sp.Matrix.hstack(sp.ones(2,1),P*sp.ones(2,1)))-(4*s-12)/25)==0
assert P.subs(s, sp.Rational(1,10)).eigenvals() == {
    (-68-2*sp.sqrt(906))/125: 1, (-68+2*sp.sqrt(906))/125: 1
}
assert (-68-2*sp.sqrt(906))/125 < -1
assert -1 < (-68+2*sp.sqrt(906))/125 < 0
assert sp.factor((sp.Rational(16,25)*s).subs(s,sp.Rational(7,64)))==sp.Rational(7,100)
# Three rounds of ordinary one-step proximal gradient multiply by (1-a_k).
for numer in range(1,1000):
    r=sp.Rational(numer,1000)
    stable = r > sp.Rational(7,64)
    det = sp.Rational(16,25)*r
    trace = (48*r-32)/25
    conds=(1-det>0, 1+det+trace>0, 1+det-trace>0)
    assert all(conds)==stable
    assert 0 < sp.Rational(16,25)*r < 1

def apg_step(x,z,curvature):
    beta=1/(1+abs(x-z))
    y=(1-beta)*x+beta*z
    Z=min(1,max(-1,2*(1-curvature)*y-x))
    X=(x+Z)/2
    return X,Z

def period(x,z,r):
    for curvature in (0.2,0.2,1-r):
        x,z=apg_step(x,z,curvature)
    return x,z

for r in (0.02,0.08,0.1,0.109375,0.12,0.4,0.8,0.99):
    T = [[float(v) for v in row] for row in P.subs(s,sp.Rational(str(r))).tolist()]
    for x0,z0 in ((1,0),(0,1),(1,1),(-1,2)):
        for h in (1e-5, 1e-7):
            x,z=period(h*x0,h*z0,r)
            refx=(T[0][0]*x0+T[0][1]*z0)*h
            refz=(T[1][0]*x0+T[1][1]*z0)*h
            assert abs(x-refx) < 100*h*h
            assert abs(z-refz) < 100*h*h
print('PASS: 12 symbolic exact identities, 999 exact Jury checks, 64 independent nonlinear derivative comparisons')
