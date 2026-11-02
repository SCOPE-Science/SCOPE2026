#!/usr/bin/env python3
"""Reproducibility checks for a weak-bond finite-path Markov semigroup theorem.
Scientific finite checks, not a proof for all path lengths/parameters.
Requires numpy and scipy. Usage: python check_slow_path.py
"""
import math
import numpy as np
from scipy.linalg import eigh, expm
from scipy.optimize import minimize_scalar

count = 0

def assert_close(a, b, *, atol=2e-9, rtol=2e-9):
    global count
    if not np.isclose(a, b, atol=atol, rtol=rtol):
        raise AssertionError(f"not close: {a} versus {b}")
    count += 1

def generator(m, eps):
    n = 2*m
    w = np.ones(n-1)
    w[m-1] = eps
    Q = np.zeros((n, n))
    for j, rate in enumerate(w):
        Q[j, j+1] = rate
        Q[j+1, j] = rate
        Q[j, j] -= rate
        Q[j+1, j+1] -= rate
    return Q

def half_operator(m, eps):
    R = np.diag([-1.-2.*eps] + [-2.]*(m-2) + [-1.])
    R += np.diag(np.ones(m-1), 1) + np.diag(np.ones(m-1), -1)
    return R

def w1_line(p,q):
    return np.sum(np.abs(np.cumsum(p-q)[:-1]))

def peak_from_spectrum(m,eps):
    vals, vecs = eigh(-half_operator(m, eps))
    z = np.arange(m) + .5
    coe = 2*vecs[0,:]*(vecs.T @ z)
    def center(t):
        return float(np.dot(coe, np.exp(-vals*t)))
    lam = 4*math.sin(math.pi/(2*m))**2
    cap = max(20., 8*math.log(1/eps)/lam)
    opt = minimize_scalar(lambda t: -center(t), method='bounded',
                          bounds=(0.,cap),options={'xatol':1e-8})
    return opt.x, center(opt.x)

# (1) Independently compare the vertex heat kernel with the reduced half-size
# matrix, stochastic-order transport, and the full Lipschitz operator norm.
for m in range(2,9):
    for eps in (0.015, 0.17, 0.55, 0.9):
        Q=generator(m,eps)
        R=half_operator(m,eps)
        for t in (0., 0.15, 0.6, 1.5, 4., 12.):
            P=expm(t*Q)
            center=2*(expm(t*R)@(np.arange(m)+.5))[0]
            w1adj=[]
            for j in range(2*m-1):
                w1adj.append(w1_line(P[j],P[j+1]))
                assert_close(w1adj[-1],
                             float(P[j+1]@np.arange(2*m)-P[j]@np.arange(2*m)))
            assert_close(center,w1adj[m-1])
            # Free-standing test of the operator-norm formula by all adjacency pairs.
            grad=np.diff(P@np.arange(2*m))
            assert_close(max(w1adj),max(grad))
            # For the checked grid, the weak edge attains the maximum.
            assert_close(max(w1adj),center)
            assert_close(float(P.sum(axis=1).min()),1.)

# (2) Independently compare the closed Neumann Fourier formula at eps=0.
for m in range(2,12):
    for t in (0.,.15,.75,2.,7.):
        direct=2*(expm(t*half_operator(m,0.))@(np.arange(m)+.5))[0]
        fourier=m-sum((2./m)/math.tan(math.pi*k/(2*m))**2
                      *math.exp(-4*math.sin(math.pi*k/(2*m))**2*t)
                      for k in range(1,m,2))
        assert_close(direct,fourier)

# (3) Test first- and second-order peak asymptotics; these are finite checks.
for m in range(2,10):
    angle=math.pi/(2*m)
    lam=4*math.sin(angle)**2
    K=4*math.cos(angle)**2/m
    B=2./m/(math.tan(angle)**2)
    assert_close(B*lam/2,K)
    for eps in (1e-4,1e-6):
        t,peak=peak_from_spectrum(m,eps)
        prediction_t=math.log(K/eps)/lam
        prediction_height=m-eps*(2/lam*math.log(1/eps)
                                   +(m-1)**2/2
                                   +2/lam*(1+math.log(K)))
        # Rescaled error converges to zero with eps. Tolerances are deliberately
        # coarser for moderate epsilon and larger path lengths.
        if abs(t-prediction_t)>0.05:
            raise AssertionError((m,eps,t,prediction_t))
        count+=1
        if abs(peak-prediction_height)>0.35*m*m*eps:
            raise AssertionError((m,eps,peak,prediction_height))
        count+=1
        if not 1 < peak < m:
            raise AssertionError('expected transient amplification')
        count+=1

print('PASS:',count,'finite comparisons / assertions; no infinite-family certification')
