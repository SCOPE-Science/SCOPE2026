#!/usr/bin/env python3
"""Check exact bounds and high-precision diagnostic values for a two-rate truncation example.

The all-ages monotonicity assertion is proved analytically in RESULT.md;
finite numerical tests below are consistency checks, not a replacement for proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction

q = Fraction(1, 4)
log_upper = q - q**2 / 2 + q**3 / 3
log_lower = log_upper - q**4 / 4
assert log_upper == Fraction(43, 192)
assert log_lower < log_upper
assert 11 - 48*log_upper == Fraction(1, 4) > 0

with localcontext() as context:
    context.prec = 70
    one = Decimal(1)
    log54 = (Decimal(5)/4).ln()
    boundary = one + 3*log54
    ratio = Decimal(4)/5
    survival_t = (-one).exp()*ratio

    def survival(x):
        if x <= one:
            return (-x).exp()
        return (-one-(x-one)/3).exp()

    def truncated_mrl(x):
        sx = survival(x)
        if x < one:
            # Integral_x^1 S + integral_1^T S - (T-x)S(T).
            numerator = (sx - (-one).exp()
                         + 3*(-one).exp()*(one-ratio)
                         - (boundary-x)*survival_t)
        else:
            numerator = 3*(sx-survival_t)-(boundary-x)*survival_t
        return numerator/(sx-survival_t)

    m_at_1 = truncated_mrl(one)
    assert abs(m_at_1 - (3-12*log54)) < Decimal('1e-65')
    slope_left = 11-48*log54
    assert slope_left > Decimal('0.25')
    lvals = [(x, truncated_mrl(x)/x) for x in
             map(Decimal, ['0.99','0.999','0.9999','0.999999','1'])]
    assert all(a[1] < b[1] for a,b in zip(lvals,lvals[1:]))
    # The right-hand slope is negative: a local maximum lies at the switch.
    slope_right = (Decimal(2)/3)*m_at_1-1
    assert slope_right < 0
    assert abs((Decimal(5)-1)*m_at_1-1-slope_left) < Decimal('1e-65')
    print('Exact certificate: 11 - 48 log(5/4) > 1/4 > 0')
    print('Cutoff =', boundary)
    print('Left slope at 1 =', slope_left)
    print('Right slope at 1 =', slope_right)
    print('Finite diagnostics: truncated GMRL increases toward 1 from below')
    for x, val in lvals:
        print('  x=', x, 'GMRL=', val)
