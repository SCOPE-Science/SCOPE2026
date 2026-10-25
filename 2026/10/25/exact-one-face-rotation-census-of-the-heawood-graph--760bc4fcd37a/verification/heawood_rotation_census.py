#!/usr/bin/env python3
"""Exact rotation-system census for the Heawood graph.

The Heawood graph is represented as the point-line incidence graph of the
Fano plane.  Each bit chooses one of the two cyclic orders at a cubic vertex.
The script enumerates all rotations, traces facial walks, and computes orbits
under the full 336-element automorphism group.
"""
from itertools import permutations, product
from collections import Counter
import json

VECTORS = tuple(range(1, 8))
VERTICES = tuple(range(14))

def bits3(x):
    return ((x >> 2) & 1, (x >> 1) & 1, x & 1)

def dot2(a, b):
    return sum(x * y for x, y in zip(bits3(a), bits3(b))) % 2

def xor_vec(*xs):
    out = 0
    for x in xs:
        out ^= x
    return out

def independent(a, b, c):
    return a != b and c not in (a, b, a ^ b)

def make_graph():
    adj = {v: [] for v in VERTICES}
    for p in VECTORS:
        for ell in VECTORS:
            if dot2(p, ell) == 0:
                u, v = p - 1, 7 + ell - 1
                adj[u].append(v)
                adj[v].append(u)
    return {v: tuple(sorted(adj[v])) for v in VERTICES}

def automorphisms():
    # Collineations induced by GL(3,2).
    collineations = []
    for a, b, c in permutations(VECTORS, 3):
        if not independent(a, b, c):
            continue
        point_map = {}
        for x in VECTORS:
            bx = bits3(x)
            point_map[x] = xor_vec(*(col for bit, col in zip(bx, (a, b, c)) if bit))
        inverse = {y: x for x, y in point_map.items()}
        # Matrix A has columns a,b,c. Lines (covectors) transform by A^{-T}.
        a_rows = [[(a >> (2-r)) & 1, (b >> (2-r)) & 1, (c >> (2-r)) & 1]
                  for r in range(3)]
        b_rows = [[(inverse[1 << (2-col)] >> (2-row)) & 1
                   for col in range(3)] for row in range(3)]
        line_map = {}
        for ell in VECTORS:
            lv = bits3(ell)
            out = [sum(b_rows[j][i] * lv[j] for j in range(3)) % 2
                   for i in range(3)]
            line_map[ell] = 4*out[0] + 2*out[1] + out[2]
        f = [None] * 14
        for p in VECTORS:
            f[p-1] = point_map[p] - 1
        for ell in VECTORS:
            f[7+ell-1] = 7 + line_map[ell] - 1
        collineations.append(tuple(f))
    # Fano-plane duality interchanges points and lines with the same vector.
    duality = tuple([7+i for i in range(7)] + [i for i in range(7)])
    group = list(collineations)
    group.extend(tuple(duality[f[i]] for i in range(14)) for f in collineations)
    group = tuple(dict.fromkeys(group))
    return group

def face_lengths(rotation, adj):
    # A dart (v,u) points from v to u. alpha reverses the dart; sigma
    # advances to the next dart in the chosen cyclic order at its start.
    darts = tuple((v, u) for v in VERTICES for u in adj[v])
    did = {d: i for i, d in enumerate(darts)}
    alpha = [did[(u, v)] for v, u in darts]
    sigma = [None] * len(darts)
    for v in VERTICES:
        nbr = adj[v]
        cyc = nbr if rotation[v] == 0 else (nbr[0], nbr[2], nbr[1])
        for i, u in enumerate(cyc):
            sigma[did[(v, u)]] = did[(v, cyc[(i+1) % 3])]
    # Each cycle of sigma after alpha is one facial walk.
    phi = [sigma[alpha[i]] for i in range(len(darts))]
    seen = set()
    lengths = []
    for start in range(len(darts)):
        if start in seen:
            continue
        cur, length = start, 0
        while cur not in seen:
            seen.add(cur)
            length += 1
            cur = phi[cur]
        assert cur == start
        lengths.append(length)
    return tuple(sorted(lengths))

def face_count_independent(rotation, adj):
    # Independent traversal formulation: after a dart reaches its head,
    # take the predecessor of the reversed dart in the local cyclic order.
    cyclic_predecessor = {}
    for v in VERTICES:
        nbr = adj[v]
        cyc = list(nbr) if rotation[v] == 0 else [nbr[0], nbr[2], nbr[1]]
        for i, u in enumerate(cyc):
            cyclic_predecessor[(v, u)] = cyc[(i - 1) % 3]
    darts = tuple((v, u) for v in VERTICES for u in adj[v])
    seen = set()
    faces = 0
    for start in darts:
        if start in seen:
            continue
        faces += 1
        cur = start
        while cur not in seen:
            seen.add(cur)
            v, u = cur
            cur = (u, cyclic_predecessor[(u, v)])
        assert cur == start
    assert len(seen) == 42
    return faces

