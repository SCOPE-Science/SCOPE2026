"""Exact checks for an incidence-logic threshold on Steiner triple systems.

Usage: python verify_steiner.py
This script needs only the Python standard library.
"""
from collections import Counter
from itertools import combinations


def projective_15():
    points = tuple(range(1, 16))
    blocks = tuple(sorted({tuple(sorted((u, v, u ^ v)))
                           for u, v in combinations(points, 2)}))
    return points, blocks


def bose_15():
    points = tuple((x, i) for x in range(5) for i in range(3))
    blocks = [tuple((x, i) for i in range(3)) for x in range(5)]
    for x, y in combinations(range(5), 2):
        z = 3 * (x + y) % 5  # reciprocal of two in F_5
        for i in range(3):
            blocks.append(((x, i), (y, i), (z, (i + 1) % 3)))
    return points, tuple(tuple(sorted(t)) for t in blocks)


def validate_design(points, blocks):
    assert len(points) == 15 and len(blocks) == 35
    assert len(set(blocks)) == 35
    incidence = Counter(pair for block in blocks for pair in combinations(block, 2))
    assert len(incidence) == 105
    assert all(multiplicity == 1 for multiplicity in incidence.values())
    assert all(len(block) == 3 and len(set(block)) == 3 for block in blocks)
    assert set().union(*map(set, blocks)) == set(points)


def pasch_data(points, blocks):
    completion = {}
    for block in blocks:
        for a, b in combinations(block, 2):
            pair = frozenset((a, b))
            assert pair not in completion
            completion[pair] = next(x for x in block if x != a and x != b)
    line_set = set(map(frozenset, blocks))
    count = 0
    noncollinear = 0
    for a, b, c in combinations(points, 3):
        if frozenset((a, b, c)) in line_set:
            continue
        noncollinear += 1
        x = completion[frozenset((a, b))]
        y = completion[frozenset((a, c))]
        z = completion[frozenset((b, c))]
        assert len({a, b, c, x, y, z}) == 6
        if frozenset((x, y, z)) in line_set:
            count += 1
    return noncollinear, count


def incidence_graph(points, blocks, marks):
    index = {p: i for i, p in enumerate(points)}
    m = len(points)
    adjacency = [[] for _ in range(m + len(blocks))]
    colors = [(0, 1 + marks.index(p) if p in marks else 0) for p in points]
    colors += [(1, 0)] * len(blocks)
    for j, block in enumerate(blocks):
        for p in block:
            i = index[p]
            adjacency[i].append(m + j)
            adjacency[m + j].append(i)
    return adjacency, colors


def signatures(graph1, graph2, rounds):
    ad1, cl1 = graph1
    ad2, cl2 = graph2
    histories = [Counter(cl1) == Counter(cl2)]
    for _ in range(rounds):
        def next_keys(ad, cl):
            return [(cl[i], tuple(sorted(Counter(cl[j] for j in ad[i]).items())))
                    for i in range(len(cl))]
        key1, key2 = next_keys(ad1, cl1), next_keys(ad2, cl2)
        canonical = {key: i for i, key in enumerate(sorted(set(key1 + key2), key=repr))}
        cl1 = [canonical[key] for key in key1]
        cl2 = [canonical[key] for key in key2]
        histories.append(Counter(cl1) == Counter(cl2))
    return tuple(histories)


def main():
    p, pg = projective_15()
    q, bose = bose_15()
    validate_design(p, pg)
    validate_design(q, bose)
    assert pasch_data(p, pg) == (420, 420)
    assert pasch_data(q, bose) == (420, 0)
    print('DESIGNS PASS: 15 points, 35 blocks, 105 pairs exactly once each')
    print('PASCH PASS: 420/420 noncollinear triples in projective design; 0/420 in Bose design')

    # Every choice of up to two differently named points is indistinguishable.
    for count in (0, 1, 2):
        source = (tuple(),) if count == 0 else combinations(p, count)
        target = (tuple(),) if count == 0 else combinations(q, count)
        standard_p = incidence_graph(p, pg, p[:count])
        standard_q = incidence_graph(q, bose, q[:count])
        assert all(signatures(incidence_graph(p, pg, marks), standard_q, 6) == (True,) * 7
                   for marks in source)
        assert all(signatures(standard_p, incidence_graph(q, bose, marks), 6) == (True,) * 7
                   for marks in target)
        print(f'ANCHORS {count} PASS: all choices tested on both designs')

    # Collinear triples remain indistinguishable even when all three points are named.
    pg_collinear = next(block for block in pg)
    bose_collinear = next(block for block in bose)
    assert signatures(incidence_graph(p, pg, pg_collinear),
                      incidence_graph(q, bose, bose_collinear), 6) == (True,) * 7
    print('COLLINEAR THREE PASS: no separation through six rounds')

    # The 3 noncollinear anchors detect a Pasch exactly at refinement round 3.
    pg_noncollinear = (1, 2, 4)
    bose_noncollinear = ((0, 0), (1, 0), (2, 0))
    profile = signatures(incidence_graph(p, pg, pg_noncollinear),
                         incidence_graph(q, bose, bose_noncollinear), 5)
    assert profile == (True, True, True, False, False, False), profile
    print('RANK PASS: refinement profiles agree at rounds 0,1,2; first differ at round 3')
    print('CERTIFICATE PASS')


if __name__ == '__main__':
    main()
