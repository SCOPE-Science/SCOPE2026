#!/usr/bin/env python3
"""Independent finite arithmetic checks for exact dyadic valuations."""

def valuation(n):
    assert n != 0
    return (abs(n) & -abs(n)).bit_length() - 1


def rational_sum_scaled_mod(power, scale, modulus_bits, terms):
    """Return 2^scale times the convergent sum of 2^j/j^power modulo 2^modulus_bits."""
    mod = 1 << modulus_bits
    total = 0
    for j in range(1, terms + 1):
        t = valuation(j)
        exponent = j + scale - power*t
        assert exponent >= 0
        odd = j >> t
        total = (total + (1 << exponent) * pow(pow(odd, power, mod), -1, mod)) % mod
    return total


def main():
    a = 0
    factorial_previous = 1
    checked = []
    for n in range(1, 2049):
        if n > 1:
            factorial_previous *= n - 1
        assert (n*a) % 2 == 0
        a = n*a // 2 + factorial_previous
        if n >= 16 and n & (n-1) == 0:
            m = n.bit_length()-1
            assert valuation(a) == n + 2*m - 3, (m, valuation(a))
            checked.append(m)
    assert checked == list(range(4,12))
    print('PASS: exact integer recurrence and dyadic valuations m=4,...,11')

    bits = 64
    terms = 192
    assert rational_sum_scaled_mod(1, 0, bits, terms) == 0
    assert rational_sum_scaled_mod(2, 0, bits, terms) == 0
    assert rational_sum_scaled_mod(3, 2, bits, terms) % 2 == 1
    for power, scale in [(1,0),(2,0),(3,2)]:
        assert all(j+scale-power*valuation(j) >= bits for j in range(terms+1,terms+100))
    print('PASS: 2-adic logarithm and dilogarithm vanish mod 2^64; 4*Li_3(2) is odd')

    for m in range(4,12):
        N = 1 << m
        for j in range(1, N+128):
            v = j - 3*valuation(j) - valuation(N+j)
            assert v >= -4, (m,j,v)
    print('PASS: tail-term valuation bound on independent finite test ranges')

if __name__ == '__main__':
    main()
