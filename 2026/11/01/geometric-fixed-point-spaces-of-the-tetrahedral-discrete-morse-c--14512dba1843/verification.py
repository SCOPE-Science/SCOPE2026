"""Exact finite certificate checker for geometric fixed points of the tetrahedral
Morse-matching complex. Python 3 standard library only.

Run: python3 verification.py [certificate.json]
"""
import json
import sys
from collections import Counter
from itertools import combinations, permutations

FACES = tuple(range(1, 16))
EDGES = tuple((a, b) for a in FACES for b in FACES
              if a & b == a and b.bit_count() == a.bit_count() + 1)
assert len(FACES) == 15 and len(EDGES) == 28


def transformed_face(p, a):
    return sum(1 << p[i] for i in range(4) if a & (1 << i))


def edge_orbits(p):
    pool = set(EDGES)
    result = []
    while pool:
        z = min(pool)
        orbit = []
        while z not in orbit:
            orbit.append(z)
            z = (transformed_face(p, z[0]), transformed_face(p, z[1]))
        assert z == orbit[0]
        assert set(orbit) <= pool
        pool.difference_update(orbit)
        result.append(tuple(sorted(orbit)))
    return result


def is_matching(edges):
    endpoints = [v for a, b in edges for v in (a, b)]
    return len(set(endpoints)) == len(endpoints)


def is_acyclic_toposort(matching):
    if not is_matching(matching):
        return False
    reversals = set(matching)
    adjacent = {a: [] for a in FACES}
    in_degree = {a: 0 for a in FACES}
    for a, b in EDGES:
        src, dst = (b, a) if (a, b) in reversals else (a, b)
        adjacent[src].append(dst)
        in_degree[dst] += 1
    queue = [x for x in FACES if in_degree[x] == 0]
    visited = 0
    while queue:
        src = queue.pop()
        visited += 1
        for dst in adjacent[src]:
            in_degree[dst] -= 1
            if not in_degree[dst]:
                queue.append(dst)
    return visited == len(FACES)


def is_acyclic_gradient_paths(matching):
    # Independent characterization: a closed Forman V-path occurs at some
    # dimension p. Vertices of the transition digraph are matched lower
    # p-faces; a -> a' when their matched upper (p+1)-face contains a'.
    if not is_matching(matching):
        return False
    by_level = {}
    for a, b in matching:
        by_level.setdefault(a.bit_count(), []).append((a, b))
    for level, pairs in by_level.items():
        targets = {a for a, _ in pairs}
        neighbours = {a: [] for a in targets}
        for a, b in pairs:
            neighbours[a] = [a2 for a2 in targets
                             if a2 != a and a2 & b == a2]
        state = {}
        def visit(x):
            if state.get(x) == 1:
                return False
            if state.get(x) == 2:
                return True
            state[x] = 1
            for y in neighbours[x]:
                if not visit(y):
                    return False
            state[x] = 2
            return True
        if not all(visit(x) for x in targets):
            return False
    return True


def orbit_complex(p):
    atoms = [o for o in edge_orbits(p) if is_acyclic_toposort(o)]
    faces = set()
    for mask in range(1, 1 << len(atoms)):
        matching = tuple(e for j, orbit in enumerate(atoms)
                         if mask & (1 << j) for e in orbit)
        test_a = is_acyclic_toposort(matching)
        test_b = is_acyclic_gradient_paths(matching)
        assert test_a == test_b, ('acyclicity cross-check', p, mask)
        if test_a:
            faces.add(mask)
    for mask in faces:
        for j in range(len(atoms)):
            if mask & (1 << j) and mask != 1 << j:
                assert mask ^ (1 << j) in faces
    return atoms, faces


def simplicial_collapse(faces, pairs):
    current = set(faces)
    for step, (a, b) in enumerate(pairs):
        assert a in current and b in current, ('missing face', step, a, b)
        assert a.bit_count() + 1 == b.bit_count() and a & b == a
        # Free face of a unique maximal coface.
        assert [u for u in current if u != a and u & a == a] == [b] or (
            {u for u in current if u != a and u & a == a} == {b})
        current.remove(a)
        current.remove(b)
    return current


