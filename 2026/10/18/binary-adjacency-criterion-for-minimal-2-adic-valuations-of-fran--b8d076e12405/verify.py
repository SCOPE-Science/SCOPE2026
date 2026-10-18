#!/usr/bin/env python3
"""Independent exact-integer finite tests for the binary Franel valuation theorem."""
from math import comb


def s2(n):
    return n.bit_count()


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def franel(n):
    return sum(comb(n, k) ** 3 for k in range(n + 1))


def strehl_term(n, k):
    return comb(n, k) ** 2 * (comb(2 * k, n) if 2 * k >= n else 0)


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


terms = []
individual_terms = 0
for n in range(257):
    f = franel(n)
    terms.append(f)
    w = s2(n)
    assert f > 0 and v2(f) >= w, (n, f, w)
    overlap = n & (n >> 1)
    expected_minima = 2 ** s2(overlap)
    min_count = 0
    acc = 0
    for k in range((n + 1) // 2, n + 1):
        a = n - k
        b = 2 * k - n
        U = s2(a) + s2(k) - s2(n)
        W = s2(a) + s2(b) - s2(n)
        assert U >= 0 and W >= 0
        t = strehl_term(n, k)
        assert t > 0
        assert v2(t) == w + U + W
        min_count += v2(t) == w
        acc += t
        individual_terms += 1
    assert acc == f, (n, acc, f)
    assert min_count == expected_minima, (n, min_count, expected_minima)
    assert (v2(f) == w) == (overlap == 0), (n, v2(f), w, overlap)
for n in range(1, 256):
    assert (n + 1) ** 2 * terms[n + 1] == (7 * n * n + 7 * n + 2) * terms[n] + 8 * n * n * terms[n - 1]
for L in range(0, 14):
    no_adjacent = sum(((n & (n >> 1)) == 0) for n in range(1 << L))
    assert no_adjacent == fibonacci(L + 2), (L, no_adjacent)
print(f"VERIFY_OK indices={len(terms)} positive_strehl_terms={individual_terms} recurrence_instances=255 fibonacci_lengths=14")
