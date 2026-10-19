#!/usr/bin/env python3
"""Exhaustive exact arithmetic for cross-join geodesics of binary order-five universal cycles.

Run: python3 verify.py --emit    to write the reference CSV.
     python3 verify.py            to independently rebuild and check the CSV.
Python 3.9+ standard library only.
"""
import argparse
import csv
from collections import Counter, deque
from itertools import combinations
from pathlib import Path

N = 32
V = 16
FREE = (1 << 15) - 2
PAIR_FLIPS = tuple((1 << a) | (1 << b) for a, b in combinations(range(16), 2))
TARGET_COUNTS = {
    3617656: 16, 3781260: 32, 3840330: 32, 3910424: 32,
    3933668: 32, 3972200: 16, 4094570: 32, 4185332: 32,
    4245320: 16, 4697036: 32, 4807588: 32, 4908248: 16,
    5096758: 32, 5954072: 16,
}
DISTANCE_COUNTS = {1: 38704, 2: 305376, 3: 758800,
                   4: 710976, 5: 254800, 6: 27104, 7: 368}
ECCENTRICITIES = {5: 48, 6: 1264, 7: 736}


def successor(edge, mask):
    vertex = edge & 15
    incoming = edge >> 4
    selected = (mask >> vertex) & 1
    return 2 * vertex + (incoming ^ selected)


def is_one_cycle(mask):
    state, visited = 0, 0
    for _ in range(32):
        if (visited >> state) & 1:
            return False
        visited |= 1 << state
        state = successor(state, mask)
    return state == 0 and visited == (1 << 32) - 1


def all_masks_by_pairings():
    return {mask for mask in range(1 << V) if is_one_cycle(mask)}


def masks_by_eulerian_dfs():
    """Independent enumeration of paths in the directed four-bit graph."""
    outputs = set()
    trail = [0]

    def visit(vertex, marked):
        if len(trail) == 32:
            if vertex == 0:
                result = 0
                for j, edge in enumerate(trail):
                    outgoing = trail[(j + 1) % 32]
                    assert outgoing >> 1 == (edge & 15)
                    bit = (edge >> 4) ^ (outgoing & 1)
                    result |= bit << (edge & 15)
                outputs.add(result)
            return
        for outgoing in (2 * vertex, 2 * vertex + 1):
            if not (marked >> outgoing) & 1:
                trail.append(outgoing)
                visit(outgoing & 15, marked | (1 << outgoing))
                trail.pop()

    visit(0, 1)
    return outputs


def cross_pair_alternation(pos, v, w):
    """Independent cross-join criterion via alternating conjugate visits."""
    a, b = pos[v], pos[v + 16]
    c, d = pos[w], pos[w + 16]

    def inside(z):
        return (a < z < b) if a < b else (z > a or z < b)
    return inside(c) != inside(d)


def make_graph(masks):
    labels = sorted(masks)
    index = {m: i for i, m in enumerate(labels)}
    neighbors = [[] for _ in labels]
    for i, mask in enumerate(labels):
        neighbors[i] = [index[mask ^ flip] for flip in PAIR_FLIPS
                        if (mask ^ flip) in index]
        # For independent validation, exactly each pair of transition changes
        # must alternate around the original Eulerian cycle.
        pos = {}
        e = 0
        for j in range(32):
            pos[e] = j
            e = successor(e, mask)
        assert len(pos) == 32
        for v, w in combinations(range(V), 2):
            y = mask ^ (1 << v) ^ (1 << w)
            assert (y in index) == cross_pair_alternation(pos, v, w), (mask, v, w)
    assert sum(map(len, neighbors)) // 2 == 38704
    assert Counter(len(lst) for lst in neighbors) == {
        31: 88, 32: 152, 33: 240, 34: 272, 35: 216, 36: 136,
        37: 208, 38: 16, 39: 176, 40: 64, 41: 48, 42: 16,
        43: 40, 45: 112, 47: 136, 48: 48, 49: 32, 51: 16,
        60: 8, 62: 16, 64: 8,
    }
    return labels, index, neighbors


