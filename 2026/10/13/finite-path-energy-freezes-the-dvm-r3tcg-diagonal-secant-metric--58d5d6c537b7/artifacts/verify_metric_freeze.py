from fractions import Fraction as F
import math

# Exact recurrence on constant-curvature secants.
q = F(3, 2)
omega = F(1, 1)
mL = F(1, 2)
mU = F(2, 1)
u = F(1, 1)
prod = F(1, 1)
steps = [F(1, 2**(k+1)) for k in range(12)]
for s in steps:
    y = q*s
    utilde = (s*y + omega*u)/(s*s + omega)
    assert mL <= utilde <= mU
    u = utilde
    prod *= omega/(s*s+omega)
    assert u-q == (F(1,1)-q)*prod

# A globally Q-linear trajectory and its exact energy bound.
r = F(1, 2)
e0 = F(1, 4)
errors = [e0 * r**k for k in range(30)]
ss = [errors[k+1]-errors[k] for k in range(len(errors)-1)]
energy_partial = sum((s*s for s in ss), F(0,1))
energy_exact = (1-r)**2 * e0**2 / (1-r**2)
assert energy_partial < energy_exact
coarse_bound = (1+r)/(1-r) * e0**2
assert energy_exact <= coarse_bound

# Numerical limiting bias is positive and exceeds the theorem's exponential floor.
u = F(1,1)
for s in ss:
    u = (q*s*s + omega*u)/(s*s+omega)
actual_bias = abs(float(u-q))
lower = abs(1.0-float(q))*math.exp(-float(coarse_bound/omega))
assert actual_bias > lower > 0.0

# Divergent excitation drives the product downward: finite check only.
p = 1.0
for k in range(1, 20000):
    s2 = 1.0/k
    p /= (1.0+s2)
assert p < 1e-3

print('VERIFY_OK')
