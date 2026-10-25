#!/usr/bin/env python3
"""Exact checks of valuation spectra for ternary Fuss--Catalan numbers.

All computations use Python's standard library. No precomputed research data is read.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def factorial_v2(n):
    result = 0
    while n:
        n //= 2
        result += n
    return result


def valuation_from_factorials(n):
    # The divisor 2n+1 is odd.
    return factorial_v2(3*n) - factorial_v2(n) - factorial_v2(2*n)


def valuation_from_binary_sum(n):
    return 2*n.bit_count() - (3*n).bit_count()


def polynomial_add(*summands):
    answer = Counter()
    for p in summands:
        for d, c in p.items():
            answer[d] += c
    return +answer


def polynomial_multiply(p, q):
    out = Counter()
    for i, a in p.items():
        for j, b in q.items():
            out[i+j] += a*b
    return dict(out)


def polynomial_scaled(p, constant):
    return {d: constant*c for d, c in p.items() if constant*c}


def transfer_histogram(L):
    # State = (preceding binary digit, incoming carry).
    states = {(0, 0): Counter({0:1})}
    for _ in range(L):
        new_states = {}
        for (prev, carry), polynomial in states.items():
            for digit in (0, 1):
                next_carry = (digit + prev + carry)//2
                target = (digit, next_carry)
                target_poly = new_states.setdefault(target, Counter())
                for weight, count in polynomial.items():
                    target_poly[weight + next_carry] += count
        states = new_states
    histogram = Counter()
    for (prev, carry), polynomial in states.items():
        for weight, count in polynomial.items():
            histogram[weight + prev*carry] += count
    return +histogram


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def exact_direct_histogram(L):
    return +Counter(valuation_from_factorials(n) for n in range(1 << L))


def main():
    for n in range(120):
        value = comb(3*n, n)//(2*n+1)
        assert value*(2*n+1) == comb(3*n, n)
        brute = (value & -value).bit_length()-1
        assert brute == valuation_from_factorials(n) == valuation_from_binary_sum(n), n

    for L in range(13):
        row = transfer_histogram(L)
        independent = exact_direct_histogram(L)
        assert row == independent, (L, row, independent)
        assert sum(row.values()) == 2**L
        assert row.get(0, 0) == fibonacci(L+2)
        if L >= 2:
            assert max(row) == L
            assert row[L] == fibonacci(L-1)
        expected_mean = Fraction(L,2) - Fraction(2,3) + Fraction(3+(-1)**L, 6*(2**L))
        actual_mean = Fraction(sum(d*v for d,v in row.items()), 2**L)
        assert actual_mean == expected_mean, (L,actual_mean,expected_mean)

    # Verify the exact polynomial recurrence in degrees, without symbolic packages.
    rows = [transfer_histogram(L) for L in range(27)]
    c1 = {0:1,1:1}
    c2 = {0:1,1:-1,2:1}
    c3 = {1:-1,2:-1}
    for L in range(3,len(rows)):
        predicted = Counter()
        for coeff,prev in [(c1,rows[L-1]),(c2,rows[L-2]),(c3,rows[L-3])]:
            for degree,number in polynomial_multiply(coeff,prev).items():
                predicted[degree] += number
        assert dict(+predicted) == dict(rows[L]), (L,predicted,rows[L])
    print('VERIFY_OK: 120 exact Fuss--Catalan integers; 8191 factorial-valued indices; '
          '13 exhaustive dyadic histograms; 24 exact polynomial recurrences; '
          '13 sharp parity/extremum/moment checks')

if __name__ == '__main__':
    main()
