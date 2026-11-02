"""Independent finite checks of the exact anti-confirmation map classification.

Run with Python 3.10+: python verify_rotation.py
This code checks identities and finite instances; the infinite statements use
an analytical rotation conjugacy and arithmetic proof in RESULT.md.
"""
from fractions import Fraction
from math import floor, log, exp, isclose


def odds_step(w, g_low, g_high):
    return w / (g_low if w < 1 else g_high)


def bayes_step(x, g_low, g_high):
    g = g_low if x < Fraction(1, 2) else g_high
    return x / (x + g * (1 - x))


def finite_arithmetic_checks():
    checked = 0
    for low, high in [(Fraction(1, 4), Fraction(4)),
                      (Fraction(1, 4), Fraction(16)),
                      (Fraction(22, 125), Fraction(93, 50)),
                      (Fraction(3, 17), Fraction(13, 7))]:
        a, b = log(1 / float(low)), log(float(high))
        length = a + b
        for initial_odds in [Fraction(1, 7), Fraction(2, 3),
                             Fraction(1), Fraction(3, 2), Fraction(12)]:
            w = initial_odds
            x = w / (1 + w)
            first_inside = False
            for k in range(101):
                assert w == x / (1 - x)
                if Fraction(1, 1) / high <= w < Fraction(1, 1) / low:
                    first_inside = True
                if first_inside:
                    assert Fraction(1, 1) / high <= w < Fraction(1, 1) / low
                w = odds_step(w, low, high)
                x = bayes_step(x, low, high)
                checked += 1
            assert first_inside
            # A dynamical check independent of the exact fractional powers.
            wr = float(initial_odds)
            for _ in range(35):
                if 1 / float(high) <= wr < 1 / float(low):
                    break
                wr = wr / (float(low) if wr < 1 else float(high))
            else:
                raise AssertionError('failed to enter trapping interval')
            t0 = (log(wr) + b) / length
            assert -1e-11 <= t0 < 1 + 1e-11
            wr_fraction = Fraction(initial_odds)
            for _ in range(35):
                if Fraction(1, 1)/high <= wr_fraction < Fraction(1, 1)/low:
                    break
                wr_fraction = odds_step(wr_fraction, low, high)
            high_count = 0
            for k in range(80):
                high_count += int(wr_fraction >= 1)
                wr_fraction = odds_step(wr_fraction, low, high)
                pred = floor(t0 + (k + 1) * a / length + 1e-12)
                assert high_count == pred, (low, high, initial_odds, k)
                checked += 1
    return checked


def exact_resonance_checks():
    for low, high, period in [
        (Fraction(1, 4), Fraction(4), 2),
        (Fraction(1, 4), Fraction(16), 3),
    ]:
        for w0 in [Fraction(2, 3), Fraction(1), Fraction(3, 2)]:
            assert Fraction(1, 1) / high <= w0 < Fraction(1, 1) / low
            w = w0
            for _ in range(period):
                w = odds_step(w, low, high)
            assert w == w0
            for k in range(1, period):
                x = w0
                for _ in range(k):
                    x = odds_step(x, low, high)
                assert x != w0
    return 6


def rotation_and_frequency_checks():
    low, high = 22 / 125, 93 / 50
    a, b = log(1 / low), log(high)
    length = a + b
    rho = a / length
    for t0 in (0.07, 0.12345678, 0.4, 0.93):
        n_high = 0
        for n in range(50000):
            t = (t0 + n * rho) % 1
            is_high = t >= 1 - rho
            n_high += is_high
            assert n_high == floor(t0 + (n + 1) * rho + 1e-9)
            assert abs(n_high - (n + 1) * rho) < 1
    sample = 200000
    t0 = 0.12345678
    empirical = sum(1 / (1 + exp(b - length * ((t0 + k * rho) % 1)))
                    for k in range(sample)) / sample
    theoretical = (log(1 + exp(a)) - log(1 + exp(-b))) / length
    assert abs(empirical - theoretical) < 2e-4, (empirical, theoretical)
    assert abs(rho - 0.736803836455561) < 1e-13
    assert abs(theoretical - 0.6230872976476242) < 1e-13
    return sample, empirical, theoretical


if __name__ == '__main__':
    print('Exact rational and itinerary checks:', finite_arithmetic_checks())
    print('Rational resonance cases:', exact_resonance_checks())
    n, empirical, theo = rotation_and_frequency_checks()
    print('Irrational model: mean after', n, 'rotation steps =', format(empirical, '.9f'),
          '; predicted =', format(theo, '.9f'))
    print('All finite checks passed.')
