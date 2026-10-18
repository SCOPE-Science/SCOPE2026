#!/usr/bin/env python3
"""Independent rational checks for triangular-bipyramid reflected mixed volumes.

Requires Python 3, numpy and scipy. This finite checker supplements, but does
not replace, the analytical proof in RESULT.md.
"""
from fractions import Fraction as F
from random import Random
import numpy as np
from scipy.spatial import ConvexHull


def det(a, b, c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def dot(a, b):
    return sum((u*v for u, v in zip(a, b)), F(0))


def positive(x):
    return max(x, F(0))


def statement(alpha, lam):
    beta = 1-alpha
    q = F(2)+sum((positive(v-alpha)+positive(v-beta) for v in lam), F(0))
    return q, 2+6*q


def facet_support_ratio(alpha, lam):
    a, b, c = lam
    beta = 1-alpha
    points = [(F(0),F(0),F(0)), (F(1),F(0),F(0)),
              (F(0),F(1),F(0)), (b,c,alpha), (b,c,-beta)]
    normals = [(F(0),-alpha,c), (F(0),-beta,-c),
               (-alpha,F(0),b), (-beta,F(0),-b),
               (alpha,alpha,a), (beta,beta,-a)]
    # Twice facet areas times outward unit normals. The support of -K is
    # the negative minimum of the outward-normal functional on K.
    support = [max((-dot(v, n) for v in points)) for n in normals]
    # vol(K) = 1/6 after affine normalization; mixed volume = sum(h)/6.
    return sum(support, F(0))


def difference_body_ratio(alpha, lam):
    a,b,c=lam
    beta=1-alpha
    points=[(F(0),F(0),F(0)),(F(1),F(0),F(0)),
            (F(0),F(1),F(0)),(b,c,alpha),(b,c,-beta)]
    differences=sorted(set(tuple(x[i]-y[i] for i in range(3))
                           for x in points for y in points))
    hull=ConvexHull(np.asarray(differences,dtype=float))
    # The origin is interior to K-K; every boundary triangle with the
    # origin forms a disjoint pyramid (up to common faces). The determinant
    # arithmetic below is exact, although facet discovery is numerical.
    vol=sum((abs(det(*[differences[int(i)] for i in face]))
             for face in hull.simplices),F(0))/6
    return 6*vol  # vol(K) = 1/6.


def main():
    tests=[(F(1,2),(F(1,3),)*3),
           (F(1,5),(F(1,3),)*3),
           (F(1,2),(F(1,10),F(4,5),F(1,10))),
           (F(1,4),(F(1,2),F(1,4),F(1,4))),
           (F(1,2),(F(1,4),F(1,4),F(1,2))),
           (F(1,3),(F(1,3),)*3),
           (F(2,3),(F(1,3),)*3)]
    rng=Random(26071017)
    for _ in range(240):
        h=F(rng.randrange(1,43),43)
        a=F(rng.randrange(1,53),53)
        b=F(rng.randrange(1,53),53)*(1-a)
        lam=(a,b,1-a-b)
        tests.append((h,lam))
    facet_checks=0
    for alpha,lam in tests:
        q,r=statement(alpha,lam)
        assert F(2)<=q<F(3), (alpha,lam,q)
        assert facet_support_ratio(alpha,lam)==q, (alpha,lam,'facet')
        facet_checks+=1
        assert difference_body_ratio(alpha,lam)==r, (alpha,lam,'hull')
    # Sharp plateau and fixed-height minima across exact rational samples.
    assert statement(F(1,2),(F(2,5),F(2,5),F(1,5)))==(F(2),F(14))
    assert statement(F(1,3),(F(1,3),)*3)==(F(2),F(14))
    assert statement(F(1,4),(F(1,3),)*3)==(F(9,4),F(31,2))
    print('BIPYRAMID_GODBERSEN_VERIFY_OK cases=%d exact_facet=%d exact_hull=%d' %
          (len(tests),facet_checks,len(tests)))


if __name__=='__main__':
    main()
