#!/usr/bin/env python3
"""Separate finite enumeration of maximal contranominal subcontexts.

No third-party packages are needed. The mathematical proof covers every dimension;
this checker tests dimensions two through eight by exhaustive candidate search.
"""
from itertools import combinations
from math import comb


def check(d):
    n = 1 << d
    near = [sum(1 << j for j in range(n) if (i ^ j).bit_count() <= 1)
            for i in range(n)]
    ball2 = [tuple(j for j in range(i + 1, n) if (i ^ j).bit_count() <= 2)
             for i in range(n)]
    sq = pa = candidates = 0
    for a in range(n):
        for b in ball2[a]:
            others = [c for c in ball2[b] if (a ^ c).bit_count() <= 2]
            for c, e in combinations(others, 2):
                if (c ^ e).bit_count() > 2:
                    continue
                candidates += 1
                obj = (a, b, c, e)
                witness = []
                for x in obj:
                    possible = (1 << n) - 1
                    for z in obj:
                        if z != x:
                            possible &= near[z]
                    possible &= ~near[x]
                    witness.append(possible)
                if not all(w != 0 for w in witness):
                    continue
                assert all(w.bit_count() == 1 for w in witness), (d, obj)
                ys = [w.bit_length() - 1 for w in witness]
                assert len(set(ys)) == 4
                for i, x in enumerate(obj):
                    for j, y in enumerate(ys):
                        assert ((x ^ y).bit_count() <= 1) == (i != j)
                distances = {(x ^ y).bit_count() for x, y in combinations(obj, 2)}
                if distances == {1, 2}:
                    sq += 1
                    assert len(set(obj)) == 4
                else:
                    assert distances == {2}, (d, obj, distances)
                    pa += 1
    assert sq == (1 << (d - 2)) * comb(d, 2), (d, sq)
    assert pa == (1 << (d - 2)) * comb(d, 3), (d, pa)
    assert sq + pa == (1 << (d - 2)) * comb(d + 1, 3)
    return candidates, sq, pa


if __name__ == '__main__':
    for dimension in range(2, 9):
        c, s, p = check(dimension)
        print(f'DIMENSION {dimension}: diameter_two_four_sets={c} '
              f'squares={s} parity_tetrahedra={p} '
              f'contrascales={s + p} PASS', flush=True)
    print('VERIFY_OK all_maximal_contranominal_four_scales=PASS '
          'witness_uniqueness=PASS geometric_type_counts=PASS')
