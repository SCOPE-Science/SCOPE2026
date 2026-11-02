"""Standalone exhaustive check of neighborhood shattering on binary 2-subspaces of F_2^4.

Run alongside grassmann35_cert.json with: python verify_grassmann35.py
Standard-library Python only. The finite exhaustive search is the upper-bound certificate.
"""
import itertools
import json
from pathlib import Path


def all_binary_lines():
    # A rank-two binary subspace has exactly three nonzero vectors.
    out = set()
    for u in range(1, 16):
        for v in range(1, 16):
            if u == v:
                continue
            out.add(tuple(sorted((u, v, u ^ v))))
    return sorted(out)


def run():
    cert = json.loads((Path(__file__).resolve().parent / 'grassmann35_cert.json').read_text())
    lines = all_binary_lines()
    assert len(lines) == 35
    assert cert['lines_as_nonzero_vectors'] == [list(t) for t in lines]
    assert all(len(set(l)) == 3 and l[0] ^ l[1] ^ l[2] == 0 for l in lines)
    sets = [set(t) for t in lines]
    adjacency = [[int(i != j and bool(sets[i] & sets[j])) for j in range(35)] for i in range(35)]
    assert all(sum(row) == 18 for row in adjacency)
    assert all(adjacency[i][j] == adjacency[j][i] for i in range(35) for j in range(35))
    # A nonadjacent pair and an adjacent pair both have exactly 9 common neighbours.
    assert all(sum(adjacency[i][z] * adjacency[j][z] for z in range(35)) == 9
               for i in range(35) for j in range(i))
    queries = [sum(adjacency[i][j] << i for i in range(35)) for j in range(35)]

    support = cert['vc_support_indices']
    assert len(support) == 4 and len(set(support)) == 4
    witnesses = cert['vc_pattern_witnesses']
    assert len(witnesses) == 16
    for pattern, center in enumerate(witnesses):
        assert 0 <= center < 35
        observed = sum(adjacency[center][q] << r for r, q in enumerate(support))
        assert observed == pattern
    print('VC_LOWER_CERTIFICATE_PASS 4 support='+','.join(map(str, support)))

    count_4 = 0
    for tup in itertools.combinations(range(35), 4):
        patterns = {sum(adjacency[i][q] << r for r, q in enumerate(tup)) for i in range(35)}
        if len(patterns) == 16:
            count_4 += 1
    assert count_4 == 41160
    print('FOUR_SUPPORT_CENSUS_PASS 41160')

    count_5 = 0
    for tup in itertools.combinations(range(35), 5):
        patterns = {sum(adjacency[i][q] << r for r, q in enumerate(tup)) for i in range(35)}
        assert len(patterns) < 32, ('Five-query support unexpectedly shattered', tup)
        count_5 += 1
    assert count_5 == 324632
    print('VC_UPPER_EXHAUSTIVE_PASS 324632')

    leaves = []
    nodes = 0
    def walk(node, depth, path):
        nonlocal nodes
        if depth == 5:
            assert isinstance(node, int) and 0 <= node < 35
            assert all(adjacency[node][q] == ans for q, ans in path)
            leaves.append(node)
            return
        assert isinstance(node, dict) and set(node) == {'query','zero','one'}
        q = node['query']
        assert type(q) is int and 0 <= q < 35
        nodes += 1
        walk(node['zero'], depth + 1, path + [(q, 0)])
        walk(node['one'], depth + 1, path + [(q, 1)])
    assert cert['littlestone_depth'] == 5
    walk(cert['decision_tree'], 0, [])
    assert nodes == 31 and len(leaves) == 32 and len(set(leaves)) == 32
    # All 35 concepts are distinct; depth six requires 64 leaf-distinct concepts.
    assert len(set(queries)) == 35 and 35 < 64
    print('LITTLESTONE_DEPTH_FIVE_CERTIFICATE_PASS 31 nodes 32 leaves')
    print('LITTLESTONE_DEPTH_SIX_CARDINALITY_OBSTRUCTION_PASS 35<64')
    print('BINARY_GRASSMANN_35_ALL_CHECKS_PASS')

if __name__ == '__main__':
    run()
