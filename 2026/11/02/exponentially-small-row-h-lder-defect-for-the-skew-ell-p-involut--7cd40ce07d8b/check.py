#!/usr/bin/env python3
"""Supplementary finite-precision checks for a two-coordinate operator norm theorem.

Run: python3 check.py (Python standard library only).  Finite checks are not a
proof of uniqueness or of any asymptotic limit.
"""
from decimal import Decimal, localcontext

COUNT = 0

def check(condition, description):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(description)

def operator_data(t, p):
    p = int(p)
    P = Decimal(p)
    s0 = (t.ln() / (P - 1)).exp()
    q = P / (P - 1)
    R = (1 + t ** q) ** (1 / q)
    rho = (1 - t) / (1 + t)

    def H(s):
        z = (s - t) / (1 + t * s)
        return s ** (p - 1) - t - (1 + t * s ** (p - 1)) * z ** (p - 1)

    check(H(s0) < 0 and H(Decimal(1)) > 0, 'bracketing')
    lo, hi = s0, Decimal(1)
    for _ in range(420):
        mid = (lo + hi) / 2
        if H(mid) > 0:
            hi = mid
        else:
            lo = mid
    s = (lo + hi) / 2
    check(s0 < s < 1, 'strict interior root')

    def f(x):
        a = abs(1 + t * x)
        b = abs(t - x)
        return ((a ** p + b ** p) / (1 + abs(x) ** p)) ** (1 / P)

    nu = f(s)
    check(nu > R, 'strict row-Holder correction')
    for j in range(401):
        x = Decimal(j) / 400
        check(nu >= f(x) - Decimal('1e-65'), 'positive-grid norm')
        check(f(x) >= f(-x) - Decimal('1e-65'), 'projective sign comparison')
    rp = (s0 - t) / (1 + t * s0)
    scaled = P * (nu / R - 1) / (rp ** p)
    displacement = ((s - s0) * t * (P - 1) /
                    (s0 * (1 + t*t) * rp ** (p - 1)))
    return scaled, displacement, nu, R, s, s0, rho


def main():
    with localcontext() as ctx:
        ctx.prec = 180
        for param in ('0.2', '0.5', '0.8'):
            t = Decimal(param)
            previous = None
            for p in (12, 20, 30, 50, 80):
                scaled, disp, nu, R, s, s0, rho = operator_data(t, p)
                check(abs(scaled - 1) < Decimal('0.08'), 'scaled correction')
                check(abs(disp - 1) < Decimal('0.08'), 'scaled optimizer displacement')
                if previous is not None:
                    check(abs(scaled - 1) <= abs(previous - 1) + Decimal('1e-32'),
                          'finite-sample convergence tendency')
                previous = scaled
            # Separate exact test of the exponential rate constant via a
            # high-precision expansion with no operator optimization.
            P = Decimal(100)
            sp = (t.ln() / (P - 1)).exp()
            rp = (sp-t)/(1+t*sp)
            r = (1-t)/(1+t)
            predicted = t ** ((1+t*t)/(1-t*t))
            check(abs((rp/r)**100 / predicted - 1) < Decimal('0.08'),
                  'exponential scale constant')
        print('PASS: %d deterministic high-precision assertions' % COUNT)
        print('Finite checks support, but do not prove, global or asymptotic statements.')

if __name__ == '__main__':
    main()
