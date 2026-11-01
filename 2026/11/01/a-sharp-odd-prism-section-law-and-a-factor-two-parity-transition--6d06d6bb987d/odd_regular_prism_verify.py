"""Independent numerical and geometric checks for odd regular-prism central sections.
Run with Python 3 standard library: python odd_regular_prism_verify.py
These finite checks corroborate, but do not replace, the general proof.
"""
import math
import random


def maximal_section_probability(n, h):
    assert n >= 5 and n % 2 == 1 and h > 0
    delta = math.pi / n
    t = 1 / math.sqrt(1 + h * h)
    H = lambda x: math.asin(t * math.sin(x))
    return (2 / delta) * (2 * H(delta) - H(delta / 2) - H(3 * delta / 2))


def side_count_by_edges(n, h, azimuth, z):
    rho = math.sqrt(1 - z * z)
    a = [rho * math.cos(azimuth - 2 * math.pi * j / n) for j in range(n)]
    low = [x - h * z for x in a]
    high = [x + h * z for x in a]
    return sum(low[j] * high[j] < 0 for j in range(n)) + sum(
        (low[j] * low[(j + 1) % n] < 0) + (high[j] * high[(j + 1) % n] < 0)
        for j in range(n)
    )


def side_count_by_threshold(n, h, azimuth, z):
    rho = math.sqrt(1 - z * z)
    s = h * abs(z)
    a = [rho * math.cos(azimuth - 2 * math.pi * j / n) for j in range(n)]
    plus = sum(x > s for x in a)
    minus = sum(x < -s for x in a)
    return n - plus - minus + 2 * (plus > 0) + 2 * (minus > 0)


def angular_integral(n, h, count=4000):
    delta = math.pi / n
    F = lambda x: math.cos(x) / math.sqrt(h*h + math.cos(x)**2)
    step = delta / (2 * count)
    return 2 / delta * step * (sum(
        (F(delta - (j+0.5)*step) - F(delta + (j+0.5)*step))
        for j in range(count)
    ))


def main():
    rng = random.Random(20261030)
    for n, h in [(5, .7), (5, 1.0), (5, 2.0), (7, 1.0), (9, 1.5)]:
        exact = maximal_section_probability(n, h)
        integral = angular_integral(n, h)
        assert abs(exact - integral) < 2e-9, (n, h, exact, integral)
        trials = 50000
        matches = 0
        for _ in range(trials):
            phi = rng.random() * 2 * math.pi
            z = 2 * rng.random() - 1
            k = side_count_by_edges(n, h, phi, z)
            assert k == side_count_by_threshold(n, h, phi, z)
            assert k <= n + 2
            matches += k == n + 2
        frequency = matches / trials
        assert abs(frequency-exact) < 0.015, (n, h, exact, frequency)
        print('FINITE_N_AND_INDEPENDENT_INTEGRAL_PASSED', n, h, exact, frequency)
    for n in [51, 101, 501]:
        h = math.sqrt(2)
        target = math.pi**2 / (3*math.sqrt(3))
        scaled = n*n*maximal_section_probability(n, h)
        assert abs(scaled - target) < 1.0/n
        print('SHARP_ODD_PARITY_ASYMPTOTIC_DIAGNOSTIC_PASSED', n, scaled)
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
