"""Exact finite checks for covariance of binary-search-tree path length and right-spine size.

Uses only Python's standard library. Run: python verify.py
The universal theorem is established analytically; this program tests finite consequences.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial, pi, sqrt, log


def harmonic(n, power=1):
    return sum((Fraction(1, j ** power) for j in range(1, n + 1)), Fraction(0))


def quick_cost(sequence):
    """Independent first-pivot partition-count implementation."""
    if len(sequence) <= 1:
        return 0
    pivot = sequence[0]
    left = tuple(v for v in sequence[1:] if v < pivot)
    right = tuple(v for v in sequence[1:] if v > pivot)
    return len(sequence) - 1 + quick_cost(left) + quick_cost(right)


def max_search_visits(sequence):
    """Number of strict upper records, including the first element."""
    seen = 0
    records = 0
    for v in sequence:
        if v > seen:
            seen = v
            records += 1
    return records


def bst_total_depth(sequence):
    """Insert directly into a pointer-tree, independent of partition recursion."""
    root = None
    total = 0
    for value in sequence:
        if root is None:
            root = [value, None, None]
            continue
        cur = root
        depth = 0
        while True:
            depth += 1
            idx = 1 if value < cur[0] else 2
            if cur[idx] is None:
                cur[idx] = [value, None, None]
                total += depth
                break
            cur = cur[idx]
    return total


def check_enumerations():
    checked_permutations = 0
    for n in range(1, 9):
        cvals = []
        rvals = []
        for perm in permutations(range(1, n + 1)):
            c = quick_cost(perm)
            assert c == bst_total_depth(perm), (n, perm)
            cvals.append(c)
            rvals.append(max_search_visits(perm))
        count = factorial(n)
        assert len(cvals) == count
        checked_permutations += count
        Ec = Fraction(sum(cvals), count)
        Er = Fraction(sum(rvals), count)
        Cov = Fraction(sum(c * r for c, r in zip(cvals, rvals)), count) - Ec * Er
        H = harmonic(n)
        J = harmonic(n, 2)
        assert Ec == 2 * (n + 1) * H - 4 * n
        assert Er == H
        assert Cov == 3 * n + H - 2 * (n + 1) * J, (n, Cov)
        vc = Fraction(sum(c * c for c in cvals), count) - Ec * Ec
        vr = Fraction(sum(r * r for r in rvals), count) - Er * Er
        assert vc == 7 * n * n + 13 * n - 2 * (n + 1) * H - 4 * (n + 1) ** 2 * J
        assert vr == H - J
    return checked_permutations


def check_root_recurrence(max_n=120):
    H = [harmonic(j) for j in range(max_n + 1)]
    J = [harmonic(j, 2) for j in range(max_n + 1)]
    c = [2 * (j + 1) * H[j] - 4 * j for j in range(max_n + 1)]
    K = [Fraction(0)]
    for n in range(1, max_n + 1):
        a = [c[k] + c[n - 1 - k] for k in range(n)]
        b = H[:n]
        avg_a = sum(a, Fraction(0)) / n
        avg_b = sum(b, Fraction(0)) / n
        g = sum(((a[k] - avg_a) * (b[k] - avg_b) for k in range(n)), Fraction(0)) / n
        assert g == Fraction(3 * (n + 1), 2) - (n + 1) * J[n] - H[n] / n, (n, g)
        value = sum(K, Fraction(0)) / n + g
        assert value == 3 * n + H[n] - 2 * (n + 1) * J[n], (n, value)
        if n >= 3:
            assert g < 0 and value < 0
        else:
            assert g == 0 and value == 0
        K.append(value)
    return max_n


def check_asymptotic(n=200_000):
    H = sum(1.0 / j for j in range(1, n + 1))
    J = sum(1.0 / (j * j) for j in range(1, n + 1))
    observed = 3 + H / n - 2 * (n + 1) * J / n
    target = 3 - pi * pi / 3
    assert abs(observed - target) < 1e-4, (observed, target)
    vc = 7*n*n + 13*n - 2*(n+1)*H - 4*(n+1)**2*J
    vr = H - J
    corr = (n*observed) / sqrt(vc * vr)
    predicted = target / sqrt(7-2*pi*pi/3) / sqrt(log(n))
    assert corr < 0 and predicted < 0
    assert abs(corr / predicted - 1) < 0.1
    return observed, corr


if __name__ == '__main__':
    count = check_enumerations()
    rec_count = check_root_recurrence()
    asym_cov, asym_corr = check_asymptotic()
    print('PASS: checked {} permutations over n=1..8'.format(count))
    print('PASS: checked {} exact root-split/mixed-moment recurrences'.format(rec_count))
    print('PASS: asymptotic illustrations at n=200000: cov/n={:.10f}, corr={:.10f}'.format(asym_cov, asym_corr))
    print('Finite checks are not proofs of the infinite-domain conclusions.')
