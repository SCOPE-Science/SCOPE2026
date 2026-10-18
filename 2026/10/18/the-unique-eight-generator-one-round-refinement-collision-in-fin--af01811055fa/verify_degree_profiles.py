"""Exact enumeration of finite distributive-lattice order-degree profiles.

All P of size n are generated from all P of size n-1 by adjoining a maximal
point whose predecessor set is an order ideal. NetworkX exact directed graph
isomorphism identifies duplicate poset presentations. No randomization is used.
"""
from collections import defaultdict
import networkx as nx

EXPECTED = [1, 2, 5, 16, 63, 318, 2045, 16999]


def ideals(lower):
    n = len(lower)
    return [s for s in range(1 << n)
            if all(not ((s >> i) & 1) or (s & lower[i]) == lower[i]
                   for i in range(n))]


def poset_graph(lower):
    g = nx.DiGraph()
    g.add_nodes_from(range(len(lower)))
    for j, pred in enumerate(lower):
        for i in range(j):
            if (pred >> i) & 1:
                g.add_edge(i, j)
    return g


def poset_fingerprint(lower):
    n = len(lower)
    return tuple(sorted((lower[i].bit_count(),
                         sum((lower[j] >> i) & 1 for j in range(n)))
                        for i in range(n)))


def lattice_profile(lower):
    jj = ideals(lower)
    return (len(jj), tuple(sorted((sum(v != u and (v & u) == v for v in jj),
                                  sum(v != u and (v & u) == u for v in jj))
                                 for u in jj)))


def extend(representatives):
    by_fp = defaultdict(list)
    for lower in representatives:
        for pred in ideals(lower):
            new = lower + [pred]
            fp = poset_fingerprint(new)
            g = poset_graph(new)
            if not any(nx.is_isomorphic(g, h) for _, h in by_fp[fp]):
                by_fp[fp].append((new, g))
    return [low for group in by_fp.values() for low, _ in group]


def main():
    representatives = [[0]]
    all_profiles = defaultdict(list)
    counts = []
    for n in range(1, 9):
        if n > 1:
            representatives = extend(representatives)
        counts.append(len(representatives))
        for lower in representatives:
            all_profiles[lattice_profile(lower)].append((n, lower))
        print(f"n={n}: {len(representatives)} distinct posets", flush=True)
    assert counts == EXPECTED, (counts, EXPECTED)
    collisions = [item for item in all_profiles.items() if len(item[1]) > 1]
    assert len(collisions) == 1, collisions
    (lattice_size, profile), witnesses = collisions[0]
    assert lattice_size == 18
    assert len(witnesses) == 2 and all(n == 8 for n, _ in witnesses)
    witness_set = {tuple(low) for n, low in witnesses}
    expected = {(0, 0, 1, 3, 5, 15, 23, 63),
                (0, 0, 1, 3, 5, 15, 23, 95)}
    assert witness_set == expected, witness_set
    assert not nx.is_isomorphic(poset_graph(witnesses[0][1]),
                                poset_graph(witnesses[1][1]))
    print("TOTAL_POSETS=19449")
    print("TOTAL_DISTINCT_PROFILES=19448")
    print("COLLISION_CLASS_COUNT=1")
    print("COLLISION_PAIR_COUNT=1")
    print("WITNESS_LATTICE_SIZE=18")
    print("WITNESS_PREDECESSOR_MASKS=", sorted(witness_set))
    print("VERIFY_EXHAUSTIVE_OK")


if __name__ == '__main__':
    main()
