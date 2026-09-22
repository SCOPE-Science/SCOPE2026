#!/usr/bin/env python3
"""Independent finite check for SCOPE 2026/09/07/001 (2026-09-22)."""
import itertools

ALL = list(itertools.combinations(range(1, 9), 4))
SETS = [set(a) for a in ALL]
N = len(ALL)

# Compatibility graph: a clique is a family with no intersection of size exactly 1.
ADJ = [set() for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if len(SETS[i] & SETS[j]) != 1:
            ADJ[i].add(j)
            ADJ[j].add(i)

def color_sort(P):
    """Partition P greedily into independent color classes; colors upper-bound a clique."""
    U = set(P)
    order, bound = [], []
    color = 0
    while U:
        color += 1
        Q = set(U)
        while Q:
            v = min(Q)
            order.append(v)
            bound.append(color)
            U.remove(v)
            Q.remove(v)
            Q -= ADJ[v]
    return order, bound

best = []
max_nodes = 0
def maximum_clique(R, P):
    global best, max_nodes
    max_nodes += 1
    if not P:
        if len(R) > len(best):
            best = R[:]
        return
    order, bound = color_sort(P)
    P = set(P)
    for i in range(len(order) - 1, -1, -1):
        v = order[i]
        if v not in P:
            continue
        if len(R) + bound[i] <= len(best):
            return
        Q = P & ADJ[v]
        R.append(v)
        if Q:
            maximum_clique(R, Q)
        elif len(R) > len(best):
            best = R[:]
        R.pop()
        P.remove(v)

maximum_clique([], set(range(N)))
assert len(best) == 17

# Enumerate every maximum family containing 1234.
v0 = ALL.index((1, 2, 3, 4))
solutions = []
enum_nodes = 0
def enumerate_target(R, P, target=17):
    global enum_nodes
    enum_nodes += 1
    if len(R) == target:
        solutions.append(tuple(R))
        return
    if not P:
        return
    order, bound = color_sort(P)
    P = set(P)
    for i in range(len(order) - 1, -1, -1):
        v = order[i]
        if v not in P:
            continue
        if len(R) + bound[i] < target:
            return
        Q = P & ADJ[v]
        R.append(v)
        if len(R) == target:
            solutions.append(tuple(R))
        else:
            enumerate_target(R, Q, target)
        R.pop()
        P.remove(v)

enumerate_target([v0], set(ADJ[v0]))
assert len(solutions) == 17

def ball(center):
    C = set(center)
    return frozenset(i for i, A in enumerate(SETS) if len(A & C) >= 3)

BALLS = {ball(c) for c in ALL}
assert all(frozenset(sol) in BALLS for sol in solutions)

# Explicit shifting counterexample.
assert len(set((2,3,4,5)) & set((1,6,7,8))) == 0
assert len(set((1,3,4,5)) & set((1,6,7,8))) == 1

print({
    "maximum": len(best),
    "max_search_nodes": max_nodes,
    "maxima_containing_1234": len(solutions),
    "enumeration_nodes": enum_nodes,
    "all_are_balls": True,
})
