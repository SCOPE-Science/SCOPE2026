#!/usr/bin/env python3
"""Exact rational interval certificate for the chord-enclosure of a regular heptagon.

No floating-point operations or external dependencies are used. Run with Python 3.
"""

from fractions import Fraction as F
from itertools import combinations
from math import factorial

SCALE = 10**18


def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = int(lo)
        self.hi = int(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def number(k):
        return Interval(k * SCALE)

    @staticmethod
    def rational_bounds(lo, hi):
        assert lo <= hi
        return Interval((lo.numerator * SCALE) // lo.denominator,
                        ceildiv(hi.numerator * SCALE, hi.denominator))

    def __add__(self, other):
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other):
        return Interval(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other):
        products = [a * b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return Interval(min(products) // SCALE, ceildiv(max(products), SCALE))

    def __truediv__(self, other):
        assert other.lo > 0
        q = [a * SCALE for a in (self.lo, self.hi)]
        lows = [v // b for v in q for b in (other.lo, other.hi)]
        highs = [ceildiv(v, b) for v in q for b in (other.lo, other.hi)]
        return Interval(min(lows), max(highs))


def atan_bounds(inv, terms=20):
    # Alternating-series theorem, x=1/inv, 0<x<1.
    acc = sum(((-1)**j * F(1, inv**(2*j+1) * (2*j+1))
               for j in range(terms)), F(0))
    remaining = F(1, inv**(2*terms+1) * (2*terms+1))
    end = acc + ((-1)**terms) * remaining
    return min(acc, end), max(acc, end)


def pi_bounds():
    a, b = atan_bounds(5)
    c, d = atan_bounds(239)
    # Machin's identity: pi = 16 arctan(1/5) - 4 arctan(1/239).
    return 16*a - 4*d, 16*b - 4*c


def trig_interval(multiplier, kind):
    # Evaluate sin/cos(j*pi/7) with Taylor + exact Lipschitz error.
    # j is 1,...,6, so the argument lies strictly between 0 and pi.
    plo, phi = pi_bounds()
    xlo = F(multiplier, 7) * plo
    xhi = F(multiplier, 7) * phi
    x = (xlo + xhi) / 2
    radius = (xhi - xlo) / 2
    m = 20
    if kind == 'sin':
        v = sum((F((-1)**j, factorial(2*j+1)) * x**(2*j+1)
                 for j in range(m)), F(0))
        err = x**(2*m+1) / factorial(2*m+1) + radius
    else:
        assert kind == 'cos'
        v = sum((F((-1)**j, factorial(2*j)) * x**(2*j)
                 for j in range(m)), F(0))
        err = x**(2*m) / factorial(2*m) + radius
    return Interval.rational_bounds(v-err, v+err)


def certificate():
    one = Interval.number(1)
    half = Interval(SCALE // 2)
    cs = [None] + [trig_interval(k, 'cos') for k in range(1,7)]
    sn = [None] + [trig_interval(k, 'sin') for k in range(1,7)]
    assert all(x.lo > 0 for x in sn[1:])
    c = cs[1]
    apothem = [one if j % 2 == 0 else c for j in range(14)]
    target = (c*c) * (sn[1]/cs[1] + Interval.number(3)*(sn[2]/cs[2]))
    feasible = 0
    optimum = []
    tested = 0
    min_gap = None
    closest = None
    for ids in combinations(range(14),4):
        gaps = [(ids[(i+1)%4]-ids[i]) % 14 for i in range(4)]
        if max(gaps) >= 7:
            continue
        feasible += 1
        # Independently compute each four-line enclosure, including winners.
        area = Interval.number(0)
        for i, gap in enumerate(gaps):
            h = apothem[ids[i]]
            k = apothem[ids[(i+1)%4]]
            numerator = h*k - half*(h*h + k*k)*cs[gap]
            area = area + numerator/sn[gap]
        is_winner = (all(j % 2 for j in ids) and
                     sorted(gaps) == [2, 4, 4, 4])
        if is_winner:
            assert area.lo <= target.hi and target.lo <= area.hi
            optimum.append(ids)
            continue
        tested += 1
        # Strong strict inequality, certified entirely in rational arithmetic.
        assert area.lo > target.hi, (ids, gaps, area.lo, target.hi)
        gap = area.lo - target.hi
        if min_gap is None or gap < min_gap:
            min_gap, closest = gap, ids
    assert feasible == 511, feasible
    assert len(optimum) == 7, optimum
    assert tested == 504, tested
    # A simple exact rational *lower* bound for the runner-up gap (unit radius).
    assert min_gap > SCALE // 40, min_gap  # > 1/40 = 0.025
    print('PASS: all 511 bounded four-support configurations')
    print('PASS: exactly seven optimizing configurations, all four edge-supported')
    print('PASS: 504 other configurations have certified area gap > 1/40')
    print('Closest nonoptimizing support indices:', closest)
    print('Target area interval, scaled by 10^18:', target.lo, target.hi)
    print('Minimum strict difference scaled by 10^18:', min_gap)


if __name__ == '__main__':
    certificate()
