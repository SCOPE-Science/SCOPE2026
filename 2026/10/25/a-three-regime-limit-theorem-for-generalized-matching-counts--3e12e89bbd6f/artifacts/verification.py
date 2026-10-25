"""Finite exact checks for the generalized matching phase-diagram formulas.
Run with Python 3; uses only the standard library. These checks do not prove
any asymptotic statement.
"""
from fractions import Fraction
from math import comb, factorial, exp, fsum


def derangements(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    a, b = 1, 0
    for k in range(2, n + 1):
        a, b = b, (k - 1) * (a + b)
    return b


def match_pmf(m, k):
    if k < 0 or k > m:
        return Fraction(0)
    return Fraction(derangements(m - k), factorial(k) * factorial(m - k))


def generalized_pmf(n, theta, k):
    out = Fraction(0)
    for ell in range(0, min(k, n) + 1):
        binom_prob = Fraction(comb(n, ell)) * theta**ell * (1 - theta)**(n - ell)
        out += binom_prob * match_pmf(n - ell, k - ell)
    return out


def moved_probability(r, d):
    if d < 0 or d > r:
        return Fraction(0)
    return Fraction(comb(r, d) * derangements(d), factorial(r))


def poissonized_moved_mass(mu, d, cutoff=100):
    """Direct finite truncation of the Poisson(R) mixture defining W_mu."""
    terms = []
    poisson = exp(-mu)
    for r in range(0, cutoff + 1):
        if r >= d:
            terms.append(poisson * float(moved_probability(r, d)))
        poisson *= mu / (r + 1)
    return fsum(terms)


def displayed_moved_mass(mu, d, cutoff=100):
    if mu == 0:
        return 1.0 if d == 0 else 0.0
    term = mu**d / factorial(d)
    terms = []
    for j in range(cutoff + 1):
        terms.append(term)
        term *= mu / ((d + j + 1) * (j + 1))
    return exp(-mu) * derangements(d) / factorial(d) * fsum(terms)


def run_checks():
    thetas = [Fraction(0), Fraction(1, 5), Fraction(1, 2), Fraction(4, 5), Fraction(1)]
    finite_cases = 0
    for n in range(0, 13):
        for theta in thetas:
            probs = [generalized_pmf(n, theta, k) for k in range(n + 1)]
            assert sum(probs, Fraction(0)) == 1, (n, theta, sum(probs))
            if n >= 1:
                assert probs[n - 1] == 0, (n, theta, probs[n - 1])
            mean = sum((k * probs[k] for k in range(n + 1)), Fraction(0))
            expected = Fraction(0) if n == 0 else 1 + n * theta - theta**n
            assert mean == expected, (n, theta, mean, expected)
            finite_cases += 1

    for mu in (0.25, 0.7, 1.0, 2.5):
        for d in range(0, 9):
            a = poissonized_moved_mass(mu, d, cutoff=80)
            b = displayed_moved_mass(mu, d, cutoff=80)
            assert abs(a - b) < 1e-12, (mu, d, a, b)
    assert derangements(1) == 0
    assert abs(sum(displayed_moved_mass(0.7, d, cutoff=100) for d in range(0, 25)) - 1) < 1e-10
    print(f"PASS: {finite_cases} exact finite convolution/normalization/mean cases")
    print("PASS: 36 finite-truncation comparisons for the Poissonized moved-point mass")
    print("PASS: one-mismatch probability is zero because D_1=0")
    print("Analytical proof remains necessary for all limiting claims.")


if __name__ == "__main__":
    run_checks()
