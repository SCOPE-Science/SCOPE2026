"""Numerical checks for equal-area centered ellipse convex-hull area.

Requires only Python 3 standard library. Polygon sampling is an independent
finite approximation, not the proof of the continuous theorem.
"""
from math import atan, cos, pi, sin, sqrt


def covariance_from_map(L):
    return (
        (L[0][0]**2 + L[0][1]**2, L[0][0]*L[1][0] + L[0][1]*L[1][1]),
        (L[0][0]*L[1][0] + L[0][1]*L[1][1], L[1][0]**2 + L[1][1]**2),
    )


def area_formula(La, Lb):
    A = covariance_from_map(La)
    B = covariance_from_map(Lb)
    detA = A[0][0]*A[1][1] - A[0][1]**2
    detB = B[0][0]*B[1][1] - B[0][1]**2
    assert abs(detA-detB) < 1e-9 * max(1, detA)
    tr = (A[1][1]*B[0][0] + A[0][0]*B[1][1] - 2*A[0][1]*B[0][1])/detA
    d = sqrt(max(0, tr-2))
    return sqrt(detA)*(pi+2*d-2*atan(d/2)), d


def sampled_points(L, count):
    return [(L[0][0]*cos(t)+L[0][1]*sin(t),
             L[1][0]*cos(t)+L[1][1]*sin(t))
            for t in (2*pi*j/count for j in range(count))]


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    points = sorted(set(points))
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def polygon_area(poly):
    return abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in
                   zip(poly,poly[1:]+poly[:1])))/2


def run():
    cases = [
        (((1,0),(0,1)),((1,0),(0,1))),
        (((1,0),(0,1)),((1.5,0),(0,2/3))),
        (((1,0),(0,1)),((2,0),(0,0.5))),
        (((1,0),(0,1)),((4,0),(0,0.25))),
        (((2,0.3),(0,1)),((1.5,-0.4),(0,4/3))),
        (((1.4,-0.7),(0,2.1)),((2.1,0.9),(0,1.4))),
        (((3,0),(0,1)),((1.5,0.5),(0,2))),
    ]
    n=10000
    for i,(La,Lb) in enumerate(cases):
        exact,d=area_formula(La,Lb)
        approx=polygon_area(hull(sampled_points(La,n)+sampled_points(Lb,n)))
        err=exact-approx
        # Polygonal approximations lie inside the exact convex hull.
        assert err > -3e-8, (i,err)
        assert err < 2e-5*max(1,exact), (i,err)
        s=abs(La[0][0]*La[1][1]-La[0][1]*La[1][0])
        if d>1e-7:
            gain=exact-pi*s
            assert s*d < gain < 2*s*d
        print('case',i,'D',round(d,8),'exact',round(exact,9),
              'polygon',round(approx,9),'error',round(err,9))
    for d in (1e-3,1e-2,1,10,10000):
        gain=2*d-2*atan(d/2)
        ratio=gain/d
        assert 1 < ratio < 2
        print('gap ratio',d,round(ratio,9))
    print('PASS: 7 independent polygon comparisons and 5 sharp-bound checks')


if __name__ == '__main__':
    run()
