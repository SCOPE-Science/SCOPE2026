"""Numerical spot checks for the finite-Hankel small-bandwidth spectral law.

Dependencies: Python 3 and mpmath (tested with 1.3.0). No data downloads.
The analytic proof, not this finite computation, covers all indices and parameters.
"""
import mpmath as mp

mp.mp.dps = 65


def monic_orthogonal(alpha, order):
    polynomials = []
    norms = []

    def inner(p, q):
        return sum(p[i] * q[j] / (2 * (alpha + i + j + 1))
                   for i in range(len(p)) for j in range(len(q)))

    for n in range(order):
        p = [mp.mpf(0)] * n + [mp.mpf(1)]
        for j in range(n):
            coefficient = inner(p, polynomials[j]) / norms[j]
            for k in range(j + 1):
                p[k] -= coefficient * polynomials[j][k]
        polynomials.append(p)
        norms.append(inner(p, p))
        binomial = mp.binomial(2 * n + alpha, n)
        expected = 1 / (2 * (2 * n + alpha + 1) * binomial ** 2)
        assert mp.almosteq(norms[-1], expected, rel_eps=mp.mpf('1e-48'))
    return polynomials, norms


def run(alpha, bandwidth, order=7, series_terms=13):
    alpha = mp.mpf(alpha)
    c = mp.mpf(bandwidth)
    p, h = monic_orthogonal(alpha, order)
    matrix = mp.matrix(order)
    for k in range(series_terms):
        b = (-1) ** k / (2 ** (alpha + 2 * k) * mp.factorial(k) * mp.gamma(alpha + k + 1))
        overlap = [sum(p[j][i] / (2 * (alpha + i + k + 1)) for i in range(j + 1)) / mp.sqrt(h[j])
                   for j in range(order)]
        for i in range(order):
            for j in range(order):
                matrix[i, j] += c ** (alpha + mp.mpf('0.5') + 2 * k) * b * overlap[i] * overlap[j]
    eigenvalues, _ = mp.eigsy(matrix)
    singular_values = sorted((abs(e) for e in eigenvalues), reverse=True)
    for n in range(3):
        b_abs = 1 / (2 ** (alpha + 2 * n) * mp.factorial(n) * mp.gamma(alpha + n + 1))
        predicted = c ** (alpha + mp.mpf('0.5') + 2 * n) * b_abs * h[n]
        ratio = singular_values[n] / predicted
        assert abs(ratio - 1) < mp.mpf('0.015'), (alpha, c, n, ratio)
        print('alpha=', alpha, 'c=', c, 'mode=', n, 'ratio=', mp.nstr(ratio, 16))


if __name__ == '__main__':
    for alpha in ('0', '0.5'):
        for c in ('0.2', '0.4'):
            run(alpha, c)
    print('All finite numerical checks passed; these are not a proof of the general theorem.')
