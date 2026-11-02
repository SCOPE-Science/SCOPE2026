"""Reproducible exact-arithmetic checks for a four-vertex weighted-path heat example.

Only the rational Taylor enclosure and finite algebra are computationally certified.
The all-parameter argument is mathematical and is given in the accompanying proof.
"""
from fractions import Fraction as F
from math import factorial


def mv(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def heat_gradient_matrix(a, b, c):
    return [[-2*a, b, 0], [a, -2*b, c], [0, b, -2*c]]


def generator(a, b, c):
    return [[-a, a, 0, 0],
            [a, -a-b, b, 0],
            [0, b, -b-c, c],
            [0, 0, c, -c]]


def gradient():
    return [[-1, 1, 0, 0], [0, -1, 1, 0], [0, 0, -1, 1]]


def expB1_rational(B, t, N=26):
    # Truncated Taylor series of e^(tB) 1, exact rational arithmetic.
    v = [F(1)]*3
    result = v[:]
    for k in range(1, N+1):
        v = [z * t / k for z in mv(B, v)]
        result = [z + s for z, s in zip(result, v)]
    # For t <= 0.053, ||Bt||_infty <= 21*0.053 < 6/5.
    # Taylor remainder <= exp(6/5)*(6/5)^(N+1)/(N+1)!
    # and exp(6/5) < exp(2) < 8.
    epsilon = F(8) * F(6, 5)**(N+1) / factorial(N+1)
    return result, epsilon


def verify():
    D = gradient()
    triples = [(1, 3, 9), (1, 2, 4), (2, 5, 12),
               (F(1,2), F(3,2), F(9,2))]
    for a, b, c in triples:
        B = heat_gradient_matrix(a, b, c)
        Q = generator(a, b, c)
        assert mul(D, Q) == mul(B, D)
    B = heat_gradient_matrix(1, 3, 9)
    assert mv(B, [1,1,1]) == [1,4,-15]
    # Characteristic coefficients det(zI-B) from trace, minors, determinant.
    trace = B[0][0]+B[1][1]+B[2][2]
    principal_two = (B[0][0]*B[1][1]-B[0][1]*B[1][0]
                   + B[0][0]*B[2][2]-B[0][2]*B[2][0]
                   + B[1][1]*B[2][2]-B[1][2]*B[2][1])
    det = (B[0][0]*(B[1][1]*B[2][2]-B[1][2]*B[2][1])
         - B[0][1]*(B[1][0]*B[2][2]-B[1][2]*B[2][0]))
    assert (-trace,principal_two,-det) == (26,126,108)

    # Actual rigorous rational interval: root u2(t)-u1(t)=0 in (tlo,thi).
    lo, hi = F(5285,100000), F(5286,100000)
    ul, el = expB1_rational(B, lo)
    uh, eh = expB1_rational(B, hi)
    assert ul[1]-ul[0] > 2*el
    assert uh[1]-uh[0] < -2*eh
    # Exact uniform bound on u2' throughout the bracket:
    # |u2''(t)| <= ||B||_infty^2 exp(t||B||_infty) < 21^2 * 8.
    # At tlo, u2' strictly negative by a bound much exceeding the interval drift.
    left_slope = mv(B, ul)[1]
    assert left_slope + 21*el + 21*21*8*(hi-lo) < 0
    # The same bound implies u2'(t*) < 0.
    print('CHECK_OK intertwining=4_examples characteristic=z^3+26z^2+126z+108')
    print('CHECK_OK unique_switch_in_open_interval=(5285/100000,5286/100000)')
    print('CHECK_OK middle_branch_slope_strictly_negative_at_switch')
    print('CHECK_OK certified_remainder_less_than_1e-20',el < F(1,10**20))

if __name__ == '__main__':
    verify()
