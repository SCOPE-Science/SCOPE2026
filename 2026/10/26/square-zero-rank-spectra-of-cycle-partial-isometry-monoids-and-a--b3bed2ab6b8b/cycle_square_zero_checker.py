#!/usr/bin/env python3
"""Exact, independent small-case checks for zero-square partial isometries of cycles.

Standard-library only. Run: python3 cycle_square_zero_checker.py
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, gcd


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return c


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def power(a, e):
    ans = [1]
    while e:
        if e & 1:
            ans = mul(ans, a)
        a = mul(a, a)
        e //= 2
    return ans


def scale(a, k):
    return [k * v for v in a]


def totient(d):
    return sum(1 for k in range(1, d + 1) if gcd(k, d) == 1)


def cycle_independent_poly(d):
    # The fixed points of a permutation do not permit occupied support.
    if d == 1:
        return [1]
    if d == 2:
        return [1, 2]
    return [(d * comb(d - k, k)) // (d - k) for k in range(d // 2 + 1)]


def predicted_rank_poly(n):
    assert n >= 3
    p = [0]
    for d in range(1, n + 1):
        if n % d == 0:
            p = add(p, scale(power(cycle_independent_poly(d), n // d), totient(d)))
    if n % 2:
        p = add(p, scale(power([1, 2], (n - 1) // 2), n))
    else:
        p = add(p, scale(add(power([1, 2], n // 2),
                             power([1, 2], (n - 2) // 2)), n // 2))
    # Identify repeated restrictions of different global symmetries.
    p[0] -= 2 * n - 1
    p[1] -= n * (n - 1)
    if n % 2 == 0:
        p[2] -= n * (n - 2) // 2
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def direct_metric_enumeration(n):
    """No global symmetry assumptions: enumerate every map A -> B with A∩B=∅.

    Check the full graph-geodesic distance condition directly on every map.
    """
    out = Counter()
    trials = 0
    vertices = tuple(range(n))
    for k in range(n // 2 + 1):
        for A in combinations(vertices, k):
            complement = tuple(v for v in vertices if v not in A)
            for B in combinations(complement, k):
                for images in permutations(B):
                    trials += 1
                    if all(min(abs(A[i] - A[j]), n - abs(A[i] - A[j])) ==
                           min(abs(images[i] - images[j]), n - abs(images[i] - images[j]))
                           for i in range(k) for j in range(i + 1, k)):
                        out[k] += 1
    ans = [out.get(k, 0) for k in range(n // 2 + 1)]
    return ans, trials


def population_stats(p):
    total = sum(p)
    mean = sum(k * c for k, c in enumerate(p)) / total
    variance = sum((k - mean) ** 2 * c for k, c in enumerate(p)) / total
    return total, mean, variance


def main():
    examined = 0
    for n in range(3, 13):
        predicted = predicted_rank_poly(n)
        direct, trials = direct_metric_enumeration(n)
        assert predicted == direct, (n, predicted, direct)
        examined += trials
        print(f'n={n:2d} square_zero={sum(predicted):10d} coefficients={predicted} tested={trials}')
    # Numerical checks of consequences, not substitutes for asymptotic proofs.
    for n in (81, 82, 121, 122):
        p = predicted_rank_poly(n)
        total, mean, variance = population_stats(p)
        leading = n * 3 ** ((n - 1) // 2) if n % 2 else (2 * n / 3) * 3 ** (n // 2)
        ratio = total / leading
        print(f'n={n}: leading_ratio={ratio:.8f}, mean/n={mean/n:.8f}, var/n={variance/n:.8f}')
        assert abs(ratio - 1) < 0.04
        assert abs(mean / n - 1 / 3) < 0.008
        assert abs(variance / n - 1 / 9) < 0.008
    print('ALL_CYCLE_SQUARE_ZERO_CHECKS_PASSED', examined)


if __name__ == '__main__':
    main()
