#!/usr/bin/env python3
"""Reproduce a finite integral homotopy and filtration certificate for Paley(13).

Usage: python check_paley13.py [CERTIFICATE.json]
Dependencies: Python 3 standard library only.
"""
import collections
import functools
import json
import sys
from pathlib import Path

CERT_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('CERTIFICATE.json')
cert = json.loads(CERT_PATH.read_text(encoding='utf-8'))
N = cert['graph_modulus']
assert N == 13
Q = set(cert['quadratic_residues'])
assert Q == {i * i % N for i in range(1, N)} == {1, 3, 4, 9, 10, 12}
ALL = (1 << N) - 1
ADJ = [sum(1 << j for j in range(N) if (i - j) % N in Q) for i in range(N)]


def bits(s):
    while s:
        b = s & -s
        yield b.bit_length() - 1
        s ^= b


def is_r_independent(s, r):
    unseen = s
    while unseen:
        first = unseen & -unseen
        component = 0
        frontier = first
        while frontier:
            v_bit = frontier & -frontier
            frontier ^= v_bit
            if component & v_bit:
                continue
            component |= v_bit
            if component.bit_count() > r:
                return False
            v = v_bit.bit_length() - 1
            frontier |= ADJ[v] & s & ~component
        unseen &= ~component
    return True


def is_r_independent_union_find(s, r):
    vs = list(bits(s))
    parent = {x: x for x in vs}

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            x, y = vs[i], vs[j]
            if ADJ[x] >> y & 1:
                parent[find(x)] = find(y)
    return all(a <= r for a in collections.Counter(find(x) for x in vs).values())


def face_bound(s):
    """Integral simplicial boundary; sorted vertex orientation."""
    out = {}
    for idx, v in enumerate(bits(s)):
        out[s ^ (1 << v)] = (-1) ** idx
    return out


def boundary(chain):
    out = collections.Counter()
    for s, coeff in chain.items():
        for t, a in face_bound(s).items():
            out[t] += coeff * a
    return {s: c for s, c in out.items() if c}


faces = {}
for r in (1, 2, 3):
    faces[r] = {s for s in range(ALL + 1) if is_r_independent(s, r)}
    assert len(faces[r]) == cert['expected_face_counts'][str(r)]
    assert all(is_r_independent_union_find(s, r) == (s in faces[r]) for s in range(ALL + 1))
    assert all((s ^ (1 << v)) in faces[r] for s in faces[r] for v in bits(s))
assert faces[1] < faces[2] < faces[3]
assert all(ADJ[v].bit_count() == 6 for v in range(N))
F1, F2, F3 = faces[1], faces[2], faces[3]

# The ordinary independence complex is a closed, orientable torus.
triangles = sorted(s for s in F1 if s.bit_count() == 3)
edges = sorted(s for s in F1 if s.bit_count() == 2)
assert len(triangles) == 26 and len(edges) == 39
assert not any(s.bit_count() > 3 for s in F1)
# Connectivity of the one-skeleton, independent of the link checks.
neighbor = collections.defaultdict(set)
for e in edges:
    x, y = list(bits(e))
    neighbor[x].add(y); neighbor[y].add(x)
seen = {0}
stack = [0]
while stack:
    x = stack.pop()
    for y in neighbor[x] - seen:
        seen.add(y); stack.append(y)
assert seen == set(range(N))
incidence = collections.Counter(e for t in triangles for e in face_bound(t))
assert set(incidence) == set(edges) and set(incidence.values()) == {2}
# Every vertex link is a 6-cycle, without additional edges.
for v in range(N):
    link_edges = [t ^ (1 << v) for t in triangles if t >> v & 1]
    link_vertices = {x for e in link_edges for x in bits(e)}
    incidence_at_link = collections.Counter(x for e in link_edges for x in bits(e))
    assert len(link_vertices) == len(link_edges) == 6
    assert set(incidence_at_link.values()) == {2}
    neighbor = collections.defaultdict(set)
    for e in link_edges:
        x, y = list(bits(e)); neighbor[x].add(y); neighbor[y].add(x)
    reached = {next(iter(link_vertices))}
    frontier = list(reached)
    while frontier:
        w = frontier.pop()
        for z in neighbor[w] - reached:
            reached.add(z); frontier.append(z)
    assert reached == link_vertices

cycle_2 = dict(cert['torus_oriented_2_cycle'])
assert set(cycle_2) == set(triangles) and set(cycle_2.values()) <= {-1, 1}
assert not boundary(cycle_2)
assert 13 - 39 + 26 == 0
# With no degree-three faces, a nonzero integral 2-cycle is nonbounding in F1.

fill_3 = dict(cert['torus_filling_3_chain'])
assert len(fill_3) == 26
assert set(fill_3.values()) <= {-1, 1}
assert all(t in F2 and t.bit_count() == 4 for t in fill_3)
assert boundary(fill_3) == cycle_2

# A vertex-toggle matching on all 313 augmented faces of Ind_2.
order = cert['matching_order']
assert sorted(order) == list(range(N))
unmatched = set(F2)
matched_up = {}
for v in order:
    bit = 1 << v
    for face in sorted(unmatched):
        larger = face | bit
        if not face & bit and larger in unmatched:
            unmatched.remove(face)
            unmatched.remove(larger)
            matched_up[face] = larger
