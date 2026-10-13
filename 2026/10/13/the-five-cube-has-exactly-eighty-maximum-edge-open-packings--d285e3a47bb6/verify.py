#!/usr/bin/env python3
"""Exact, standard-library verification for maximum edge-open packings of Q5.

Independent of any MILP solver.  Every decision is exact; the search tree uses
only greedy graph coloring as a rigorously valid upper bound on clique size.
"""
from itertools import permutations
from collections import Counter

DIMENSION = 5
VERTICES = range(1 << DIMENSION)
EDGES = tuple((x, x ^ (1 << k)) for x in VERTICES for k in range(DIMENSION)
              if not (x & (1 << k)))
assert len(EDGES) == 80 and EDGES[0] == (0, 1)
EDGESET = frozenset(EDGES)


def directly_conflict(edge1, edge2):
    """Implementation of the defining *third graph edge* condition."""
    a = set(edge1)
    b = set(edge2)
    for u, v in EDGES:
        third = (u, v)
        if third == edge1 or third == edge2:
            continue
        if (u in a and v in b) or (v in a and u in b):
            return True
    return False


def faster_conflict(edge1, edge2):
    """Equivalent cube-specific condition, checked against directly_conflict."""
    if set(edge1) & set(edge2):
        return False
    return any((u ^ v).bit_count() == 1 for u in edge1 for v in edge2)


N = len(EDGES)
C = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        d = directly_conflict(EDGES[i], EDGES[j])
        assert d == faster_conflict(EDGES[i], EDGES[j])
        if d:
            C[i] |= 1 << j
            C[j] |= 1 << i
assert sum(x.bit_count() for x in C) // 2 == 1120
assert all(x.bit_count() == 28 for x in C)

FIXED = 0
AVAILABLE = tuple(j for j in range(1, N) if not ((C[FIXED] >> j) & 1))
assert len(AVAILABLE) == 51
K = len(AVAILABLE)
# Compatibility graph: its cliques are exactly EOP sets among AVAILABLE.
ADJ = [0] * K
for i, x in enumerate(AVAILABLE):
    for j, y in enumerate(AVAILABLE):
        if i != j and not ((C[x] >> y) & 1):
            ADJ[i] |= 1 << j
assert all(bool((ADJ[i] >> j) & 1) == bool((ADJ[j] >> i) & 1)
           for i in range(K) for j in range(K))


def greedy_color_order(p):
    """Partition p into independent color classes of ADJ, in increasing order."""
    order = []
    upper = []
    color = 0
    while p:
        color += 1
        choices = p
        while choices:
            bit = choices & -choices
            v = bit.bit_length() - 1
            p ^= bit
            choices ^= bit
            choices &= ~ADJ[v]
            order.append(v)
            upper.append(color)
    # Every clique in any prefix has size <= the number of colors in that prefix.
    return order, upper


def count_cliques_of_size(target):
    """Exactly enumerate target-cliques by all branches with valid color pruning."""
    total = 0
    visits = 0
    first = None

    def rec(p, chosen):
        nonlocal total, visits, first
        visits += 1
        if len(chosen) == target:
            total += 1
            if first is None:
                first = tuple(chosen)
            return
        if not p:
            return
        order, bound = greedy_color_order(p)
        for pos in range(len(order) - 1, -1, -1):
            if len(chosen) + bound[pos] < target:
                return
            v = order[pos]
            rec(p & ADJ[v], chosen + [v])
            p &= ~(1 << v)

    rec((1 << K) - 1, [])
    return total, visits, first


COUNT_12, NODES_12, _ = count_cliques_of_size(12)
COUNT_11, NODES_11, W = count_cliques_of_size(11)
assert (COUNT_12, COUNT_11) == (0, 12)
assert W is not None
# Explicit human-readable construction: split five coordinates into blocks 3+2.
CENTERS = (0b00000, 0b11000, 0b10111, 0b01111)
WITNESS = frozenset(tuple(sorted((center, center ^ (1 << k))))
                    for center in CENTERS for k in (0, 1, 2))
assert len(WITNESS) == 12 and WITNESS <= EDGESET
assert all(not directly_conflict(a, b) for i, a in enumerate(sorted(WITNESS))
           for b in sorted(WITNESS)[i + 1:])
assert sum(1 for e in WITNESS if e == EDGES[FIXED]) == 1

# An automorphism is a translation x -> x xor t followed by a coordinate permutation.
def orbit(seed):
    out = set()
    for perm in permutations(range(DIMENSION)):
        table = [sum(((x >> k) & 1) << perm[k] for k in range(DIMENSION))
                 for x in VERTICES]
        for t in VERTICES:
            out.add(frozenset(tuple(sorted((table[x] ^ t, table[y] ^ t)))
                              for x, y in seed))
    return out

ORB = orbit(WITNESS)
assert len(ORB) == 80
assert all(len(obj) == 12 for obj in ORB)
assert all(all(not faster_conflict(e, f) for i, e in enumerate(sorted(obj))
               for f in sorted(obj)[i + 1:]) for obj in ORB)
# Edge transitivity + double counting: 80 edges *12 optima through a fixed edge /12.
TOTAL = len(EDGES) * COUNT_11 // 12
assert TOTAL == 80 and TOTAL == len(ORB)

# Every maximum configuration in the orbit is exactly four induced K_(1,3)'s;
# all four centers lie in the same bipartition class.
def component_signature(selected):
    adj = {}
    for a, b in selected:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    seen = set()
    component_edges = []
    parities = []
    for v in adj:
        if v in seen:
            continue
        stack = [v]
        seen.add(v)
        component = []
        while stack:
            u = stack.pop()
            component.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        component_edges.append(sum(len(adj[u]) for u in component) // 2)
        center = max(component, key=lambda u: len(adj[u]))
        parities.append(center.bit_count() % 2)
    return tuple(sorted(component_edges)), len(set(parities)) == 1

assert all(component_signature(obj) == ((3, 3, 3, 3), True) for obj in ORB)

print('Q5 vertices=32 edges=80 conflict_pairs=1120 degree=28')
print(f'Fixed edge=(0,1) permitted_other_edges={K}')
print(f'Compatibility 12-cliques={COUNT_12} search_nodes={NODES_12}')
print(f'Compatibility 11-cliques={COUNT_11} search_nodes={NODES_11}')
print('Maximum edge-open-packing size=12')
print(f'Total maximum edge-open packings={TOTAL}')
print(f'Cube-automorphism orbit size={len(ORB)} (single orbit of all maxima)')
print('Maximum components=K1,3+K1,3+K1,3+K1,3')
print('Verification result: PASS')
