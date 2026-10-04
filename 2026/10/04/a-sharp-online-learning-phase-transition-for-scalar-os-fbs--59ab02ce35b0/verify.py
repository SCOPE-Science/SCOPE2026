from fractions import Fraction as Q


def proj(v, lo, hi):
    return min(max(v, lo), hi)


def step_p(p, s, theta):
    pstar = Q(1, 1) / s
    rho = Q(1, 1) - theta
    lo = Q(1, 1)
    hi = Q(2, 1) / s - Q(1, 1)
    return proj(pstar + rho * (p - pstar), lo, hi)


def step_x(x, p, s):
    return (Q(1, 1) - s * p) * x


def feedback_direct(x, p, a, s):
    F = lambda z: a * (Q(1, 1) - s) * z * z / Q(2, 1)
    d = s * x
    return (F((Q(1, 1) - s * p) * x) - F(x)) / (d * d)


def feedback_closed(p, a, s):
    return a * (Q(1, 1) - s) * (p * p - Q(2, 1) * p / s) / Q(2, 1)


def check_case(s, a, theta, steps=10):
    assert Q(0) < s < Q(1)
    pstar = Q(1, 1) / s
    hi = Q(2, 1) / s - Q(1, 1)
    p = Q(1, 1)
    x = Q(7, 5)
    x0 = x

    # Feedback identity on a nontrivial exact point.
    assert feedback_direct(Q(5, 3), Q(7, 4), a, s) == feedback_closed(Q(7, 4), a, s)

    rho = Q(1, 1) - theta
    for k in range(steps):
        # Every candidate p in this orbit lies in the set and every probe contracts.
        assert Q(1, 1) <= p <= hi
        q = Q(1, 1) - s * p
        assert abs(q) <= Q(1, 1) - s < Q(1, 1)

        if Q(0) < theta < Q(2) and theta != Q(1):
            p_formula = pstar + (rho ** k) * (Q(1, 1) - pstar)
            x_formula = x0 * ((Q(1, 1) - s) ** k) * (rho ** (k * (k - 1) // 2))
            assert p == p_formula
            assert x == x_formula
        elif theta >= Q(2):
            assert p == (Q(1, 1) if k % 2 == 0 else hi)
            assert abs(x) == abs(x0) * ((Q(1, 1) - s) ** k)

        x = step_x(x, p, s)
        p = step_p(p, s, theta)

    if theta == Q(1):
        p = Q(1, 1)
        x = x0
        x = step_x(x, p, s)
        p = step_p(p, s, theta)
        assert p == pstar
        x = step_x(x, p, s)
        assert x == 0


def main():
    s = Q(2, 5)
    a = Q(7, 3)
    for theta in [Q(1, 2), Q(1), Q(3, 2), Q(2), Q(5, 2), Q(4)]:
        check_case(s, a, theta)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
