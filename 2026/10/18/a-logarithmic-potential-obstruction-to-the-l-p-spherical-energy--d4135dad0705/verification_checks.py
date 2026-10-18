"""Diagnostics for the exact rectangle-density obstruction.

The proof uses strict convexity on a continuum; finite checks below are not
substitutes for the analytic inequality or for the small-exponent limit.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def main():
    a = Fraction(1, 8)
    s = a ** 3
    assert s == Fraction(1, 512)
    assert 2 * s < 1
    # On [0, 2s], h''(u) = 4/9 * (1-u)^(-7/3) >= 4/9.
    proven_lower_bound = Fraction(4, 9) * s * s
    assert proven_lower_bound == Fraction(1, 589824)
    with localcontext() as context:
        context.prec = 80
        one = Decimal(1)
        ss = Decimal(s.numerator) / Decimal(s.denominator)
        h = lambda z: (one - z) ** (Decimal(-1) / Decimal(3))
        difference = h(2 * ss) + h(Decimal(0)) - 2 * h(ss)
        lower = Decimal(proven_lower_bound.numerator) / Decimal(proven_lower_bound.denominator)
        assert difference > lower > 0
        print('density finite difference / positive normalization:', difference)
        print('strict analytic lower bound / positive normalization:', lower)
    print('PASS: convexity sign and rational support conditions')


if __name__ == '__main__':
    main()