def map_rotation(rotation, f, adj):
    out = [None] * 14
    for v in VERTICES:
        nbr = adj[v]
        cyc = list(nbr if rotation[v] == 0 else (nbr[0], nbr[2], nbr[1]))
        image = [f[u] for u in cyc]
        w, base = f[v], list(adj[f[v]])
        def cyclically_equal(a, b):
            return any(a == b[k:] + b[:k] for k in range(len(b)))
        if cyclically_equal(image, base):
            out[w] = 0
        elif cyclically_equal(image, [base[0], base[2], base[1]]):
            out[w] = 1
        else:
            raise AssertionError("automorphism did not preserve adjacency/cyclic order")
    return tuple(out)

def main():
    adj = make_graph()
    assert len(adj) == 14
    assert sum(len(nbr) for nbr in adj.values()) // 2 == 21
    assert all(len(adj[v]) == 3 for v in VERTICES)

    group = automorphisms()
    assert len(group) == 336
    for f in group:
        assert all({f[u] for u in adj[v]} == set(adj[f[v]]) for v in VERTICES)

    rotations = tuple(product((0, 1), repeat=14))
    profiles = {r: face_lengths(r, adj) for r in rotations}
    face_count_distribution = Counter(len(p) for p in profiles.values())
    independent_distribution = Counter(
        face_count_independent(r, adj) for r in rotations
    )
    assert independent_distribution == face_count_distribution
    assert sum(face_count_distribution.values()) == 2**14
    assert face_count_distribution == Counter({1: 4480, 3: 10880, 5: 1008, 7: 16})

    one_face = {r for r, p in profiles.items() if len(p) == 1}
    unseen = set(one_face)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {map_rotation(representative, f, adj) for f in group}
        assert orbit <= one_face
        orbits.append((len(orbit), representative))
        unseen -= orbit
    assert len(one_face) == 4480
    assert len(orbits) == 16
    assert Counter(size for size, _ in orbits) == Counter({336: 12, 112: 4})

    # Burnside's lemma independently checks the orbit count.
    fixed_counts = [
        sum(map_rotation(rotation, f, adj) == rotation for rotation in one_face)
        for f in group
    ]
    assert sum(fixed_counts) % len(group) == 0
    assert sum(fixed_counts) // len(group) == len(orbits)
    assert Counter(fixed_counts) == Counter({0: 279, 16: 56, 4480: 1})

    # Mirror reversal complements every local cyclic-order bit.
    rep_to_orbit = {}
    for i, (size, rep) in enumerate(orbits):
        for f in group:
            rep_to_orbit[map_rotation(rep, f, adj)] = i
    mirror_partner = {}
    for i, (size, rep) in enumerate(orbits):
        mirror = tuple(1 - bit for bit in rep)
        mirror_partner[i] = rep_to_orbit[mirror]
    assert all(mirror_partner[mirror_partner[i]] == i for i in range(len(orbits)))
    assert all(mirror_partner[i] != i for i in range(len(orbits)))
    mirror_pairs = {tuple(sorted((i, j))) for i, j in mirror_partner.items()}
    assert len(mirror_pairs) == 8
    mirror_class_sizes = Counter(
        orbits[i][0] + orbits[j][0] for i, j in mirror_pairs
    )
    assert mirror_class_sizes == Counter({672: 6, 224: 2})
    mirror_pair_records = [
        {
            "representative_a": "".join(map(str, orbits[i][1])),
            "size_a": orbits[i][0],
            "representative_b": "".join(map(str, orbits[j][1])),
            "size_b": orbits[j][0],
        }
        for i, j in sorted(mirror_pairs)
    ]

    # Euler check: H has V=14 and E=21; for one face, chi=-6 and genus=4.
    euler_characteristic = 14 - 21 + 1
    genus = (2 - euler_characteristic) // 2
    assert euler_characteristic == -6 and genus == 4

    print(json.dumps({
        "graph": "Heawood graph (Fano-plane incidence graph)",
        "vertices": 14,
        "edges": 21,
        "automorphism_group_order": len(group),
        "total_rotation_systems": len(rotations),
        "face_count_distribution": {str(k): face_count_distribution[k]
                                    for k in sorted(face_count_distribution)},
        "independent_face_tracer_agrees": True,
        "one_face_rotation_systems": len(one_face),
        "one_face_genus": genus,
        "orientation_preserving_orbits": len(orbits),
        "burnside_fixed_count_distribution": {str(k): Counter(fixed_counts)[k]
                                              for k in sorted(Counter(fixed_counts))},
        "orbit_size_distribution": {str(k): Counter(size for size, _ in orbits)[k]
                                    for k in sorted(Counter(size for size, _ in orbits))},
        "mirror_classes": len(mirror_pairs),
        "mirror_class_size_distribution": {str(k): mirror_class_sizes[k]
                                           for k in sorted(mirror_class_sizes)},
        "mirror_pairs": mirror_pair_records,
        "orbit_representatives_bits": [
            {"size": size, "bits": "".join(map(str, rep))}
            for size, rep in sorted(orbits, key=lambda item: (item[0], item[1]))
        ],
    }, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
