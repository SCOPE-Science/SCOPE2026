#!/usr/bin/env python3
"""Independent finite residue-image check for the quartic--sextic local theorem."""
from fractions import Fraction

# Each entry denotes 2^(12k+shift)*(offset + modulus*Z_2).
BALLS = ((0, 1, 8), (0, 2, 8), (4, 1, 16), (4, 5, 16),
         (6, 1, 8), (6, 5, 8), (8, 1, 16))

def theoretical_image(n):
    size = 1 << n
    image = {0}
    for k in range(n // 12 + 1):
        for shift, offset, unit_mod in BALLS:
            power = 12 * k + shift
            if power >= n:
                continue
            target = (1 << power) * offset
            period = min(size, (1 << power) * unit_mod)
            image.update(range(target % period, size, period))
    return image

def brute_image(n):
    size = 1 << n
    fourth = {pow(x, 4, size) for x in range(size)}
    sixth = {pow(y, 6, size) for y in range(size)}
    # Direct modular convolution; no use of the theoretical residue conditions.
    return {(x + y) % size for x in fourth for y in sixth}

def main():
    d = sum((Fraction(1, (1 << shift) * unit_mod) for shift, _, unit_mod in BALLS), Fraction()) / (1 - Fraction(1, 1 << 12))
    assert d == Fraction(1073, 4095), d
    counts = []
    for n in range(1, 17):
        actual, predicted = brute_image(n), theoretical_image(n)
        assert actual == predicted, (n, sorted(actual - predicted)[:8], sorted(predicted - actual)[:8])
        counts.append(len(actual))
    assert counts == [2, 3, 3, 5, 10, 18, 36, 68, 136, 270, 538, 1074, 2148, 4295, 8587, 17173]
    print('VERIFIED: all residues modulo 2^n for 1 <= n <= 16; Haar mass 1073/4095')
    print('cardinalities:', counts)
if __name__ == '__main__':
    main()
