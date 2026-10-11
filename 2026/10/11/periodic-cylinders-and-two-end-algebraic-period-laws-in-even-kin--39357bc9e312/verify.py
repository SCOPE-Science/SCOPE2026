"""Reproducibility checks for an even-kinetic Hamiltonian skew flow.

These tests check exact polynomial identities and numerical consequences of
proved quadratures. Finite numerical checks are not a substitute for proofs.
"""
from math import isfinite

import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import beta as B

u, v = sp.symbols("u v", real=True)
V = u**2 - u**3 / 3
assert sp.expand(sp.Rational(4, 3) - V - (u + 1) * (2 - u)**2 / 3) == 0
for p in (4, 6, 8):
    H = v**p / p + V
    assert sp.expand(sp.diff(H, u) * v**(p-1) + sp.diff(H, v) * u*(u-2)) == 0


def data(p, h):
    alpha = 1 - 1 / p
    a = brentq(lambda z: z*z - z**3/3 - h, -1, 0)
    b = brentq(lambda z: z*z - z**3/3 - h, 0, 2)
    c = brentq(lambda z: z*z - z**3/3 - h, 2, 4)
    span = b - a
    def moment(k):
        def smooth(t):
            z = a + span*t
            return (span**(1-2*alpha))*(3/(c-z))**alpha * z**k
        return quad(smooth, 0, 1, weight="alg", wvar=(-alpha,-alpha), epsabs=2e-11, epsrel=2e-11)[0]
    i0, i1, i2 = (moment(k) for k in (0,1,2))
    T = 2*p**(-alpha)*i0
    drift = i1/i0 - 1
    assert abs(i2 - 2*i1) < 2e-7 * max(1,i2), (p,h,i1,i2)
    return T, drift


for p in (4,6):
    alpha, exponent = 1-1/p, 0.5-1/p
    csmall = 2*p**(-alpha)*B(0.5,1/p)
    csaddle = p**(-alpha)*B(1/p,exponent)
    cdrift = 2*3**(2/p)*B(1/p,2/p)/B(1/p,exponent)
    hsmall = 1e-4
    ts,ds = data(p,hsmall)
    assert abs(ts*hsmall**exponent/csmall - 1) < .018
    assert abs((ds + 1)/hsmall - p/(2*(p+2))) < .001
    delta = 1e-5
    tl,dl = data(p,4/3-delta)
    assert abs(tl*delta**exponent/csaddle - 1) < .12
    assert abs((1-dl)/(cdrift*delta**exponent) - 1) < .12
    assert data(p,1.2)[1] < 0 < data(p,1.3)[1]
    root = brentq(lambda h:data(p,h)[1],1.2,1.3,xtol=1e-13)
    assert 2/3 < root < 4/3
    assert isfinite(data(p,root)[0])

# One-return physical-time check for p=4 at a numerically bracketed zero.
p=4
h = brentq(lambda h:data(p,h)[1],1.2,1.3,xtol=1e-13)
T,drift=data(p,h)
y0=[0.,0.,(p*h)**(1/p)]
sol=solve_ivp(lambda t,y:(y[1]-1, y[2]**(p-1), y[1]*(y[1]-2)),[0,T],y0,
              method='DOP853',rtol=2e-12,atol=2e-12)
assert sol.success and max(abs(sol.y[:,-1]-y0))<1e-7
print('CHECK_OK')
