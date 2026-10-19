"""Independent numerical tests for a two-point antithetic sampled proximal map.

The universal results are analytical; quadrature is a finite sanity check.
Run: python verify.py (requires NumPy and SciPy).
"""
import math
import numpy as np
from scipy.special import roots_hermitenorm
from scipy.optimize import brentq

nodes, weights = roots_hermitenorm(160)
weights = weights / math.sqrt(2 * math.pi)
checks = 0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

# Direct two-sample Gibbs weighting versus independently simplified tanh map.
for curvature in (0.15, 0.5, 2/3, 0.9, 2.1):
    for x in (-2., -.7, -.2, 0., .2, .7, 2.):
        for z in (-3., -1.5, -.2, .5, 2.7):
            a, delta = 1., 1.
            yp, ym = x + a*z, x - a*z
            up = math.exp(-curvature * yp * yp / (2*delta))
            um = math.exp(-curvature * ym * ym / (2*delta))
            direct = (yp*up + ym*um) / (up+um)
            closed = x - a*z*math.tanh(curvature*z*x/a)
            check(abs(direct - closed) <= 3e-14*(1+abs(x)), 'weighted estimator identity')

# Conditional second-moment exact quadrature vs sign of stability boundary.
for curvature in (0.1, 0.3, 0.5, 2/3):
    for u in (0.05, 0.1, 0.2, 0.5, 1., 2., 4., 8., 16.):
        nxt = u - nodes*np.tanh(curvature*nodes*u)
        mean_square = float(weights @ (nxt*nxt))
        check(mean_square < u*u - 1e-12, 'strict global mean-square descent')
for curvature in (0.7, 0.8, 1., 1.5, 2.):
    for u in (0.002, 0.005, 0.01, 0.02):
        nxt = u - nodes*np.tanh(curvature*nodes*u)
        mean_square = float(weights @ (nxt*nxt))
        check(mean_square > u*u + 1e-13, 'sharp local failure')

# Local Gaussian moment coefficient and quartic endpoint law.
for curvature in (0.1, 0.3, 0.5, 2/3, 0.7, 1., 1.5):
    m = float(weights @ ((1-curvature*nodes*nodes)**2))
    check(abs(m - (1-2*curvature+3*curvature*curvature))<1e-11,
          'exact Gaussian linear multiplier')
critical=2/3
for u in (0.0075, 0.01, 0.015, 0.025):
    nxt=u-nodes*np.tanh(critical*nodes*u)
    defect=(float(weights@(nxt*nxt))-u*u)/(u**4)
    check(abs(defect+112/81) < 0.007, 'critical quartic coefficient')

# Negative association inequality is tested on the same Gaussian quadrature grid.
for b in (0.05, 0.1, 0.2, 0.5, 1., 2., 5.):
    h = np.ones_like(nodes)
    mask=np.abs(nodes)>1e-15
    h[mask] = np.tanh(b*nodes[mask])/(b*nodes[mask])
    mu=float(weights@(nodes*nodes*h))
    bigger=float(weights@(nodes**4*h))
    check(bigger < 3*mu, 'negative covariance of tilted Gaussian moments')

# Frozen-draw map: global attraction below d=2; unique stable symmetric two-cycle above.
for d in (0.2, 0.8, 1.9, 2.):
    for v in (0.0002, 0.01, 0.1, 0.4, 1., 3., 10.):
        mapped = v - math.tanh(d*v)
        check(abs(mapped) < v, 'global frozen-draw attraction below threshold')
for d in (2.01, 2.1, 3., 4., 10., 30.):
    vstar = brentq(lambda v: math.tanh(d*v)-2*v, 1e-9, .5)
    g = lambda v: v - math.tanh(d*v)
    derivative=1-d/(math.cosh(d*vstar)**2)
    check(abs(g(vstar)+vstar)<2e-12, 'frozen-draw two-cycle')
    check(abs(derivative)<1, 'two-cycle local attraction')
    check(g(0)==0 and 1-d < -1, 'fixed-point instability')
print(f'PASS: {checks} deterministic quadrature, identity, and dynamical checks')
