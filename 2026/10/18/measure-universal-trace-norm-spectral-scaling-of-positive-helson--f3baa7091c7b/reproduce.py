#!/usr/bin/env python3
"""Supplementary finite-atomic diagnostics for the critical Helson spectral scaling.

Requires Python 3, numpy, scipy; tests do not certify an infinite-dimensional theorem.
"""
from math import sqrt, log, prod
import numpy as np
from scipy.special import zeta
GAMMA = 0.57721566490153286060651209008
EXAMPLES = [
    ([0.7, 1.6, 3.2], [2.0, 1.5, 0.5]),
    ([0.11, 2.8, 19.0], [1.0, 0.2, 0.9]),
]
for nodes, masses in EXAMPLES:
    a, w = np.array(nodes), np.array(masses)
    A = a[:, None] + a[None, :]
    W = np.sqrt(w[:, None] * w[None, :])
    I = float(np.sum(w / (2 * a)))
    M = float(np.sum(w))
    C = W / A
    eig0 = np.linalg.eigvalsh(C)[::-1]
    det_expected = prod(float(v) for v in w)
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            det_expected *= float((a[j] - a[i])**2)
    for i in range(len(a)):
        for j in range(len(a)):
            det_expected /= float(a[i]+a[j])
    assert abs(np.linalg.det(C) / det_expected-1) < 1e-9
    assert abs(sum(eig0)-I) < 1e-10
    errors = []
    for eps in (0.2, 0.1, 0.05, 0.02, 0.01):
        E = W * eps * zeta(1 + eps * A, 1)
        eig = np.linalg.eigvalsh(E)[::-1]
        gap = sum(abs(eig-eig0))
        bound = GAMMA*eps*M + sqrt((4*I+2*eps*log(2)*M)*(eps*log(2)*M))
        assert np.min(eig) > 0
        assert gap < bound + 1e-10
        errors.append(float(gap))
    assert all(errors[k] > errors[k+1] for k in range(len(errors)-1))
    eps = 0.001
    E = W * eps * zeta(1 + eps * A, 1)
    assert abs((np.trace(E)-I)/eps-GAMMA*M) < 0.03
print('FINITE_ATOMIC_DIAGNOSTICS_OK')
