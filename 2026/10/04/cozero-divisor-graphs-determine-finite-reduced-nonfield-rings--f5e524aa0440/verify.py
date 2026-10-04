#!/usr/bin/env python3
from itertools import combinations, combinations_with_replacement
from math import prod

def build_graph(qs):
    r = len(qs)
    a = [q - 1 for q in qs]
    vertices = []
    for mask in range(1, (1 << r) - 1):
        w = 1
        for i in range(r):
            if (mask >> i) & 1:
                w *= a[i]
        for copy in range(w):
            vertices.append((mask, copy))

    adj = [set() for _ in vertices]
    for i in range(len(vertices)):
        S = vertices[i][0]
        for j in range(i + 1, len(vertices)):
            T = vertices[j][0]
            # Supports are adjacent precisely when they are incomparable.
            if (S & T) != S and (S & T) != T:
                adj[i].add(j)
                adj[j].add(i)
    return vertices, adj

def recover_field_orders(adj):
    # False twins are grouped by identical open neighborhoods.
    twin_groups = {}
    for v, N in enumerate(adj):
        twin_groups.setdefault(frozenset(N), []).append(v)
    classes = list(twin_groups.values())
    class_count = len(classes)

    x = class_count + 2
    r = x.bit_length() - 1
    assert (1 << r) == x and r >= 2

    class_of = {}
    for c, group in enumerate(classes):
        for v in group:
            class_of[v] = c

    qadj = [set() for _ in classes]
    for c, group in enumerate(classes):
        v = group[0]
        for u in adj[v]:
            d = class_of[u]
            if d != c:
                qadj[c].add(d)

    sizes = [len(group) for group in classes]

    if r == 2:
        assert class_count == 2
        assert qadj[0] == {1} and qadj[1] == {0}
        return sorted([sizes[0] + 1, sizes[1] + 1])

    degrees = [len(N) for N in qadj]
    minimum = min(degrees)
    extremal = [c for c, d in enumerate(degrees) if d == minimum]
    assert len(extremal) == 2 * r

    # In the minimum-degree quotient subgraph there are exactly two r-cliques:
    # singleton supports and co-singleton supports.
    r_cliques = []
    for C in combinations(extremal, r):
        if all(v in qadj[u] for u, v in combinations(C, 2)):
            r_cliques.append(set(C))
    assert len(r_cliques) == 2
    A, B = r_cliques
    assert A.isdisjoint(B) and A | B == set(extremal)

    def try_orientation(singletons, cosingletons):
        matching = {}
        for u in singletons:
            cross = qadj[u] & cosingletons
            if len(cross) != 1:
                return None
            matching[u] = next(iter(cross))

        total = prod(sizes[u] for u in singletons)
        for u, v in matching.items():
            if sizes[v] != total // sizes[u]:
                return None
        return sorted(sizes[u] + 1 for u in singletons)

    candidates = [
        ans for ans in
        (try_orientation(A, B), try_orientation(B, A))
        if ans is not None
    ]
    assert candidates
    assert all(ans == candidates[0] for ans in candidates)
    return candidates[0]

checked = 0
largest = 0

# Exhaustive profile check for 2 <= r <= 4 and field orders 2,...,5.
for r in range(2, 5):
    for qs in combinations_with_replacement(range(2, 6), r):
        vertices, adj = build_graph(qs)
        recovered = recover_field_orders(adj)
        assert recovered == list(qs), (qs, recovered)
        checked += 1
        largest = max(largest, len(vertices))

# Additional five-factor cases, including the side-swap-symmetric all-F_2 case.
extra = [
    (2, 2, 2, 2, 2),
    (2, 2, 2, 2, 3),
    (2, 2, 3, 3, 3),
    (2, 3, 3, 4, 4),
]
for qs in extra:
    vertices, adj = build_graph(qs)
    recovered = recover_field_orders(adj)
    assert recovered == sorted(qs), (qs, recovered)
    checked += 1
    largest = max(largest, len(vertices))

print("VERIFY_OK")
print(f"profiles_checked={checked}")
print(f"largest_vertex_count={largest}")
print("false_twin_support_recovery=passed")
print("quotient_extremal_clique_recovery=passed")
print("field_order_reconstruction=passed")
