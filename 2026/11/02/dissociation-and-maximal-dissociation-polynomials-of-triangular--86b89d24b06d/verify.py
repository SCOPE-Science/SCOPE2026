"""Direct finite checks for dissociation sets in triangular graphs.

Uses only the Python standard library. Run with ``python verify.py``.
The upper cutoff for n >= 7 comes from the independent size bound in RESULT.md.
"""
from collections import Counter
from itertools import combinations
from math import factorial, floor, ceil


def expected_all(n):
    out = Counter()
    for b in range(n // 3 + 1):
        for a in range((n - 3 * b) // 2 + 1):
            u = n - 3 * b - 2 * a
            out[a + 2 * b] += factorial(n) // (
                factorial(u) * 2 ** (a + b) * factorial(a) * factorial(b)
            )
    return +out


def expected_maximal(n):
    out = Counter()
    for b in range(n // 3 + 1):
        if (n - 3 * b) % 2:
            continue
        a = (n - 3 * b) // 2
        out[a + 2 * b] += factorial(n) // (
            2 ** (a + b) * factorial(a) * factorial(b)
        )
    if (n - 1) % 3 == 0:
        b = (n - 1) // 3
        out[2 * b] += factorial(n) // (2 ** b * factorial(b))
    return +out


def direct(n, exhaustive=False):
    vertices = list(combinations(range(n), 2))
    v_count = len(vertices)
    neighbors = [sum(1 << k for k, f in enumerate(vertices)
                     if j != k and (e[0] in f or e[1] in f))
                 for j, e in enumerate(vertices)]
    full = Counter()
    maximal = Counter()
    tested = 0
    upper = v_count if exhaustive else floor(2 * n / 3)
    for k in range(upper + 1):
        for chosen in combinations(range(v_count), k):
            tested += 1
            mask = sum(1 << i for i in chosen)
            if any((neighbors[i] & mask).bit_count() > 1 for i in chosen):
                continue
            full[k] += 1
            extendible = any(
                (neighbors[j] & mask).bit_count() <= 1 and
                all((neighbors[i] & (mask | (1 << j))).bit_count() <= 1
                    for i in chosen)
                for j in range(v_count) if not ((mask >> j) & 1)
            )
            if not extendible:
                maximal[k] += 1
    return +full, +maximal, tested


def main():
    total = 0
    for n in range(2, 10):
        exhaustive = n <= 6
        full, maximal, tested = direct(n, exhaustive)
        total += tested
        assert full == expected_all(n), (n, full, expected_all(n))
        assert maximal == expected_maximal(n), (n, maximal, expected_maximal(n))
        assert set(maximal) == set(range(ceil(n / 2), floor(2 * n / 3) + 1))
        print(f"n={n} candidate_subsets={tested} exhaustive={exhaustive} "
              f"maximal_coefficients={dict(sorted(maximal.items()))}")
    for n in range(2, 201):
        values = [v for _, v in sorted(expected_maximal(n).items())]
        assert all(values[j] ** 2 > values[j-1] * values[j+1]
                   for j in range(1, len(values)-1)), n
    print(f"VERIFY_OK graph_orders=8 candidate_subsets={total} "
          "all_and_maximal_polynomials=PASS "
          "exhaustive_graph_orders=2..6 "
          "higher_orders_truncated_by_proved_size_bound=7..9 "
          "arithmetic_logconcavity_orders=2..200")


if __name__ == '__main__':
    main()
