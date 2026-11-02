#!/usr/bin/env python3
"""Exact finite checks of the three-class environmental-invasion calculation.

The analytical proof, not this test grid, establishes the infinite-parameter theorem.
Requires Python 3 standard library only.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
from itertools import product


def det3(x):
    return (x[0][0] * (x[1][1]*x[2][2]-x[1][2]*x[2][1])
            - x[0][1] * (x[1][0]*x[2][2]-x[1][2]*x[2][0])
            + x[0][2] * (x[1][0]*x[2][1]-x[1][1]*x[2][0]))


def trial(a, z, d, eps, delta, b):
    matrix = [[-(a+z+eps), (1-delta)*b, b],
              [eps, -d+delta*b, Q(0)],
              [a, a+d, -(z+b)]]
    q = a+z
    t = b*(b+q)
    h = eps*(t-d*z)+z*(b+q)*(delta*b-d)
    c = (a+z+eps)*(z+b)-a*b
    k = b*((1-delta)*(z+b)+a+d)/c
    zz = (a*k+a+d)/(z+b)
    assert c > 0 and k > 0 and zz > 0
    assert det3(matrix) == h
    assert sum(matrix[0][j] * [k,Q(1),zz][j] for j in range(3)) == 0
    assert sum(matrix[2][j] * [k,Q(1),zz][j] for j in range(3)) == 0
    assert sum(matrix[1][j] * [k,Q(1),zz][j] for j in range(3)) == eps*k+delta*b-d
    assert c*(eps*k+delta*b-d) == h
    if delta*b < d and t > d*z:
        ecrit = z*(b+q)*(d-delta*b)/(t-d*z)
        assert ecrit > 0
        assert (h > 0) == (eps > ecrit)
        assert (h == 0) == (eps == ecrit)
    if delta*b >= d:
        assert h > 0
    return h


def main():
    rates = [Q(1,3), Q(1), Q(5,2)]
    ratios = [Q(0), Q(1,2), Q(1)]
    checks = 0
    for a, z, d, eps, delta, b in product(rates,rates,rates,rates,ratios,rates):
        trial(a,z,d,eps,delta,b)
        checks += 1
    a=z=d=Q(1)
    assert trial(a,z,d,Q(1,2),Q(0),Q(2)) < 0
    assert trial(a,z,d,Q(1,2),Q(0),Q(3)) > 0
    assert trial(a,z,d,Q(3,4),Q(1,2),Q(1)) == 0
    q = 2.0
    floor = (sqrt(q*q+4)-q)/2
    assert isclose(floor,sqrt(2)-1,rel_tol=1e-14)
    bstar = sqrt(5)
    assert isclose(.5*(bstar*(bstar+2)-1)-(bstar+2),0,abs_tol=1e-12)
    for eps in [0.01,0.1,0.4,1.0,2.0,10.0,100.0]:
        # Purely environmental case: exact quadratic positive root.
        b = (-(2*eps-1)+sqrt((2*eps-1)**2+4*eps*(2+eps)))/(2*eps)
        assert b > floor
        assert abs((b+2)*(eps*b-1)-eps) < 5e-10
        assert 1/eps < b < 1/eps+eps
    print('PASS:',checks,'exact-rational determinant and positive-witness trials;')
    print('PASS: two exact threshold witnesses, singular bounds, limiting floor.')
    print('Finite checks do not prove the general theorem.')


if __name__ == '__main__':
    main()
