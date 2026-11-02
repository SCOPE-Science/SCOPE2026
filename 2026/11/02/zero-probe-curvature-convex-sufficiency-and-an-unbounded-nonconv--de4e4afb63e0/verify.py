"""Exact rational checks for SQP probe-blindness and convex sufficiency witness.
Run with Python 3, no third-party dependencies.
This is supporting arithmetic, not a substitute for the quantified proof.
"""
from fractions import Fraction as F


def q(x, y, r, m):
    return ((x-r)**2 + (y-m)**2) / 2


def c(x, y):
    return y * (1-x)


def neglected(x, y):
    return -x*y


def grad_quadratic_constraint(x, y):
    return -y, 1-x


def check_case(r, m):
    assert r > 1 and m > 0
    # Exact minimizer of the affine SQP constraint y <= 0.
    xL, yL = r, F(0)
    # Exact unconstrained minimizer, feasible for the quadratic model.
    xQ, yQ = r, m
    assert c(0, 0) == 0
    assert c(xL, yL) == 0
    assert neglected(xL, yL) == 0
    assert c(xQ, yQ) == m*(1-r) < 0
    assert q(xL, yL, r, m) == m*m/2
    assert q(xQ, yQ, r, m) == 0
    # SQP objective gradient at dL is (0,-m).
    # Quadratic-model active-constraint gradient is (0,1-r).
    # Stationarity requires multiplier m/(1-r), which is negative.
    assert m/(1-r) < 0
    # There is an explicit feasible descent ray from the SQP point.
    delta = min(m, F(1, 4))
    assert c(r, delta) < 0
    assert q(r, delta, r, m) < q(r, 0, r, m)
    # Hessian of c has eigenvalues +1 and -1; ||H||_2=1.
    assert grad_quadratic_constraint(r, 0) == (0, 1-r)


count = 0
for numerator in range(2, 51):
    for denominator in (1, 2, 3, 7):
        r = F(numerator, denominator)
        if r <= 1:
            continue
        for n in range(1, 30):
            for d in (1, 2, 11):
                check_case(r, F(n, d))
                count += 1

# Explicit convex quadratic counterpart: y <= 0 versus y + y^2/2 <= 0.
# The linearized solution (r,0) lies in both feasible sets and remains optimal.
for r in (F(1), F(3, 2), F(9, 4)):
    for m in (F(1), F(7, 3), F(100)):
        assert q(r, 0, r, m) == m*m/2
        assert 0 + 0**2/F(2) <= 0
        # Globally convex correction y^2/2 is nonnegative,
        # so every quadratic-feasible point satisfies y <= 0.
        for y_n in range(-30, 31):
            y = F(y_n, 10)
            if y + y*y/2 <= 0:
                assert y <= 0
                assert q(r, y, r, m) >= q(r, 0, r, m)

print(f"PASS: {count} nonconvex exact-rational witness cases; 9 convex control cases")