assert len(matched_up) == 155
assert sum((1 << v) in matched_up.values() for v in range(N)) == 1
assert (0 in matched_up and matched_up[0] == (1 << order[0]))
# Discard the augmented empty face and its pair, keeping that vertex critical.
paired_without_empty = {lo: hi for lo, hi in matched_up.items() if lo != 0}
critical_ordinary = set(F2) - {0} - set(paired_without_empty) - set(paired_without_empty.values())
crit_expected = {int(k): set(v) for k, v in cert['expected_critical_nonempty'].items()}
assert {dim: {s for s in critical_ordinary if s.bit_count() - 1 == dim}
        for dim in crit_expected} == crit_expected
assert len(critical_ordinary) == 4

# Exhaustive directed face-poset acyclicity: matching arrows go upward.
nexts = collections.defaultdict(list)
indegree = collections.Counter()
incidence_count = 0
for face in F2:
    if face == 0:
        continue
    for v in range(N):
        larger = face | (1 << v)
        if larger == face or larger not in F2:
            continue
        if paired_without_empty.get(face) == larger:
            src, dst = face, larger
        else:
            src, dst = larger, face
        nexts[src].append(dst)
        indegree[dst] += 1
        incidence_count += 1
ordinary = F2 - {0}
frontier = collections.deque(s for s in ordinary if indegree[s] == 0)
visited = 0
while frontier:
    s = frontier.popleft()
    visited += 1
    for t in nexts[s]:
        indegree[t] -= 1
        if indegree[t] == 0:
            frontier.append(t)
assert visited == len(ordinary) == 312
assert incidence_count == 897

# Signed gradient-path reduction for the Morse differential.
upper = set(matched_up.values())
@functools.lru_cache(maxsize=None)
def project(s):
    if s in unmatched:
        return {s: 1}
    if s in upper:
        return {}
    tau = matched_up[s]
    eps = face_bound(tau)[s]
    total = collections.Counter()
    for t, coeff in face_bound(tau).items():
        if t == s:
            continue
        for c, val in project(t).items():
            total[c] -= eps * coeff * val
    return {c: a for c, a in total.items() if a}

morsematrix = {}
for uppercell in sorted(crit_expected[3]):
    bnd = collections.Counter()
    for s, a in face_bound(uppercell).items():
        for c, coeff in project(s).items():
            bnd[c] += a * coeff
    morsematrix[uppercell] = {c: a for c, a in bnd.items() if a}
assert all(b == {} for b in morsematrix.values())

# Check purity: every facet of Ind_2 is a tetrahedron.
facets2 = {s for s in F2 if not any((s | (1 << v)) in F2 for v in range(N) if not s >> v & 1)}
assert len(facets2) == 78 and all(s.bit_count() == 4 for s in facets2)

# Construct a literal elementary simplicial collapse from Ind_3 to Ind_2.
remaining = set(F3)
relative = F3 - F2
assert len(relative) == 364
collapse_sequence = []
while remaining != F2:
    candidates = []
    for lo in remaining - F2:
        cofaces = [lo | (1 << v) for v in range(N)
                   if not lo >> v & 1 and lo | (1 << v) in remaining]
        if len(cofaces) != 1:
            continue
        hi = cofaces[0]
        if hi not in F2 and all((hi | (1 << v)) not in remaining
                                for v in range(N) if not hi >> v & 1):
            candidates.append((lo, hi))
    assert candidates, 'relative elementary-collapse process stalled'
    lo, hi = min(candidates)
    assert lo in remaining and hi in remaining
    remaining.remove(lo)
    remaining.remove(hi)
    collapse_sequence.append((lo, hi))
assert len(collapse_sequence) == cert['expected_retracted_pairs'] == 182

# Independent simplicial homology over several characteristics.
def rank_mod_prime(column_faces, row_faces, prime):
    rows = {s: idx for idx, s in enumerate(row_faces)}
    pivots = {}
    for cell in column_faces:
        a = {rows[s]: v % prime for s, v in face_bound(cell).items() if v % prime}
        while a:
            pivot = max(a)
            if pivot not in pivots:
                inv = pow(a[pivot], -1, prime)
                pivots[pivot] = {k: (x * inv) % prime for k, x in a.items()}
                break
            scale = a[pivot]
            for i, val in pivots[pivot].items():
                a[i] = (a.get(i, 0) - scale * val) % prime
                if a[i] == 0:
                    del a[i]
    return len(pivots)

expected_betti = {1: {0: 1, 1: 2, 2: 1},
                  2: {0: 1, 2: 1, 3: 2},
                  3: {0: 1, 2: 1, 3: 2}}
for r in (1, 2, 3):
    bydim = {d: sorted(s for s in faces[r] if s.bit_count() == d + 1)
             for d in range(N)}
    for prime in (2, 3, 5):
        rank = {k: rank_mod_prime(bydim[k], bydim[k - 1], prime)
                for k in range(1, N) if bydim[k]}
        betti = {k: len(bydim[k]) - rank.get(k, 0) - rank.get(k + 1, 0)
                 for k in range(N)}
        assert {k: b for k, b in betti.items() if b} == expected_betti[r]

print('PALEY13_HIGHER_INDEPENDENCE_AND_NULL_INCLUSION_OK')
print('face_counts 1=79 2=313 3=677; torus_2_cycle=26; filling_3_chain=26')
print('morse_critical_ind2={0:1,2:1,3:2}; matched_pairs=154; hasse_incidence=897; acyclic=yes')
print('integral_Morse_boundary_3_to_2=[0,0]')
print('relative_elementary_collapse Ind3_to_Ind2 pairs=182; remaining_Ind2_faces=313')
print('inclusion_H2(Ind1_to_Ind2)=zero; Betti_stages_1_2_3=PASS (mod 2,3,5)')
print('Ind2_pure_3_dimensional_and_nonshellable=yes')
