#!/usr/bin/env python3
"""Exhaustive verification for maximum Kendall-tau codes in S_5 at distance 6."""
from itertools import permutations, combinations
from collections import Counter

N = 5
PERMS = list(permutations(range(N)))
INDEX = {p: i for i, p in enumerate(PERMS)}
IDENTITY = tuple(range(N))


def kendall(p, q):
    pos = [0] * N
    for i, value in enumerate(p):
        pos[value] = i
    seq = [pos[value] for value in q]
    return sum(seq[i] > seq[j] for i in range(N) for j in range(i + 1, N))


DIST = [[0] * len(PERMS) for _ in PERMS]
for i, p in enumerate(PERMS):
    for j in range(i + 1, len(PERMS)):
        d = kendall(p, PERMS[j])
        DIST[i][j] = d
        DIST[j][i] = d

# Compatibility graph: an edge means Kendall distance at least 6.
ADJ = [0] * len(PERMS)
EDGE_COUNT = 0
for i in range(len(PERMS)):
    mask = 0
    for j in range(len(PERMS)):
        if i != j and DIST[i][j] >= 6:
            mask |= 1 << j
    ADJ[i] = mask
    EDGE_COUNT += mask.bit_count()
EDGE_COUNT //= 2

MAXIMAL_HIST = Counter()
MAX_SIZE = 0
MAXIMA = []
BK_NODES = 0


def bron_kerbosch(r, p, x):
    """Enumerate every maximal clique using the standard pivot recurrence."""
    global MAX_SIZE, MAXIMA, BK_NODES
    BK_NODES += 1
    if not p and not x:
        size = r.bit_count()
        MAXIMAL_HIST[size] += 1
        if size > MAX_SIZE:
            MAX_SIZE = size
            MAXIMA = [r]
        elif size == MAX_SIZE:
            MAXIMA.append(r)
        return

    union = p | x
    if union:
        u_mask = union
        pivot = -1
        best = -1
        while u_mask:
            bit = u_mask & -u_mask
            u = bit.bit_length() - 1
            u_mask -= bit
            score = (p & ADJ[u]).bit_count()
            if score > best:
                best = score
                pivot = u
        extension = p & ~ADJ[pivot]
    else:
        extension = p

    while extension:
        bit = extension & -extension
        v = bit.bit_length() - 1
        extension -= bit
        bron_kerbosch(r | bit, p & ADJ[v], x & ADJ[v])
        p -= bit
        x |= bit


bron_kerbosch(0, (1 << len(PERMS)) - 1, 0)
MAXIMUM_SET = set(MAXIMA)

assert MAX_SIZE == 5
assert len(MAXIMA) == 168
assert MAXIMAL_HIST == Counter({2: 300, 3: 3120, 4: 3960, 5: 168})

# Independent ordered enumeration of every 5-clique.  Any clique of size at
# least 6 would extend one of these 5-cliques, so the absence of a common
# neighbor independently certifies the upper bound 5.
FIVE_CLIQUES = []
def extend_five(prefix, candidates):
    if len(prefix) == 5:
        mask = 0
        for v in prefix:
            mask |= 1 << v
        FIVE_CLIQUES.append(mask)
        return
    need = 5 - len(prefix)
    cand = candidates
    while cand and cand.bit_count() >= need:
        bit = cand & -cand
        v = bit.bit_length() - 1
        cand -= bit
        higher = cand & ADJ[v]
        extend_five(prefix + [v], higher)

extend_five([], (1 << len(PERMS)) - 1)
assert len(FIVE_CLIQUES) == 168
assert set(FIVE_CLIQUES) == set(MAXIMA)
for code in FIVE_CLIQUES:
    common = (1 << len(PERMS)) - 1
    for v in [i for i in range(len(PERMS)) if (code >> i) & 1]:
        common &= ADJ[v]
    assert common == 0


def members(mask):
    return [i for i in range(len(PERMS)) if (mask >> i) & 1]


def pair_spectrum(mask):
    ids = members(mask)
    return Counter(DIST[i][j] for i, j in combinations(ids, 2))


for code in MAXIMA:
    assert pair_spectrum(code) == Counter({6: 10})

# Isometry group used here: arbitrary relabeling of the five ranked items,
# together with simultaneous reversal of one-line positions.
RELABELINGS = list(permutations(range(N)))
GROUP_MAPS = []
for relabel in RELABELINGS:
    for reverse in (False, True):
        mapping = []
        for p in PERMS:
            q = tuple(relabel[value] for value in p)
            if reverse:
                q = q[::-1]
            mapping.append(INDEX[q])
        GROUP_MAPS.append(mapping)

