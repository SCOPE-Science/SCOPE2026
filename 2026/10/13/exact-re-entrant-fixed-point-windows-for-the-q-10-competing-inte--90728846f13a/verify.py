#!/usr/bin/env python3
import sympy as sp

u,b=sp.symbols("u b")
P=sp.expand((1+(b+8)*u)**2-sp.Rational(6,5)*u*(b+9*u)**2)
D=15*b**4-458*b**3+2190*b**2+9840*b-58405
disc=sp.factor(sp.discriminant(P,u))
expected=sp.Rational(12,125)*(b-1)**2*(b+9)**2*D
assert sp.expand(disc-expected)==0
polyD=sp.Poly(D,b)
assert polyD.count_roots(0,sp.oo)==3
assert polyD.count_roots(-sp.oo,0)==1
intervals=[
 (sp.Rational(592465054,10**8),sp.Rational(592465055,10**8)),
 (sp.Rational(593839039,10**8),sp.Rational(593839040,10**8)),
 (sp.Rational(2339979284,10**8),sp.Rational(2339979285,10**8)),
]
for lo,hi in intervals:
    assert polyD.count_roots(lo,hi)==1
    assert D.subs(b,lo)*D.subs(b,hi)<0
A,B,C,E=sp.Poly(P,u).all_coeffs()
triple=sp.factor(B**2-3*A*C)
res=sp.resultant(D,triple,b)
assert res!=0
assert sp.expand(P.subs(b,1)+sp.Rational(1,5)*(6*u-5)*(9*u+1)**2)==0
Bcoef=sp.Poly(P,u).coeff_monomial(u**2)
Ccoef=sp.Poly(P,u).coeff_monomial(u)
assert sp.discriminant(5*Bcoef,b)<0
threshold=(sp.Integer(5)+sp.sqrt(505))/6
assert float(intervals[0][0])>float(threshold)
assert sp.N(Ccoef.subs(b,intervals[0][0]))<0
roots=[r for r in sp.nroots(D,n=30,maxsteps=100) if abs(sp.im(r))<sp.Rational(1,10)**20]
positive=sorted(float(sp.re(r)) for r in roots if sp.re(r)>0)
print("VERIFY_OK", "roots=", ",".join(f"{x:.15f}" for x in positive), "resultant=", res)
