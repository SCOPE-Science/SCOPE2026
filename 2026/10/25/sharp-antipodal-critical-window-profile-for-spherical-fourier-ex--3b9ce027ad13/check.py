"""Numerical and algebraic checks for the spherical critical-window theorem.

Requires numpy and scipy. Finite tests do not certify the infinite-dimensional limit.
"""
import math
import numpy as np
from scipy.integrate import simpson
from scipy.special import jv, gamma


def mean_power(p, a, b, samples=20000):
    phase = (np.arange(samples) + 0.5) * (2 * math.pi / samples)
    return float(np.mean((a + b*np.cos(phase))**p))


def shell(d, weights, r0, width, lam):
    p = d/(d-1)
    nu = d/2 - 1
    log_r = math.log(r0)
    q_over_two = p + lam/(2*log_r)
    r = np.arange(r0, r0*math.exp(width), 0.035)
    coeff = (2*math.pi)**d * r**(-2*nu)
    power = sum(a*jv(nu+k, r)**2 for k,a in enumerate(weights))
    integral = simpson((coeff*power)**q_over_two * r**(d-1), x=r)
    b = sum((-1)**k*a for k,a in enumerate(weights))
    a = sum(weights)
    C = ((2*math.pi)**d/math.pi)**p
    h = mean_power(q_over_two, a, b)
    C *= ((2*math.pi)**d/math.pi)**(q_over_two-p)
    z = (d-1)*lam/(2*log_r)
    exact_weight = -math.expm1(-z*width)/z if z != 0 else width
    return integral/(C*h*exact_weight*math.exp(-z*log_r))


for d in (2,3,4):
    p = d/(d-1)
    m = 2**p * gamma(p+0.5) / (math.sqrt(math.pi)*gamma(p+1))
    assert abs(mean_power(p,1,1)-m) < 2e-10
    assert abs(mean_power(p,1,0)-1) < 1e-12
    for b in (0,0.2,0.6,0.9,1):
        val = mean_power(p,1,b)
        lower = 1 + (m-1)*b*b
        assert val <= lower + 3e-10, ('convexity sign',d,b,val,lower)
        assert m - val + 3e-10 >= (m-1)*(1-b*b)
    for lam in (-1.,0.,1.):
        ratio = shell(d, [0.8,0.2], 1100., 0.8, lam)
        assert abs(ratio - 1) < 0.006, (d,lam,ratio)

print('CHECK_OK: Bessel shell convergence (3 dimensions x 3 exponents), gamma identity and sharp parity-deficit inequalities')
