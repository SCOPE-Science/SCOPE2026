#!/usr/bin/env python3
"""Reproducible symbolic and numerical checks for the smooth-curve short-distance theorem.
Requires Python 3, sympy, numpy and scipy.  Exact algebra proves only identities;
all-dimensional analytic assertions are proved in RESULT.md, not by finite tests.
"""
import math
import sympy as sp

s,h,t = sp.symbols('s h t', real=True)
k=sp.Function('k')(s)
# Frenet differentiation in the moving orthonormal frame: T'=k*N, N'=-k*T.
def D(pair):
    a,b=pair
    return (sp.expand(sp.diff(a,s)-k*b), sp.expand(k*a+sp.diff(b,s)))
v=[(sp.Integer(1),sp.Integer(0))]
for _ in range(6):v.append(D(v[-1]))
assert sp.simplify(v[2][0]+k**2)==0
assert sp.simplify(v[2][1]-sp.diff(k,s))==0
assert sp.simplify(v[4][0]-(k**4-3*sp.diff(k,s)**2-4*k*sp.diff(k,s,2)))==0
# Components of a symmetric midpoint chord through quintic order.
A=h+v[2][0]*h**3/24+v[4][0]*h**5/1920
B=v[2][1]*h**3/24+v[4][1]*h**5/1920
S=sp.series(sp.expand(A**2+B**2),h,0,8).removeO()
expect=h**2-k**2*h**4/12+(k**4/sp.Integer(360)-sp.diff(k,s)**2/sp.Integer(720)-k*sp.diff(k,s,2)/sp.Integer(240))*h**6
assert sp.simplify(S-expect)==0
# The positive-radius chord length: h - k^2 h^3/24 + ... .
C=sp.series(sp.sqrt(S/h**2),h,0,6).removeO()*h
C=sp.expand(C)
assert sp.simplify(sp.expand(C).coeff(h,3)+k**2/24)==0
assert sp.simplify(sp.expand(C).coeff(h,5)-(k**4/sp.Integer(1920)-k*sp.diff(k,s,2)/sp.Integer(480)-sp.diff(k,s)**2/sp.Integer(1440)))==0
# Inverse function series for the positive arclength gap.
H=t+k**2*t**3/24+(3*k**4/sp.Integer(640)+sp.diff(k,s)**2/sp.Integer(1440)+k*sp.diff(k,s,2)/sp.Integer(480))*t**5
res=sp.series(C.subs(h,H),t,0,7).removeO()
assert sp.simplify(res-t)==0
# Integration by parts on a periodic closed curve gives the claimed negative derivative energy.
assert sp.Rational(2,1)*(sp.Rational(1,1440)-sp.Rational(1,480))==-sp.Rational(1,360)
assert 2*sp.Rational(3,640)==sp.Rational(3,320)
# Circle of radius R: CDF exactly 2/pi * asin(t/(2R)).
r=sp.symbols('r',positive=True)
Fcircle=sp.series(2*sp.asin(t/(2*r))/sp.pi,t,0,7).removeO()
Fexpected=t/(sp.pi*r)+t**3/(24*sp.pi*r**3)+3*t**5/(640*sp.pi*r**5)
assert sp.simplify(Fcircle-Fexpected)==0
# Exact even Fourier averages for k(s)=rho*(1+a*cos(n*rho*s)).
a,n,rho=sp.symbols('a n rho',real=True)
u=sp.symbols('u',real=True)
kap=rho*(1+a*sp.cos(u))
kapu=rho**2*n*(-a*sp.sin(u))
mean_k4=sp.integrate(sp.expand_trig(kap**4),(u,0,2*sp.pi))/(2*sp.pi)
mean_kp2=sp.integrate(sp.expand_trig(kapu**2),(u,0,2*sp.pi))/(2*sp.pi)
assert sp.simplify(mean_k4-rho**4*(1+3*a**2+3*a**4/8))==0
assert sp.simplify(mean_kp2-rho**4*n**2*a**2/2)==0
cut=sp.Rational(9,320)-n*n/sp.Integer(720)+sp.Rational(9,2560)*a*a
assert cut.subs(n,4).subs(a,0)>0
assert cut.subs(n,5).subs(a,1)<0
assert sp.simplify(cut.subs(n,4).subs(a,0))==sp.Rational(17,2880) # 9/320-16/720
# Independent fixed-order quadrature of the chord radius inverse, not a proof.
import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import brentq
nodes,weights=roots_legendre(48)

def measured_CDF(harmonic,amplitude,threshold,samples=144):
    # L=2*pi, theta(u)=u+(a/n)*sin(nu)
    U=2*math.pi*(np.arange(samples)+0.5)/samples
    def dist(u,w):
        ss=u+0.5*w*nodes
        theta=ss+(amplitude/harmonic)*np.sin(harmonic*ss)
        return 0.5*w*math.hypot(np.dot(weights,np.cos(theta)),np.dot(weights,np.sin(theta)))
    values=[brentq(lambda w:dist(u,w)-threshold,threshold*.95,threshold*3,xtol=1e-13) for u in U]
    return float(np.mean(values)/math.pi)  # 2/L * mean(H) = mean(H)/pi

for mode in (2,4,5,12):
    amplitude=0.4
    c3=(1+amplitude**2/2)/(12*(2*math.pi))
    c5=((3/320)*(1+3*amplitude**2+3*amplitude**4/8)-amplitude**2*mode**2/720)/(2*math.pi)
    for threshold in (0.08,0.12):
        actual=measured_CDF(mode,amplitude,threshold)
        predicted=threshold/math.pi+c3*threshold**3+c5*threshold**5
        assert abs(actual-predicted)< 0.45*threshold**7, (mode,threshold,actual,predicted,abs(actual-predicted))
print('VERIFY_OK Frenet_series=6 inverse_series=1 exact_fourier=2 circle=1 numerical_cases=8')
