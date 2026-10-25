"""Exact finite checks for square-zero transformations and maximal null-semigroup containment.
Run: python check.py (standard-library only)."""
from itertools import product
from math import comb, factorial


def stirling_row(m):
    row = [1]
    for z in range(1, m + 1):
        new = [0] * (z + 1)
        for a, value in enumerate(row):
            new[a] += a * value
            new[a + 1] += value
        row = new
    return row


def optimal_sizes(n):
    vals = [pow(t, n - t) for t in range(1, n + 1)]
    highest = max(vals)
    return [t for t, value in enumerate(vals, 1) if value == highest]


def exact_counts(n):
    candidates = optimal_sizes(n)
    low, high = min(candidates), max(candidates)
    total = 0
    extendible = 0
    for b in range(1, n + 1):
        base = n * comb(n - 1, b - 1)
        total += base * ((b - 1) ** (n - b))
        if b < low:
            continue
        row = stirling_row(n - b)
        for a in range(min(high - 1, b - 1, n - b) + 1):
            extendible += base * comb(b - 1, a) * factorial(a) * row[a]
    return total, extendible


def direct_counts(n):
    if n > 7:
        raise ValueError('Direct enumeration limited to seven points')
    low, high = min(optimal_sizes(n)), max(optimal_sizes(n))
    total = extendible = 0
    for f in product(range(n), repeat=n):
        sq = [f[f[x]] for x in range(n)]
        if len(set(sq)) != 1:
            continue
        c = sq[0]
        assert f[c] == c
        total += 1
        b = sum(y == c for y in f)
        k = len(set(f))
        if any(k <= t <= b for t in optimal_sizes(n)):
            extendible += 1
        assert (low <= b and k <= high) == any(k <= t <= b for t in optimal_sizes(n))
    return total, extendible


def verify():
    print('n | optimal sizes | square-zero | extendible | direct equality')
    tested = 0
    for n in range(2, 8):
        actual = direct_counts(n)
        formula = exact_counts(n)
        assert actual == formula, (n, actual, formula)
        print(f'{n} | {optimal_sizes(n)} | {actual[0]} | {actual[1]} | PASS')
        tested += n ** n
    print(f'ALL_NULL_CONTAINMENT_CHECKS_PASSED orders=2..7 transformations={tested}')


if __name__ == '__main__':
    verify()
