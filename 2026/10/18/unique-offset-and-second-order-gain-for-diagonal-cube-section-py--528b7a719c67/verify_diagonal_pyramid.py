#!/usr/bin/env python3
"""Reproducible exact asymptotic coefficient and sample numerical checks.

Requires Python 3 with sympy and scipy for the optional numerical portion.
All algebraic equalities below use exact SymPy rational arithmetic.
"""
from fractions import Fraction as F
import math

# Fourier scaling moment values for a centered Gaussian of variance 12.
M = {0: 1}
for k in range(1, 7):
    M[2*k] = M[2*k-2] * (2*k-1) * 12
assert [M[i] for i in (2,4,6,8)] == [12,432,25920,2177280]
a0 = -F(M[4], 2880)
b0 = F(M[8], 2*2880**2)-F(M[6],181440)
assert a0 == -F(3,20) and b0 == -F(13,1120)
# Coefficients f_n(t)/f_n(0) = 1 + a(t)/n + b(t)/n^2.
# a(t)=-6t^2, b(t)=18t^2/5+18t^4.
t = F(1,6)
first = 2*t-6*t*t
second = F(18,5)*t*t - 12*t**3 + 18*t**4
assert first == F(1,6) and second == F(7,120)
assert b0 + second + a0*first == F(73,3360)
# Derivative of log of pyramid volume: (2-12t)/n+(16t/5)/n^2.
shift = F(16,5)*t/12
assert shift == F(2,45)

# Exact n=3 maximizer and best volume.
from sympy import symbols, sqrt, simplify, Rational, diff
x = symbols('x', real=True)
v3 = (Rational(3,2)+x)*(Rational(3,4)-x*x)/3
xstar=(sqrt(2)-1)/2
assert simplify(diff(v3,x).subs(x,xstar))==0
assert simplify(v3.subs(x,xstar)-(1+sqrt(2))/6)==0
assert 0 < float(xstar) < .5

# Independent Fourier-integral evaluation of f_n and its derivative.
# For n>=8, absolute convergence is rapid and the n=100 tail is negligible.
from scipy.integrate import quad
from scipy.optimize import brentq

def val_deriv(n,t):
    def spectral(s):
        return (math.sin(s/2)/(s/2))**n if s else 1.
    # scipy quad on [0,40] suffices for n>=8; tail below 1e-7 for n>=8.
    f = quad(lambda s: math.cos(t*s)*spectral(s),0,40,epsabs=2e-11,limit=250)[0]/math.pi
    df=quad(lambda s: -s*math.sin(t*s)*spectral(s),0,40,epsabs=2e-11,limit=250)[0]/math.pi
    return f,df
for n in (8,20,100):
    central = val_deriv(n,0)[0]
    tn=brentq(lambda z: val_deriv(n,z)[1]+val_deriv(n,z)[0]/(n/2+z),0,.35,xtol=2e-12)
    ft=val_deriv(n,tn)[0]
    ratio=(1+2*tn/n)*ft/central
    pred_t=float(t+shift/n)
    pred_r=1+1/(6*n)+7/(120*n*n)
    assert abs(tn-pred_t) < 0.00025, (n,tn,pred_t)
    assert abs(ratio-pred_r) < 0.00003, (n,ratio,pred_r)
    print(f'n={n}: optimal offset={tn:.9f}; ratio={ratio:.10f}; expansions t={pred_t:.9f}, ratio={pred_r:.10f}')
print('PASS: exact rational coefficients, dimension-three formula, and numerical checks')
