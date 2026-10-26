#!/usr/bin/env python3
"""Numerical corroboration for the logarithmic annular Szego metric theorem.

Run: python annular_szego_metric_checker.py
Requirements: Python 3, mpmath. Finite numerical checks do not replace the proof.
"""
import mpmath as mp

mp.mp.dps = 65


def modulus(h):
    nome = mp.exp(-h)
    return (mp.jtheta(2, 0, nome) / mp.jtheta(3, 0, nome))**4


def elliptic_metric(h, u):
    m = modulus(h)
    k = mp.ellipk(m)
    c = mp.re(mp.ellipfun('cn', (2*k/mp.pi)*u*1j, m))
    return k*k/(mp.pi*mp.pi)*(m*c*c+(1-m)/(c*c))


def series_metric(h, u, nmax=None):
    if nmax is None:
        nmax = int(mp.ceil(125/(h-2*abs(u))))+20
    terms = []
    for n in range(-nmax, nmax+1):
        t = mp.mpf(n)+mp.mpf('0.5')
        w = mp.exp(2*u*t)/mp.cosh(h*t)
        terms.append((t,w))
    z0 = mp.fsum(w for _, w in terms)
    z1 = mp.fsum(2*t*w for t,w in terms)
    z2 = mp.fsum(4*t*t*w for t,w in terms)
    return (z2/z0-(z1/z0)**2)/4


def roots(h):
    m = modulus(h)
    if m >= mp.mpf('0.5'):
        return [mp.mpf(0)]
    k = mp.ellipk(m)
    complementary = 1-m
    theta = mp.acos((m/complementary)**mp.mpf('0.25'))
    u = (mp.pi/(2*k))*mp.ellipf(theta, complementary)
    return [-u,u]


checks = 0

def close(a,b,atol=mp.mpf('1e-40')):
    global checks
    checks += 1
    assert abs(a-b) < atol, f'failed {a!s} vs {b!s}'

for hs in ('0.9', '2', str(mp.pi), '4', '5', '8'):
    h = mp.mpf(hs)
    m = modulus(h)
    close(mp.pi*mp.ellipk(1-m)/mp.ellipk(m),h)
    for ratio in ('-0.7', '-0.2', '0', '0.25', '0.8'):
        u = h*mp.mpf(ratio)/2
        close(elliptic_metric(h,u),series_metric(h,u))
        close(elliptic_metric(h,u),elliptic_metric(h,-u))
    us = roots(h)
    for u in us:
        v = elliptic_metric(h,u)
        if m >= mp.mpf('0.5'):
            close(v,mp.ellipk(m)**2/mp.pi**2)
        else:
            close(v,2*mp.ellipk(m)**2/mp.pi**2*mp.sqrt(m*(1-m)))
            close(elliptic_metric(h,u),elliptic_metric(h,-u))
    samples = [-h/2+mp.mpf('0.0001')+j*(h-mp.mpf('0.0002'))/199 for j in range(200)]
    min_theorem = elliptic_metric(h,us[0])
    for u in samples:
        checks += 1
        assert elliptic_metric(h,u)>min_theorem-mp.mpf('1e-43')

hc=mp.pi
kc=mp.ellipk(mp.mpf('0.5'))
coefficient=8*kc**6/mp.pi**6
for u in ('0.005','0.003','0.002'):
    x=mp.mpf(u)
    ratio=(elliptic_metric(hc,x)-elliptic_metric(hc,0))/x**4
    checks += 1
    assert abs(ratio/coefficient-1)<mp.mpf('0.0001')

assert modulus(mp.pi)==mp.mpf('0.5') or mp.almosteq(modulus(mp.pi),mp.mpf('0.5'))
print('PASS:', checks, 'numerical corroboration checks')
for hs in ('2',str(mp.pi),'4','5','8'):
    h=mp.mpf(hs)
    print('h=',mp.nstr(h,10),'m=',mp.nstr(modulus(h),10),'minimizers=',[mp.nstr(u,12) for u in roots(h)],'minimum=',mp.nstr(elliptic_metric(h,roots(h)[0]),15))
