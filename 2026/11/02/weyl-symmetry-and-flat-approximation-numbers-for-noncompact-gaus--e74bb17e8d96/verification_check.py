#!/usr/bin/env python3
"""Reproducible finite consistency checks of the Gaussian covariance identity."""
import cmath
import math
import random

rng = random.Random(42016)
count = 0
for _ in range(3000):
    alpha = (rng.random() - .5) * .65 + 1j * (rng.random() - .5) * .65
    beta = (rng.random() - .5) * .55 + 1j * (rng.random() - .5) * .55
    gamma = (.2 + rng.random() * .75) * cmath.exp(2j * math.pi * rng.random())
    d = 1 - 4 * abs(alpha)**2
    if d <= 0:
        continue
    a = abs(gamma)**2 - 1 - 4 * alpha * beta * gamma.conjugate() / gamma
    b = 2 * (beta.conjugate() + alpha * gamma.conjugate() / gamma)
    lhs = d * (abs(a)**2 - abs(b)**2)
    rhs = (abs(gamma)**2 - d)**2 - 4 * abs(d * beta.conjugate() + alpha * gamma.conjugate()**2)**2
    assert abs(lhs - rhs) < 4e-14, (lhs, rhs)
    count += 1

alpha = 1 / 10
beta = 1 / 5
gamma = 2 * math.sqrt(3) / 5
u = 1
v = math.sqrt(3) / 2
D = 1 - 4 * abs(alpha)**2
N = beta + alpha * gamma**2 / D
assert abs(abs(gamma)**2 / D + 2 * abs(N) - 1) < 1e-13
assert abs(gamma * v - (u - 2 * beta * u)) < 1e-13
assert abs(gamma * u - (v - 2 * alpha * v)) < 1e-13
c_exponent = beta * u**2 - u**2/2 - alpha * v**2 + v**2/2
assert abs(c_exponent) < 1e-13
count += 4

# Compare logarithms of TW_u k_w and W_v T k_w on the explicit boundary example.
for _ in range(1500):
    w = (rng.random() - .5) * 3 + 1j*(rng.random() - .5) * 3
    z = (rng.random() - .5) * 3 + 1j*(rng.random() - .5) * 3
    phase = (u*w - u*w.conjugate())/2
    wl = w + u
    left = phase + alpha*z*z + beta*wl.conjugate()**2 + gamma*z*wl.conjugate() - abs(wl)**2/2
    right = z*v - v*v/2 + alpha*(z-v)**2 + beta*w.conjugate()**2 + gamma*(z-v)*w.conjugate() - abs(w)**2/2
    assert abs(left-right) < 3e-13, (w,z,left,right)
    count += 1
print(f"PASS: {count} finite algebraic/coherent-state consistency assertions")
