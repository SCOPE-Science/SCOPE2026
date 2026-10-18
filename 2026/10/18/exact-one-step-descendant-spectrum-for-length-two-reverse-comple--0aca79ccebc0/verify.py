"""Exact finite cross-checks for reverse-complement length-two duplication.

Usage: python verify.py
Python >=3.9, standard library only.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def reverse_complement_pair(a, b):
    return b ^ 1, a ^ 1


def outputs(w):
    n = len(w)
    return [w[:i + 2] + reverse_complement_pair(w[i], w[i + 1]) + w[i + 2:]
            for i in range(n - 1)]


def alternating_segment(w, i, j):
    return all(w[k + 1] == (w[k] ^ 1) for k in range(i, j + 1))


def collision_count(w):
    return sum(w[i] == w[i + 2] and w[i + 1] == (w[i] ^ 1)
               for i in range(len(w) - 2))


def polynomial_multiply_linear(p, a, b):
    out = Counter()
    for power, coeff in p.items():
        out[power] += a * coeff
        out[power + 1] += b * coeff
    return out


def theoretical_histogram(q, n):
    # State 0: adjacent pair not complementary; state 1: complementary.
    x = Counter({0: q * (q - 1)})
    y = Counter({0: q})
    for _ in range(n - 2):
        nx = Counter({j: (q - 1) * (x[j] + y[j]) for j in set(x) | set(y)})
        ny = x.copy()
        for j, v in y.items():
            ny[j + 1] += v
        x, y = nx, ny
    return x + y


def expected_variance(q, n):
    mu = Fraction(n - 1, 1) - Fraction(n - 2, q*q)
    if n == 2:
        return mu, Fraction(0)
    va = Fraction((n - 2) * (q*q - 1) + 2 * (n - 3) * (q - 1), q**4)
    return mu, va


def check(q, n):
    hist = Counter()
    for w in product(range(q), repeat=n):
        found = outputs(w)
        k = collision_count(w)
        assert len(set(found)) == n - 1 - k, (q, n, w, 'sphere')
        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                assert (found[i] == found[j]) == alternating_segment(w, i, j), \
                    (q, n, w, i, j, 'collision')
        hist[k] += 1
    assert hist == theoretical_histogram(q, n), (q, n, hist, theoretical_histogram(q, n))
    assert sum(hist.values()) == q**n
    mu, va = expected_variance(q, n)
    check_mu = sum((n - 1 - k) * count for k, count in hist.items()) / Fraction(q**n)
    check_var = sum((n - 1 - k - mu)**2 * count for k, count in hist.items()) / Fraction(q**n)
    assert mu == check_mu and va == check_var, (q, n, va, check_var)
    if n >= 3:
        assert hist[n - 2] == q, (q, n, 'min sphere')
    return hist


def verify_rational_recurrence(q, nmax=35):
    # Coefficient of t^(n-2) in
    # q(q+(q-1)(1-z)t) / (1-(q-1+z)t+(q-1)(z-1)t^2).
    p2 = Counter({0: q*q})
    p3 = Counter({0: q**3 - q, 1: q})
    assert theoretical_histogram(q, 2) == p2
    assert theoretical_histogram(q, 3) == p3
    previous2, previous1 = p2, p3
    for n in range(4, nmax + 1):
        now = polynomial_multiply_linear(previous1, q-1, 1)
        subtractor = polynomial_multiply_linear(previous2, -(q-1), q-1)
        for power, coeff in subtractor.items():
            now[power] -= coeff
        now = Counter({k: v for k, v in now.items() if v})
        assert now == theoretical_histogram(q, n), (q, n)
        previous2, previous1 = previous1, now


def main():
    for q, max_n in [(2, 12), (4, 7), (6, 5), (8, 4)]:
        for n in range(2, max_n+1):
            check(q, n)
        verify_rational_recurrence(q)
        print('PASS q=', q, 'exhaustive n=2..', max_n, 'recurrence n=2..35')
    print('PASS: collision iff complement-alternating interval; complete distribution and moments')


if __name__ == '__main__':
    main()
