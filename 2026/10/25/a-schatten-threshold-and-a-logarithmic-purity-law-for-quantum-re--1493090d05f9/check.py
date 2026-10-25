"""Finite diagnostics for a uniform-history quantum dephasing law.

Requires Python 3, NumPy, and mpmath. These tests do not certify infinite-dimensional limits.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 40
passed = 0

def check(cond, message):
    global passed
    assert bool(cond), message
    passed += 1

def f(freq, t, r=1):
    z = mp.mpc(0, freq)
    a = z / (r + z)
    return complex(mp.hyp1f1(a, 1, -(r + z) * t))

def asymptotic(freq, t, r=1):
    z = mp.mpc(0, freq)
    a = z / (r + z)
    return complex(mp.power((r + z) * t, -a) / mp.gamma(1-a))

for t in (0.2, 1.1, 6.0, 22.0):
    check(abs(f(0,t)-1)<1e-11, 'zero-frequency mode')
    for w in (0.03,0.2,0.8):
        check(abs(f(-w,t)-f(w,t).conjugate())<1e-11, 'conjugate-frequency symmetry')
        check(abs(f(w,t))<=1+1e-9, 'CPTP characteristic-function bound')
for w in (0.13,0.5,1.1):
    check(abs(f(w,80)-asymptotic(w,80)) < 0.02, 'Kummer large-time expansion')

# Directly test the scalar Volterra equation at finite time.
for w in (0.1, 0.7):
    t=1.1
    z=mp.mpc(0,w)
    a=z/(1+z)
    val=mp.hyp1f1(a,1,-(1+z)*t)
    deriv=-z*mp.hyp1f1(a+1,2,-(1+z)*t)
    integ=mp.quad(lambda s: mp.hyp1f1(a,1,-(1+z)*s),[0,t])
    check(abs(complex(deriv + (1+z)*val -integ/t))<1e-10, 'Volterra differential equation')

# A continuous-spectrum rank-one state has purity integral
# 2 * integral_0^1 (1-w) |f(w,t)|^2 dw for a flat energy band.
# Compare the exact integral with the sharply localised Kummer asymptotic.
for t in (30.0, 120.0):
    x=np.linspace(0,1,121)
    y=np.array([abs(f(float(w),t))**2 for w in x])
    approx=np.array([abs(asymptotic(float(w),t))**2 for w in x])
    exact=float(2*np.trapezoid((1-x)*y,x))
    proxy=float(2*np.trapezoid((1-x)*approx,x))
    check(0<exact<1, 'purity bounds')
    check(abs(proxy-exact)<0.03, 'spectral purity integral')

# Each eigenpair coherence is a literal 2-by-2 trace-norm witness.
for w in (1e-4, 0.01, 0.4):
    t=11
    c=f(w,t)
    rho=np.array([[0.5,0.5*c],[0.5*c.conjugate(),0.5]])
    evals=np.linalg.eigvalsh(rho)
    check(evals.min()>=-1e-10, 'positivity of dephased qubit')
    check(abs(float(np.trace(rho).real)-1)<1e-12, 'trace preserved')
    diff=rho-0.5*np.eye(2)
    check(abs(float(np.linalg.svd(diff,compute_uv=False).sum())-abs(c))<1e-10,'exact block trace norm')

# Small Bohr gaps keep almost all coherence over any fixed finite horizon.
for t in (1.0,9.0,90.0):
    check(abs(f(1e-9,t)-1)<1e-5, 'frequency continuity at zero')
print('PASS:',passed,'finite deterministic assertions')
