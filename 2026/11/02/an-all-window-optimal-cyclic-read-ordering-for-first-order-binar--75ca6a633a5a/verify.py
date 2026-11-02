"""Exhaustive checks for cyclic b-symbol distances of first-order binary Reed-Muller codes.

Independent direct computation over affine Boolean evaluations, with a primitive
field-power coordinate order. Pure Python 3, no external packages.
"""
from collections import Counter
from itertools import permutations

PRIMITIVE = {2:0x7, 3:0xb, 4:0x13, 5:0x25, 6:0x43, 7:0x83, 8:0x11d}


def times_generator(x, poly, m):
    x <<= 1
    if x & (1 << m):
        x ^= poly
    return x & ((1 << m) - 1)


def field_order(m):
    N = 1 << m
    result = [0]
    element = 1
    for _ in range(N - 1):
        result.append(element)
        element = times_generator(element, PRIMITIVE[m], m)
    assert element == 1
    assert len(set(result)) == N
    return result


def b_weight(bits, width):
    n = len(bits)
    # Independent direct window OR, not a use of the character argument.
    return sum(any(bits[(j+t) % n] for t in range(width)) for j in range(n))


def codewords(order, m):
    for a in range(1 << m):
        for c in range(2):
            yield a, c, [((a & x).bit_count() & 1) ^ c for x in order]


def full_spectra(order, m, widths):
    spectra = {b: Counter() for b in widths}
    for a, c, bits in codewords(order, m):
        for b in widths:
            spectra[b][b_weight(bits, b)] += 1
    return spectra


def direct_test(m):
    N = 1 << m
    order = field_order(m)
    widths = list(range(1, m+2))
    spectra = full_spectra(order, m, widths)
    result = []
    for b in widths:
        dist = min(w for w, count in spectra[b].items() if w > 0 and count > 0)
        expect = N - (1 << (m-b)) if b <= m else N
        assert dist == expect, (m, b, dist, expect, spectra[b])
        result.append(dist)
    # For b=2, verify also the nonzero pair-weight multiplicities.
    pair_spectrum = spectra[2]
    target = Counter()
    target[0] += 1
    target[3*N//4] += 3*N//2-2
    target[3*N//4+1] += N//2
    target[N] += 1
    assert pair_spectrum == target, (m, pair_spectrum, target)
    return m, PRIMITIVE[m], result, dict(sorted(pair_spectrum.items()))


def exhaust_dimension_three():
    m = 3
    N = 1 << m
    max_minima = [0] * (m + 2)
    order_count_simultaneous = 0
    for suffix in permutations(range(1, N)):
        words = list(codewords((0,) + suffix, m))
        distances = [min(b_weight(bits, b) for a, c, bits in words if a or c)
                     for b in range(1, m + 2)]
        for b, d in enumerate(distances, start=1):
            max_minima[b] = max(max_minima[b], d)
        if distances == [4, 6, 7, 8]:
            order_count_simultaneous += 1
    assert max_minima[1:] == [4, 6, 7, 8]
    assert order_count_simultaneous > 0
    return max_minima[1:], order_count_simultaneous


def main():
    for m in PRIMITIVE:
        print('dimension, polynomial, distances for b=1..m+1, pair spectrum:', direct_test(m))
    print('complete m=3 coordinate-order search:', exhaust_dimension_three())
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
