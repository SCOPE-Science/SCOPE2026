"""Supplementary numerical checks for exact exponential–apple inclusion.
The complete mathematical proof is in RESULT.md. This script does not prove
continuous inequalities from its finite samples.
"""
from decimal import Decimal, localcontext
from math import atan2, cos, sin, pi
import cmath


def high_precision_root(q_text: str) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = 85
        q = Decimal(q_text)
        one = Decimal(1)
        lo = Decimal(0)
        hi = one - Decimal('1e-70')

        def residual(r):
            return r - q * (one - r).ln() - one

        assert residual(lo) < 0 < residual(hi)
        for _ in range(350):
            mid = (lo + hi) / 2
            if residual(mid) < 0:
                lo = mid
            else:
                hi = mid
        r = (lo + hi) / 2
        assert abs(residual(r)) < Decimal('1e-70')
        u = one - r
        assert abs(u + q * u.ln()) < Decimal('1e-70')
        return +r


def supplementary_angular_check():
    for q in (0.0, 0.125, 0.25, 0.5):
        highest = 0.0
        for k in range(1, 20000):
            theta = -pi + 2*pi*k/20000
            z = complex(cos(theta),sin(theta))
            # Direct boundary formula avoids taking log at z = -1.
            angle = abs(sin(theta) + q*theta/2)
            highest = max(highest,angle)
        assert highest < 1.5
        print('angular diagnostic',q,highest)


if __name__ == '__main__':
    for q in ('0.5','0.25','0.125'):
        print('q',q,'sharp radius',high_precision_root(q))
    supplementary_angular_check()
    print('Supplementary checks passed; the universal claims use the analytic proof.')
