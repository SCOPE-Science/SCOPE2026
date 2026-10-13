from fractions import Fraction
from math import comb, ceil, log2


def v2(n):
    if n == 0:
        raise ValueError('v2(0) undefined')
    n = abs(n)
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def lower_hull(points):
    hull = []
    for pt in points:
        while len(hull) >= 2:
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            x3, y3 = pt
            s12 = Fraction(y2-y1, x2-x1)
            s23 = Fraction(y3-y2, x3-x2)
            if s12 >= s23:
                hull.pop()
            else:
                break
        hull.append(pt)
    return hull


def floor_ordinates(hull, n):
    out = []
    j = 0
    for r in range(1, n):
        while not (hull[j][0] <= r <= hull[j+1][0]):
            j += 1
        x1, y1 = hull[j]
        x2, y2 = hull[j+1]
        y = Fraction(y1*(x2-x1) + (y2-y1)*(r-x1), x2-x1)
        out.append(y.numerator // y.denominator)
    return out

cases = 0
for k in range(1, 11):
    n = 2**k
    for r in range(1, n):
        assert v2(comb(n, r)) == k - v2(r)
    for s in range(0, k + 5):
        points = [(0, s+1)]
        points += [(r, v2(comb(n, r))) for r in range(1, n)]
        points += [(n, 0)]
        hull = lower_hull(points)
        got = floor_ordinates(hull, n)
        t = min(s, k)
        predicted = [min(t, k - ceil(log2(r))) for r in range(1, n)]
        assert got == predicted, (k, s, hull, got, predicted)
        expected_sum = n - 2**(k-t)
        assert sum(got) == expected_sum, (k, s, sum(got), expected_sum)
        if 1 <= s <= k:
            mid = 2**(k-s)
            assert v2(comb(n, mid)) == s
        cases += 1

print('VERIFY_OK newton_cases=%d k_max=10 index_formula=OK residual_midpoints=OK' % cases)
