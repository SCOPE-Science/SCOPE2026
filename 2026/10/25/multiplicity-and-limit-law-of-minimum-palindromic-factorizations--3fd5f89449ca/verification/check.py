"""Independent exact checks for minimum-palindrome-factorization multiplicities.

This program uses only the Python standard library. It tests counts of distinct
positional cuts, not merely one optimal factorization. No outside data is used.
"""
from collections import Counter
from itertools import product
from math import comb
from random import Random


def predicted(a, b, c, d, e):
    if b == d:
        if a == e:
            return 1, 1
        return 2, 1 + (c == a + e)
    if c == a + e:
        return 2, 1
    if c < min(a, e):
        return 4, c + 2
    multiplicity = (
        (c == a) + (c == e)
        + (e < c < a + e) + (a < c < a + e)
        + (c > a + e)
    )
    return 3, multiplicity


def direct_dynamic_programming(a, b, c, d, e):
    word = '0' * a + '1' * b + '0' * c + '1' * d + '0' * e
    n = len(word)
    # Palindrome truth computed independently by symmetry on every interval.
    pal = [[False] * (n + 1) for _ in range(n + 1)]
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            end = start + length
            pal[start][end] = (
                word[start] == word[end - 1]
                and (length < 3 or pal[start + 1][end - 1])
            )
    distance = [n + 1] * (n + 1)
    counts = [0] * (n + 1)
    distance[0] = 0
    counts[0] = 1
    for end in range(1, n + 1):
        for start in range(end):
            if not pal[start][end]:
                continue
            new_distance = distance[start] + 1
            if new_distance < distance[end]:
                distance[end] = new_distance
                counts[end] = counts[start]
            elif new_distance == distance[end]:
                counts[end] += counts[start]
    return distance[n], counts[n]


def compositions5(n):
    for a in range(1, n - 3):
        for b in range(1, n - a - 2):
            for c in range(1, n - a - b - 1):
                for d in range(1, n - a - b - c):
                    e = n - a - b - c - d
                    if e >= 1:
                        yield a, b, c, d, e


def gf_coefficient(n, c):
    # Coefficient of z^n v^(c+2) in
    # 2*z^8*v^3/((1-z)^3*(1-z^2)*(1-z^3*v)).
    residual = n - 3 * c - 5
    if residual < 0:
        return 0
    return 2 * sum(comb(residual - 2 * j + 2, 2)
                   for j in range(residual // 2 + 1))


def main():
    checked = 0
    for params in product(range(1, 7), repeat=5):
        expected = predicted(*params)
        observed = direct_dynamic_programming(*params)
        assert observed == expected, (params, expected, observed)
        checked += 1
    rng = Random(2026)
    large = 0
    for _ in range(400):
        params = tuple(rng.randrange(1, 24) for _ in range(5))
        assert predicted(*params) == direct_dynamic_programming(*params), params
        large += 1
    gf_checks = 0
    for n in range(5, 31):
        grouped = Counter()
        best = 0
        for params in compositions5(n):
            pl, k = predicted(*params)
            best = max(best, k)
            if pl == 4:
                grouped[params[2]] += 1
        for c in range(1, n + 1):
            assert grouped[c] == gf_coefficient(n, c), (n, c, grouped[c])
            gf_checks += 1
        expected_max = 1 if n == 5 else 2 if n < 8 else 2 + (n - 5) // 3
        assert best == expected_max, (n, best, expected_max)
    # Finitary sanity checks only; asymptotic claims are proved analytically.
    assert sum(gf_coefficient(8, c) for c in range(1, 9)) == 2
    assert sum(gf_coefficient(9, c) for c in range(1, 10)) == 6
    print('VERIFY_OK dp_five_run=%d large_instances=%d gf_coefficients=%d lengths=5..30' %
          (checked, large, gf_checks))

if __name__ == '__main__':
    main()
