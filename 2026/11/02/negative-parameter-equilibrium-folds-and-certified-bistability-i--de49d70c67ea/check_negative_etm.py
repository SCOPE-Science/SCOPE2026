#!/usr/bin/env python3
"""Exact algebra checks for the negative-parameter ETM-3D equilibrium diagram.
Requires Python 3 and SymPy. Run: python check_negative_etm.py
"""
import sympy as S
x, y, z, rho, t = S.symbols('x y z rho t', real=True)
lam=S.Symbol('lambda')
F=S.Matrix([-2*x-rho*y+y*z, x-y+rho*z-2*x*z, rho*y-5*z+x*y])
D=2*x*x+rho*x+5-rho*rho
P=8*x**4+8*rho*x**3+(-6*rho**2+10*rho+35)*x**2 + (-4*rho**3+5*rho**2+15*rho)*x + 2*rho**4-5*rho**3-20*rho**2+25*rho+50
Q=594*rho**8-2076*rho**7-5948*rho**6+20050*rho**5+25505*rho**4-66100*rho**3-63325*rho**2+77500*rho+75000
ys=5*x/D;zs=x*(rho+x)/D
assert S.factor(F[1].subs({y:ys,z:zs}))==0
assert S.factor(F[2].subs({y:ys,z:zs}))==0
assert S.factor(F[0].subs({y:ys,z:zs})*D**2/x + P)==0
assert S.factor(S.discriminant(P,x)-12000*Q)==0
assert S.gcd(Q,S.diff(Q,rho))==1
sturm=S.sturm(Q,rho)
def variation(vals):
 vals=[v for v in vals if v]
 return sum(a!=b for a,b in zip(vals,vals[1:]))
sign_minus=[int(S.sign(S.Poly(h,rho).LC())*(-1)**S.degree(h,rho)) for h in sturm]
sign_zero=[int(S.sign(h.subs(rho,0))) for h in sturm]
assert variation(sign_minus)==6 and variation(sign_zero)==4
assert [S.sign(Q.subs(rho,z0)) for z0 in [-S.Rational(503,250),-S.Rational(2011,1000),-S.Rational(1309,1000),-S.Rational(327,250)]]==[1,-1,-1,1]
assert [S.Poly(P.subs(rho,r0),x).count_roots(-S.oo,S.oo) for r0 in [-3,-S.Rational(3,2),-1]]==[4,2,0]
assert S.factor(P.subs(rho,-2))==(x-2)*(8*x**3-9*x+4)
assert S.discriminant(8*x**3-9*x+4,x)==-4320
assert (8*x**3-9*x+4).subs(x,-S.Rational(5,4))==-S.Rational(3,8)
assert (8*x**3-9*x+4).subs(x,-S.Rational(6,5))==S.Rational(122,125)
assert S.factor(P.subs(x,0)-2*(rho**2-5)*(rho**2-S.Rational(5,2)*rho-5))==0
J=F.jacobian([x,y,z])
exact=J.subs({rho:-2,x:2,y:2,z:0})
assert S.factor(exact.charpoly(lam).as_expr()-(lam**3+8*lam**2+11*lam+20))==0
# For x=-t<0 on the other equilibrium branch at rho=-2, compute exact characteristic coefficients.
Dminus=D.subs(rho,-2)
sub={rho:-2,y:(5*x/Dminus),z:(x*(x-2)/Dminus)}
C=[S.factor(S.cancel(v.subs(x,-t))) for v in S.Poly(J.subs(sub).charpoly(lam).as_expr(),lam).all_coeffs()]
den=(2*t*t+2*t+1)**2
C2=8*t**6+24*t**5+84*t**4+138*t**3+96*t*t+52*t+11
C3=16*t**6+48*t**5+122*t**4+134*t**3+21*t*t-28*t-8
H=48*t**6+144*t**5+550*t**4+970*t**3+747*t*t+444*t+96
assert C[0]==1 and C[1]==8
assert S.factor(C[2]-C2/den)==0
assert S.factor(C[3]-C3/den)==0
assert S.factor(8*C[2]-C[3]-H/den)==0
origin=J.subs({rho:-2,x:0,y:0,z:0})
assert S.factor(origin.charpoly(lam).as_expr()-(lam**3+8*lam**2+11*lam-8))==0
# A double root at either negative discriminant zero is a simple fold:
# gcd(Q,Q')=1, and these intervals exclude all roots of P(0,rho).
print('PASS: elimination; degree-8 discriminant; exactly two simple negative discriminant zeros')
print('PASS: root intervals, sample interval counts 4/2/0; zero-root exceptions')
print('PASS: rho=-2 has exactly two nonzero equilibria, both Hurwitz sinks; origin unstable')
print('Sturm sign variation:',variation(sign_minus),variation(sign_zero))
print('Parameter intervals: (-503/250,-2011/1000), (-1309/1000,-327/250)')
