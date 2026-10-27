#!/usr/bin/env python3
"""Exact-rational interval checks for a regular-hexagon Lipschitz extension formula.

All square-root bounds are rational and certified by integer-square comparisons.
The geometric proof in RESULT.md, not finite computation, establishes optimality.
"""
from fractions import Fraction as F
from math import isqrt

SCALE = 10 ** 16


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def as_i(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        other = I.as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -I.as_i(other)

    def __rsub__(self, other):
        return I.as_i(other) - self

    def __mul__(self, other):
        other = I.as_i(other)
        candidates = (self.lo * other.lo, self.lo * other.hi,
                      self.hi * other.lo, self.hi * other.hi)
        return I(min(candidates), max(candidates))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I.as_i(other)
        assert other.lo > 0 or other.hi < 0
        return self * I(F(1, 1) / other.hi, F(1, 1) / other.lo)

    def contains(self, x):
        return self.lo <= F(x) <= self.hi

    def show(self):
        return f'[{float(self.lo):.14f}, {float(self.hi):.14f}]'


def root(r):
    r = F(r)
    assert r >= 0
    # sqrt(p/q) = sqrt(p*q)/q, so floor(sqrt(p*q)*SCALE)/(q*SCALE).
    p, q = r.numerator, r.denominator
    n = isqrt(p * q * SCALE * SCALE)
    return I(F(n, q * SCALE), F(n + 1, q * SCALE))


r3, r7, r13 = root(3), root(7), root(13)
K = 2 * (2 + r3) / (1 + r7 + r13)
B = (1 + r3 - K * r7) / (r3 - 1)
Delta = K * (r13 - 1) / (1 + r3)
A, C = (1 - B + Delta) / 2, (1 - B - Delta) / 2
a, b, c = A / 2, B / 2, C / 2
assert c.lo > 0 and b.lo > c.hi and a.lo > b.hi
assert (2 * (a + b + c)).lo < 1 < (2 * (a + b + c)).hi
assert K.lo > 1

# Coordinates (x,y*sqrt(3)) of vertices on the unit circumcircle.
v = [(F(1), F(0)), (F(1, 2), F(1, 2)),
     (F(-1, 2), F(1, 2)), (F(-1), F(0)),
     (F(-1, 2), F(-1, 2)), (F(1, 2), F(-1, 2))]
m = [((v[i][0] + v[(i+1) % 6][0]) / 2,
      (v[i][1] + v[(i+1) % 6][1]) / 2) for i in range(6)]


def sqdist(x, y):
    return (x[0] - y[0]) ** 2 + 3 * (x[1] - y[1]) ** 2


def dist(x, y):
    return root(sqdist(x, y))


assert [sqdist(m[0], v[k]) for k in range(6)] == [
    F(1, 4), F(1, 4), F(7, 4), F(13, 4), F(13, 4), F(7, 4)]
assert [sqdist(m[0], m[k]) for k in range(1, 4)] == [
    F(3, 4), F(9, 4), F(3)]

weights = [a, a, b, c, c, b]
for i in range(6):
    w = [weights[(j-i) % 6] for j in range(6)]
    for j in range(6):
        expression = sum((w[k] * dist(v[k], v[j]) for k in range(6)), I(0))
        target = K * dist(m[i], v[j])
        assert abs(float(expression.lo - target.hi)) < 2e-12
        assert abs(float(expression.hi - target.lo)) < 2e-12

# Convolution kernel: mu_i = nu_i * eta with nu_i=(delta_i+delta_(i+1))/2.
eta = [2 * (a - b + c), 2 * (b-c), 2*c, I(0), 2*c, 2 * (b-c)]
assert all(x.lo >= 0 for x in eta)
assert (sum(eta, I(0))).lo < 1 < (sum(eta, I(0))).hi
for j in range(6):
    convoluted = (eta[j] + eta[(j-1) % 6]) / 2
    assert abs(float(convoluted.lo - weights[j].hi)) < 2e-12
    assert abs(float(convoluted.hi - weights[j].lo)) < 2e-12

# Base-k transportation couplings for midpoint pairs: k=1,2,3.
# Rotations and reflections cover all other pairs.
base_coupling_costs = [dist(v[0], v[2]) / 2,
                       (dist(v[0], v[3]) + dist(v[1], v[2])) / 2,
                       (dist(v[0], v[4]) + dist(v[1], v[3])) / 2]
for i in range(6):
    for j in range(i + 1, 6):
        separation = min((j - i) % 6, (i - j) % 6)
        target = dist(m[i], m[j])
        cost = base_coupling_costs[separation - 1]
        assert abs(float(cost.lo - target.hi)) < 2e-12
        assert abs(float(cost.hi - target.lo)) < 2e-12

# Symmetric dual distance-test average: the three orbit sums coincide.
for pair in ((0,1), (2,5), (3,4)):
    val = sum((dist(v[j], v[q]) for j in pair for q in (0, 2, 3)), I(0))
    assert abs(float(val.lo - (4+2*r3).hi)) < 2e-12
    assert abs(float(val.hi - (4+2*r3).lo)) < 2e-12

# Endpoint averaging has a strictly worse sharp operator norm.
ordinary = (2+r3) / r13
assert ordinary.lo > ((1+r3)/r7).hi
assert ordinary.lo > K.hi
print('hexagon interpolation checks passed')
print('sharp constant:', K.show())
print('orbit weights:', a.show(), b.show(), c.show())
print('arithmetic midpoint norm:', ordinary.show())
print('vertex-to-midpoint pairs: 36; midpoint pairs: 15; signed lower-bound orbit identities: 3')
