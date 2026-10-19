#!/usr/bin/env python3
"""Exact, stdlib-only verification of the complete 8-bit / three-deletion list-size profile.
Usage: python3 verify_three_deletion_profile.py three_deletion_capacity_cert.json
"""
import itertools
import json
import sys
from fractions import Fraction


def subsequence_indices(n, r):
    return tuple(itertools.combinations(range(n), r))


def desc_mask(word, idxs):
    bits = f'{word:08b}'
    res = 0
    for positions in idxs:
        y = int(''.join(bits[i] for i in positions), 2)
        res |= 1 << y
    return res


def main(filename):
    c = json.load(open(filename, 'r', encoding='utf8'))
    assert c['n'] == 8 and c['deletions'] == 3
    idxs = subsequence_indices(8, 5)
    masks = [desc_mask(x, idxs) for x in range(256)]
    A = [[int(bool(masks[x] & (1 << y))) for x in range(256)] for y in range(32)]
    assert all(sum(row) == 93 for row in A)
    lines = []
    for line in c['dual_envelope']:
        y = [Fraction(*a) for a in line['dual_y']]
        assert len(y) == 32 and all(t >= 0 for t in y)
        z = [max(Fraction(0), Fraction(1) - sum(y[j]*A[j][x] for j in range(32))) for x in range(256)]
        assert all(sum(y[j]*A[j][x] for j in range(32)) + z[x] >= 1 for x in range(256))
        slope, intercept = Fraction(line['slope']), Fraction(line['intercept'])
        assert sum(y) == slope and sum(z) == intercept
        lines.append((slope, intercept))
    expected_lines = [(Fraction(10,3), Fraction(2,3)),
                      (Fraction(13,4),Fraction(1)),
                      (Fraction(3),Fraction(4)),
                      (Fraction(14,5),Fraction(10)),
                      (Fraction(8,3),Fraction(44,3)),
                      (Fraction(5,2),Fraction(47,2))]
    assert lines == expected_lines
    def bound(L):
        v = min([Fraction(256)] + [a * L + b for a,b in lines])
        return v.numerator // v.denominator
    assert bound(0) == 0 and bound(93) == 256
    seen = set()
    for row in c['witnesses']:
        L = row['list_size']
        assert 1 <= L <= 93 and L not in seen
        seen.add(L)
        words = row['codewords']
        assert len(set(words)) == len(words) and all(type(w) is int and 0 <= w < 256 for w in words)
        assert len(words) == bound(L), (L,len(words),bound(L))
        cover = [0] * 32
        for w in words:
            for y in range(32):
                cover[y] += A[y][w]
        assert max(cover) <= L, (L,max(cover))
    assert seen == set(range(1,94))
    for L in range(93,300):
        assert bound(L) == 256
    print('VERIFY_OK n=8 deletions=3 dual_lines=6 explicit_witnesses=93; exact capacity for every integer list size L>=0')

if __name__ == '__main__':
    assert len(sys.argv) == 2, 'Provide certificate JSON path'
    main(sys.argv[1])