assert len(GROUP_MAPS) == 240
for mapping in GROUP_MAPS:
    for i in range(len(PERMS)):
        for j in range(i + 1, len(PERMS)):
            assert DIST[mapping[i]][mapping[j]] == DIST[i][j]


def transform(mask, mapping):
    out = 0
    work = mask
    while work:
        bit = work & -work
        i = bit.bit_length() - 1
        work -= bit
        out |= 1 << mapping[i]
    return out


seen = set()
ORBITS = []
for code in MAXIMA:
    if code in seen:
        continue
    orbit = {transform(code, mapping) for mapping in GROUP_MAPS}
    assert orbit <= MAXIMUM_SET
    seen |= orbit
    ORBITS.append(orbit)

ORBIT_SIZES = sorted(len(orbit) for orbit in ORBITS)
assert ORBIT_SIZES == [48, 120]
STABILIZERS = sorted(240 // size for size in ORBIT_SIZES)
assert STABILIZERS == [2, 5]


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def is_subgroup(mask):
    ps = {PERMS[i] for i in members(mask)}
    if IDENTITY not in ps:
        return False
    return all(compose(a, b) in ps for a in ps for b in ps)


id_index = INDEX[IDENTITY]
NORMALIZED = [code for code in MAXIMA if (code >> id_index) & 1]
assert len(NORMALIZED) == 7
SUBGROUP_MAXIMA = [code for code in NORMALIZED if is_subgroup(code)]
assert len(SUBGROUP_MAXIMA) == 2

# Each subgroup has order 5 and hence is cyclic.  Its 24 left cosets are
# maximum codes.  The two coset families are disjoint and are precisely the
# 48-element isometry orbit.
def mask_of(ps):
    mask = 0
    for p in ps:
        mask |= 1 << INDEX[p]
    return mask


COSET_FAMILIES = []
for subgroup in SUBGROUP_MAXIMA:
    h = [PERMS[i] for i in members(subgroup)]
    cosets = {mask_of(compose(g, x) for x in h) for g in PERMS}
    assert len(cosets) == 24
    assert cosets <= MAXIMUM_SET
    COSET_FAMILIES.append(cosets)

assert not (COSET_FAMILIES[0] & COSET_FAMILIES[1])
SMALL_ORBIT = next(orbit for orbit in ORBITS if len(orbit) == 48)
assert COSET_FAMILIES[0] | COSET_FAMILIES[1] == SMALL_ORBIT

# The code displayed in Appendix D of Vijayakumaran (2016) is checked
# explicitly and lies in the other, 120-element orbit.
published = [
    (1, 2, 3, 4, 5),
    (3, 5, 1, 4, 2),
    (4, 1, 5, 3, 2),
    (4, 2, 3, 5, 1),
    (5, 2, 1, 4, 3),
]
published = [tuple(value - 1 for value in p) for p in published]
published_mask = mask_of(published)
assert published_mask in MAXIMUM_SET
assert any(published_mask in orbit and len(orbit) == 120 for orbit in ORBITS)
assert not is_subgroup(published_mask)

# Record generators of the two normalized subgroup maxima.
def cycle_string(p):
    visited = [False] * N
    cycles = []
    for start in range(N):
        if visited[start]:
            continue
        cyc = []
        j = start
        while not visited[j]:
            visited[j] = True
            cyc.append(j + 1)
            j = p[j]
        if len(cyc) > 1:
            cycles.append("(" + " ".join(map(str, cyc)) + ")")
    return "".join(cycles) or "()"


generators = []
for subgroup in SUBGROUP_MAXIMA:
    nonidentity = [PERMS[i] for i in members(subgroup) if PERMS[i] != IDENTITY]
    generators.append(cycle_string(nonidentity[0]))
generators.sort()

print(
    "VERIFY_OK "
    f"vertices={len(PERMS)} edges={EDGE_COUNT} "
    f"bk_nodes={BK_NODES} maximal_hist=2:300,3:3120,4:3960,5:168 "
    f"maximum={MAX_SIZE} labeled_maxima={len(MAXIMA)} equidistant_maxima={len(MAXIMA)} "
    f"group_size={len(GROUP_MAPS)} orbits=2 orbit_sizes=48,120 stabilizers=5,2 "
    f"normalized_maxima={len(NORMALIZED)} subgroup_maxima={len(SUBGROUP_MAXIMA)} "
    f"cosets_per_subgroup=24 published_orbit=120 generators={'|'.join(generators)}"
)
