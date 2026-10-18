#!/usr/bin/env python3
"""Exact arithmetic and independent numerical log-derivative checks for the saturated RTP modality theorem.

Requires Python 3 standard library only. The general theorem is proved in RESULT.md;
these finite checks are a reproducibility aid, not an exhaustive proof.
"""
from fractions import Fraction as F
from math import tanh, atanh, log, exp, isfinite
from random import Random

checks = 0

def ck(condition, msg):
    global checks
    if not condition:
        raise AssertionError(msg)
    checks += 1

def scale_poly(k,m,n):
    # Coefficients of Q(y), ascending powers, under g=4u.
    return (k-m-n, 5*k-6*m-n, -5*k-m, -k)

def poly_eval(coeffs,y):
    s = F(0)
    for coef in reversed(coeffs): s=s*y+coef
    return s

def tanh4_rat(t):
    return 4*t*(1+t*t)/(1+6*t*t+t**4)

# Symbolically verify the four-angle identity from the double-angle formula
# using exact rational t at hundreds of points.
for j in range(1,201):
    t=F(j, 202)
    a=2*t/(1+t*t)
    b=2*a/(1+a*a)
    ck(b==tanh4_rat(t), f'four-angle at t={t}')

# Verify the polynomial clearing of denominators for random rational
# k,m,n,y in the physically meaningful positive parameter octant.
rng=Random(41)
for i in range(1800):
    k=F(rng.randrange(1,30),rng.randrange(1,20))
    m=F(rng.randrange(1,30),rng.randrange(1,20))
    n=F(rng.randrange(1,30),rng.randrange(1,20))
    y=F(rng.randrange(0,100),101)
    coeffs=scale_poly(k,m,n)
    raw=(k*(1-y)-m)*(1+6*y+y*y)-n*(1+y)
    ck(raw==poly_eval(coeffs,y), f'polynomial clearing {i}')
    ck(poly_eval(coeffs,F(1)) == -8*m-2*n,f'endpoint {i}')
    ck(-10*k-2*m-6*k*y < 0, f'concavity {i}')

# Exhibit strict central-negative, interior-positive, boundary-negative
# for a strict-parameter example: v0=1, v1=1/2, gamma0=3/8,
# gamma1=1/4, u=4, g=16.
v0,v1,gamma0,gamma1,u,g=F(1),F(1,2),F(3,8),F(1,4),F(4),F(16)
ck(v0>v1>0 and gamma0>gamma1>0 and g==4*u,'physical domain')
k=u*v1*v1
m=gamma0*v1
n=4*gamma1*v0
coeffs=scale_poly(k,m,n)
ck(coeffs == (F(-3,16),F(46,16),F(-83,16),F(-16,16)), 'example cubic')
ck(poly_eval(coeffs,F(0))==F(-3,16),'negative at center')
ck(poly_eval(coeffs,F(1,4))==F(49,256),'positive middle')
ck(poly_eval(coeffs,F(1))==F(-7,2),'negative right endpoint')

# The derivative is a decreasing quadratic and has exactly one root on (0,1).
# Check strict sign transitions at rational isolating points with exact arithmetic.
for a,b in [(F(7,100),F(8,100)),(F(43,100),F(44,100))]:
    ck(poly_eval(coeffs,a)*poly_eval(coeffs,b)<0, f'root bracket {a},{b}')

# Compare exact-sign prediction with numerical logarithmic-density derivative.
# This is independent of polynomial expansion: it directly uses the derivative
# of the stationary flux expression.
A=float(v0); B=float(v1); c=float(gamma0); d=float(gamma1); uu=float(u); gg=float(g)
for i in range(1,401):
    x=0.0003+i*0.0015
    t=tanh(uu*x)
    tm=tanh(gg*x)
    den=A*A-B*B*t*t
    direct=(2/den)*(uu*B*B*t*(1-t*t)-c*B*t-d*A*tm)
    yy=F(i,1001) # distinct exact rational y for polynomial sign checks below
    sign_curve=float(poly_eval(coeffs,F.from_float(t*t)))
    if abs(direct)>1e-11: ck((direct>0)==(sign_curve>0), f'log derivative sign {i}')
    ck(isfinite(direct),f'finite derivative {i}')

# Exact endpoint and strict-sign existence imply two simple roots of the
# strictly concave Q in (0,1), hence 5 critical points of the even density.
print('PASS', checks, 'checks; example Q(y)=(-3+46y-83y^2-16y^3)/16')
