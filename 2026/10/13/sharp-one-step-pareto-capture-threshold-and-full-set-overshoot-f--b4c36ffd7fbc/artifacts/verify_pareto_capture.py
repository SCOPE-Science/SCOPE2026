import math
import random


def common_gradient(x, lam, c):
    if x > c:
        return lam * (x - c)
    if x < -c:
        return lam * (x + c)
    return 0.0


def run(x0, lam, c, zeta, steps):
    x = x0
    w2 = zeta
    xs = [x]
    for _ in range(steps):
        g = common_gradient(x, lam, c)
        w2 += g * g
        if g == 0.0:
            xs.append(x)
            continue
        x = x - g / math.sqrt(w2)
        xs.append(x)
    return xs


def delta(r, y):
    return y * (1.0 / math.sqrt(r + y*y) - 1.0)

# Exact maximizer formula over a range of r values.
for r in [1e-6, 1e-3, 0.02, 0.125, 0.25, 0.6, 0.9, 0.999]:
    ystar = r**(1.0/3.0) * math.sqrt(1.0 - r**(1.0/3.0))
    dstar = (1.0 - r**(1.0/3.0))**1.5
    assert abs(delta(r, ystar) - dstar) < 1e-12
    # Nearby points do not exceed the analytic maximum.
    ymax = math.sqrt(1.0-r)
    for j in range(1, 1000):
        y = ymax*j/1000.0
        assert delta(r, y) <= dstar + 1e-12

# Safe-width example: every sampled crossing lands in the Pareto interval.
lam = 1.0
zeta = 0.125
r = zeta/(lam*lam)
dmax = (1.0-r**(1.0/3.0))**1.5
c = 0.51*dmax
for j in range(1,1000):
    y = math.sqrt(1.0-r)*j/1000.0
    x1 = run(c+y, lam, c, zeta, 1)[1]
    assert -c-1e-12 <= x1 <= c+1e-12

# Unsafe-width example: the analytic maximizer skips the entire Pareto interval.
c = 0.20*dmax
ystar = r**(1.0/3.0)*math.sqrt(1.0-r**(1.0/3.0))
x1 = run(c+ystar, lam, c, zeta, 1)[1]
assert x1 < -c
x1_left = run(-c-ystar, lam, c, zeta, 1)[1]
assert x1_left > c

# Exact endpoint hit at r+y^2=1.
c = 0.3
y = math.sqrt(1.0-r)
x1 = run(c+y, lam, c, zeta, 1)[1]
assert abs(x1-c) < 1e-12

# Noncrossing branch stays on its side and converges monotonically to the endpoint.
for r in [0.125, 0.8, 1.0, 2.0]:
    lam = 1.0
    zeta = r
    c = 0.4
    y0 = (math.sqrt(max(0.0,1.0-r)) + 0.7) if r < 1.0 else 0.7
    xs = run(c+y0, lam, c, zeta, 50000)
    assert all(x >= c - 1e-13 for x in xs)
    assert all(xs[k+1] <= xs[k] + 1e-15 for k in range(len(xs)-1))
    assert xs[-1]-c < 2e-4

# Random first-step algebra and left/right symmetry.
random.seed(11)
for _ in range(1000):
    lam = 10**random.uniform(-1,1)
    zeta = random.uniform(1e-4,0.99)
    c = 10**random.uniform(-2,0.5)
    y = 10**random.uniform(-3,0.5)
    r = zeta/(lam*lam)
    expected = c + y*(1.0 - 1.0/math.sqrt(r+y*y))
    got = run(c+y, lam, c, zeta, 1)[1]
    assert abs(got-expected) < 1e-11*max(1.0,abs(expected))
    left = run(-c-y, lam, c, zeta, 1)[1]
    assert abs(left + got) < 1e-11*max(1.0,abs(got))

print('VERIFY_OK')
