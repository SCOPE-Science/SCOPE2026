#!/usr/bin/env python3
"""Reproduce the finite Desargues ordinary-zero-forcing census.

Usage: python3 verify_python.py output_certificate.tsv
Standard Python only; every 20-bit state is checked from the graph definition.
"""
import collections
import itertools
import pathlib
import sys


def main(destination):
    # Two and three-subsets of {0,1,2,3,4}, encoded as 5-bit integers.
    ground = tuple(range(5))
    vertices = sorted(m for m in range(32) if m.bit_count() in (2, 3))
    assert len(vertices) == 20
    index = {s: i for i, s in enumerate(vertices)}
    lower_mask = sum(1 << i for i, s in enumerate(vertices) if s.bit_count() == 2)
    upper_mask = ((1 << 20) - 1) ^ lower_mask
    adj = [0] * 20
    for i, a in enumerate(vertices):
        for j, b in enumerate(vertices):
            if a.bit_count() == 2 and b.bit_count() == 3 and (a & b) == a:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    assert sum(a.bit_count() for a in adj) == 60
    FULL = (1 << 20) - 1

    # Parallel forcing update: all eligible unique white neighbours simultaneously.
    def is_forcing(start):
        blue = start
        while True:
            new = 0
            for i, ni in enumerate(adj):
                if blue & (1 << i):
                    white = ni & ~blue
                    if white and white & (white - 1) == 0:
                        new |= white
            if not (new & ~blue):
                return blue == FULL
            blue |= new

    poly = [0] * 21
    states = []
    for start in range(1 << 20):
        if is_forcing(start):
            k = start.bit_count()
            poly[k] += 1
            if k == 8:
                states.append(start)
    assert sum(poly) == 524462
    assert len(states) == 13520
    assert all((m & lower_mask).bit_count() == (m & upper_mask).bit_count() == 4 for m in states)
    assert all(poly[k] == 0 for k in range(8))
    lookup = {m: idx for idx, m in enumerate(states)}
    neighbors = [[] for _ in states]
    edges = []
    for ii, m in enumerate(states):
        for u in range(20):
            if m & (1 << u):
                for v in range(20):
                    if not m & (1 << v):
                        changed = m ^ (1 << u) ^ (1 << v)
                        jj = lookup.get(changed)
                        if jj is not None and changed > m:
                            edges.append((m, changed))
                            neighbors[ii].append(jj)
                            neighbors[jj].append(ii)
    edges.sort()
    assert len(edges) == 178560
    degdist = sorted(collections.Counter(map(len, neighbors)).items())
    assert sum(k * x for k, x in degdist) == 2 * len(edges)

    # Permute the five underlying points and optionally swap subsets with complements.
    permutations = []
    for perm in itertools.permutations(ground):
        for complement in (False, True):
            point_map = []
            for s in vertices:
                mapped = sum(1 << perm[i] for i in ground if s & (1 << i))
                if complement:
                    mapped ^= 31
                point_map.append(index[mapped])
            permutations.append(tuple(point_map))
    assert len(set(permutations)) == 240

    def transform(mask, mapping):
        image = 0
        for i in range(20):
            if mask & (1 << i):
                image |= 1 << mapping[i]
        return image

    seen = set()
    orbits = []
    for mask in states:
        if mask in seen:
            continue
        orbit = {transform(mask, perm) for perm in permutations}
        assert orbit <= lookup.keys()
        assert not (orbit & seen)
        seen |= orbit
        orbits.append((mask, len(orbit)))
    assert len(seen) == len(states)
    assert len(orbits) == 67
    ecci = collections.Counter()
    final_orbits = []
    for mask, size in orbits:
        source = lookup[mask]
        distance = [-1] * len(states)
        distance[source] = 0
        queue = [source]
        for cur in queue:
            for successor in neighbors[cur]:
                if distance[successor] == -1:
                    distance[successor] = distance[cur] + 1
                    queue.append(successor)
        assert len(queue) == len(states)
        eccentricity = max(distance)
        ecci[eccentricity] += size
        distribution = [distance.count(k) for k in range(eccentricity + 1)]
        final_orbits.append((mask, size, eccentricity, distribution))
    assert dict(ecci) == {7: 980, 8: 12540}

    # A complete certificate of minima and every unordered exchange, followed by
    # one eccentricity and distance profile per verified automorphism orbit.
    lines = ['DZF1\n', 'POLY ' + ' '.join(map(str, poly)) + '\n',
             'Z8 13520\n', 'JUMPEDGES 178560\n',
             'ECC 7:980 8:12540\n',
             'DEGREES ' + ' '.join(f'{k}:{v}' for k, v in degdist) + '\n',
             'ORBITS 67\n']
    lines += [f'S {m:05x}\n' for m in states]
    lines += [f'E {u:05x} {v:05x}\n' for u, v in edges]
    lines += [f'O {m:05x} {size} {ecc} ' + ','.join(map(str, counts)) + '\n'
              for m, size, ecc, counts in final_orbits]
    output = ''.join(lines).encode('ascii')
    pathlib.Path(destination).write_bytes(output)
    print('verified vertices=20 edges=30 kmin=8 minsets=13520 balanced=13520')
    print('forcing_polynomial=' + ','.join(map(str, poly)))
    print(f'exchanges={len(edges)} degree_hist={degdist}')
    print('token_slide_edges=0 (all minimum sets have 4+4 bipartition profile)')
    print('automorphism_action_size=240 orbit_count=67 orbit_sizes=' + str(dict(sorted(collections.Counter(size for _, size in orbits).items()))))
    print('jump_components=1 radius=7 diameter=8 eccentricity_hist=' + str(dict(sorted(ecci.items()))))
    print(f'certificate_bytes={len(output)}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: verify_python.py certificate_path')
    main(sys.argv[1])
