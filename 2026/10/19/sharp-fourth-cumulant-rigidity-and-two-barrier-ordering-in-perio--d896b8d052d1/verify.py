"""Finite exact checks of the fourth-cumulant corrector-variance identity."""

from itertools import combinations
from sympy import Rational, eye, factorial, ones, zeros


def cumulants(resistance):
    n = len(resistance)
    one = ones(n, 1)
    generators = [zeros(n) for _ in range(5)]
    for i in range(n):
        for direction, edge in ((1, i), (-1, (i - 1) % n)):
            j = (i + direction) % n
            rate = 1 / resistance[edge]
            generators[0][i, i] -= rate
            for order in range(5):
                generators[order][i, j] += rate * direction**order / factorial(order)
    projection = eye(n) - one * one.T / n
    inverse_on_mean_zero = (generators[0] + one * one.T / n).inv() * projection
    eigenvector = [one]
    eigenvalue = [0]
    for order in range(1, 5):
        forcing = zeros(n, 1)
        for j in range(1, order + 1):
            forcing += generators[j] * eigenvector[order - j]
        eigenvalue.append(sum(forcing) / n)
        for j in range(1, order):
            forcing -= eigenvalue[j] * eigenvector[order - j]
        eigenvector.append(-inverse_on_mean_zero * forcing)
    assert eigenvalue[1] == eigenvalue[3] == 0
    return 2 * eigenvalue[2], 24 * eigenvalue[4]


def check(resistance):
    n = len(resistance)
    total = sum(resistance)
    primitive = [n * sum(resistance[:j]) / total - j for j in range(n)]
    chi = [u - sum(primitive) / n for u in primitive]
    assert sum(chi) == 0
    for i in range(n):
        assert (1 + chi[(i + 1) % n] - chi[i]) / resistance[i] == n / total
    variance = sum(u * u for u in chi) / n
    k = 0
    for i, j in combinations(range(n), 2):
        arc = sum(resistance[i:j])
        k += arc * (total - arc) / total
    assert k == total * (Rational(n * n - 1, 12) - variance)
    second, fourth = cumulants(resistance)
    assert second == 2 * n / total
    assert fourth == second * (1 + 12 * variance)


if __name__ == '__main__':
    count = 0
    for n in range(3, 9):
        check([Rational(3, 2)] * n)
        count += 1
        for r in range(7):
            check([Rational(1 + (j*j + 3*r*j + r*r + n) % 23,
                            1 + (2*j + r + n) % 13) for j in range(n)])
            count += 1
    print(f'{count} exact cumulant, harmonic-coordinate and resistance-deficit comparisons passed')
