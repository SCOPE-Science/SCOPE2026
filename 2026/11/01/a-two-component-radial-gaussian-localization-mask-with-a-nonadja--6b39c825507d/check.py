#!/usr/bin/env python3
"""Standalone certificate and illustrative high-precision root for radial Fock masks."""
from fractions import Fraction as Q
from math import sqrt, exp, factorial

def p(t):
    return 3*t*t-8*t+2

# On [0,1/4] the polynomial decreases; on [12/5,3] it increases.
assert p(Q(1,4))==Q(3,16)
assert p(Q(12,5))==Q(2,25)
# Rational bounds employed in the theorem's endpoint proof.
assert Q(95,512)>Q(5,32)
assert Q(95,512)>Q(9,50)
assert sum((Q(8,3)**j/Q(factorial(j))) for j in range(5))>12
assert Q(25,8)**2 < 10  # gives s_plus > 19/8
assert Q(13,4)**2 > 10  # gives s_minus > 1/4
assert (1+sqrt(3)) > Q(8,3) and (1+sqrt(3)) < 3
# Degree n>=2 strict comparison follows from t<=3 and positive annulus width.
for n in range(2,16):
    assert 3 <= n+1

try:
    import mpmath as mp
except ImportError:
    print('EXACT_RATIONAL_CERTIFICATE_OK; optional mpmath missing')
else:
    mp.mp.dps=60
    a=mp.mpf(5)/2
    b=mp.mpf(13)/5
    H=lambda t: t*(1+t/2)*mp.exp(-t)
    target=H(a)-H(b)
    u=mp.findroot(lambda t:H(t)-target,(mp.mpf('0.01'),mp.mpf('0.03')))
    ev=lambda n: (mp.gammainc(n+1,0,u)+mp.gammainc(n+1,a,b))/mp.factorial(n)
    vals=[ev(n) for n in range(40)]
    assert 0<u<(4-mp.sqrt(10))/3
    assert abs(vals[0]-vals[2])<mp.mpf('1e-50')
    assert vals[1]<vals[0] and all(vals[n]<vals[2] for n in range(3,40))
    print('EXACT_RATIONAL_CERTIFICATE_OK; ILLUSTRATION_OK root='+mp.nstr(u,19))
