"""Reproducibility checks for sharp reflected mixed-volume bounds on planar products.

Uses exact rational arithmetic for coefficients and polygon areas; finite
checks supplement, but cannot replace, the theorem's all-dimensional proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, pi, sqrt


def conv(a, b):
    ans = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i + j] += x * y
    return ans


def coeffs(rs):
    p = [Fraction(1)]
    for r in rs:
        p = conv(p, [Fraction(1), 2*r, Fraction(1)])
    return p


def central_triangle(m):
    return coeffs([Fraction(2)] * m)[m]


def convex_hull(points):
    points = sorted(set(points))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lower = []
    for v in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], v) <= 0:
            lower.pop()
        lower.append(v)
    upper = []
    for v in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], v) <= 0:
            upper.pop()
        upper.append(v)
    return lower[:-1] + upper[:-1]


def polygon_area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1] -
                   poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly)))) / 2


def reflected_sum_area(poly, t):
    return polygon_area(convex_hull([
        (x[0]-t*y[0], x[1]-t*y[1])
        for x in poly for y in poly]))


def checks():
    total = 0
    tri = [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)),
           (Fraction(0), Fraction(1))]
    square = [(Fraction(0), Fraction(0)), (Fraction(2), Fraction(0)),
              (Fraction(2), Fraction(2)), (Fraction(0), Fraction(2))]
    for poly, r in ((tri, Fraction(2)), (square, Fraction(1))):
        a = polygon_area(poly)
        for t in (Fraction(0), Fraction(1,5), Fraction(1,2),
                  Fraction(1), Fraction(3,2), Fraction(2)):
            assert reflected_sum_area(poly, t) == a*(1+2*r*t+t*t)
            total += 1
    # Every rational assignment in the 3-point grid for 1 <= m <= 6.
    for m in range(1, 7):
        top = coeffs([Fraction(2)]*m)
        bottom = [Fraction(comb(2*m, k)) for k in range(2*m+1)]
        for rs in product((Fraction(1), Fraction(3,2), Fraction(2)), repeat=m):
            out = coeffs(rs)
            mean = sum(rs, Fraction(0))/m
            balanced = coeffs([mean]*m)
            for k in range(1, 2*m):
                assert bottom[k] <= out[k] <= balanced[k] <= top[k]
                if 2 <= k <= 2*m-2 and out[k] == balanced[k]:
                    assert all(r == mean for r in rs)
                gap = top[k]-out[k]
                bound = (top[k]-bottom[k])*sum(2-r for r in rs)/m
                assert gap >= bound, (m,k,rs,gap,bound)
                if 2 <= k <= 2*m-2 and gap==bound:
                    assert all(r==1 for r in rs) or all(r==2 for r in rs)
                total += 1
    for m in (2,3,5,10,40,100,300):
        val = int(central_triangle(m))
        h = sum(comb(m,j)*comb(m-j,j)*4**(m-2*j)
                for j in range(m//2 + 1))
        assert h == val
        ratio = h/comb(2*m,m)**2
        pred = (3/8)**m * sqrt(3*pi*m/2)
        if m>=100:
            assert abs(ratio/pred-1) < 0.01
        total += 1
    print('VERIFY_OK', total)
    for m in (2,3,4,5,10,30):
        print('central',m, 'coefficient',int(central_triangle(m)),
              'normalized_ratio',float(central_triangle(m)/comb(2*m,m)**2))

if __name__ == '__main__':
    checks()
