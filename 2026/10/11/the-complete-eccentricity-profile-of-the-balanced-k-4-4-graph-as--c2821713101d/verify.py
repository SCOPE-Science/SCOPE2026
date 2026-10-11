#!/usr/bin/env python3
"""Exhaustive integer certificate for the skeleton of Asso(K_{4,4}).

Usage: python verify.py --emit  (writes orbit_certificate.json alongside script)
       python verify.py         (checks every byte-independent scientific assertion)
Requires standard Python 3 library only. Source definitions are restated in RESULT.md.
"""
import json
import sys
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product, permutations
from math import factorial
from pathlib import Path

N_A = 4
N_B = 4
N = N_A + N_B
FULL = (1 << N) - 1
A = tuple(range(N_A))
B = tuple(range(N_A, N))


def components(mask):
    """Connected components of the induced subgraph K_{4,4}[mask]."""
    rem = mask
    found = []
    while rem:
        seed = rem & -rem
        comp, frontier = seed, seed
        while frontier:
            vbit = frontier & -frontier
            frontier -= vbit
            vertex = vbit.bit_length() - 1
            neighbors = (sum(1 << v for v in B) if vertex < N_A
                         else sum(1 << v for v in A))
            added = neighbors & mask & ~comp
            comp |= added
            frontier |= added
        found.append(comp)
        rem &= ~comp
    return tuple(found)


@lru_cache(maxsize=None)
def generic_search_tubings(mask):
    """All maximal tubing bit-mask tuples from all search trees on G[mask].

    Root decomposition: choose r, then one search tree in every component of G[mask]-r.
    A nonempty connected search-tree subtree contributes one tube; tuples are sorted.
    """
    if mask == 0:
        return ((),)
    assert len(components(mask)) == 1
    output = []
    for r in range(N):
        if not mask & (1 << r):
            continue
        fragments = [generic_search_tubings(c) for c in components(mask & ~(1 << r))]
        for choice in product(*fragments):
            output.append(tuple(sorted((mask,) + tuple(t for fragment in choice for t in fragment))))
    assert len(output) == len(set(output))
    return tuple(output)


def words():
    """Every A/B spine pattern ending on the first exhaustion of one side."""
    result = []
    def rec(word, a, b):
        if a == N_A or b == N_B:
            result.append(word)
        else:
            rec(word + 'A', a + 1, b)
            rec(word + 'B', a, b + 1)
    rec('', 0, 0)
    return sorted(result)


def tube_word(word, labeled_vertices):
    remaining = FULL
    tubes = []
    for v in labeled_vertices:
        tubes.append(remaining)
        remaining ^= (1 << v)
    assert len(labeled_vertices) == len(word)
    while remaining:
        bit = remaining & -remaining
        tubes.append(bit)
        remaining -= bit
    assert len(tubes) == N
    return tuple(sorted(tubes))


def representative(word):
    ia = ib = 0
    labels = []
    for side in word:
        if side == 'A':
            labels.append(A[ia]); ia += 1
        else:
            labels.append(B[ib]); ib += 1
    return tube_word(word, labels)


def orbit_size(word):
    na = word.count('A')
    nb = word.count('B')
    return (factorial(N_A) // factorial(N_A - na)
            * factorial(N_B) // factorial(N_B - nb))


def independent_broom_set():
    """Direct special-case generation, independent of the graph-component recursion."""
    out = set()
    for word in words():
        na, nb = word.count('A'), word.count('B')
        for aa in permutations(A, na):
            for bb in permutations(B, nb):
                ia = ib = 0
                labels = []
                for side in word:
                    if side == 'A':
                        labels.append(aa[ia]); ia += 1
                    else:
                        labels.append(bb[ib]); ib += 1
                key = tube_word(word, labels)
                assert key not in out
                out.add(key)
    return out


def skeleton(tubings):
    """Adjacent iff maximal tubings differ in exactly one (proper) tube."""
    by_shared = defaultdict(list)
    for i, tube_tuple in enumerate(tubings):
        assert len(tube_tuple) == N and FULL in tube_tuple
        for j in range(N):
            by_shared[tube_tuple[:j] + tube_tuple[j + 1:]].append(i)
    adj = [set() for _ in tubings]
    for shared, completions in by_shared.items():
        if FULL not in shared:
            # Deleting the mandatory whole-graph tube has only this completion.
            assert len(completions) == 1
        else:
            # Each 1-dimensional face of a simple polytope has two vertices.
            assert len(completions) == 2, (shared, completions)
            i, j = completions
            assert i != j
            adj[i].add(j)
            adj[j].add(i)
    assert all(len(row) == N - 1 for row in adj)
    for i, row in enumerate(adj):
        for j in row:
            assert i in adj[j]
            assert len(set(tubings[i]) ^ set(tubings[j])) == 2
    return tuple(tuple(sorted(row)) for row in adj)


def distances(graph, root):
    dist = [-1] * len(graph)
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    assert -1 not in dist
    return dist


def calculate():
    all_keys = tuple(generic_search_tubings(FULL))
    assert len(all_keys) == 29616
    assert set(all_keys) == independent_broom_set()
    index = {t: i for i, t in enumerate(all_keys)}
    graph = skeleton(all_keys)
    assert sum(map(len, graph)) // 2 == 103656
    pats = words()
    assert len(pats) == 70
    assert sum(orbit_size(p) for p in pats) == len(all_keys)
    profile = Counter()
    table = []
    for word in pats:
        key = representative(word)
        dist = distances(graph, index[key])
        far = max(range(len(all_keys)), key=lambda i: dist[i])
        ecc = dist[far]
        assert ecc == 15 + len(word), (word, ecc)
        size = orbit_size(word)
        profile[ecc] += size
        table.append({
            'spine_pattern': word,
            'orbit_size': size,
            'representative_tubes': list(key),
            'eccentricity': ecc,
            'eccentricity_formula': '15 + spine_pattern_length',
            'farthest_tubes': list(all_keys[far]),
        })
    assert dict(sorted(profile.items())) == {19: 48, 20: 768, 21: 5760, 22: 23040}
    assert max(profile) == 22
    assert len(table) == 70
    return {
        'object': '1-skeleton of the graph associahedron of the complete bipartite graph K_{4,4}',
        'vertex_partition': {'A': [0, 1, 2, 3], 'B': [4, 5, 6, 7]},
        'bitmask_definition': 'vertex i represents bit 2**i; a tube is an induced connected nonempty subset',
        'vertices': 29616,
        'edges': 103656,
        'regular_degree': 7,
        'spine_pattern_orbits': 70,
        'eccentricity_multiplicities': {'19': 48, '20': 768, '21': 5760, '22': 23040},
        'diameter': 22,
        'eccentricity_formula': '15 + length of the canonical colored broom spine',
        'orbit_table': table,
    }


def main():
    content = calculate()
    path = Path(__file__).with_name('orbit_certificate.json')
    if len(sys.argv) == 2 and sys.argv[1] == '--emit':
        path.write_text(json.dumps(content, indent=2, sort_keys=True) + '\n', encoding='utf-8')
        print('EMITTED orbit_certificate.json')
    else:
        assert sys.argv == [sys.argv[0]]
        assert path.is_file()
        actual = json.loads(path.read_text(encoding='utf-8'))
        assert actual == content, 'Orbit-by-orbit certificate does not match exhaustive recomputation'
        print('VERIFY_OK K4,4 vertices=29616 edges=103656 degree=7 orbits=70 diameter=22')
        print('VERIFY_OK ecc=19:48,20:768,21:5760,22:23040 generic_vs_broom=yes certificate_replayed=yes')

if __name__ == '__main__':
    main()
