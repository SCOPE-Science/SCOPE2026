"""Enumerate unlabelled rooted forests and test one-dimensional refinement."""
from collections import Counter, defaultdict
from functools import lru_cache
import networkx as nx

@lru_cache(None)
def forests(n, minimum=''):
    if n == 0:
        return ((),)
    answer = []
    for size in range(1, n + 1):
        for tree in trees(size):
            if tree < minimum:
                continue
            for remainder in forests(n - size, tree):
                answer.append((tree,) + remainder)
    return tuple(answer)

@lru_cache(None)
def trees(n):
    return tuple('(' + ''.join(branches) + ')' for branches in forests(n - 1))

def graph_from_forest(forest):
    graph = nx.Graph()
    count = [0]
    def visit(tree, ancestors):
        node = count[0]
        count[0] += 1
        graph.add_node(node)
        graph.add_edges_from((node, x) for x in ancestors)
        position = 1
        while position < len(tree) - 1:
            depth, endpoint = 1, position + 1
            while depth:
                depth += 1 if tree[endpoint] == '(' else -1
                endpoint += 1
            visit(tree[position:endpoint], ancestors + (node,))
            position = endpoint
    for tree in forest:
        visit(tree, ())
    return graph

def refinement(graph):
    colors = {v: 0 for v in graph}
    while True:
        signatures = {v: (colors[v], tuple(sorted(Counter(colors[w] for w in graph[v]).items()))) for v in graph}
        indices = {signature: i for i, signature in enumerate(sorted(set(signatures.values())))}
        updated = {v: indices[signatures[v]] for v in graph}
        if updated == colors:
            return colors
        colors = updated

def same_orbit(graph, x, y):
    left, right = graph.copy(), graph.copy()
    nx.set_node_attributes(left, 0, 'mark')
    nx.set_node_attributes(right, 0, 'mark')
    left.nodes[x]['mark'] = 1
    right.nodes[y]['mark'] = 1
    return nx.is_isomorphic(left, right, node_match=nx.algorithms.isomorphism.categorical_node_match('mark', 0))

def verify(maximum=11):
    counts = []
    tested = 0
    for size in range(1, maximum + 1):
        encodings = forests(size)
        counts.append(len(encodings))
        for encoding in encodings:
            graph = graph_from_forest(encoding)
            assert len(graph) == size
            colors = refinement(graph)
            classes = defaultdict(list)
            for vertex, color in colors.items():
                classes[color].append(vertex)
            for vertices in classes.values():
                for candidate in vertices[1:]:
                    assert same_orbit(graph, vertices[0], candidate), (encoding, vertices)
                    tested += 1
    return counts, tested

if __name__ == '__main__':
    counts, tested = verify()
    print('forest_counts_1_to_11=' + ','.join(map(str, counts)))
    print('same_colour_orbit_checks=' + str(tested))
    print('PASS')
