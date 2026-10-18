"""Independent forbidden-subgraph graph-atlas verification up to seven vertices."""
from collections import Counter, defaultdict
from itertools import combinations
import networkx as nx

def is_trivially_perfect(graph):
    for subset in combinations(graph, 4):
        induced = graph.subgraph(subset)
        degrees = sorted(dict(induced.degree()).values())
        if degrees == [1, 1, 2, 2] and induced.number_of_edges() == 3:
            return False  # Induced path of length three.
        if degrees == [2, 2, 2, 2] and induced.number_of_edges() == 4:
            return False  # Induced quadrangle.
    return True

def partition(graph):
    old = {v: 0 for v in graph}
    for _ in range(len(graph) + 1):
        fingerprints = {v: (old[v], tuple(sorted(Counter(old[w] for w in graph[v]).items()))) for v in graph}
        symbols = {s: k for k, s in enumerate(sorted(set(fingerprints.values())))}
        new = {v: symbols[fingerprints[v]] for v in graph}
        if new == old:
            return new
        old = new
    raise AssertionError('No stable partition')

def is_automorphic(graph, first, second):
    # Test an isomorphism between two individually coloured copies.
    a, b = graph.copy(), graph.copy()
    nx.set_node_attributes(a, 0, 'tag')
    nx.set_node_attributes(b, 0, 'tag')
    a.nodes[first]['tag'] = b.nodes[second]['tag'] = 1
    return nx.is_isomorphic(a, b, node_match=lambda x, y: x['tag'] == y['tag'])

if __name__ == '__main__':
    result = Counter()
    tests = 0
    for graph in nx.graph_atlas_g():
        n = len(graph)
        if not n or not is_trivially_perfect(graph):
            continue
        result[n] += 1
        cols = partition(graph)
        color_classes = defaultdict(list)
        for v, color in cols.items():
            color_classes[color].append(v)
        for cell in color_classes.values():
            for other in cell[1:]:
                assert is_automorphic(graph, cell[0], other)
                tests += 1
    print('atlas_counts_1_to_7=' + ','.join(str(result[k]) for k in range(1, 8)))
    print('same_colour_orbit_checks=' + str(tests))
    print('PASS')
