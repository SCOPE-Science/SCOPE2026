"""Exact finite certification for six consecutive Legendre-sign words.

This program checks the complete finite range needed by the analytic
character-sum inequality. Only Python's standard library is used.
"""
from math import isqrt

LIMIT = 16384
LENGTH = 6
FULL = (1 << (1 << LENGTH)) - 1


def is_prime(n):
    if n < 2:
        return False
    return all(n % divisor for divisor in range(2, isqrt(n) + 1))


def masks_at_prime(p):
    """Return the 64-bit support mask for the nonwrapping length-six words."""
    square = bytearray(p)
    for y in range(1, p):
        square[(y*y) % p] = 1
    support = 0
    for x in range(1, p - LENGTH + 1):
        word = 0
        for j in range(LENGTH):
            word = (word << 1) | square[x+j]
        support |= 1 << word
    return support


def alternate_masks(p):
    """Independent Euler-criterion implementation for small primes."""
    support = 0
    for x in range(1, p - LENGTH + 1):
        word = 0
        for j in range(LENGTH):
            chi = pow(x+j, (p-1)//2, p)
            assert chi in (1, p-1)
            word = (word << 1) | (chi == 1)
        support |= 1 << word
    return support


def main():
    exceptional = []
    checked = 0
    successful_tail = 0
    for p in range(3, LIMIT, 2):
        if not is_prime(p):
            continue
        checked += 1
        support = masks_at_prime(p)
        if p <= 1009:
            assert support == alternate_masks(p), p
        if support != FULL:
            exceptional.append(p)
        if p >= 461:
            assert support == FULL, (p, (FULL ^ support).bit_count())
            successful_tail += 1
        if p == 457:
            assert support.bit_count() == 63
            assert (support & (1 << 63)) == 0
            assert (FULL ^ support) == (1 << 63)
        if p == 461:
            assert support == FULL
    assert exceptional[-1] == 457
    assert len(exceptional) == 61
    assert not any(461 <= p < LIMIT for p in exceptional)
    print('VERIFY_OK', 'odd_primes_checked', checked,
          'complete_primes_at_least_461', successful_tail,
          'exceptions', len(exceptional),
          'last_exception', exceptional[-1],
          'missing_pattern_at_457', 'RRRRRR')
    print('exceptional_primes:', ','.join(map(str, exceptional)))


if __name__ == '__main__':
    main()
