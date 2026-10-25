#!/usr/bin/env python3
"""Exact rational identities and supplementary deterministic tail tests.

Only the standard library is required. The universal assertions are proved
analytically in RESULT.md; this script checks algebra and numerical diagnostics.
"""
from fractions import Fraction as Q
from math import factorial, pi, sqrt, asin, sin, cos, hypot


def poly_add(x, y):
    out = x.copy()
    for i, v in y.items():
        out[i] = out.get(i, Q(0)) + v
    return {i: v for i, v in out.items() if v}


def poly_mul(x, y):
    out = {}
    for i, a in x.items():
        for j, b in y.items():
            out[i + j] = out.get(i + j, Q(0)) + a * b
    return {i: v for i, v in out.items() if v}


def determinant_poly(p):
    c = {2 * k: Q((-1) ** k * 2 ** (2 * k), factorial(2 * k))
         for k in range(p // 2 + 1)}
    s = {2 * k + 1: Q((-1) ** k * 2 ** (2 * k + 1), factorial(2 * k + 1))
         for k in range((p - 1) // 2 + 1)}
    return {i: v / 4 for i, v in poly_add({0: Q(1)},
                {j: -v for j, v in poly_add(poly_mul(c, c), poly_mul(s, s)).items()}).items() if v}


def mat_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def mat_scale(a, t):
    return [[t * a[i][j] for j in range(2)] for i in range(2)]


def mat_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def commutator(a):
    j = [[Q(0), Q(-1)], [Q(1), Q(0)]]
    x, y = mat_mul(j, a), mat_mul(a, j)
    return mat_add(x, mat_scale(y, Q(-1)))


def matrix_taylor(p, h):
    x = [[Q(1), Q(0)], [Q(0), Q(0)]]
    a = [[Q(0), Q(0)], [Q(0), Q(0)]]
    for k in range(p + 1):
        a = mat_add(a, mat_scale(x, h ** k / factorial(k)))
        x = commutator(x)
    return a


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def mv(a, v):
    return [dot(row, v) for row in a]


def transpose(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]


def norm_sq(a):
    return sum(a[i][j] ** 2 for i in range(2) for j in range(2))


def nystrom(a, w, v):
    aw, atv = mv(a, w), mv(transpose(a), v)
    d = dot(v, aw)
    if d == 0:
        return None
    return [[aw[i] * atv[j] / d for j in range(2)] for i in range(2)]


def residual(a, n):
    return mat_add(a, mat_scale(n, Q(-1)))


check_count = 0
for p in range(1, 15):
    coeffs = determinant_poly(p)
    m = (p - 1) // 2 if p % 2 else p // 2
    if p % 2:
        lead_power = p + 1
        lead = Q((-1) ** (m + 1) * 2 ** (p + 1), 2 * factorial(p + 1))
    else:
        lead_power = p + 2
        lead = Q((-1) ** m * 2 ** (p + 2), 2 * (p + 2) * factorial(p))
    assert min(coeffs) == lead_power and coeffs[lead_power] == lead, (p, coeffs)
    assert (lead > 0) == (p % 4 in (0, 3))
    check_count += 1

known = {
    1: {2: Q(-1)},
    2: {4: Q(-1)},
    3: {4: Q(1, 3), 6: Q(-4, 9)},
    4: {6: Q(2, 9), 8: Q(-1, 9)},
}
for p, polynomial in known.items():
    assert determinant_poly(p) == polynomial
    check_count += 1

for p in range(1, 10):
    for h in [Q(1, 9), Q(1, 2), Q(5, 4)]:
        a = matrix_taylor(p, h)
        assert a[0][0] + a[1][1] == 1 and a[0][1] == a[1][0]
        assert det(a) == sum(val * h ** degree for degree, val in determinant_poly(p).items())
        check_count += 1

vectors = [[Q(1), Q(2)], [Q(2), Q(3)], [Q(3), Q(-2)],
           [Q(-1), Q(4)], [Q(7), Q(5)]]
for p in range(1, 9):
    a = matrix_taylor(p, Q(2, 5))
    d = det(a)
    assert d != 0
    for v in vectors:
        for w in vectors:
            g = nystrom(a, w, v)
            if g is None:
                continue
            e = residual(a, g)
            denom = dot(v, mv(a, w))
            target = d ** 2 * dot(v, v) * dot(w, w) / (denom ** 2)
            assert norm_sq(e) == target
            check_count += 1


def tail_tied_exact(d, threshold):
    # Trace-one indefinite input, eigenvalues a > 0 > -b; det=-d.
    discr = sqrt(1 + 4 * d)
    a, b = (1 + discr) / 2, (discr - 1) / 2
    mid, width = (a - b) / 2, (a + b) / 2
    eps = d / threshold
    lo = max(-1.0, min(1.0, (-eps - mid) / width))
    hi = max(-1.0, min(1.0, (eps - mid) / width))
    return (asin(hi) - asin(lo)) / pi

for p, h in [(1, 0.4), (2, 0.6), (3, 1.3), (4, 2.1)]:
    dpol = determinant_poly(p)
    d = -float(sum(v * Q(str(h)) ** k for k, v in dpol.items()))
    assert d > 0
    asymptotic = 2 * sqrt(d) / pi
    for threshold in [1e4, 1e6]:
        tail = tail_tied_exact(d, threshold)
        assert abs(threshold * tail / asymptotic - 1) < 0.0002
        check_count += 1

# Conditional angular integration for two independent one-column Gaussian sketches.
a = matrix_taylor(4, Q(1, 2))  # positive definite, full rank
D = abs(float(det(a)))
N = 4096
elliptic_average = 0.0
conditional_tail = 0.0
T = 10 ** 5
for k in range(N):
    theta = 2 * pi * (k + 0.5) / N
    u = (cos(theta), sin(theta))
    z0 = float(a[0][0]) * u[0] + float(a[0][1]) * u[1]
    z1 = float(a[1][0]) * u[0] + float(a[1][1]) * u[1]
    radius = hypot(z0, z1)
    elliptic_average += 1 / radius / N
    conditional_tail += 2 * asin(D / (T * radius)) / pi / N
C = 2 * D * elliptic_average / pi
assert abs(T * conditional_tail / C - 1) < 1e-8
assert C > 0
check_count += 1

print('VERIFY_OK', check_count, 'exact rational and asymptotic checks; independent-tail constant', f'{C:.12g}')
