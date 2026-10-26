#!/usr/bin/env python3
"""Reproduce beta/gamma and convolution-kernel checks for two diameter Bergman traces."""
import math
import scipy.integrate as integrate
from scipy.special import beta, gamma

for alpha in (-0.9, -0.5, 0.0, 1.0, 2.0, 10.0):
    lam=alpha+2
    C=(2**(lam-1))*gamma(lam/2)**2/gamma(lam)
    D=2*beta(0.5,lam)
    integral,_=integrate.quad(lambda t: 1/math.cosh(t)**lam, -25,25,epsabs=2e-10)
    assert abs(integral-C)<5e-8
    assert C<D<2*C
    print(f'alpha={alpha:.1f}: essential edge={C:.12f}; uniform Rayleigh bound={D:.12f}; gap={D-C:.12f}')
print('All finite numerical diagnostics passed; the spectrum and eigenvalue-count limit use the analytic proof.')
