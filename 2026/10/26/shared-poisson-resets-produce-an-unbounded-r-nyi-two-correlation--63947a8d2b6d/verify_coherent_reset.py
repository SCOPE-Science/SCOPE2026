#!/usr/bin/env python3
"""Independent numerical checks for synchronized-reset quantum-walk purity.

Requires numpy and scipy.  All physical rates and hopping amplitudes are positive.
The analytic infinite-lattice and small-rate assertions are established separately
in the accompanying proof; finite numerical tests are consistency checks.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk, j0, jv, roots_laguerre

checks = 0

def close(x, y, *, atol=2e-9, rtol=2e-9):
    global checks
    assert np.isfinite(x) and np.isfinite(y)
    assert abs(x-y) <= atol + rtol*max(abs(x),abs(y)), (x,y)
    checks += 1

def purity(d, rate, hopping):
    assert d >= 1 and rate > 0 and hopping > 0
    return rate * quad(lambda u: math.exp(-rate*u)*j0(2*hopping*u)**(2*d),
                       0., np.inf, epsabs=1e-11, epsrel=1e-11,
                       limit=2000)[0]

def elliptic_p1(rate, hopping):
    z = math.hypot(rate, 4*hopping)
    return 2*rate*ellipk((4*hopping/z)**2)/(math.pi*z)

# Classical Bessel addition identity, independently tested via finite Fourier sums.
for x in (0.2, 0.7, 1.3, 4.8):
    for theta in (-2.0, -0.7, 0., 0.8, 2.2):
        lhs = sum(jv(n,x)**2*complex(math.cos(n*theta),math.sin(n*theta))
                  for n in range(-55, 56))
        close(lhs.real, j0(2*x*math.sin(theta/2)), atol=3e-13)
        close(lhs.imag, 0., atol=3e-13)

# The density-matrix purity from the independent age-mixture calculation.
# (Two-particle density matrix is constructed in the product basis in Gram form.)
for rate, hopping in ((1.5, .8), (2., 1.25), (3.2, .7)):
    grid, weights = roots_laguerre(95)
    ages = grid/rate
    basis = np.arange(-85,86)
    phases = (1j)**basis
    psi = (jv(basis[:,None], 2*hopping*ages[None,:])
           *phases[:,None])
    overlaps = psi.conj().T @ psi
    close(float(np.sum(weights * np.sum(abs(psi)**2,axis=0))), 1., atol=2e-11)
    rho1 = (psi * weights[None,:]) @ psi.conj().T
    direct1 = np.real(np.trace(rho1 @ rho1))
    gram1 = float(np.sum((weights[:,None]*weights[None,:])*abs(overlaps)**2))
    gram2 = float(np.sum((weights[:,None]*weights[None,:])*abs(overlaps)**4))
    close(direct1, gram1)
    close(direct1, purity(1,rate,hopping), atol=6e-8)
    close(gram2, purity(2,rate,hopping), atol=6e-8)
    close(direct1,elliptic_p1(rate,hopping), atol=6e-8)
    assert gram2 > direct1**2
    checks += 1

# Independent direct double-age quadrature, without the renewal convolution reduction.
for rate,hopping in ((1.2,1.),(3.,0.7)):
    for d in (1,2):
        def outer(s):
            return rate**2*math.exp(-rate*s)*quad(
                lambda t: math.exp(-rate*t)*j0(2*hopping*(s-t))**(2*d),
                0., 20./rate,epsabs=2e-9,limit=400)[0]
        p = quad(outer, 0, 20./rate, epsabs=2e-8, limit=120)[0]
        close(p, purity(d,rate,hopping),atol=8e-8)

# General weak-reset regime and normalized two-body purity ratio.
# C is an absolutely convergent Bessel fourth-power integral.
C_partial = quad(lambda x: j0(x)**4, 0., 10000.,
                 epsabs=2e-8, limit=18000)[0]
C_est = C_partial + 3/(2*math.pi**2*10000)
close(C_est,0.9027286,atol=6e-7)
for rate in (0.3,0.1,0.03,0.01,0.003):
    hopping = 1.
    p1 = elliptic_p1(rate,hopping)
    p2 = purity(2,rate,hopping)
    ratio = p2/p1**2
    assert ratio > 1.
    checks += 1
    r_asym = 2*math.pi**2*hopping*C_est / (
        rate * math.log(16*hopping/rate)**2)
    if rate <= 0.03:
        assert abs(ratio/r_asym-1) < 0.06
        checks += 1

print(f"PASS: {checks} deterministic checks; C≈{C_est:.9f}")
