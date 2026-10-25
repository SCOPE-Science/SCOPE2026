#!/usr/bin/env python3
"""Independent finite rational-cycle tests for the Sturmian k-tortoise formula.

For coprime a,q and n<q, the periodic mechanical word has n+1
factors. The test checks k=1..8 against both a direct word-transform
implementation and an independent zero-position transform.
"""
from math import gcd


def tortoise_once(w):
    i = w.find('1')
    return w if i < 0 else w[:i] + w[i + 1:] + '1'


def tortoise_iterated(w, k):
    for _ in range(k):
        w = tortoise_once(w)
    return w


def tortoise_via_zero_positions(w, k):
    n = len(w)
    target = ['1'] * n
    zeros = [j + 1 for j, c in enumerate(w) if c == '0']
    for i, old_pos in enumerate(zeros, 1):
        new_pos = max(i, old_pos - k)
        if target[new_pos - 1] != '1':
            raise AssertionError(('zero collision', w, k))
        target[new_pos - 1] = '0'
    return ''.join(target)


def mechanical_factors(a, q, n):
    cycle = ''.join(str(((r + 1) * a) // q - (r * a) // q) for r in range(q))
    wrapped = cycle + cycle[:n - 1]
    return {wrapped[r:r + n] for r in range(q)}


def interval_factors(a, q, n):
    # Discontinuities of coordinates 0..n-1 for the rotation code.
    boundaries = sorted({(-j * a) % q for j in range(n + 1)})
    assert len(boundaries) == n + 1
    result = set()
    for r in boundaries:  # right-sided intervals, floor convention
        word = ''.join(str((r + (j + 1) * a)//q - (r + j * a)//q)
                       for j in range(n))
        result.add(word)
    return result


def run():
    instances = 0
    for q in (11, 19, 37, 53, 101, 211):
        for a in range(1, q):
            if gcd(a, q) != 1:
                continue
            m = (q - 1) // a
            for n in range(1, min(q, 36)):
                f = mechanical_factors(a, q, n)
                assert len(f) == n + 1, (q, a, n, len(f))
                if q <= 53 or n in (1, 2, 5, 17, 35):
                    assert interval_factors(a, q, n) == f
                for k in range(1, 9):
                    outputs = {tortoise_iterated(w, k) for w in f}
                    other = {tortoise_via_zero_positions(w, k) for w in f}
                    assert outputs == other, (q, a, n, k)
                    threshold = (k * q - 1) // a
                    expected = n + 1 - min(n - 1, threshold)
                    assert len(outputs) == expected, (q, a, n, k, len(outputs), expected)
                    instances += 1
    print('VERIFY_OK rational_cycles=%d q_values=6 k_range=1..8 n<36' % instances)
    # Demonstration for a rational approximation to the Fibonacci slope.
    a, q = 377, 987
    for n in (1, 2, 3, 4, 5, 10, 20, 35, 50, 100):
        f = mechanical_factors(a, q, n)
        assert len(f) == n + 1
        for k in range(1, 6):
            computed = len({tortoise_iterated(w, k) for w in f})
            expected = n + 1 - min(n - 1, (k * q - 1) // a)
            assert computed == expected, (n, k, computed, expected)
    print('FIBONACCI_APPROX_OK')


if __name__ == '__main__':
    run()
