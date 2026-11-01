#!/usr/bin/env python3
"""Checks for an ellipsoidal near-diameter crossover theorem.

Requires Python >=3.9, mpmath and sympy. Run: python geometry_crossover_verifier.py
The analytic all-dimensional proof is in RESULT.md; finite checks do not certify it.
"""
import math
from fractions import Fraction
import mpmath as mp
import sympy as sp

mp.mp.dps = 55
checks = 0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def near(a, b, tol, description):
    check(abs(a-b) <= tol*max(1,abs(a),abs(b)), description)

def ball3_radial_tail(s):
    s=mp.mpf(s)
    if s<=0: return mp.mpf(0)
    if s>=2: return mp.mpf(1)
    return mp.mpf(3)/16*(8*s**3-7*s**4+2*s**5-s**6/6)

def spheroid_exact(t, c, x=1):
    t=mp.mpf(str(t));c=mp.mpf(str(c));x=mp.mpf(str(x))
    if c==0:
        return ball3_radial_tail(t*x)
    zmax = mp.sqrt((x-t*x*x/4)/(2*c-t*c*c))
    zmax = min(mp.mpf(1),zmax)
    return mp.quad(lambda z: ball3_radial_tail(2-(2-t*x)/mp.sqrt(1-(2*t*c-t*t*c*c)*z*z)), [0,zmax])

def crossover3(c,x=1):
    c=mp.mpf(str(c));x=mp.mpf(str(x))
    if 2*c<=x:
        return x**3 - 2*c*x*x + mp.mpf(12)/5*c*c*x - mp.mpf(8)/7*c**3
    return mp.mpf(16)/35 * x**mp.mpf('3.5') / mp.sqrt(2*c)

# Exact overlap-lens identity in dimension three.
s=sp.symbols('s',positive=True)
r=sp.symbols('r',real=True)
radial_integrand=sp.Rational(3,16)*r**2*(4+r)*(2-r)**2
lens_integral=sp.integrate(radial_integrand,(r,2-s,2))
expected=sp.Rational(3,16)*(8*s**3-7*s**4+2*s**5-s**6/6)
check(sp.simplify(lens_integral-expected)==0, '3D lens-overlap integral')

# Exact cubic crossover chamber match and fourth derivative jump.
c,x=sp.symbols('c x',positive=True)
lo=x**3-2*c*x**2+sp.Rational(12,5)*c**2*x-sp.Rational(8,7)*c**3
hi=sp.Rational(16,35)*x**sp.Rational(7,2)/sp.sqrt(2*c)
for j in range(4):
    check(sp.simplify((sp.diff(hi,c,j)-sp.diff(lo,c,j)).subs(c,x/2))==0,'C^3 transition')
check(sp.simplify((sp.diff(hi,c,4)-sp.diff(lo,c,4)).subs(c,x/2)-48/x)==0,'fourth derivative jump')

# Compare both crossover formulas with independent angular integration.
for xf in ['0.7','1.0','1.4']:
    for cf in ['0','0.1','0.3','0.35','0.5','0.7','1','3','8']:
        xfmp=mp.mpf(xf); cfmp=mp.mpf(cf)
        zlim=min(mp.mpf(1),mp.sqrt(xfmp/(2*cfmp))) if cfmp else mp.mpf(1)
        angular=mp.quad(lambda z:max(mp.mpf(0),xfmp-2*cfmp*z*z)**3,[0,zlim])
        near(angular,crossover3(cf,xf),mp.mpf('1e-39'),'independent angular integration')

# Exact moving-ellipsoid tail vs limiting coefficient.
for cf in ['0','0.1','0.5','1','4','10']:
    target=mp.mpf(3)/2*crossover3(cf)
    for t in ['0.01','0.002','0.0004']:
        ratio=spheroid_exact(t,cf)/mp.mpf(t)**3
        check(abs(ratio-target)<mp.mpf('2.0')*mp.mpf(t),'uniform-order convergence diagnostic')

# Independent general lens constant, checked at d=2,3,4 against known volumes.
def kappa(d):
    return mp.pi**(mp.mpf(d)/2)/mp.gamma(mp.mpf(d)/2+1)
def K(d):
    return mp.power(2,d+1)*d*kappa(d-1)/((d+1)*(d+3)*kappa(d))
near(K(2),32/(15*mp.pi),mp.mpf('1e-45'),'2D spherical constant')
near(K(3),mp.mpf('1.5'),mp.mpf('1e-45'),'3D spherical constant')
near(K(4),1024/(105*mp.pi),mp.mpf('1e-45'),'4D spherical constant')

# Rank-one large-contraction matching constant in 3D.
T=mp.mpf('100000')
ratio = crossover3(T)*mp.sqrt(2*T)
near(ratio,mp.mpf(16)/35,mp.mpf('1e-40'),'rank-one matching constant')

# Schur majorization: independent deterministic tensor-product Gauss quadrature.
# The azimuth is periodic; the polar coordinate cos(theta) is uniform on [-1,1].
import numpy as np
from numpy.polynomial.legendre import leggauss
zz, ww = leggauss(100)
phis = (np.arange(256)+0.5)*2*np.pi/256
sint = np.sqrt(1-zz[:,None]**2)
squares = [np.broadcast_to(zz[:,None]**2,(100,256)),
           (sint*np.cos(phis)[None,:])**2,
           (sint*np.sin(phis)[None,:])**2]
def angular3(lam, threshold):
    q = sum(float(lam[j])*squares[j] for j in range(3))
    f = np.maximum(0,float(threshold)-2*q)**3
    return float(np.sum(ww[:,None]*f)/(2*256))
for xval in [0.8,2.5]:
    Fbal=angular3([0,0.3,0.3],xval)
    Fmid=angular3([0,0.15,0.45],xval)
    Fsp=angular3([0,0,0.6],xval)
    check(Fbal<Fmid<Fsp,'strict Schur monotonicity sample')

print(f'PASS: {checks} independent symbolic and numerical checks')
