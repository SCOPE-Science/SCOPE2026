"""Reproducibility checks for nested-circle random-chord crossing probabilities.
Requires Python 3, NumPy and SciPy. Run: python check.py
"""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi

def p_integral(radius):
    if radius < 1:
        raise ValueError('radius must be at least one')
    alpha = math.asin(1.0 / radius)
    integrand = lambda t: math.asin(min(1.0, radius * math.sin(t))) ** 2
    value, error = quad(integrand, 0.0, alpha, epsabs=2e-13, epsrel=2e-13, limit=250)
    assert error < 2e-9
    return alpha / PI - 4.0 * value / PI**3

def p_second_integral(radius):
    def g(x):
        return 0.5 - 2.0 * math.asin(x)**2 / PI**2
    # Angle coordinate eliminates the arcsine-endpoint singularity when radius=1.
    return 2.0 / PI * quad(
        lambda angle: g(math.sin(angle)) * math.cos(angle)
        / math.sqrt(max(1e-300, radius*radius-math.sin(angle)**2)),
        0.0, PI / 2.0, epsabs=2e-12, epsrel=2e-12, limit=200
    )[0]

def coefficient(k):
    b = math.comb(2 * k, k) / (4.0**k)
    j = 2.0 * quad(lambda x: (0.5-2.0*math.asin(x)**2/PI**2)
                   * x**(2*k), 0.0, 1.0,
                   epsabs=1e-13, limit=250)[0]
    return b * j / PI

for k, exact in [(0, 8/PI**3), (1, 28/(27*PI**3)),
                 (2, 149/(375*PI**3))]:
    observed = coefficient(k)
    assert abs(observed-exact) < 2e-11, (k, observed, exact)
print('INDEPENDENT_COEFFICIENT_INTEGRALS_PASSED')

assert abs(p_integral(1.0)-1/3) < 1e-12
for radius in [1.0, 1.0001, 1.001, 1.02, 1.5, 2.0, 4.0, 12.0]:
    a, b = p_integral(radius), p_second_integral(radius)
    assert abs(a-b) < 4e-10, (radius, a, b)
    lower, upper = 8/(PI**3*radius), 1/(3*radius)
    assert lower -1e-12 < a < upper +1e-12
print('TWO_INDEPENDENT_QUADRATURES_AND_SHARP_GLOBAL_BOUNDS_PASSED')

radii = [1.0, 1.0002, 1.003, 1.05, 1.2, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0]
values = [p_integral(r) for r in radii]
assert all(values[i] > values[i+1] for i in range(len(values)-1))
assert all(radii[i]*values[i] > radii[i+1]*values[i+1]
           for i in range(len(values)-1))
for r in [1.3, 1.7, 2.0, 3.0, 10.0]:
    partial = sum(coefficient(k) / (r**(2*k+1)) for k in range(3))
    remainder_bound = (1/3 - sum(coefficient(k) for k in range(3))) / r**7
    assert partial < p_integral(r) < partial+remainder_bound+2e-12
print('POSITIVE_POWER_SERIES_REMAINDER_AND_ORDER_DIAGNOSTICS_PASSED')

for eps in [1e-3, 1e-4, 1e-5, 1e-6]:
    ratio = (1/3-p_integral(1+eps))/(eps*math.log(1/eps))
    assert abs(ratio-2/PI**2) < 0.018, (eps, ratio)
for r in [20, 40, 100]:
    pred = 8/(PI**3*r)+28/(27*PI**3*r**3)
    assert abs(p_integral(r)-pred) < 0.014/r**5
print('SHARP_LOGARITHMIC_CUSP_AND_FAR_FIELD_COEFFICIENTS_PASSED')

# Independent direct segment intersections, using oriented areas and no line-offset law.
rng = np.random.default_rng(724103)
n = 100_000
angles = rng.uniform(0, 2 * PI, size=(n,4))
points = np.stack([np.cos(angles), np.sin(angles)], axis=2)
def cross(a,b): return a[:,0]*b[:,1]-a[:,1]*b[:,0]
for r in [1.0, 1.05, 1.2, 2.0, 5.0, 10.0]:
    p = points.copy()
    p[:,2:,:] *= r
    a,b,c,d = [p[:,k,:] for k in range(4)]
    c1,c2=cross(b-a,c-a),cross(b-a,d-a)
    d1,d2=cross(d-c,a-c),cross(d-c,b-c)
    observed = np.mean((c1*c2<0)&(d1*d2<0))
    exact=p_integral(r)
    se=math.sqrt(exact*(1-exact)/n)
    assert abs(observed-exact) < 5.0*se, (r, observed,exact,se)
print('INDEPENDENT_DIRECT_FOUR_ENDPOINT_SEGMENT_SIMULATIONS_PASSED 6x100000')
print('ALL_CHECKS_PASSED')
