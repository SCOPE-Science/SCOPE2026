#!/usr/bin/env python3
"""Exact independent finite checks for the radix-residue opacity formula.

Runs without external packages. The infinite theorem is established in RESULT.md;
this script tests finite automata, witnesses, and level counts.
"""
from itertools import product


def formula_depth(base, modulus):
    assert base >= 2 and modulus >= 1
    if modulus % base == 0:
        return None
    length = 2
    while base**length - base < modulus:
        length += 1
    return length


def has_inhomogeneous_path(base, modulus, digits):
    state = 0
    seen = {}
    for digit in digits:
        state = (base * state + digit) % modulus
        old_digit = seen.get(state)
        if old_digit is not None and old_digit != digit:
            return True
        seen[state] = digit
    return False


def brute_shortest(base, modulus, cap):
    for length in range(1, cap + 1):
        for digits in product(range(base), repeat=length):
            if has_inhomogeneous_path(base, modulus, digits):
                return length
    return None


def padded_digits(value, base, length):
    out = [0] * length
    for position in range(length - 1, -1, -1):
        out[position] = value % base
        value //= base
    assert value == 0
    return tuple(out)


def construction(base, modulus):
    length = formula_depth(base, modulus)
    assert length is not None
    scale = base**(length - 1) - 1
    first = min(base - 1, modulus // scale)
    tail = modulus - first * scale
    assert 0 <= tail <= scale
    word = (first,) + padded_digits(tail, base, length - 1)
    assert has_inhomogeneous_path(base, modulus, word)
    assert (first - (first * base**(length-1) + tail)) % modulus == 0
    assert word[-1] != word[0]
    assert not (base**(length-1) - base >= modulus) if length > 2 else True
    return word


def main():
    checked = 0
    for base in range(2, 7):
        for modulus in range(1, 81):
            depth = formula_depth(base, modulus)
            finite_cap = 6
            observed = brute_shortest(base, modulus, finite_cap)
            if depth is not None and depth <= finite_cap:
                assert observed == depth, (base, modulus, observed, depth)
            else:
                assert observed is None, (base, modulus, observed, depth)
            if depth is not None:
                construction(base, modulus)
            checked += 1
    for base in range(2, 9):
        for length in range(2, 5):
            upper = base**length - base
            lower = 0 if length == 2 else base**(length-1) - base
            count = sum(
                1 for modulus in range(lower + 1, upper + 1)
                if formula_depth(base, modulus) == length
            )
            assert count == (base - 1)**2 * base**(length - 2), (base, length, count)
    # Larger witnesses test constructive rather than brute conditions.
    for base in (2, 3, 4, 5, 7, 10):
        for modulus in range(1, 1001):
            if modulus % base:
                construction(base, modulus)
    print('VERIFY_OK brute_base_range=2..6 brute_moduli=1..80 finite_cap=6 ' +
          f'checked_pairs={checked} exact_level_spectra_bases=2..8_depths=2..4 ' +
          'constructive_witnesses_bases=2,3,4,5,7,10_moduli=1..1000')


if __name__ == '__main__':
    main()
