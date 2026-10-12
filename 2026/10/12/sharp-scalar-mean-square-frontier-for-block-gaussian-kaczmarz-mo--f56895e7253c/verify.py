"""Exact-rational checks for scalar Gaussian-block momentum identities.

Only the Python standard library is needed. This checks algebraic identities and
finite-sample recurrences, not an infinite-dimensional or machine proof.
"""
from fractions import Fraction as F
from itertools import permutations


def det(a):
    total = F(0)
    for ix in permutations(range(3)):
        inversions = sum(ix[i] > ix[j] for i in range(3) for j in range(i + 1, 3))
        term = F(-1 if inversions % 2 else 1)
        for i in range(3):
            term *= a[i][ix[i]]
        total += term
    return total


def matrix(p, alpha, omega):
    mu = 1 + omega - alpha
    return [[mu**2 + F(2, p) * alpha**2, omega**2, -2 * omega * mu],
            [F(1), F(0), F(0)],
            [mu, F(0), -omega]]


def characteristic(p, alpha, omega, z):
    a = matrix(p, alpha, omega)
    return det([[z * int(i == j) - a[i][j] for j in range(3)]
                for i in range(3)])


def coeff_at_r(p, omega):
    r = F(2, p + 2)
    constant = characteristic(p, F(0), omega, r)
    positive = characteristic(p, F(1), omega, r)
    negative = characteristic(p, F(-1), omega, r)
    quadratic = (positive + negative - 2 * constant) / 2
    linear = (positive - negative) / 2
    return quadratic, linear, constant


def assert_rational_identities():
    n = 0
    for p in range(1, 31):
        r = F(2, p + 2)
        for omega in [F(0), r / 2, r, (1 + r) / 2, F(1, 6), F(1, 3), F(1, 2), F(3, 4), F(9, 10)]:
            for alpha in [F(0), F(1, 20), F(1, 3), F(1, 2), F(2, 3), F(1), F(7, 4)]:
                got = characteristic(p, alpha, omega, F(1))
                expected = alpha * (2 * p * (1 - omega**2) - alpha * (p + 2 + (2 - p) * omega)) / p
                assert got == expected, (p, omega, alpha, got, expected)
                assert det(matrix(p, alpha, omega)) == omega**3
                n += 1
            qa, qb, qc = coeff_at_r(p, omega)
            expected_quad = -r * (2 + (2 - p) * omega) / p
            assert qa == expected_quad, (p, omega, qa, expected_quad)
            discriminant = qb * qb - 4 * qa * qc
            expected_disc = (F(8) * p * omega**2 * ((p + 2) * omega - 2) *
                             ((p + 2) * omega + 2) / (p + 2)**4)
            assert discriminant == expected_disc, (p, omega, discriminant, expected_disc)
            if F(0) < omega < r:
                assert qa < 0 and discriminant < 0
            if omega == r:
                assert qb == qc == 0 and qa < 0
    return n


def example():
    p, a, w = 1, F(1, 2), F(1, 2)
    critical = F(2 * p) * (1 - w * w) / (p + 2 + (2 - p) * w)
    assert critical == F(3, 7)
    assert a < F(2, 3) and a > critical
    assert characteristic(p, a, w, F(1)) < 0  # root above 1
    M = matrix(p, a, w)
    moment = [F(1), F(1), F(1)]
    seq = []
    for _ in range(8):
        seq.append(moment[0])
        moment = [sum(M[i][j] * moment[j] for j in range(3)) for i in range(3)]
    assert seq == [F(1), F(3, 4), F(7, 8), F(1), F(35, 32),
                   F(77, 64), F(85, 64), F(375, 256)]
    lo, hi = 1., 2.
    assert characteristic(p, a, w, F(1)) < 0 < characteristic(p, a, w, F(2))
    for _ in range(70):
        mid = (lo + hi) / 2
        if float(characteristic(p, a, w, F(mid))) < 0:
            lo = mid
        else:
            hi = mid
    root = (lo + hi) / 2
    assert abs(root - 1.1027847152002952) < 1e-11
    # For these parameters E[e_{t+1}]=E[e_t]-E[e_{t-1}]/2,
    # characteristic roots have modulus 1/sqrt(2).
    return seq


def main():
    n = assert_rational_identities()
    seq = example()
    print('PASS:', n, 'exact determinant checks; discriminant and leading-coefficient identities')
    print('PASS: rank-one block-width examples and eight exact rational second moments')
    print('example S_t:', ', '.join(str(z) for z in seq))
    print('This finite verifier supports but does not replace the analytic proof.')


if __name__ == '__main__':
    main()