def component_sizes(graph_vertices, graph_edges):
    adjacent = {v: set() for v in graph_vertices}
    for f in graph_edges:
        a, b = [j for j in graph_vertices if f & (1 << j)]
        adjacent[a].add(b)
        adjacent[b].add(a)
    unseen = set(graph_vertices)
    comps = []
    while unseen:
        seed = min(unseen)
        stack = [seed]
        comp = {seed}
        unseen.remove(seed)
        while stack:
            for y in adjacent[stack.pop()]:
                if y in unseen:
                    unseen.remove(y)
                    comp.add(y)
                    stack.append(y)
        comps.append(comp)
    return adjacent, comps


def run(certificate_path):
    with open(certificate_path, encoding='utf-8') as f:
        data = json.load(f)
    names = ['transposition', 'double_transposition', 'three_cycle', 'four_cycle']
    assert list(data['classes'].keys()) == sorted(names) or set(data['classes']) == set(names)
    expected = {
        'transposition': (10, [10, 36, 56, 36, 8]),
        'double_transposition': (8, [8, 8]),
        'three_cycle': (3, [3, 3, 1]),
        'four_cycle': (0, []),
    }
    for name in names:
        entry = data['classes'][name]
        p = tuple(entry['permutation'])
        assert tuple(sorted(p)) == (0, 1, 2, 3)
        os, faces = orbit_complex(p)
        assert entry['orbit_vertices'] == [[list(e) for e in o] for o in os]
        f = Counter(x.bit_count()-1 for x in faces)
        fvec = [f.get(k, 0) for k in range(max(f)+1)] if f else []
        assert (len(os), fvec) == expected[name], (name, len(os), fvec)
        assert entry['face_vector'] == fvec
        assert entry['simplices_count'] == len(faces)
        if name == 'transposition':
            assert len(entry['collapse_pairs']) == 60
            survived = simplicial_collapse(faces, entry['collapse_pairs'])
            survivors = {j for j in range(len(os)) if 1 << j in survived}
            assert sorted(survivors) == entry['survivor_vertices']
            opposite = [tuple(pair) for pair in entry['octahedral_opposite_pairs']]
            assert len(opposite) == 3
            assert sorted(i for pair in opposite for i in pair) == sorted(survivors)
            # The remaining faces are exactly all nonempty subsets choosing
            # at most one vertex from each opposite pair: boundary of octahedron.
            target = set()
            for mask in range(1, 1 << len(os)):
                used = {j for j in range(len(os)) if mask & (1 << j)}
                if used <= survivors and all(len(used & set(pair)) <= 1 for pair in opposite):
                    target.add(mask)
            assert survived == target and len(target) == 26
            facets = {s for s in survived if not any(t != s and t & s == s for t in survived)}
            assert sorted(facets) == entry['survivor_facets'] and len(facets) == 8
        elif name == 'double_transposition':
            vertices = set(range(len(os)))
            assert all(x.bit_count() <= 2 for x in faces)
            adj, comps = component_sizes(vertices, {x for x in faces if x.bit_count() == 2})
            assert sorted(map(len, comps)) == [4, 4]
            assert all(len(adj[j]) == 2 for j in vertices)
        elif name == 'three_cycle':
            assert faces == set(range(1, 8))
        elif name == 'four_cycle':
            assert not os and not faces
    # All conjugates have the same orbit-model combinatorial type.
    for p in permutations(range(4)):
        found = (lambda cyc: None)(p)
        # Every automorphism is conjugate to one of the representatives:
        # compare permutation cycle-length partitions.
        seen = set(); cycle_lengths = []
        for a in range(4):
            if a not in seen:
                x = a; k = 0
                while x not in seen:
                    seen.add(x); k += 1; x = p[x]
                cycle_lengths.append(k)
        cycle_type = tuple(sorted(cycle_lengths))
        if cycle_type == (1, 1, 1, 1):
            continue  # identity fixed space is the full complex
        typ = {(1,1,2):'transposition',(2,2):'double_transposition',
               (1,3):'three_cycle',(4,):'four_cycle'}[cycle_type]
        a, b = orbit_complex(p)
        assert (len(a), [sum(x.bit_count() == d+1 for x in b)
                         for d in range(max((x.bit_count() for x in b), default=0))]) == expected[typ]
    print('VERIFY_OK: all 24 permutations; 60 exact free-face collapses; 2 four-cycles; one filled triangle; one empty fixed set')


if __name__ == '__main__':
    run(sys.argv[1] if len(sys.argv) == 2 else 'certificate.json')
