#!/usr/bin/env python3
import bisect
import itertools
import json
from collections import Counter

N = 5
D = 3
V = list(itertools.permutations(range(1, N + 1)))
INDEX = {p: i for i, p in enumerate(V)}


def lcs_len(a, b):
    pos = {x: i for i, x in enumerate(b)}
    tails = []
    for x in a:
        y = pos[x]
        k = bisect.bisect_left(tails, y)
        if k == len(tails):
            tails.append(y)
        else:
            tails[k] = y
    return len(tails)


def ulam(a, b):
    return N - lcs_len(a, b)


def build_graph():
    adj = [0] * len(V)
    edges = 0
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            if ulam(V[i], V[j]) >= D:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
                edges += 1
    return adj, edges


def maximal_cliques(adj):
    out = []
    nodes = 0
    def rec(R, P, X):
        nonlocal nodes
        nodes += 1
        if not P and not X:
            out.append(tuple(R))
            return
        U = P | X
        if U:
            z = U
            pivot = None
            score = -1
            while z:
                bit = z & -z
                u = bit.bit_length() - 1
                z -= bit
                s = (P & adj[u]).bit_count()
                if s > score:
                    score = s
                    pivot = u
            Q = P & ~adj[pivot]
        else:
            Q = P
        while Q:
            bit = Q & -Q
            v = bit.bit_length() - 1
            Q -= bit
            rec(R + [v], P & adj[v], X & adj[v])
            P -= bit
            X |= bit
    rec([], (1 << len(V)) - 1, 0)
    return out, nodes


def group_maps():
    maps = []
    for alpha in V:
        amap = {i + 1: alpha[i] for i in range(N)}
        for rev in (False, True):
            m = []
            for p in V:
                q0 = p[::-1] if rev else p
                q = tuple(amap[x] for x in q0)
                m.append(INDEX[q])
            maps.append(tuple(m))
    assert len(set(maps)) == 240
    return maps


def code_key(C):
    return tuple(''.join(map(str, V[i])) for i in sorted(C))


def main():
    adj, edges = build_graph()
    degrees = Counter(a.bit_count() for a in adj)
    assert degrees == Counter({42: 120}), degrees
    assert edges == 2520, edges

    cliques, nodes = maximal_cliques(adj)
    hist = Counter(map(len, cliques))
    assert hist == Counter({4: 4020, 3: 120, 2: 60}), hist
    maximum = max(hist)
    maxima = {frozenset(C) for C in cliques if len(C) == maximum}
    assert len(maxima) == 4020

    pair_profiles = Counter()
    for C in maxima:
        ds = Counter(ulam(V[i], V[j]) for i, j in itertools.combinations(C, 2))
        pair_profiles[tuple(sorted(ds.items()))] += 1
    assert pair_profiles == Counter({((3, 6),): 4020}), pair_profiles

    maps = group_maps()
    # Check every declared group element preserves every pairwise Ulam distance.
    for m in maps:
        for i in range(len(V)):
            for j in range(i + 1, len(V)):
                assert ulam(V[i], V[j]) == ulam(V[m[i]], V[m[j]])

    unseen = set(maxima)
    orbits = []
    reps = []
    while unseen:
        seed = min(unseen, key=code_key)
        orbit = {frozenset(m[i] for i in seed) for m in maps}
        assert orbit <= maxima
        unseen -= orbit
        rep = min(orbit, key=code_key)
        size = len(orbit)
        orbits.append(size)
        reps.append({
            'orbit_size': size,
            'stabilizer_order_in_240_group': 240 // size,
            'representative': list(code_key(rep)),
        })
    orbit_sizes = Counter(orbits)
    assert orbit_sizes == Counter({240: 12, 120: 7, 60: 5}), orbit_sizes
    assert len(orbits) == 24

    reps.sort(key=lambda r: (r['orbit_size'], r['representative']))
    with open('orbit_representatives.json', 'w', encoding='utf-8') as f:
        json.dump({
            'n': N,
            'minimum_ulam_distance': D,
            'maximum_code_size': maximum,
            'labeled_maximum_codes': len(maxima),
            'isometry_subgroup_order': 240,
            'orbit_size_distribution': {'60': 5, '120': 7, '240': 12},
            'representatives': reps,
        }, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write('\n')

    print(
        'VERIFY_OK '
        f'vertices={len(V)} edges={edges} degree=42 '
        f'maximal_cliques=4200 histogram=2:60,3:120,4:4020 '
        f'maximum={maximum} labeled_maxima={len(maxima)} '
        'equidistant_maxima=4020 pair_distance=3 '
        'group_size=240 orbits=24 orbit_sizes=60x5,120x7,240x12 '
        f'bron_kerbosch_nodes={nodes}'
    )


if __name__ == '__main__':
    main()
