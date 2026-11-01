#!/usr/bin/env python3
"""Exact rational checks and finite spot tests for switched Abel flows.

The general two-root theorem is proved algebraically in RESULT.md; finite
checks here are corroborative, not a proof for every parameter.
"""
from fractions import Fraction as F
from math import isqrt, sqrt, isclose
from itertools import product


def perfect_square_root(q):
    n, d = q.numerator, q.denominator
    assert n >= 0 and d > 0
    a, b = isqrt(n), isqrt(d)
    assert a*a == n and b*b == d, (q, a, b)
    return F(a, b)


def exact_stages(y, b, a, c, d):
    y1 = y-b
    assert y1 > 0
    y2 = perfect_square_root(y1*y1-2*a)
    assert y2 > 0
    y3 = y2-c
    assert y3 > 0
    y4 = perfect_square_root(y3*y3-2*d)
    assert y4 > 0
    multiplier = (y1/y2)*(y3/y4)
    return (y, y1, y2, y3, y4), multiplier


def algebraic_quadratic(y, b, a, c, d):
    k = (b*b-2*a+c*c-2*d)/(2*c)
    return (k - (b/c)*y)**2 - ((y-b)**2-2*a)


def numeric_return(y, b, a, c, d):
    y1=y-b
    if y1<=0:return None
    z1=y1*y1-2*a
    if z1<=0:return None
    y2=sqrt(z1)
    y3=y2-c
    if y3<=0:return None
    z2=y3*y3-2*d
    if z2<=0:return None
    return sqrt(z2)


def main():
    b,a,c,d = F(-1),F(-5),F(2),F(1)
    checks=0
    expected=[
        (F(1,2), (F(1,2),F(3,2),F(7,2),F(3,2),F(1,2)), F(9,7)),
        (F(7,6), (F(7,6),F(13,6),F(23,6),F(11,6),F(7,6)), F(143,161)),
    ]
    for y, stages, multiplier in expected:
        obs, mult=exact_stages(y,b,a,c,d)
        assert obs == stages
        assert mult == multiplier
        assert obs[-1]==obs[0]
        assert algebraic_quadratic(y,b,a,c,d)==0
        checks+=4
    assert expected[0][2]>1 and 0<expected[1][2]<1
    checks+=1
    # Explicit polynomial: (k+(y/2))^2-((y+1)^2+10) =
    # -(2y-1)(6y-7)/16; denominator 16.
    for y in [F(-2),F(-1),F(0),F(1,4),F(1,2),F(7,6),F(2),F(4)]:
        assert algebraic_quadratic(y,b,a,c,d) == -((2*y-1)*(6*y-7))/16
        checks+=1
    # Verify squaring relation for arbitrary rational positive orbit-stage
    # domains. These are finite tests of the underlying algebra, not
    # enumeration of all fixed points.
    for ib,ia,ic,id_ in product((-2,-1,1,2),(-3,-1,1,3),(-2,-1,1,2),(-3,-1,1,3)):
        B,A,C,D = map(F,(ib,ia,ic,id_))
        for Y in (F(1,2),F(1),F(2),F(5)):
            y1=Y-B
            if y1<=0 or y1*y1-2*A<=0:continue
            s=sqrt(float(y1*y1-2*A))
            y3=s-float(C)
            if y3<=0 or y3*y3-2*float(D)<=0:continue
            p=sqrt(y3*y3-2*float(D))
            discrepancy=2*float(C)*s +2*float(B)*Y - float(B*B-2*A+C*C-2*D)
            assert isclose(discrepancy, float(Y*Y)-p*p,abs_tol=1e-9,rel_tol=1e-9)
            checks+=1
    print('PASS; assertions:',checks)
    print('positive period-four-time initial x-values:', '2', '6/7')
    print('Floquet multipliers:', '9/7', '143/161')


if __name__=='__main__': main()
