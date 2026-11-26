"""Exact finite checks for two-patch stationary occupancy and a separating example.

The parameter-uniform theorem is proved in RESULT.md.
"""

from fractions import Fraction as F
from itertools import product


def solve(matrix, rhs):
    a = [[F(z) for z in row] + [F(b)] for row, b in zip(matrix, rhs)]
    n = len(a)
    for column in range(n):
        pivot = next(i for i in range(column, n) if a[i][column])
        a[column], a[pivot] = a[pivot], a[column]
        leading = a[column][column]
        a[column] = [z / leading for z in a[column]]
        for i in range(n):
            if i != column:
                f = a[i][column]
                a[i] = [x - f*y for x, y in zip(a[i], a[column])]
    return [row[-1] for row in a]


def stationary(c, e, f, B, u):
    a, b = c+u, c+B-u
    generator = [[-2*c,c,c,0], [e,-e-a,0,a],
                 [f,0,-f-b,b], [0,f,e,-e-f]]
    p = solve([[row[i] for row in generator] for i in range(3)] + [[1]*4],
              [0,0,0,1])
    assert sum(p) == 1 and min(p) > 0
    return p[1]+p[2]+2*p[3], p[3]


def closed(c, e, f, B, u):
    L = B+2*c+e+f
    t, delta, g = u-B/2, f-e, e*f/c
    a = (B+2*c)*L/2
    D = a+L*(e+f+g)-delta*t-2*t*t
    return (L*L-4*t*t)/D, (a+delta*t-2*t*t)/D


def check():
    n = 0
    for c, e, f, B in product((F(1,2), F(1), F(3)), repeat=4):
        for share in (F(0), F(1,7), F(1,2), F(6,7), F(1)):
            u = B*share
            assert stationary(c,e,f,B,u) == closed(c,e,f,B,u)
            n += 1

    # At c=e=B=1, f=3, the derivative numerators in t=u-1/2
    # are 98-280t+8t^2 and 140-196t+8t^2, respectively.
    def WE(t):
        return 98-280*t+8*t*t

    def WP(t):
        return 140-196*t+8*t*t

    assert WE(F(0)) > 0 > WE(F(1,2))
    assert WP(F(1,2)) > 0
    assert WE(F(35,100)) > 0 > WE(F(36,100))

    # The smaller quadratic root is t=(280-sqrt(discriminant))/16,
    # so u=18-7*sqrt(6). Verify the radical simplification and the
    # bracket for u without a floating-point calculation.
    assert 280**2-4*8*98 == (16*7)**2*6
    assert (18-F(86,100))**2 < 7**2*6 < (18-F(85,100))**2

    def example(u):
        return stationary(F(1),F(1),F(3),F(1),u)

    assert example(F(1,2))[0] < example(F(17,20))[0] > example(F(1))[0]
    assert example(F(1))[1] > example(F(17,20))[1]
    print('PASS: exact rational stationary-distribution comparisons:', n)
    print('PASS: exact separated optimum checks for c=e=1, f=3, B=1')


if __name__ == '__main__':
    check()
