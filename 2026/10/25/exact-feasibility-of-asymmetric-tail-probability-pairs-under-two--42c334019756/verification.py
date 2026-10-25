from fractions import Fraction as F


def minimum_second_moment(u, v, a, b):
    """Return (closed-interval infimum, attained) or None if means are infeasible."""
    u, v, a, b = map(F, (u, v, a, b))
    c = 1 - a - b
    if u <= 0 or v <= 0 or a < 0 or b < 0 or c < 0:
        raise ValueError("Require u,v>0 and a,b>=0 with a+b<=1.")
    if a == 0 and b == 0:
        return None
    if c == 0:
        if a == 0 or b == 0:
            return None
        return max(a * u * u / b, b * v * v / a), True
    if a == 0:
        if b >= u / (u + v):
            return None
        return b * v * v / c, True
    if b == 0:
        if a >= v / (u + v):
            return None
        return a * u * u / c, True

    r, s = u / (u + v), v / (u + v)
    if b <= r and a <= s:
        m = a * u * u + b * v * v + (a * u - b * v) ** 2 / c
        return m, (b < r and a < s)
    if b > r:
        x = (c * u - b * v) / a
        return a * x * x + b * v * v + c * u * u, False
    if a > s:
        y = (a * u - c * v) / b
        return a * u * u + b * y * y + c * v * v, False
    raise AssertionError("The parameter cases should be exhaustive.")


def feasible(u, v, a, b):
    u, v, a, b = map(F, (u, v, a, b))
    c = 1 - a - b
    if u <= 0 or v <= 0 or a < 0 or b < 0 or c < 0:
        return False
    if a == 0 and b == 0:
        return u * v > 1
    result = minimum_second_moment(u, v, a, b)
    if result is None:
        return False
    m, attained = result
    return m < 1 or (m == 1 and attained)


def moments(atoms):
    mass = sum((p for x, p in atoms), F(0))
    mean = sum((x * p for x, p in atoms), F(0))
    second = sum((x * x * p for x, p in atoms), F(0))
    return mass, mean, second


def verify_witness(atoms, u, v, expected_a, expected_b):
    mass, mean, second = moments(atoms)
    a = sum((p for x, p in atoms if x <= -F(u)), F(0))
    b = sum((p for x, p in atoms if x >= F(v)), F(0))
    assert (mass, mean, second) == (F(1), F(0), F(1))
    assert (a, b) == (F(expected_a), F(expected_b))


def main():
    # Exact witness laws for the no-tail, one-tail, two-tail, and interior cases.
    verify_witness(
        [(F(-3, 2), F(4, 13)), (F(2, 3), F(9, 13))],
        2, 1, 0, 0
    )
    verify_witness(
        [(F(1), F(1, 5)), (F(7, 2), F(1, 20)), (F(-1, 2), F(3, 4))],
        2, 1, 0, F(1, 4)
    )
    verify_witness(
        [(F(-1), F(1, 2)), (F(1), F(1, 2))],
        1, 1, F(1, 2), F(1, 2)
    )
    verify_witness(
        [(F(-2), F(1, 8)), (F(0), F(3, 4)), (F(2), F(1, 8))],
        2, 2, F(1, 8), F(1, 8)
    )

    # The three positive-mass minimization regimes are checked exactly.
    assert minimum_second_moment(2, 2, F(1, 8), F(1, 8)) == (F(1), True)
    assert minimum_second_moment(1, 2, F(1, 5), F(1, 2)) == (F(19, 4), False)
    assert minimum_second_moment(2, 1, F(3, 4), F(1, 10)) == (F(171, 8), False)
    assert minimum_second_moment(1, 1, F(1, 2), F(1, 4)) == (F(1), False)

    # Boundary and feasibility predicates; these are spot checks, not the proof.
    checks = [
        feasible(2, 1, 0, 0),
        not feasible(1, 1, 0, 0),
        feasible(2, 1, 0, F(1, 4)),
        not feasible(1, 1, 0, F(1, 2)),
        feasible(1, 1, F(1, 2), F(1, 2)),
        feasible(2, 2, F(1, 8), F(1, 8)),
        not feasible(1, 1, F(1, 2), F(1, 4)),
        not feasible(1, 1, F(3, 4), F(1, 2)),
    ]
    assert all(checks)
    print("PASS: 4 exact witness laws, 4 exact minimization-regime checks, and 8 boundary/feasibility predicates.")


if __name__ == "__main__":
    main()
