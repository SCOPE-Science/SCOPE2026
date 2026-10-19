#!/usr/bin/env python3
"""Exact symbolic checks for the three-species symmetric interaction-modifier theorem.

Requires Python 3 and SymPy. Run: python verify.py
Finite sample checks supplement rather than replace the analytic proof.
"""
import sympy as sp

m, w, ell = sp.symbols('m w ell', real=True)
den = 4*m*m + 9
u = (6*m + 7)/den
v = (2*m + 11)/den
z = (4*m*m + 8*m + 1)/den
beta = (m-1)/z
S = sp.factor(u+v+z)
Q = sp.factor(u*v + u*z + v*z + 4*m*m*u*v + 4*(u+v)*z)
R = sp.factor(u*v*z*(9+4*m*m))
C1 = sp.factor(Q-8*beta*u*v*z)
D1 = sp.factor(R+4*beta*u*v*z*(2*m*(u-v)-u-v))
A = S+w
B = Q+S*w
C = R+C1*w
D = D1*w
P = ell**4+A*ell**3+B*ell**2+C*ell+D
J = sp.Matrix([
    [-u, 2*m*u, -2*u, 2*u*v],
    [-2*m*v, -v, 2*v, -2*u*v],
    [2*z, -2*z, -z, 0],
    [0, 0, w*beta, -w],
])

assert sp.simplify(1-u+2*m*v-2*z)==0
assert sp.simplify(1-v-2*m*u+2*z)==0
assert sp.simplify(1-z+2*u-2*v)==0
assert sp.simplify(1-m+beta*z)==0
assert sp.simplify((ell*sp.eye(4)-J).det()-P)==0
assert sp.simplify(C1-3*(4*m*m+32*m+29)/den)==0
assert sp.simplify(D1-(2*m+11)*(6*m+7)*(16*m**4+64*m**3-56*m*m+64*m+81)/den**3)==0
assert sp.simplify(sp.diff(beta,m)-(16*m**4+64*m**3-56*m*m+64*m+81)/(4*m*m+8*m+1)**2)==0

Delta = sp.factor(A*B*C-C*C-A*A*D)
Delta_0 = 16*(108*w+31)*(405*w*w-2322*w+385)/59049
assert sp.simplify(Delta.subs(m,0)-Delta_0)==0
assert [sp.factor(expr.subs(m,0)) for expr in (u,v,z,beta)] == [sp.Rational(7,9), sp.Rational(11,9), sp.Rational(1,9), -9]
assert [sp.factor(expr.subs(m,0)) for expr in (S,Q,R,C1,D1)] == [sp.Rational(19,9), sp.Rational(167,81), sp.Rational(77,81), sp.Rational(29,3), sp.Rational(77,9)]
w_minus = sp.Rational(43,15)-2*sp.sqrt(3679)/45
w_plus = sp.Rational(43,15)+2*sp.sqrt(3679)/45
assert sp.simplify(Delta_0.subs(w,w_minus)) == 0
assert sp.simplify(Delta_0.subs(w,w_plus)) == 0
assert sp.simplify(w_minus>0) is sp.true
assert sp.simplify(w_plus>w_minus) is sp.true
# At the threshold, p(i Omega)=0 when Omega^2=C/A by the Hurwitz identity.
for edge in [w_minus,w_plus]:
    at = {m: 0,w: edge}
    A0,B0,C0,D0 = [sp.simplify(t.subs(at)) for t in (A,B,C,D)]
    om2 = sp.simplify(C0/A0)
    assert sp.simplify((B0-om2)*om2-D0)==0
    assert float(om2)>0 and float(B0-om2)>0
# Independent direct matrix-eigenvalue checks in all three regimes.
for speed, expected in [(sp.Rational(1,10),0),(sp.Integer(1),2),(sp.Integer(10),0)]:
    eigen = [complex(root) for root in sp.nroots(sp.Poly(P.subs({m:0,w:speed}),ell),maxsteps=100)]
    count = sum(a.real>1e-8 for a in eigen)
    assert count == expected, (speed,eigen)
    print('w=',speed,'unstable eigenvalues=',count,'spectrum=',[complex(round(a.real,7),round(a.imag,7)) for a in eigen])
for value in [sp.Rational(-1,8),sp.Rational(-1,20),sp.Rational(0),sp.Rational(1,10),sp.Rational(1,5),sp.Rational(1,2)]:
    # Formula and direct determinant are identical symbolically; sample positive parameters for Routh signs.
    for speed in [sp.Rational(1,10),sp.Integer(1),sp.Integer(3),sp.Integer(10)]:
        substitutions={m:value,w:speed}
        coeffs=[sp.N(c.subs(substitutions)) for c in (A,B,C,D)]
        assert all(float(c)>0 for c in coeffs)
        pol=sp.Poly(P.subs(substitutions),ell)
        eig=[complex(t) for t in sp.nroots(pol,maxsteps=100)]
        rh_sign=float(Delta.subs(substitutions))
        actual=sum(t.real>1e-8 for t in eig)
        assert actual == (0 if rh_sign>0 else 2), (value,speed,rh_sign,eig)
print('PASS: symbolic equilibrium, Jacobian, quartic, factorization, boundaries, and 24 independent spectra.')
