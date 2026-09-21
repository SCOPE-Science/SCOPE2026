#!/usr/bin/env python3
"""Finite check for the explicit induced-path obstruction in the theorem.

Requires NetworkX. It enumerates every nonisomorphic base tree of orders 2..6,
forms the twice-subdivision of every ordered pair, and checks the displayed
19-vertex obstruction for every relevant leaf/branch-center/triple in both
factor orientations.
"""
import itertools
import networkx as nx

def twice_subdivide(T):
    R = nx.Graph()
    R.add_nodes_from(("o", v) for v in T.nodes())
    for i, (u, v) in enumerate(T.edges()):
        a, b = ("s", i, 0), ("s", i, 1)
        R.add_edges_from([(("o", u), a), (a, b), (b, ("o", v))])
    return R

def adjacent(A, B, p, q):
    (x, y), (x2, y2) = p, q
    return (x == x2 and B.has_edge(y, y2)) or (
        y == y2 and A.has_edge(x, x2)
    )

def is_induced_path(A, B, path):
    if len(set(path)) != len(path):
        return False
    if any(not adjacent(A, B, path[i], path[i+1])
           for i in range(len(path)-1)):
        return False
    return all(not adjacent(A, B, path[i], path[j])
               for i in range(len(path))
               for j in range(i+2, len(path)))

def leaf_chain(A, leaf):
    chain = [leaf]
    prev, cur = None, leaf
    for _ in range(3):
        nxt = [z for z in A.neighbors(cur) if z != prev]
        assert nxt
        z = nxt[0]
        chain.append(z)
        prev, cur = cur, z
    return chain

def outward_chain(B, center, nbr, length):
    chain = [center, nbr]
    prev, cur = center, nbr
    while len(chain) <= length:
        nxt = [z for z in B.neighbors(cur) if z != prev]
        assert nxt
        z = nxt[0]
        chain.append(z)
        prev, cur = cur, z
    return chain

def obstruction(A, B, x, center, a, b, c):
    x0, x1, x2, x3 = x
    aa = outward_chain(B, center, a, 2)
    cc = outward_chain(B, center, c, 3)
    a1, a2 = aa[1], aa[2]
    c1, c2, c3 = cc[1], cc[2], cc[3]
    b1 = b
    return [
        (x0,a1),(x0,a2),(x1,a2),(x2,a2),(x3,a2),
        (x3,a1),(x3,center),(x3,c1),(x3,c2),(x2,c2),
        (x2,c3),(x1,c3),(x0,c3),(x0,c2),(x0,c1),
        (x1,c1),(x1,center),(x1,b1),(x0,b1),
    ]

bases = []
for n in range(2, 7):
    bases.extend(nx.generators.nonisomorphic_trees(n))

pairs = 0
checked = 0
for F in bases:
    A = twice_subdivide(F)
    for H in bases:
        B = twice_subdivide(H)
        pairs += 1
        for X, Y in ((A, B), (B, A)):
            leaves = [v for v in X if X.degree(v) == 1]
            centers = [v for v in Y if Y.degree(v) >= 3]
            for leaf in leaves:
                x = leaf_chain(X, leaf)
                for center in centers:
                    for tri in itertools.combinations(list(Y.neighbors(center)), 3):
                        path = obstruction(X, Y, x, center, *tri)
                        assert is_induced_path(X, Y, path)
                        targets = {(x[0], z) for z in tri}
                        assert targets.issubset(path)
                        checked += 1

print(f"base_trees={len(bases)}")
print(f"ordered_pairs={pairs}")
print(f"oriented_obstructions_checked={checked}")
print("all_obstructions_induced=True")
