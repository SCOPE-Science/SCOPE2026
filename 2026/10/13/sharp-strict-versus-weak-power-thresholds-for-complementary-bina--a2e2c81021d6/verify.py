#!/usr/bin/env python3
"""Finite certificates for complementary binary power-free morphisms.

The positive implication from the finite tests uses Kobayashi's
sufficient criterion as stated in Shallit--Shur--Zorcic, Theorem 4,
arXiv:2310.15064. All enumerations below are exact integer operations.
"""
import csv
from fractions import Fraction
from itertools import product
from pathlib import Path

CASES = ((5, 8, 3, ('01001', '01101')),
         (7, 5, 2, ('0100110', '0110010')))

def strings(n):
    for bits in product('01', repeat=n):
        yield ''.join(bits)

def flip(word):
    return ''.join('1' if c == '0' else '0' for c in word)

def period(word):
    return next(p for p in range(1, len(word) + 1)
                if word[:-p] == word[p:])

def exponent_bound(word, num, den, plus):
    """Return one forbidden (start,length,period,factor) or None.

    plus=True prohibits exponent > num/den; otherwise prohibits >=.
    Checking every start and every possible period proves exhaustiveness.
    """
    n = len(word)
    for size in range(1, n + 1):
        for i in range(n - size + 1):
            for p in range(1, size + 1):
                if (size * den <= num * p) if plus else (size * den < num * p):
                    continue
                if all(word[j] == word[j+p] for j in range(i, i + size - p)):
                    return i, size, p, word[i:i+size]
    return None

def image(v, x):
    complement = flip(v)
    return ''.join(v if b == '0' else complement for b in x)

def inputs(num, den, plus):
    return [x for n in range(1, 5) for x in strings(n)
            if exponent_bound(x, num, den, plus) is None]

def positive_conditions(v, num, den):
    k = len(v)
    comp = flip(v)
    assert k < 2 * period(v), 'Kobayashi condition (a)'
    assert v[0] != comp[0] and v[-1] != comp[-1], '(b1),(b2)'
    for h0 in (v, comp):
        for h1 in (v, comp):
            for t in range((k + 1)//2, k):
                if h0[:t] == h1[-t:]:
                    assert h0[t:] == h1[:-t], '(b3)'
    src = inputs(num, den, plus=True)
    assert len(src) == 22
    max_e = Fraction(0)
    for x in src:
        w = image(v, x)
        assert exponent_bound(w, num, den, plus=True) is None, '(c)'
        # Independent fraction-valued critical-exponent check.
        for i in range(len(w)):
            for j in range(i+1, len(w)+1):
                t = w[i:j]
                max_e = max(max_e, Fraction(len(t), period(t)))
    assert max_e == Fraction(num, den)
    return len(src)

def build_witnesses():
    rows = []
    for k, num, den, expected in CASES:
        for plus in (False, True):
            good = []
            source = inputs(num, den, plus)
            assert len(source) == 22
            for suffix in strings(k-1):
                v = '0' + suffix
                for x in source:
                    witness = exponent_bound(image(v,x), num, den, plus)
                    if witness is not None:
                        i, size, p, factor = witness
                        rows.append((k, f'{num}/{den}', int(plus), v,
                                     x, i, size, p, factor))
                        break
                else:
                    good.append(v)
            assert good == (list(expected) if plus else [])
    return rows

def verify_certificate(path):
    expected = build_witnesses()
    with Path(path).open(newline='', encoding='utf-8') as fp:
        reader = csv.reader(fp, delimiter='\t')
        assert next(reader) == ['k','boundary','plus','image0','input',
                                'factor_start','factor_length','factor_period','factor']
        got = list(reader)
    assert got == [[str(y) for y in row] for row in expected]
    for k, num, den, vset in CASES:
        for v in vset:
            positive_conditions(v, num, den)
    print('VERIFY_OK normalized_candidates=80 failed_strict=80 '
          'failed_plus=76 surviving_plus=4 finite_source_words=22 '
          'boundaries=8/3,5/2')

def make_certificate(path):
    with Path(path).open('w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp, delimiter='\t', lineterminator='\n')
        writer.writerow(['k','boundary','plus','image0','input',
                         'factor_start','factor_length','factor_period','factor'])
        writer.writerows(build_witnesses())

if __name__ == '__main__':
    verify_certificate(Path(__file__).with_name('witnesses.tsv'))
