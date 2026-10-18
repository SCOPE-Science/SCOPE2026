"""Numerical checks for symmetric conditional-reset sign-memory theorem.

Requirements: Python 3, NumPy, SciPy. Run: python verify.py
These checks support but do not replace the analytic proof.
"""
from math import factorial, gamma, pi, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import jv, kv, lqmn

N = 0

def check(condition, message):
    global N
    if not condition:
        raise AssertionError(message)
    N += 1

def integral(func, lo=0.0, hi=np.inf, **kw):
    return quad(func, lo, hi, epsabs=1e-11, epsrel=1e-11, limit=600, **kw)[0]

def flip(a, eps):
    return a * integral(lambda x: np.exp(-eps * x) * jv(a,x)**2 / x if x else 0.)

def eigen_direct(a, z):
    return 1.0 - 2.0 * flip(a, z/a)

def eigen_coupling(a,z):
    def g(u):
        w = 2*a*np.sinh(u/(2*a))
        return np.exp(-u) * np.arcsin(min(1.,z/w)) if w > 0 else np.pi/2
    return 2 / pi * integral(g, 0., 50.)

def limit(z):
    return 2/pi*integral(lambda t: kv(0,t),0.,z,points=[0.,z])

def coeff(z):
    return -(z*z*kv(1,z)+z**3*kv(0,z))/(12*pi)

# Exact equality among independent Bessel-series, flux integral, and renewal coupling.
for a in (1,2,3,4,7):
    for z in (0.4,0.9,1.8,3.3):
        direct = eigen_direct(a,z)
        coupling = eigen_coupling(a,z)
        check(abs(direct-coupling)<6e-8, f'Bessel/renewal mismatch a={a}, z={z}: {direct}, {coupling}')

# Identity M'_a=-2a J_a^2/x, verified by finite differencing, not relied on as proof.
for a in (1,2,3,5,7):
    def M(x):
        return jv(0,x)**2+2*sum(jv(j,x)**2 for j in range(1,a))+jv(a,x)**2
    for x in (0.2,0.5,1.,2.,3.,5.):
        h=1e-5
        fd=(M(x+h)-M(x-h))/(2*h)
        check(abs(fd+2*a*jv(a,x)**2/x)<2e-9, f'flux identity a={a}, x={x}')

# At fixed scaled rate z the sign memory is strictly increasing with distance.
for z in (0.2,0.6,1.,2.,5.):
    values=[eigen_coupling(a,z) for a in (1,2,4,8,16,40)]
    check(all(values[j]<values[j+1] for j in range(len(values)-1)), f'nonmonotonic {z}: {values}')
    check(values[-1]<limit(z),f'failed upper limiting bound {z}')

# Predicted sharp coefficient, tested without mistaking finite tests for a proof.
for z in (0.3,1.,2.,4.):
    for a in (15,30,60):
        q=eigen_coupling(a,z)
        check(abs((q-limit(z))*a*a-coeff(z))<0.05/(a*a)+0.003, f'coefficient mismatch {z} {a}')

# Zero-distance and large-distance normalization of limiting crossover.
for z in (0.2,0.5,1.,2.,4.,8.):
    check(0<limit(z)<1, f'limit outside unit interval: {z}')

# Large reset frequency (quantum Zeno) asymptotics at fixed site distance.
for a in (1,2,3):
    eps=80.
    predicted=(factorial(2*a)/(4**a*factorial(a)**2))*eps**(-2*a)
    measured=1-(1-2*flip(a,eps))
    check(abs(measured-predicted)/predicted < 0.09, f'Zeno asymptotic {a}: {measured}/{predicted}')

print(f'PASS: {N} numerical assertions')
