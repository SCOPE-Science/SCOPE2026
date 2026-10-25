#!/usr/bin/env python3
"""Finite checks for complement-reflection of binary block counts.

This is a reproducibility check, not a proof of the infinite identity.
Only the Python standard library is required.
"""
from itertools import product


def complement(block):
    return ''.join('1' if char == '0' else '0' for char in block)


def occurrences(block, integer):
    """Overlapping pattern count with leading-zero convention."""
    binary = format(integer, 'b')
    if block[0] == '0':
        leading_zeros = len(block) - len(block.lstrip('0'))
        binary = '0' * leading_zeros + binary
    m = len(block)
    return sum(binary[i:i + m] == block
               for i in range(len(binary) - m + 1))


def boundary_shift(block):
    other = complement(block)
    r = len(other) - len(other.lstrip('0'))
    return int(0 < r < len(other) and other == '0' * r + '1' * (len(other) - r))


def test_point(block, integer, width):
    assert width >= len(block) + max(1, integer.bit_length())
    reflected = (1 << width) - 1 - integer
    lhs = occurrences(complement(block), reflected)
    rhs = occurrences(block, integer) + boundary_shift(block)
    assert lhs == rhs, (block, integer, width, lhs, rhs)


def main():
    blocks = [''.join(bits) for m in range(2, 8)
              for bits in product('01', repeat=m)
              if len(set(bits)) == 2]
    count_points = 0
    count_runs = 0
    for block in blocks:
        for integer in range(256):
            width = len(block) + max(1, integer.bit_length()) + (integer % 3)
            test_point(block, integer, width)
            count_points += 1
        for index in range(20):
            start = 7 * index + len(block)
            difference = index + 1
            length = 2 + index % 7
            maximum = start + (length - 1) * difference
            width = len(block) + max(1, maximum.bit_length())
            observed = [occurrences(block, start + j * difference)
                        for j in range(length)]
            reflected_start = (1 << width) - 1 - maximum
            reflected = [occurrences(complement(block),
                                     reflected_start + j * difference)
                         for j in range(length)]
            expected = [value + boundary_shift(block)
                        for value in reversed(observed)]
            assert reflected == expected, (block, start, difference, length)
            for modulus in (2, 3, 5, 7):
                assert [v % modulus for v in reflected] == [v % modulus for v in expected]
            count_runs += 1
    print('VERIFIED:', len(blocks), 'mixed blocks of lengths 2..7,',
          count_points, 'exact point identities,', count_runs,
          'full arithmetic-progression reversals.')


if __name__ == '__main__':
    main()
