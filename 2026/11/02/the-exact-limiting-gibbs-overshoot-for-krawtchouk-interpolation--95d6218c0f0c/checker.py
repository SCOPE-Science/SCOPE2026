#!/usr/bin/env python3
"""Independent numerical checks for the limiting sign interpolation formula.
Dependency: mpmath (pip install mpmath). No numerical test proves the infinite theorem.
"""
import math
import mpmath as mp
mp.mp.dps = 60

def H(x):
    return mp.digamma((x+1)/2)-mp.digamma(x/2)-1/x

def Hp(x):
    return (mp.polygamma(1,(x+1)/2)-mp.polygamma(1,x/2))/2+1/(x*x)

def F_limit(x):
    return 1-mp.sin(mp.pi*x)*H(x)/mp.pi

def F_finite(M,x):
    product=mp.mpf(1); b=mp.mpf(1); series=mp.mpf(0)
    for k in range(1,M+1):
        b *= mp.mpf(M-k+1)/(M+k)
        product *= (1-x*x/(k*k))
        series += (-1)**k*b*k/(x*x-k*k)
    return 2*x*product*series

xi = mp.findroot(lambda x: mp.pi*mp.cot(mp.pi*x)+Hp(x)/H(x),
                 (mp.mpf('1.3'),mp.mpf('1.5')))
gamma=F_limit(xi)
assert abs(xi-mp.mpf('1.3769917692039388658'))<mp.mpf('5e-19')
assert abs(gamma-mp.mpf('1.0657838882664480991'))<mp.mpf('5e-19')
assert 1 < F_limit(mp.mpf('1.5')) < gamma
assert F_limit(mp.mpf('3.5')) < F_limit(mp.mpf('1.5'))
for M in (1,2,3,5,10,20,50,100,300):
    val=F_finite(M,xi)
    assert val>gamma
    if M>=20:
        assert abs(val-gamma)<mp.mpf('0.2')/M
for x in (mp.mpf('0.1'),mp.mpf('0.4'),mp.mpf('0.9'),mp.mpf('1.3'),mp.mpf('1.7')):
    assert abs(F_finite(1000,x)-F_limit(x))<mp.mpf('0.002')
for n in (1,2,3,4,5):
    assert abs(F_limit(mp.mpf(n))-1)<mp.mpf('1e-50')
print('Numerical interpolation, root, peak and first-lobe checks passed;')
print('critical point:',mp.nstr(xi,36))
print('limiting peak:',mp.nstr(gamma,36))
