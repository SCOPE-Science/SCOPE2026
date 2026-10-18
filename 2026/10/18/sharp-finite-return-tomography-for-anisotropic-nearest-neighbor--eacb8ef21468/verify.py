"""Exact finite diagnostics for finite-return tomography of nearest-neighbor walks.

Run with: python3 verify.py
Uses only Python's standard library. The general theorem requires its analytical proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial


def bessel_log_coefficients(m):
    """Coefficients of log(I_0(z)) as a series in z^2."""
    c = [F(0)] * (m + 1)
    c[1] = F(1, 4)
    for n in range(2, m + 1):
        c[n] = -sum(F(k * (n - k), n * n) * c[k] * c[n - k]
                    for k in range(1, n))
    return c


def return_coefficients(h, m):
    """Exact probability of return at times 0,2,...,2m."""
    a = [F(1)] + [F(0)] * m
    for weight in h:
        b = [(weight / 2) ** (2 * j) / factorial(j) ** 2
             for j in range(m + 1)]
        a = [sum(a[i] * b[k - i] for i in range(k + 1))
             for k in range(m + 1)]
    return [factorial(2 * k) * a[k] for k in range(m + 1)]


def log_coefficients_of_return_egf(r):
    """Formal log of sum r_2m z^(2m)/(2m)!, in w=z^2."""
    m = len(r) - 1
    a = [r[k] / factorial(2 * k) for k in range(m + 1)]
    b = [F(0)] * (m + 1)
    for n in range(1, m + 1):
        b[n] = a[n] - sum(F(k, n) * b[k] * a[n - k]
                           for k in range(1, n))
    return b


def newton_elementaries(power_sums):
    e = [F(1)]
    for n in range(1, len(power_sums) + 1):
        e.append(sum((-1) ** (k - 1) * e[n - k] * power_sums[k - 1]
                     for k in range(1, n + 1)) / n)
    return e


def determinant(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    det = F(1)
    for i in range(n):
        pivot = next((j for j in range(i, n) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            det = -det
        x = a[i][i]
        det *= x
        for j in range(i + 1, n):
            factor = a[j][i] / x
            a[j] = [u - factor * v for u, v in zip(a[j], a[i])]
    return det


def main():
    checks = 0
    def verify(predicate, message):
        nonlocal checks
        assert predicate, message
        checks += 1

    c = bessel_log_coefficients(12)
    for m in range(1, 13):
        verify((-1) ** (m - 1) * c[m] > 0,
               'coefficient sign %s' % m)

    for d in range(2, 9):
        h = [F(i, d * (d + 1) // 2) for i in range(1, d + 1)]
        mmax = min(9, d + 2)
        return_prob = return_coefficients(h, mmax)
        series_log = log_coefficients_of_return_egf(return_prob)
        for m in range(1, mmax + 1):
            s = sum(v ** (2 * m) for v in h)
            verify(series_log[m] == c[m] * s, 'Bessel log identity')
            verify(0 <= return_prob[m] <= 1, 'return probability range')
        inferred = [series_log[m] / c[m] for m in range(1, d)]
        actual = [sum(v ** (2 * m) for v in h) for m in range(1, d)]
        verify(inferred == actual, 'power-sum inversion')
        e = newton_elementaries(inferred)
        for k in range(1, d):
            verify(e[k] == sum_product_squares(h, k), 'Newton inversion')
        if d >= 3:
            # Rank of constraints: sum h_i and even moments through 2(d-2).
            jac = [[F(1)] * (d - 1)]
            for k in range(1, d - 1):
                jac.append([2 * k * h[j] ** (2 * k - 1)
                            for j in range(d - 1)])
            verify(determinant(jac) != 0, 'Jacobian full rank')
        # Renewal conversion first-return <-> ordinary-return coefficients.
        first = [F(0)] * (mmax + 1)
        first[0] = F(0)
        for m in range(1, mmax + 1):
            first[m] = return_prob[m] - sum(
                first[k] * return_prob[m-k] for k in range(1, m))
            verify(first[m] >= 0, 'first-return probability nonnegative')
            verify(return_prob[m] == sum(
                first[k] * return_prob[m-k] for k in range(1, m+1)),
                'first-return renewal inversion')

    # An explicit pair of nonpermutation 3-axis weights with one identical
    # even-time return probability (insufficient for d=3).
    found = None
    for total in range(8, 55):
        seen = {}
        for a in range(1, total):
            for b in range(a, total):
                z = total - a - b
                if z < b:
                    break
                if a >= b or b >= z:
                    continue
                key = a * a + b * b + z * z
                if key in seen:
                    found = (total, seen[key], (a, b, z))
                    break
                seen[key] = (a, b, z)
            if found:
                break
        if found:
            break
    verify(found is not None, 'sharpness witness in dimension three')
    total, u, v = found
    hu = [F(x, total) for x in u]
    hv = [F(x, total) for x in v]
    verify(hu != hv and sum(hu) == sum(hv) == 1, 'distinct weight vectors')
    verify(return_coefficients(hu, 1) == return_coefficients(hv, 1),
           'same two-step return')
    verify(return_coefficients(hu, 2) != return_coefficients(hv, 2),
           'different four-step return')

    print('PASS: %s exact rational checks' % checks)
    print('Dimension-three sharpness example with denominator %s: %s versus %s' %
          (total, u, v))
    print('All finite tests supplement, not replace, the analytical proof.')


def sum_product_squares(h, k):
    total = F(0)
    for combo in combinations(h, k):
        prod = F(1)
        for weight in combo:
            prod *= weight * weight
        total += prod
    return total


if __name__ == '__main__':
    main()
