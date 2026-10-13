#!/usr/bin/env python3
"""Reproduce exact polynomial elimination and the two model-specific comparisons."""
import sympy as sp
u=sp.symbols('u', real=True)
r,K,alpha,m,beta,gamma,beta1,beta2,beta3,A,gamma1,eta=sp.symbols(
    'r K alpha m beta gamma beta1 beta2 beta3 A gamma1 eta',positive=True)
R=r*(1-u/K)-beta1*eta
C1=gamma+beta2*A+beta3*eta
Theta=K*(alpha-m*r+m*beta1*eta)
T=Theta+m*r*u
Q=K*(r-beta1*eta)-r*u
v=sp.cancel(u*R/(alpha-m*R))
G1=sp.cancel(r*u*(1-u/K)-alpha*u*v/(u+m*v)-beta1*eta*u)
G2=sp.cancel(beta*u*v/(u+m*v)-gamma*v-beta2*v*(A-u)-beta3*eta*v-gamma1*v*v)
F=sp.expand(beta*T*T-alpha*K*C1*T+alpha*K*beta2*u*T-alpha*K*gamma1*u*Q)
assert sp.simplify(G1)==0
assert sp.simplify(G2/v-F/(alpha*K*T))==0
expected_A=beta*(r*m)**2+alpha*K*r*(m*beta2+gamma1)
expected_B=2*beta*r*m*Theta-alpha*K*r*m*C1+alpha*K*beta2*Theta-alpha*K*K*gamma1*(r-beta1*eta)
expected_C=beta*Theta*Theta-alpha*K*Theta*C1
poly=sp.Poly(F,u)
assert sp.simplify(poly.coeff_monomial(u*u)-expected_A)==0
assert sp.simplify(poly.coeff_monomial(u)-expected_B)==0
assert sp.simplify(poly.coeff_monomial(1)-expected_C)==0
C2=beta2-gamma1
Fsrc=sp.expand((beta*(r*m)**2+alpha*K*r*C2)*u*u
    +(2*beta*r*m*Theta-alpha*K*r*m*C1-alpha*K*K*(r-beta1*eta)*C2)*u
    +beta*Theta*Theta-alpha*K*Theta*C1)
params={r:2,K:2,alpha:2,m:1,beta:sp.Rational(4,3),gamma:sp.Rational(1,4),
 beta1:1,beta2:1,beta3:sp.Rational(1,2),A:1,gamma1:sp.Rational(3,2),eta:sp.Rational(1,2)}
assert sp.simplify(F.subs(params)-sp.Rational(2,3)*(u-1)*(38*u+7))==0
assert sp.simplify(Fsrc.subs(params)-sp.Rational(2,3)*(2*u*u-u-7))==0
assert sp.simplify(v.subs(params).subs(u,1))==sp.Rational(1,3)
assert sp.simplify(G1.subs(params).subs(u,1))==0
assert sp.simplify(G2.subs(params).subs(u,1))==0
U=K*(1-beta1*eta/r)
L=K*(r-beta1*eta-alpha/m)/r
assert sp.simplify(U.subs(params))==sp.Rational(3,2)
assert sp.simplify(L.subs(params))==sp.Rational(-1,2)
assert sp.simplify(R.subs(params).subs(u,1))==sp.Rational(1,2)
assert sp.solve(sp.Eq(Fsrc.subs(params),0),u)==[(1-sp.sqrt(57))/4,(1+sp.sqrt(57))/4]
assert (1+sp.sqrt(57))/4 > sp.Rational(3,2)
# Numerical baseline (6.1) from the article, recorded as exact rational decimals.
source={r:sp.Rational(12,10),K:2,alpha:sp.Rational(9,10),m:sp.Rational(45,100),
 beta:sp.Rational(8,10),gamma:sp.Rational(3,10),beta1:sp.Rational(1,10),eta:1,
 beta2:sp.Rational(1,10),A:sp.Rational(1,10),beta3:sp.Rational(1,10),gamma1:sp.Rational(15,100)}
assert sp.simplify(F.subs(source)-sp.Rational(27,50000)*(1212*u*u-272*u-135))==0
assert sp.simplify(Fsrc.subs(source)-sp.Rational(9,50000)*(696*u*u+2774*u-405))==0
true_roots=[float(sp.re(t)) for t in sp.nroots(F.subs(source)) if abs(float(sp.im(t)))<1e-12 and float(sp.re(t))>0]
source_roots=[float(sp.re(t)) for t in sp.nroots(Fsrc.subs(source)) if abs(float(sp.im(t)))<1e-12 and float(sp.re(t))>0]
assert len(true_roots)==1 and len(source_roots)==1
assert abs(true_roots[0]-0.4643156045)<1e-9
assert abs(source_roots[0]-0.1410097041)<1e-9
true_v=float(v.subs(source).subs(u,true_roots[0]))
assert abs(true_v-0.7191153701)<1e-8
print('VERIFY_OK')
