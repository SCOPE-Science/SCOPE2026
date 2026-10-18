"""Reproduce exact Stirling/Irwin--Hall identities and numerical TV benchmarks.

Run: python3 verify.py
Uses Python standard library only. Computations are finite checks, not a
replacement for the proof of the limiting theorem.
"""
from fractions import Fraction
from math import comb, factorial, lgamma, log, exp, fsum, sqrt, pi


def stirling_column(k, last):
    # Bell triangle gives S(j,k) for j=0,...,last.
    rows = [[1]]
    for j in range(1, last + 1):
        old = rows[-1]
        row = [0] * (j + 1)
        for h in range(1, j + 1):
            row[h] = h * (old[h] if h < len(old) else 0) + old[h - 1]
        rows.append(row)
    return [rows[j][k] if k <= j else 0 for j in range(last + 1)]


def exact_check():
    cases = 0
    for k in range(1, 6):
        for R in range(2, 12):
            S = stirling_column(k, k + R)
            for phi in (1, 2, 5):
                # Two independently specified weight systems.
                w_sp = [comb(k + R, k + j) * phi ** (R - j) * S[k + j]
                        for j in range(R + 1)]
                w_mix = [Fraction(comb(R, j) * phi ** (R - j) * S[k + j],
                                  comb(k + j, k)) for j in range(R + 1)]
                factor = comb(k + R, k)
                assert all(Fraction(a, 1) == factor * b for a, b in zip(w_sp, w_mix))
                total = sum(w_sp)
                probabilities = [Fraction(a, total) for a in w_sp]
                assert sum(probabilities) == 1
                mean = sum(j * p for j, p in enumerate(probabilities))
                fac2 = sum(j * (j - 1) * p for j, p in enumerate(probabilities))
                q_mean = mean / R
                q_variance = fac2 / (R * (R - 1)) - q_mean ** 2
                assert q_variance > 0, (k, R, phi, q_variance)
                variance = sum((j - mean) ** 2 * p for j, p in enumerate(probabilities))
                assert variance - R * q_mean * (1 - q_mean) == R * (R - 1) * q_variance
                cases += 1
    return cases


def tv_approx(k, phi, R):
    S = stirling_column(k, k + R)
    q = k / (k + phi)
    log_weights = [lgamma(k + R + 1) - lgamma(k + j + 1)
                   - lgamma(R - j + 1) + (R - j) * log(phi) + log(S[k + j])
                   for j in range(R + 1)]
    top = max(log_weights)
    weights = [exp(v - top) for v in log_weights]
    norm = fsum(weights)
    trial = [exp(lgamma(R + 1) - lgamma(j + 1) - lgamma(R - j + 1)
                 + j * log(q) + (R - j) * log(1 - q)) for j in range(R + 1)]
    return 0.5 * fsum(abs(a / norm - b) for a, b in zip(weights, trial))


def main():
    cases = exact_check()
    print('EXACT CHECKS PASSED:', cases)
    for k, phi in ((1, 1), (2, 3), (3, 1), (5, 5)):
        predicted = sqrt(k * phi / (2 * pi))
        output = []
        for R in (200, 500, 1000):
            observed = sqrt(R) * tv_approx(k, phi, R)
            output.append((R, round(observed, 8)))
        assert abs(output[-1][1] - predicted) < 0.20 * predicted
        print('k={}, phi={}, target={:.8f}, sqrt(R)*TV={}'.format(
            k, phi, predicted, output))
    print('Numerical checks demonstrate convergence, not a proof of an infinite limit.')


if __name__ == '__main__':
    main()
