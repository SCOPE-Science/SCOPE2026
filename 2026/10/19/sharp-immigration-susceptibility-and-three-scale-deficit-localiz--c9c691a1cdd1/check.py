"""Reproduce symbolic stationarity and sharp weak-immigration asymptotics.

Run: python check.py
Requires: sympy, mpmath.
"""
from math import isfinite
import mpmath as mp
import sympy as sp

x, alpha, D, b, immigration = sp.symbols('x alpha D b immigration', positive=True)
r = D * (alpha+1)
stationary_weight = x**(alpha-1)*sp.exp(-b*x/D-immigration/(D*x))
current = (r*x-b*x**2+immigration)*stationary_weight - sp.diff(D*x**2*stationary_weight,x)
assert sp.simplify(current/stationary_weight) == 0

mp.mp.dps=65

def normalization(a,s):
    return 2*s**(a/2)*mp.besselk(a, 2*mp.sqrt(s))/mp.gamma(a)

def total_variation(a,s):
    a,s=mp.mpf(a),mp.mpf(s)
    z=normalization(a,s)
    crossing=-s/mp.log(z)
    f=lambda y: y**(a-1)*mp.exp(-y)*(mp.exp(-s/y)/z-1)/mp.gamma(a)
    # Integrate the positive side of the one-crossing density difference.
    return mp.quad(f,[crossing,1,5,mp.inf]) if crossing <1 else mp.quad(f,[crossing,5,mp.inf])

def leading_tv(a,s):
    a,s=mp.mpf(a),mp.mpf(s)
    if a<1: return mp.gamma(1-a)/mp.gamma(1+a)*s**a
    if a==1: return s*mp.log(1/s)
    return (a-1)**(a-2)*mp.exp(-(a-1))/mp.gamma(a)*s

for a in ['0.5','1','1.5','2']:
    values=[]
    for s in ['1e-4','1e-7']:
        tv=total_variation(a,s)
        asymp=leading_tv(a,s)
        assert tv>0 and 0.25 < tv/asymp < 1.2
        values.append(float(tv/asymp))
    assert values[1]>values[0]
    print('shape',a,'tv/asymptotic at s=1e-4,1e-7:',values)

# Check Bessel normalization against its independently quadrature-computed integral.
for a in ['0.5','1','1.8']:
    a=mp.mpf(a)
    s=mp.mpf('0.13')
    integral=mp.quad(lambda y:y**(a-1)*mp.exp(-y-s/y)/mp.gamma(a),[0,1,5,mp.inf])
    assert abs(integral/normalization(a,s)-1)<mp.mpf('1e-45')

# Limiting subcritical boundary-layer density has unit integral.
for a in ['0.3','0.5','0.8']:
    a=mp.mpf(a)
    integral = mp.quad(lambda z:z**(a-1)*(-mp.expm1(-1/z)),[0,1,mp.inf])
    assert abs(integral/(mp.gamma(1-a)/a)-1) < mp.mpf("1e-11")
    print('subcritical boundary law normalized:',float(a))

# The normalized signed deficit at alpha=1 spreads uniformly on log scales.
a=mp.mpf(1)
s=mp.exp(-120)
z=normalization(a,s)
tv=total_variation(a,s)
L=mp.log(1/s)
for t in [mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75')]:
    upper=s**(1-t)
    # log coordinates: y = s exp(u), u = log(y/s)
    g=lambda u: s*mp.exp(u)*mp.exp(-s*mp.exp(u))*max(0,1-mp.exp(-mp.exp(-u))/z)
    part=mp.quad(g,[-12,0,t*L])
    ratio=part/tv
    assert abs(ratio-t)<mp.mpf('0.12')
    print('critical log-scale CDF:',str(t),float(ratio))

# Verify an independent incomplete-Gamma integral for the supercritical TV coefficient.
for a in ['1.5','2','3.2']:
    a=mp.mpf(a); aa=a-1
    f=lambda y:y**(a-1)*mp.exp(-y)/mp.gamma(a)
    integral=mp.quad(lambda y:f(y)*(1/aa-1/y),[aa,1+aa,mp.inf])
    exact=aa**(a-2)*mp.exp(-aa)/mp.gamma(a)
    assert abs(integral/exact-1)<mp.mpf('1e-45')
print('ALL CHECKS PASSED')
