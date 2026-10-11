#!/usr/bin/env python3
"""Finite reproducibility checker for the Morse complex of K_{2,4}."""
from collections import Counter, defaultdict, deque
from itertools import product, permutations

N = 4
EDGES = tuple((a, 2 + j) for a in range(2) for j in range(N))
EDGE_INDEX = {e: k for k, e in enumerate(EDGES)}
FACES = set()
for choices in product((0, 1, 2), repeat=len(EDGES)):
    used_sources, directed, vertices = set(), {}, []
    for k, state in enumerate(choices):
        if state == 0:
            continue
        source = EDGES[k][state - 1]
        target = EDGES[k][2 - state]
        if source in used_sources:
            break
        used_sources.add(source)
        directed[source] = target
        vertices.append(2*k + state - 1)
    else:
        cyclic = False
        for start in directed:
            seen, current = set(), start
            while current in directed and current not in seen:
                seen.add(current)
                current = directed[current]
            if current in seen:
                cyclic = True
                break
        if not cyclic:
            FACES.add(sum(1 << t for t in vertices))
assert len(FACES) == 945 and 0 in FACES
nonempty = FACES - {0}
f_vector = tuple(sum(f.bit_count() == k for f in nonempty) for k in range(1, 6))
assert f_vector == (16, 96, 272, 368, 192), f_vector

# Lexicographic face-toggle matching; empty-face pair is omitted to retain a critical vertex.
remaining = set(FACES)
pairs = []
for v in range(16):
    for f in sorted(remaining):
        if f & (1 << v):
            continue
        t = f | (1 << v)
        if t in remaining:
            remaining.remove(f)
            remaining.remove(t)
            pairs.append((f, t))
assert len(pairs) == 465
assert Counter(f.bit_count()-1 for f in remaining) == {4:15}
matched = set(p for p in pairs if p[0] != 0)
assert len(matched) == 464
critical = set(nonempty)
for small, big in matched:
    critical.remove(small)
    critical.remove(big)
assert Counter(f.bit_count()-1 for f in critical) == {0:1, 4:15}

# Check every cover and topologically sort all directed Hasse edges after reversal.
adjacency = {f: [] for f in nonempty}
indegree = {f: 0 for f in nonempty}
covers = 0
for big in nonempty:
    for v in range(16):
        if not big & (1 << v):
            continue
        small = big ^ (1 << v)
        if small == 0:
            continue
        source, target = (small,big) if (small,big) in matched else (big,small)
        adjacency[source].append(target)
        indegree[target] += 1
        covers += 1
assert covers == 3440
queue = deque(f for f, degree in indegree.items() if degree == 0)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for g in adjacency[f]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)
assert visited == len(nonempty), 'The discrete-Morse matching is cyclic'

# Enumerate every automorphism in S2 x S4; obtain its trace from signed simplex orbits.
def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j)
            j = p[j]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths))

expected = {
    0: {(1,1,1,1):15, (1,1,2):-3, (1,3):0, (2,2):-1, (4,):1},
    1: {(1,1,1,1):3, (1,1,2):1, (1,3):0, (2,2):-5, (4,):1},
}
trace_samples = {}
for swap in (0,1):
    for p in permutations(range(4)):
        vertex_map = {a:(1-a if swap else a) for a in range(2)}
        vertex_map.update({2+j:2+p[j] for j in range(4)})
        atom_map = []
        for k, (a,b) in enumerate(EDGES):
            edge_idx = EDGE_INDEX[(vertex_map[a],vertex_map[b])]
            for endpoint in (a,b):
                side = 0 if vertex_map[endpoint] == vertex_map[a] else 1
                atom_map.append(2*edge_idx + side)
        assert sorted(atom_map) == list(range(16))
        trace_by_dimension = Counter()
        for mask in nonempty:
            atoms = [i for i in range(16) if mask & (1 << i)]
            image = [atom_map[i] for i in atoms]
            if sum(1 << j for j in image) != mask:
                continue
            inversions = sum(image[i] > image[j] for i in range(len(image)) for j in range(i+1,len(image)))
            trace_by_dimension[len(atoms)-1] += (-1)**inversions
        reduced_lefschetz = sum((-1)**k*v for k,v in trace_by_dimension.items()) - 1
        # Only reduced H_4 is nonzero, so the reduced Lefschetz trace is the H_4 trace.
        typ = cycle_type(p)
        assert reduced_lefschetz == expected[swap][typ], (swap,typ,reduced_lefschetz)
        trace_samples[(swap,p)] = reduced_lefschetz
assert len(trace_samples) == 48

# Rational irreducible decomposition under S4, separately in +/- eigenspaces of S2.
irreps = {
    'sign': {(1,1,1,1):1,(1,1,2):-1,(1,3):1,(2,2):1,(4,):-1},
    'standard': {(1,1,1,1):3,(1,1,2):1,(1,3):0,(2,2):-1,(4,):-1},
    'sign_standard': {(1,1,1,1):3,(1,1,2):-1,(1,3):0,(2,2):-1,(4,):1},
    'two_two': {(1,1,1,1):2,(1,1,2):0,(1,3):-1,(2,2):2,(4,):0},
}
for typ in expected[0]:
    plus = (expected[0][typ] + expected[1][typ]) // 2
    minus = (expected[0][typ] - expected[1][typ]) // 2
    assert plus == irreps['standard'][typ] + 2*irreps['sign_standard'][typ]
    assert minus == irreps['sign'][typ] + irreps['sign_standard'][typ] + irreps['two_two'][typ]
assert expected[0][(1,1,1,1)] == 15
print('VERIFY_OK faces=944 covers=3440 matching_pairs=464 critical={0:1,4:15} automorphisms=48')
