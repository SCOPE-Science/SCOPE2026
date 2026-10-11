#!/usr/bin/env python3
from fractions import Fraction
import math


def volume_bounds_sq(q2):
    q2 = float(q2)
    disc = (q2 - 9.0) ** 3 * (q2 - 1.0)
    if disc < -1e-11:
        raise AssertionError("q^2 below 9")
    disc = max(0.0, disc)
    core = q2 * q2 + 18.0 * q2 - 27.0
    root = math.sqrt(disc)
    return (8.0 / 9.0 * (core - root), 8.0 / 9.0 * (core + root))


def check_grid():
    total = 0
    for den in (24, 36, 48, 60):
        for i in range(1, den - 1):
            for j in range(1, den - i):
                k = den - i - j
                a = Fraction(i, den)
                b = Fraction(j, den)
                c = Fraction(k, den)
                q2 = 1 / a + 1 / b + 1 / c
                product = a * b * c
                # rho=1, so R^2=q2 and V^2=(64/9) q2^3 abc.
                v2 = Fraction(64, 9) * q2 ** 3 * product
                lo, hi = volume_bounds_sq(q2)
                vf = float(v2)
                tol = 2e-9 * max(1.0, hi)
                if vf < lo - tol or vf > hi + tol:
                    raise AssertionError((den, i, j, k, float(q2), vf, lo, hi))
                total += 1
    return total


def check_endpoints():
    cases = 0
    for q2 in range(9, 201):
        d = math.sqrt((q2 - 1.0) * (q2 - 9.0))
        u_minus = (q2 + 3.0 - d) / (4.0 * q2)
        u_plus = (q2 + 3.0 + d) / (4.0 * q2)
        D = math.sqrt((q2 - 9.0) ** 3 * (q2 - 1.0))
        s_minus = (q2*q2 + 18*q2 - 27 - D) / (8.0 * q2**3)
        s_plus = (q2*q2 + 18*q2 - 27 + D) / (8.0 * q2**3)
        lhs_minus = u_minus*u_minus*(1.0 - 2.0*u_minus)
        lhs_plus = u_plus*u_plus*(1.0 - 2.0*u_plus)
        if not math.isclose(lhs_minus, s_minus, rel_tol=2e-12, abs_tol=2e-14):
            raise AssertionError((q2, "lower", lhs_minus, s_minus))
        if not math.isclose(lhs_plus, s_plus, rel_tol=2e-12, abs_tol=2e-14):
            raise AssertionError((q2, "upper", lhs_plus, s_plus))
        lo, hi = volume_bounds_sq(q2)
        vm = 64.0/9.0 * q2**3 * s_minus
        vp = 64.0/9.0 * q2**3 * s_plus
        if not math.isclose(vm, lo, rel_tol=2e-12, abs_tol=2e-11):
            raise AssertionError((q2, "volume lower", vm, lo))
        if not math.isclose(vp, hi, rel_tol=2e-12, abs_tol=2e-11):
            raise AssertionError((q2, "volume upper", vp, hi))
        cases += 1
    return cases


def main():
    triples = check_grid()
    endpoint_cases = check_endpoints()
    print(f"VERIFY_OK concentric-bicentric-tetrahedra triples={triples} endpoint_cases={endpoint_cases}")


if __name__ == "__main__":
    main()
