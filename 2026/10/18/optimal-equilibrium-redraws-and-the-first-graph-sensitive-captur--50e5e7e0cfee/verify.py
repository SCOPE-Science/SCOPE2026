"""Independent finite-matrix checks of stationary-redraw capture formulas.

Dependencies: numpy, scipy, sympy. Run: python verify.py
"""
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.linalg import expm

checks = 0

def verify(W, weights, killing):
    global checks
    n = len(weights)
    p = np.array(weights, dtype=float)
    p /= np.sum(p)
    Q = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                Q[i, j] = W[i][j] / p[i]
    np.fill_diagonal(Q, -np.sum(Q, axis=1))
    K = np.diag(np.array(killing, dtype=float))
    H = -Q + K
    one = np.ones(n)
    mu = float(p @ killing)
    variance = float(p @ ((killing-mu)**2))
    skew = float(p @ ((killing-mu)**3))
    energy = float(np.dot(p*killing, -Q @ killing))
    moments = [float(np.dot(p, np.linalg.matrix_power(H, m) @ one)) for m in range(1, 4)]
    assert np.allclose(moments, [mu,mu*mu+variance,
                                  mu**3+3*mu*variance+skew+energy], atol=1e-8)
    checks += 1
    sqrtp = np.sqrt(p)
    Hsym = (sqrtp[:,None]*H)/sqrtp[None,:]
    eig, vec = np.linalg.eigh(Hsym)
    assert eig.min() > 0
    a = vec.T @ sqrtp
    assert np.isclose(np.dot(a, a), 1.0)
    checks += 2
    for t in [0.05, 0.14, 0.5, 0.9]:
        def s(u):
            direct = np.dot(p, expm(-u*H) @ one)
            spectral = np.sum(a*a*np.exp(-eig*u))
            assert abs(direct-spectral) < 1e-12
            return direct
        assert s(t/2)**2 < s(t)
        assert s(t/3)**3 < s(t/2)**2
        assert s(t/3)**3 < s(.2*t)*s(.3*t)*s(.5*t)
        checks += 4
    # Independent Taylor coefficients from the generator powers and spectrum.
    for t in [0.1, 0.3]:
        for q in [32,64,128,256]:
            f = q*np.log(s(t/q))
            taylor = -mu*t+variance*t*t/(2*q)-(skew+energy)*t**3/(6*q*q)
            assert abs(f-taylor) < .005*t**4/q**3 * max(1.,float(np.linalg.norm(H,ord=2)**4)), (f,taylor)
            checks += 1
    return mu,variance,skew,energy

for r in [0.5,1.,2.]:
    # Stationary distribution uniform; nearest-neighbor symmetric weighted path.
    W = np.array([[0.,r,0.],[r,0.,r],[0.,r,0.]])/3
    moments = verify(W, np.array([1,1,1]),np.array([0.,2.,4.]))
    assert np.allclose(moments, [2.,8./3,0.,8*r/3])
    checks += 1

# Nonuniform equilibrium weights with conductances independent of the weights.
W = np.array([[0.,.4,.2],[.4,0.,.3],[.2,.3,0.]])
verify(W,np.array([1.,2.,5.]),np.array([0.2,1.3,4.5]))
print('All', checks, 'finite-matrix, spectral and asymptotic checks passed.')
