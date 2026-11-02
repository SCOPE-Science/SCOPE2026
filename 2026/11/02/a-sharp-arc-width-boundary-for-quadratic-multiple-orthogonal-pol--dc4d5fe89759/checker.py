"""Supplementary numerical checks of the quadratic MOPUC moment classification.

Only finite tests are performed. The theorem for all measures follows from the
analytic argument in RESULT.md rather than these tests.
"""
from __future__ import annotations
import cmath
import math
import random

RNG = random.Random(1729)
assertions = 0

def check(condition: bool, message: str) -> None:
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)

def coefficients(u: float, v: float, theta: float):
    omega = cmath.exp(1j * theta)
    return -(v / u) * (1 + omega), v * omega

def rotated_roots(u: float, v: float, theta: float):
    b = -2 * v * math.cos(theta / 2) / u
    square = cmath.sqrt(b * b - 4 * v)
    return (-b + square) / 2, (-b - square) / 2

def near(a, b, tol=1e-10):
    return abs(a - b) < tol

# Validate all orthogonality equations and the precise Schur equivalence
# for diverse symmetric angular probability measures (finite mixtures).
for _ in range(2100):
    alpha = RNG.uniform(.01, math.pi / 2 - .01)
    theta = RNG.uniform(2 * alpha + 1e-5, 2 * math.pi - 2 * alpha - 1e-5)
    terms = [RNG.random() for _ in range(4)]
    scales = [RNG.uniform(0, alpha) for _ in range(4)]
    weights = [w / sum(terms) for w in terms]
    u = sum(w * math.cos(t) for w, t in zip(weights, scales))
    v = sum(w * math.cos(2 * t) for w, t in zip(weights, scales))
    A, B = coefficients(u, v, theta)
    omega = cmath.exp(1j * theta)
    check(near(v + A * u + B, 0), 'First moment condition')
    check(near(v * omega ** 2 + A * u * omega + B, 0), 'Second moment condition')
    roots = rotated_roots(u, v, theta)
    criterion = (1 + v) * u > 2 * abs(v) * abs(math.cos(theta / 2))
    for root in roots:
        check(near(root * root - 2 * (v / u) * math.cos(theta / 2) * root + v, 0), 'Root identity')
    if abs((1 + v) * u - 2 * abs(v) * abs(math.cos(theta / 2))) > 1e-8:
        check(criterion == all(abs(z) < 1 - 1e-9 for z in roots), 'Schur criterion')
    if alpha <= math.acos(1 / math.sqrt(3)):
        check(criterion, 'Subcritical support bound')

# Construct endpoint pair failures for an unbounded family of widths.
star = math.acos(1 / math.sqrt(3))
for j in range(1, 451):
    alpha = star + j * (math.pi / 2 - star) / 451
    c = math.cos(alpha)
    v = math.cos(2 * alpha)
    hcritical = c ** 3 / (1 - 2 * c ** 2)
    theta = (2 * alpha + 2 * math.acos(hcritical)) / 2
    check(2 * alpha < theta < 2 * math.acos(hcritical), 'Admissible escape interval')
    roots = rotated_roots(c, v, theta)
    check(max(abs(z) for z in roots) > 1, 'Endpoint-pair exterior zero')

# Explicit exact-angle example, and smooth-density approximations
# concentrate sufficiently near the endpoint point masses.
alpha = math.pi / 3
theta = 5 * math.pi / 6
u = .5
v = -.5
check(max(abs(z) for z in rotated_roots(u, v, theta)) > 1.01, 'Explicit exterior root')
check(.5 - 2 * math.cos(5 * math.pi / 12) < 0, 'Exact rational-trigonometric sign')

# Interior two-bump approximations: numerically integrate normalized
# beta-shaped bumps near +/-alpha, plus a small uniform background.
def composite_simpson(f, lo, hi, N=1600):
    h = (hi - lo) / N
    return h / 3 * (f(lo) + f(hi) +
           4 * sum(f(lo + h * (2 * k + 1)) for k in range(N // 2)) +
           2 * sum(f(lo + h * 2 * k) for k in range(1, N // 2)))

def bump(x, center, width):
    t = (x - center) / width
    return math.exp(-1 / (1 - t * t)) if abs(t) < 1 else 0.

width = 0.001
center = alpha - 2 * width
background = 1e-6
# support is exactly the full [-alpha,alpha]; the background is flat at both endpoints.
f = lambda s: .5 * (bump(s,center,width) + bump(s,-center,width)) + background * bump(s, 0.0, alpha)
norm = composite_simpson(f, -alpha, alpha)
u = composite_simpson(lambda s: f(s) * math.cos(s), -alpha, alpha) / norm
v = composite_simpson(lambda s: f(s) * math.cos(2*s), -alpha, alpha) / norm
check(max(abs(z) for z in rotated_roots(u, v, theta)) > 1, 'Full-support smooth approximation')

# Uniform angular weights never escape in the admissible separated family.
for j in range(1, 301):
    alpha = j * math.pi / 602
    u = math.sin(alpha) / alpha
    v = math.sin(2 * alpha) / (2 * alpha)
    for tfrac in (.001, .33, .5, .67, .999):
        theta = 2 * alpha + tfrac * (2 * math.pi - 4 * alpha)
        check(max(abs(z) for z in rotated_roots(u, v, theta)) < 1, 'Uniform arc localization')

if __name__ == '__main__':
    print('PASS: ' + str(assertions) + ' deterministic supplementary assertions')
    print('Non-exhaustive numerical checks; proof is in RESULT.md.')
