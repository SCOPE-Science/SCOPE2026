#!/usr/bin/env python3
"""Exhaustive functional-digraph majority census on two 16-vertex graphs.
Standard library only; a state is a 16-bit integer, vertex (i,j) is 4*i+j.
"""
from collections import Counter, defaultdict
import json


def graph(kind):
    verts = [(i, j) for i in range(4) for j in range(4)]
    masks = []
    for i, j in verts:
        mask = 0
        for a, b in verts:
            rook = (i == a) != (j == b)
            u, v = ((a-i) % 4, (b-j) % 4)
            shr = (u, v) in {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
            if rook if kind == 'rook' else shr:
                mask |= 1 << (4*a+b)
        masks.append(mask)
    return masks


def check_graph(masks):
    assert len(masks) == 16
    for i in range(16):
        assert masks[i].bit_count() == 6
        assert not (masks[i] & (1 << i))
        for j in range(16):
            assert bool(masks[i] & (1 << j)) == bool(masks[j] & (1 << i))
            if i != j:
                assert (masks[i] & masks[j]).bit_count() == 2
    clique4 = 0
    for a in range(16):
        for b in range(a+1,16):
            for c in range(b+1,16):
                for d in range(c+1,16):
                    vs = [a,b,c,d]
                    if all(masks[u] & (1 << v) for k,u in enumerate(vs) for v in vs[k+1:]):
                        clique4 += 1
    return clique4


def census(kind):
    masks = graph(kind)
    clique4 = check_graph(masks)
    def update(x):
        out = 0
        for i, mask in enumerate(masks):
            neighbors_on = (x & mask).bit_count()
            if neighbors_on > 3 or (neighbors_on == 3 and (x & (1 << i))):
                out |= 1 << i
        return out
    nextstate = [update(x) for x in range(65536)]
    # Independent, full-state check of asserted global iterate identity.
    max_claim = 3 if kind == 'rook' else 5
    for x in range(65536):
        y = x
        for _ in range(max_claim):
            y = nextstate[y]
        assert y == nextstate[nextstate[y]], (kind, x)
    dist = [-1] * 65536
    period = [0] * 65536
    rep = [-1] * 65536
    cycles = {}
    for root in range(65536):
        if dist[root] != -1:
            continue
        seen = {}
        path = []
        v = root
        while dist[v] < 0 and v not in seen:
            seen[v] = len(path)
            path.append(v)
            v = nextstate[v]
        if v in seen:
            start = seen[v]
            orbit = path[start:]
            assert len(orbit) in (1, 2)
            canonical = min(orbit)
            assert canonical not in cycles
            cycles[canonical] = len(orbit)
            for w in orbit:
                dist[w] = 0
                period[w] = len(orbit)
                rep[w] = canonical
            path = path[:start]
        for w in reversed(path):
            z = nextstate[w]
            assert dist[z] >= 0
            dist[w] = dist[z] + 1
            period[w] = period[z]
            rep[w] = rep[z]
    assert all(k >= 0 for k in dist)
    basins = Counter(rep)
    fixed_orbits = sum(p == 1 for p in cycles.values())
    two_orbits = sum(p == 2 for p in cycles.values())
    depth_hist = Counter(dist)
    byperiod = {str(p): {str(t): sum(dist[x] == t and period[x] == p for x in range(65536))
                         for t in range(max(dist)+1)} for p in (1,2)}
    basin_hist = {str(p): dict(sorted(Counter(basins[r] for r,q in cycles.items() if q == p).items())) for p in (1,2)}
    maxd = max(dist)
    exemplar = min(x for x in range(65536) if dist[x] == maxd)
    orbitpath = [exemplar]
    for _ in range(max(dist)+2):
        orbitpath.append(nextstate[orbitpath[-1]])
    assert max(dist) == max_claim
    assert basins[0] == basins[65535]
    out = {
        'graph': kind, 'states': 65536, 'srg_parameters': [16,6,2,2],
        'four_cliques': clique4,
        'fixed_orbits': fixed_orbits, 'primitive_two_cycle_orbits': two_orbits,
        'periodic_states': fixed_orbits+2*two_orbits,
        'max_first_periodic_time': max(dist),
        'first_periodic_time_counts': dict(sorted(depth_hist.items())),
        'by_eventual_period_and_time': byperiod,
        'basin_size_hist_by_period': basin_hist,
        'zero_consensus_basin': basins[0], 'one_consensus_basin': basins[65535],
        'sharp_witness_state': exemplar, 'sharp_witness_trajectory': orbitpath
    }
    assert sum(depth_hist.values()) == 65536
    assert sum(b * int(c) for p,hist in basin_hist.items() for b,c in hist.items()) == 65536
    return out


if __name__ == '__main__':
    answer = [census('rook'),census('shrikhande')]
    assert answer[0]['four_cliques'] == 8 and answer[1]['four_cliques'] == 0
    assert answer[0]['fixed_orbits'] == 302 and answer[1]['fixed_orbits'] == 142
    assert answer[0]['primitive_two_cycle_orbits'] == 1197 and answer[1]['primitive_two_cycle_orbits'] == 685
    print(json.dumps(answer, sort_keys=True, indent=2))
