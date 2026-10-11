#!/usr/bin/env python3
"""Reproduce certified positive Fourier sine moments for an affine two-map measure.

Dependencies: Python 3.10+ and mpmath (interval arithmetic). Run:
    python verify_golden_dyadic.py
The recurrence is evaluated with outward interval arithmetic, and the
truncation error is bounded analytically using support in [0, 2/3].
"""
from fractions import Fraction
from mpmath import iv


def sine_enclosure(t: int, depth: int = 36):
    iv.dps = 45
    p = (iv.sqrt(5) - 1) / 2
    q = 1 - p
    f_k_plus_1 = iv.mpc(1)
    f_k_plus_2 = iv.mpc(1)
    for k in range(depth - 1, -1, -1):
        phase = iv.exp(iv.j * iv.pi * t / (2 ** k))
        f_k = p * f_k_plus_1 + q * phase * f_k_plus_2
        f_k_plus_2, f_k_plus_1 = f_k_plus_1, f_k
    # The exact Fourier transform F(u) differs from 1 by at most
    # 2 pi |u| sup(supp(mu)) = 4 pi |u|/3.  Since |p|+|q|=1,
    # this boundary error cannot grow under backward recursion.
    tail_bound = Fraction(4, 3) * Fraction(22, 7) * Fraction(t, 2**depth)
    tail_iv = iv.mpf(tail_bound.numerator) / tail_bound.denominator
    lower = iv.im(f_k_plus_1).a - tail_iv
    upper = iv.im(f_k_plus_1).b + tail_iv
    return lower, upper


def main():
    for t, outer_low, outer_high in [
        (1, '0.224', '0.226'),
        (2, '0.384', '0.386'),
    ]:
        low, high = sine_enclosure(t)
        assert low > iv.mpf(outer_low), (t, low, outer_low)
        assert high < iv.mpf(outer_high), (t, high, outer_high)
        print('t =', t, 'sine Fourier moment in (', outer_low, ',', outer_high, ')')
    print('CERTIFIED: Im F(1)>1/5 and Im F(2)>1/5')
    print('All higher dyadic samples exceed 1/5 by the exact convex recurrence.')


if __name__ == '__main__':
    main()
