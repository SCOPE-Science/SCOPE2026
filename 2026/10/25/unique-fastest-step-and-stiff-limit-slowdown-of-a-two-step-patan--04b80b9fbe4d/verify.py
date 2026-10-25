#!/usr/bin/env python3
"""Reproducible algebra and exact-rational checks for a two-step Patankar model."""
from fractions import Fraction as F
import math
import sympy as S

h = S.symbols('h', positive=True, real=True)
v,w = S.symbols('v w', real=True)
# The sign assumptions on v and w for numerical tests are |v|,|w|<1/2.
t=1+2*h
sigma1=S.Rational(1,2)+v/t
sigma2=S.Rational(1,2)-v/t
A=(S.Rational(1,2)-v)/sigma2
B=(S.Rational(1,2)+v)/sigma1
u_formula=S.factor((w+h*(A-B))/(1+2*h*(A+B)))
u_closed=(w*(t*t-4*v*v)-8*h*h*t*v)/(t*t-4*v*v+4*h*t*(t-4*v*v))
assert S.factor(u_formula-u_closed)==0

a=1/(1+4*h)
b=-8*h*h/((1+2*h)*(1+4*h))
assert S.factor(S.diff(u_formula,w).subs({v:0,w:0})-a)==0
assert S.factor(S.diff(u_formula,v).subs({v:0,w:0})-b)==0
assert S.factor(1+b-a)==4*h/((1+2*h)*(1+4*h))
assert S.factor((1-b-a)-(4*h/(1+4*h)+8*h*h/((1+2*h)*(1+4*h))))==0
m=1/(1+2*h)
assert S.factor(m*m+b*m-a)==-12*h*h/((1+2*h)**2*(1+4*h))

rho=(-b+S.sqrt(b*b+4*a))/2
assert S.simplify(rho*rho+b*rho-a)==0
assert S.limit((1-rho)*h,h,S.oo)==S.Rational(1,2)
assert S.limit((1-rho)/h,h,0)==2
assert S.limit(rho,h,S.oo)==1
assert S.limit(rho,h,0)==1
rcrit=S.factor(S.diff(a,h)/S.diff(b,h))
assert S.factor(rcrit-(2*h+1)**2/(4*h*(3*h+1)))==0
Q=32*h**4+32*h**3-8*h**2-8*h-1
assert S.factor((rcrit*rcrit+b*rcrit-a)+Q/(16*h*h*(3*h+1)**2))==0
assert Q.subs(h,0)<0 and Q.subs(h,1)>0
# Descending coefficient signs +,+,-,-,- certify one positive root by Descartes.
assert S.Poly(Q,h).all_coeffs()==[32,32,-8,-8,-1]
roots=S.nroots(Q,maxsteps=200)
positives=[float(S.re(z)) for z in roots if abs(float(S.im(z)))<1e-12 and float(S.re(z))>0]
assert len(positives)==1
hstar=positives[0]
rstar=float(rho.subs(h,hstar).evalf())
assert 0.53656<hstar<0.53657 and 0.76732<rstar<0.76734

checks=0
hs=[F(1,100),F(1,10),F(1,4),F(1,2),F(1),F(3),F(12),F(50)]
us=[F(-2,5),F(-1,4),F(-1,20),F(0),F(1,20),F(1,4),F(2,5)]
for H in hs:
    for V in us:
        # Independent two-component backward Euler predictor.
        q1=F(1,2)+V; q2=F(1,2)-V
        s1=(q1+H)/(1+2*H); s2=(q2+H)/(1+2*H)
        av=q2/s2; bv=q1/s1
        for W in us:
            # Solve original 2x2 mass-transfer equation directly.
            p1=F(1,2)+W
            y1=(p1+2*H*av)/(1+2*H*(av+bv))
            y2=1-y1
            u_exact=y1-F(1,2)
            T=1+2*H
            u_closed_q=(W*(T*T-4*V*V)-8*H*H*T*V)/(T*T-4*V*V+4*H*T*(T-4*V*V))
            assert y1>0 and y2>0 and u_exact==u_closed_q
            checks+=1
print('OK symbolic identities, single positive optimal-step root,',checks,'exact-rational updates')
print('h*=',format(hstar,'.15f'),'rho*=',format(rstar,'.15f'))
