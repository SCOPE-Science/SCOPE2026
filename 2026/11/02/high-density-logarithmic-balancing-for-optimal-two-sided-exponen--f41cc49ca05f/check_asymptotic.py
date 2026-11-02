#!/usr/bin/env python3
"""Supplementary numerical checks of the sharp exponential Gabor optimizer asymptotics.

The infinite-density asymptotic theorem relies on its analytic proof, not this finite sample.
"""
import mpmath as mp

mp.mp.dps = 60

def terms(t, q):
    x = t / q
    a = x / mp.sinh(x)
    b = x / mp.tanh(x)
    u = t / mp.sinh(t)
    ap = (1 - x / mp.tanh(x)) / (q * mp.sinh(x))
    bp = (1/mp.tanh(x) - x/mp.sinh(x)**2) / q
    up = (1 - t/mp.tanh(t)) / mp.sinh(t)
    kappa = (mp.coth(t/2)**2) * (b + u)/(a - u)
    deriv = -2/mp.sinh(t) + (bp+up)/(b+u) - (ap-up)/(a-u)
    return kappa, deriv

errors=[]
for q in (2,3,4,8,16,32,64,128,256,512,1024,4096,16384):
    qq=mp.mpf(q)
    loc=2*mp.log(2*qq)
    root=mp.findroot(lambda t:terms(t,qq)[1], (loc+mp.mpf('0.001'),loc+mp.mpf('0.1')))
    k, d = terms(root, qq)
    logq=mp.log(qq)
    residual = qq**2 * (k-1) - (2*mp.log(2*qq)**2+2*mp.log(2*qq)+1)
    print(f'q={q:6d} location={float(root):.12f} shift={float(root-loc):.9g} residual={float(residual):.9g} derivative={float(d):.3g}')
    assert root > 0 and k > 1
    assert abs(d) < mp.mpf('1e-44')
    errors.append(abs(residual))
assert all(errors[i+1] < errors[i] for i in range(4,len(errors)-1))
print('PASS: stationarity, monotone high-q residual decay, positive frame conditioning.')
