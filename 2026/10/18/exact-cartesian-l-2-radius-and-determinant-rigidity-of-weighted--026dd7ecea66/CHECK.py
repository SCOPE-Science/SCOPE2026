#!/usr/bin/env python3
"""Independent finite diagnostics for the three-cycle averaged Cartesian radius.
Requires numpy and scipy; finite numerical evidence does not replace the proof.
"""
import cmath
import math
import numpy as np
from scipy.integrate import quad

def exact_squared(weights):
    a, b, c = weights
    s = sum(abs(w)**2 for w in weights)
    if not s:
        return 0.0
    eta = 3 * math.sqrt(3) * abs(a*b*c) / s**1.5
    eta = min(1.0, eta)  # floating-point roundoff at equality
    f = lambda t: math.cos(math.acos(min(1.0, eta*math.cos(t)))/3)**2
    return 2*s/(3*math.pi)*quad(f, 0, math.pi/2, epsabs=2e-12)[0]

def original_angular_squared(weights, n=16384):
    a, b, c = weights
    M = np.array([[0,0,c],[a,0,0],[0,b,0]], dtype=complex)
    angles = 2*math.pi*np.arange(n)/n
    H = (np.exp(1j*angles)[:,None,None]*M + np.exp(-1j*angles)[:,None,None]*M.conj().T)/2
    eigen = np.linalg.eigvalsh(H)
    return float(np.mean(np.max(np.abs(eigen), axis=1)**2))

sets = [(1,0,1),(1,1,1),(2,1,0.5),(1+2j,3-4j,-1j),(0,0,2),(1,1j,-1j)]
for weights in sets:
    x = exact_squared(weights)
    y = original_angular_squared(weights)
    assert abs(x-y) < 2e-6 * max(1.0,x), (weights,x,y)
    a,b,c = weights
    M = np.array([[0,0,c],[a,0,0],[0,b,0]], dtype=complex)
    s = sum(abs(w)**2 for w in weights)
    for theta in [0.0,0.13,0.73,1.71]:
        H = (cmath.exp(1j*theta)*M + cmath.exp(-1j*theta)*M.conj().T)/2
        coefficients = np.poly(H)
        expected = [1,0,-s/4, -float((cmath.exp(3j*theta)*a*b*c).real)/4]
        assert np.allclose(coefficients,expected,atol=2e-12), (weights,theta,coefficients)
print('PASS: 6 independent eigenvalue/angular-integral comparisons, 24 characteristic polynomials')
print('Upper squared constant',1/6+math.sqrt(3)/(4*math.pi))
