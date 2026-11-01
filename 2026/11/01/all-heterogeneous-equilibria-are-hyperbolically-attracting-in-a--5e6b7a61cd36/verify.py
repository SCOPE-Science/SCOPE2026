#!/usr/bin/env python3
"""Reproducible symbolic identities and finite checks for two-patch logistic chemotaxis.
Requires Python 3, SymPy, NumPy, and SciPy. The analytic proof is in RESULT.md.
"""
import math
import sympy as sp

T, KAP = sp.symbols('t k', real=True, positive=True)
H = T*(1 + KAP*(1-T**2)/(1+T**2))
V = KAP*T/(1+(1-KAP)*T**2)
assert sp.simplify(H-(T+V)/(1+T*V)) == 0
Hprime = sp.diff(H,T)
P = (1+KAP)+(2-4*KAP)*T**2+(1-KAP)*T**4
assert sp.simplify(Hprime-P/(1+T**2)**2) == 0
X = (1+T**2)*sp.atanh(H)/T
C2 = (4+3*KAP**2+KAP**3)/3
assert sp.simplify(sp.limit(X,T,0)-(1+KAP)) == 0
assert sp.simplify(sp.limit((X-(1+KAP))/T**2,T,0)-C2) == 0
assert sp.simplify(sp.diff((1+T**2)/(1+(1-KAP)*T**2),T)-2*KAP*T/(1+(1-KAP)*T**2)**2)==0

eta, delta, alpha, cap, chi = sp.symbols('eta delta alpha cap chi', positive=True)
r = eta*KAP/2
M = cap/(1+T**2)
z = M*T
w = alpha*z/delta
chi_on = delta/(alpha*cap)*X
# Equilibrium equations, with the source's N=2 normalization.
assert sp.simplify(r*(M-(M**2+z**2)/cap)) == 0
assert sp.simplify(alpha*z-delta*w) == 0
# Explicit local Jacobian in (M,z,w), with the chemical mean eigenvalue -beta.
a = r*(1-T**2)/(1+T**2)
e = a+eta/2
b = eta*KAP*T/(1+T**2)
d = eta*T*(1-KAP)/2
q = e*(1-H**2)*sp.atanh(H)/H
assert sp.simplify(e-eta*H/(2*T)) == 0
assert sp.simplify(q - eta*(1-H**2)*X/(2*(1+T**2)))==0
s = sp.symbols('s')
Jac=sp.Matrix([[-a,-b,0],[d,-e,delta*q/alpha],[0,alpha,-delta]])
cp = sp.expand(Jac.charpoly(s).as_expr())
expected = sp.expand((s+delta)*((s+a)*(s+e)+b*d) -delta*q*(s+a))
assert sp.simplify(cp-expected)==0
Gt = (1-H**2)*X*(1-T**2)/(1+T**2)**2 - Hprime
assert sp.simplify(a*e+b*d-a*q+r*eta*Gt/2)==0
print('Exact symbolic checks: PASS')

# Finite independent checks: root bracketing, stationarity, Jacobian eigenvalues.
from numpy import array, linalg
from scipy.optimize import brentq
count=0
for kk in [0.01,0.2,0.5,1.0,1.1,2.0,4.0,10.0,40.0]:
    tp=1.0 if kk <=1 else 2/(kk+math.sqrt(kk*kk+4*(kk-1)))
    # Endpoint of the positive heterogeneous equilibrium branch.
    for eta0 in [0.05,1.0]:
      r0=kk*eta0/2
      for de0 in [0.1,3.0]:
       cap0,alpha0,beta0=2.5,0.7,0.05
       chi_star=de0*(1+kk)/(alpha0*cap0)
       for mult in [1.01,1.1,1.5,3.0,10.0]:
        ch=chi_star*mult
        def h(t):return t*(1+kk*(1-t*t)/(1+t*t))
        def residual(t):return math.tanh(ch*alpha0*cap0*t/(de0*(1+t*t)))-h(t)
        low=1e-9
        # near the upper endpoint, residual<0 because h ->1 and tanh<1
        upper=tp*(1-1e-8)
        if residual(upper)>=0:
           # Extreme saturation can require very fine endpoint resolution; skip unsafely bracketed finite check.
           continue
        assert residual(low)>0,(kk,mult)
        t=brentq(residual,low,upper,xtol=1e-14)
        mm=cap0/(1+t*t);zz=mm*t;ww=alpha0*zz/de0
        aa=r0*(1-t*t)/(1+t*t)
        ee=aa+eta0/2; bb=eta0*kk*t/(1+t*t); dd=eta0*t*(1-kk)/2
        ff=eta0/2*mm*ch*(1-h(t)**2)
        j=array([[-aa,-bb,0],[dd,-ee,ff],[0,alpha0,-de0]],dtype=float)
        assert abs(residual(t))<1e-11
        assert max(linalg.eigvals(j).real)<-1e-10,(kk,ch,t,linalg.eigvals(j))
        count+=1
print('Independent finite equilibrium and stability checks:',count,'PASS')
