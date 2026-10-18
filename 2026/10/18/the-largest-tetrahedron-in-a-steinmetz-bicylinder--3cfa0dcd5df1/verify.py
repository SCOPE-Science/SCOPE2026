"""Standalone numerical and exact-rational spot checks for the bicylinder theorem.

Run with Python >=3.9: python verify.py. The proof in RESULT.md,
not these finite tests, establishes the universal bound.
"""
from fractions import Fraction as F
import math
import random


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def tetra_det(p, q, r, s):
    return det3(tuple(q[i]-p[i] for i in range(3)),
                tuple(r[i]-p[i] for i in range(3)),
                tuple(s[i]-p[i] for i in range(3)))


def circle(t, disk):
    # Rational parametrization of the unit circle.
    x = (1-t*t)/(1+t*t)
    z = 2*t/(1+t*t)
    return (x,F(0),z) if disk == 0 else (F(0),x,z)


def main():
    rng=random.Random(137)
    for _ in range(3000):
        tt=[F(rng.randint(-13,13),rng.randint(1,15)) for _ in range(4)]
        p,q,r,s=[circle(t,k) for t,k in zip(tt,(0,0,1,1))]
        det=tetra_det(p,q,r,s)
        # Bound 16/(3*sqrt(3)) for six times the volume in the two-disk hull.
        assert 27*det*det <= 256
        pp=[circle(t,k) for t,k in zip(tt,(0,0,0,1))]
        det=tetra_det(*pp)
        # Bound 3*sqrt(3)/2 for three points in one disk.
        assert 4*det*det <= 27
    a=math.sqrt(2/3)
    c=1/math.sqrt(3)
    tetra=[(a,a,c),(-a,-a,c),(a,-a,-c),(-a,a,-c)]
    for x,y,z in tetra:
        assert abs(x*x+z*z-1)<1e-14
        assert abs(y*y+z*z-1)<1e-14
    target=16/(9*math.sqrt(3))
    assert abs(abs(tetra_det(*tetra))/6-target)<1e-14
    # The bi-cylinder has square horizontal sections of area 4*(1-z*z).
    volume=16/3
    assert abs(target/volume-1/(3*math.sqrt(3)))<1e-14
    for _ in range(5000):
        pts=[]
        for _ in range(4):
            z=rng.uniform(-1,1)
            h=math.sqrt(1-z*z)
            pts.append((rng.uniform(-h,h),rng.uniform(-h,h),z))
        assert abs(tetra_det(*pts))/6 <= target+1e-12
    print('PASS: 6000 rational cases, 5000 contained tetrahedra, sharp equality and ratio')

if __name__=='__main__':
    main()
