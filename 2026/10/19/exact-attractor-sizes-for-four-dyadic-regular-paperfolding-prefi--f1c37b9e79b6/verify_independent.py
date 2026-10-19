#!/usr/bin/env python3
"""Second exact verifier using integer bitsets for factor occurrence coverage."""
import json
from pathlib import Path


def paperfolding(length):
    return ''.join('0' if ((x // (x & -x)) % 4 == 1) else '1'
                   for x in range(1, length + 1))


def main():
    cases = json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf8'))['cases']
    for case in cases:
        n = case['length']
        word = paperfolding(n)
        gamma = sum(1 << p for p in case['attractor_positions_0_based'])
        covered = {}
        for width in range(1, n+1):
            occurrences = {}
            span = (1 << width) - 1
            for begin in range(n-width+1):
                f = word[begin:begin+width]
                occurrences[f] = occurrences.get(f, 0) | (span << begin)
            for factor, mask in occurrences.items():
                assert gamma & mask, (n, width, factor)
            covered.update(occurrences)
        assert len(covered) == case['expected_distinct_factor_count']
        weighted = [0]*n
        for row in case['lower_certificate_factors']:
            mask = covered[row['factor']]
            for p in range(n):
                weighted[p] += row['numerator'] * ((mask >> p) & 1)
        den = case['lower_certificate_denominator']
        numer = sum(r['numerator'] for r in case['lower_certificate_factors'])
        assert max(weighted) <= den
        assert numer > (len(case['attractor_positions_0_based'])-1)*den
        print('BITSET_OK',n,len(covered),max(weighted))
    print('INDEPENDENT_VERIFY_OK')


if __name__=='__main__':
    main()
