#!/usr/bin/env python3
"""Supplementary algebraic checks and finite numerical consistency tests for the small-skew theorem."""
from __future__ import annotations
import math
import sympy as sp
from mpmath import mp

mp.dps = 75
r = sp.symbols('r', positive=True)
r0 = 2 - sp.sqrt(3)
J = r**sp.Rational(1, 4) * (1-r) / (1-r+r*r)**sp.Rational(3, 4)
S = sp.sqrt(r / (1-r+r*r))
P = J - sp.Rational(9, 2)*J*S + sp.Rational(7, 2)*J**3
c = (sp.Rational(4, 27))**sp.Rational(1, 4)
checks = 0

def check(condition, why):
    global checks
    assert bool(condition), why
    checks += 1

def exact_zero(expr, why):
    check(sp.simplify(sp.radsimp(expr)) == 0, why)

exact_zero(J**4-r*(1-r)**4/(1-r+r*r)**3, 'quartic J')
exact_zero(S**2-r/(1-r+r*r), 'quadratic S')
exact_zero(sp.diff(sp.log(J),r) + (r+1)*(r*r-4*r+1)/(4*r*(r-1)*(r*r-r+1)), 'critical polynomial')
exact_zero(J.subs(r,r0)**4-sp.Rational(4,27), 'c fourth power')
exact_zero(S.subs(r,r0)**2-sp.Rational(1,3), 'S value')
exact_zero((sp.diff(J,r,2)/J).subs(r,r0)+sp.Rational(7,2)+2*sp.sqrt(3), 'nondegeneracy')
exact_zero((P/J).subs(r,r0)-1+sp.Rational(13,18)*sp.sqrt(3), 'quadratic value')
exact_zero((-sp.diff(P,r)/sp.diff(J,r,2)).subs(r,r0)+6-3*sp.sqrt(3), 'quadratic shift')
exact_zero((sp.Rational(3,2)*c**2)**2 - sp.Rational(1,3), 'linear value')

r0f = 2-mp.sqrt(3)
cf = (mp.mpf(4)/27)**mp.mpf('.25')
kf = 3*mp.sqrt(3)-6
P0 = cf*(1-13*mp.sqrt(3)/18)

def vecs(rr):
    s=rr**mp.mpf('.25')
    a=(1+s**4)**mp.mpf('.25')
    b=(1+s**12)**mp.mpf('.25')
    return (1/a,s/a),(-s**3/b,1/b)

def fourth(v):
    return sum(z**4 for z in v)

def f_direct(rr,tt):
    x,y=vecs(rr)
    return (fourth((x[0]+tt*y[0],x[1]+tt*y[1]))**mp.mpf('.25')-
            fourth((tt*x[0]-y[0],tt*x[1]-y[1]))**mp.mpf('.25'))/tt

def f_scalar(rr,tt):
    jj=rr**mp.mpf('.25')*(1-rr)/(1-rr+rr*rr)**mp.mpf('.75')
    ss=mp.sqrt(rr/(1-rr+rr*rr))
    return ((1+6*ss*tt**2+4*jj*tt**3+tt**4)**mp.mpf('.25')-
           (1-4*jj*tt+6*ss*tt**2+tt**4)**mp.mpf('.25'))/tt

for frac in range(1,100):
    rr=mp.mpf(frac)/100
    x,y=vecs(rr)
    check(abs(fourth(x)-1)<mp.mpf('1e-65'), 'unit x')
    check(abs(fourth(y)-1)<mp.mpf('1e-65'), 'unit y')
    check(abs(x[0]**3*y[0]+x[1]**3*y[1])<mp.mpf('1e-65'), 'Birkhoff')
    for tt in (mp.mpf('.0008'), mp.mpf('.005'), mp.mpf('.03')):
        check(abs(f_direct(rr,tt)-f_scalar(rr,tt))<mp.mpf('1e-64'),'direct norm scalar reduction')

for tt in [mp.mpf('0.0005'),mp.mpf('0.002'),mp.mpf('0.005'),mp.mpf('0.01')]:
    fun=lambda x:f_scalar(x,tt)
    opt=mp.findroot(lambda x:mp.diff(fun,x), (r0f-mp.mpf('.002'),r0f+mp.mpf('.002')))
    check(0<opt<1, 'interior stationary')
    check(abs(mp.diff(fun,opt))<mp.mpf('1e-59'), 'stationarity')
    check(mp.diff(fun,opt,2)<0, 'local maximum')
    check(abs(opt-r0f-kf*tt**2)<tt**3*10, 'quadratic optimizer shift')
    check(abs(fun(opt)-(cf+tt/mp.sqrt(3)+P0*tt**2))<tt**3*5, 'uniform cubic remainder scale')
    for i in range(101):
        rr=mp.mpf(i)/100
        if 0<rr<1:
            check(fun(opt)+mp.mpf('1e-50')>=fun(rr),'grid majorization')

print('PASS:', checks,'exact and deterministic numerical assertions')
print('r0=',mp.nstr(r0f,20),'c=',mp.nstr(cf,20))
print('quadratic coefficient=',mp.nstr(P0,20),'displacement=',mp.nstr(kf,20))
