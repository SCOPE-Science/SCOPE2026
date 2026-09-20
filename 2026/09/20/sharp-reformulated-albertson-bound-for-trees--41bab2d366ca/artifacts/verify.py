"""Exhaustively verify the stated tree extremum for all non-isomorphic trees up to n=17.

Requires NetworkX 3.6.1 (or a compatible version providing nonisomorphic_trees).
"""
import networkx as nx


def ralb(T):
    degree = dict(T.degree())
    total = 0
    for v in T:
        nbrs = list(T.neighbors(v))
        for i in range(len(nbrs)):
            for j in range(i + 1, len(nbrs)):
                total += abs(degree[nbrs[i]] - degree[nbrs[j]])
    return total


def trees_of_order(n):
    if n == 2:
        return [nx.path_graph(2)]
    return nx.nonisomorphic_trees(n)


for n in range(2, 18):
    best = -1
    count = 0
    best_degree_sequence = None
    number_of_trees = 0
    for T in trees_of_order(n):
        number_of_trees += 1
        value = ralb(T)
        if value > best:
            best = value
            count = 1
            best_degree_sequence = sorted((d for _, d in T.degree()), reverse=True)
        elif value == best:
            count += 1
    target = (n - 2) * (n - 2) // 2
    assert best == target
    if n >= 4:
        assert count == 1
    print(n, number_of_trees, best, count, best_degree_sequence)
