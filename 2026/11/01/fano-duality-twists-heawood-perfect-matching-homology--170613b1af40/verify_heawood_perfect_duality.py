#!/usr/bin/env python3
"""Exhaustive proof checks for Fano-incidence matching-complex symmetry.

Uses only Python standard library.  No external files or software are required.
"""
from collections import Counter, defaultdict, deque
from itertools import product
from math import lcm

V = range(1, 8)
parity = lambda x: x.bit_count() % 2
edges = tuple((p, q) for p in V for q in V if parity(p & q) == 0)
edge_id = {e: i for i, e in enumerate(edges)}
assert len(edges) == 21
assert Counter(p for p, q in edges) == Counter({p: 3 for p in V})
assert Counter(q for p, q in edges) == Counter({q: 3 for q in V})

# All 7-edge perfect matchings, by exhaustive point-to-line injection.
perfect_facets = []
def match_point(p, used_lines, es):
    if p == 8:
        perfect_facets.append(sum(1 << k for k in es))
        return
    for q in V:
        if not (used_lines >> q) & 1 and (p, q) in edge_id:
            match_point(p + 1, used_lines | (1 << q), es + (edge_id[(p, q)],))
match_point(1, 0, ())
assert len(perfect_facets) == 24 and len(set(perfect_facets)) == 24

perfect_faces = {0}
for facet in perfect_facets:
    sub = facet
    while True:
        perfect_faces.add(sub)
        if not sub:
            break
        sub = (sub - 1) & facet
assert len(perfect_faces) == 2202

# All ordinary matchings; independent face recursion, not using perfect facets.
ordinary_faces = {0}
for j, (p, q) in enumerate(edges):
    for face in tuple(ordinary_faces):
        if all(p != edges[k][0] and q != edges[k][1]
               for k in range(21) if (face >> k) & 1):
            ordinary_faces.add(face | (1 << j))
assert len(ordinary_faces) == 3462 and perfect_faces <= ordinary_faces
ordinary_facets = [f for f in ordinary_faces if all((f | (1 << j)) not in ordinary_faces
                     for j in range(21) if not f & (1 << j))]
assert Counter(f.bit_count() for f in ordinary_facets) == {5: 42, 6: 168, 7: 24}

def f_vector(faces):
    return tuple(sum(f.bit_count() == k for f in faces) for k in range(1, 8))
assert f_vector(perfect_faces) == (21, 168, 560, 756, 504, 168, 24)
assert f_vector(ordinary_faces) == (21, 168, 644, 1218, 1050, 336, 24)

# Staged element-toggle Morse matching on nonempty perfect-complex faces.
remaining = set(perfect_faces) - {0}
pairs = []
for j in range(21):
    bit = 1 << j
    ps = [(f, f | bit) for f in remaining
          if not f & bit and (f | bit) in remaining]
    for low, high in ps:
        remaining.remove(low)
        remaining.remove(high)
    pairs.extend(ps)
critical = Counter(f.bit_count() - 1 for f in remaining)
assert len(pairs) == 1092 and critical == {0: 1, 2: 16}

# Direct Hasse-graph acyclicity check, including every incidence.
paired = set(pairs)
nonempty = perfect_faces - {0}
indeg = {x: 0 for x in nonempty}
outs = defaultdict(list)
incidences = 0
for high in nonempty:
    sub = high
    while sub:
        bit = sub & -sub
        low = high ^ bit
        if low:
            if (low, high) in paired:
                a, b = low, high
            else:
                a, b = high, low
            outs[a].append(b)
            indeg[b] += 1
            incidences += 1
        sub ^= bit
Q = deque(f for f, deg in indeg.items() if deg == 0)
visited = 0
while Q:
    f = Q.popleft()
    visited += 1
    for v in outs[f]:
        indeg[v] -= 1
        if indeg[v] == 0:
            Q.append(v)
assert visited == len(nonempty) == 2201 and incidences == 8736

# Rational homology dimensions of the ordinary matching complex.
# Compute mod-2 ranks of all six differentials; chain identities and integral
# rank inequalities force the same ranks over Q in this special complex.
def rank_mod2_boundary(faces, n):
    row_faces = sorted(f for f in faces if f.bit_count() == n)
    col_faces = sorted(f for f in faces if f.bit_count() == n + 1)
    rows = {f: i for i, f in enumerate(row_faces)}
    pivots = {}
    for f in col_faces:
        v = 0
        sub = f
        while sub:
            bit = sub & -sub
            v ^= (1 << rows[f ^ bit])
            sub ^= bit
        while v:
            b = v.bit_length() - 1
            if b in pivots:
                v ^= pivots[b]
            else:
                pivots[b] = v
                break
    return len(pivots)
ranks = tuple(rank_mod2_boundary(ordinary_faces, n) for n in range(1, 7))
assert ranks == (20, 148, 496, 722, 312, 24), ranks
# Degree 0/1 lower bound and rank<=dim chains bound are saturated,
# propagating to 4, and high-degree ranks are also saturated backwards.
assert ranks[0] == f_vector(ordinary_faces)[0] - 1
for i in range(1, 4):
    assert ranks[i - 1] + ranks[i] == f_vector(ordinary_faces)[i]
assert ranks[-1] == f_vector(ordinary_faces)[-1]
assert ranks[-2] + ranks[-1] == f_vector(ordinary_faces)[-2]
assert f_vector(ordinary_faces)[4] - ranks[3] - ranks[4] == 16

