#!/usr/bin/env python3
"""Independent finite checks for distributivity in near-complete formal contexts.
Uses only the Python standard library. Run: python3 verify.py
"""
from collections import Counter
from itertools import product


def concepts_from_missing(n_obj, n_attr, missing_edges):
    """Enumerate closed extents directly from incidence (the complement of missing_edges)."""
    rows = [(1 << n_attr) - 1 for _ in range(n_obj)]
    for i, j in missing_edges:
        rows[i] &= ~(1 << j)
    extents = set()
    for subset in range(1 << n_obj):
        common = (1 << n_attr) - 1
        for i in range(n_obj):
            if (subset >> i) & 1:
                common &= rows[i]
        closure = sum(1 << i for i in range(n_obj) if rows[i] & common == common)
        extents.add(closure)
    return frozenset(extents)


def is_distributive(extents):
    ex = sorted(extents)
    joins = {}
    for a in ex:
        for b in ex:
            upper = [c for c in ex if (c & (a | b)) == (a | b)]
            assert upper
            join = min(upper, key=int.bit_count)
            assert all((join & c) == join for c in upper)
            joins[a, b] = join
    for a in ex:
        for b in ex:
            for c in ex:
                if (a & joins[b, c]) != joins[a & b, a & c]:
                    return False
    return True


def prufer_edges(n, word):
    if n == 1:
        return []
    degrees = [1] * n
    for x in word:
        degrees[x] += 1
    edges = []
    for x in word:
        leaf = next(i for i in range(n) if degrees[i] == 1)
        edges.append((leaf, x))
        degrees[leaf] -= 1
        degrees[x] -= 1
    a, b = [i for i in range(n) if degrees[i] == 1]
    edges.append((a, b))
    return edges


def bipartition_tree(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    colors = {0: 0}
    stack = [0]
    while stack:
        a = stack.pop()
        for b in adj[a]:
            if b not in colors:
                colors[b] = 1 - colors[a]
                stack.append(b)
            else:
                assert colors[b] == 1 - colors[a]
    assert len(colors) == n
    left = [i for i in range(n) if colors[i] == 0]
    right = [i for i in range(n) if colors[i] == 1]
    li = {a: i for i, a in enumerate(left)}
    ri = {a: i for i, a in enumerate(right)}
    cross = {(li[a], ri[b]) if a in li else (li[b], ri[a]) for a, b in edges}
    return len(left), len(right), cross


def is_six_path(n, edges):
    degree = [0] * n
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    return n == 6 and sorted(degree) == [1, 1, 2, 2, 2, 2]


def verify_tree_classification():
    for n in range(1, 7):
        checked = 0
        nondistributive = 0
        path_count = 0
        profile = Counter()
        for word in product(range(n), repeat=max(0, n - 2)) if n >= 2 else [()]:
            edges = prufer_edges(n, word)
            left, right, missing = bipartition_tree(n, edges)
            extents = concepts_from_missing(left, right, missing)
            good = is_distributive(extents)
            path = is_six_path(n, edges)
            assert good == (not path), (n, word, edges, good)
            checked += 1
            nondistributive += (not good)
            path_count += path
            profile[(len(extents), good)] += 1
        assert checked == (n ** (n - 2) if n >= 2 else 1)
        assert nondistributive == (360 if n == 6 else 0)
        assert nondistributive == path_count
        print(f'TREE_{n}_OK labelled={checked} nondistributive={nondistributive} spectrum={sorted(profile.items())}')


def verify_three_by_three():
    count = Counter()
    for mask in range(1 << 9):
        missing = {(i, j) for i in range(3) for j in range(3) if (mask >> (3*i+j)) & 1}
        good = is_distributive(concepts_from_missing(3, 3, missing))
        count[(len(missing), good)] += 1
    assert sum(count.values()) == 512
    assert {e:c for (e,good),c in count.items() if not good} == {5:36, 6:6}
    print(f'CONTEXT_3x3_OK 512 masks; nondistributive_by_missing_edges={dict(sorted((e,c) for (e,g),c in count.items() if not g))}')


def verify_product():
    # The disjoint union of a six-vertex path and a single isolated missing edge.
    six_path = {(0,0),(1,0),(1,1),(2,1),(2,2)}
    one_edge = {(0,0)}
    c1 = concepts_from_missing(3,3,six_path)
    c2 = concepts_from_missing(1,1,one_edge)
    union = set(six_path) | {(i+3,j+3) for i,j in one_edge}
    cu = concepts_from_missing(4,4,union)
    assert len(c1) == 5 and len(c2) == 2 and len(cu) == 10
    assert not is_distributive(c1) and not is_distributive(cu)
    assert {((a & 7), (a >> 3) & 1) for a in cu} == set(product(c1,c2))
    print('PRODUCT_OK P6 x K2: 5 * 2 = 10 concepts; non-distributivity preserved')


if __name__ == '__main__':
    verify_tree_classification()
    verify_three_by_three()
    verify_product()
    print('VERIFY_OK')
