#!/usr/bin/env python3
"""Exact recurrence and finite symbolic-itinerary census for a three-zone affine map.

Only standard-library rational and combinatorial arithmetic is used.
The finite enumeration is exhaustive for periods at most five; it is not
claimed to classify higher periods or nonperiodic dynamics.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd


def periodic_coordinates(signs, b):
    """Return x_i/d for an n-periodic solution with a proposed sign sequence.

    The recurrence is x_(i+1) = -b*x_(i-1)+d*sign_i.
    0<b<1, hence the denominator 1-(-b)^L never vanishes.
    """
    n = len(signs)
    L = n // gcd(n, 2)
    denominator = 1 - (-b) ** L
    return tuple(sum(((-b) ** k * signs[(i - 1 - 2*k) % n]
                      for k in range(L)), F(0)) / denominator
                 for i in range(n))


def canonical_rotation(word):
    return min(tuple(word[j:] + word[:j]) for j in range(len(word)))


def admissible_range(signs, b):
    """Calculate ALL r=d/h>0 giving this exact itinerary.

    Output (lower_exclusive, upper_inclusive), where None is infinity.
    Zero symbol uses |x_i-x_(i-1)| <= h; active uses strict inequality.
    """
    if not any(signs):
        return None
    q = periodic_coordinates(signs, b)
    u = [q[i] - q[i-1] for i in range(len(signs))]
    if any(signs[i]*u[i] <= 0 for i in range(len(signs)) if signs[i]):
        return None
    H = min(abs(u[i]) for i in range(len(signs)) if signs[i])
    Z = max([abs(u[i]) for i in range(len(signs)) if not signs[i]]+[F(0)])
    if H <= Z:
        return None
    return (1/H, 1/Z if Z else None)


def orbit_catalog(n, b):
    found = {}
    for code in product((-1, 0, 1), repeat=n):
        if not any(code):
            continue
        word = tuple(code)
        interval = admissible_range(word, b)
        if interval:
            key = canonical_rotation(word)
            if key in found:
                assert found[key] == interval
            else:
                found[key] = interval
    return found


def selected_five_cycle(d):
    return tuple(d * F(num, 1025) for num in (-84, -1344, -1004, 336, 1276))


def step(x, y, b, d, h):
    delta = x-y
    sigma = (delta > h) - (delta < -h)
    return -b*y + d*sigma, x


def verify():
    b = F(1, 4)
    catalog = {n: orbit_catalog(n, b) for n in range(1, 6)}
    assert {n:len(v) for n, v in catalog.items()} == {1:0,2:0,3:0,4:0,5:4}
    assert catalog[5] == {
        (-1, -1, 0, 1, 0): (F(205,252), F(205,188)),
        (-1, 0, 1, 1, 0): (F(205,252), F(205,188)),
        (-1, -1, 0, 1, 1): (F(41,16), F(41,4)),
        (-1, -1, 1, 1, 0): (F(41,16), F(41,4))
    }
    # Each strict weak-forcing point has the expected cycles and no other
    # length-<=5 nontrivial orbits. Check full physical map, not just symbols.
    for r in (F(41,50), F(9,10), F(99,100)):
        h = F(1); d = r
        x = selected_five_cycle(d)
        for i in range(5):
            assert step(x[i], x[i-1], b, d, h) == (x[(i+1)%5], x[i])
            assert step(-x[i], -x[i-1], b, d, h) == (-x[(i+1)%5], -x[i])
        assert len(set(x)) == 5
        assert len(set(x).intersection({-z for z in x})) == 0
    assert admissible_range((-1,-1,0,1,0), b) == (F(205,252),F(205,188))
    # Boundary must not be mistaken for an active lower branch.
    x = selected_five_cycle(F(205,252))
    assert step(x[1], x[0], b, F(205,252), F(1)) != (x[2],x[1])
    # An explicit parameter family of additional examples, checked exactly.
    for b in (F(1,10),F(1,5),F(1,4),F(2,5),F(1,2),F(11,20)):
        Q = 1-b+b*b-b**3+b**4
        Z = max(b+b**3, abs(1-b-b**3))
        lower = Q/(1-b**3)
        upper = min(F(1),Q/Z)
        assert b+2*b**3<1 and lower<upper
        r=(lower+upper)/2
        q=periodic_coordinates((-1,-1,0,1,0),b)
        for i in range(5):
            assert step(r*q[i],r*q[i-1],b,r,F(1)) == (r*q[(i+1)%5],r*q[i])
    print('PASS: all 358 nonzero ternary words of lengths 1 to 5 were checked exactly')
    print('PASS: periods 1 through 4 have no nonzero cycles; all 4 canonical length-5 words enumerated')
    print('PASS: weak forcing has exactly 2 period-five cycles precisely for 205/252 < d/h < 1')
    print('PASS: exact map closure, symmetry, boundary semantics, rational parameter witnesses')

if __name__ == '__main__':
    verify()
