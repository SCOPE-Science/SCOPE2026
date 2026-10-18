#!/usr/bin/env python3
"""Exhaustive certificate for the 2 by 3 by 4 domino-flip graph.

Uses only the Python standard library. State enumeration, independent
layer-transfer counting, and two independently phrased flip tests.
"""
from collections import Counter, deque
from itertools import combinations, product

SIZE = (2, 3, 4)
CELLS = tuple(product(*(range(n) for n in SIZE)))
CELL_ID = {v: i for i, v in enumerate(CELLS)}
FULL = (1 << len(CELLS)) - 1
EDGES = tuple(sorted(tuple(sorted((i, CELL_ID[w])))
                     for i, v in enumerate(CELLS)
                     for axis in range(3)
                     if (w := tuple(v[j] + (j == axis) for j in range(3)))
                     in CELL_ID))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}
INCIDENT = [tuple(i for i, (a, b) in enumerate(EDGES) if v in (a, b))
            for v in range(len(CELLS))]


def enumerate_matchings():
    """First-uncovered-cell recursion: disjoint and exhaustive branches."""
    result = []

    def rec(occupied, selected):
        if occupied == FULL:
            result.append(selected)
            return
        first = next(i for i in range(len(CELLS)) if not (occupied >> i) & 1)
        for e in INCIDENT[first]:
            a, b = EDGES[e]
            other = a ^ b ^ first
            if not (occupied >> other) & 1:
                rec(occupied | (1 << first) | (1 << other),
                    selected | (1 << e))
    rec(0, 0)
    assert len(set(result)) == len(result)
    return result


def transfer_count():
    """Independent width-six transfer across four successive 2x3 floors."""
    floor = tuple(product(range(2), range(3)))
    coord = {v: i for i, v in enumerate(floor)}
    within = [[] for _ in floor]
    for v, (x, y) in enumerate(floor):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (x + dx, y + dy) in coord:
                within[v].append(coord[(x + dx, y + dy)])
    full = (1 << len(floor)) - 1

    def transitions(incoming, allow_exit):
        ways = Counter()

        def fill(occupied, outgoing):
            if occupied == full:
                ways[outgoing] += 1
                return
            first = next(i for i in range(len(floor)) if not (occupied >> i) & 1)
            for v in within[first]:
                if not (occupied >> v) & 1:
                    fill(occupied | (1 << first) | (1 << v), outgoing)
            if allow_exit:
                fill(occupied | (1 << first), outgoing | (1 << first))
        fill(incoming, 0)
        return ways

    values = {0: 1}
    for layer in range(4):
        nxt = Counter()
        for incoming, count in values.items():
            for outgoing, multiplicity in transitions(incoming, layer != 3).items():
                nxt[outgoing] += count * multiplicity
        values = nxt
    return values.get(0, 0)


def squares():
    pairs = []
    for v in CELLS:
        for a, b in combinations(range(3), 2):
            if v[a] + 1 >= SIZE[a] or v[b] + 1 >= SIZE[b]:
                continue
            u = list(v); u[a] += 1
            w = list(v); w[b] += 1
            z = list(u); z[b] += 1
            i, j, k, l = (CELL_ID[t] for t in (v, tuple(u), tuple(w), tuple(z)))
            e0 = ((1 << EDGE_ID[tuple(sorted((i, j)))]) |
                  (1 << EDGE_ID[tuple(sorted((k, l)))]))
            e1 = ((1 << EDGE_ID[tuple(sorted((i, k)))]) |
                  (1 << EDGE_ID[tuple(sorted((j, l)))]))
            pairs.append((e0, e1))
    return pairs


def flip_graph(matchings):
    lookup = {m: i for i, m in enumerate(matchings)}
    adj = [set() for _ in matchings]
    sq = squares()
    for i, m in enumerate(matchings):
        for a, b in sq:
            if (m & a) == a:
                adj[i].add(lookup[m ^ a ^ b])
            elif (m & b) == b:
                adj[i].add(lookup[m ^ a ^ b])
    actual = {(i, j) for i in range(len(adj)) for j in adj[i] if i < j}
    for i in range(len(adj)):
        assert i not in adj[i]
        assert all(i in adj[j] for j in adj[i])

    # Independent characterization: symmetric difference is a four-edge cycle.
    # In an ordinary rectangular grid every graph-theoretic 4-cycle is a unit square.
    other = {(i, j) for i, x in enumerate(matchings)
             for j in range(i + 1, len(matchings))
             if (x ^ matchings[j]).bit_count() == 4}
    assert actual == other
    return adj


