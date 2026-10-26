"""Exhaustive perfect-matching decomposition of the Desargues graph, GP(10,3).

Uses only the Python standard library. Run with certificate.json in this directory.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
import hashlib
import json
from pathlib import Path


def graph_edges():
    n = 10
    edges = set()
    for i in range(n):
        for a, b in ((i, (i + 1) % n), (i, n + i),
                     (n + i, n + ((i + 3) % n))):
            edges.add(tuple(sorted((a, b))))
    return tuple(sorted(edges))


def build():
    edges = graph_edges()
    assert len(edges) == 30
    incidence = [[] for _ in range(20)]
    for j, (a, b) in enumerate(edges):
        incidence[a].append((b, j))
        incidence[b].append((a, j))
    assert all(len(row) == 3 for row in incidence)

    @lru_cache(None)
    def rec(remaining):
        if remaining == 0:
            return (0,)
        u = (remaining & -remaining).bit_length() - 1
        solutions = []
        for v, e in incidence[u]:
            if remaining & (1 << v):
                new = remaining ^ (1 << u) ^ (1 << v)
                solutions.extend((1 << e) | m for m in rec(new))
        return tuple(solutions)

    matchings = set(rec((1 << 20) - 1))
    assert len(matchings) == 60
    all_edges = (1 << 30) - 1

    def factor_cycles(edge_mask):
        local = [[] for _ in range(20)]
        for j, (u, v) in enumerate(edges):
            if (edge_mask >> j) & 1:
                local[u].append((v, j))
                local[v].append((u, j))
        assert all(len(lst) == 2 for lst in local)
        unseen = set(range(20))
        result = []
        while unseen:
            start = min(unseen)
            at, prior = start, -1
            cycle = []
            while at in unseen:
                unseen.remove(at)
                v, e = next((v, e) for v, e in local[at] if v != prior)
                cycle.append(e)
                prior, at = at, v
            assert at == start
            result.append(tuple(cycle))
        assert sum(map(len, result)) == 20
        return result

    matching_profile = Counter()
    colorings = set()
    for m0 in matchings:
        cycles = factor_cycles(all_edges ^ m0)
        matching_profile[tuple(sorted(map(len, cycles)))] += 1
        assert all(len(c) % 2 == 0 for c in cycles)
        for choice in range(1 << len(cycles)):
            m1, m2 = 0, 0
            for j, c in enumerate(cycles):
                for pos, edge_id in enumerate(c):
                    if (pos + ((choice >> j) & 1)) % 2:
                        m1 |= 1 << edge_id
                    else:
                        m2 |= 1 << edge_id
            colorings.add(tuple(sorted((m0, m1, m2))))
    assert matching_profile == Counter({(10, 10): 36, (20,): 24})
    assert len(colorings) == 32
    cs = sorted(colorings)
    index = {c: i for i, c in enumerate(cs)}
    exchange_edges = set()
    coloring_profile = Counter()
    for i, c in enumerate(cs):
        pattern = []
        for a, b in combinations(range(3), 2):
            cycles = factor_cycles(c[a] | c[b])
            pattern.append(tuple(sorted(map(len, cycles))))
            for cycle in cycles:
                delta = sum(1 << e for e in cycle)
                next_state = list(c)
                next_state[a] ^= delta
                next_state[b] ^= delta
                key = tuple(sorted(next_state))
                assert key in index
                j = index[key]
                if i != j:
                    exchange_edges.add(tuple(sorted((i, j))))
        coloring_profile[tuple(sorted(pattern))] += 1
    assert coloring_profile == Counter({((10, 10), (10, 10), (10, 10)): 20,
                                        ((10, 10), (20,), (20,)): 12})
    graph = [set() for _ in cs]
    for i, j in exchange_edges:
        graph[i].add(j)
        graph[j].add(i)
    assert Counter(map(len, graph)) == Counter({3: 20, 1: 12})
    assert len(exchange_edges) == 36
    comps = []
    remaining = set(range(32))
    while remaining:
        seed = min(remaining)
        q = [seed]
        remaining.remove(seed)
        for i in q:
            for j in graph[i]:
                if j in remaining:
                    remaining.remove(j)
                    q.append(j)
        comps.append(sorted(q))
    comps.sort(key=lambda c: (-len(c), c))
    assert sorted(map(len, comps)) == [2, 2, 2, 2, 2, 2, 20]
    return {
        'base_edges': [list(edge) for edge in edges],
        'colorings': [list(c) for c in cs],
        'kempe_edges': [list(e) for e in sorted(exchange_edges)],
        'components': comps,
    }


def check_isomorphism(certificate):
    large = certificate['components'][0]
    iso = {int(k): v for k, v in certificate['desargues_isomorphism'].items()}
    assert set(iso) == set(large)
    assert set(iso.values()) == set(range(20))
    canonical_edges = graph_edges()
    image = {tuple(sorted((iso[i], iso[j]))) for i, j in certificate['kempe_edges']
             if i in iso and j in iso}
    assert image == set(canonical_edges), 'The 20-state component must be GP(10,3)'
    assert len(image) == 30


def main():
    actual = build()
    certificate = json.loads(Path('certificate.json').read_text(encoding='utf8'))
    assert set(certificate) == set(actual) | {'desargues_isomorphism'}
    for k, value in actual.items():
        assert certificate[k] == value, f'Certificate mismatch: {k}'
    check_isomorphism(certificate)
    print(json.dumps({
        'graph': 'GP(10,3)', 'perfect_matchings': 60,
        'complement_type_10_10': 36, 'complement_type_20': 24,
        'three_edge_coloring_classes': len(actual['colorings']),
        'kempe_edges': len(actual['kempe_edges']),
        'component_sizes': [len(x) for x in actual['components']],
        'isomorphic_twenty_vertex_component': True,
        'certificate_sha256': hashlib.sha256(Path('certificate.json').read_bytes()).hexdigest()
    }, sort_keys=True))


if __name__ == '__main__':
    main()
