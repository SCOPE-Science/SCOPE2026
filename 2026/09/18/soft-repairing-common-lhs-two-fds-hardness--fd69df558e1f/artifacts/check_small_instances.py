#!/usr/bin/env python3
"""Small exhaustive checks for the soft-repair hardness reduction.

This script is a compact scientific sanity check.  It constructs the reduction
for two graphs on three vertices and exhaustively evaluates every database
subset, confirming the closed-form optimum from the proof.
"""
from itertools import combinations


def build_instance(n, edges, r):
    m = len(edges)
    D = 2 * m + 1
    shared = [None] * m
    incident = [[] for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        shared[j] = j
        incident[u].append(j)
        incident[v].append(j)
    nxt = m
    for v in range(n):
        while len(incident[v]) < D:
            incident[v].append(nxt)
            nxt += 1
    facts = [(v, c) for v in range(n) for c in incident[v]]
    W = ((4 * r - 1) * D - 1) // 2
    return D, W, facts


def induced_edges(edges, K):
    K = set(K)
    return sum(u in K and v in K for u, v in edges)


def brute(n, edges, r):
    D, W, facts = build_instance(n, edges, r)
    N = len(facts)
    best = None
    best_masks = []
    # Gray-code traversal updates degrees in O(1) per subset.
    deg_b = [0] * n
    max_c = max(c for _, c in facts) + 1
    deg_c = [0] * max_c
    s = 0
    sum_b2 = 0
    sum_c2 = 0
    prev_gray = 0
    for k in range(1 << N):
        gray = k ^ (k >> 1)
        if k:
            flip = gray ^ prev_gray
            i = flip.bit_length() - 1
            b, c = facts[i]
            if gray & flip:
                old = deg_b[b]
                sum_b2 += 2 * old + 1
                deg_b[b] = old + 1
                old = deg_c[c]
                sum_c2 += 2 * old + 1
                deg_c[c] = old + 1
                s += 1
            else:
                old = deg_b[b]
                sum_b2 += -2 * old + 1
                deg_b[b] = old - 1
                old = deg_c[c]
                sum_c2 += -2 * old + 1
                deg_c[c] = old - 1
                s -= 1
        prev_gray = gray
        twice_utility = 2 * W * s - 2 * s * s + sum_b2 + sum_c2
        if best is None or twice_utility > best:
            best = twice_utility
            best_masks = [gray]
        elif twice_utility == best:
            best_masks.append(gray)

    max_induced = max(induced_edges(edges, K) for K in combinations(range(n), r))
    predicted_twice = 2 * (D * D * r * r + max_induced)
    assert best == predicted_twice, (best, predicted_twice)

    # Every optimum must be exactly the union of all D incident facts of r B-values.
    for mask in best_masks:
        counts = [0] * n
        for i, (b, _) in enumerate(facts):
            if mask >> i & 1:
                counts[b] += 1
        assert sorted(counts) == [0] * (n - r) + [D] * r
    return D, W, N, best // 2, len(best_masks)


def main():
    cases = [
        (3, [(0, 1), (1, 2)], 3, "path P3 (no 3-clique)"),
        (3, [(0, 1), (1, 2), (0, 2)], 3, "triangle K3"),
    ]
    for n, edges, r, name in cases:
        D, W, N, optimum, multiplicity = brute(n, edges, r)
        print(f"{name}: D={D}, tuple_weight={W}, facts={N}, "
              f"max_utility={optimum}, optimal_subsets={multiplicity}")


if __name__ == "__main__":
    main()
