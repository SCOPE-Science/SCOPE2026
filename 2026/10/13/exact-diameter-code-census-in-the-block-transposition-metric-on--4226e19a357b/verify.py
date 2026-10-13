#!/usr/bin/env python3
import collections
import itertools
import json

N = 5
PERMS = list(itertools.permutations(range(1, N + 1)))
INDEX = {p: i for i, p in enumerate(PERMS)}
IDENTITY = tuple(range(1, N + 1))


def compose(p, q):
    """Function composition p o q in one-line notation."""
    return tuple(p[q[i] - 1] for i in range(N))


def inverse(p):
    out = [0] * N
    for i, value in enumerate(p, 1):
        out[value - 1] = i
    return tuple(out)


def block_transpose(p, i, j, k):
    """Swap the adjacent position blocks p[i:j] and p[j:k]."""
    return p[:i] + p[j:k] + p[i:j] + p[k:]


CUTS = list(itertools.combinations(range(N + 1), 3))
GENERATORS = sorted({block_transpose(IDENTITY, *cuts) for cuts in CUTS})
assert len(GENERATORS) == 20

# Distance from the identity, reconstructed directly from the generators.
distance_from_identity = {IDENTITY: 0}
queue = collections.deque([IDENTITY])
while queue:
    p = queue.popleft()
    d = distance_from_identity[p]
    for cuts in CUTS:
        q = block_transpose(p, *cuts)
        if q not in distance_from_identity:
            distance_from_identity[q] = d + 1
            queue.append(q)
assert len(distance_from_identity) == 120


def distance(p, q):
    # This is the Cayley-graph convention for which right translations are automorphisms.
    return distance_from_identity[compose(q, inverse(p))]


distance_histogram = collections.Counter(distance_from_identity.values())
assert distance_histogram == {0: 1, 1: 20, 2: 68, 3: 31}
assert max(distance_from_identity.values()) == 3

# Compatibility graph for minimum distance at least three.
adjacency = [0] * len(PERMS)
edge_count = 0
for a in range(len(PERMS)):
    for b in range(a + 1, len(PERMS)):
        if distance(PERMS[a], PERMS[b]) >= 3:
            adjacency[a] |= 1 << b
            adjacency[b] |= 1 << a
            edge_count += 1
assert edge_count == 1860
assert {row.bit_count() for row in adjacency} == {31}

# Exhaustive Bron-Kerbosch enumeration of maximal cliques.
maximal_histogram = collections.Counter()
maximum_cliques = []
bk_nodes = 0


def bron_kerbosch(R, P, X):
    global bk_nodes
    bk_nodes += 1
    if not P and not X:
        maximal_histogram[len(R)] += 1
        if len(R) >= 4:
            maximum_cliques.append(frozenset(R))
        return
    union = P | X
    if union:
        vertices = []
        z = union
        while z:
            bit = z & -z
            vertices.append(bit.bit_length() - 1)
            z -= bit
        pivot = max(vertices, key=lambda v: (P & adjacency[v]).bit_count())
        candidates = P & ~adjacency[pivot]
    else:
        candidates = P
    while candidates:
        bit = candidates & -candidates
        v = bit.bit_length() - 1
        bron_kerbosch(R + (v,), P & adjacency[v], X & adjacency[v])
        P &= ~bit
        X |= bit
        candidates &= ~bit


bron_kerbosch(tuple(), (1 << len(PERMS)) - 1, 0)
assert maximal_histogram == {2: 60, 4: 540}
maximum_cliques = set(maximum_cliques)
assert len(maximum_cliques) == 540

# Independent increasing-order enumeration of all four-cliques.
four_cliques = set()
for a in range(120):
    bmask = adjacency[a] & ~((1 << (a + 1)) - 1)
    z = bmask
    while z:
        bit_b = z & -z
        b = bit_b.bit_length() - 1
        z -= bit_b
        cmask = bmask & adjacency[b] & ~((1 << (b + 1)) - 1)
        y = cmask
        while y:
            bit_c = y & -y
            c = bit_c.bit_length() - 1
            y -= bit_c
            dmask = cmask & adjacency[c] & ~((1 << (c + 1)) - 1)
            w = dmask
            while w:
                bit_d = w & -w
                d = bit_d.bit_length() - 1
                w -= bit_d
                four_cliques.add(frozenset((a, b, c, d)))
assert four_cliques == maximum_cliques
assert all(
    distance(PERMS[a], PERMS[b]) == 3
    for code in maximum_cliques
    for a, b in itertools.combinations(code, 2)
)

identity_index = INDEX[IDENTITY]
normalized_codes = [code for code in maximum_cliques if identity_index in code]
assert len(normalized_codes) == 18

# Toric maps and reversal, from the standard formulas for the block-transposition graph.
def toric(p, r):
    augmented = (0,) + p
    base = augmented[r]
    out = tuple(
        (augmented[(r + t) % (N + 1)] - base) % (N + 1)
        for t in range(1, N + 1)
    )
    assert sorted(out) == list(range(1, N + 1))
    return out


def reverse_map(p):
    return tuple(N + 1 - p[N - 1 - i] for i in range(N))


