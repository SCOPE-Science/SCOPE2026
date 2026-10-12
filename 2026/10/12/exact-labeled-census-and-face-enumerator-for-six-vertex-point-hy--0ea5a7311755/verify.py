from itertools import combinations, permutations

V = tuple(range(6))
TRIPLES = list(combinations(V, 3))
TRIPLE_INDEX = {t: i for i, t in enumerate(TRIPLES)}
FOURS = list(combinations(V, 4))
FOUR_MASKS = []
for q in FOURS:
    mask = 0
    for t in combinations(q, 3):
        mask |= 1 << TRIPLE_INDEX[t]
    FOUR_MASKS.append(mask)

# Theorem 5.16 obstruction, translated from 1,...,6 to 0,...,5.
OBSTRUCTION = {
    (0, 1, 3), (0, 2, 4), (0, 3, 4),
    (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5),
}
OBSTRUCTION_MASK = sum(1 << TRIPLE_INDEX[t] for t in OBSTRUCTION)
PERMS = list(permutations(V))


def permute_mask(mask, p):
    out = 0
    while mask:
        low = mask & -mask
        i = low.bit_length() - 1
        t = TRIPLES[i]
        u = tuple(sorted((p[t[0]], p[t[1]], p[t[2]])))
        out |= 1 << TRIPLE_INDEX[u]
        mask -= low
    return out


def tetrahedron_condition(mask):
    # Three faces on any four vertices are forbidden; 0,1,2,4 are allowed.
    return all((mask & q).bit_count() != 3 for q in FOUR_MASKS)


obstruction_orbit = {permute_mask(OBSTRUCTION_MASK, p) for p in PERMS}
assert len(obstruction_orbit) == 120
assert all(tetrahedron_condition(m) for m in obstruction_orbit)

adequate = set()
adequate_by_faces = [0] * 21
for mask in range(1 << len(TRIPLES)):
    if tetrahedron_condition(mask):
        adequate.add(mask)
        adequate_by_faces[mask.bit_count()] += 1

point = adequate - obstruction_orbit
point_by_faces = [0] * 21
for mask in point:
    point_by_faces[mask.bit_count()] += 1

expected_face_distribution = {
    0: 1, 1: 20, 2: 190, 3: 1080, 4: 3885, 5: 8844,
    6: 12510, 7: 10800, 8: 6870, 9: 3540, 10: 1568,
    11: 440, 12: 330, 13: 60, 14: 60, 16: 15, 20: 1,
}
assert len(adequate) == 50334
assert len(point) == 50214
assert {i: c for i, c in enumerate(point_by_faces) if c} == expected_face_distribution
assert adequate_by_faces[7] - point_by_faces[7] == 120
assert all(adequate_by_faces[i] == point_by_faces[i] for i in range(21) if i != 7)

# Quotient independently by the full S_6 action.  Removing one orbit at a time
# avoids relying on canonical-labeling software.
remaining = set(point)
orbit_profile = {}
num_orbits = 0
while remaining:
    representative = min(remaining)
    orbit = {permute_mask(representative, p) for p in PERMS}
    assert orbit <= point
    num_orbits += 1
    orbit_profile[len(orbit)] = orbit_profile.get(len(orbit), 0) + 1
    remaining -= orbit

expected_orbit_profile = {
    1: 2, 6: 1, 10: 1, 12: 1, 15: 6, 20: 3, 30: 2, 45: 4,
    60: 13, 72: 2, 90: 15, 120: 7, 180: 28, 240: 1,
    360: 61, 720: 27,
}
assert num_orbits == 174
assert orbit_profile == expected_orbit_profile
assert sum(size * count for size, count in orbit_profile.items()) == 50214

print('triples=20 total_labeled_hypergraphs=1048576')
print('tetrahedron_condition_count=50334')
print('octahedral_obstruction_orbit_size=120')
print('point_hypergraph_labeled_count=50214')
print('face_distribution=' + repr(expected_face_distribution))
print('S6_orbit_count=174')
print('S6_orbit_size_profile=' + repr(expected_orbit_profile))
print('VERIFY_OK')
