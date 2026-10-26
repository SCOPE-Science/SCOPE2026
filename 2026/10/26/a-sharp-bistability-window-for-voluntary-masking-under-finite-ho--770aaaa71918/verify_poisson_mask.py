"""Standalone consistency checks for the finite-horizon Poisson mask game.

Run with: python verify_poisson_mask.py
The analytic theorem is proved in RESULT.md; sampling is not its proof.
"""
from fractions import Fraction
from math import exp, log, sqrt, isclose


def mask_advantage(p, q, exposure, severity, cost):
    mean_attenuator = 1.0 - (1.0 - q) * p
    return severity * (
        exp(-exposure * q * mean_attenuator)
        - exp(-exposure * mean_attenuator)
    ) - cost


def max_attenuator(q, exposure):
    return log(1.0 / q) / (exposure * (1.0 - q))


def verify_exact_example():
    # The substitution y=exp(-m) yields y-y*y=63/256 exactly.
    cost = Fraction(63, 256)
    for y in (Fraction(7, 16), Fraction(9, 16)):
        assert y - y * y == cost
    assert (Fraction(7, 16) + Fraction(9, 16)) == 1
    assert Fraction(7, 16) * Fraction(9, 16) == cost

    q = 0.5
    exposure = 2.0
    m_peak = max_attenuator(q, exposure)
    assert 0.5 < m_peak < 1.0
    p_lower = 2.0 * (1.0 + log(7.0 / 16.0))
    p_upper = 2.0 * (1.0 + log(9.0 / 16.0))
    assert 0.0 < p_lower < p_upper < 1.0

    c = float(cost)
    assert mask_advantage(0.0, q, exposure, 1.0, c) < 0
    assert mask_advantage(1.0, q, exposure, 1.0, c) < 0
    assert abs(mask_advantage(p_lower, q, exposure, 1.0, c)) < 1e-14
    assert abs(mask_advantage(p_upper, q, exposure, 1.0, c)) < 1e-14
    assert mask_advantage((p_lower + p_upper) / 2, q, exposure, 1.0, c) > 0
    assert mask_advantage(p_lower / 2, q, exposure, 1.0, c) < 0
    assert mask_advantage((p_upper + 1) / 2, q, exposure, 1.0, c) < 0
    assert isclose(0.5, exp(-exposure * 0.5 * m_peak), abs_tol=1e-14)
    return p_lower, p_upper


def verify_parameter_windows():
    # Representative parameter checks, not a substitute for the derivative proof.
    for q in (0.15, 0.35, 0.5, 0.8):
        lower = log(1 / q) / (1 - q)
        upper = lower / q
        for exposure in (lower * 0.9, (lower + upper) / 2, upper * 1.1):
            interior = lower < exposure < upper
            mstar = max_attenuator(q, exposure)
            assert interior == (q < mstar < 1)
            if interior:
                h = lambda m: exp(-exposure * q * m) - exp(-exposure * m)
                left, peak, right = h(1.0), h(mstar), h(q)
                assert peak > left and peak > right
                cost = (max(left, right) + peak) / 2
                gain = lambda p: mask_advantage(p, q, exposure, 1, cost)
                pstar = (1 - mstar) / (1 - q)
                assert gain(0) < 0 and gain(1) < 0 and gain(pstar) > 0
                crossings = [i for i in range(2000)
                             if gain(i / 2000) * gain((i + 1) / 2000) < 0]
                assert len(crossings) == 2
            else:
                hvals = [exp(-exposure * q * (1-(1-q)*i/1000))
                         - exp(-exposure * (1-(1-q)*i/1000))
                         for i in range(1001)]
                trend = hvals[1] - hvals[0]
                assert all((hvals[j+1] - hvals[j]) * trend >= -1e-13
                           for j in range(1000))


if __name__ == '__main__':
    p_minus, p_plus = verify_exact_example()
    verify_parameter_windows()
    print('Exact fractional roots, sign/stability checks, and sample parameter tests: PASS')
    print(f'Interior roots: {p_minus:.12f}, {p_plus:.12f}')
