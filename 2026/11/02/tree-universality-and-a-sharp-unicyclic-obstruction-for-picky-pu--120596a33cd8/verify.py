"""Reproduce finite certificates for strict binary public-goods equilibria.

Standard library only. Uses the Prüfer bijection for exhaustive labeled
unicyclic graphs through six vertices; cycles are not sampled.
"""
from itertools import product
from collections import Counter
from heapq import heapify, heappop, heappush


def prufer_tree(n, word):
    if n == 1:
        return ()
    degree = [1] * n
    for w in word:
        degree[w] += 1
    leaves = [i for i in range(n) if degree[i] == 1]
    heapify(leaves)
    edges = []
    for w in word:
        v = heappop(leaves)
        edges.append((min(v, w), max(v, w)))
        degree[v] -= 1
        degree[w] -= 1
        if degree[w] == 1:
            heappush(leaves, w)
    a, b = sorted(leaves)
    edges.append((a, b))
    return tuple(sorted(edges))


def all_trees(n):
    if n == 1:
        yield ()
    else:
        for word in product(range(n), repeat=n-2):
            yield prufer_tree(n, word)


def adjacent_masks(n, edges):
    masks = [0] * n
    for a, b in edges:
        masks[a] |= (1 << b)
        masks[b] |= (1 << a)
    return masks


def is_equilibrium(n, edges, q, m):
    nbr = adjacent_masks(n, edges)
    return all(((m >> v) & 1) == ((m & nbr[v]).bit_count() in (0, q))
               for v in range(n))


def equilibria(n, edges, q):
    nbr = adjacent_masks(n, edges)
    return [m for m in range(1 << n) if all(
        ((m >> v) & 1) == ((m & nbr[v]).bit_count() in (0, q))
        for v in range(n))]


def rooted_feasible(n, edges, q):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    def rec(v, parent):
        children = [(u, rec(u, v)) for u in adj[v] if u != parent]
        states = []
        for par_action in (0, 1):
            valid = set()
            for own in (0, 1):
                # Every subtree decision is encoded by its root's feasible set.
                sums = {0}
                for _, sub in children:
                    sums = {s + t for s in sums for t in sub[own]}
                if any(own == (par_action + s in (0, q)) for s in sums):
                    valid.add(own)
            states.append(frozenset(valid))
        assert states[0]
        assert states[1] <= {0}
        if not states[1]:
            assert states[0] == {0, 1}
        return tuple(states)
    return rec(0, -1)[0]


def graph_key(n, edges):
    return tuple(sorted(edges))


def labeled_unicyclic(n):
    all_edges = {(i, j) for i in range(n) for j in range(i+1, n)}
    out = set()
    for tree in all_trees(n):
        ed = set(tree)
        for e in all_edges - ed:
            out.add(graph_key(n, (*tree, e)))
    return out


def double_hub_triangle(q):
    n = 2*q + 1
    e = [(0, 1), (1, 2), (0, 2)]
    for w in range(3, q+2):
        e.append((1, w))
    for w in range(q+2, 2*q+1):
        e.append((2, w))
    return n, tuple(sorted(e))


def main():
    # Independent exhaustive small-tree cross-checks of the induction.
    tree_checks = Counter()
    for n in range(1, 7):
        for edges in all_trees(n):
            for q in range(2, 7):
                assert rooted_feasible(n, edges, q)
                assert equilibria(n, edges, q)
                tree_checks[n] += 1
    print('Tree q-cross-checks:', dict(sorted(tree_checks.items())))
    counts = {}
    for n in range(3, 7):
        graphs = labeled_unicyclic(n)
        counts[n] = len(graphs)
        for edges in graphs:
            assert equilibria(n, edges, 3), (n, edges)
    print('Exhaustive labeled unicyclic graph counts n=3..6:', counts)
    assert counts == {3: 1, 4: 15, 5: 222, 6: 3660}, counts
    for q in range(3, 9):
        n, edges = double_hub_triangle(q)
        assert len(edges) == n
        assert not equilibria(n, edges, q)
    n, edges = double_hub_triangle(3)
    print('Smallest seven-vertex obstruction for q=3:', edges)
    print('All finite certificates passed.')


if __name__ == '__main__':
    main()
