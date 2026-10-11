#!/usr/bin/env python3
"""Exact finite verification for nine-term two-variable root-of-unity Fourier polynomials.

Run: python3 checker.py
Only standard-library modules are needed. All energy calculations use exact integer pairs
in the Gaussian or Eisenstein rings. The two energy formulas are independently summed.
"""
from itertools import product
from collections import Counter

POSITIONS = [(r, c) for r in range(3) for c in range(3)]
SHIFT_PAIRS = {}
SUM_PAIRS = {}
for a, u in enumerate(POSITIONS):
    for b, v in enumerate(POSITIONS):
        SHIFT_PAIRS.setdefault((u[0]-v[0], u[1]-v[1]), []).append((a, b))
        SUM_PAIRS.setdefault((u[0]+v[0], u[1]+v[1]), []).append((a, b))

RINGS = {
    2: ('Gaussian', [(1, 0), (-1, 0)]),
    3: ('Eisenstein', [(1, 0), (0, 1), (-1, -1)]),
    4: ('Gaussian', [(1, 0), (0, 1), (-1, 0), (0, -1)]),
    6: ('Eisenstein', [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]),
}
EXPECTED = {2: (113, 8), 3: (97, 2), 4: (105, 16), 6: (97, 6)}
FREE = (2, 4, 5, 6, 7, 8)  # row-major; entries (0,0), (0,1), (1,0) normalized

def pair_mul(x, y, ring):
    a, b = x; c, d = y
    if ring == 'Gaussian':
        return a*c-b*d, a*d+b*c
    return a*c-b*d, a*d+b*c-b*d

def pair_conj(x, ring):
    a, b = x
    return (a, -b) if ring == 'Gaussian' else (a-b, -b)

def pair_norm(x, ring):
    a, b = x
    return a*a+b*b if ring == 'Gaussian' else a*a-a*b+b*b

def energy_from_difference(coeff, ring):
    out = 0
    for pairs in SHIFT_PAIRS.values():
        a = b = 0
        for i, j in pairs:
            c, d = pair_mul(coeff[i], pair_conj(coeff[j], ring), ring)
            a += c; b += d
        out += pair_norm((a, b), ring)
    return out

def energy_from_convolution(coeff, ring):
    out = 0
    for pairs in SUM_PAIRS.values():
        a = b = 0
        for i, j in pairs:
            c, d = pair_mul(coeff[i], coeff[j], ring)
            a += c; b += d
        out += pair_norm((a, b), ring)
    return out

def check():
    results = {}
    for q, (ring, roots) in RINGS.items():
        frequencies = Counter()
        winners = []
        for z in product(range(q), repeat=6):
            e = [0]*9
            for idx, exponent in zip(FREE, z):
                e[idx] = exponent
            coeff = [roots[t] for t in e]
            e1 = energy_from_difference(coeff, ring)
            e2 = energy_from_convolution(coeff, ring)
            assert e1 == e2, (q, z, e1, e2)
            frequencies[e1] += 1
            if not winners or e1 < winners[0][0]:
                winners = [(e1, z)]
            elif e1 == winners[0][0]:
                winners.append((e1, z))
        optimum, normalized_count = EXPECTED[q]
        assert min(frequencies) == optimum, (q, min(frequencies))
        assert len(winners) == normalized_count, (q, len(winners))
        assert frequencies[optimum] == normalized_count
        assert max(frequencies) == 361
        results[q] = winners
        print(f'CHECK_PASS q={q} normalized_checked={q**6} minimum={optimum} '
              f'normalized_minimizers={len(winners)} all_minimizers={len(winners)*q**3} '
              f'distinct_energy_levels={len(frequencies)}')
    # A complete exact uniqueness certificate for the ternary phase alphabet.
    assert [z for _, z in results[3]] == [
        (0, 1, 2, 0, 2, 1),
        (0, 2, 1, 0, 1, 2),
    ]
    assert [z for _, z in results[6]] == [
        (0, 2, 4, 0, 4, 2), (0, 4, 2, 0, 2, 4),
        (1, 2, 5, 5, 3, 2), (1, 4, 3, 5, 1, 4),
        (5, 2, 3, 1, 5, 2), (5, 4, 1, 1, 3, 4),
    ]
    # Analytical lower bound: mixed differences have overlap counts 1, 2 or 4,
    # none a multiple of three; therefore their ternary autocorrelations cannot vanish.
    mixed = [h for h in SHIFT_PAIRS if h != (0, 0)
             and h[0] != 0 and h[1] != 0]
    assert len(mixed) == 16
    assert sorted(set(len(SHIFT_PAIRS[h]) for h in mixed)) == [1, 2, 4]
    assert 81 + len(mixed) == 97
    print('CHECK_PASS ternary_mixed_overlap_lower_bound=97 normalized_winners=Fourier_matrix_and_conjugate')
    print('CHECK_PASS all_representatives_exactly_enumerated_and_both_ Parseval_identities_agree')

if __name__ == '__main__':
    check()
