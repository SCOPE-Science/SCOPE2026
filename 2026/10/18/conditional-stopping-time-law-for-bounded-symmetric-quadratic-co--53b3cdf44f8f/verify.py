#!/usr/bin/env python3
"""Finite exact-arithmetic checks of a quadratic-map stopping-time theorem.

The published exhaustive classification is a mathematical input; finite
enumeration here does not certify its truth for all integers.
"""
from math import sqrt


def step(n):
    assert n >= 0
    return n // 2 if n % 2 == 0 else (n * n - 1) // 4


def hit(n):
    t = 0
    while n:
        n = step(n)
        t += 1
        assert t < 10000, "iteration ceiling (not an impossibility proof)"
    return t


def candidates(X):
    """Return every positive classified terminating seed <= X with exact time."""
    result = {}
    for m in range(1, X.bit_length() + 1):
        for sign in (-1, +1):
            q = (1 << m) + sign
            if q > X:
                continue
            n, ell = q, 0
            while n <= X:
                t = ell + m * (m + 1) // 2 + (2 if sign == 1 else 0)
                if n in result:
                    assert result[n] == t, (n, t, result[n])
                result[n] = t
                n *= 2
                ell += 1
    for q, base_t in ((11, 12), (23, 20), (181, 80)):
        n, ell = q, 0
        while n <= X:
            assert n not in result
            result[n] = base_t + ell
            n *= 2
            ell += 1
    return result


def dyadic_count(L):
    return L * L + 2 * L - 12


def dyadic_total(L):
    n = L**4 + 8 * L**3 + 23 * L**2 + 1144 * L - 7548
    assert n % 12 == 0
    return n // 12


def stop_count_formula(L):
    pos = lambda v: max(v, 0)
    first = sum(pos(L - m * (m + 1) // 2 + 1)
                for m in range(1, L + 1))
    second = sum(pos(L - m * (m + 1) // 2 - 1)
                 for m in range(1, L + 1))
    return (first + second - pos(L - 2) + pos(L - 11)
            + pos(L - 19) + pos(L - 79))


assert [hit(q) for q in (1, 3, 11, 23, 181)] == [1, 3, 12, 20, 80]
terminal_tests = 0
for m in range(1, 24):
    for sign in (-1, +1):
        for ell in range(7):
            x = (1 << ell) * ((1 << m) + sign)
            expected = ell + m * (m + 1) // 2 + (2 if sign == 1 else 0)
            assert hit(x) == expected
            terminal_tests += 1

seed_tests = 0
for L in range(7, 36):
    population = candidates(1 << L)
    assert len(population) == dyadic_count(L), (L, len(population))
    assert sum(population.values()) == dyadic_total(L), L
    assert sum(t <= L for t in population.values()) == stop_count_formula(L), L
    for n, t in population.items():
        assert hit(n) == t, (L, n, t)
        seed_tests += 1

# The precise sharpness testpoint is genuinely finite and is not an
# extrapolation certificate of the asserted asymptotic constant.
for L in (100, 400, 1600):
    X = 1 << L
    total = 0
    for m in range(1, L + 2):
        for sign in (-1, +1):
            q = (1 << m) + sign
            if q <= X:
                total += (X // q).bit_length()
    total -= (X // 3).bit_length()  # double-counted odd part 3
    total += sum((X // q).bit_length() for q in (11, 23, 181))
    assert total == dyadic_count(L)
    finite_prob = stop_count_formula(L) / total
    limit_cdf = 2 * sqrt(2 / L) - 2 / L
    assert finite_prob < limit_cdf

print("VERIFY_OK terminal_tests=%d seed_tests=%d dyadic_L=7..35" %
      (terminal_tests, seed_tests))
