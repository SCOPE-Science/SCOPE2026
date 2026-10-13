"""Numerical cross-checks for the two-Poisson dispersion-order theorem.

Only the accompanying analytic proof establishes the continuous-parameter assertion.
Dependency-free: Python 3 standard library only.
"""
import math


def poisson_probs(rate):
    mass = [math.exp(-rate)]
    cap = max(20, int(rate + 25 * math.sqrt(rate) + 80))
    for k in range(cap):
        mass.append(mass[-1] * rate / (k + 1))
    assert math.fsum(mass) > 1 - 1e-13
    return mass


def moment_stats_from_pmf(pmf):
    mean = math.fsum(k * p for k, p in enumerate(pmf))
    variance = math.fsum((k - mean)**2 * p for k, p in enumerate(pmf))
    return mean, variance


def independent_order_stats(probs):
    minimum = []
    maximum = []
    cumulative = 0.0
    for p in probs:
        last = cumulative
        cumulative += p
        maximum.append((cumulative - last) * (cumulative + last))
        minimum.append(p * (2 - cumulative - last))
    return moment_stats_from_pmf(minimum), moment_stats_from_pmf(maximum)


def evaluate(rate):
    probs = poisson_probs(rate)
    a = math.fsum(p * p for p in probs)
    b = math.fsum(p * q for p, q in zip(probs, probs[1:]))
    c = a + b
    gap_bessel = b - rate * c**3
    upper_bound = (1 + 2 * rate)**(-0.5)
    qpoly = 2 - (2 + 4 * rate) * c**2 + 3 * rate * c**4
    assert gap_bessel > 0, (rate, gap_bessel)
    assert c < upper_bound, (rate, c, upper_bound)
    assert qpoly > 0, (rate, qpoly)
    fano_min = (1 - a - rate * c**2) / (1 - c)
    fano_max = (1 + a - rate * c**2) / (1 + c)
    assert fano_min > fano_max, rate
    min_stats, max_stats = independent_order_stats(probs)
    expect_means = [rate * (1 - c), rate * (1 + c)]
    expect_variances = [rate * (1 - a - rate*c*c), rate * (1 + a - rate*c*c)]
    for (mean, variance), expected_mean, expected_var in zip(
        (min_stats, max_stats), expect_means, expect_variances
    ):
        assert abs(mean - expected_mean) < 2e-9 * max(1, mean)
        assert abs(variance - expected_var) < 2e-8 * max(1, variance)
    assert abs((fano_min-fano_max) - 2*gap_bessel/(1-c*c)) < 2e-10
    return fano_min, fano_max, gap_bessel


def main():
    rates = [0.01,0.05,0.1,0.2,0.3,0.5,1,2,3,5,7,10,15,20,30,50,100]
    for rate in rates:
        ans = evaluate(rate)
        print(f"lambda={rate:g}: Fano(min)={ans[0]:.12f}, Fano(max)={ans[1]:.12f}")
    print(f"VERIFIED {len(rates)} intensity points using independent count-distribution calculations")

if __name__ == "__main__":
    main()
