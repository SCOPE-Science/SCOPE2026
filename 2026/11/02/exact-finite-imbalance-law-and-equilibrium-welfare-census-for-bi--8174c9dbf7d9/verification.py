#!/usr/bin/env python3
"""Independent finite checks of exact two-color cycle swap equilibrium formulas."""
from collections import Counter
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def colored_run_polynomial(size, k):
    if size == k:
        return {k: 1}
    return {k + t: choose(k, t) * choose(size - k - 1, t - 1)
            for t in range(1, min(k, size - k) + 1)}


def predicted_welfare_census(n, b):
    r = n - b
    counts = Counter()
    for k in range(1, b + 1):
        for integrated_red, multiplicity in colored_run_polynomial(r, k).items() if r >= k else ():
            numerator = n * choose(k, b - k) * multiplicity
            assert numerator % k == 0
            counts[b + integrated_red] += numerator // k
        for integrated_blue, multiplicity in colored_run_polynomial(b, k).items():
            numerator = n * choose(k, r - k) * multiplicity
            assert numerator % k == 0
            counts[r + integrated_blue] += numerator // k
        numerator = n * choose(k, b - k) * choose(k, r - k)
        assert numerator % k == 0
        counts[n] -= numerator // k
    return {w: count for w, count in counts.items() if count}


def integrated(v, i):
    n = len(v)
    return (v[(i - 1) % n] != v[i]) or (v[(i + 1) % n] != v[i])


def segregated_types(v):
    n = len(v)
    return {v[i] for i in range(n) if not integrated(v, i)}


def stable_directly(v):
    n = len(v)
    for i in range(n):
        for j in range(i + 1, n):
            if v[i] == v[j]:
                continue
            before_i = integrated(v, i)
            before_j = integrated(v, j)
            after = list(v)
            after[i], after[j] = after[j], after[i]
            if integrated(after, j) > before_i and integrated(after, i) > before_j:
                return False
    return True


def run_all_tests():
    checked = 0
    direct = 0
    for n in range(3, 17):
        for b in range(1, n // 2 + 1):
            brute = Counter()
            for positions in combinations(range(n), b):
                blue = set(positions)
                v = tuple(int(i in blue) for i in range(n))
                run_stable = len(segregated_types(v)) < 2
                if n <= 15:
                    assert stable_directly(v) == run_stable, (n, b, v)
                    direct += 1
                if run_stable:
                    welfare = sum(int(integrated(v, i)) for i in range(n))
                    brute[welfare] += 1
                checked += 1
            pred = predicted_welfare_census(n, b)
            assert dict(brute) == pred, (n, b, brute, pred)
            assert min(brute) == b + (b + 1) // 2 + 1, (n, b, brute)
            assert max(brute) == min(n, 3 * b), (n, b, brute)
            assert sum(brute.values()) == sum(pred.values())
        print(f"PASS n={n}: every minority size, welfare count, extrema")
    assert predicted_welfare_census(8, 4) == {7: 16, 8: 30}
    assert predicted_welfare_census(10, 5) == {9: 60, 10: 72}
    print(f"PASS: {checked} colorings checked; {direct} direct swap tests")


if __name__ == '__main__':
    run_all_tests()
