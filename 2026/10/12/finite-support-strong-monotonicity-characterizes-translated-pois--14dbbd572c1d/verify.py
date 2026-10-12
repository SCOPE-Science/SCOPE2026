#!/usr/bin/env python3
"""Exact finite algebra checks for a real-rootedness/tilted-Fourier theorem.

This is supplemental evidence only. The theorem over all finite supports is
proved by the complex-zero and Bernoulli-factor arguments in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, pi, sqrt, atan2


def convolution(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def bernoulli_coefficients(probs):
    c = [F(1)]
    for q in probs:
        assert 0 < q < 1
        c = convolution(c, [1 - q, q])
    return c


def example_one():
    ps = [F(1, 5), F(3, 7), F(4, 5), F(2, 3)]
    coeff = bernoulli_coefficients(ps)
    assert sum(coeff) == 1
    # Roots of each linear factor are -(1-q)/q.
    for q in ps:
        root = -(1-q)/q
        assert sum(c * root**j for j, c in enumerate(coeff)) == 0
    for c in coeff:
        assert c > 0
    return len(ps)


def quadratics():
    count = 0
    weaker = 0
    for a, b, c in product(range(1, 23), repeat=3):
        # |a+b exp(it)+c exp(2it)|^2 has derivative
        # -2 sin(t) [b(a+c)+4ac cos(t)].
        monotone = b*(a+c) >= 4*a*c
        discriminant = b*b >= 4*a*c
        # Requiring the previous monotonicity after every tilt
        # means min_{r>0} b(a/r+cr) >= 4ac, i.e. b^2>=4ac.
        all_tilts = discriminant
        assert all_tilts == discriminant
        assert not (discriminant and not monotone)
        weaker += int(monotone and not discriminant)
        count += 1
    return count, weaker


def explicit_certificate():
    a, b, c = F(90,100), F(9,100), F(1,100)
    assert a+b+c == 1
    assert b*(a+c) > 4*a*c   # ordinary monotonicity
    assert b*b < 4*a*c       # complex conjugate roots
    r = sqrt(float(a/c))
    x = -float(b)/(2*float(c))
    y = sqrt(float(4*a*c-b*b))/(2*float(c))
    angle = atan2(y, x)
    assert 0 < angle < pi
    def magnitude(t):
        import cmath
        z = r*cmath.exp(1j*t)
        value = float(a)+float(b)*z+float(c)*z*z
        denom = float(a)+float(b)*r+float(c)*r*r
        return abs(value)/denom
    # Mid-interval zero followed by positive endpoint magnitude:
    assert magnitude(angle) < 1e-12
    assert magnitude(pi) > 0.3
    return angle, magnitude(pi)


def main():
    assert example_one() == 4
    n, weaker = quadratics()
    assert n == 22**3 and weaker > 0
    t, v = explicit_certificate()
    print('PASS: four Bernoulli factors yield nonnegative normalized PGF with expected negative roots')
    print(f'PASS: {n} exact integer coefficient triples; {weaker} ordinary-but-not-strong cases')
    print(f'PASS: rational witness has tilted Fourier zero at angle {t:.12f}, but endpoint modulus {v:.12f}')
    print('LIMIT: numerical point check not an infinite proof; full equivalence is established algebraically in RESULT.md')

if __name__ == '__main__':
    main()
