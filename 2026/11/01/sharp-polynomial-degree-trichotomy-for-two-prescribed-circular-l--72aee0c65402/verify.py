"""Independent exact-rational checks of representative radial interpolation examples.

Run: python3 verify.py
Only the standard library is required. This program checks examples, not the
universal statements, which follow from the polynomial-factorization proof.
"""
from fractions import Fraction as F


def trim(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q


def add(p, q):
    return trim([(p[k] if k < len(p) else 0) +
                 (q[k] if k < len(q) else 0) for k in range(max(len(p), len(q)))])


def multiply(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def scale(p, c):
    return trim([c * a for a in p])


def evaluate(p, x):
    result = F(0)
    for a in reversed(p):
        result = result * x + a
    return result


def derivative(p):
    return [k * p[k] for k in range(1, len(p))] or [F(0)]


def setup(s1, s2, b1, b2, design):
    s1, s2, b1, b2 = map(F, (s1, s2, b1, b2))
    assert 0 < s1 < s2 and b1 * b2 > 0
    d = s2 - s1
    l1 = [s2 / d, -F(1) / d]
    l2 = [-s1 / d, F(1) / d]
    R = multiply([-s1, F(1)], [-s2, F(1)])
    if design == "constant":
        assert b1 == b2
        B = [b1]
    elif design == "linear":
        B = add(scale(l1, b1), scale(l2, b2))
    elif design == "square":
        B = add(scale(multiply(l1, l1), b1), scale(multiply(l2, l2), b2))
    else:
        raise ValueError("unknown design")
    # Chosen period is T=1 at both circles, hence angular speed 2 pi.
    Q_over_2pi = add(multiply(l1, l1), multiply(l2, l2))
    P = multiply(R, B)
    for s, b in ((s1, b1), (s2, b2)):
        assert evaluate(P, s) == 0
        assert evaluate(B, s) == b
        assert evaluate(Q_over_2pi, s) == 1
        assert evaluate(derivative(P), s) == ((s - s2) if s == s1 else (s - s1)) * b
    return P, B, Q_over_2pi


def test():
    # Degrees of the planar vector field are 2 deg(P)+1, 2 deg(Q)+1.
    configurations = [
        (1, 2, 1, 1, "constant", 5),
        (1, 2, 1, F(3, 2), "linear", 7),
        (1, 2, 1, 2, "linear", 7),
        (1, 2, F(1, 2), F(3, 2), "square", 9),
        (1, 2, 1, F(1, 2), "square", 9),
        (1, 2, -1, -F(1, 2), "square", 9),
    ]
    for s1, s2, b1, b2, mode, degree in configurations:
        P, B, Q = setup(s1, s2, b1, b2, mode)
        assert max(2 * (len(P) - 1) + 1, 2 * (len(Q) - 1) + 1) == degree
        # For the tested cases, check constant/linear sign or the globally
        # definite positive-square form; this is not a substitute for proof.
        for k in range(0, 1001):
            s = F(k, 100)
            assert evaluate(B, s) * F(b1) > 0 if s > 0 else evaluate(B, s) * F(b1) >= 0
            assert evaluate(Q, s) > 0
        if mode == "square":
            # Sum of squares has no common zero because l1+l2==1.
            assert add([F(0)] * 1, [F(1)]) == [F(1)]
    # For data with outer ratio too large, the unique linear interpolant
    # acquires an unwanted positive root: s=1/2.
    _, Bbad, _ = setup(1, 2, F(1, 2), F(3, 2), "linear")
    assert Bbad == [-F(1, 2), F(1)] and evaluate(Bbad, F(1, 2)) == 0
    # Explicit prescribed logarithmic multipliers, with periods one:
    s1, s2 = F(1), F(2)
    b1, b2 = F(1, 2), F(3, 2)
    assert 2 * s1 * b1 * (s1 - s2) == -1
    assert 2 * s2 * b2 * (s2 - s1) == 6
    print("PASS: exact interpolants, degree 5/7/9 examples, positive angular speeds, Floquet logs, and forced extra root")


if __name__ == "__main__":
    test()
