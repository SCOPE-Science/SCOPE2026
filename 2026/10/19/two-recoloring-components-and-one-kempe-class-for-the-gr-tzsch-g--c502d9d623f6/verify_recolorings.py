#!/usr/bin/env python3
"""Exact, self-contained census of two reconfiguration rules on Mycielski(C5).

The finite proof uses exhaustive generation and reachability with no external modules.
All vertex labels and edge tests are specified explicitly below.
"""
from collections import Counter, deque
from itertools import permutations, product

N = 11
# Original pentagon: 0,...,4; shadows: 5,...,9; apex: 10.
EDGES = sorted({tuple(sorted((i, (i + 1) % 5))) for i in range(5)} |
               {tuple(sorted((5 + i, (i - 1) % 5))) for i in range(5)} |
               {tuple(sorted((5 + i, (i + 1) % 5))) for i in range(5)} |
               {(5 + i, 10) for i in range(5)})
assert len(EDGES) == 20 and len(set(EDGES)) == 20
NEIGHBORS = [set() for _ in range(N)]
for u, v in EDGES:
    NEIGHBORS[u].add(v)
    NEIGHBORS[v].add(u)
assert sorted(map(len, NEIGHBORS)) == [3]*5 + [4]*5 + [5]


def proper(z):
    return all(z[u] != z[v] for u, v in EDGES)


def backtracking(k):
    """Exhaustive coloring search with vertices in descending degree order."""
    order = sorted(range(N), key=lambda v: (-len(NEIGHBORS[v]), v))
    z = [-1] * N
    result = []
    def rec(j):
        if j == N:
            result.append(tuple(z))
            return
        v = order[j]
        disallowed = {z[w] for w in NEIGHBORS[v] if z[w] >= 0}
        for c in range(k):
            if c not in disallowed:
                z[v] = c
                rec(j + 1)
        z[v] = -1
    rec(0)
    return result


def layer_enumeration(k):
    """Independent exhaustive method: condition on pentagon and apex,
    then choose each shadow independently from its admissible palette."""
    for outer in product(range(k), repeat=5):
        if any(outer[i] == outer[(i + 1) % 5] for i in range(5)):
            continue
        for apex in range(k):
            palettes = [tuple(c for c in range(k)
                              if c != apex and c != outer[(i-1) % 5]
                              and c != outer[(i+1) % 5]) for i in range(5)]
            for shadows in product(*palettes):
                yield outer + shadows + (apex,)


def recolor_edges(states, idx):
    graph = [set() for _ in states]
    for i, z in enumerate(states):
        for v in range(N):
            used = {z[w] for w in NEIGHBORS[v]}
            for c in range(4):
                if c != z[v] and c not in used:
                    candidate = z[:v] + (c,) + z[v+1:]
                    graph[i].add(idx[candidate])
    return graph


def kempe_components(z, a, b):
    unseen = {v for v, c in enumerate(z) if c == a or c == b}
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        queue = [root]
        for v in queue:
            for w in NEIGHBORS[v]:
                if w in unseen:
                    unseen.remove(w)
                    queue.append(w)
        yield queue


def kempe_edges(states, idx):
    graph = [set() for _ in states]
    for i, z in enumerate(states):
        for a in range(4):
            for b in range(a + 1, 4):
                for chain in kempe_components(z, a, b):
                    zz = list(z)
                    for v in chain:
                        zz[v] = a + b - zz[v]
                    candidate = tuple(zz)
                    assert proper(candidate)
                    graph[i].add(idx[candidate])
    return graph


def graph_check(graph, states, kind):
    for i, ns in enumerate(graph):
        assert i not in ns
        for j in ns:
            assert i in graph[j]
            if kind == 'recolor':
                assert sum(a != b for a, b in zip(states[i], states[j])) == 1
            else:
                diff = [v for v in range(N) if states[i][v] != states[j][v]]
                assert diff
                pairs = {(states[i][v], states[j][v]) for v in diff}
                assert len(pairs) <= 2
                assert all(a != b for a, b in pairs)
                pair = set().union(*(set(t) for t in pairs))
                assert len(pair) == 2
                aa, bb = sorted(pair)
                assert any(set(diff) == set(chain) for chain in kempe_components(states[i], aa, bb))
    return sum(map(len, graph)) // 2


def components(graph):
    label = [-1] * len(graph)
    sizes = []
    for i in range(len(graph)):
        if label[i] != -1:
            continue
        current = len(sizes)
        queue = deque([i])
        label[i] = current
        total = 0
        while queue:
            u = queue.popleft()
            total += 1
            for v in graph[u]:
                if label[v] == -1:
                    label[v] = current
                    queue.append(v)
        sizes.append(total)
    # Independent connectivity cross-check: union-find over all graph edges.
    parent = list(range(len(graph)))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, ns in enumerate(graph):
        for j in ns:
            x, y = root(i), root(j)
            parent[x] = y
    assert sorted(Counter(root(i) for i in range(len(graph))).values()) == sorted(sizes)
    return label, sizes


