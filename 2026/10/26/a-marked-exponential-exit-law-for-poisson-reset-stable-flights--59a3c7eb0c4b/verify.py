#!/usr/bin/env python3
"""Independent algebraic consistency checks for the marked stable exit formulas."""
import math
from fractions import Fraction


def stable_c(alpha, sigma=1.0):
    return sigma**alpha * math.gamma(1.0 + alpha) * math.sin(math.pi * alpha / 2.0) / math.pi


def lambda_exit(alpha, sigma, theta):
    c = stable_c(alpha, sigma)
    return c / alpha * ((1 - theta)**(-alpha) + (1 + theta)**(-alpha))


def check_close(a, b, tol=1e-12):
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)


def run():
    checks = 0
    for alpha in (0.3, 0.5, 0.9, 1.0, 1.25, 1.8):
        c = stable_c(alpha, 1.7)
        assert c > 0
        checks += 1
        if alpha != 1.0:
            c_alt = alpha * 1.7**alpha / (2 * math.gamma(1-alpha) * math.cos(math.pi*alpha/2))
            check_close(c, c_alt)
            checks += 1
        for theta in (-0.7, -0.2, 0.0, 0.4, 0.75):
            lam = lambda_exit(alpha, 1.7, theta)
            right = c / alpha * (1-theta)**(-alpha) / lam
            left = c / alpha * (1+theta)**(-alpha) / lam
            check_close(right+left, 1.0)
            checks += 1
            for u in (0.0, 0.5, 1.0, 10.0):
                check_close((1-theta+u)**(-alpha) / ((1-theta)**(-alpha)),
                            ((1-theta)/(1-theta+u))**alpha)
                check_close((1+theta+u)**(-alpha) / ((1+theta)**(-alpha)),
                            ((1+theta)/(1+theta+u))**alpha)
                checks += 2
            for s in (0.0, 0.5*lam, 3*lam):
                # Conditional time transform times the normalized right mark mass.
                joint_right = (c / alpha * (1-theta)**(-alpha)) / (lam+s)
                check_close(joint_right, (lam/(lam+s))*right)
                checks += 1
    # Exact Cauchy reference example: c=1/pi, theta=1/3.
    theta = Fraction(1,3)
    right_jump_mass_over_c = 1 / (1-theta)
    left_jump_mass_over_c = 1 / (1+theta)
    assert right_jump_mass_over_c + left_jump_mass_over_c == Fraction(9,4)
    assert right_jump_mass_over_c / (right_jump_mass_over_c+left_jump_mass_over_c) == Fraction(2,3)
    assert left_jump_mass_over_c / (right_jump_mass_over_c+left_jump_mass_over_c) == Fraction(1,3)
    check_close(lambda_exit(1.0,1.0,1/3), 9/(4*math.pi))
    checks += 4
    print('VERIFICATION_OK', checks)


if __name__ == '__main__':
    run()
