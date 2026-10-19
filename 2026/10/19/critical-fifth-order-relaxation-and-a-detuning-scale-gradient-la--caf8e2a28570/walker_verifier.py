#!/usr/bin/env python3
"""Reproducible checks for a critical two-harmonic discrete-wave walker map.

Symbolic identities use exact arithmetic. Numerical tests only check finite cases;
the continuum and infinite-time assertions require the accompanying proof.
"""
from math import pi, sin, cos, atan, sqrt
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

mu=0.6; coupling=0.05
beta_star=pi-atan(3/5)
x,beta=sp.symbols('x beta', real=True)
P=(sp.cos(beta)*sp.sin(3*x)+sp.sin(beta)*sp.sin(5*x))/sp.sqrt(sp.pi)
s=sp.symbols('s',real=True)
expression=((3*sp.cos(beta)+5*sp.sin(beta))*s +(-4*sp.cos(beta)-20*sp.sin(beta))*s**3+16*sp.sin(beta)*s**5)/sp.sqrt(sp.pi)
assert sp.simplify(sp.trigsimp(sp.expand_trig(P)-expression.subs(s,sp.sin(x))))==0
bval={sp.cos(beta):-5/sp.sqrt(34),sp.sin(beta):3/sp.sqrt(34)}
critical=sp.expand(expression.subs(bval,simultaneous=True))
assert sp.simplify(critical-(-40*s**3+48*s**5)/sp.sqrt(34*sp.pi))==0
A=sp.symbols('A',real=True)
critical_slope=sp.simplify(((-3*sp.sin(beta)+5*sp.cos(beta))/sp.sqrt(sp.pi)).subs(bval,simultaneous=True))
assert sp.simplify(critical_slope+sp.sqrt(34/sp.pi))==0
c=-40/sp.sqrt(34*sp.pi)
coef=sp.simplify(4*3*sp.Rational(1,20)*sp.Rational(3,5)/(1-sp.Rational(3,5))*c**2)
assert sp.simplify(coef-sp.Rational(9600,17)*sp.Rational(1,20)*sp.Rational(3,5)/sp.Rational(2,5)/sp.pi)==0

def wave(beta,x):
    return (cos(beta)*sin(3*x)+sin(beta)*sin(5*x))/sqrt(pi)

def deriv(beta,x):
    return (3*cos(beta)*cos(3*x)+5*sin(beta)*cos(5*x))/sqrt(pi)

def A_sigma(z,sig):
    return -(34*sig*z+40*z**3)/sqrt(34*pi)

def B_sigma(z,sig):
    return -(34*sig+120*z*z)/sqrt(34*pi)

# Test all five finite parameter stationary states using exact root equations in u=sin(x)^2.
for eps in [0.03,0.015,0.0075]:
    beta_minus=beta_star-eps
    a=3*cos(beta_minus)+5*sin(beta_minus)
    b=-4*cos(beta_minus)-20*sin(beta_minus)
    d=16*sin(beta_minus)
    roots_psi=sorted(float(r.real) for r in np.roots([d,b,a]) if abs(r.imag)<1e-12 and 0<r.real<0.1)
    roots_der=sorted(float(r.real) for r in np.roots([5*d,3*b,a]) if abs(r.imag)<1e-12 and 0<r.real<0.1)
    assert len(roots_psi)==len(roots_der)==1
    node=sqrt(roots_psi[0]); antinode=sqrt(roots_der[0])
    assert abs(node/sqrt(eps)-sqrt(17/20))<0.1
    assert abs(antinode/sqrt(eps)-sqrt(17/60))<0.1

# Numerical time-rescaling tests for each sign of detuning.
# Use initial wave amplitude zero; the finite transient is invisible at slow time.
for sig in [-1,1]:
    errs=[]
    for eps in [0.025,0.0125,0.00625]:
        beta=beta_star+sig*eps
        XX=0.65
        ww=0.0
        horizon=0.35
        steps=round(horizon/eps**2)
        for _ in range(steps):
            px=XX*sqrt(eps)
            newx=px-coupling*ww*deriv(beta,px)
            neww=mu*(ww+wave(beta,px))
            XX,ww=newx/sqrt(eps),neww
        target=solve_ivp(lambda t,z:[-coupling*mu/(1-mu)*A_sigma(z[0],sig)*B_sigma(z[0],sig)],
                         (0,steps*eps**2),[0.65],rtol=1e-12,atol=1e-12).y[0,-1]
        errs.append(abs(XX-target))
    assert errs[2]<errs[1]<errs[0],(sig,errs)

# Check the algebraic reciprocal-fourth-power slope numerically.
ww=0.0; xx=0.15
slopes=[]
for it in range(1,200001):
    newx=xx-coupling*ww*deriv(beta_star,xx)
    neww=mu*(ww+wave(beta_star,xx))
    xx,ww=newx,neww
    if it in (20000,200000):
        slopes.append(1/(it*xx**4))
limit=9600*coupling*mu/(17*pi*(1-mu))
assert abs(slopes[-1]-limit)<abs(slopes[0]-limit)
assert abs(slopes[-1]-limit)/limit<0.08,(slopes,limit)
print('VERIFY_OK', {'crossover_errors_last':errs[-1], 'slope_200000':slopes[-1], 'slope_exact':limit})
