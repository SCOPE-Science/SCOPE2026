#!/usr/bin/env python3
"""Reproduce independent symbolic and numerical checks for the cubic-center period law.

Requires Python 3, SymPy, and mpmath. Numerical tests are finite checks, not a
substitute for the uniform asymptotic proof in RESULT.md.
"""
import math
import sympy as sp
import mpmath as mp

x, y, beta, gamma = sp.symbols('x y beta gamma', positive=True, real=True)
e = sp.exp(beta*x*x)
H_x = beta*x*e*y*y + e*x*(1+gamma*x*x)
H_y = e*y
assert sp.simplify(H_x*y + H_y*(-x-gamma*x**3-beta*x*y*y)) == 0
f = x*sp.exp(beta*x*x/2)/(1+beta*x*x)
assert sp.simplify(sp.diff(f,x) - sp.exp(beta*x*x/2)*(1+beta**2*x**4)/(1+beta*x*x)**2)==0
B = 1+(beta+3*gamma)*x*x+beta*gamma*x**4
assert sp.factor(B-(1+beta*x*x)*(1+gamma*x*x)) == 2*gamma*x*x

mp.mp.dps=48

def period(b,g,a):
    b,g,a=map(mp.mpf,(b,g,a))
    L=1+g*a*a
    def inside(u):
        if u==0: return mp.mpf(0)
        E0=mp.expm1(b*u)/b
        E1=(mp.expm1(b*u)-b*u)/(b*b)
        return L*E0-g*E1
    def integrand(t):
        if t==0: return 4/mp.sqrt(L)
        u=a*a*mp.sin(t)**2
        return 4*a*mp.sin(t)/mp.sqrt(inside(u))
    return mp.quad(integrand,[0,mp.pi/2])

def asymptotic(b,g,a):
    b,g,a=map(mp.mpf,(b,g,a))
    L=1+g*a*a
    r=g*a*a/L
    return 2*mp.pi/(a*mp.sqrt(b*L))*(1+(2*mp.log(2)+r*(2*mp.log(2)-1))/(2*b*a*a))

max_scaled_remainder=0
cases=0
for b,g in [('0.4','0.000001'),('0.4','0.3'),('0.4','10'),
            ('1.2','0.000001'),('1.2','0.3'),('1.2','10')]:
    for a in [8,16,32]:
        t=period(b,g,a)
        pred=asymptotic(b,g,a)
        assert t>0 and pred>0
        remainder=float(abs(t/pred-1)*a**4)
        max_scaled_remainder=max(max_scaled_remainder,remainder)
        assert remainder<100, (b,g,a,remainder)
        cases+=1
for b,g in [('0.4','0.3'),('1.2','10')]:
    vals=[period(b,g,a) for a in [1,2,4,8]]
    assert all(vals[j]>vals[j+1] for j in range(len(vals)-1))
for b,g in [('0.4','0.3'),('1.2','1')]:
    a=mp.mpf('0.008')
    T=period(b,g,a)
    rate=(T/(2*mp.pi)-1)/(a*a)
    predicted=-(mp.mpf(b)+3*mp.mpf(g))/8
    assert abs(rate-predicted)<mp.mpf('.0005'), (rate,predicted)

print('CHECK_OK: conservation, monotonicity comparison identity,',cases,
      'two-term period quadratures, sampled strict decrease, local coefficient.')
print('maximum |relative remainder| * A^4:',format(max_scaled_remainder,'.7f'))
