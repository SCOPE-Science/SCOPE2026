#!/usr/bin/env python3
from itertools import product, combinations
from math import gcd, lcm

def add(a, b, mods):
    return tuple((x + y) % m for x, y, m in zip(a, b, mods))

def element_order(a, mods):
    out = 1
    for x, m in zip(a, mods):
        if x:
            out = lcm(out, m // gcd(x, m))
    return out

def extend(H, g, mods):
    out = set()
    cur = tuple(0 for _ in mods)
    for _ in range(element_order(g, mods)):
        for h in H:
            out.add(add(h, cur, mods))
        cur = add(cur, g, mods)
    return frozenset(out)

def proper_nontrivial_subgroups(mods):
    elems = list(product(*[range(m) for m in mods]))
    zero = tuple(0 for _ in mods)
    trivial = frozenset([zero])
    whole = frozenset(elems)
    seen = {trivial}
    frontier = [trivial]
    while frontier:
        H = frontier.pop()
        for g in elems:
            if g not in H:
                K = extend(H, g, mods)
                if K not in seen:
                    seen.add(K)
                    frontier.append(K)
    return [H for H in seen if H != trivial and H != whole]

def intersection_graph(mods):
    V = proper_nontrivial_subgroups(mods)
    adj = [set() for _ in V]
    for i, H in enumerate(V):
        for j in range(i + 1, len(V)):
            K = V[j]
            if len(H.intersection(K)) > 1:
                adj[i].add(j)
                adj[j].add(i)
    return V, adj

def perfect_matching(vertices, adj):
    vertices = set(vertices)
    if not vertices:
        return True
    if len(vertices) % 2:
        return False
    v = next(iter(vertices))
    for u in adj[v] & vertices:
        if perfect_matching(vertices - {v, u}, adj):
            return True
    return False

def paired_dominates(S, adj):
    S = set(S)
    if not all(v in S or bool(adj[v] & S) for v in range(len(adj))):
        return False
    return perfect_matching(S, adj)

def paired_number(mods, max_k=6):
    V, adj = intersection_graph(mods)
    if any(not a for a in adj):
        return len(V), None
    for k in range(2, min(max_k, len(V)) + 1, 2):
        for S in combinations(range(len(V)), k):
            if paired_dominates(S, adj):
                return len(V), k
    return len(V), None

cases = [
    ("C4", (4,), None),
    ("C8", (8,), 2),
    ("C2xC2", (2, 2), None),
    ("C2^3", (2, 2, 2), 4),
    ("C3^2", (3, 3), None),
    ("C3^3", (3, 3, 3), 4),
    ("C6", (6,), None),
    ("C2^2xC3", (2, 2, 3), 2),
    ("C30", (30,), 2),
    ("C4xC2", (4, 2), 2),
]

rows = []
for name, mods, expected in cases:
    nv, got = paired_number(mods)
    assert got == expected, (name, got, expected)
    rows.append((name, nv, got))

print("VERIFY_OK")
for name, nv, got in rows:
    value = "none" if got is None else str(got)
    print(f"{name}: vertices={nv} paired_domination={value}")
