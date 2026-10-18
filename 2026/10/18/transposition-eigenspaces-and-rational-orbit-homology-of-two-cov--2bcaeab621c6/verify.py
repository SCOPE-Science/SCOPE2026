"""Independent finite checks for a transposition on the two-cover graph complex.

Standard-library only.  The infinite-parameter proof is combinatorial, not
inferred from these finite checks.
"""
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def all_graphs_two_covered_and_weights(n):
    """Check the exact alternating-sum classification for all eligible Z."""
    edges = list(combinations(range(n), 2))
    covers = edges
    patterns = {}
    counts = {}
    for mask in range(1, 1 << len(edges)):
        Z = tuple(e for j, e in enumerate(edges) if (mask >> j) & 1)
        C = [c for c in covers if all(c[0] in e or c[1] in e for e in Z)]
        if not C:
            continue
        U = set(v for c in C for v in c)
        W1 = {v for v in range(n) if all(v in e for e in Z)}
        s = 1 - bool(W1) - len(U) + len(W1) + len(C)
        degree = tuple(sorted(sum(v in e for e in Z) for v in range(n) if any(v in f for f in Z)))
        kind = (len(Z), degree)
        expected = (
            (n - 1 if kind == (1, (1, 1)) else
             1 if kind in ((2, (1, 1, 1, 1)), (2, (1, 1, 2)), (3, (2, 2, 2))) else
             -1 if kind == (4, (2, 2, 2, 2)) else 0)
        )
        assert s == expected, (n, Z, s, expected)
        if s:
            counts[kind] = counts.get(kind, 0) + 1
        patterns[len(Z)] = patterns.get(len(Z), 0) + (-1) ** len(Z) * s
    return counts, -sum(patterns.values())


def transposition_lefschetz_direct(m):
    """Enumerate every invariant simplex as unions of edge-orbits."""
    edges = list(combinations(range(m), 2))
    indices = {e: i for i, e in enumerate(edges)}
    perm = list(range(m))
    perm[0], perm[1] = 1, 0
    visited = set()
    orbits = []
    for i, e in enumerate(edges):
        if i in visited:
            continue
        members = []
        j = i
        while j not in visited:
            visited.add(j)
            members.append(j)
            j = indices[tuple(sorted(perm[v] for v in edges[j]))]
        orbits.append(members)
    covers = []
    for a, b in edges:
        coverage = 0
        for j, orbit in enumerate(orbits):
            if all(a in edges[k] or b in edges[k] for k in orbit):
                coverage |= 1 << j
        covers.append(coverage)
    covers = tuple(set(covers))
    alt = 0
    for mask in range(1 << len(orbits)):
        if any(mask & ~C == 0 for C in covers):
            alt += (-1) ** mask.bit_count()
    return -alt, len(orbits)


def main():
    for n in range(2, 7):
        kinds, reduced_lefschetz = all_graphs_two_covered_and_weights(n)
        formula = choose(n + 1, 3)
        assert reduced_lefschetz == formula
        print(f"OUTSIDE n={n}: exceptional_types={len(kinds)}, reduced_L={formula}")
    for m in range(4, 8):
        n = m - 2
        actual, num_orbits = transposition_lefschetz_direct(m)
        predicted = choose(n + 1, 3)
        trace_h4 = choose(n, 4) + choose(n, 2)
        trace_h3 = trace_h4 - actual
        assert actual == predicted
        assert trace_h3 == choose(n, 4) - choose(n, 3)
        b3 = choose(m - 1, 4)
        b4 = choose(m, 4)
        assert (b3 + trace_h3) // 2 == choose(n, 4)
        assert (b4 + trace_h4) // 2 == choose(n, 4) + choose(n, 3) + choose(n, 2)
        print(f"FULL m={m}: edge_orbits={num_orbits}, reduced_L={actual}, trace_H3={trace_h3}, invariant_b3={choose(n,4)}")
    for m in range(4, 101):
        n = m - 2
        E = choose(n, 2)
        direct = (n - 1) * E - choose(E, 2) + choose(n, 3) + 3 * choose(n, 4)
        assert direct == choose(n + 1, 3)
    print("VERIFY_OK all exhaustive covering classifications, edge-orbit Lefschetz values, and binomial identities agree")


if __name__ == "__main__":
    main()
