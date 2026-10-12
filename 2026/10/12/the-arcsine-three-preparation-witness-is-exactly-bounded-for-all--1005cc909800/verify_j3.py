#!/usr/bin/env python3
import math

TOL = 2e-12

def check_gradient_grid():
    vals = [i / 40 for i in range(-40, 41)]
    cs = [i / 50 for i in range(-50, 51)]
    for a in vals:
        max_t = 1.0 - abs(a)
        for j in range(21):
            t = max_t * j / 20.0
            for c in cs:
                lhs = t * t * (1.0 - c * c)
                rhs = 1.0 - (a + t * c) ** 2
                if lhs > rhs + TOL:
                    raise AssertionError(("gradient", a, t, c, lhs, rhs))

def check_boundary_grid():
    vals = [i / 40 for i in range(-40, 41)]
    cs = [i / 50 for i in range(0, 51)]
    for a in vals:
        max_t = 1.0 - abs(a)
        for j in range(21):
            t = max_t * j / 20.0
            for c in cs:
                left = math.asin(a + t * c) + math.asin(a - t * c)
                right = math.pi / 2.0 + math.asin(a - t)
                if left > right + TOL:
                    raise AssertionError(("boundary", a, t, c, left, right))

def check_equality():
    q = 1.0 / math.sqrt(2.0)
    e11, e12, e21, e22, e31 = q, q, q, -q, -1.0
    J = abs(math.asin(e11) + math.asin(e12) + math.asin(e21)
            - math.asin(e22) - math.asin(e31))
    target = 3.0 * math.pi / 2.0
    if abs(J - target) > TOL:
        raise AssertionError(("equality", J, target))

if __name__ == "__main__":
    check_gradient_grid()
    check_boundary_grid()
    check_equality()
    print("VERIFY_OK")
