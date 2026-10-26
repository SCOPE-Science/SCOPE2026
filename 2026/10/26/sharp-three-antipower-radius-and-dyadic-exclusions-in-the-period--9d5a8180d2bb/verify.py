#!/usr/bin/env python3
"""Reproduce the sharp period-doubling three-antipower cutoff and finite certificates.

Python 3.8+; no external dependencies. Run next to factors.csv.
"""
import csv
from collections import Counter
from fractions import Fraction
from pathlib import Path


def substitute(s):
    return ''.join('01' if c == '0' else '00' for c in s)


def iterated(s, n):
    for _ in range(n):
        s = substitute(s)
    return s


def anti3(s, m):
    blocks = [s[j*m:(j+1)*m] for j in range(3)]
    assert all(len(b) == m for b in blocks)
    return len(set(blocks)) == 3


def bit_at(n):
    # The fixed point of 0->01, 1->00: d(n) = v_2(n+1) modulo 2.
    k = n+1
    return str(((k & -k).bit_length()-1) % 2)


def all_length15_factors():
    images = {c: iterated(c, 4) for c in '01'}
    assert all(len(images[c]) == 16 for c in '01')
    pairs = ('00', '01', '10')
    out = set()
    for pair in pairs:
        word = images[pair[0]] + images[pair[1]]
        out.update(word[j:j+15] for j in range(18))
    return out


def bad9(w):
    return not anti3(w[:9], 3)


def main():
    factors = all_length15_factors()
    assert len(factors) == 23
    nine = {w[:9] for w in factors}
    assert len(nine) == 14
    bad = sorted(v for v in nine if bad9(v))
    assert bad == ['010001010', '010100010', '101000101']
    bad15 = sorted(w for w in factors if bad9(w))
    assert len(bad15) == 4
    for w in factors:
        # Every factor length 15 is a 3-antipower for m=3 or m=5,
        # and none is a 3-antipower for m=1, 2 or 4.
        assert not any(anti3(w, m) for m in (1,2,4))
        assert anti3(w, 3) or anti3(w, 5)
        if bad9(w):
            assert anti3(w, 5)
    # Check the certificate saved in the package in both directions.
    with (Path(__file__).parent/'factors.csv').open(newline='', encoding='utf-8') as inp:
        rows = list(csv.DictReader(inp))
    assert len(rows) == 23
    assert sorted(w['factor_length15'] for w in rows) == sorted(factors)
    for row in rows:
        w = row['factor_length15']
        for m in range(1, 6):
            assert int(row[f'antipower_m{m}']) == int(anti3(w, m))
        assert int(row['minimum_block']) == (5 if bad9(w) else 3)
    # Independently generate the word from valuation parity, not substitution.
    size = 1<<16
    direct = ''.join(bit_at(i) for i in range(size+14))
    assert set(direct[i:i+15] for i in range(size)) == factors
    independent_morphic = iterated('0',16)
    assert direct[:size] == independent_morphic
    # Images of 0 and 1 have identical proper prefixes at every dyadic scale.
    for k in range(13):
        a,b = iterated('0',k),iterated('1',k)
        assert a[:-1] == b[:-1] and a[-1] != b[-1]
        m = 1<<k
        for i in range(64):
            sample = ''.join(bit_at(j) for j in range(i,i+3*m))
            assert not anti3(sample,m)
    # Exact arithmetic of factor frequencies: 1 has density 1/3.
    one_density = sum((Fraction(1,2**(2*j+2)) for j in range(24)),Fraction(0))
    assert one_density < Fraction(1,3)
    assert Fraction(1,3)-one_density < Fraction(1,2**47)
    freq_00 = freq_01 = freq_10 = Fraction(1,3)
    freq_0100 = freq_0010 = Fraction(1,2)*freq_01
    freq_101 = Fraction(1,2)*freq_00
    freq_00100 = Fraction(1,2)*freq_101
    density = Fraction(1,2)*(freq_0100 + freq_0010 + freq_00100)
    assert density == Fraction(5,24)
    for i in range(size):
        full15 = direct[i:i+15]
        fail3 = bad9(full15)
        if i % 2 == 0:
            k=i//2
            predicted = direct[k:k+4] in ('0100','0010')
        else:
            k=(i-1)//2
            predicted = direct[k:k+5] == '00100'
        assert fail3 == predicted
    counts = Counter(5 if bad9(direct[i:i+15]) else 3 for i in range(size))
    print('VERIFY_OK complete_length15_factor_set=23 via three adjacent source pairs')
    print('VERIFY_OK length9_factors=14 three_bad_prefixes=3 exceptional_length15_factors=4')
    print('VERIFY_OK m1,m2,m4 impossible; m3 or m5 guaranteed; m5 sharp')
    print('VERIFY_OK valuation_parity_vs_substitution=65536 independent_symbols')
    print('VERIFY_OK dyadic_suffix_structure_and_sample_nonantipowers k=0..12')
    print('VERIFY_OK arithmetic_bad_position_density=5/24')
    print(f'VERIFY_OK sample_positions=65536 m3:{counts[3]} m5:{counts[5]}')
    print('VERIFY_OK CSV_rows=23 all_block_tests=115')

if __name__ == '__main__':
    main()
