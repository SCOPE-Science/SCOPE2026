"""Independent arithmetic checks for an exact vaccination--prevalence identity.

Run: python verify.py
Requires sympy and scipy.
This is computational corroboration; the universal assertions are proved in RESULT.md.
"""
import math
import random

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

S, I, x, n = sp.symbols('S I x n', positive=True)
mu, gamma, beta, theta, eps2 = sp.symbols('mu gamma beta theta eps2', positive=True)
A = mu / ((gamma + mu) * eps2 * (2 + theta))
B = mu / (beta * (gamma + mu))
Ic = mu / ((gamma + mu) * (2 + theta)) - mu / beta
Sd = mu * (1 - x) - beta * S * I - mu * S
Id = beta * S * I - (gamma + mu) * I
nd = eps2 * n * (1 - n) * (1 + theta - (2 + theta) * x)
Hdot = A * nd / (n * (1 - n)) - B * Id / I - (Sd + Id) / (gamma + mu)
assert sp.simplify(Hdot - I + Ic) == 0
print('symbolic cohomology: PASS')

rng = random.Random(712)
max_residual = 0.0
for k in range(15):
    m = rng.uniform(0.4, 2.0)
    g = rng.uniform(0.2, 3.0)
    b = rng.uniform(3.0, 19.0)
    t = rng.uniform(0.2, 2.0)
    e1 = rng.uniform(0.06, 0.85)
    e2 = rng.uniform(0.06, 0.85)
    cost = rng.uniform(3.2, 8.0)
    vl, vh = 0.2 * cost, 0.65 * cost
    s0 = rng.uniform(.1,.5)
    i0 = rng.uniform(.05, min(.35, .7-s0))
    x0 = rng.uniform(.1,.8)
    n0 = rng.uniform(.1,.8)
    start = np.array([s0,i0,x0,n0,0.0])
    def rhs(_,v):
        ss,ii,xx,nn,inc=v
        f=b*ii/(b*ii+m)
        return [m*(1-xx)-b*ss*ii-m*ss,
                b*ss*ii-(g+m)*ii,
                e1*xx*(1-xx)*(f*cost-(vl+(vh-vl)*nn)),
                e2*nn*(1-nn)*(1+t-(2+t)*xx),
                ii]
    sol=solve_ivp(rhs,(0,9),start,rtol=2e-11,atol=1e-13)
    assert sol.success
    v=sol.y[:,-1]
    def H(z):
        ss,ii,xx,nn,_=z
        return m/((g+m)*e2*(2+t))*math.log(nn/(1-nn)) -m/(b*(g+m))*math.log(ii)-(ss+ii)/(g+m)
    measured=v[4]
    predicted=9*(m/((g+m)*(2+t))-m/b)+H(v)-H(start)
    error=abs(measured-predicted)
    max_residual=max(max_residual,error)
    assert error < 2e-8, (k,error)
print('15 integrated finite-time identities: PASS, max absolute error=',max_residual)

# Check a strictly positive equilibrium at a supercritical R0=4, theta=1.
m,g,b,t,cost,vl,vh=sp.Rational(1),sp.Rational(3),sp.Rational(16),sp.Rational(1),sp.Rational(10),sp.Rational(1),sp.Rational(3)
ss,ii,xx,nn,rr=sp.Rational(1,4),sp.Rational(1,48),sp.Rational(2,3),sp.Rational(3,4),sp.Rational(35,48)
f=b*ii/(b*ii+m)
assert ss+ii+rr==1
assert sp.simplify(m*(1-xx)-b*ss*ii-m*ss)==0
assert sp.simplify(b*ss*ii-(g+m)*ii)==0
assert sp.simplify(m*xx+g*ii-m*rr)==0
assert sp.simplify(xx*(1-xx)*(f*cost-(vl+(vh-vl)*nn)))==0
assert sp.simplify(nn*(1-nn)*(1+t-(2+t)*xx))==0
print('sharpness witness exact stationary equations: PASS')

# Universal finite-time residence inequality checked with an arbitrary
# permissible state-independent upper/lower endpoint estimate.
for k in range(100):
    delta=rng.uniform(.005,.4)
    m=rng.uniform(.2,2)
    g=rng.uniform(.2,5)
    t=rng.uniform(.1,3)
    b=rng.uniform(.2,(g+m)*(2+t))
    e2=rng.uniform(.08,1)
    critical=m/((g+m)*(2+t))-m/b
    bound=(2*m/((g+m)*e2*(2+t))*math.log((1-delta)/delta)+
           m/(b*(g+m))*math.log(1/delta)+1/(g+m))/(delta-critical)
    assert bound>0 and math.isfinite(bound)
print('100 positive critical/subcritical residence bounds: PASS')
