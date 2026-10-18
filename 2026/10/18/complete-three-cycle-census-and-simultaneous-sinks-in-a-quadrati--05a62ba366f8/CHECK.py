"""Exact rational checks for the three-cycle classification witness.

Uses only Python standard library. Infinite-parameter exhaustion is analytic.
"""
from fractions import Fraction as Q
from itertools import permutations


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def jac(y, z, a):
    d = y * y - z * z
    return [[Q(0), Q(1)], [4 * a * y * d, -4 * a * z * d]]


def trdet(M):
    return M[0][0] + M[1][1], M[0][0] * M[1][1] - M[0][1] * M[1][0]


def return_trdet(A, B, C, a):
    return trdet(matmul(jac(C, A, a), matmul(jac(B, C, a), jac(A, B, a))))


def recurrence(A, B, C, a, nu):
    return (C == nu + a * (A * A - B * B) ** 2
            and A == nu + a * (B * B - C * C) ** 2
            and B == nu + a * (C * C - A * A) ** 2)


def conditions(trace, determinant):
    return 1-trace+determinant, 1+trace+determinant, 1-determinant


def main():
    checks = 0
    def check(test, message):
        nonlocal checks
        checks += 1
        assert test, message

    a = Q(6331625, 4572288)
    nu = Q(-1)
    A, B, C = Q(-183, 185), Q(57, 185), Q(3, 37)
    check(len({A, B, C}) == 3, 'distinct triple')
    check(a > Q(125, 96), 'five-cycle regime')
    check(A + B + C == Q(3, 5) * nu, 'sum')
    check(A * B + B * C + C * A == -Q(9, 25) * nu * nu, 'pair products')
    check(A * B * C == -Q(27, 125) * nu**3 - 1 / (3*a), 'triple product')

    for t in permutations((A, B, C)):
        check(recurrence(*t, a, nu), f'ordered triple {t}')
    check(return_trdet(A, B, C, a) == (Q(-67853, 250047), Q(-318725, 1000188)),
          'first exact return spectrum')
    check(return_trdet(A, C, B, a) == (Q(183019, 500094), Q(318725, 1000188)),
          'reversed exact return spectrum')
    for orient, expected in (
            ((A, B, C), (Q(15125, 15876), Q(410051, 1000188), Q(1318913, 1000188))),
            ((A, C, B), (Q(15125, 15876), Q(1684951, 1000188), Q(681463, 1000188)))):
        actual = conditions(*return_trdet(*orient, a))
        check(actual == expected, 'three exact Jury inequalities')
        for value in actual:
            check(value > 0, 'hyperbolic sink condition')

    # Two-equal cycles at the first and second exact parameter boundaries.
    for a0, s0 in ((Q(27,32), Q(-1,3)), (Q(125,96), Q(1,5))):
        check(a0 * (s0 + 1) * (s0 - 1)**2 == 1, 'canonical root at critical')
        check(recurrence(nu, s0, s0, a0, nu), 'critical period-three return')
        check(Q(16)*s0**2/(s0+nu)**2 == 1, 'critical unit multiplier')
        check(return_trdet(nu, s0, s0, a0) == (Q(1), Q(0)), 'return spectrum boundary')

    # At a = 1, nu = -1, canonical s = 0 has two zero planar return multipliers.
    check(recurrence(Q(-1), Q(0), Q(0), Q(1), Q(-1)), 'superattracting canonical orbit')
    check(return_trdet(Q(-1), Q(0), Q(0), Q(1)) == (Q(0),Q(0)), 'double zero')

    # Check finite nearby rational examples on both sides of each root-count transition
    # by exact signs of the canonical cubic at its stationary critical points.
    for k, above_fold, above_distinct in ((Q(1,2), False, False),
                                           (Q(27,32), False, False),
                                           (Q(1), True, False),
                                           (Q(125,96), True, False),
                                           (Q(3,2), True, True)):
        fmax = Q(32,27)-1/k
        check((fmax > 0) == above_fold, 'canonical fold sign')
        discr_numer = Q(96)*k-Q(125)
        check((discr_numer > 0) == above_distinct, 'all-distinct discriminant sign')
    print('PASS: exact rational checks =', checks)


if __name__ == '__main__':
    main()
