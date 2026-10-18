#!/usr/bin/env python3
"""Exact colour-refinement census of connected P4-free graphs to order 12.

Standalone Python 3 standard-library verifier. Running the script enumerates
unlabeled connected cographs via their unique reduced cotrees. The code
compares the color histograms after n globally coordinated WL rounds.
"""
from collections import Counter, defaultdict
from functools import lru_cache

LEAF = ('leaf',)

@lru_cache(None)
def cotrees(n, op):
    """All unordered reduced cotrees with n leaves and root op.

    A root labelled 0 means disjoint union, 1 means graph join, while
    a leaf has no internal label (op=2). All internal nodes have at least
    two children, and internal parent-child labels alternate.
    """
    if n == 1:
        return (LEAF,) if op == 2 else ()
    if op == 2:
        return ()
    children = sorted((size, t)
                      for size in range(1, n)
                      for t in cotrees(size, 2 if size == 1 else 1-op))
    output = []
    def visit(first, remaining, selected):
        if remaining == 0:
            if len(selected) >= 2:
                output.append((op, tuple(selected)))
            return
        for k in range(first, len(children)):
            size, t = children[k]
            if size > remaining:
                break
            visit(k, remaining - size, selected + [(size, t)])
    visit(0, n, [])
    return tuple(output)

@lru_cache(None)
def adjacency(tree):
    """Adjacency rows as integers, with bit j representing vertex j."""
    if tree == LEAF:
        return (0,)
    op, children = tree
    n = sum(size for size, _ in children)
    rows = [0]*n
    offset = 0
    for size, sub in children:
        a = adjacency(sub)
        for i in range(size):
            rows[offset+i] = a[i] << offset
        offset += size
    if op == 1:
        offset = 0
        for size, _ in children:
            outside = ((1 << n) - 1) ^ (((1 << size) - 1) << offset)
            for i in range(offset, offset+size):
                rows[i] |= outside
            offset += size
    return tuple(rows)

def wl_histograms(trees, n):
    """Color histograms after n simultaneous 1-WL rounds.

    A single globally shared color dictionary ensures that IDs computed
    on different graphs are genuinely comparable, just as when running
    color refinement on the disjoint union of the graphs.
    """
    graphs = [adjacency(t) for t in trees]
    colors = [[0]*n for _ in graphs]
    for _ in range(n):
        features = []
        for graph, old in zip(graphs, colors):
            one = []
            for v, bits in enumerate(graph):
                neighbors = tuple(sorted(old[w] for w in range(n)
                                         if (bits >> w) & 1))
                one.append((old[v], neighbors))
            features.append(one)
        all_features = sorted({feature for one in features for feature in one})
        dictionary = {feature: color for color, feature in enumerate(all_features)}
        colors = [[dictionary[feature] for feature in one] for one in features]
    return [tuple(sorted(Counter(one).items())) for one in colors]

def complement_components(rows):
    n = len(rows)
    all_bits = (1 << n)-1
    unseen = set(range(n))
    sizes = []
    while unseen:
        todo = [min(unseen)]
        unseen.remove(todo[0])
        count = 0
        while todo:
            v = todo.pop()
            count += 1
            comp = (all_bits ^ rows[v]) & ~(1 << v)
            new = [u for u in tuple(unseen) if (comp >> u) & 1]
            for u in new:
                unseen.remove(u)
                todo.append(u)
        sizes.append(count)
    return tuple(sorted(sizes))

def graph_components(rows, complement=False):
    """Connected-component vertex lists of a graph or its complement."""
    n = len(rows)
    total = (1 << n) - 1
    unseen = set(range(n))
    parts = []
    while unseen:
        start = min(unseen)
        todo = [start]
        unseen.remove(start)
        part = []
        while todo:
            v = todo.pop()
            part.append(v)
            mask = total ^ rows[v] ^ (1 << v) if complement else rows[v]
            new = [w for w in tuple(unseen) if (mask >> w) & 1]
            for w in new:
                unseen.remove(w)
                todo.append(w)
        parts.append(tuple(sorted(part)))
    return parts

def restrict_graph(rows, indices):
    return tuple(sum(((rows[i] >> j) & 1) << k
                     for k, j in enumerate(indices)) for i in indices)

