"""Reproduce the width law of a triangle sampled on the unit circle.
Run: python verify_inscribed_triangle_width.py
Dependencies: numpy, scipy, sympy.
"""
from math import pi, sin, cos, asin, sqrt, log
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq


def width_cdf(t):
    if t <= 0: return 0.0
    if t >= 1.5: return 1.0
    b0 = brentq(lambda b: 2*sin(b)*cos(b/2)-t, 0., pi/3., xtol=2e-14)
    b1 = asin(sqrt(t/2.))
    initial = (pi*b0)/2. - .75*b0*b0
    remainder = quad(lambda b: asin(min(1.,t/(2*sin(b))))-b,
                     b0, b1, epsabs=5e-12, epsrel=5e-12, limit=200)[0]
    return 12./pi**2*(initial+remainder)


# Check symbolic integrals independently, including all normalization factors.
b = sp.symbols('b', real=True)
l = (sp.pi-b)/2
j0 = sp.integrate(l-b, (b,0,sp.pi/3))
assert sp.simplify(12*j0/sp.pi**2-1)==0
j1 = sp.integrate(sp.sin(b)*(sp.cos(b)-sp.cos(l)), (b,0,sp.pi/3))
assert sp.simplify(24*j1/sp.pi**2-5/sp.pi**2)==0
j2_inner = (l-b)/2-(sp.sin(2*l)-sp.sin(2*b))/4
j2 = sp.integrate(sp.sin(b)**2*j2_inner, (b,0,sp.pi/3))
assert sp.simplify(48*j2/sp.pi**2-(1-sp.Rational(47,8)/sp.pi**2))==0
print('EXACT_SPACINGS_NORMALIZATION_AND_BOTH_MOMENT_INTEGRALS_OK')

# Independent Euclidean altitude reconstruction from Cartesian vertices,
# using ordinary cross products and maximum Euclidean side length.
rng = np.random.default_rng(20261020)
raw = rng.uniform(0,2*pi,size=(32000,3))
xy = np.stack((np.cos(raw),np.sin(raw)),axis=-1)
a = xy[:,0,:]; c = xy[:,1,:]; d = xy[:,2,:]
longest = np.maximum.reduce([np.linalg.norm(a-c,axis=1),
                            np.linalg.norm(a-d,axis=1),
                            np.linalg.norm(c-d,axis=1)])
area_double = np.abs((c[:,0]-a[:,0])*(d[:,1]-a[:,1])-(c[:,1]-a[:,1])*(d[:,0]-a[:,0]))
width_from_cartesian = area_double/longest
ordered = np.sort(raw,axis=1)
gaps = np.concatenate((np.diff(ordered,axis=1),
                       2*pi-ordered[:,2:3]+ordered[:,0:1]),axis=1)/2
smallest = np.sort(gaps,axis=1)
width_from_gaps = 2*np.sin(smallest[:,0])*np.sin(smallest[:,1])
assert np.max(np.abs(width_from_cartesian-width_from_gaps))<1e-11
print('DIRECT_CARTESIAN_MIN_ALTITUDE_EQUALS_ORDERED_GAP_FORMULA_OK')

# Independent 2D quadrature of the moments, without using antiderivatives.
for exponent,target in [(1,5/pi**2),(2,1-47/(8*pi**2))]:
    val=12/pi**2*quad(lambda z:quad(lambda y:(2*sin(z)*sin(y))**exponent,
           z,(pi-z)/2,epsabs=2e-10)[0],0,pi/3,epsabs=2e-10)[0]
    assert abs(val-target)<2e-11,(exponent,val,target)
print('INDEPENDENT_NUMERICAL_TWO_DIMENSIONAL_MOMENTS_OK')

# Direct Haar/circle sampling with a fixed reproducible seed.
N=450000
angle = np.sort(rng.uniform(0,2*pi,size=(N,3)),axis=1)
half_gaps = np.concatenate((np.diff(angle,axis=1),
                 2*pi-angle[:,2:3]+angle[:,0:1]),axis=1)/2
half_gaps.sort(axis=1)
w=2*np.sin(half_gaps[:,0])*np.sin(half_gaps[:,1])
assert abs(w.mean()-5/pi**2)<0.004
assert abs((w*w).mean()-(1-47/(8*pi**2)))<0.004
for t in [0.025,0.1,0.25,0.5,0.75,1.,1.25,1.4]:
    val=width_cdf(t)
    assert 0<val<1 and abs(float(np.mean(w<=t))-val)<0.004
print('DIRECT_UNIFORM_CIRCLE_SAMPLING_CDF_MOMENTS_OK',N)

# Both tail coefficients by direct quadrature; the first verifies the
# sharper two-term expression rather than only its leading logarithm.
for t in [1e-3,1e-4,1e-5]:
    approx=(3*t/pi**2)*(log(8/t)+1)
    assert abs(width_cdf(t)-approx)/t<0.0003
for e in [0.003,0.001]:
    coeff=(1-width_cdf(1.5-e))/(e*e)
    assert abs(coeff-12/pi**2)<0.02
print('TWO_TERM_THIN_TAIL_AND_SHARP_EQUILATERAL_TAIL_OK')
print('ALL_RANDOM_INSCRIBED_TRIANGLE_WIDTH_CHECKS_OK')
