#!/usr/bin/env python3
"""Finite exact checks for a family of symmetric central holes of the negative-doubling map.
The infinite theorems require the accompanying mathematical proof."""
from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import product


def map_step(x):
    if x < Fraction(1, 2):
        return 1 - 2*x
    if x > Fraction(1, 2):
        return 2 - 2*x
    raise ValueError('critical point: one-sided coding required')


def word(m):
    a = ('00' + '10'*m)[:m]
    b = ''.join('1' if c == '0' else '0' for c in a)
    return a, b


def code_of_dyadic_cell(k, m):
    x = Fraction(2*k + 1, 2**(m+1))
    bits = []
    for _ in range(m):
        bits.append('0' if x < Fraction(1, 2) else '1')
        x = map_step(x)
    return ''.join(bits)


def admissible_count(length, m):
    w, v = word(m)
    return sum(not (w in ''.join(bits) or v in ''.join(bits))
               for bits in product('01', repeat=length))


def recurrence_count(length, m):
    if length == 0:
        return 1
    a = [1]
    for k in range(1, length + 1):
        a.append(2 + sum(a[k-j] for j in range(1,m-1) if k-j >= 1))
    return a[-1]


def small_t(m):
    getcontext().prec = 75
    q = Decimal(2) ** (1-m)
    r = m-2
    left, right = q, 2*q
    assert right < 1 and right * (1-right)**r > q
    for _ in range(280):
        mid=(left+right)/2
        if mid*(1-mid)**r > q:
            right=mid
        else:
            left=mid
    return (left+right)/2


def main():
    total = 0
    for m in range(2, 10):
        w,v = word(m)
        cells = []
        codes = set()
        for k in range(2**m):
            s = code_of_dyadic_cell(k, m)
            assert s not in codes, (m,k,s)
            codes.add(s)
            if s in (w,v): cells.append(k)
            total += 1
        assert cells == [2**(m-1)-1, 2**(m-1)]
        for length in range(0,14):
            e=admissible_count(length,m)
            r=recurrence_count(length,m)
            assert e == r, (m,length,e,r)
            total += 1
    for m in range(8,26):
        q=Decimal(2)**(1-m)
        t=small_t(m)
        gamma=-(1-t).ln()
        approx=q + (Decimal(m)-Decimal('1.5'))*q*q
        assert abs(gamma-approx) < 20*Decimal(m*m)*q**3
        total += 1
    print('PASS: %d finite and high-precision diagnostics; the proof supplies the infinite statement.'%total)


if __name__ == '__main__':
    main()
