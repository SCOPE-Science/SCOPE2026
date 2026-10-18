#!/usr/bin/env python3
"""Numerical sanity checks for circular-annulus Fourier dark-ring branches.

Requirements: Python 3, NumPy, SciPy. The mathematical proof is analytic;
these finite-precision checks are deliberately not offered as a proof.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import j0, j1, jn_zeros

MAX_N = 12
js0 = jn_zeros(0, MAX_N + 1)
js1 = jn_zeros(1, MAX_N)
q_samples = (0.01, 0.04, 0.17, 0.39, 0.72, 0.94, 0.995)

def root(n, q):
    lo, hi = js0[n-1], js0[n]
    return brentq(lambda x: j1(x)-q*j1(q*x), lo, hi, xtol=1e-13)

# Each root is in the predicted J_0 gap and has strict positive branch y'(q).
for n in range(1, MAX_N + 1):
    samples = [root(n, q) for q in q_samples]
    for q, x in zip(q_samples, samples):
        assert js0[n-1] < x < js0[n]
        assert abs(j1(x)-q*j1(q*x)) < 8e-13
        gx = j0(x)-q*q*j0(q*x)
        yp = x*j0(x)/gx
        assert yp > 0.0, (n, q, yp)
    assert all(q_samples[i]*samples[i] < q_samples[i+1]*samples[i+1]
               for i in range(len(q_samples)-1))

# Every root branch has exactly n-1 predicted stationary points,
# with no extras according to the analytic monotonicity proof.
checks = 0
for n in range(2, MAX_N + 1):
    lo, hi = js0[n-1], js0[n]
    cp = []
    for m in range(1, n):
        target = js0[m-1]*j1(js0[m-1])
        X = brentq(lambda x: x*j1(x)-target, lo, hi, xtol=1e-12)
        q = js0[m-1]/X
        assert 0.0 < q < 1.0
        assert abs(j1(X)-q*j1(q*X)) < 3e-12
        assert abs(j0(q*X)) < 3e-12
        second = -q*X*X*j1(js0[m-1])/j0(X)
        assert np.sign(second) == (-1)**(m+n)
        assert abs(second)>1e-6
        cp.append(q)
        checks += 1
    assert all(cp[i]<cp[i+1] for i in range(len(cp)-1))

# Thin-ring and filled-disk endpoints: uniform sampling convergence.
for n in range(1, MAX_N + 1):
    assert abs(root(n, 1e-4)-js1[n-1]) < 2e-5
    assert abs(root(n, 1-1e-5)-js0[n-1]) < 3e-4

print(f'PASS: {MAX_N*len(q_samples)} sample Fourier zeros in J0 gaps;')
print(f'      {checks} predicted nondegenerate critical points checked;')
print(f'      {2*MAX_N} endpoint convergence checks; no analytic claims from enumeration.')
