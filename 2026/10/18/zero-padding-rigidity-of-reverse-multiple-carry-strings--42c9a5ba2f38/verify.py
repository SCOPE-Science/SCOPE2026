#!/usr/bin/env python3
"""Exact independent finite checks for the palintiple carry-boundary theorem.

The theorem is proved for all bases and lengths in RESULT.md. These tests
exercise its hypotheses and separately implement the grade-school carries.
Standard-library Python 3 only.
"""
from itertools import product


def base_digits(value, base, count):
    out = []
    for _ in range(count):
        out.append(value % base)
        value //= base
    assert value == 0
    return out


def find_palintiples(max_base=16, max_length=5):
    examined = 0
    valid = 0
    with_top_zero = 0
    for base in range(3, max_base + 1):
        for length in range(2, max_length + 1):
            for first in range(1, base):
                for last in range(1, base):
                    for middle in product(range(base), repeat=length - 2):
                        digits = (first,) + middle + (last,)  # low to high
                        examined += 1
                        v = sum(d * base**j for j, d in enumerate(digits))
                        reversed_v = sum(digits[length-1-j] * base**j for j in range(length))
                        multiplier, rem = divmod(v, reversed_v)
                        if rem or not (1 < multiplier < base):
                            continue
                        valid += 1
                        carried = [0]
                        carry = 0
                        for j in range(length):
                            t = multiplier * digits[length-1-j] + carry
                            assert t % base == digits[j]
                            carry = t // base
                            carried.append(carry)
                        assert carry == 0
                        assert 0 < carried[1] <= multiplier-1
                        assert all(0 <= c <= multiplier-1 for c in carried)
                        assert not (carried[-2] == 0 and carried[-3] == 0), (base, multiplier, digits, carried)
                        if carried[-2] == 0:
                            with_top_zero += 1
    return examined, valid, with_top_zero


def check_modular_obstruction(max_base=35):
    # Check independent finite solutions of both necessary modular congruences.
    checked = 0
    for b in range(3, max_base+1):
        for n in range(2, b):
            modulus = n*n-1
            for c1 in range(1, n):
                for c2 in range(n):
                    checked += 1
                    if b*c1 % modulus == 0 and (b*c2-c1) % modulus == 0:
                        raise AssertionError(('forbidden modular solution', b,n,c1,c2))
    return checked


if __name__ == '__main__':
    tested, found, top = find_palintiples()
    modtested = check_modular_obstruction()
    print(f'PASS exhaustive finite inputs={tested}, actual palintiples={found}, with one top zero={top};')
    print(f'PASS modular-boundary tuples={modtested}; infinite theorem uses algebraic proof.')
