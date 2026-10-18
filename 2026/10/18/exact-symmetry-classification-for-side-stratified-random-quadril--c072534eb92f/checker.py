#!/usr/bin/env python3
"""Exact moment and symmetry identities for a side-stratified inscribed quadrilateral.

Requires SymPy. Run: python checker.py
"""
import sympy as s
p,q=s.symbols('p q',real=True)
u,v,w,t=s.symbols('u v w t',real=True)
A=s.Matrix([-p,0]);B=s.Matrix([0,-q]);C=s.Matrix([1-p,0]);D=s.Matrix([0,1-q])
P=[A+u*(B-A),B+v*(C-B),C+w*(D-C),D+t*(A-D)]
cross=lambda a,b: a[0]*b[1]-a[1]*b[0]
R=s.expand(sum(cross(P[i],P[(i+1)%4]) for i in range(4)))
expected=1+p*t*u-p*u-p*v*w+p*w-q*t*w+q*t+q*u*v-q*v+t*w-t+v*w-w
assert s.expand(R-expected)==0

def exact_average(poly):
    out=0
    for powers,coef in s.Poly(s.expand(poly),u,v,w,t).terms():
        out+=coef*s.prod(s.Rational(1,j+1) for j in powers)
    return s.factor(out)
assert exact_average(R)==s.Rational(1,2)
mu3=exact_average((R-s.Rational(1,2))**3)
mu5=exact_average((R-s.Rational(1,2))**5)
assert mu3==0
assert s.factor(mu5+(p-q)**2*(p+q-1)**2/s.Integer(2160))==0
X,Y,Z,T,a,b=s.symbols('X Y Z T a b',real=True)
F=s.expand(4*(R-s.Rational(1,2)).subs({u:(1+X)/2,v:(1+Y)/2,w:(1+Z)/2,t:(1+T)/2},simultaneous=True).subs({p:s.Rational(1,2)+a,q:s.Rational(1,2)+b}, simultaneous=True))
f_equal=(T+Y)*((X+Z)/2+a*(X-Z))+2*a*(T-Y)
f_opposite=((T+Y)/2+a*(T-Y))*(X+Z)-2*a*(X-Z)
assert s.expand(F.subs(b,a)-f_equal)==0
assert s.expand(F.subs(b,-a)-f_opposite)==0
assert s.expand(f_equal+f_equal.subs({T:-T,Y:-Y},simultaneous=True))==0
assert s.expand(f_opposite+f_opposite.subs({X:-X,Z:-Z},simultaneous=True))==0
# Exact coordinate test independent of symbolic moment expansions.
subs={p:s.Rational(2,7),q:s.Rational(3,5),u:s.Rational(1,4),v:s.Rational(2,3),w:s.Rational(3,8),t:s.Rational(5,9)}
assert R.subs(subs)==expected.subs(subs)
print('PASS: exact area, mean, third/fifth moments, and both sign involutions')
print('mu5=',mu5)
