#!/usr/bin/env python3
from itertools import combinations

L = 3
Q = tuple(range(-2 * L, 2 * L + 1))
CORE = tuple(range(-L, L + 1))

def is_vertex(D):
    D = tuple(sorted(D))
    separated = all(abs(a - b) > L for i, a in enumerate(D) for b in D[i+1:])
    covering = all(any(abs(x - a) <= L for a in D) for x in CORE)
    return separated and covering

def witness_labels(D, E):
    D, E = set(D), set(E)
    out = []
    qset = set(Q)
    for g in (-1, 1):
        gQ = {x + g for x in Q}
        lhs = D & gQ
        rhs = {g + x for x in E} & qset
        if lhs == rhs:
            out.append(g)
    return tuple(out)

vertices = []
for mask in range(1 << len(Q)):
    D = tuple(Q[i] for i in range(len(Q)) if (mask >> i) & 1)
    if is_vertex(D):
        vertices.append(D)

index = {D: i for i, D in enumerate(vertices)}
edges = {}
adj = [set() for _ in vertices]
for i, D in enumerate(vertices):
    for j in range(i + 1, len(vertices)):
        E = vertices[j]
        labs = witness_labels(D, E)
        if labs:
            edges[(i, j)] = labs
            adj[i].add(j)
            adj[j].add(i)

assert len(vertices) == 59
assert len(edges) == 75
assert all(len(labs) == 1 for labs in edges.values())

def direction(u, v):
    if u < v:
        return edges[(u, v)][0]
    return -edges[(v, u)][0]

def canonical_cycle(c):
    c = tuple(c)
    reps = []
    for seq in (c, tuple(reversed(c))):
        for k in range(4):
            reps.append(seq[k:] + seq[:k])
    return min(reps)

cycles = set()
for a in range(len(vertices)):
    for b in adj[a]:
        for c in adj[b]:
            if c == a:
                continue
            for d in adj[c]:
                if d in (a, b):
                    continue
                if a in adj[d]:
                    cycles.add(canonical_cycle((a, b, c, d)))

assert len(cycles) == 4
cycle_data = []
for cyc in sorted(cycles):
    seq = cyc + (cyc[0],)
    dirs = tuple(direction(u, v) for u, v in zip(seq[:-1], seq[1:]))
    cycle_data.append((cyc, dirs, sum(dirs)))

bad = [x for x in cycle_data if x[2] != 0]
assert len(bad) == 1
assert sorted(abs(x[2]) for x in bad) == [4]

D0 = (-5, -1, 3)
D1 = (-4, 0, 4)
D2 = (-3, 1, 5)
D3 = (-6, -2, 2, 6)
explicit = (index[D0], index[D1], index[D2], index[D3])
assert all(direction(u, v) == -1 for u, v in zip(explicit, explicit[1:] + explicit[:1]))
assert sum(direction(u, v) for u, v in zip(explicit, explicit[1:] + explicit[:1])) == -4
assert canonical_cycle(explicit) == bad[0][0]

print("VERIFY_OK")
print("vertices=59")
print("edges=75")
print("simple_4_cycles=4")
print("bad_canonical_4_cycles=1")
print("exceptional_cycle=" + repr((D0, D1, D2, D3)))
print("exceptional_directions=(-1,-1,-1,-1)")
print("exceptional_sum=-4")
