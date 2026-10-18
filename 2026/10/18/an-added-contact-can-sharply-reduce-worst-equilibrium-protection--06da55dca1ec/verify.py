"""Finite checks for the one-edge epidemic-containment equilibrium theorem.

No third-party packages are needed. This program checks the exact graph
combinatorics, not the SIS model's dynamical approximation.
"""
from itertools import combinations


def family(k, extra_edge):
    """Return the tree and its one-edge augmentation on vertices 0..2k+1.

    Hubs: 0, 1.  Leaves at 0: 2..k+1; at 1: k+2..2k+1.
    The bridge joins leaves 2 and k+2.  Added edge joins hubs.
    """
    assert k >= 2
    edges = [(0, 2+j) for j in range(k)]
    edges += [(1, k+2+j) for j in range(k)]
    edges.append((2, k+2))
    if extra_edge:
        edges.append((0, 1))
    return 2*k+2, edges


def bounds(n, edges):
    """Exact independence and independent domination from all subsets."""
    neighbors = [0]*n
    for a,b in edges:
        assert a != b
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a
    alpha = 0
    min_maximal = n+1
    maximal_count = 0
    for subset in range(1 << n):
        if any(((subset >> u) & 1) and (neighbors[u] & subset)
               for u in range(n)):
            continue
        cardinality = subset.bit_count()
        alpha = max(alpha, cardinality)
        if all(((subset >> u) & 1) or (neighbors[u] & subset)
               for u in range(n)):
            maximal_count += 1
            min_maximal = min(min_maximal, cardinality)
    return alpha, min_maximal, maximal_count


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    reached = {0}
    stack = [0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in reached:
                reached.add(v)
                stack.append(v)
    return len(reached) == n


def verify_family():
    for k in range(2, 7):
        n, old = family(k, False)
        _, new = family(k, True)
        assert connected(n, old)
        assert len(old) == n-1
        assert len(new) == n
        alpha_old, i_old, count_old = bounds(n, old)
        alpha_new, i_new, count_new = bounds(n, new)
        assert (alpha_old, i_old) == (2*k-1, 2)
        assert (alpha_new, i_new) == (2*k-1, k+1)
        print('k=%d n=%d alpha_old=%d alpha_new=%d i_old=%d i_new=%d NE_counts=%d,%d'
              % (k, n, alpha_old, alpha_new, i_old, i_new, count_old, count_new))


def verify_small_cutoff():
    for n in range(2, 6):
        possible = list(combinations(range(n), 2))
        num_connected = 0
        num_edge_checks = 0
        for edge_bits in range(1 << len(possible)):
            old = [e for j,e in enumerate(possible) if edge_bits & (1 << j)]
            if not connected(n, old):
                continue
            num_connected += 1
            _, i_old, _ = bounds(n, old)
            for j,e in enumerate(possible):
                if edge_bits & (1 << j):
                    continue
                _, i_new, _ = bounds(n, old + [e])
                assert i_new <= i_old, (n, old, e)
                num_edge_checks += 1
        print('n=%d connected_labelled_graphs=%d added_edges_checked=%d reversals=0'
              % (n, num_connected, num_edge_checks))


if __name__ == '__main__':
    verify_family()
    verify_small_cutoff()
