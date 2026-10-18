"""Exact finite classification of orbit-refinement failures in connected outerplanar graphs of order at most 8.
Requires NetworkX 3.6.1. The 7-vertex graph atlas is complete up to isomorphism.
"""
import collections
import itertools
import json
import networkx as nx


def outerplanar(graph):
    h = graph.copy()
    apex = len(graph)
    h.add_node(apex)
    h.add_edges_from((apex, v) for v in graph)
    return nx.check_planarity(h, counterexample=False)[0]


def invariant(graph):
    degrees = dict(graph.degree())
    return (graph.number_of_edges(),
            tuple(sorted(degrees.values())),
            tuple(sorted(sum(degrees[w] for w in graph[v]) for v in graph)))


def stable_colours(graph):
    colours = {v: 0 for v in graph}
    while True:
        signatures = {
            v: (colours[v], tuple(sorted(collections.Counter(
                colours[w] for w in graph[v]).items()))) for v in graph
        }
        palette = {sig: i for i, sig in enumerate(sorted(set(signatures.values())))}
        refined = {v: palette[signatures[v]] for v in graph}
        if len(set(refined.values())) == len(set(colours.values())):
            return refined
        colours = refined


def orbit_labels(graph):
    parent = {v: v for v in graph}
    def representative(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for auto in nx.algorithms.isomorphism.GraphMatcher(graph, graph).isomorphisms_iter():
        for v, w in auto.items():
            parent[representative(v)] = representative(w)
    return {v: representative(v) for v in graph}


def is_failure(graph):
    colours = stable_colours(graph)
    orbits = orbit_labels(graph)
    return any(colours[a] == colours[b] and orbits[a] != orbits[b]
               for a in graph for b in graph), colours, orbits


def graph_edges(graph):
    return [[min(a,b), max(a,b)] for a,b in sorted(graph.edges())]


def up_to_seven(atlas):
    return {n: [g for g in atlas if len(g) == n and nx.is_connected(g) and outerplanar(g)]
            for n in range(1,8)}


def complete_eight(parents):
    buckets = collections.defaultdict(list)
    for graph in parents:
        for size in (1, 2):
            for neighbors in itertools.combinations(range(7), size):
                augmented = nx.Graph(graph)
                augmented.add_node(7)
                augmented.add_edges_from((7, v) for v in neighbors)
                if not outerplanar(augmented):
                    continue
                key = invariant(augmented)
                if not any(nx.is_isomorphic(augmented, old) for old in buckets[key]):
                    buckets[key].append(augmented)
    return [g for graphs in buckets.values() for g in graphs]


def main():
    all_by_n = up_to_seven(nx.graph_atlas_g())
    all_by_n[8] = complete_eight(all_by_n[7])
    population = []
    failures = []
    two_connected = []
    for n in range(1, 9):
        graphs = all_by_n[n]
        population.append(len(graphs))
        two_connected.append(sum(int(nx.is_biconnected(g)) for g in graphs if len(g)>2))
        for g in graphs:
            fail, colours, orbits = is_failure(g)
            if fail:
                failures.append({
                    'n': n, 'm':g.number_of_edges(),
                    'degree_sequence': sorted(d for v,d in g.degree()),
                    'edges': graph_edges(g),
                    'stable_partition': sorted([sorted([v for v in g if colours[v] == c])
                                               for c in set(colours.values())]),
                    'orbit_partition': sorted([sorted([v for v in g if orbits[v] == o])
                                              for o in set(orbits.values())]),
                    'is_2_connected': nx.is_biconnected(g),
                    'graph6': nx.to_graph6_bytes(g, header=False).decode().strip()
                })
    assert population == [1,1,2,5,13,46,172,777], population
    assert len(failures) == 4 and all(g['n'] == 8 for g in failures), failures
    assert sum(x['is_2_connected'] for x in failures) == 2
    # Canonical isomorphism classes, identified by their edge count and degree sequence.
    print(json.dumps({
        'population_by_order_1_to_8': population,
        'biconnected_counts_orders_1_to_8': two_connected,
        'failing_by_order_1_to_8': [sum(x['n']==n for x in failures) for n in range(1,9)],
        'counterexamples': sorted(failures, key=lambda x:(x['m'],x['degree_sequence']))
    }, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
