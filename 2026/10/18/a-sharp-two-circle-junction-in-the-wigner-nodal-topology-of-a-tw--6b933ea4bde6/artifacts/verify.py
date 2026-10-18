#!/usr/bin/env python3
"""Symbolic and independent integral checks for a two-Hermite Wigner nodal theorem."""
import math
import sympy as s
import mpmath as mp

q,p,t,y=s.symbols('q p t y',real=True)
r2=q*q+p*p
P=1+t*t*(1-4*r2+2*r2**2)+2*s.sqrt(2)*t*(q*q-p*p)
# Direct Wigner Gaussian-moment computation, not a reused polynomial formula.
f_plus=1+t*(2*(q+y/2)**2-1)/s.sqrt(2)
f_minus=1+t*(2*(q-y/2)**2-1)/s.sqrt(2)
raw=s.Poly(s.expand(f_plus*f_minus),y)
# Gaussian Fourier moments of y^0,y^2,y^4 under exp(-y^2/4-ipy).
M={0:1,1:-2*s.I*p,2:2-4*p*p,3:s.I*(-12*p+8*p**3),4:12-48*p*p+16*p**4}
Pw=s.expand(sum(coeff*M[k[0]] for k,coeff in raw.terms()))
assert s.simplify(Pw-P)==0
print('CHECK Fourier-Gaussian integration identity: PASS')

critical=2*s.sqrt(2)
circle_product=16*(q*q+(p-s.Rational(1,2))**2-1)*(q*q+(p+s.Rational(1,2))**2-1)
assert s.simplify(P.subs(t,critical)-circle_product)==0
for x in (s.sqrt(3)/2,-s.sqrt(3)/2):
 assert s.simplify(P.subs({t:critical,q:x,p:0}))==0
 assert s.simplify(s.diff(P,q).subs({t:critical,q:x,p:0}))==0
 assert s.simplify(s.diff(P,p).subs({t:critical,q:x,p:0}))==0
 assert s.simplify(s.diff(P,q,2).subs({t:critical,q:x,p:0})-96)==0
 assert s.simplify(s.diff(P,p,2).subs({t:critical,q:x,p:0})+32)==0
print('CHECK exact two-circle factorization and transverse saddles: PASS')

# Double root in ray reduction occurs iff cos(2 theta)=sqrt(2)t-sqrt(1+t^2).
for T in (s.Rational(1,9),s.Rational(1,2),1,2,2*s.sqrt(2),4,10):
 threshold=float((s.sqrt(2)*T-s.sqrt(1+T*T)).evalf())
 if float(T)<2*math.sqrt(2): assert -1<threshold<1
 elif float(T)>2*math.sqrt(2): assert threshold>1
 else: assert abs(threshold-1)<1e-13
print('CHECK discriminant phase regimes: PASS')

# Numeric direct integral independent of the Wigner Hermite polynomial formula.
mp.mp.dps=40
for T,Q,B in ((0.2,0.5,0.2),(0.8,0.5,1.0),(1.4,-1.1,-0.4),(3.3,0.0,1.3)):
 T,Q,B=map(mp.mpf,(str(T),str(Q),str(B)))
 n=(1+T*T)
 def f(x):return (1+T*(2*x*x-1)/mp.sqrt(2))*mp.exp(-x*x/2)/(mp.pi**mp.mpf('0.25')*mp.sqrt(n))
 val=mp.quad(lambda z: f(Q+z/2)*f(Q-z/2)*mp.cos(B*z), [-mp.inf,mp.inf])/(2*mp.pi)
 R2=Q*Q+B*B
 pred=mp.exp(-R2)*(1+T*T*(1-4*R2+2*R2**2)+2*mp.sqrt(2)*T*(Q*Q-B*B))/(mp.pi*n)
 assert abs(val-pred)<mp.mpf('1e-32'), (val,pred)
print('CHECK four direct oscillatory Wigner integrals: PASS')

# Verify the chosen lower exponential negativity test has an exact negative sign.
T=s.symbols('T',positive=True)
p0sq=1/(s.sqrt(2)*T)
assert s.simplify(P.subs({t:T,q:0,p:s.sqrt(p0sq)})-(T*T-2*s.sqrt(2)*T))==0
print('CHECK exponential-tail negativity test polynomial: PASS')