def normalized(z):
    renaming = {}
    return tuple(renaming.setdefault(x, len(renaming)) for x in z)


def dihedral_transform(z, shift, reflection):
    # These are the ten graph automorphisms of the construction.
    ans = [0] * N
    for i in range(5):
        j = ((-i if reflection else i) + shift) % 5
        ans[j], ans[5 + j] = z[i], z[5 + i]
    ans[10] = z[10]
    return tuple(ans)


def orbits_under_symmetries(states):
    normalized_states = {normalized(z) for z in states}
    assert len(normalized_states) == 520
    unseen = set(normalized_states)
    orbits = []
    while unseen:
        z = min(unseen)
        orbit = {normalized(dihedral_transform(z, shift, reflection))
                 for shift in range(5) for reflection in (False, True)}
        assert orbit <= unseen
        unseen -= orbit
        orbits.append(orbit)
    assert Counter(map(len, orbits)) == {10: 48, 5: 8}
    # Every relabeling and graph symmetry is an automorphism of both reconfiguration graphs.
    for shift in range(5):
        for reflection in (False, True):
            vertex_map = [0]*N
            for i in range(5):
                j = ((-i if reflection else i) + shift) % 5
                vertex_map[i] = j
                vertex_map[5+i] = 5+j
            vertex_map[10] = 10
            assert {tuple(sorted((vertex_map[u], vertex_map[v]))) for u, v in EDGES} == set(EDGES)
    return orbits


def distances(graph, source):
    d = [-1] * len(graph)
    d[source] = 0
    q = deque([source])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                q.append(v)
    return d


def eccentricities_by_orbits(graph, states, idx, orbits, reachable):
    hist = Counter()
    for orbit in orbits:
        z = min(orbit)
        d = distances(graph, idx[z])
        assert len(d) - d.count(-1) == reachable
        hist[max(d)] += 24 * len(orbit)
    assert sum(hist.values()) == len(states)
    return hist


def main():
    assert not backtracking(3)
    assert not list(layer_enumeration(3))
    states = sorted(backtracking(4))
    states2 = list(layer_enumeration(4))
    assert len(states) == len(states2) == 12480
    assert len(set(states2)) == 12480 and set(states2) == set(states)
    assert all(proper(z) and set(z) == {0,1,2,3} for z in states)
    idx = {z:i for i,z in enumerate(states)}

    single = recolor_edges(states, idx)
    kempe = kempe_edges(states, idx)
    assert graph_check(single, states, 'recolor') == 45240
    assert graph_check(kempe, states, 'kempe') == 87120
    assert Counter(map(len, single)) == {5:480, 6:2640, 7:3840, 8:4320, 9:1200}
    assert Counter(map(len, kempe)) == {13:3600, 14:6000, 15:2640, 16:240}
    component_id, sizes = components(single)
    assert sorted(sizes) == [6240, 6240]
    assert components(kempe)[1] == [12480]
    crossing = sum(component_id[i] != component_id[j]
                   for i, ns in enumerate(kempe) for j in ns if i < j)
    assert crossing == 37440

    z = states[0]
    for pi in permutations(range(4)):
        parity = sum(pi[i] > pi[j] for i in range(4) for j in range(i+1, 4)) % 2
        image = tuple(pi[a] for a in z)
        assert (component_id[idx[image]] != component_id[idx[z]]) == bool(parity)
    # Connectivity and equivariance then extend the verified parity action to every coloring.

    orbits = orbits_under_symmetries(states)
    hist_single = eccentricities_by_orbits(single, states, idx, orbits, 6240)
    hist_kempe = eccentricities_by_orbits(kempe, states, idx, orbits, 12480)
    assert hist_single == {15:2160, 16:10200, 17:120}
    assert hist_kempe == {7:12480}

    # Direct two-colour connected-component witness that crosses the single-vertex split.
    before = (0,1,0,1,2,3,1,2,1,2,0)
    after = (1,0,1,0,2,3,0,2,0,2,1)
    assert before in idx and after in idx
    assert idx[after] in kempe[idx[before]]
    assert component_id[idx[before]] != component_id[idx[after]]

    print('graph: 11 vertices, 20 edges; chromatic number 4')
    print('proper labeled 4-colorings: 12480; partitions modulo S4: 520')
    print('single-vertex recoloring: vertices=12480 edges=45240 components=[6240, 6240]')
    print('single-vertex component radius=15 diameter=17 (both components)')
    print('single-vertex eccentricity multiplicities:', sorted(hist_single.items()))
    print('Kempe change: vertices=12480 edges=87120 components=[12480]')
    print('Kempe radius=diameter=7, all 12480 vertices eccentricity 7')
    print('Kempe edges across single-vertex components:', crossing)
    print('color permutation action on the two recoloring components: sign')
    print('symmetry orbits under D5 x S4:', len(orbits), dict(sorted(Counter(map(len,orbits)).items())))
    print('cross-component Kempe witness:', before, '=>', after)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
