"""Independent checks of intrinsic pair-distance moments on truncated Euclidean cones.
Only numerical diagnostics and exact algebraic identities; the analytic proof is in RESULT.md.
"""
from fractions import Fraction
from math import pi, sin, sqrt
from numpy.polynomial.legendre import leggauss
import numpy as np
import sympy as sp

def F(t):
    return 1-8*sin(t)/(9*t)

def H(t):
    return 5/3+sin(2*t)/(4*t)-32*sin(t)/(15*t)

def K(t):
    return H(t)/F(t)**2

def Q(t):
    return F(t)/t

p=sp.symbols('p',positive=True)
q=sp.symbols('q',positive=True)
assert sp.simplify((sp.Rational(5,3)-sp.Rational(64,15)/p)-sp.Rational(5,3)*(1-sp.Rational(16,9)/p)**2-32*(63*p-200)/(1215*p**2))==0
assert sp.simplify((sp.Rational(5,3)-sp.Rational(143,80)*q)-sp.Rational(5,3)*(1-2*q/3)**2-q*(939-1600*q)/2160)==0
assert Fraction(7,12)<Fraction(939,1600)
assert Fraction(31,10)<Fraction(22,7)<Fraction(200,63)
assert Fraction(81,1)*Fraction(31,10)>Fraction(200,1)*(Fraction(9,4)-1)
assert K(pi/2)<5/3<K(2*pi/3)
assert Q(pi/2)<1/pi<Q(9*pi/10)
print('EXACT_ENDPOINT_SIGN_IDENTITIES_PASSED')

# Direct quadrature integrates the original two-point geodesic metric,
# not the derived closed moments. Independently approximates second/fourth moments.
nodes,weights=leggauss(52)
u=(nodes+1)/2
w=weights/2
R1=u[:,None,None]
R2=u[None,:,None]
radweight=(2*u*w)[:,None,None]*(2*u*w)[None,:,None]
for t in [0.36, pi/3,pi/2,2*pi/3, 9*pi/10]:
    delta=t*u
    dw=t*w/t
    metric2=R1**2+R2**2-2*R1*R2*np.cos(delta[None,None,:])
    m2=np.sum(radweight*dw[None,None,:]*metric2)
    m4=np.sum(radweight*dw[None,None,:]*metric2**2)
    assert abs(m2-F(t))<2e-13,(t,m2,F(t))
    assert abs(m4-H(t))<2e-13,(t,m4,H(t))
print('INDEPENDENT_THREE_FOLD_DIRECT_GEODESIC_QUADRATURE_PASSED')

# Construct three nonisometric examples for each open-ambiguity claim.
from scipy.optimize import brentq
level_K=1.69
intervals=[(1e-7,pi/2),(pi/2,2*pi/3),(2*pi/3,pi)]
roots_K=[brentq(lambda t:K(t)-level_K,*ab,xtol=1e-14) for ab in intervals]
assert all(a<b for a,b in zip(roots_K,roots_K[1:]))
for t in roots_K:
    radius=1/sqrt(F(t))
    assert abs(radius**2*F(t)-1)<2e-13
    assert abs(radius**4*H(t)-level_K)<2e-12
print('TRIPLE_MOMENT_SIGNATURE_WITNESSES_PASSED',[(round(t,12),round(1/sqrt(F(t)),12)) for t in roots_K])
level_Q=.31865
intervals=[(1e-7,pi/2),(pi/2,9*pi/10),(9*pi/10,pi)]
roots_Q=[brentq(lambda t:Q(t)-level_Q,*ab,xtol=1e-14) for ab in intervals]
assert all(a<b for a,b in zip(roots_Q,roots_Q[1:]))
for t in roots_Q:
    radius=1/sqrt(t)
    assert abs(t*radius**2-1)<2e-13
    assert abs(radius**2*F(t)-level_Q)<2e-12
print('TRIPLE_AREA_SECOND_MOMENT_WITNESSES_PASSED',[(round(t,12),round(1/sqrt(t),12)) for t in roots_Q])

# Spot-check direct point-pair Monte Carlo with angular periodic separation.
rng=np.random.default_rng(77823)
N=450000
for t in (pi/3, 2*pi/3):
    r=np.sqrt(rng.uniform(size=N));s=np.sqrt(rng.uniform(size=N))
    a=rng.uniform(0,2*t,size=N);b=rng.uniform(0,2*t,size=N)
    delta=np.abs(a-b);delta=np.minimum(delta,2*t-delta)
    d2=r*r+s*s-2*r*s*np.cos(delta)
    assert abs(d2.mean()-F(t))<0.005
    assert abs(np.mean(d2**2)-H(t))<0.015
print('INDEPENDENT_RANDOM_POINT_PAIR_SAMPLING_PASSED')
print('ALL_CHECKS_PASSED')