identity_stabilizer = []
for r in range(N + 1):
    identity_stabilizer.append(tuple(INDEX[toric(p, r)] for p in PERMS))
    identity_stabilizer.append(tuple(INDEX[reverse_map(toric(p, r))] for p in PERMS))
identity_stabilizer = list(dict.fromkeys(identity_stabilizer))
assert len(identity_stabilizer) == 12
assert all(m[identity_index] == identity_index for m in identity_stabilizer)
for mapping in identity_stabilizer:
    for a in range(120):
        for b in range(a + 1, 120):
            assert distance(PERMS[a], PERMS[b]) == distance(
                PERMS[mapping[a]], PERMS[mapping[b]]
            )

# Right translations combined with the twelve maps above give 1440 distinct isometries.
right_translations = [
    tuple(INDEX[compose(p, tau)] for p in PERMS)
    for tau in PERMS
]
isometry_group = []
seen_maps = set()
for translation in right_translations:
    for fixed_map in identity_stabilizer:
        mapping = tuple(translation[fixed_map[i]] for i in range(120))
        if mapping not in seen_maps:
            seen_maps.add(mapping)
            isometry_group.append(mapping)
assert len(isometry_group) == 1440

# Orbits of maximum codes under the constructed 1440-element group.
unseen = set(maximum_cliques)
orbits = []
while unseen:
    code = min(unseen, key=lambda c: tuple(sorted(c)))
    orbit = {
        frozenset(mapping[i] for i in code)
        for mapping in isometry_group
    }
    assert orbit <= maximum_cliques
    orbits.append(orbit)
    unseen -= orbit
assert sorted(map(len, orbits)) == [180, 360]


def code_strings(code):
    return sorted("".join(map(str, PERMS[i])) for i in code)


orbit_records = []
for orbit in sorted(orbits, key=len):
    representative = min(orbit, key=lambda c: tuple(code_strings(c)))
    orbit_records.append({
        "size": len(orbit),
        "stabilizer_order": 1440 // len(orbit),
        "representative": code_strings(representative),
    })
assert orbit_records == [
    {
        "size": 180,
        "stabilizer_order": 8,
        "representative": ["12345", "15432", "52413", "53142"],
    },
    {
        "size": 360,
        "stabilizer_order": 4,
        "representative": ["12345", "21543", "35241", "53142"],
    },
]


def as_permutations(code):
    return {PERMS[i] for i in code}


def is_subgroup(code):
    subset = as_permutations(code)
    return IDENTITY in subset and all(compose(a, b) in subset for a in subset for b in subset)


def element_order(p):
    power = IDENTITY
    for order in range(1, 121):
        power = compose(power, p)
        if power == IDENTITY:
            return order
    raise AssertionError("order not found")


subgroup_codes = [code for code in normalized_codes if is_subgroup(code)]
assert len(subgroup_codes) == 4
subgroup_records = []
coset_families = []
for code in sorted(subgroup_codes, key=lambda c: tuple(code_strings(c))):
    subgroup = as_permutations(code)
    orders = sorted(element_order(p) for p in subgroup)
    assert orders == [1, 2, 4, 4]
    generators = sorted("".join(map(str, p)) for p in subgroup if element_order(p) == 4)
    family = {
        frozenset(INDEX[compose(h, g)] for h in subgroup)
        for g in PERMS
    }
    assert len(family) == 30
    assert family <= maximum_cliques
    coset_families.append(family)
    subgroup_records.append({
        "elements": sorted("".join(map(str, p)) for p in subgroup),
        "order4_generators": generators,
    })
assert all(
    not (coset_families[i] & coset_families[j])
    for i in range(4)
    for j in range(i + 1, 4)
)
coset_codes = set().union(*coset_families)
assert len(coset_codes) == 120
small_orbit, large_orbit = sorted(orbits, key=len)
assert len(coset_codes & small_orbit) == 0
assert len(coset_codes & large_orbit) == 120

certificate = {
    "n": 5,
    "generator_count": len(GENERATORS),
    "distance_histogram": dict(sorted(distance_histogram.items())),
    "diameter": 3,
    "compatibility_edges": edge_count,
    "bk_nodes": bk_nodes,
    "maximal_clique_histogram": dict(sorted(maximal_histogram.items())),
    "maximum_code_size": 4,
    "labeled_maximum_codes": len(maximum_cliques),
    "normalized_maximum_codes": len(normalized_codes),
    "constructed_isometry_group_order": len(isometry_group),
    "maximum_code_orbits": orbit_records,
    "subgroup_maximum_codes": len(subgroup_codes),
    "cyclic_order4_subgroups": subgroup_records,
    "right_coset_maximum_codes": len(coset_codes),
    "noncoset_maximum_codes": len(maximum_cliques - coset_codes),
}
print(json.dumps(certificate, sort_keys=True))
print(
    "VERIFY_OK "
    "vertices=120 generators=20 distance_hist=0:1,1:20,2:68,3:31 "
    "compatibility_edges=1860 maximal_hist=2:60,4:540 maximum=4 "
    "labeled_maxima=540 normalized_maxima=18 group_size=1440 "
    "orbits=180,360 subgroup_maxima=4 right_coset_maxima=120 noncoset_maxima=420"
)