def components(adj):
    left = set(range(len(adj)))
    result = []
    while left:
        s = min(left)
        left.remove(s)
        comp = [s]
        for u in comp:
            for v in adj[u]:
                if v in left:
                    left.remove(v)
                    comp.append(v)
        result.append(comp)
    return sorted(result, key=lambda c: (-len(c), min(c)))


def ecc_profile(adj, component):
    histogram = Counter()
    distance_histogram = Counter()
    diameter_example = None
    for source in component:
        dist = {source: 0}
        q = deque([source])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    q.append(w)
        assert len(dist) == len(component)
        ecc = max(dist.values())
        histogram[ecc] += 1
        for dest, d in dist.items():
            if source < dest:
                distance_histogram[d] += 1
        if ecc == 16 and diameter_example is None:
            diameter_example = (source, next(v for v, d in dist.items() if d == 16))
    return histogram, distance_histogram, diameter_example


def reflections_are_transitive(matchings, components):
    """Show the four small components comprise a single box-isometry orbit."""
    lookup = {m: i for i, m in enumerate(matchings)}
    owner = {u: k for k, comp in enumerate(components) for u in comp}
    seen = set()
    for axes in product((0, 1), repeat=3):
        def move(v):
            return tuple(SIZE[k] - 1 - v[k] if axes[k] else v[k] for k in range(3))
        perm = [EDGE_ID[tuple(sorted((CELL_ID[move(CELLS[a])],
                                      CELL_ID[move(CELLS[b])])))]
                for a, b in EDGES]
        representative = matchings[components[1][0]]
        transformed = sum(1 << perm[i] for i in range(len(EDGES))
                          if (representative >> i) & 1)
        seen.add(owner[lookup[transformed]])
    assert seen == {1, 2, 3, 4}
    return len(seen)


def main():
    print('box dimensions:', SIZE)
    print('cells, allowed dimers, elementary squares:',
          len(CELLS), len(EDGES), len(squares()))
    states = enumerate_matchings()
    via_transfer = transfer_count()
    assert len(states) == via_transfer == 1845
    adj = flip_graph(states)
    comps = components(adj)
    sizes = [len(c) for c in comps]
    assert sizes == [1825, 5, 5, 5, 5]
    edge_count = sum(len(a) for a in adj) // 2
    assert edge_count == 6949
    assert min(len(a) for a in adj) == 1
    for comp in comps[1:]:
        assert Counter(len(adj[u]) for u in comp) == {1: 2, 2: 3}
        assert sum(len(adj[u]) for u in comp) == 8
    assert reflections_are_transitive(states, comps) == 4
    eps, dhist, witness = ecc_profile(adj, comps[0])
    assert eps == {10: 100, 11: 1041, 12: 473, 13: 163,
                   14: 32, 15: 10, 16: 6}
    assert len(comps[0]) * (len(comps[0]) - 1) // 2 == sum(dhist.values())
    assert dhist == {1: 6933, 2: 28954, 3: 82937, 4: 175354,
                     5: 281394, 6: 345558, 7: 324438, 8: 231738,
                     9: 124562, 10: 48770, 11: 12096, 12: 1325,
                     13: 278, 14: 47, 15: 12, 16: 4}
    print('matchings (recursion and independent transfer):', len(states), via_transfer)
    print('single-square-flip edges (two independent tests):', edge_count)
    print('component sizes:', sizes)
    print('exceptional components: four P5, one reflection orbit')
    print('minimum vertex degree:', min(map(len, adj)))
    print('giant component radius, diameter:', min(eps), max(eps))
    print('giant component eccentricity counts:', dict(sorted(eps.items())))
    print('giant component unordered distance histogram:', dict(sorted(dhist.items())))
    print('diameter witness matching indices:', witness)
    print('verification: PASS')


if __name__ == '__main__':
    main()
