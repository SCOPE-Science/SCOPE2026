#!/usr/bin/env python3
"""Exact finite checks for the minimal-domination concept class on cycles."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def cycle_neighborhoods(n):
    return [sum(1 << v for v in ((i - 1) % n, i, (i + 1) % n)) for i in range(n)]


def minimal_dominating_concepts(n):
    neighborhoods = cycle_neighborhoods(n)
    everything = (1 << n) - 1
    result = []
    for subset in range(1 << n):
        selected = [i for i in range(n) if subset & (1 << i)]
        covered = 0
        for i in selected:
            covered |= neighborhoods[i]
        if covered != everything:
            continue
        # Each selected vertex has a private dominated vertex.
        if all(any(neighborhoods[w] & subset == 1 << i
                   for w in range(n) if neighborhoods[w] & (1 << i))
               for i in selected):
            result.append(subset)
    return result


def trace_count(concepts, support):
    return len({sum(((c >> v) & 1) << j for j, v in enumerate(support))
                for c in concepts})


def vc_dimension(n, concepts):
    largest = 0
    witnesses = {}
    for size in range(1, n + 1):
        witness = next((s for s in combinations(range(n), size)
                        if trace_count(concepts, s) == 1 << size), None)
        if witness is None:
            break
        largest = size
        witnesses[size] = witness
    return largest, witnesses


def validate_tree(node, depth, path, concepts, leaves):
    if depth == 0:
        assert set(node) == {'witness'}
        witness = int(node['witness'], 16)
        assert witness in concepts
        assert all(((witness >> query) & 1) == answer for query, answer in path)
        leaves.append(witness)
        return 0
    assert set(node) == {'query', '0', '1'}
    query = node['query']
    assert isinstance(query, int) and 0 <= query < 11
    assert not any(query == previous for previous, _ in path)
    count_zero = validate_tree(node['0'], depth - 1, path + ((query, 0),), concepts, leaves)
    count_one = validate_tree(node['1'], depth - 1, path + ((query, 1),), concepts, leaves)
    return count_zero + count_one + 1


def main():
    expected = {
        3: (3, 1), 4: (6, 2), 5: (5, 2), 6: (5, 2),
        7: (14, 3), 8: (14, 3), 9: (21, 4),
        10: (27, 4), 11: (44, 4),
    }
    for n, (expected_count, expected_vc) in expected.items():
        c = minimal_dominating_concepts(n)
        v, witnesses = vc_dimension(n, c)
        assert len(c) == expected_count and v == expected_vc, (n, len(c), v)
        # The entropy upper bound already equals VC for n <= 10.
        if n <= 10:
            assert len(c).bit_length() - 1 == v, (n, len(c), v)
    print('FIRST_CYCLE_GAP_MINIMALITY_PASS n=3..10')

    c = minimal_dominating_concepts(11)
    cert = json.loads((HERE / 'cycle11_certificate.json').read_text(encoding='utf-8'))
    assert cert['n'] == 11 and cert['maximal_depth'] == 5
    assert len(c) == 44 and len(c).bit_length() - 1 == 5

    support = cert['vc_shattered_support']
    assert len(support) == 4 and trace_count(c, support) == 16
    witness_map = cert['vc_trace_witnesses']
    assert len(witness_map) == 16
    for pattern in range(16):
        witness = int(witness_map[f'{pattern:04b}'], 16)
        assert witness in c
        assert sum(((witness >> i) & 1) << j for j, i in enumerate(support)) == pattern

    spectrum = Counter(trace_count(c, s) for s in combinations(range(11), 5))
    expected_spectrum = {11: 11, 14: 22, 15: 44, 16: 11, 18: 11,
                         19: 88, 20: 33, 21: 77, 22: 44, 23: 11,
                         24: 66, 25: 33, 29: 11}
    assert dict(spectrum) == expected_spectrum
    assert sum(spectrum.values()) == 462 and max(spectrum) == 29
    print('C11_FIVE_QUERY_COMPLETE_SPECTRUM_PASS supports=462 max=29 achievers=11')

    leaves = []
    internal = validate_tree(cert['tree'], 5, tuple(), set(c), leaves)
    assert internal == 31 and len(leaves) == 32 and len(set(leaves)) == 32
    print('C11_DEPTH_FIVE_TREE_PASS internal=31 distinct_leaves=32 hypotheses=44')

    maximal_independent = [x for x in c if all(not ((x >> i) & 1 and
                             (x >> ((i + 1) % 11)) & 1) for i in range(11))]
    assert len(maximal_independent) == 22
    assert vc_dimension(11, maximal_independent)[0] == 4
    assert len(maximal_independent).bit_length() - 1 == 4
    print('C11_MAXIMAL_INDEPENDENT_COMPARISON_PASS count=22 VC=4 Ldim=4')
    print('ALL_CYCLE11_MINIMAL_DOMINATION_CHECKS_PASS')


if __name__ == '__main__':
    main()
