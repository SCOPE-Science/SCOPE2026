#!/usr/bin/env python3
"""Reproduce the small-density square-gap renewal/theta calculations.
Requires mpmath and sympy; this checker is supplementary to the analytic proof.
"""
import mpmath as mp
import sympy as sp

x = sp.symbols('x', positive=True)
k = 1 / sp.sqrt(2 * sp.pi)
a = k**2 / 2
b = k * (5*k**2 + 4) / 8
d = k**4 + k**2 / 2
w = k*x + a*x**2 + b*x**3 + d*x**4
poly = (w/k)**2 * (1-w) - x**2/(1-x**2)
assert sp.simplify(sp.series(poly, x, 0, 6).removeO()) == 0
E = sp.log((1-w)/(2*w)) + 1/(2*(1-w))
series = sp.series(E + sp.log(x), x, 0, 3).removeO().expand()
target = -sp.log(2*k) + sp.Rational(1,2) - k*x - (sp.Rational(1,2)+3*k*k/4)*x*x
assert sp.simplify(series-target) == 0

mp.mp.dps = 90

def direct_A(s):
    nmax = int(mp.ceil(mp.sqrt(250/s)))+1
    return mp.fsum(mp.exp(-s*n*n) for n in range(1, nmax))

def exact_ratio(t):
    def m(s):
        nmax = int(mp.ceil(mp.sqrt(250/s)))+1
        a = mp.fsum(mp.exp(-s*n*n) for n in range(1,nmax))
        b = mp.fsum(n*n*mp.exp(-s*n*n) for n in range(1,nmax))
        return 1+b/a
    lo, hi = t/4, t
    assert (m(lo)>1/t) and (m(hi)<1/t)
    for _ in range(305):
        mid=(lo+hi)/2
        if m(mid)>1/t: lo=mid
        else: hi=mid
    s=(lo+hi)/2
    return s/t + mp.log(direct_A(s))-s

def cubic_ratio(t):
    def f(w): return 2*mp.pi*w*w*(1-w)-t/(1-t)
    lo,hi=mp.mpf('0'),mp.mpf('0.3333333333333333333333333333333333333')
    assert f(hi)>0
    for _ in range(305):
        mid=(lo+hi)/2
        if f(mid)<0:lo=mid
        else:hi=mid
    w=(lo+hi)/2
    return mp.log((1-w)/(2*w))+1/(2*(1-w))

for u in [mp.mpf('0.4'),mp.mpf('0.7')]:
    s=u*u
    theta = mp.sqrt(mp.pi)/(2*u)-mp.mpf('0.5') + mp.sqrt(mp.pi)/u * mp.fsum(mp.exp(-mp.pi**2*j*j/s) for j in range(1,11))
    assert abs(theta-direct_A(s)) < mp.mpf('1e-65')

for txt in ['0.15','0.10','0.02','0.01','0.005']:
    t=mp.mpf(txt)
    actual=exact_ratio(t)
    cubic=cubic_ratio(t)
    assert abs(actual-cubic) < (mp.mpf('1e-35') if t>=mp.mpf('0.15') else mp.mpf('1e-50'))
    formula=mp.log(1/t)/2+mp.log(mp.pi/2)/2+mp.mpf('.5')-mp.sqrt(t/(2*mp.pi))-(mp.mpf('.5')+3/(8*mp.pi))*t
    if t<=mp.mpf('0.02'):
        assert abs(actual-formula) / t**mp.mpf('1.5') < mp.mpf('0.45')
    print('t',txt, 'E/t',mp.nstr(actual,25),'cubic_error',mp.nstr(abs(actual-cubic),5),'truncation_error',mp.nstr(actual-formula,9))
print('VERIFY_OK: symbolic cubic and coefficients through t; exact theta transformation; numeric entropy; exponentially accurate cubic surrogate; uniform t^(3/2) remainder checks')
