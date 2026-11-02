#!/usr/bin/env python3
"""Finite checks for the run-length/phase matrix construction.

The mathematical proof establishes the statement for all positive parameters;
these tests independently enumerate short matrix-product languages.
Uses only the Python standard library.
"""
from math import cos, pi, sin, isclose
from itertools import product


def identity(size):
    return tuple(tuple(float(i == j) for j in range(size)) for i in range(size))


def apply_zero(rows):
    size = len(rows)
    return (rows[0],) + rows[2:] + ((0.0,) * size,)


def apply_one(rows, c, s):
    r0, r1 = rows[0], rows[1]
    new0 = tuple(c * x - s * y for x, y in zip(r0, r1))
    new1 = tuple(s * x + c * y for x, y in zip(r0, r1))
    return (new0, new1) + rows[2:]


def max_abs(rows):
    return max(abs(x) for row in rows for x in row)


def verify_pair(a, n):
    theta = pi / (2 * n)
    c, s = cos(theta), sin(theta)
    nlen = a + n + 1
    target = '0' * a + '1' * n + '0'
    states = [(identity(a + 1), '')]
    min_nonzero = float('inf')
    zeros = []
    total_products = 0
    for length in range(1, nlen + 1):
        nxt = []
        for rows, prefix in states:
            for letter in '01':
                out = apply_zero(rows) if letter == '0' else apply_one(rows, c, s)
                word = prefix + letter
                norm = max_abs(out)
                total_products += 1
                if norm < 1e-10:
                    if length != nlen:
                        raise AssertionError(('early zero', a, n, word, norm))
                    zeros.append(word)
                else:
                    min_nonzero = min(min_nonzero, norm)
                    if length < nlen:
                        nxt.append((out, word))
        states = nxt
    assert zeros == [target], (a, n, zeros, target)
    assert min_nonzero > 1e-7, (a, n, min_nonzero)
    return total_products, min_nonzero


def run():
    aggregate = 0
    min_gap = float('inf')
    for a in range(1, 9):
        for n in range(1, 6):
            count, gap = verify_pair(a, n)
            aggregate += count
            min_gap = min(min_gap, gap)
    print('PASS: 40 parameter pairs, a=1..8, n=1..5')
    print('PASS: complete binary matrix-product enumeration through length a+n+1')
    print('PASS: exactly one shortest zero word at each pair: 0^a 1^n 0')
    print('Matrix products evaluated:', aggregate)
    print('Smallest observed nonzero max-entry (floating check):', format(min_gap, '.12g'))
    for a in range(1, 33):
        d = next(k for k in range(2, 33) if k*k - 1 >= a + 1)
        assert (d-1)*(d-1)-1 < a+1 <= d*d-1
    print('PASS: Hilbert-dimension rounding through a=32')
    print('Finite checks are not a proof of the all-parameter theorem.')

if __name__ == '__main__':
    run()
