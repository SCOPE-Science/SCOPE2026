#!/usr/bin/env python3
"""Arithmetic diagnostics for rational planar scattering statements.

This finite program tests exact conjugacy identities and representative numerical
asymptotics. The infinite-time assertions require the argument in RESULT.md.
"""
from fractions import Fraction
from decimal import Decimal, localcontext


def exact_normalization_checks():
    for a, c, x, y in [
        (Fraction(2), Fraction(1), Fraction(1, 3), Fraction(-2)),
        (Fraction(3, 2), Fraction(-2), Fraction(1, 7), Fraction(4)),
        (Fraction(5), Fraction(-3, 2), Fraction(-2, 9), Fraction(-5, 3)),
    ]:
        sign = 1 if c * x > 0 else -1
        z = sign * y
        w = abs(c * x)
        xp = x * (1 + a / (1 + y * y))
        yp = y + c * x
        assert sign * yp == z + w
        assert abs(c * xp) == w * (1 + a / (1 + z * z))
        assert xp * x > 0
    return 3


def finite_diagnostics():
    cases = [
        ('2', '1', '0.01', '0'),
        ('0.5', '2', '-0.75', '7'),
        ('3', '-2', '0.25', '-3'),
        ('4', '0.5', '-1', '-2'),
        ('1', '1', '0.000000000001', '0'),
    ]
    outputs = []
    with localcontext() as ctx:
        ctx.prec = 65
        for aa, cc, xx, yy in cases:
            a, c, x, y = map(Decimal, (aa, cc, xx, yy))
            x0, y0 = x, y
            sign = 1 if c*x0 > 0 else -1
            z0 = Decimal(sign)*y0
            R2 = max(z0*z0, (z0+1)*(z0+1))
            lower = a/(1+R2)
            N = 12000
            samples = {}
            for n in range(1, N+1):
                xn = x*(1+a/(1+y*y))
                yn = y+c*x
                assert xn*x > 0
                x,y = xn,yn
                if n in (3000,6000,12000):
                    Xest = x + a/(c*c*x*Decimal(n))
                    Cest = y-c*Xest*Decimal(n)+a/(c*Xest)*Decimal(n).ln()
                    samples[n] = (Xest, Cest)
            X3,C3 = samples[3000]
            X6,C6 = samples[6000]
            X12,C12 = samples[12000]
            assert abs(c*X12) > lower
            assert abs((X12-X6)/X12) < Decimal('0.00001')
            assert abs((X12-X3)/X12) < Decimal('0.0001')
            assert abs(C12-C6) < Decimal('0.02')
            outputs.append((aa,cc,xx,yy,str(X12),str(C12),str(lower)))
    return outputs


if __name__ == '__main__':
    print('Exact fractional normalization cases:', exact_normalization_checks())
    print('Finite diagnostics (a,c,x0,y0,X-estimate,C-estimate,velocity lower bound):')
    for v in finite_diagnostics():
        print(' | '.join(v))
    print('PASS: exact normalization and finite asymptotic diagnostics.')
