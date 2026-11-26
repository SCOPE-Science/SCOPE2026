"""Exact support-size distributions for the two Gray blocks."""
from collections import Counter
from itertools import product
from pathlib import Path
import json


def spaces(n):
    if n == 0:
        yield 0, frozenset({0})
        return
    top = 1 << (n-1)
    for d, x in spaces(n-1):
        yield d, x
        unseen = set(range(top, 2*top))
        while unseen:
            v = min(unseen)
            affine = {v^w for w in x}
            unseen.difference_update(affine)
            yield d+1, x|affine


def main():
    cert = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
    expected = [{int(w): c for w, c in cert['support_spectra'][str(r)].items()} for r in range(1,7)]
    # Bit i carries coordinate i+1 of each three-bit block.
    defining = [(p,q) for p,q in product(range(8), repeat=2) if p&4 or q&2]
    first = [q|(p<<3) for p,q in defining]
    second = [(p^q)|(p<<3) for p,q in defining]
    assert len(first) == len(set(first)) == len(second) == len(set(second)) == 48
    S, T = set(range(64))-set(first), set(range(64))-set(second)
    assert S == {v for v in range(64) if not v&32 and not v&2}
    assert T == {v for v in range(64) if not v&32 and ((v>>1)^(v>>4))&1 == 0}
    assert (len(S),len(T),len(S&T)) == (16,16,8)
    assert Counter(Counter(first+second).values()) == {1:16,2:40}
    for r in range(1,7):
        W = {0}
        for v in cert['annihilator_witness_bases'][f'r{r}']:
            assert len(v) == 6 and set(v) <= {'0','1'}
            vector = sum((1 << i) for i, bit in enumerate(v) if bit == '1')
            W |= {w^vector for w in W}
        assert len(W) == 2**(6-r)
        assert len(W&S) == len(W&T) == 2**max(0,4-r)
    rows = [Counter() for _ in expected]
    for h,W in spaces(6):
        if h == 6:
            continue
        by_formula = 96 - 2**(h+1) + len(W&S) + len(W&T)
        direct = sum(v not in W for v in first+second)
        assert by_formula == direct
        rows[5-h][direct] += 1
    assert rows == expected
    assert {str(i):sum(row.values()) for i,row in enumerate(rows,1)} == cert['subspaces_by_dimension']
    assert sum(map(sum,(r.values() for r in rows))) == cert['subspaces_checked'] == 2824
    assert [min(r) for r in rows] == cert['generalized_hamming_weights']
    assert [r[min(r)] for r in rows] == cert['minimum_subcode_counts']
    assert {0:1, **rows[0]} == {int(w):c for w,c in cert['source_weight_distribution'].items()}
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
