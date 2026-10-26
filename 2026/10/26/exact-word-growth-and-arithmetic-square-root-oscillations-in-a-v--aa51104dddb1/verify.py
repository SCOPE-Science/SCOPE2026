"""Standalone exact checks for valuation-parity spacing-shift complexity.

Run with Python 3.9 or later: python verify.py.
The exhaustive checks cover finite words only; the infinite statements
follow from the separate structural proof.
"""
from functools import lru_cache
from math import sqrt, log

@lru_cache(None)
def odd_count(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return even_count((n + 1) // 2) + even_count(n // 2) - 1

@lru_cache(None)
def even_count(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return odd_count((n + 1) // 2) * odd_count(n // 2)


def brute_counts(n):
    """Independent exhaustive mask test, without calling either recurrence."""
    invalid_if_selected = [[0] * n for _ in range(2)]
    for i in range(n):
        for j in range(i):
            d = i - j
            v = (d & -d).bit_length() - 1
            # 0: odd valuation allowed; 1: even valuation allowed
            invalid_if_selected[0][i] |= ((v & 1) == 0) << j
            invalid_if_selected[1][i] |= ((v & 1) == 1) << j
    total = [0, 0]
    maxima = [0, 0]
    for kind in range(2):
        valid = bytearray(1 << n)
        valid[0] = 1
        total[kind] = 1
        for mask in range(1, 1 << n):
            i = mask.bit_length() - 1
            rest = mask ^ (1 << i)
            ok = valid[rest] and not (rest & invalid_if_selected[kind][i])
            valid[mask] = 1 if ok else 0
            if ok:
                total[kind] += 1
                maxima[kind] = max(maxima[kind], mask.bit_count())
    return total, maxima


def verify():
    assert odd_count(0) == even_count(0) == 1
    assert odd_count(1) == even_count(1) == 2
    for n in range(1, 19):
        (o, e), maxima = brute_counts(n)
        assert (o, e) == (odd_count(n), even_count(n)), (n, o, e)
        if n in (1, 4, 16):
            assert maxima[0] == round(sqrt(n)), (n, maxima[0])
    for n in range(1, 1001):
        assert odd_count(4 * n) == 2 * odd_count(n)**2 - 1
    a, b = 2, 3
    for m in range(9):
        assert odd_count(4**m) == a, m
        assert odd_count(2 * 4**m) == b, m
        a, b = 2 * a * a - 1, 2 * b * b - 1
    c0 = log(2 + sqrt(3))
    c1 = log(3 + 2 * sqrt(2)) / sqrt(2)
    assert 1.3169 < c0 < 1.3170
    assert 1.2464 < c1 < 1.2465
    assert c0 > c1
    print('VERIFY_OK: exhaustive independent binary-mask counts for n=1..18,')
    print('both valuation parities; exact full-length recursion for n=1..1000;')
    print('all 18 dyadic Chebyshev values m=0..8; sharp maximum supports')
    print('at lengths 1,4,16; distinct normalized square-root constants.')
    print('FIRST_ODD_COMPLEXITIES', [(n, odd_count(n)) for n in range(1, 17)])
    print('DYADIC_CONSTANTS', format(c0, '.15f'), format(c1, '.15f'))

if __name__ == '__main__':
    verify()
