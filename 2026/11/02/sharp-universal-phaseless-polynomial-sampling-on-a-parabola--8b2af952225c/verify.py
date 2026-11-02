"""Exact-rational, dependency-free finite checks for the parabolic sharpness construction.

Run: python3 verify.py. The finite checks supplement an all-degree proof.
"""
from fractions import Fraction as F


def conv(p, q):
    s = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            s[i + j] += a * b
    return s


def evaluate(p, u):
    total = F(0)
    for a in reversed(p):
        total = total * u + a
    return total


def base_polynomial(R):
    return [F(R * R), F(1 - 2 * R), F(1)]

R = [100, 10**7, 10**14, 10**21]
alpha = [F(1, 2), F(7, 8), F(15, 16), F(31, 32)]
c = F(1, 4)
assert c < 1
# The deck symmetries are polynomial identities over Gaussian integers.
# Represent coefficients in ascending powers of a formal t.
def cconv(a, b):
    out = [0j] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

def z_of(a, sign):
    square = cconv(a, a)
    out = [0j] * max(len(a), len(square))
    for j, x in enumerate(a):
        out[j] += x
    for j, x in enumerate(square):
        out[j] += sign * 1j * x
    return out

assert z_of([1j, -1], +1) == [0j, 1+0j, 1j]
assert z_of([-1j, -1], -1) == [0j, 1+0j, -1j]

checks = 4
for n in range(1, len(R) + 1):
    P, Q = [F(1)], [c * c]
    for j in range(n):
        P = conv(P, base_polynomial(R[j]))
        Q = conv(Q, base_polynomial(alpha[j] * R[j]))
        if j > 0:
            Q = [k / (alpha[j] * alpha[j]) for k in Q]
    assert len(P) == len(Q) == 2*n + 1
    D = [P[j] - Q[j] for j in range(2*n + 1)]
    assert D[-1] != 0, 'nonzero full degree in u'
    assert P[-1] / Q[-1] > 1, 'large-u ratio must exceed one'
    points = [F(0)]
    for j in range(n):
        if j > 0:
            points.append(F(R[j], 1000))
        points.append(F(R[j]))
    assert len(points) == 2*n
    assert points == sorted(points)
    signs = [1 if evaluate(D, u) > 0 else -1 if evaluate(D, u) < 0 else 0 for u in points]
    assert signs == [1 if k % 2 == 0 else -1 for k in range(2*n)], (n, signs)
    # The final sign at infinity is positive. Thus 2*n disjoint sign-change
    # intervals, each containing a distinct positive simple root of D(u).
    # The polynomial has degree 2*n, so these are all its roots.
    checks += 4*n + 5
    print(f'n={n}: {2*n} sign-separated positive roots in u; {4*n} t-points; leading ratio={P[-1]/Q[-1]}')
print('ALL_CHECKS_PASS')
