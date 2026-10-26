#!/usr/bin/env python3
"""Independent finite enumeration through matchings. Only the Python standard library."""
import collections
import hashlib
import itertools
import json

N = 18
SHIFTS = (5, 7, -7, 7, -7, -5)
EDGES = sorted({tuple(sorted((i, (i + 1) % N))) for i in range(N)} |
               {tuple(sorted((i, (i + SHIFTS[i % 6]) % N))) for i in range(N)})
assert len(EDGES) == 27
EID = {e: j for j, e in enumerate(EDGES)}
INC = {v: [j for j, (a, b) in enumerate(EDGES) if v in (a, b)] for v in range(N)}
assert all(len(INC[v]) == 3 for v in range(N))
ALL = (1 << 27) - 1
ROOT = INC[0]


def matchings(unused):
    if not unused:
        yield 0
        return
    v = (unused & -unused).bit_length() - 1
    for e in INC[v]:
        a, b = EDGES[e]
        w = b if a == v else a
        if unused >> w & 1:
            for rest in matchings(unused & ~(1 << v) & ~(1 << w)):
                yield rest | (1 << e)


def canon(color_masks):
    colors = [-1] * 27
    for e in ROOT:
        for t, mask in enumerate(color_masks):
            if (mask >> e) & 1:
                home = t
                break
        for j in range(27):
            if (color_masks[home] >> j) & 1:
                colors[j] = ROOT.index(e)
    assert len(set(colors)) == 3 and all(x >= 0 for x in colors)
    return tuple(colors)


def pair_components(A, B):
    eids = [e for e in range(27) if ((A | B) >> e) & 1]
    neigh = {v: [] for v in range(18)}
    for j in eids:
        a, b = EDGES[j]
        neigh[a].append((b, j)); neigh[b].append((a, j))
    assert all(len(neigh[v]) == 2 for v in range(18))
    unseen = set(range(18)); result = []
    while unseen:
        stack = [min(unseen)]; nodes = set()
        while stack:
            v = stack.pop()
            if v in nodes: continue
            nodes.add(v)
            stack.extend(w for w, _ in neigh[v] if w not in nodes)
        unseen -= nodes
        cmask = 0
        for j in eids:
            a, b = EDGES[j]
            if a in nodes: cmask |= 1 << j
        result.append((len(nodes), cmask))
    return result


def main():
    mats = sorted(set(matchings((1 << 18) - 1)))
    assert len(mats) == 42
    matset = set(mats)
    factors = set()
    for a in mats:
        for b in mats:
            if a & b: continue
            c = ALL ^ (a | b)
            if c in matset:
                factors.add(canon((a, b, c)))
    configs = sorted(factors)
    assert len(configs) == 20
    lookup = {z: i for i, z in enumerate(configs)}
    adj = [set() for _ in configs]
    signatures = []
    for i, config in enumerate(configs):
        cmasks = [sum(1 << e for e, q in enumerate(config) if q == t) for t in range(3)]
        profile = []
        for a, b in itertools.combinations(range(3), 2):
            components = pair_components(cmasks[a], cmasks[b])
            profile.append(tuple(sorted(s for s, _ in components)))
            for _, mask in components:
                newA = cmasks[a] ^ mask
                newB = cmasks[b] ^ mask
                updated = list(cmasks); updated[a] = newA; updated[b] = newB
                moved = canon(updated)
                if moved != config:
                    assert moved in lookup
                    adj[i].add(lookup[moved])
        signatures.append(tuple(sorted(profile)))
    assert all(i in adj[j] for i, neigh in enumerate(adj) for j in neigh)
    components = []
    unseen = set(range(len(configs)))
    while unseen:
        root = min(unseen); q = [root]; found = {root}
        while q:
            for w in adj[q.pop()]:
                if w not in found:
                    found.add(w); q.append(w)
        unseen -= found
        components.append(sorted(found))
    assert sorted(map(len, components)) == [10, 10]
    for block in components:
        centers = [v for v in block if len(adj[v]) == 9]
        assert len(centers) == 1
        leaves = [v for v in block if v not in centers]
        assert all(len(adj[v]) == 3 for v in leaves)
        leftover = set(leaves); clusters = []
        while leftover:
            v = min(leftover)
            triple = {v} | (adj[v] & set(leaves))
            assert len(triple) == 3
            assert all((adj[w] & set(leaves)) == (triple - {w}) for w in triple)
            clusters.append(sorted(triple)); leftover -= triple
        assert len(clusters) == 3
        assert all(c in adj[v] for v in leaves for c in centers)
    center_sig = ((6, 6, 6),) * 3
    leaf_sig = ((6, 6, 6), (18,), (18,))
    assert sum(s == center_sig for s in signatures) == 2
    assert sum(s == leaf_sig for s in signatures) == 18
    edges = sorted((i, j) for i in range(20) for j in adj[i] if i < j)
    assert len(edges) == 36
    serialized = json.dumps({'colorings': configs, 'edges': edges}, separators=(',', ':'), sort_keys=True)
    report = {'method': 'perfect_matchings_and_even_two_factors', 'vertices': 18,
        'edges': 27, 'perfect_matchings': len(mats), 'one_factorizations': len(configs),
        'Kempe_edges': len(edges), 'components': sorted(map(len, components)),
        'degree_histogram': dict(sorted(collections.Counter(map(len, adj)).items())),
        'two_factor_profile_histogram': {'three_hexagon_pairs_3': 2, 'three_hexagon_pairs_1': 18},
        'full_graph_sha256': hashlib.sha256(serialized.encode('utf-8')).hexdigest(),
        'conclusion': '2 copies of K_1 join (3 K_3)'}
    print(json.dumps(report, sort_keys=True, indent=2))
    if __name__ == '__main__' and __import__('sys').argv[1:] == ['--certificate']:
        obj={'graph_edge_list':EDGES, 'canonical_color_vectors': [''.join(map(str, c)) for c in configs],
            'adjacency': [sorted(row) for row in adj], 'pair_cycle_profiles': [list(map(list,s)) for s in signatures],
            'components': components, 'graph_sha256': report['full_graph_sha256']}
        with open('classification_certificate.json', 'w', encoding='utf-8') as out:
            json.dump(obj,out,sort_keys=True,indent=2)
            out.write('\n')

if __name__ == '__main__': main()
