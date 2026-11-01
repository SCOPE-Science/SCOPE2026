"""Exact finite consistency checks for the path maximal variation theorem.

Finite enumeration is not a proof of the quantified theorem.
"""
from fractions import Fraction
from itertools import product


def maximal(values):
    n = len(values)
    answer = []
    for i in range(n):
        averages = []
        for r in range(n):
            lo = max(0, i - r)
            hi = min(n, i + r + 1)
            averages.append(Fraction(sum(values[lo:hi]), hi - lo))
        answer.append(max(averages))
    return answer


def var(values):
    return sum(abs(values[i + 1] - values[i]) for i in range(len(values) - 1))


def unimodal_at(values, k):
    return all(values[i] <= values[i + 1] for i in range(k)) and all(
        values[i] >= values[i + 1] for i in range(k, len(values) - 1)
    )


def check(values):
    n = len(values)
    y = maximal(values)
    for k in range(n):
        if not unimodal_at(values, k):
            continue
        p = values[k]
        assert unimodal_at(y, k), (values, y, k)
        assert y[k] == p
        lhs = var(y)
        prefix = Fraction(sum(values[: k + 1]), k + 1)
        suffix = Fraction(sum(values[k:]), n - k)
        assert lhs == 2 * p - y[0] - y[-1]
        assert lhs <= 2 * p - prefix - suffix
        assert lhs <= var(values) - Fraction(p - values[0], k + 1) - Fraction(
            p - values[-1], n - k
        )
        assert lhs <= Fraction(n - 1, n) * var(values)
        if 0 < k < n - 1 and values[0] == values[-1] == 0 and p > 0:
            C = Fraction(1) - Fraction(1, 2 * (k + 1)) - Fraction(
                1, 2 * (n - k)
            )
            rem = Fraction(sum(values[1:k]), k + 1) + Fraction(
                sum(values[k + 1 : n - 1]), n - k
            )
            assert C * var(values) - lhs >= rem
            if C * var(values) == lhs:
                assert all(values[i] == 0 for i in range(n) if i != k)


count = 0
for n in range(3, 9):
    for v in product(range(4), repeat=n):
        if not any(unimodal_at(v, k) for k in range(n)):
            continue
        check(v)
        count += 1
    for k in range(1, n - 1):
        v = [0] * n
        v[k] = 7
        y = maximal(v)
        c = Fraction(1) - Fraction(1, 2 * (k + 1)) - Fraction(1, 2 * (n - k))
        assert var(y) == c * var(v)
        count += 1
    for end in (0, n - 1):
        v = [3] * n
        v[end] = 8
        assert var(maximal(v)) == Fraction(n - 1, n) * var(v)
        count += 1
print('EXACT_CHECK_OK', count)
