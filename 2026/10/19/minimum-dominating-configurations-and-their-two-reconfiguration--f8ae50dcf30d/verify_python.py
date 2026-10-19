#!/usr/bin/env python3
"""Exhaustive verifier for minimum domination reconfiguration in J(7,3).
Python 3, standard library only. Usage: python verify_python.py output.tsv
The output uses vertex indices 00..34 in lexicographic 3-subset order.
"""
import collections
import itertools
import pathlib
import sys

N = 7
TRIPLES = tuple(itertools.combinations(range(N), 3))
WHERE = {x: i for i, x in enumerate(TRIPLES)}
FULL = (1 << len(TRIPLES)) - 1
NEIGHBORHOOD = tuple(sum(1 << j for j, u in enumerate(TRIPLES)
                         if len(set(t).intersection(u)) >= 2) for t in TRIPLES)


def all_optima():
    # All C(35,4)=52,360 four-element vertex subsets, without pruning.
    out = []
    for combo in itertools.combinations(range(len(TRIPLES)), 4):
        covered = 0
        for vertex in combo:
            covered |= NEIGHBORHOOD[vertex]
        if covered == FULL:
            out.append(combo)
    return out


def geometric_family():
    # A four-point core A, complement B of size three; two canonical types.
    owner, types = {}, {}
    for B in TRIPLES:
        A = tuple(v for v in range(N) if v not in B)
        three_A = tuple(itertools.combinations(A, 3))
        for family in itertools.combinations(three_A, 3):
            config = tuple(sorted(WHERE[x] for x in ((B,) + family)))
            assert config not in owner
            owner[config], types[config] = B, 'I'
        for P in itertools.combinations(A, 2):
            Q = tuple(v for v in A if v not in P)
            for b in B:
                blocks = [B, tuple(sorted(P + (Q[0],))),
                          tuple(sorted(P + (Q[1],))), tuple(sorted(Q + (b,)))]
                config = tuple(sorted(WHERE[x] for x in blocks))
                assert config not in owner
                owner[config], types[config] = B, 'II'
    assert len(owner) == 770
    return owner, types


def graph_edges(optima):
    index = {x: i for i, x in enumerate(optima)}
    jump, slide = [], []
    for i, four in enumerate(optima):
        fset = set(four)
        for old in four:
            other = fset - {old}
            for new in range(35):
                if new in fset:
                    continue
                candidate = tuple(sorted(other | {new}))
                j = index.get(candidate)
                if j is None or j <= i:
                    continue
                jump.append((i, j))
                if len(set(TRIPLES[old]) & set(TRIPLES[new])) == 2:
                    slide.append((i, j))
    return sorted(slide), sorted(jump)


def adjacency(k, edges):
    neighbors = [set() for _ in range(k)]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    return neighbors


def connected_components(adj):
    remains = set(range(len(adj)))
    result = []
    while remains:
        start = min(remains)
        remains.remove(start)
        visited = {start}
        queue = [start]
        for vertex in queue:
            for nxt in adj[vertex]:
                if nxt in remains:
                    remains.remove(nxt)
                    visited.add(nxt)
                    queue.append(nxt)
        result.append(frozenset(visited))
    return result


def eccentricities(adj):
    output = []
    for root in range(len(adj)):
        dist = {root: 0}
        queue = [root]
        for cur in queue:
            for nxt in adj[cur]:
                if nxt not in dist:
                    dist[nxt] = dist[cur] + 1
                    queue.append(nxt)
        output.append((len(dist), max(dist.values())))
    return output


def main(filename):
    optima = all_optima()
    assert len(optima) == 770
    owner, kinds = geometric_family()
    assert set(owner) == set(optima), 'geometric classification is not exhaustive'
    assert collections.Counter(kinds.values()) == {'I': 140, 'II': 630}
    # Orbit certificate: two generators under all 7! relabelings.
    perms = list(itertools.permutations(range(N)))
    perm_trip = [tuple(WHERE[tuple(sorted(p[v] for v in t))] for t in TRIPLES)
                 for p in perms]
    seen = set()
    orbit_sizes = []
    for s in optima:
        if s in seen:
            continue
        orbit = {tuple(sorted(pt[v] for v in s)) for pt in perm_trip}
        assert orbit <= set(optima)
        orbit_sizes.append(len(orbit))
        seen |= orbit
    assert sorted(orbit_sizes) == [140, 630]
    slide, jump = graph_edges(optima)
    assert len(slide) == 2100 and len(jump) == 2730
    Tadj, Jadj = adjacency(len(optima), slide), adjacency(len(optima), jump)
    Ts = connected_components(Tadj)
    assert len(Ts) == 35 and all(len(c) == 22 for c in Ts)
    assert len(connected_components(Jadj)) == 1
    owners = [owner[s] for s in optima]
    assert all(owners[a] == owners[b] for a, b in slide)
    assert len({frozenset(owners[v] for v in component) for component in Ts}) == 35
    cross = collections.Counter()
    for a, b in jump:
        if owners[a] != owners[b]:
            assert set(owners[a]).isdisjoint(owners[b])
            cross[frozenset((owners[a], owners[b]))] += 1
    assert len(cross) == 70 and set(cross.values()) == {9}
    assert sum(cross.values()) == 630
    assert all(sum(b in item for item in cross) == 4 for b in TRIPLES)
    assert collections.Counter(map(len, Tadj)) == {12: 140, 4: 630}
    assert collections.Counter(map(len, Jadj)) == {12: 140, 6: 630}
    # Verify the component's K4 core and six K5 edge thickenings.
    for comp in Ts:
        core = {v for v in comp if kinds[optima[v]] == 'I'}
        rim = set(comp) - core
        assert len(core) == 4 and len(rim) == 18
        assert all(len(Tadj[x] & core) == 3 for x in core)
        by_pair = collections.defaultdict(list)
        for x in rim:
            pair = frozenset(Tadj[x] & core)
            assert len(pair) == 2
            by_pair[pair].append(x)
        assert len(by_pair) == 6 and all(len(group) == 3 for group in by_pair.values())
        for group in by_pair.values():
            assert all(set(group) - {x} == Tadj[x] & set(group) for x in group)
            assert all(len(Tadj[x]) == 4 for x in group)
    T_ecc = eccentricities(Tadj)
    J_ecc = eccentricities(Jadj)
    assert collections.Counter(e for _, e in T_ecc) == {2: 140, 3: 630}
    assert all(n == 22 for n, _ in T_ecc)
    assert all(n == 770 and e == 7 for n, e in J_ecc)
    lines = []
    for s in optima:
        lines.append('D ' + ' '.join(f'{v:02d}' for v in s) + '\n')
    for a, b in slide:
        lines.append(f'S {a:03d} {b:03d}\n')
    for a, b in jump:
        lines.append(f'J {a:03d} {b:03d}\n')
    pathlib.Path(filename).write_bytes(''.join(lines).encode('ascii'))
    print('OPTIMA=770; ORBITS=140,630; TYPE_COUNTS=140,630')
    print('SLIDE_EDGES=2100; SLIDE_COMPONENTS=35x22; SLIDE_RADIUS_DIAMETER=2,3')
    print('JUMP_EDGES=2730; JUMP_COMPONENTS=1x770; JUMP_RADIUS_DIAMETER=7,7')
    print('CROSS_JUMP_EDGES=630; DISJOINT_TRIPLE_QUOTIENT=35v,70e,9peredge')
    print('CERTIFICATE_LINES=' + str(len(lines)))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python verify_python.py output.tsv')
    main(sys.argv[1])
