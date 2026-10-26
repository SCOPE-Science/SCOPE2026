"""Finite exact tests for partial-injection path/cycle component identities.

Run: python verify_partial_injection.py (Python 3 standard library).
The program tests finite combinatorial identities, not infinite asymptotics.
"""
from itertools import combinations, permutations
from math import factorial
from fractions import Fraction


def injections(n):
    values = tuple(range(n))
    for k in range(n + 1):
        for dom in combinations(values, k):
            for img in permutations(values, k):
                f = [-1] * n
                for a, b in zip(dom, img):
                    f[a] = b
                yield tuple(f)


def components(f):
    n = len(f)
    ins = [0] * n
    for b in f:
        if b >= 0:
            ins[b] += 1
    seen = set()
    paths = {}
    cycles = {}
    for x in range(n):
        if ins[x] == 0:
            v, length = x, 0
            while v != -1:
                assert v not in seen
                seen.add(v)
                length += 1
                v = f[v]
            paths[length] = paths.get(length, 0) + 1
    for x in range(n):
        if x not in seen:
            v, length = x, 0
            while v not in seen:
                seen.add(v)
                length += 1
                v = f[v]
            assert v == x
            cycles[length] = cycles.get(length, 0) + 1
    assert len(seen) == n
    assert sum(k * v for k, v in paths.items()) + sum(k * v for k, v in cycles.items()) == n
    return paths, cycles


def falling(x, k):
    v = 1
    for j in range(k):
        v *= x - j
    return v


def coefficients(N):
    P = [1, 2]
    for n in range(2, N + 1):
        P.append(2 * n * P[n - 1] - (n - 1) ** 2 * P[n - 2])
    return [Fraction(P[n], factorial(n)) for n in range(N + 1)], P


def main():
    N = 6
    a, P = coefficients(500)
    patterns = [((1, 1),), ((2, 1),), ((3, 1),), ((1, 2),), ((-1, 1),), ((-2, 1),), ((-3, 1),), ((1, 1), (-1, 1)), ((2, 1), (-1, 1)), ((1, 1), (-2, 1)), ((-1, 2),), ((1, 2), (-1, 1))]
    inspected = 0
    for n in range(N + 1):
        count = 0
        totals = [0] * len(patterns)
        for f in injections(n):
            p, c = components(f)
            count += 1
            for i, pattern in enumerate(patterns):
                factor = 1
                for length, power in pattern:
                    factor *= falling((p if length > 0 else c).get(abs(length), 0), power)
                totals[i] += factor
        assert count == P[n], (n, count, P[n])
        inspected += count
        for pattern, total in zip(patterns, totals):
            size = sum(abs(length) * power for length, power in pattern)
            expected = Fraction(0)
            if size <= n:
                expected = factorial(n) * a[n - size]
                for length, power in pattern:
                    if length < 0:
                        expected *= Fraction(1, abs(length)) ** power
            assert total == expected, (n, pattern, total, expected)
    # Exact coefficient ratios are the only numerical asymptotic diagnostic.
    ratios = [float(a[n-2] / a[n]) for n in (20, 100, 500)]
    assert ratios[0] < ratios[1] < ratios[2] < 1
    print("PARTIAL_INJECTION_EXACT_OK", inspected, len(patterns), ratios)

if __name__ == '__main__':
    main()
