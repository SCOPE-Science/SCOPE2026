#!/usr/bin/env python3
"""Exact independent finite tests for a mixed-prime binomial criterion."""
from math import comb


def digit_sum(number, base):
    total = 0
    while number:
        number, digit = divmod(number, base)
        total += digit
    return total


def predicted(q, t, p, e):
    c = comb(q ** (t + 1), q ** t)
    r = (e - 1) // 3
    b = comb(q ** (t + 1) * p ** r, q ** t * p ** r)
    return (c % p == pow(q, q ** t, p)
            and pow(b, p - 1, p ** e) == 1
            and digit_sum((q - 1) * p ** e, q) >= (q - 1) * t)


def direct(q, t, p, e):
    n = q ** t * p ** e
    return comb(q * n, n) % n == pow(q, n, n)


def test():
    count = 0
    for q in [2, 3, 5, 7, 11, 13, 17, 19, 23, 31]:
        for t in [1, 2]:
            for p in [5, 7, 11, 13]:
                if p == q:
                    continue
                for e in [1, 2, 3, 4]:
                    if q ** (t + 1) * p ** e > 16000:
                        continue
                    assert predicted(q, t, p, e) == direct(q, t, p, e), (q, t, p, e)
                    count += 1
    assert count == 106, count
    for q, p, e, residue, n in [
        (23, 7, 2, 851, 1127),
        (31, 5, 2, 651, 775),
        (31, 5, 3, 3751, 3875),
    ]:
        assert predicted(q, 1, p, e) and direct(q, 1, p, e)
        assert comb(q * n, n) % n == pow(q, n, n) == residue
    assert comb(45, 15) % 625 == 584
    assert comb(9, 3) % 625 == 84
    print('CERTIFICATE_OK exact_parameter_comparisons=106 mixed_prime_power_examples=3 fourth_layer_difference=true')


if __name__ == '__main__':
    test()
