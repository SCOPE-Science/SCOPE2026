#!/usr/bin/env python3
"""Exact verification of the binary rank-four fooling-set maximum."""
from itertools import product

R = 4
FIXED_PAIRS = [
    (15, 14), (14, 15), (13, 13), (12, 8), (11, 1), (10, 2),
    (8, 12), (6, 5), (5, 3), (2, 10), (1, 7),
]


def bits(x):
    return tuple((x >> k) & 1 for k in (3, 2, 1, 0))


def dot_idx(x, y):
    return sum(a * b for a, b in zip(bits(x), bits(y))) & 1


def gf2_rank(A):
    A = [row[:] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if A[i][col]), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        for i in range(m):
            if i != rank and A[i][col]:
                A[i] = [a ^ b for a, b in zip(A[i], A[rank])]
        rank += 1
    return rank


def build_matrix(pairs):
    return [[dot_idx(u, v) for _, v in pairs] for u, _ in pairs]


def is_fooling(M):
    n = len(M)
    return (
        all(M[i][i] == 1 for i in range(n))
        and all(M[i][j] * M[j][i] == 0 for i in range(n) for j in range(n) if i != j)
    )


def admissible_types():
    # A rank-at-most-four factorization M=UV^T assigns one ordered pair
    # (u_i,v_i) in F_2^4 x F_2^4 to each diagonal position, with u_i.v_i=1.
    return [(u, v) for u in range(16) for v in range(16) if dot_idx(u, v) == 1]


def compatibility_graph(types):
    n = len(types)
    adj = [0] * n
    incompatible = 0
    for i in range(n):
        ui, vi = types[i]
        for j in range(i + 1, n):
            uj, vj = types[j]
            bad = dot_idx(ui, vj) == 1 and dot_idx(uj, vi) == 1
            if bad:
                incompatible += 1
            else:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj, incompatible


def maximum_clique(adj):
    """Exact branch-and-bound maximum clique with a valid greedy-color upper bound."""
    best = []
    nodes = 0

    def color_sort(P):
        # Partition the current induced graph greedily into independent color classes.
        # The assigned color number is therefore an upper bound on the size of a clique
        # in each processed prefix of the returned order.
        order = []
        bounds = []
        color = 0
        remaining = P
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)
                remaining &= ~bit
                available &= ~bit
                available &= ~adj[v]
        return order, bounds

    def expand(C, P):
        nonlocal best, nodes
        nodes += 1
        if not P:
            if len(C) > len(best):
                best = C[:]
            return
        order, bounds = color_sort(P)
        for idx in range(len(order) - 1, -1, -1):
            if len(C) + bounds[idx] <= len(best):
                return
            v = order[idx]
            bit = 1 << v
            if not (P & bit):
                continue
            expand(C + [v], P & adj[v])
            P &= ~bit

    expand([], (1 << len(adj)) - 1)
    return best, nodes


def main():
    witness = build_matrix(FIXED_PAIRS)
    assert is_fooling(witness)
    assert gf2_rank(witness) == 4

    types = admissible_types()
    assert len(types) == 120
    adj, incompatible = compatibility_graph(types)
    clique, nodes = maximum_clique(adj)
    assert len(clique) == 11

    fixed_type_indices = []
    index = {pair: i for i, pair in enumerate(types)}
    for pair in FIXED_PAIRS:
        fixed_type_indices.append(index[pair])
    assert all((adj[i] >> j) & 1 for a, i in enumerate(fixed_type_indices) for j in fixed_type_indices[a+1:])

    print("VERIFY_OK")
    print(f"admissible_types={len(types)}")
    print(f"incompatible_edges={incompatible}")
    print(f"compatibility_edges={len(types)*(len(types)-1)//2-incompatible}")
    print(f"exact_maximum_clique={len(clique)}")
    print(f"branch_nodes={nodes}")
    print("witness_order=11")
    print(f"witness_rank={gf2_rank(witness)}")
    print("witness_matrix=")
    for row in witness:
        print("".join(map(str, row)))


if __name__ == "__main__":
    main()
