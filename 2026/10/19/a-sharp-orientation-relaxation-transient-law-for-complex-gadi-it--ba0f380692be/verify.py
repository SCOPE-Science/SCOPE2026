#!/usr/bin/env python3
"""Symbolic and direct-stage tests of a planar GADI transient theorem.

Requires SymPy (tested with version 1.13). All rational identities are exact.
The infinite-parameter and all-iteration conclusions require the accompanying proof.
"""
import sympy as S
I = S.I
checks = 0

def eq(a, b):
    global checks
    assert S.simplify(a-b) == 0, (a,b,S.simplify(a-b))
    checks += 1

# Generic rational/radical orientations and parameters; independent checks
# against both stages of the source iteration, not just against the theorem formula.
for a,b,t,q,th in [
    (S.Integer(1),S.Integer(3),S.Integer(5),S.Rational(1,2),S.Rational(3,4)),
    (S.Integer(2),S.Integer(5),S.Integer(7),S.Rational(1,4),S.Rational(1,2)),
    (S.Integer(3),S.Integer(1),S.Integer(11),S.Rational(3,4),S.Integer(0)),
    (S.Integer(1),S.Integer(4),S.Integer(2),S.Integer(0),S.Rational(1,3)),
    (S.Integer(2),S.Integer(7),S.Integer(9),S.Integer(1),S.Rational(4,5)),
]:
    E=S.eye(2); e=S.Matrix([0,1]); v=S.Matrix([S.sqrt(1-q),S.sqrt(q)])
    W=S.diag(a,b); T=t*v*v.T; d=(a-b)/(a+b)
    C=a*E+I*T; B=a*E-I*T
    # Error map obtained directly from the source's two stages, with omega=2 theta.
    half=(a*E+W).inv()*B
    G_direct=C.inv()*(I*T-(1-2*th)*a*E+(2-2*th)*a*half)
    D=(a*E-W)*(a*E+W).inv()
    H=C.inv()*D*B
    G=th*E+(1-th)*H
    for i in range(2):
        for j in range(2):
            eq(G_direct[i,j],G[i,j])
    lam=d*(a+I*t*(1-2*q))/(a+I*t)
    eq(S.trace(H),lam)
    eq(S.det(H),0)
    for i in range(2):
        for j in range(2):
            eq((H*H)[i,j],(lam*H)[i,j])
    # Rank-one Euclidean operator norm squared is its Frobenius norm squared.
    normsq=S.trace(H.conjugate().T*H)
    expected=d**2*(1+q*(1-q)*t**4/(a**2*(a**2+t**2)))
    eq(normsq,expected)
    eq(S.simplify(lam*S.conjugate(lam)),
       d**2*(a**2+(1-2*q)**2*t**2)/(a**2+t**2))
    for k in range(1,8):
        coefficient=S.expand(((th+(1-th)*lam)**k-th**k)/lam)
        target=th**k*E+coefficient*H
        for i in range(2):
            for j in range(2):
                eq((G**k)[i,j],target[i,j])

# Analytic-form and exact threshold checks in the balanced orientation.
x,d=S.symbols('x d',positive=True,real=True)
N2=d**2*(x**2+2)**2/(4*(1+x**2))
eq(N2,d**2*(1+x**4/(4*(1+x**2))))
s=S.sqrt(1-d**2)
# When d=1/2, the positive crossing is x^2=6+4 sqrt(3).
eq(N2.subs({d:S.Rational(1,2),x:S.sqrt(6+4*S.sqrt(3))}),1)
# Exact positive critical level general d in (0,1):
y=2*s/(1-s)
eq(S.factor((d**2*(y+2)**2-4*(1+y)).subs(d**2,1-s**2)),0)
# For theta=3/4 the coefficient peaks jointly at k=3 and k=4.
th=S.Rational(3,4)
eq(3*th**2,4*th**3)
eq(S.Rational(1,4)*S.Rational(1,4)*3*th**2,S.Rational(27,256))
print('PASS:',checks,'exact symbolic identities and stage-to-formula comparisons')
