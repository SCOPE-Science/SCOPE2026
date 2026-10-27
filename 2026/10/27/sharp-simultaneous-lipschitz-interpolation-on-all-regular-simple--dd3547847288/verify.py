"""Direct pairwise tests for a finite-dimensional Lipschitz extension theorem.

Uses only the Python standard library. These finite tests do not establish
universal quantifiers; the analytic proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import sqrt


def formula(n, k):
    assert n >= 4 and 3 <= k <= n - 1
    p = sqrt((k - 1) / (2 * k))
    q = sqrt((k + 1) / (2 * k))
    r = min(k, n - k)
    if r == 1:
        b = (k * p - (k - 1) * q) / (q + k * p)
        lam = (n - 1) / (q + k * p)
    else:
        b = (k * p * sqrt(r) - (k - 1)) / (n - k + n * k * p * sqrt(r))
        lam = k * sqrt(r) * (n - 1) / (n - k + n * k * p * sqrt(r))
    return lam, (1 - (n - k) * b) / k, b


def all_pairs(n, k):
    lam, a, b = formula(n, k)
    assert 0 < b < 1 / n < a
    faces = list(combinations(range(n), k))
    weights = [[float(i == j) for j in range(n)] for i in range(n)]
    weights.extend([[a if j in S else b for j in range(n)] for S in faces])
    kinds = [('vertex', i) for i in range(n)] + [('face', S) for S in faces]
    peak = 0.0
    total_pairs = 0
    for i in range(len(kinds)):
        for j in range(i + 1, len(kinds)):
            x, y = kinds[i], kinds[j]
            if x[0] == 'vertex' and y[0] == 'vertex':
                d = 1.0
            elif x[0] == 'face' and y[0] == 'face':
                d = sqrt(k - len(set(x[1]) & set(y[1]))) / k
            else:
                if x[0] == 'vertex':
                    x, y = y, x
                d = sqrt((k - 1 if y[1] in x[1] else k + 1) / (2 * k))
            norm = sum(abs(u - v) for u, v in zip(weights[i], weights[j])) / (2 * d)
            peak = max(peak, norm)
            total_pairs += 1
    assert abs(peak - lam) <= 2e-11, (n, k, peak, lam)
    p = sqrt((k - 1) / (2 * k))
    q = sqrt((k + 1) / (2 * k))
    naive = (1 / q if n - k == 1 else sqrt(min(k, n - k)))
    assert lam + 1e-9 < naive
    return total_pairs


def radical_comparison():
    unit = 10**9
    radicals = [(17, 4123105625, 4123105626),
                (2, 1414213562, 1414213563),
                (30, 5477225575, 5477225576)]
    for base, lo, hi in radicals:
        assert lo * lo < base * unit * unit < hi * hi
    l17 = 17 * Fraction(4123105625, unit) / (1 + 34 * Fraction(1414213563, unit))
    u16 = Fraction(64) / (1 + 8 * Fraction(5477225575, unit))
    assert l17 > u16
    return float(l17), float(u16)


def main():
    instances = 0
    pairs = 0
    for n in range(4, 10):
        for k in range(3, n):
            pairs += all_pairs(n, k)
            instances += 1
    l17, u16 = radical_comparison()
    print(f'PASS {instances} parameter pairs and {pairs} complete point-pair checks')
    print(f'PASS rational strict bound: L17 > {l17:.12f} > {u16:.12f} > L16')


if __name__ == '__main__':
    main()
