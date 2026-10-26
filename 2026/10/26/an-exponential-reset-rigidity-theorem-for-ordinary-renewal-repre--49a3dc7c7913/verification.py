"""Finite checks of resetting/waiting-transform and marginal laws.

This is a reproducible numerical diagnostic, not a substitute for the proof.
Requires Python 3, NumPy, and SciPy. Run: python verification.py
"""
import math
import numpy as np
from scipy.linalg import expm

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def F_exponential(s, r):
    return 1.0 / (s + r)

def F_deterministic(s, a):
    return -math.expm1(-a * s) / s

# Exactly the two analytically different Laplace-count formulas.
for lam in (0.25, 1.3, 4.0):
    for r in (0.0, 0.3, 2.8):
        for s in (0.2, 0.8, 2.5):
            F0 = F_exponential(s, r)
            w = lam / (s + lam + r)
            check(abs(1 - F_exponential(s+lam, r)/F0 - w) < 5e-15, 'unique waiting transform')
            for z in (0., 0.23, 0.5, 0.9, 1.):
                reset = F_exponential(s + lam * (1-z), r) / (s * F0)
                renewal = (1-w) / (s * (1-z*w))
                check(abs(reset-renewal) < 1e-13, 'exponential-reset renewal identity')

# For deterministic reset a single waiting transform cannot work at two z values.
for a in (0.8, 1.7, 3.1):
    for lam in (0.5, 1.3, 3.0):
        for s in (0.3, 0.8, 2.0):
            F0 = F_deterministic(s,a)
            w = 1 - F_deterministic(s+lam, a)/F0
            predicted = (1-w)/(1-0.5*w)
            actual = F_deterministic(s+0.5*lam,a)/F0
            check(abs(actual-predicted)>1e-6, 'deterministic reset obstructs ordinary renewal')

# Independent finite-dimensional master-equation constructions: the reset walk
# has a spatial generator on 2M+1 states, whereas the stopped walk has
# alive/dead states (the latter permanently freezes after its first kill).
M = 20
L = 2*M+1
xs = np.arange(-M,M+1)
zero = M
for lam,r,t1,t2 in ((0.75,0.4,0.9,1.5),(1.3,1.2,0.5,1.7),(2.5,0.8,1.2,2.0)):
    Q = np.zeros((L,L))
    R = np.zeros((2*L,2*L))
    for i in range(L):
        for step in (-1,1):
            j = i+step
            if 0 <= j < L:
                Q[j,i] += lam/2
                R[j,i] += lam/2
        # Probability escaping a finite interval: killing at its boundary.
        Q[i,i] -= lam
        R[i,i] -= lam+r
        Q[zero,i] += r
        Q[i,i] -= r
        R[i+L,i] += r
    check(np.linalg.norm(Q.sum(axis=0))<lam, 'bounded spatial generator')
    init = np.zeros(L); init[zero] = 1
    init2 = np.zeros(2*L); init2[zero] = 1
    eY1 = expm(Q*t1)@init
    eZ1 = expm(R*t1)@init2
    eY2 = expm(Q*t2)@init
    eZ2 = expm(R*t2)@init2
    marginal_Z1 = eZ1[:L]+eZ1[L:]
    marginal_Z2 = eZ2[:L]+eZ2[L:]
    check(max(abs(eY1-marginal_Z1))<2e-9, 'spatial marginals at t1')
    check(max(abs(eY2-marginal_Z2))<2e-9, 'spatial marginals at t2')
    # Two-time covariance using conditional position at t2 given position at t1.
    predY=xs@(expm(Q*(t2-t1)))
    eYcross=(xs*eY1)@predY
    predZ=(np.concatenate([xs,xs]))@(expm(R*(t2-t1)))
    eZcross=(np.concatenate([xs,xs])*eZ1)@predZ
    expectY=(lam/r)*(1-math.exp(-r*t1))*math.exp(-r*(t2-t1))
    expectZ=(lam/r)*(1-math.exp(-r*t1))
    check(abs(eYcross-expectY)<3e-8, 'reset two-time covariance')
    check(abs(eZcross-expectZ)<3e-8, 'stopped two-time covariance')
    check(eYcross<eZcross, 'trajectory law distinct')

print(f'PASS {checks} numerical cross-checks; analytic proof required for all-time results')
