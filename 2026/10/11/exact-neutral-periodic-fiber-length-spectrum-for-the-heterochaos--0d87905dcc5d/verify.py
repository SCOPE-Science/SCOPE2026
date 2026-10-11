"""Exact finite tests for the neutral-fiber length spectrum in generalized baker maps.

Requires only Python 3 standard library. Finite tests support, but do not replace,
the all-period proof based on bracket cancellation and the reflection principle.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb


def center_fixed_interval(M, word):
    """Return length in [0,1] of center initial values with valid identity return."""
    scale, offset = F(1), F(0)
    low, high = F(0), F(1)
    for typ, digit in word:
        if typ == "b":
            low = max(low, (F(digit - 1, M) - offset) / scale)
            high = min(high, (F(digit, M) - offset) / scale)
            scale, offset = scale * M, M * offset - (digit - 1)
        else:
            scale, offset = scale / M, (offset + digit - 1) / M
        low = max(low, -offset / scale)
        high = min(high, (1 - offset) / scale)
        if high <= low:
            return F(0)
    return high - low if scale == 1 and offset == 0 else F(0)


def outside_coordinate_fixed_points(M, word):
    """Check exact unique unstable and stable fixed points and their strict itineraries."""
    a, b = F(1, M + 2), F(1, M + 3)
    au, bu = F(1), F(0)
    ass, bs = F(1), F(0)
    for typ, digit in word:
        if typ == "a":
            au, bu = au / a, (bu - (digit - 1) * a) / a
            ass, bs = (1 - M * b) * ass, (1 - M * b) * bs
        else:
            au, bu = au / (1 - M * a), (bu - M * a) / (1 - M * a)
            ass, bs = b * ass, b * bs + 1 + b * (digit - M - 1)
    u = -bu / (au - 1)
    s = bs / (1 - ass)
    if not (0 < s < 1):
        return False
    for typ, digit in word:
        if typ == "a":
            if not ((digit - 1) * a < u < digit * a):
                return False
            u = (u - (digit - 1) * a) / a
        else:
            if not (M * a < u < 1):
                return False
            u = (u - M * a) / (1 - M * a)
    return True


def verify():
    for M in (2, 3):
        for m in (1, 2, 3):
            counts = Counter()
            alphabet = [(typ, digit) for typ in "ab" for digit in range(1, M + 1)]
            for word in product(alphabet, repeat=2 * m):
                length = center_fixed_interval(M, word)
                if length:
                    assert outside_coordinate_fixed_points(M, word), (M, m, word)
                    counts[length] += 1
            predicted = Counter({F(1, M**j): M**m *
                                 (comb(2*m, m+j) - (comb(2*m, m+j+1) if j < m else 0))
                                 for j in range(m + 1)})
            assert counts == predicted, (M, m, counts, predicted)
            assert sum(counts.values()) == M**m * comb(2*m, m)
    print("CHECK_OK")


if __name__ == "__main__":
    verify()