# GL(3,2) and its Fano duality coset.
def act(A, x):
    return ((A[0] if x & 1 else 0) ^
            (A[1] if x & 2 else 0) ^
            (A[2] if x & 4 else 0))
def inverse(A):
    return tuple(next(x for x in range(8) if act(A, x) == 1 << i)
                 for i in range(3))
def transpose(A):
    return tuple(sum((parity(A[j] & (1 << i)) << j)
                     for j in range(3)) for i in range(3))
GL = [A for A in product(V, repeat=3)
      if len({act(A, x) for x in V}) == 7]
assert len(GL) == 168

def cycles(perm):
    used = set()
    orbits = []
    for x in range(len(perm)):
        if x in used:
            continue
        o = []
        y = x
        while y not in used:
            used.add(y)
            o.append(y)
            y = perm[y]
        orbits.append(tuple(o))
    return tuple(orbits)

def char_fixed_faces(faces, perm):
    # Reduced Lefschetz: trace on the unique reduced homology degree.
    # Includes empty-face term -1.
    ans = -1
    for f in faces:
        if not f:
            continue
        mapped = 0
        count = 0
        used = set()
        for k in range(21):
            if f >> k & 1:
                mapped |= 1 << perm[k]
        if mapped != f:
            continue
        for k in range(21):
            if (f >> k & 1) and k not in used:
                j = k
                while j not in used:
                    used.add(j)
                    j = perm[j]
                count += 1
        ans += 1 if count % 2 else -1
    return ans

def char_orbit_subsets(faces, perm):
    # Independent calculation: each g-invariant face is a union of edge orbits.
    # A face in the perfect complex lies inside one of the 24 maximal matchings.
    orbit_masks = []
    for orb in cycles(perm):
        orbit_masks.append(sum(1 << k for k in orb))
    invariant = {0}
    for facet in (perfect_facets if faces is perfect_faces else
                  ordinary_facets):
        allowed = [j for j, orbmask in enumerate(orbit_masks)
                   if (facet & orbmask) == orbmask]
        for choose in range(1 << len(allowed)):
            s = 0
            for t, j in enumerate(allowed):
                if choose >> t & 1:
                    s |= 1 << j
            invariant.add(s)
    return -sum((-1) ** s.bit_count() for s in invariant)

# Exhaust all symmetries, separately checking both equivariant Euler formulas.
counts = Counter()
character_sums = [0, 0]
character_tables = [{}, {}]
for A in GL:
    B = transpose(inverse(A))
    for swap in (0, 1):
        if not swap:
            perm = tuple(edge_id[(act(A, p), act(B, q))] for p, q in edges)
            vperm = tuple(act(A, p) - 1 for p in V) + tuple(7 + act(B, q) - 1 for q in V)
        else:
            perm = tuple(edge_id[(act(B, q), act(A, p))] for p, q in edges)
            vperm = tuple(7 + act(A, p) - 1 for p in V) + tuple(act(B, q) - 1 for q in V)
        assert len(set(perm)) == 21
        assert len(set(vperm)) == 14
        assert all(sum(1 << perm[j] for j in range(21) if f >> j & 1) in perfect_faces
                   for f in perfect_facets)
        order = 1
        for cycle in cycles(vperm):
            order = lcm(order, len(cycle))
        cp = char_fixed_faces(perfect_faces, perm)
        co = char_fixed_faces(ordinary_faces, perm)
        assert cp == char_orbit_subsets(perfect_faces, perm)
        assert co == char_orbit_subsets(ordinary_faces, perm)
        assert cp == ((-1) ** swap) * co
        key = (swap, order)
        if key in character_tables[0]:
            assert character_tables[0][key] == cp
            assert character_tables[1][key] == co
        character_tables[0][key] = cp
        character_tables[1][key] = co
        counts[key] += 1
        character_sums[0] += cp
        if not swap:
            character_sums[1] += cp

expected = {
    (0, 1): (1, 16, 16),
    (0, 2): (21, 0, 0),
    (0, 3): (56, 1, 1),
    (0, 4): (42, 0, 0),
    (0, 7): (48, 2, 2),
    (1, 2): (28, -4, 4),
    (1, 6): (56, -1, 1),
    (1, 8): (84, 0, 0),
}
assert set(counts) == set(expected) and sum(counts.values()) == 336
for k, (num, cp, co) in expected.items():
    assert counts[k] == num and character_tables[0][k] == cp and character_tables[1][k] == co
assert character_sums == [0, 168]
print('HEAWOOD_PERFECT_DUALITY_VERIFY_OK')
print('perfect_matchings', len(perfect_facets), 'complex_faces', len(perfect_faces)-1)
print('perfect_f_vector', f_vector(perfect_faces))
print('ordinary_f_vector', f_vector(ordinary_faces))
print('ordinary_mod2_boundary_ranks', ranks)
print('Morse_pairs', len(pairs), 'critical', dict(sorted(critical.items())),
      'Hasse_incidences', incidences, 'DAG_vertices', visited)
print('aut_count', sum(counts.values()), 'color_preserving', sum(n for (s, order), n in counts.items() if not s))
for k in sorted(expected):
    print('color_swap', k[0], 'order', k[1], 'count', counts[k],
          'perfect_H2_trace', character_tables[0][k],
          'ordinary_H4_trace', character_tables[1][k])
print('perfect_fixed_dim_full', character_sums[0]//336,
      'perfect_fixed_dim_preserving', character_sums[1]//168)
print('perfect_module_is_ordinary_module_tensor_bipartition_sign', True)
