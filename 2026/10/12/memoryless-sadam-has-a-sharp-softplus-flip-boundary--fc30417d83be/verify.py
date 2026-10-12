import math

LOG2 = math.log(2.0)

def L(u):
    if u > 700.0:
        return u
    return math.log1p(math.exp(u))

def step_scaled(z, a):
    u = abs(z)
    return z * (1.0 - a / L(u))

for a in (0.2*LOG2, LOG2, 1.5*LOG2, 2.0*LOG2):
    for z0 in (1e-4, 0.1, 1.0, 10.0, 100.0):
        z = z0
        prev = abs(z)
        for _ in range(2000):
            z = step_scaled(z, a)
            assert abs(z) <= prev + 1e-13 * max(1.0, prev)
            prev = abs(z)

for a in (0.3*LOG2, 1.4*LOG2):
    z = 1e-9
    ratio = step_scaled(z, a) / z
    target = 1.0 - a / LOG2
    assert abs(ratio - target) < 2e-9

a = LOG2
for z in (1e-4, 2e-5, 5e-6):
    zn = abs(step_scaled(z, a))
    assert abs(zn/(z*z) - 1.0/(2.0*LOG2)) < 2e-3

a = 2.0 * LOG2
for z0 in (0.1, 1.0, 10.0):
    z = z0
    n = 200000
    for _ in range(n):
        z = step_scaled(z, a)
    assert abs(n*abs(z) - LOG2) < 2e-3

for a in (2.1*LOG2, 3.0*LOG2, 6.0*LOG2, 10.0):
    q = a/2.0
    u = math.log(math.exp(q) - 1.0)
    z = u
    z1 = step_scaled(z, a)
    z2 = step_scaled(z1, a)
    assert abs(z1 + z) < 2e-12
    assert abs(z2 - z) < 2e-12
    p = 1.0 - math.exp(-q)
    d = -1.0 + 4.0*u*p/a
    assert -1.0 < d < 1.0
    assert d*d < 1.0

for a in (2.01*LOG2, 3.0*LOG2):
    slope = 1.0 - a/LOG2
    assert abs(slope) > 1.0

print("verification passed")
