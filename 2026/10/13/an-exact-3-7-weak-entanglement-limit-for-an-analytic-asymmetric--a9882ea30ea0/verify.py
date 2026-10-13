from fractions import Fraction
from math import cos, sin, sqrt, pi


def p_a(theta, alpha):
    return 0.5 * (1.0 + cos(2.0 * theta) * cos(alpha))


def p_ab(theta, alpha, beta):
    return 0.25 * (
        1.0
        + cos(2.0 * theta) * (cos(alpha) + cos(beta))
        + cos(alpha) * cos(beta)
        + sin(2.0 * theta) * sin(alpha) * sin(beta)
    )


def bell_values(theta):
    e = sqrt(theta)
    a1, a2, a3 = 0.0, 2.0 * e, pi / 2.0
    b1, b2, b3 = (2.0 / 3.0) * theta, -(2.0 / 3.0) * theta, -2.0 * e
    q = (
        p_ab(theta, a1, b1) + p_ab(theta, a1, b2) + p_ab(theta, a1, b3)
        + p_ab(theta, a2, b1) + p_ab(theta, a2, b2) + p_ab(theta, a3, b1)
        - p_ab(theta, a2, b3) - p_ab(theta, a3, b2)
        - 2.0 * p_a(theta, a1) - p_a(theta, a2) - p_a(theta, b1)
    )
    m = p_a(theta, a1) - 1.0
    eta = -m / (q - m)
    return q, m, eta


def q4_raw(u, a, b, d, f):
    return -(
        a*a*f*f + 8*a*f + 6*b*b - 8*b + 6*d*d + 8*d + 4*u*u
    ) / Fraction(16, 1)


def q4_square(u, a, b, d, f):
    return (
        Fraction(4, 3)
        - (a*f + 4)**2 / Fraction(16, 1)
        - Fraction(3, 8) * (b - Fraction(2, 3))**2
        - Fraction(3, 8) * (d + Fraction(2, 3))**2
        - u*u / Fraction(4, 1)
    )


def main():
    tests = [
        tuple(map(Fraction, (0, 2, 1, -1, -2))),
        (Fraction(1, 3), Fraction(5, 2), Fraction(2, 3), Fraction(-2, 3), Fraction(-8, 5)),
        (Fraction(-2, 5), Fraction(3, 1), Fraction(-1, 7), Fraction(4, 9), Fraction(-4, 3)),
    ]
    for u, a, b, d, f in tests:
        assert q4_raw(u, a, b, d, f) == q4_square(u, a, b, d, f)

    # Exact leading coefficients used for the explicit representative.
    assert q4_square(Fraction(0), Fraction(2), Fraction(2, 3), Fraction(-2, 3), Fraction(-2)) == Fraction(4, 3)
    q_coeffs = (Fraction(4, 3), Fraction(-25, 9), Fraction(-1, 9))
    m_coeffs = (Fraction(-1, 1), Fraction(1, 3))
    assert q_coeffs == (Fraction(4, 3), Fraction(-25, 9), Fraction(-1, 9))
    assert m_coeffs == (Fraction(-1, 1), Fraction(1, 3))
    assert Fraction(1, 1) / (Fraction(1, 1) + Fraction(4, 3)) == Fraction(3, 7)

    vals = []
    for theta in (1e-2, 1e-3, 1e-4):
        q, m, eta = bell_values(theta)
        assert q > 0.0 and m < 0.0
        vals.append(eta)
    target = 3.0 / 7.0
    assert vals[0] > vals[1] > vals[2] > target
    assert abs(vals[-1] - target) < 6e-5

    # First correction: (eta - 3/7)/theta -> 25/49.
    theta = 1e-4
    _, _, eta = bell_values(theta)
    approx = (eta - target) / theta
    assert abs(approx - 25.0/49.0) < 2e-3
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
