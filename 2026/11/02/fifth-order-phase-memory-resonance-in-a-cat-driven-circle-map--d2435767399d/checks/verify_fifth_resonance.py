#!/usr/bin/env python3
"""Independent exact-integer finite checks for cat-driven phase moments.

The finite search is a stress test. The infinite minimal-resonance theorem
is proved analytically in RESULT.md, not inferred from this enumeration.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import factorial


def frequency_vectors(n):
    v = (1, 0)
    data = []
    for _ in range(n):
        data.append(v)
        v = (2*v[0]+v[1], v[0]+v[1])
    return data


def is_pair_cancellation(indices, signs):
    c = Counter()
    for j, s in zip(indices, signs):
        c[j] += s
    return all(z == 0 for z in c.values())


def is_three_site_resonance(indices, signs):
    c = Counter()
    for j, s in zip(indices, signs):
        c[j] += s
    c = {j: z for j, z in c.items() if z}
    if len(c) != 3:
        return False
    a, b, d = sorted(c)
    return b == a + 1 and d == a + 2 and (c[a], c[b], c[d]) in ((1, -3, 1), (-1, 3, -1))


def all_sign_resonances(n, degree):
    v = frequency_vectors(n)
    for indices in combinations_with_replacement(range(n), degree):
        for signs in product((-1, 1), repeat=degree):
            x = sum(s*v[j][0] for s, j in zip(signs, indices))
            y = sum(s*v[j][1] for s, j in zip(signs, indices))
            if x == y == 0:
                yield indices, signs


def ordered_multiplicity(indices):
    v = Counter(indices)
    w = factorial(len(indices))
    for count in v.values():
        w //= factorial(count)
    return w


def cos_moment(n, degree):
    # When alpha=pi/2, sin(phi+alpha)=cos(phi), and each of the two Fourier
    # characters carries coefficient 1/2. All arithmetic is exact.
    total = sum(ordered_multiplicity(idx) for idx, _ in all_sign_resonances(n, degree))
    return Fraction(total, 2**degree)


def test():
    counts = Counter()
    for degree in range(1, 6):
        for indices, signs in all_sign_resonances(17, degree):
            if degree in (2, 4):
                assert is_pair_cancellation(indices, signs), (degree, indices, signs)
            elif degree == 5:
                assert is_three_site_resonance(indices, signs), (indices, signs)
            else:
                raise AssertionError((degree, indices, signs))
            counts[degree] += 1
    assert counts[1] == counts[3] == 0
    assert counts[5] == 2 * (17 - 2)
    for n in range(1, 11):
        assert cos_moment(n, 1) == 0
        assert cos_moment(n, 2) == Fraction(n, 2)
        assert cos_moment(n, 3) == 0
        assert cos_moment(n, 4) == Fraction(3*n*(2*n-1), 8)
        assert cos_moment(n, 5) == Fraction(5*max(n-2, 0), 4)
    # Fourier coefficient for sin(phi+alpha), with z=e^{i alpha}, is
    # sigma*z^sigma/(2i). At the unique five-term relation the two
    # contributing sign patterns give (z-z^(-1))/(32i)=sin(alpha)/16.
    # Verify the signed frequency relation for every tested time triple.
    v = frequency_vectors(60)
    for j in range(58):
        assert all(v[j][d]+v[j+2][d] == 3*v[j+1][d] for d in (0, 1))
    print('PASS: exact 2D Fourier-resonance census through degree five at 17 sites;')
    print('PASS: exact first, second, third, fourth, fifth cosine moments for N=1,...,10;')
    print('PASS: 58 exact integer recurrence identities; analytic proof handles all N.')
    print('finite signed-resonance counts by degree:', dict(counts))


if __name__ == '__main__':
    test()
