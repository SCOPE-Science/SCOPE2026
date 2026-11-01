"""Exact-rational checks for an elliptic harmonic-convolution witness.

This checks the concrete example and symbolic limits stated in the accompanying
proof; it is not a substitute for the maximum-modulus argument over the disk.
Run: python3 verify.py
"""
from fractions import Fraction as Q
from math import sqrt


def witness(k: Q, eps: Q, x: Q):
    a, b = -1 + eps, k * eps
    assert -1 < a < 0 < b < 1 and -1 < x < 0
    # The numerator of 1 + P_a(cos t) - P_b(cos t) is
    # N(X) = 4ab X^2 - 4b(ab+1)X + a^2b^2-a^2+3b^2+1.
    assert a * b < 0
    nminus = (a + 1) * (b + 1) * (a*b - a + 3*b + 1)
    nplus = (a - 1) * (b - 1) * (a*b + a - 3*b + 1)
    assert nminus > 0 and nplus > 0

    c1 = (a*a - a*b + b*b - 1) / (a*b - 1)
    cm = -b * (a-b) * (b*b-1) / (a*b-1)
    c2 = (a*a - 1) * (a-b) / (a*b-1)
    delta = c1*c1 - cm*cm
    assert c1 > cm > 0 and delta > 0
    aa = c1*c2/delta
    bb = -cm*cm*b/delta
    cc = c1*cm*b/delta
    dd = -cm*c2/delta

    def S(r):
        return x*(2-r*x)/(1-r*x)**2

    p = 1 + aa*aa*S(a*a) + 2*aa*bb*S(a*b) + bb*bb*S(b*b)
    q = dd*dd*S(a*a) + 2*dd*cc*S(a*b) + cc*cc*S(b*b)
    ratio = (c1+cm)/(c1-cm)
    return p, q, ratio

k, eps, x = Q(23, 100), Q(1, 100), Q(-99, 100)
p, q, ratio = witness(k, eps, x)
assert Q(15, 1000) < p < Q(16, 1000)
assert -Q(17, 1000) < q < -Q(16, 1000)
assert p*p - q*q < 0
assert Q(1) < ratio < Q(13, 10)
assert ratio == Q(6030299371723, 4647100628277)

# The limiting profile at parameter d=k/[2(1-k)] has transition at
# d_c=(-3+sqrt(15))/6 and limiting ellipse ratio sqrt(5/3).
d = k / (2*(1-k))
c = (1+d)**2 + d*d
assert c > Q(4, 3)
assert Q(0) < d < Q(1, 6)
print('CHECK_OK: exact circle orientation, normalized coefficients,')
print('          ellipse ratio under 13/10 and negative convolution Jacobian')
print('axis_ratio=', ratio)
print('p_prime=', float(p), 'q_prime=', float(q), 'Jacobian=', float(p*p-q*q))
