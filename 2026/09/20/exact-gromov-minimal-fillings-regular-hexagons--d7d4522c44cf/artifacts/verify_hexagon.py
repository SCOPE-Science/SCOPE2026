#!/usr/bin/env python3
"""Finite verifier for the six-point tour lemma used in the minimal-filling proof.

The script generates all labeled unrooted binary trees on leaves 0,...,5 by edge
subdivision, enumerates cyclic leaf orders up to rotation and reversal, recognizes
tree-compatible tours by the circular-interval criterion for edge splits, and
checks that every tree has a tour in one of the six gap-count classes used in
the analytic lower bound.
"""
from itertools import permutations

N = 6
TARGET = {
    (2, 4, 0),
    (0, 4, 2),
    (1, 4, 1),
    (2, 2, 2),
    (3, 0, 3),
    (1, 2, 3),
}

def edge_key(adj):
    return frozenset(
        (u, v) for u, nbrs in adj.items() for v in nbrs if u < v
    )

def insert_leaf(adj, leaf, internal):
    out = []
    for u, v in list(edge_key(adj)):
        nxt = {x: set(nbrs) for x, nbrs in adj.items()}
        nxt[u].remove(v)
        nxt[v].remove(u)
        nxt[internal] = {u, v, leaf}
        nxt[u].add(internal)
        nxt[v].add(internal)
        nxt[leaf] = {internal}
        out.append(nxt)
    return out

def all_binary_trees():
    # Unique 3-leaf star. Internal labels are auxiliary only.
    trees = [{0: {6}, 1: {6}, 2: {6}, 6: {0, 1, 2}}]
    internal = 7
    for leaf in (3, 4, 5):
        nxt = {}
        for tree in trees:
            for child in insert_leaf(tree, leaf, internal):
                nxt[edge_key(child)] = child
        trees = list(nxt.values())
        internal += 1
    return trees

def component_leaves(adj, start, blocked):
    stack = [start]
    seen = {blocked}
    leaves = set()
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        if 0 <= u < N:
            leaves.add(u)
        stack.extend(v for v in adj[u] if v not in seen)
    return frozenset(leaves)

def canonical_side(side):
    comp = frozenset(range(N)) - side
    if len(side) > len(comp):
        side = comp
    elif len(side) == len(comp) and tuple(sorted(side)) > tuple(sorted(comp)):
        side = comp
    return side

def nontrivial_splits(adj):
    out = set()
    for u, v in edge_key(adj):
        side = canonical_side(component_leaves(adj, u, v))
        if 1 < len(side) < N - 1:
            out.add(side)
    return frozenset(out)

def circular_interval(side, order):
    flags = [x in side for x in order]
    transitions = sum(
        flags[i] != flags[(i + 1) % N] for i in range(N)
    )
    return transitions == 2

def compatible(adj, order):
    return all(circular_interval(side, order) for side in nontrivial_splits(adj))

def gap_count(order):
    count = [0, 0, 0, 0]
    for i in range(N):
        x, y = order[i], order[(i + 1) % N]
        gap = abs(x - y)
        gap = min(gap, N - gap)
        count[gap] += 1
    return tuple(count[1:])

def cyclic_orders():
    # Fix 0 to remove rotations; order[1] < order[-1] removes reversal.
    for rest in permutations(range(1, N)):
        order = (0,) + rest
        if order[1] < order[-1]:
            yield order

def dihedral_permutations():
    for sign in (1, -1):
        for shift in range(N):
            yield {x: (sign * x + shift) % N for x in range(N)}

def split_key(adj):
    return tuple(
        sorted(tuple(sorted(side)) for side in nontrivial_splits(adj))
    )

def transform_key(key, perm):
    transformed = []
    for tup in key:
        side = canonical_side(frozenset(perm[x] for x in tup))
        transformed.append(tuple(sorted(side)))
    return tuple(sorted(transformed))

def main():
    trees = all_binary_trees()
    assert len(trees) == 105, len(trees)
    orders = list(cyclic_orders())
    assert len(orders) == 60, len(orders)

    witnesses = {}
    for tree in trees:
        key = split_key(tree)
        good = [
            order for order in orders
            if compatible(tree, order) and gap_count(order) in TARGET
        ]
        assert good, f"no target tour for {key}"
        witnesses[key] = min(good)

    # Reduce by the dihedral symmetry of the labeled hexagon.
    keys = set(witnesses)
    unseen = set(keys)
    orbit_rows = []
    while unseen:
        seed = min(unseen)
        orbit = {
            transform_key(seed, perm) for perm in dihedral_permutations()
        } & keys
        rep = min(orbit)
        rep_tree = next(tree for tree in trees if split_key(tree) == rep)
        good = sorted(
            order for order in orders
            if compatible(rep_tree, order) and gap_count(order) in TARGET
        )
        witness = good[0]
        orbit_rows.append((rep, len(orbit), witness, gap_count(witness)))
        unseen -= orbit

    assert len(orbit_rows) == 17, len(orbit_rows)
    assert sum(row[1] for row in orbit_rows) == 105

    print("labeled_binary_trees=105")
    print("dihedral_orbits=17")
    print("all_trees_have_target_tour=true")
    print("orbit_representative | orbit_size | witness_tour | gap_count")
    for rep, size, witness, gaps in sorted(orbit_rows):
        print(f"{rep} | {size} | {witness} | {gaps}")

if __name__ == "__main__":
    main()
