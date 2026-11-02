#!/usr/bin/env python3
"""Checks for weak-flux first-detection asymptotics on a three-site ring.

Python 3.10+ with NumPy and SciPy. This is a consistency checker,
not a substitute for the analytic perturbation proof.
"""
import cmath
import math
import numpy as np
from scipy.linalg import expm, solve_discrete_lyapunov


def survivor(t, alpha):
    u = cmath.exp(2j * t * math.cos(alpha))
    w = cmath.exp(-1j * t * math.cos(alpha))
    b = math.sqrt(3) * t * math.sin(alpha)
    return np.array([[(2*u+w*math.cos(b))/3, w*math.sin(b)/math.sqrt(3)],
                     [-w*math.sin(b)/math.sqrt(3), w*math.cos(b)]], dtype=complex)


def direct(t, alpha):
    h = np.zeros((3, 3), dtype=complex)
    for j, k in ((0, 1), (1, 2), (2, 0)):
        h[j, k] = -np.exp(1j*alpha)
        h[k, j] = -np.exp(-1j*alpha)
    U = expm(-1j*t*h)
    s = np.array([0, 1, 1], dtype=complex)/math.sqrt(2)
    d = np.array([0, 1, -1], dtype=complex)/math.sqrt(2)
    B = np.column_stack((s,d))
    return B.conj().T@U@B


def mean_attempts(t, alpha):
    K = survivor(t, alpha)
    # The Hermitian discrete Lyapunov identity M-K^* M K=I.
    # Solve it in transposed form using solve_discrete_lyapunov.
    M = solve_discrete_lyapunov(K.conj().T, np.eye(2, dtype=complex))
    assert np.linalg.norm(M-K.conj().T@M@K-np.eye(2)) < 1e-6
    return float(M[1, 1].real)


def survival(t, alpha, x):
    n = int(x/(alpha*alpha))
    d = np.array([0, 1], dtype=complex)
    z = np.linalg.matrix_power(survivor(t, alpha), n)@d
    return float(np.vdot(z, z).real)


def run_checks():
    nchecks = 0
    for t in (0.6, 1.0, 2*math.pi/3, 4*math.pi/3, 3.2):
        for alpha in (-0.21, -0.03, 0.0, 0.04, 0.27):
            err = np.max(np.abs(survivor(t,alpha)-direct(t,alpha)))
            assert err < 5e-14, (t,alpha,err)
            nchecks += 1
    for t, rate in ((1.0, 4.5), (0.7, 4.5*0.7**2),
                    (2*math.pi/3, (2*math.pi/3)**2),
                    (4*math.pi/3, (4*math.pi/3)**2)):
        for a in (.02,.01,.005):
            scaled = a*a*mean_attempts(t,a)
            predicted = 1/rate
            assert abs(scaled-predicted)/predicted < (0.04 if a == .02 else 0.015), (t,a,scaled,predicted)
            nchecks += 1
        for x in (.3,1.0):
            actual = survival(t,.008,x)
            target = math.exp(-rate*x)
            assert abs(actual-target) < .007, (t,x,actual,target)
            nchecks += 1
    for t in (1.0, 2*math.pi/3):
        for a in (.015,.008):
            vals = np.linalg.eigvals(survivor(t,a))
            decay = sorted([(1-abs(z)**2)/a**2 for z in vals])
            expected = t*t if abs(t-2*math.pi/3)<1e-9 else 4.5*t*t
            if expected==t*t:
                assert all(abs(v-expected) < .5 for v in decay), (t,a,decay)
            else:
                assert abs(decay[0]-expected)<.15, (t,a,decay)
            nchecks += 1
    print(f"PASS {nchecks} independent numerical/structural tests")
    for t in (1, 2*math.pi/3):
        for a in (.02,.01,.005):
            print(f"t={t:.12f} alpha={a:.3g} alpha^2 E[N]={a*a*mean_attempts(t,a):.12f}")


if __name__ == '__main__':
    run_checks()
