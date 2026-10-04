from fractions import Fraction


def P(n, coeffs):
    a3, a2, a1, a0 = coeffs
    return a3*n**3 + a2*n**2 + a1*n + a0


def s(n, coeffs):
    a3, a2, a1, a0 = map(Fraction, coeffs)
    n = Fraction(n)
    return (
        a3*n**4/Fraction(2)
        + (Fraction(2)*a2/Fraction(3)-a3)*n**3
        + (a1-a2+a3/Fraction(2))*n**2
        + (Fraction(2)*a0-a1+a2/Fraction(3))*n
    )


def recurrence_values(r, coeffs, c, N):
    c = Fraction(c)
    u = [Fraction(1), Fraction(P(0, coeffs))]
    for n in range(1, N):
        nxt = (Fraction(P(n, coeffs))*u[n] - c*Fraction(n**r)*u[n-1]) / Fraction((n+1)**r)
        u.append(nxt)
    return u


def check_case(r, coeffs, c):
    c = Fraction(c)
    for n in range(0, 13):
        assert s(n+1, coeffs) - s(n, coeffs) == 2*P(n, coeffs)
    for N in range(1, 13):
        u = recurrence_values(r, coeffs, c, N)
        lhs = Fraction(0)
        for n in range(N):
            W = -c*Fraction((n+1)**(2*r)) + c*Fraction(n**(2*r)) - Fraction(P(n, coeffs))**2 - s(n, coeffs)*P(n, coeffs)
            lhs += W*u[n]**2 / ((-c)**n)
        rhs = (
            Fraction(N**(2*r))*u[N]**2
            - c*Fraction(N**(2*r))*u[N-1]**2
            - Fraction(N**r)*s(N, coeffs)*u[N]*u[N-1]
        ) / ((-c)**(N-1))
        assert lhs == rhs, (r, coeffs, c, N, lhs, rhs)


cases = [
    (1, (1, 2, 0, 1), 1),
    (2, (0, 11, 11, 3), -1),
    (2, (0, 7, 7, 2), -8),
    (3, (5, 27, 51, 34), 1),
    (3, (-3, -7, -21, -14), 81),
    (4, (2, 1, -3, 2), -5),
]
for case in cases:
    check_case(*case)

print("VERIFY_OK finite_difference=exact cases=6 r=1..4 N=1..12 rational_replay=exact")
