#!/usr/bin/env python3
"""Reproduce the exact local distance law and its first break for orthotopes."""
from itertools import combinations
from math import gamma, pi, prod, sqrt
from scipy.integrate import quad
import numpy as np

def elementary(v, k):
    return sum(prod(x) for x in combinations(v, k))

def coefficients(lengths):
    d = len(lengths)
    v = [1/a for a in lengths]
    V = prod(lengths)
    return [(-1)**k * elementary(v,k) * pi**((d-k)/2) /
            (V * gamma((d+k)/2+1)) for k in range(d+1)]

def invert_first_d(coeffs, d):
    V = pi**(d/2) / (gamma(d/2+1)*coeffs[0])
    e = [1.0]
    for k in range(1, d):
        e.append((-1)**k * coeffs[k] * V * gamma((d+k)/2+1) /
                 pi**((d-k)/2))
    e.append(1/V)
    poly = [(-1)**k * e[k] for k in range(d+1)]
    roots = np.roots(poly)
    assert max(abs(z.imag) for z in roots) < 1e-6
    return sorted(1/z.real for z in roots)

def local_polynomial(lengths, r):
    return sum(c * r**(len(lengths)+k) for k,c in enumerate(coefficients(lengths)))

def cdf_123(r):
    # Independent slicing computation, valid for r<2.
    def disk(R):
        return pi*R*R - 4/3*(1/2+1/3)*R**3 + R**4/12
    def integrand(x):
        return (1-x)*disk(sqrt(max(0,r*r-x*x)))
    return (2/6) * quad(integrand,0,min(r,1),epsabs=1e-13,epsrel=1e-13)[0]

for length in ((1.,2.,3.), (0.7, 1.3, 2.1, 4.), (0.6,1.1,1.9,2.7,4.3)):
    recovered=invert_first_d(coefficients(length),len(length))
    assert np.allclose(sorted(length),recovered,atol=1e-6,rtol=1e-6),(length,recovered)
print('ALL_DIMENSION_RECONSTRUCTION_CASES_PASSED')
for r in (0.20,0.50,0.90,0.99):
    assert abs(cdf_123(r)-local_polynomial((1.,2.,3.),r)) < 1e-10
print('INDEPENDENT_SLICING_POLYNOMIAL_PASSED')
V=6
amin=1
kappa2=pi
pred=8*kappa2*(2*amin)**1/(V*amin*4*6)
assert abs(pred-pi/9) < 1e-13
for h,tol in ((0.1,0.2),(0.04,0.12),(0.015,0.07)):
    ratio=(cdf_123(1+h)-local_polynomial((1.,2.,3.),1+h))/h**3
    print('h=',h,'observed=',ratio,'prediction=',pred)
    assert abs(ratio/pred-1)<tol
print('FIRST_BREAK_SINGULARITY_PASSED')
print('ALL_CHECKS_PASSED')
