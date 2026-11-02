#!/usr/bin/env python3
"""Reproducible high-precision consistency checks for the rational sine interval map.

Requires mpmath. This numerical diagnostic does not replace the analytic proof.
"""
import mpmath as mp

mp.mp.dps = 70
pi = mp.pi
c = mp.acos(-1/pi)/pi
s = mp.sin(pi*c)
rcrit = (s-c)/(c*c)
A = 1/(6*s)
C = (s*pi*pi/2 + 1/(3*s) + rcrit*(c/(3*s)-1))/(c*c)
k = pi*pi*c**4/(2*s)

def f(x, r):
    return mp.sin(pi*x)/(1+r*x)

def fp(x, r):
    return (pi*mp.cos(pi*x)*(1+r*x)-r*mp.sin(pi*x))/(1+r*x)**2

def m(d):
    return mp.acos(-d/mp.sin(pi*d))/pi if d else c

def F(d, r):
    mm=m(d)
    return mp.sin(pi*mm)*mp.cos(pi*d)-mm-r*(mm*mm-d*d)

def bisect(fun, lo, hi, n=240):
    vlo, vhi = fun(lo),fun(hi)
    assert vlo>0 and vhi<0
    for _ in range(n):
        mid=(lo+hi)/2
        if fun(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

dmax=mp.findroot(lambda d:m(d)+d-1, (mp.mpf('0.3'),mp.mpf('0.4')))
assert 0<dmax<mp.mpf('0.5')
assert mp.mpf('0.6')<c<mp.mpf('0.667')
assert 0<rcrit<1
assert abs(f(c,rcrit)-c)<mp.mpf('1e-65')
assert abs(fp(c,rcrit)+1)<mp.mpf('1e-65')
assert C>0 and k>0
count=0
for rvalue in ('0','0.01','0.1','0.3','0.5','0.7','0.8','0.9','0.94'):
    r=mp.mpf(rvalue)
    d=bisect(lambda z:F(z,r),mp.mpf('0'),dmax)
    x,y=m(d)-d,m(d)+d
    assert 0<x<c<y<1
    assert abs(f(x,r)-y)<mp.mpf('1e-65')
    assert abs(f(y,r)-x)<mp.mpf('1e-65')
    assert abs(F(d,r))<mp.mpf('1e-65')
    count+=3

for r in (rcrit,rcrit+mp.mpf('.0001'),rcrit+1,mp.mpf('100')):
    for j in range(1,100):
        d=dmax*j/100
        assert F(d,r)<0
        count+=1

for idx in range(1,101):
    d=dmax*idx/101
    assert mp.diff(lambda z:F(z,mp.mpf('0.95')),d)<0
    count+=1

for delta_txt in ('0.0001','0.000001','0.00000001'):
    delta=mp.mpf(delta_txt)
    r=rcrit-delta
    d=bisect(lambda z:F(z,r),mp.mpf('0'),dmax)
    x,y=m(d)-d,m(d)+d
    lam=fp(x,r)*fp(y,r)
    assert 0<lam<1
    assert abs(d/mp.sqrt(delta/C)-1)<mp.mpf('.02')
    assert abs((1-lam)/delta-4*k)<mp.mpf('0.005')
    count+=3

print('PASS: %s high-precision assertions; r*=%.18f; C=%.14f; k=%.14f; dmax=%.14f' %
      (count+8,float(rcrit),float(C),float(k),float(dmax)))
