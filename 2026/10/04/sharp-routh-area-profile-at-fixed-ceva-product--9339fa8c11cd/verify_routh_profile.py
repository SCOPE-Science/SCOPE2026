#!/usr/bin/env python3
import math
import random


def routh_ratio(x, y, z):
    num = (x*y*z - 1.0)**2
    den = (1.0 + x + x*y) * (1.0 + y + y*z) * (1.0 + z + z*x)
    return num / den


def profile_from_product(product):
    s = abs(math.log(product)) / 3.0
    c = math.cosh(s)
    return 2.0*(c - 1.0)/(2.0*c + 1.0)


def inverse_log_defect(alpha):
    if alpha <= 0.0:
        return 0.0
    return 3.0*math.acosh((2.0 + alpha)/(2.0*(1.0 - alpha)))


def main():
    rng = random.Random(20261001)
    worst_profile = 0.0
    worst_equal = 0.0
    worst_inverse = 0.0
    checked = 0

    # Generic triples spanning many scales.
    for _ in range(30000):
        a = rng.uniform(-8.0, 8.0)
        b = rng.uniform(-8.0, 8.0)
        c = rng.uniform(-8.0, 8.0)
        x, y, z = math.exp(a), math.exp(b), math.exp(c)
        alpha = routh_ratio(x, y, z)
        bound = profile_from_product(x*y*z)
        worst_profile = max(worst_profile, alpha - bound)
        if alpha > 1e-14:
            lhs = abs(math.log(x*y*z))
            rhs = inverse_log_defect(alpha)
            worst_inverse = max(worst_inverse, rhs - lhs)
        checked += 1

    # Equality branch x=y=z=q.
    for u in [i/20.0 for i in range(-120, 121)]:
        q = math.exp(u)
        alpha = routh_ratio(q, q, q)
        bound = profile_from_product(q**3)
        worst_equal = max(worst_equal, abs(alpha - bound))
        checked += 1

    # Fixed-product path demonstrating approach to zero away from Ceva.
    for q in (0.2, 0.5, 2.0, 5.0):
        vals = []
        for k in (2, 4, 8, 12, 16, 20):
            t = math.exp(k)
            x = t
            y = q**3 / t
            z = 1.0
            vals.append(routh_ratio(x, y, z))
        if not all(vals[i+1] < vals[i] for i in range(len(vals)-1)):
            raise AssertionError((q, vals))
        if vals[-1] > 1e-12:
            raise AssertionError((q, vals[-1]))
        checked += len(vals)

    tol = 2e-12
    if worst_profile > tol:
        raise AssertionError(("profile", worst_profile))
    if worst_equal > tol:
        raise AssertionError(("equality", worst_equal))
    if worst_inverse > 2e-10:
        raise AssertionError(("inverse", worst_inverse))

    print("VERIFY_OK")
    print(f"cases={checked}")
    print(f"worst_profile_violation={worst_profile:.3e}")
    print(f"worst_equality_error={worst_equal:.3e}")
    print(f"worst_inverse_violation={worst_inverse:.3e}")


if __name__ == "__main__":
    main()
