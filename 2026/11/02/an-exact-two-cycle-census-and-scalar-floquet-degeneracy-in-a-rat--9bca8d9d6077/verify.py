#!/usr/bin/env python3
"""Independent reproducible symbolic checks of the period-two theorem.

Dependency: SymPy (tested with installed version); run `python verify.py`.
The accompanying proof establishes the infinite statements; this program
checks the exact identities and local expansions used in that proof.
"""
import sympy as sp

u, v, a, t, c = sp.symbols('u v a t c', real=True)
G = sp.Matrix([(1+a/(1+v*v))*u, v+u])
J = G.jacobian((u,v))
G2 = G.subs({u:G[0],v:G[1]}, simultaneous=True)
Q = {u:-2*t, v:t, a:-2*(1+t*t)}
P = sp.Matrix([-2*t,t])
Pnext = sp.Matrix([2*t,-t])
assert all(sp.simplify(z)==0 for z in G.subs(Q)-Pnext)
assert all(sp.simplify(z)==0 for z in G2.subs(Q)-P)
Jc = sp.simplify(J.subs(Q))
lam = (1-7*t*t)/(1+t*t)
assert all(sp.simplify(z)==0 for z in Jc*Jc-lam*sp.eye(2))
assert all(sp.simplify(z)==0 for z in G2.jacobian((u,v)).subs(Q)-lam*sp.eye(2))
assert sp.simplify(lam-(-7-16/a).subs(a,-2*(1+t*t)))==0

# At a=-16/7, t=1/sqrt(7), the first coordinate of G^2 has a
# nonzero second derivative, so its local leading order is quadratic.
Q0 = {u:-2/sp.sqrt(7),v:1/sp.sqrt(7),a:-sp.Rational(16,7)}
assert G2.jacobian((u,v)).subs(Q0).applyfunc(sp.simplify)==sp.zeros(2)
H0 = sp.hessian(G2[0],(u,v)).subs(Q0).applyfunc(sp.simplify)
assert H0 == sp.Matrix([[3*sp.sqrt(7)/2, sp.sqrt(7)],
                         [sp.sqrt(7),2*sp.sqrt(7)]])

# Exact trial values: return multipliers on either side of both boundaries.
for ai, expected in [(-sp.Rational(21,10),sp.Rational(13,21)),
                     (-sp.Rational(5,2),-sp.Rational(3,5)),
                     (-sp.Rational(8,3),-1),
                     (-sp.Rational(3,1),-sp.Rational(5,3)),
                     (-sp.Rational(16,7),0)]:
    ti = sp.sqrt(-ai/2-1)
    assert sp.simplify(lam.subs(t,ti)-expected)==0
    for ci in [sp.Rational(1,10),sp.Integer(-2),sp.Integer(3)]:
        pt = sp.Matrix([-2*ti/ci,ti])
        Qorig = sp.Matrix([(1+ai/(1+v*v))*u, v+ci*u])
        pt1 = Qorig.subs({u:pt[0],v:pt[1]})
        pt2 = Qorig.subs({u:pt1[0],v:pt1[1]})
        assert all(sp.simplify(z)==0 for z in pt1+pt)
        assert all(sp.simplify(z)==0 for z in pt2-pt)
        JJ = Qorig.jacobian((u,v)).subs({u:pt[0],v:pt[1]}).applyfunc(sp.simplify)
        assert all(sp.simplify(z)==0 for z in JJ*JJ-expected*sp.eye(2))
print('PASS: general symbolic return, Jacobian, quadratic degeneracy, and 15 exact parameter-coordinate cases')
