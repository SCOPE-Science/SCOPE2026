"""Exact graph/subset checks for the six-vertex cubic almost-independent-set theorem.
Run with Python 3 (standard library only)."""
from itertools import combinations
from collections import Counter
from math import comb

V = tuple(range(6))
ALL_EDGES = tuple(combinations(V, 2))


def edge_distribution(edges):
    """Count all labelled vertex subsets by the number of induced edges."""
    out = [0] * (len(edges) + 1)
    for mask in range(1 << 6):
        internal = sum(((mask >> u) & 1) * ((mask >> v) & 1)
                       for (u, v) in edges)
        out[internal] += 1
    return tuple(out)


def complement_cycles(edges):
    """Lengths of the degree-two components of the six-vertex complement."""
    selected = set(edges)
    missing = set(ALL_EDGES) - selected
    adj = {u: set() for u in V}
    for u, v in missing:
        adj[u].add(v)
        adj[v].add(u)
    assert all(len(adj[u]) == 2 for u in V)
    unseen = set(V)
    lengths = []
    while unseen:
        start = next(iter(unseen))
        stack = [start]
        component = set()
        while stack:
            u = stack.pop()
            if u in component:
                continue
            component.add(u)
            stack.extend(adj[u] - component)
        unseen -= component
        lengths.append(len(component))
    return tuple(sorted(lengths))


K33 = tuple((i, j) for i in range(3) for j in range(3, 6))
PRISM = tuple([(i, (i + 1) % 3) for i in range(3)]
              + [(i + 3, (i + 1) % 3 + 3) for i in range(3)]
              + [(i, i + 3) for i in range(3)])


def distribution_closed_form_k33():
    out = [0] * 10
    for a in range(4):
        for b in range(4):
            out[a * b] += comb(3, a) * comb(3, b)
    return tuple(out)


def distribution_by_size_prism():
    """Alternative enumeration: choose subsets by their two triangle layers."""
    out = [0] * 10
    A = range(3)
    for amask in range(8):
        a = amask.bit_count()
        for bmask in range(8):
            b = bmask.bit_count()
            matching = (amask & bmask).bit_count()
            internal = comb(a, 2) + comb(b, 2) + matching
            out[internal] += 1
    return tuple(out)


assert distribution_closed_form_k33() == edge_distribution(K33)
assert distribution_by_size_prism() == edge_distribution(PRISM)
k = edge_distribution(K33)
p = edge_distribution(PRISM)
expect_k = (15, 9, 18, 6, 9, 0, 6, 0, 0, 1)
expect_p = (13, 15, 12, 8, 9, 0, 6, 0, 0, 1)
assert k == expect_k and p == expect_p
assert tuple(p[i] - k[i] for i in range(10)) == (-2, 6, -6, 2, 0, 0, 0, 0, 0, 0)
assert sum(k) == sum(p) == 64
assert sum(k[:2]) == 24 and sum(p[:2]) == 28
assert [sum(p[:r+1]) - sum(k[:r+1]) for r in range(10)] == [-2, 4, -2, 0, 0, 0, 0, 0, 0, 0]

# All labelled simple cubic graphs on six specified vertices (choose nine of 15 edges).
counts = Counter()
for edges in combinations(ALL_EDGES, 9):
    deg = [0] * 6
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    if any(x != 3 for x in deg):
        continue
    type_ = complement_cycles(edges)
    assert type_ in ((3, 3), (6,))
    observed = edge_distribution(edges)
    assert observed == (expect_k if type_ == (3, 3) else expect_p)
    counts[type_] += 1
assert counts == {(3, 3): 10, (6,): 60}
# The only simple two-regular graph on four vertices is C4; thus no smaller
# admissible instance (d >= 2 and 2d dividing n) can yield a counterexample.
print('CUBIC_LABELLED_GRAPHS_OK', dict(counts))
print('EDGE_COUNT_DISTRIBUTIONS_OK', 'K33=', k, 'PRISM=', p)
print('PHASE_DIAGRAM_OK', [-2, 4, -2, 0])
print('EXACT_COUNTEREXAMPLE_OK', 28, '>', 24)
print('VERIFY_OK')