def canonical_cotree(rows):
    """Canonical unlabeled cograph signature from connectivity decomposition."""
    if len(rows) == 1:
        return LEAF
    comp = graph_components(rows)
    if len(comp) > 1:
        return (0, tuple(sorted((len(part), canonical_cotree(restrict_graph(rows, part)))
                                for part in comp)))
    comp = graph_components(rows, complement=True)
    if len(comp) > 1:
        return (1, tuple(sorted((len(part), canonical_cotree(restrict_graph(rows, part)))
                                for part in comp)))
    raise ValueError('Graph is not a cograph')

def union(*graphs):
    rows = []
    shift = 0
    for graph in graphs:
        rows.extend(bits << shift for bits in graph)
        shift += len(graph)
    return tuple(rows)

def join(*graphs):
    rows = list(union(*graphs))
    total = (1 << len(rows)) - 1
    offset = 0
    for graph in graphs:
        k = len(graph)
        out = total ^ (((1 << k)-1) << offset)
        for j in range(offset, offset + k):
            rows[j] |= out
        offset += k
    return tuple(rows)

def complement(graph):
    n = len(graph)
    return tuple(((1 << n) - 1) ^ graph[i] ^ (1 << i)
                 for i in range(n))

def clique(n):
    return complement((0,) * n)

def edgeless(n):
    return (0,) * n

def copies(n, graph):
    return union(*(graph for _ in range(n)))

def complete_multipartite(*sizes):
    return join(*(edgeless(s) for s in sizes))

def named_witnesses():
    return {
        7: (
            complement(union(clique(5), join(edgeless(3), copies(2, clique(2))))),
            complement(copies(2, complete_multipartite(2,2,2))),
        ),
        8: (
            complement(copies(3, clique(4))),
            complement(copies(2, complete_multipartite(3,3))),
        ),
        9: (
            complement(copies(4, clique(3))),
            complement(copies(3, complete_multipartite(2,2))),
        ),
    }

def verify():
    expected_cographs = (1, 1, 2, 5, 12, 33, 90, 261,
                         766, 2312, 7068, 21965)
    observed = []
    observed_ambiguous = {}
    observed_cotrees = {}
    for n in range(1, 13):
        trees = cotrees(1, 2) if n == 1 else cotrees(n, 1)
        count = len(trees)
        observed.append(count)
        assert count == expected_cographs[n-1], (n, count)
        if n == 1:
            continue
        hist = wl_histograms(trees, n)
        groups = defaultdict(list)
        for t, signature in zip(trees, hist):
            groups[signature].append(t)
        bad = [g for g in groups.values() if len(g) > 1]
        if n < 12:
            assert not bad, (n, len(bad))
        else:
            assert len(bad) == 3 and all(len(g) == 2 for g in bad), [len(g) for g in bad]
            for pair in bad:
                a, b = (adjacency(t) for t in pair)
                assert all(x.bit_count() == a[0].bit_count() for x in a)
                assert all(x.bit_count() == b[0].bit_count() for x in b)
                degree = a[0].bit_count()
                assert degree == b[0].bit_count()
                sig = tuple(sorted((complement_components(a),
                                    complement_components(b))))
                observed_ambiguous[degree] = sig
                observed_cotrees[degree] = {t for t in pair}
        print(f'n={n}: connected_cographs={count}, ambiguous_classes={len(bad)}')
    assert tuple(observed) == expected_cographs
    expected_pairs = {
        7: ((5,7), (6,6)),
        8: ((4,4,4), (6,6)),
        9: ((3,3,3,3), (4,4,4)),
    }
    assert observed_ambiguous == expected_pairs, observed_ambiguous
    for degree, pair in named_witnesses().items():
        assert {canonical_cotree(g) for g in pair} == observed_cotrees[degree]
        assert canonical_cotree(pair[0]) != canonical_cotree(pair[1])
    print("NAMED_WITNESSES_VERIFIED")
    for degree, sizes in sorted(observed_ambiguous.items()):
        print(f'degree={degree}: complement_component_orders={sizes}')
    print('CENSUS_VERIFIED')

if __name__ == '__main__':
    verify()
