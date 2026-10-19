"""Numerical checks of the Parry-density endpoint response asymptotics.

The rigorous statements use the analytic proof; finite decimal calculations here
check the density identities and the approach to the predicted coefficients.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR
from math import log


def parry_statistics(base, exponent):
    with localcontext() as ctx:
        ctx.prec = 170
        b = Decimal(base)
        eps = Decimal(10) ** (-exponent)
        beta = b - eps
        a = Decimal(1)
        weight = Decimal(1)
        intervals = [(a, weight)]
        # A long enough prefix makes the missing positive tail negligible
        # relative to eps*log(1/eps).
        iterations = max(450, int(5.0 * exponent * log(10) / log(base)))
        for _ in range(iterations):
            t = beta * a
            digit = t.to_integral_value(rounding=ROUND_FLOOR)
            a = t - digit
            weight /= beta
            intervals.append((a, weight))
        weighted_length = sum((a * wt for a, wt in intervals), Decimal(0))
        weighted_x = sum((a * a * wt / 2 for a, wt in intervals), Decimal(0))
        mean = weighted_x / weighted_length
        S = beta / (beta - 1)
        defect = S - weighted_length
        scale = eps * (Decimal(exponent) * Decimal(10).ln())
        # TV positive mass of normalized density difference.
        breakpoints = sorted((a, wt) for a, wt in intervals[1:])
        curr = Decimal(0)
        accrued = Decimal(0)
        integral_positive = Decimal(0)
        for point, wt in breakpoints:
            if point > curr and defect > accrued:
                integral_positive += (point - curr) * (defect - accrued)
            accrued += wt
            curr = point
        if curr < 1 and defect > accrued:
            integral_positive += (1 - curr) * (defect - accrued)
        tv = integral_positive / weighted_length
        return float((mean - Decimal('0.5')) / scale), float(tv / scale), float(defect / scale)


def run():
    for b in (2, 3, 5):
        predicted_mean = -1 / (2 * b * log(b))
        predicted_tv = 1 / (b * log(b))
        prev_mean_error = None
        prev_tv_error = None
        for exponent in (5, 10, 20, 35):
            measured_mean, measured_tv, measured_defect = parry_statistics(b, exponent)
            m_err = abs(measured_mean - predicted_mean)
            t_err = abs(measured_tv - predicted_tv)
            print('base', b, 'epsilon=10^-'+str(exponent),
                  'mean_norm', f'{measured_mean:.10g}', 'TV_norm', f'{measured_tv:.10g}',
                  'defect_norm', f'{measured_defect:.10g}')
            if prev_mean_error is not None:
                assert m_err < prev_mean_error * 1.12
                assert t_err < prev_tv_error * 1.12
            prev_mean_error, prev_tv_error = m_err, t_err
        assert m_err < abs(predicted_mean) * .1, (b, m_err, predicted_mean)
        assert t_err < predicted_tv * .1, (b, t_err, predicted_tv)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