def shortest_distances_and_multiplicities(neighbors, source):
    distances = [-1] * len(neighbors)
    paths = [0] * len(neighbors)
    distances[source] = 0
    paths[source] = 1
    todo = deque([source])
    while todo:
        u = todo.popleft()
        for v in neighbors[u]:
            if distances[v] < 0:
                distances[v] = distances[u] + 1
                todo.append(v)
            if distances[v] == distances[u] + 1:
                paths[v] += paths[u]
    return distances, paths


def paths_using_only_difference_coordinates(first, second, masks):
    """Independent subset dynamic program for shortest geodesic length seven.

    Every geodesic between a complement pair changes each differing
    transition coordinate exactly once, in one of seven disjoint pairs.
    """
    assert first ^ second == FREE
    states = {0: 1}
    for _ in range(7):
        new = {}
        for flipped, number in states.items():
            left = FREE ^ flipped
            remaining = [v for v in range(1, 15) if (left >> v) & 1]
            for v, w in combinations(remaining, 2):
                more = flipped | (1 << v) | (1 << w)
                if (first ^ more) in masks:
                    new[more] = new.get(more, 0) + number
        states = new
    return states.get(FREE, 0)


def compute():
    valid = all_masks_by_pairings()
    assert len(valid) == 2048
    independent = masks_by_eulerian_dfs()
    assert independent == valid, 'Eulerian DFS and transition pairing disagree'
    assert all((mask & 32769) == 32769 for mask in valid)
    labels, index, neighbors = make_graph(valid)
    ecc = Counter()
    pairs_by_dist = Counter()
    diametral = []
    for i, first in enumerate(labels):
        dist, npaths = shortest_distances_and_multiplicities(neighbors, i)
        assert -1 not in dist
        ecc[max(dist)] += 1
        for j in range(i + 1, len(labels)):
            d = dist[j]
            pairs_by_dist[d] += 1
            assert d == (first ^ labels[j]).bit_count() // 2
            if d == 7:
                assert first ^ labels[j] == FREE
                diametral.append((first, labels[j], npaths[j]))
    assert dict(pairs_by_dist) == DISTANCE_COUNTS
    assert dict(ecc) == ECCENTRICITIES
    assert len(diametral) == 368
    for a, b, npaths in diametral:
        assert paths_using_only_difference_coordinates(a, b, valid) == npaths
    spectrum = Counter(row[2] for row in diametral)
    assert dict(spectrum) == TARGET_COUNTS
    return diametral, spectrum


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--emit', action='store_true')
    args = p.parse_args()
    rows, dist = compute()
    outfile = Path(__file__).with_name('diametral_pairs.csv')
    if args.emit:
        with outfile.open('w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['mask_a_hex', 'mask_b_hex', 'shortest_cross_join_histories'])
            for a, b, count in rows:
                writer.writerow([f'{a:04x}', f'{b:04x}', count])
    else:
        with outfile.open(newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            seen = [(int(row['mask_a_hex'], 16), int(row['mask_b_hex'], 16),
                     int(row['shortest_cross_join_histories'])) for row in reader]
        assert seen == rows, 'CSV differs from independent computation'
    print('VERIFY_OK Eulerian_DFS=2048 pairings_tested=65536 graph_edges=38704')
    print('VERIFY_OK all_pairs=2096128 cross_join_diameter=7 diametral_pairs=368')
    print('VERIFY_OK independent_cross_join_interleavings=yes, Hamming_half_metric=yes')
    print('VERIFY_OK geodesic_dynamic_program_agrees_with_BFS=368_pairs')
    print('VERIFY_OK distance_marginal=' + ','.join(f'{k}:{v}' for k,v in sorted(DISTANCE_COUNTS.items())))
    print('VERIFY_OK geodesic_levels=' + ','.join(f'{k}:{v}' for k,v in sorted(dist.items())))


if __name__ == '__main__':
    main()
