"""Supplementary standard-library checks for the Legendre sign-onset law.

This finite computation is not a proof of the uniform asymptotic theorem.
Run: python CHECK.py
"""
import math
from fractions import Fraction


def phase_max(p, q):
    """Exact attainable sin maximum for a reduced angle 2*pi*p/q."""
    if q % 2:
        return math.cos(math.pi / (2*q))
    return 1.0 if q % 4 == 2 else math.cos(math.pi / q)


def legendre_coefficient(n, delta, theta, steps=18000):
    """Composite Simpson rule; fixed resolution, only for low degrees."""
    assert steps % 2 == 0
    h = theta / steps
    total = 0.0
    for j in range(steps + 1):
        t = h*j
        c = math.cos(t)
        p0, p1 = 1.0, c
        for k in range(1, n):
            p0, p1 = p1, ((2*k+1)*c*p1-k*p0)/(k+1)
        poly = p0 if n == 0 else p1
        val = (theta-t)**delta * poly * math.sin(t)
        total += (1 if j in (0, steps) else 4 if j % 2 else 2) * val
    return h*total/3


def a_b(delta, theta):
    return (math.gamma(delta+1)*math.sqrt(2*math.sin(theta)/math.pi),
            delta*theta**(delta-1))


count = 0
for q in range(3, 151):
    for p in range(1, (q+1)//2):
        if math.gcd(p, q) != 1:
            continue
        angle = 2*math.pi*p/q
        brute = max(math.sin((j+0.5)*angle) for j in range(2*q))
        assert abs(brute-phase_max(p, q)) < 2e-12, (p, q, brute)
        count += 1
for theta in (math.pi/5, math.pi/3, math.pi/2, 2*math.pi/3):
    A, B = a_b(1.5, theta)
    m = max(math.sin((j+0.5)*theta) for j in range(1000))
    assert B > A*m and math.log(B/(A*m)) > 0
    count += 1
for n, delta, theta, expected in [
    (20, 1.30, math.pi/2, -1),
    (20, 1.35, math.pi/2, +1),
    (84, 1.35, math.pi/2, -1),
    (84, 1.50, math.pi/2, +1),
]:
    val = legendre_coefficient(n, delta, theta)
    assert val*expected > 1e-10, (n, delta, val)
    count += 1
# Check the two-source leading expansion for one moderately large index.
n, delta, theta = 100, 1.30, math.pi/2
numer = legendre_coefficient(n, delta, theta)
A, B = a_b(delta, theta)
N = n+0.5
pred = (B + A*N**(1.5-delta)*math.cos(N*theta-math.pi/4-(delta+1)*math.pi/2))/N**3
assert abs((numer-pred)/pred) < .05, (numer, pred)
count += 1
print('PASS:', count, 'supplementary assertions; no infinite-domain certification')
