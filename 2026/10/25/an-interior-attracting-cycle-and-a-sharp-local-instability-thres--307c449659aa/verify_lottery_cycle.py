"""Exact rational interval certificate for an interior best-response two-cycle.

Run: python verify_lottery_cycle.py
No external libraries. Every interval bound uses integer arithmetic and
conservative outward rounding, including square roots.
"""
from fractions import Fraction as Q
from math import isqrt

SCALE = 10**24


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = Q(lo)
        self.hi = Q(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        b = interval(other)
        return Interval(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-interval(other))

    def __rsub__(self, other):
        return interval(other) - self

    def __mul__(self, other):
        b = interval(other)
        vals = [a * d for a in (self.lo, self.hi)
                for d in (b.lo, b.hi)]
        return Interval(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = interval(other)
        assert b.lo * b.hi > 0, "division interval contains zero"
        return self * Interval(1 / b.hi, 1 / b.lo)

    def __rtruediv__(self, other):
        return interval(other) / self

    def sqrt(self):
        assert self.lo >= 0
        def lower_grid_root(q):
            return isqrt(q.numerator * SCALE * SCALE // q.denominator)
        return Interval(Q(lower_grid_root(self.lo), SCALE),
                        Q(lower_grid_root(self.hi) + 1, SCALE))


def interval(value):
    return value if isinstance(value, Interval) else Interval(value)


def F(y):
    """For cost ratio c=1/6, F(y) = sqrt(6*(sqrt(y)-y))-(sqrt(y)-y)."""
    x = y.sqrt() - y
    return (6 * x).sqrt() - x


def derivative_F(y):
    x = y.sqrt() - y
    return (1 / (2 * (x / 6).sqrt()) - 1) * (1 / (2 * y.sqrt()) - 1)


def main():
    lo, hi = Q(26299, 100000), Q(26300, 100000)
    a, b = Interval(lo), Interval(hi)
    g_a, g_b = F(F(a)) - a, F(F(b)) - b
    assert Q(3, 1000000) < g_a.lo <= g_a.hi < Q(4, 1000000)
    assert -Q(6, 1000000) < g_b.lo <= g_b.hi < -Q(5, 1000000)
    J = Interval(lo, hi)
    K = F(J)
    assert Q(97447, 100000) < K.lo <= K.hi < Q(97455, 100000)
    assert J.hi < K.lo
    multiplier = derivative_F(J) * derivative_F(K)
    assert Q(17, 100) < multiplier.lo <= multiplier.hi < Q(18, 100)
    # F^2(y)-y changes sign on J. IVT supplies a genuine cycle point.
    # Because K is disjoint from J and |(F^2)'|<1 on J, that point
    # belongs to a locally attracting (prime-two) orbit of F.
    print('PASS: exact-rational endpoint, interiority, and attraction certificate')
    print('g(lo) enclosure:', str(g_a.lo), str(g_a.hi))
    print('g(hi) enclosure:', str(g_b.lo), str(g_b.hi))
    print('F(J) numerical enclosure:', float(K.lo), float(K.hi))
    print('(F^2) derivative enclosure:', float(multiplier.lo), float(multiplier.hi))


if __name__ == '__main__':
    main()
