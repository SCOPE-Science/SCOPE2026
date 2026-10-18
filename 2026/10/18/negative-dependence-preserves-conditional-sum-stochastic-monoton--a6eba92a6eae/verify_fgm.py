"""Supplementary checks for an exponential-pair conditional-order theorem.

Standard library only; finite checks do not establish the universal theorem.
Run: python verify_fgm.py
"""
import math
from fractions import Fraction


def weight(x, s, theta):
    u = math.exp(-x)
    v = math.exp(x - s)
    return 1.0 + theta * (1.0 - 2.0 * u) * (1.0 - 2.0 * v)


def primitive(s, t, theta):
    """Integral from 0 to t of the conditional unnormalised weight."""
    z = math.exp(-s)
    c = -math.expm1(-t)
    d = math.expm1(t) - 2.0 * t
    r = -theta
    return (1.0 - r) * t + 2.0 * r * (c + z * d)


def cdf(s, t, theta):
    if t <= 0.0:
        return 0.0
    if t >= s:
        return 1.0
    return primitive(s, t, theta) / primitive(s, s, theta)


def midpoint_integral(s, t, theta, steps=12000):
    return sum(weight((j + 0.5) * t / steps, s, theta) for j in range(steps)) * t / steps


def check():
    count = 0
    # The nonstandard mixed logarithmic-curvature identity is checked in
    # rational arithmetic on independent rational values of u,v and theta.
    for u_num in range(1, 9):
        for v_num in range(1, 9):
            u = Fraction(u_num, 10)
            v = Fraction(v_num, 10)
            A = 1 - 2 * u
            B = 1 - 2 * v
            for numerator in range(-10, 11):
                theta = Fraction(numerator, 10)
                H = 1 + theta * A * B
                H_x = 2 * theta * (u - v)
                H_s = 2 * theta * v * A
                H_xs = 2 * theta * v
                assert H * H_xs - H_x * H_s == 2 * theta * v * (1 + theta * A * A)
                count += 1

    for theta in (-1.0, -0.99, -0.8, -0.3, -0.05, 0.0, 0.1, 0.5, 1.0):
        for s in (0.4, 0.8, 1.5, 2.5, 4.5, 9.0):
            for fraction in (0.1, 0.25, 0.5, 0.75, 0.9):
                t = fraction * s
                num = primitive(s, t, theta)
                denom = primitive(s, s, theta)
                assert 0.0 < num < denom
                assert abs(num - midpoint_integral(s, t, theta)) < 5e-7
                assert abs(denom - midpoint_integral(s, s, theta)) < 5e-7
                assert 0.0 < cdf(s, t, theta) < 1.0
                count += 1
        for s1,s2 in ((0.4,0.7),(0.7,1.1),(1.0,1.9),(1.9,3.5),(3.5,6.0)):
            for fraction in (0.1,0.25,0.5,0.75,0.9):
                t = fraction * s1
                assert cdf(s2,t,theta) < cdf(s1,t,theta)
                count += 1
    for theta in (-1., -0.8, -.2, 0., .4, 1.):
        for s in (0.5, 2., 5.):
            for fraction in (0.2,0.5,0.8):
                x = s * fraction
                u = math.exp(-x)
                v = math.exp(x-s)
                H = weight(x,s,theta)
                curvature = 2*theta*v*(1+theta*(1-2*u)**2)/H**2
                if theta < 0:
                    assert curvature < 0
                elif theta > 0:
                    assert curvature > 0
                else:
                    assert curvature == 0
                count += 1
    return count


if __name__ == '__main__':
    checks = check()
    print(f'PASS: {checks} supplementary exact-rational and numerical checks')
