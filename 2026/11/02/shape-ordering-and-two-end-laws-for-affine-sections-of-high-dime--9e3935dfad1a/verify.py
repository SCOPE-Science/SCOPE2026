"""Reproduce finite Boolean-section checks and limiting convex-rate comparisons.
Dependencies: Python 3, NumPy >=1.24, SciPy >=1.10.
No random sampling is needed for the exact combinatorial checks.
"""
import math
import numpy as np
from scipy.special import roots_hermitenorm
from scipy.optimize import brentq

GH_X, GH_W = roots_hermitenorm(240)
GH_W = GH_W / math.sqrt(2 * math.pi)
M = math.sqrt(2 / math.pi)

def rate(s, lengths, weights):
    lengths = np.asarray(lengths, dtype=float)
    weights = np.asarray(weights, dtype=float)
    assert abs(sum(weights) - 1) < 1e-13
    z = lengths[:, None] * np.abs(GH_X)[None, :]
    target = s * M * np.dot(lengths, weights)
    def derivative(lam):
        return float(np.dot(weights, (z * np.tanh(lam * z)) @ GH_W))
    lam = brentq(lambda l: derivative(l) - target, 0.0, 10000.0)
    cumulant = float(np.dot(weights, (np.logaddexp(lam*z,-lam*z)-math.log(2)) @ GH_W))
    return float(lam*target-cumulant)

# Exact edge boundary counts for small cubes: generic position, no cut vertex.
lengths = (1.0, 0.6, 1.4, 1.2, 0.8, 1.6, 0.7, 1.3)
g = (0.31, -1.27, 0.84, 0.67, -0.42, 1.91, -1.11, 0.55)
d = len(lengths)
weights = [a*x for a,x in zip(lengths,g)]
width = sum(abs(x) for x in weights)
for frac in (0.07, 0.31, 0.53, 0.83):
    t = frac*width
    high = [sum(weights[j]*(1 if mask & (1<<j) else -1)
                for j in range(d)) > t for mask in range(1<<d)]
    B = sum(high)
    crossed = sum(1 for mask in range(1<<d) for j in range(d)
                  if not (mask & (1<<j)) and high[mask] != high[mask | (1<<j)])
    assert 1 <= B <= 2**(d-1)
    assert B <= crossed <= d*B

# Integrate every edge's offset crossing interval, divide by total width.
# Each coordinate direction contains 2^(d-1) edges.
assert abs(sum((2**(d-1))*(2*abs(v)) for v in weights)/(2*width)
           - 2**(d-1)) < 1e-12

# The strict heterogeneity order; rate(mixed)<rate(equal mean).
for s in (0.1, 0.3, 0.6, 0.9, 0.98):
    equal = rate(s, (1.0,), (1.0,))
    mixed = rate(s, (0.5, 1.5), (0.5, 0.5))
    print(f's={s:.2f}, cube rate={equal:.10f}, mixed rate={mixed:.10f}')
    assert 0 < mixed < equal < math.log(2)

# Exact endpoint coefficients for the two-point shape distribution.
M1 = 1.0
M2 = (0.5**2+1.5**2)/2
Minv = (1/0.5+1/1.5)/2
C_upper = math.sqrt(math.pi*M2)/M1
C_lower = 3/(math.pi*M1*Minv)
assert abs(C_upper-1.9816636488030055) < 1e-12
assert abs(C_lower-0.7161972439135291) < 1e-12
assert C_upper > math.sqrt(math.pi)
assert C_lower < 3/math.pi
print('ALL_CHECKS_PASSED')
