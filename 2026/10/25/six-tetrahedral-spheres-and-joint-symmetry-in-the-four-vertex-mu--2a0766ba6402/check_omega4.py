#!/usr/bin/env python3
"""Finite reproducibility checks for the four-vertex cycle-free chessboard complex.

No external packages required. Run: python3 check_omega4.py
"""
from collections import defaultdict
from itertools import combinations, permutations

N = 4
V = tuple(range(N))
ARCS = tuple((a, b) for a in V for b in V if a != b)


def simple_multipath(edges):
    if len({a for a, b in edges}) != len(edges):
        return False
    if len({b for a, b in edges}) != len(edges):
        return False
    next_vertex = dict(edges)
    for start in next_vertex:
        seen = set()
        x = start
        while x in next_vertex:
            if x in seen:
                return False
            seen.add(x)
            x = next_vertex[x]
    return True


FACES = {k: {frozenset(es) for es in combinations(ARCS, k)
             if simple_multipath(es)} for k in (1, 2, 3)}
assert tuple(len(FACES[k]) for k in (1, 2, 3)) == (12, 36, 24)

# The six sets of four consecutive arcs of an oriented Hamiltonian circuit.
CYCLES = {
    frozenset((p[i], p[(i + 1) % N]) for i in range(N))
    for p in permutations(V)
}
assert len(CYCLES) == 6
for t in FACES[3]:
    assert sum(t <= c for c in CYCLES) == 1
for e in FACES[2]:
    assert sum(e <= c for c in CYCLES) == 1
assert all({frozenset(t) for t in combinations(c, 3)} <= FACES[3]
           for c in CYCLES)
INCIDENCES = {(c, a) for c in CYCLES for a in c}
assert len(INCIDENCES) == 24

# Connectivity of the incidence graph, with bipartite nodes ('c',c),('a',arc).
adj = defaultdict(set)
for c, a in INCIDENCES:
    u, v = ('c', c), ('a', a)
    adj[u].add(v)
    adj[v].add(u)
start = ('c', next(iter(CYCLES)))
seen, todo = {start}, [start]
while todo:
    for node in adj[todo.pop()]:
        if node not in seen:
            seen.add(node)
            todo.append(node)
assert len(seen) == 18
assert len(INCIDENCES) - len(seen) + 1 == 7


def class_type(p):
    seen, lens = set(), []
    for i in V:
        if i not in seen:
            j, ln = i, 0
            while j not in seen:
                seen.add(j)
                j, ln = p[j], ln + 1
            lens.append(ln)
    return tuple(sorted(lens, reverse=True))


def sign(order):
    return (-1) ** sum(order[i] > order[j]
                       for i in range(len(order))
                       for j in range(i + 1, len(order)))


def character(p, swap):
    def act(a):
        i, j = a
        return (p[j], p[i]) if swap else (p[i], p[j])

    fixed_cycles = [c for c in CYCLES if frozenset(map(act, c)) == c]
    trace2 = 0
    for c in fixed_cycles:
        baseline = sorted(c)
        pos = {a: i for i, a in enumerate(baseline)}
        trace2 += sign([pos[act(a)] for a in baseline])

    fixed_arcs = sum(act(a) == a for a in ARCS)
    fixed_inc = sum(act(a) == a for c in fixed_cycles for a in c)
    trace1 = fixed_inc - len(fixed_cycles) - fixed_arcs + 1
    return trace1, trace2


CHARACTERS = {}
for p in permutations(V):
    for swap in (0, 1):
        key = (class_type(p), swap)
        val = character(p, swap)
        assert key not in CHARACTERS or CHARACTERS[key] == val
        CHARACTERS[key] = val

ORDER = [(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]
SIZES = [1, 6, 3, 8, 6]
EXPECTED_H1 = {0: (7, -1, -1, 1, -1), 1: (1, -3, 1, 1, 1)}
EXPECTED_H2 = {0: (6, 0, 2, 0, -2), 1: (0, 2, -4, 0, 0)}
for swap in (0, 1):
    assert tuple(CHARACTERS[(ct, swap)][0] for ct in ORDER) == EXPECTED_H1[swap]
    assert tuple(CHARACTERS[(ct, swap)][1] for ct in ORDER) == EXPECTED_H2[swap]

IRREPS = {
    '(4)':       (1, 1, 1, 1, 1),
    '(1,1,1,1)': (1, -1, 1, 1, -1),
    '(3,1)':     (3, 1, -1, 0, -1),
    '(2,1,1)':   (3, -1, -1, 0, 1),
    '(2,2)':     (2, 0, 2, -1, 0),
}
EXPECTED = {
    1: {1: {'(1,1,1,1)': 1, '(2,1,1)': 1},
       -1: {'(3,1)': 1}},
    2: {1: {'(3,1)': 1},
       -1: {'(1,1,1,1)': 1, '(2,2)': 1}},
}
for degree in (1, 2):
    for swap_sign in (1, -1):
        mults = {}
        for name, irrep in IRREPS.items():
            top = 0
            for i, cycle_type in enumerate(ORDER):
                c0 = CHARACTERS[(cycle_type, 0)][degree-1]
                c1 = CHARACTERS[(cycle_type, 1)][degree-1]
                top += SIZES[i] * irrep[i] * (c0 + swap_sign*c1)
            assert top % 48 == 0
            multiplicity = top // 48
            assert multiplicity >= 0
            if multiplicity:
                mults[name] = multiplicity
        assert mults == EXPECTED[degree][swap_sign]

print('PASS: (f0,f1,f2) = (12,36,24); 6 tetrahedral sphere boundaries')
print('PASS: intersection incidence graph = 18 vertices, 24 edges, connected')
print('PASS: integral homotopy type = wedge of 7 circles and 6 two-spheres')
print('PASS: all 48 symmetries; S4 class characters for both arrow-reversal cosets')
for degree in (1,2):
    for swap in (0,1):
        print('degree %d, reversal %d, types in [1111,211,22,31,4]: %s' %
              (degree, swap, tuple(CHARACTERS[(ct,swap)][degree-1] for ct in ORDER)))
print('PASS: all stated rational irreducible multiplicities')
