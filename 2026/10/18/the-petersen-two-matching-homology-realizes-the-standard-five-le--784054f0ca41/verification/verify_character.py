#!/usr/bin/env python3
"""Finite verification of the Petersen two-matching S5 character.

Python standard library only.  All faces and face-poset relations are rebuilt
from the definition, and all seven S5 conjugacy classes are evaluated twice.
"""
from collections import Counter, deque
from itertools import combinations

POINTS = tuple(range(5))
PVERT = list(combinations(POINTS, 2))
PEDGES = [(a, b) for a in range(10) for b in range(a + 1, 10)
          if set(PVERT[a]).isdisjoint(PVERT[b])]
assert len(PEDGES) == 15
EDGE_INDEX = {e: j for j, e in enumerate(PEDGES)}
CLASSES = [
    ("1^5", ()),
    ("2,1^3", ((0, 1),)),
    ("2^2,1", ((0, 1), (2, 3))),
    ("3,1^2", ((0, 1, 2),)),
    ("3,2", ((0, 1, 2), (3, 4))),
    ("4,1", ((0, 1, 2, 3),)),
    ("5", ((0, 1, 2, 3, 4),)),
]
EXPECTED_F = [15, 105, 445, 1245, 2358, 2985, 2400, 1095, 215, 6]
EXPECTED_CHI = [4, 2, 0, 1, -1, 0, -1]


def degree_test(mask):
    degree = [0] * 10
    for e, (a, b) in enumerate(PEDGES):
        if (mask >> e) & 1:
            degree[a] += 1
            degree[b] += 1
            if degree[a] > 2 or degree[b] > 2:
                return False
    return True


def induced_edge_permutation(cycles):
    p = list(POINTS)
    for cycle in cycles:
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            p[a] = b
    vp = [PVERT.index(tuple(sorted((p[a], p[b])))) for a, b in PVERT]
    ep = [EDGE_INDEX[tuple(sorted((vp[a], vp[b])))] for a, b in PEDGES]
    assert sorted(vp) == list(range(10))
    assert sorted(ep) == list(range(15))
    return p, ep


def orbit_sets(ep):
    marked = set()
    orbits = []
    for e in range(15):
        if e in marked:
            continue
        orbit = []
        x = e
        while x not in marked:
            marked.add(x)
            orbit.append(x)
            x = ep[x]
        assert x == e
        orbits.append(tuple(orbit))
    return orbits


def orbit_alternating_sum(orbits):
    face_count = Counter()
    for choice in range(1 << len(orbits)):
        mask = 0
        for k, orbit in enumerate(orbits):
            if (choice >> k) & 1:
                for e in orbit:
                    mask |= 1 << e
        if degree_test(mask):
            face_count[choice.bit_count()] += 1
    return sum((-1) ** k * v for k, v in face_count.items()), face_count


def direct_signed_trace(ep, faces):
    # Reduced Lefschetz sum has an empty-face term -1.
    lefschetz = -1
    for mask in faces:
        active = [e for e in range(15) if (mask >> e) & 1]
        image = [ep[e] for e in active]
        if set(image) != set(active):
            continue
        inversions = sum(image[i] > image[j] for i in range(len(image))
                         for j in range(i + 1, len(image)))
        lefschetz += (-1) ** (len(active) - 1 + inversions)
    # Since only reduced H_7 is present, its trace equals -Ltilde.
    return -lefschetz


def repeated_toggle_morse(faces):
    remaining = set(faces)
    partners = {}
    for pivot in range(15):
        bit = 1 << pivot
        matches = [(m, m | bit) for m in sorted(remaining)
                   if m & bit == 0 and (m | bit) in remaining]
        for a, b in matches:
            assert a in remaining and b in remaining and b == (a | bit)
            assert a.bit_count() + 1 == b.bit_count()
            remaining.remove(a)
            remaining.remove(b)
            partners[(a, b)] = 1
    crit = Counter(m.bit_count() - 1 for m in remaining)
    assert crit == Counter({0: 1, 7: 4}), crit
    assert len(partners) == 5432
    return partners, crit


def certify_acyclicity(faces, partners):
    # All nonempty faces are vertices of the Hasse digraph. Default
    # orientation: larger face -> codimension-one smaller face. Reverse
    # precisely the matched edges, then verify a full topological sort.
    indegree = {m: 0 for m in faces}
    adj = {m: [] for m in faces}
    count = 0
    for high in faces:
        rem = high
        while rem:
            bit = rem & -rem
            low = high ^ bit
            rem ^= bit
            if low == 0:
                continue
            a, b = (low, high) if (low, high) in partners else (high, low)
            adj[a].append(b)
            indegree[b] += 1
            count += 1
    assert count == 63780, count
    queue = deque(m for m, n in indegree.items() if n == 0)
    seen = 0
    while queue:
        m = queue.popleft()
        seen += 1
        for z in adj[m]:
            indegree[z] -= 1
            if indegree[z] == 0:
                queue.append(z)
    assert seen == len(faces), (seen, len(faces))
    return count, seen


def main():
    faces = [mask for mask in range(1, 1 << 15) if degree_test(mask)]
    f = Counter(mask.bit_count() - 1 for mask in faces)
    assert [f[j] for j in range(10)] == EXPECTED_F
    print("Petersen vertices=10 edges=15 nonempty_faces=%d" % len(faces))
    print("f_vector:", [f[j] for j in range(10)])
    matching, critical = repeated_toggle_morse(faces)
    count, seen = certify_acyclicity(faces, matching)
    print("Morse_pairs=%d critical=%s Hasse_covers=%d DAG_vertices=%d" %
          (len(matching), dict(sorted(critical.items())), count, seen))
    result = []
    for name, cycles in CLASSES:
        p, edgep = induced_edge_permutation(cycles)
        orbits = orbit_sets(edgep)
        orbital, counts = orbit_alternating_sum(orbits)
        signed = direct_signed_trace(edgep, faces)
        expected = sum(i == p[i] for i in POINTS) - 1
        assert orbital == signed == expected
        result.append(orbital)
        print("class=%s edge_orbits=%d orbit_euler=%d fixed_face_trace=%d fixed_points_minus_one=%d admissible_orbit_subset_counts=%s" %
              (name, len(orbits), orbital, signed, expected, [counts[j] for j in range(max(counts) + 1)]))
    assert result == EXPECTED_CHI
    print("character:", result)
    print("PASS: complete topological sort and two independent character enumerations")


if __name__ == "__main__":
    main()
