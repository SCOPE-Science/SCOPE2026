"""Finite diagnostics for the digit-complement progression theorem.

Run: python3 verify.py. Only the written proof extends to unbounded integers.
"""
from itertools import product


def base_digits(n, base):
    assert n >= 0 and base >= 2
    if n == 0:
        return (0,)
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    return tuple(reversed(digits))


def occurrence_count(pattern, digits):
    length = len(pattern)
    # Enough leading zeros to capture every boundary-spanning occurrence.
    padded = (0,) * (length - 1) + tuple(digits)
    return sum(padded[i:i+length] == pattern
               for i in range(len(padded) - length + 1))


def boundary(pattern, base):
    r = len(pattern)
    for t in range(1, r):
        if pattern == (0,) * t + (base - 1,) * (r - t):
            return 1
    return 0


def verify_count_identity():
    tests = 0
    for base in range(2, 6):
        for r in range(1, 5):
            for pattern in product(range(base), repeat=r):
                if pattern == (0,) * r or pattern == (base - 1,) * r:
                    continue
                flipped = tuple(base - 1 - x for x in pattern)
                width = r + 9
                limit = base ** width - 1
                shift = boundary(flipped, base)
                for n in range(128):
                    reflected_n = limit - n
                    delta = (occurrence_count(flipped, base_digits(reflected_n, base))
                             - occurrence_count(pattern, base_digits(n, base)))
                    assert delta == shift, (base, pattern, n, delta, shift)
                    tests += 1
    return tests


def verify_progression_transfer():
    tests = 0
    for base in (2, 3, 4):
        for r in (1, 2, 3):
            for pattern in product(range(base), repeat=r):
                if pattern == (0,) * r or pattern == (base - 1,) * r:
                    continue
                flipped = tuple(base - 1 - x for x in pattern)
                for m in (2, 3, 5):
                    for n, d, count in product(range(16), range(1, 6), range(1, 6)):
                        width = r + 8
                        assert n + (count - 1) * d < base ** (width - r)
                        origin = base ** width - 1 - n - (count - 1) * d
                        left = [occurrence_count(pattern, base_digits(n+j*d, base)) % m
                                for j in range(count)]
                        right = [occurrence_count(flipped, base_digits(origin+j*d, base)) % m
                                 for j in range(count)]
                        assert right == [(x+boundary(flipped, base)) % m
                                         for x in reversed(left)], (base, pattern, n, d, count, m)
                        tests += 1
    return tests


if __name__ == '__main__':
    identities = verify_count_identity()
    progressions = verify_progression_transfer()
    print('VERIFY_OK count_identities=%d finite_progression_transfers=%d'
          % (identities, progressions))
