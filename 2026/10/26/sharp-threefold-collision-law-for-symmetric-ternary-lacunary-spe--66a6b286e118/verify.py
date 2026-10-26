"""Finite independent enumeration for the ternary lacunary triple-collision law.

This is a diagnostic for finite truncations, not a substitute for the proof.
"""
from collections import defaultdict
from itertools import combinations_with_replacement


def count_primitive(J):
    spectrum = [0] + [sgn * 3**j for j in range(J) for sgn in (-1, 1)]
    buckets = defaultdict(list)
    for triple in combinations_with_replacement(spectrum, 3):
        if any(triple[i] + triple[j] == 0 for i in range(3) for j in range(i + 1, 3)):
            continue
        buckets[sum(triple)].append(triple)
    return buckets


if __name__ == '__main__':
    for J in (3, 4, 5, 7, 11):
        buckets = count_primitive(J)
        assert 0 not in buckets
        assert max(map(len, buckets.values())) <= 3
        observed = {d for d, triples in buckets.items() if len(triples) == 3}
        expected = {sign * base * 3**k
                    for sign in (-1, 1) for base in (5, 7)
                    for k in range(max(0, J - 2))}
        # At truncation J, attaining both representations that use 3^(k+2)
        # requires k+2 < J. The first J-2 scales therefore all occur.
        assert observed == expected, (J, sorted(observed ^ expected))
        # Every other fiber has at most two primitive unordered representations.
        assert all(len(triples) < 3 for d, triples in buckets.items()
                   if d not in expected)
    test = count_primitive(11)
    assert {tuple(sorted(t)) for t in test[5]} == {(-3, -1, 9), (-1, 3, 3), (1, 1, 3)}
    assert len(test[7]) == 3
    print('VERIFY_OK finite_depths=3,4,5,7,11 max_count=3 exact_triple_fibers=36')
