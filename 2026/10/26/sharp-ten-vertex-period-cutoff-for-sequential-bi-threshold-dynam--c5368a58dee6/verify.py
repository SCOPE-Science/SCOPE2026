#!/usr/bin/env python3
"""Exact exhaustive census of sequential bi-threshold (1,3) dynamics on trees.

Requires Python standard library only. The graph has n vertices, binary states,
and each sweep visits vertices in increasing label order. The published tree
schedule-equivalence theorem makes the primitive-period census independent
of the chosen permutation of each tree's vertices.
"""
from collections import Counter


def center_vertices(adj):
    n = len(adj)
    if n <= 2:
        return tuple(range(n))
    degree = [len(row) for row in adj]
    leaves = [i for i, d in enumerate(degree) if d <= 1]
    remaining = n
    while remaining > 2:
        remaining -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            for neighbor in adj[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
            degree[leaf] = 0
        leaves = new_leaves
    return tuple(leaves)


def rooted_code(adj, vertex, parent=-1):
    return '(' + ''.join(sorted(rooted_code(adj, w, vertex)
                                   for w in adj[vertex] if w != parent)) + ')'


def canonical_code(adj):
    return min(rooted_code(adj, c) for c in center_vertices(adj))


def all_unlabelled_trees(max_n):
    trees = {1: [(( ),)]}
    for n in range(2, max_n+1):
        distinct = {}
        for adj in trees[n-1]:
            for vertex in range(n-1):
                new = [list(row) for row in adj] + [[vertex]]
                new[vertex].append(n-1)
                new = tuple(tuple(sorted(row)) for row in new)
                distinct.setdefault(canonical_code(new), new)
        trees[n] = [distinct[key] for key in sorted(distinct)]
    return trees


def transition(state, adj):
    for v, neighbors in enumerate(adj):
        on = sum((state >> w) & 1 for w in neighbors)
        old = (state >> v) & 1
        new = int(on >= old + 1)
        state = (state & ~(1 << v)) | (new << v)
    return state


def cycles(adj):
    n = len(adj)
    next_state = [transition(s, adj) for s in range(1 << n)]
    visited = bytearray(1 << n)
    counts = Counter()
    witnesses = {}
    for start in range(1 << n):
        if visited[start]:
            continue
        trail, index = [], {}
        s = start
        while not visited[s] and s not in index:
            index[s] = len(trail)
            trail.append(s)
            s = next_state[s]
        if s in index:
            orbit = tuple(trail[index[s]:])
            counts[len(orbit)] += 1
            witnesses.setdefault(len(orbit), orbit)
        for x in trail:
            visited[x] = 1
    return counts, witnesses


def edges(adj):
    return [(i,j) for i,row in enumerate(adj) for j in row if i < j]


def compute(max_n=10):
    alltrees = all_unlabelled_trees(max_n)
    summary = {}
    all_22 = []
    for n in range(1, max_n+1):
        counts, maximum, winners = Counter(), 0, []
        for adj in alltrees[n]:
            orbits, witnesses = cycles(adj)
            counts.update(orbits)
            p = max(orbits) if orbits else 0
            if p > maximum:
                maximum, winners = p, [(adj, orbits, witnesses)]
            elif p == maximum:
                winners.append((adj, orbits, witnesses))
            if n == 10 and 22 in orbits:
                all_22.append((adj, orbits[22], witnesses[22]))
        summary[n] = (len(alltrees[n]), maximum, len(winners), dict(sorted(counts.items())))
    return summary, all_22


def main():
    summary, winners = compute()
    for n, (number, period, winner_count, census) in summary.items():
        print(f'n={n} trees={number} max_period={period} maximizing_trees={winner_count} cycle_census={census}')
    assert [summary[n][0] for n in range(1, 11)] == [1,1,1,2,3,6,11,23,47,106]
    assert [summary[n][1] for n in range(1, 11)] == [1,1,1,1,2,3,6,10,14,22]
    assert len(winners) == 1 and winners[0][1] == 2
    adj, count, example = winners[0]
    print('unique_10_vertex_22_period_tree_edges', edges(adj))
    print('number_22_cycles', count)
    print('witness_22_cycle_states', list(example))
    assert len(set(example)) == 22
    assert all(transition(example[i], adj) == example[(i+1)%22] for i in range(22))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
