"""Independent finite checks for dyadic index-shift congruences of central Delannoy numbers.

Run: python3 delannoy_period_verifier.py
This program tests finite ranges only; the supplied mathematical proof handles all indices.
"""
from math import comb


def central_delannoy_recurrence(limit):
    values = [1, 3]
    for n in range(2, limit + 1):
        top = 3 * (2 * n - 1) * values[-1] - (n - 1) * values[-2]
        assert top % n == 0
        values.append(top // n)
    return values[:limit + 1]


def central_delannoy_binomial(n):
    return sum((1 << j) * comb(n, j) ** 2 for j in range(n + 1))


def valuation_two(n):
    assert n
    a = abs(n)
    return (a & -a).bit_length() - 1


def predicted_period(k):
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 4
    return 1 << (k - 2)


def run():
    N = 1800
    values = central_delannoy_recurrence(N)
    crosschecks = 0
    for n in range(161):
        assert central_delannoy_binomial(n) == values[n], n
        crosschecks += 1

    phase_checks = 0
    sharp_checks = 0
    # Every h divisible by four in [4, 512], and every permitted n < 1800-h.
    for h in range(4, 513, 4):
        a = valuation_two(h)
        modulus = 1 << (a + 3)
        required = 1 << (a + 2)
        for n in range(N - h + 1):
            delta = values[n + h] - values[n]
            phase = (n + n * (n - 1) // 2) & 1
            assert delta % modulus == required * phase, (n, h)
            phase_checks += 1
            if phase:
                assert valuation_two(delta) == a + 2, (n, h)
                sharp_checks += 1

    period_checks = 0
    strict_nonperiod_checks = 0
    for k in range(1, 12):
        modulus = 1 << k
        period = predicted_period(k)
        assert period * 2 <= N
        for n in range(period):
            assert values[n] % modulus == values[n + period] % modulus, (k, n)
            period_checks += 1
        for d in range(1, period):
            assert any(values[n] % modulus != values[n + d] % modulus for n in range(period)), (k, d)
            strict_nonperiod_checks += 1

    assert values[:9] == [1, 3, 13, 63, 321, 1683, 8989, 48639, 265729]
    print('VERIFY_OK',
          'independent_binomial_crosschecks=', crosschecks,
          'dyadic_phase_checks=', phase_checks,
          'sharp_valuation_checks=', sharp_checks,
          'period_entries=', period_checks,
          'shorter_period_exclusions=', strict_nonperiod_checks,
          'highest_modulus=', 1 << 11)


if __name__ == '__main__':
    run()
