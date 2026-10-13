#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt, isclose

def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

def poly_add(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out

# Exact polynomial identity behind the global lower bound.
left = poly_add(poly_mul([0, 0, 1], [-1, 1]), [4, 0, -2])
right = poly_mul(poly_mul([-2, 1], [-2, 1]), [1, 1])
assert left == right == [4, 0, -3, 1]

# Consistency checks for the cleared-denominator eigenvalue identities.
for theta, t in [(0.1, 0.5), (0.4, 2.0), (1/sqrt(2), 2*sqrt(2)), (0.9, 7.0)]:
    D = theta*t*t + (2*theta*theta + 1)*t + 2*theta
    l1 = (1 - 2*theta*theta)*t / D
    l2 = 1 / (theta*t + 1)
    lhs_minus = (l2-l1)*D*(theta*t+1)
    rhs_minus = 2*theta*(theta*t+1)**2
    lhs_plus = (l2+l1)*D*(theta*t+1)
    rhs_plus = 2*(theta*t+1)*(t*(1-theta*theta)+theta)
    assert isclose(lhs_minus, rhs_minus, rel_tol=1e-12, abs_tol=1e-12)
    assert isclose(lhs_plus, rhs_plus, rel_tol=1e-12, abs_tol=1e-12)
    assert abs(l1) <= l2 + 1e-12

max_eta = -10.0
argmax = None
for r in [1.5, 2.0, 3.0, 5.0, 10.0]:
    y = sqrt(r)
    theta = (y**3-y)/(y**4-2)
    residual = theta*y**4-y**3+y-2*theta
    tau = theta*y**3
    exact_form = r*r*(r-1)/(r*r-2)
    assert abs(residual) < 1e-11
    assert isclose(tau, exact_form, rel_tol=1e-12, abs_tol=1e-12)
    assert tau >= 2 - 1e-12
    if 0 < theta < 1:
        eta = 3/(tau+1)**2 - 1
        if eta > max_eta:
            max_eta, argmax = eta, (r, theta)
        assert eta <= -Fraction(2,3) + 1e-12

assert isclose(argmax[0], 2.0, abs_tol=1e-12)
assert isclose(argmax[1], 1/sqrt(2), rel_tol=1e-12)
assert isclose(max_eta, -2/3, rel_tol=1e-12)
print("VERIFY_OK factorization=exact eigenvalue_identities=4 large_branch_points=5 sharp_eta=-2/3")
