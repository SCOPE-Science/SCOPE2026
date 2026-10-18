#!/usr/bin/env python3
"""Reproduce exact algebra for a parameter-dependent rational plane map.

Uses SymPy for rational symbolic identities. Finite tests are supporting checks;
analytic stable-manifold existence and asymptotics are proved in RESULT.md.
"""
import sympy as S

A, b, d, y, x, e = S.symbols('A b d y x e', real=True)
q=b-A
B=2*b-A
F1=b*x/(A+y)
F2=(d*(A+y)+e)/x
J=S.Matrix([F1,F2]).jacobian([x,y])
E=S.Matrix([(b*d+e)/q,q])
assert S.factor(J.det()+b*e/(x*(A+y)**2)) == 0
assert S.factor(F1*F2-b*d-b*e/(A+y)) == 0
assert S.factor((F1-E[0]).subs({x:E[0],y:q})) == 0
assert S.factor((F2-E[1]).subs({x:E[0],y:q})) == 0
assert S.factor(J.trace().subs({x:b*d/q,y:q,e:0})-B/b) == 0
assert S.factor(J.det().subs({x:b*d/q,y:q,e:0})) == 0

s0=d*(A+y)/q
u=(b+y)/(q*B)
v=q*(y-q)/(d*B**3*(A+y))
s=s0+e*u+e**2*v
P=b*s/(A+y)
w=(d*(A+y)+e)/s
R=s0.subs(y,w)+e*u.subs(y,w)+e**2*v.subs(y,w)
for derivative in range(3):
    assert S.factor(S.diff(P-R,e,derivative).subs(e,0)) == 0
assert S.factor(v.subs(y,q)) == 0
assert S.factor(u.subs(y,q)-1/q) == 0
assert S.factor(S.diff(v,y,2)+2*b*q/(d*B**3*(A+y)**3)) == 0

# Several rational interior and boundary inputs check rank collapse and basins.
for a0,b0,d0 in [(S.Rational(1), S.Rational(3), S.Rational(2)),
                 (S.Rational(2), S.Rational(7), S.Rational(3,2)),
                 (S.Rational(1,2), S.Rational(9,4), S.Rational(5,3))]:
    q0=b0-a0
    root=b0*d0/q0
    for y0 in [S.Rational(0), S.Rational(1,2), S.Rational(3)]:
        exactline=d0*(a0+y0)/q0
        for factor in [S.Rational(1,2),S.Rational(1),S.Rational(2)]:
            x0=exactline*factor
            X=b0*x0/(a0+y0)
            Y=d0*(a0+y0)/x0
            assert X*Y==b0*d0
            assert S.sign(X-root)==S.sign(factor-1)
            assert S.sign((b0*X**2/(a0*X+b0*d0))-X)==S.sign(factor-1)
# Numerical shooting tests an independent interpretation of the stable curve.
# It is a finite precision sanity check, not a uniqueness/proof certificate.
import mpmath as mp
mp.mp.dps=55
for epsilon in [mp.mpf('0.03'),mp.mpf('-0.03')]:
    aa=mp.mpf(1);bb=mp.mpf(3);dd=mp.mpf(2)
    qq=bb-aa;BB=2*bb-aa
    xe=(bb*dd+epsilon)/qq
    for y0 in [mp.mpf('0.5'),mp.mpf(4)]:
        center=dd*(aa+y0)/qq
        approx=(center+epsilon*(bb+y0)/(qq*BB)
                +epsilon**2*qq*(y0-qq)/(dd*BB**3*(aa+y0)))
        def sign_of_escape(x0):
            X=x0;Y=y0
            for _ in range(250):
                X,Y=bb*X/(aa+Y),(dd*(aa+Y)+epsilon)/X
                if X>5*xe:return +1
                if X<xe/5:return -1
            return 0
        left=center-mp.mpf('0.5');right=center+mp.mpf('0.5')
        assert sign_of_escape(left)==-1 and sign_of_escape(right)==1
        for _ in range(170):
            mid=(left+right)/2
            if sign_of_escape(mid)>0:right=mid
            else:left=mid
        threshold=(left+right)/2
        assert abs(threshold-approx) < mp.mpf('0.004')*abs(epsilon)**3

print('VERIFY_OK')
