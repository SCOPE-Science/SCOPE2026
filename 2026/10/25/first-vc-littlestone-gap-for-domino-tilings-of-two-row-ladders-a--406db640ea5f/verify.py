"""Reproducible exact checks for edge-query shattering of domino tilings.

Python >= 3.9; standard library only. All graph instances are constructed here.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path


def graph_ladder(n: int):
    vertices = tuple((r, c) for c in range(1, n + 1) for r in (0, 1))
    edges = {}
    for c in range(1, n + 1):
        edges[f'V{c}'] = ((0, c), (1, c))
    for c in range(1, n):
        edges[f'T{c}'] = ((0, c), (0, c + 1))
        edges[f'B{c}'] = ((1, c), (1, c + 1))
    return vertices, edges


def enumeration_by_tiles(n: int):
    ans = []
    def build(i, es):
        if i > n:
            ans.append(frozenset(es))
            return
        build(i + 1, es + [f'V{i}'])
        if i < n:
            build(i + 2, es + [f'T{i}', f'B{i}'])
    build(1, [])
    return set(ans)


def enumerate_perfect_matchings(vertices, edges):
    neighbors = {v: [] for v in vertices}
    for name, (u, v) in edges.items():
        neighbors[u].append((v, name))
        neighbors[v].append((u, name))
    ans = set()
    def run(remaining, selected):
        if not remaining:
            ans.add(frozenset(selected))
            return
        u = min(remaining)
        for v, e in neighbors[u]:
            if v in remaining:
                run(remaining - {u, v}, selected + (e,))
    run(frozenset(vertices), ())
    return ans


def dimensions(matchings, edges):
    concepts = tuple(sorted(matchings, key=lambda m: tuple(sorted(m))))
    q = tuple(sorted(edges))
    N = len(concepts)
    full = (1 << N) - 1
    masks = {e: sum(1 << i for i, m in enumerate(concepts) if e in m) for e in q}
    vc = 0
    for size in range(1, N.bit_length() + 1):
        exists = False
        for S in combinations(q, size):
            traces = {tuple(e in m for e in S) for m in concepts}
            if len(traces) == 1 << size:
                exists = True
                break
        if not exists:
            break
        vc = size
    @lru_cache(None)
    def ldim(mask):
        if mask.bit_count() < 2:
            return 0
        best = 0
        for e in q:
            yes = mask & masks[e]
            no = mask & (full ^ masks[e])
            if yes and no:
                best = max(best, 1 + min(ldim(yes), ldim(no)))
        return best
    return vc, ldim(full)


def verify_witness(matchings, certificate):
    concepts = [frozenset(m) for m in certificate['concepts_in_index_order']]
    assert set(concepts) == matchings
    queries = certificate['query_at_path']
    leaf_ids = certificate['leaf_index_at_path']
    assert len(queries) == 7 and len(leaf_ids) == 8
    assert set(queries) == {'', '0', '1', '00', '01', '10', '11'}
    assert set(leaf_ids) == {format(x, '03b') for x in range(8)}
    assert set(leaf_ids.values()) == set(range(1, 9))
    for path, idx in leaf_ids.items():
        concept = concepts[idx - 1]
        for j in range(3):
            e = queries[path[:j]]
            assert int(e in concept) == int(path[j]), (path, idx, e)
    return len(leaf_ids)


def chain_graph(s: int):
    vertices = []
    edges = {}
    for b in range(s):
        vs, es = graph_ladder(5)
        vertices.extend((b,) + v for v in vs)
        for name, (u, v) in es.items():
            edges[f'block{b+1}_{name}'] = ((b,) + u, (b,) + v)
    for b in range(s - 1):
        edges[f'bridge{b+1}'] = ((b, 0, 5), (b + 1, 0, 1))
    return tuple(vertices), edges


def graph_properties(vertices, edges):
    nbrs = {v: set() for v in vertices}
    for u, v in edges.values():
        nbrs[u].add(v)
        nbrs[v].add(u)
    assert max(map(len, nbrs.values())) <= 3
    color = {}
    for origin in vertices:
        if origin in color:
            continue
        color[origin] = 0
        frontier = [origin]
        while frontier:
            u = frontier.pop()
            for v in nbrs[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    frontier.append(v)
                else:
                    assert color[v] != color[u]
    assert len(color) == len(vertices)


def main():
    file = Path(__file__).with_name('certificate.json')
    cert = json.loads(file.read_text(encoding='utf8'))
    table = {}
    for n in range(1, 6):
        vertices, edges = graph_ladder(n)
        brute = enumerate_perfect_matchings(vertices, edges)
        tiled = enumeration_by_tiles(n)
        assert brute == tiled
        dims = dimensions(brute, edges)
        table[n] = (len(brute), *dims)
    expected = {1:(1,0,0),2:(2,1,1),3:(3,1,1),4:(5,2,2),5:(8,2,3)}
    assert table == expected, (table, expected)
    print('LADDER_EXACT_TABLE')
    for n in range(1, 6):
        print('n=%d matchings=%d VC=%d Ldim=%d' % ((n,) + table[n]))

    _, edges = graph_ladder(5)
    matchings = enumeration_by_tiles(5)
    frequency = {e: sum(e in m for m in matchings) for e in edges}
    assert frequency == cert['edge_frequencies'], frequency
    balanced = [e for e, count in frequency.items() if count == 4]
    assert balanced == ['V3']
    assert len({tuple(e in m for e in ('T1','T4')) for m in matchings}) == 4
    print('LADDER_5_UNIQUE_BALANCED_QUERY V3; PAIR T1 T4 SHATTERED')
    print('LADDER_5_COMPLETE_DEPTH_3_LEAVES', verify_witness(matchings, cert))

    for s in range(1, 4):
        vertices, edges = chain_graph(s)
        graph_properties(vertices, edges)
        matchings = enumerate_perfect_matchings(vertices, edges)
        assert len(matchings) == 8 ** s
        assert all(all(f'bridge{k}' not in m for k in range(1,s)) for m in matchings)
        projected = {tuple(frozenset(e.split('_',1)[1] for e in m if e.startswith(f'block{b+1}_'))
                           for b in range(s)) for m in matchings}
        base = enumeration_by_tiles(5)
        from itertools import product
        assert projected == set(product(base, repeat=s))
        print(f'CONNECTED_CHAIN s={s} vertices={len(vertices)} matchings={len(matchings)} bridges_unused=YES maximum_degree<=3 bipartite=YES')
    print('ALL_MATCHING_SHATTERING_CHECKS_PASS')

if __name__ == '__main__':
    main()
