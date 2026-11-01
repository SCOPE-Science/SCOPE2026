#!/usr/bin/env python3
"""Finite reproducibility checks for the Bessel/Laguerre identities.

These tests corroborate finite calculations; the analytic proof establishes
injectivity and the sharp threshold for all ranks and all real exponents.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_laguerre, j0, roots_laguerre

checks = 0
for degree in range(1, 12):
    roots, _ = roots_laguerre(degree)
    assert len(roots) == degree
    assert np.all(roots > 0)
    assert np.all(np.diff(roots) > 0)
    for root in roots:
        assert abs(eval_laguerre(degree, root)) < 2e-7
        eps = 1e-5
        derivative = (eval_laguerre(degree, root+eps)-eval_laguerre(degree, root-eps))/(2*eps)
        assert abs(derivative) > 1e-6
        checks += 2

# The first invisible frequency is the unique zero of L_1(t) = 1-t.
assert abs(eval_laguerre(1, 1.0)) < 1e-14
checks += 1
for radius in [0.0, 0.25, 0.75, 1.0, 2.0, 3.0]:
    theta = np.linspace(0.0, 2*math.pi, 16384, endpoint=False)
    sample = np.exp(1j * 2 * radius * np.sin(theta)).mean()
    assert abs(sample.real - j0(2*radius)) < 3e-12
    assert abs(sample.imag) < 1e-12
    checks += 2

# The endpoint fourth-power annular mass has an explicit logarithmic slope.
def radial_fourth_mass(r0, r1):
    ans, err = quad(lambda r: 2*math.pi*r*j0(2*r)**4, r0, r1,
                    epsabs=5e-8, epsrel=5e-8, limit=2000)
    return ans
for r0, r1 in [(50, 250), (100, 500), (200, 1000)]:
    expected = 3/(4*math.pi)*math.log(r1/r0)
    observed = radial_fourth_mass(r0, r1)
    assert abs(observed-expected) < 0.009
    checks += 1

# A p>4 bound must decay faster than the p=4 critical tail.
for r in [10, 30, 100, 500, 1000]:
    assert abs(j0(2*r)) <= min(1.0, 1.2/math.sqrt(r))
    checks += 1
print(f"PASS: {checks} deterministic Laguerre, angular-identity, and Bessel-tail checks")
