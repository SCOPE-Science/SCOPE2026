#!/usr/bin/env python3
"""Exact checks for leaf-path online shattering on rooted trees.

Only the Python standard library is required. The all-order proof is mathematical;
these independent finite checks test the formula and its extremal witnesses.
"""
from functools import lru_cache
from collections import defaultdict
from math import log2


def materialize(shape):
    children = []
    def visit(s):
        u = len(children)
        children.append([])
        for sub in s:
            v = visit(sub)
            children[u].append(v)
        return u
    visit(shape)
    return children


def ld_exact(children):
    n = len(children)
    leaves = [v for v, ch in enumerate(children) if not ch]
    leaf_index = {v: i for i, v in enumerate(leaves)}
    masks = [0] * n
    for v in range(n - 1, -1, -1):
        masks[v] = (1 << leaf_index[v]) if v in leaf_index else 0
        for w in children[v]:
            masks[v] |= masks[w]
    queries = tuple(sorted(set(masks)))
    @lru_cache(maxsize=None)
    def f(mask):
        best = 0
        for q in queries:
            yes = mask & q
            if yes and yes != mask:
                best = max(best, 1 + min(f(yes), f(mask ^ yes)))
        return best
    return f((1 << len(leaves)) - 1)


def enumerated_shapes(limit):
    by_n = {1: [()]}
    yield 1, by_n[1]
    for n in range(2, limit + 1):
        pool = []
        for sz in range(1, n):
            pool.extend((sz, s) for s in by_n[sz])
        answers = []
        def rec(rem, start, children):
            if rem == 0:
                answers.append(tuple(children))
                return
            for idx in range(start, len(pool)):
                sz, shape = pool[idx]
                if sz > rem:
                    break
                children.append(shape)
                rec(rem - sz, idx, children)
                children.pop()
        rec(n-1, 0, [])
        assert len(answers) == len(set(answers))
        by_n[n] = answers
        yield n, answers


def build_extremizer(depth):
    assert depth >= 1
    if depth == 1:
        return [[1, 2], [], []], 0, (1, [2, 1])
    b, root_b, cert_b = build_extremizer(depth - 1)
    a, root_a, cert_a = build_extremizer(depth - 1)
    shift = len(b)
    graph = [list(v) for v in b]
    graph.extend([[x+shift for x in v] for v in a])
    graph[root_b].append(root_a + shift)
    def shift_cert(c):
        if isinstance(c, int):
            return c + shift
        q, children = c
        return (q + shift, [shift_cert(children[0]), shift_cert(children[1])])
    return graph, root_b, (root_a+shift, [cert_b, shift_cert(cert_a)])


def verify_certificate(graph, root, cert, depth):
    assert root == 0
    parents = [-1]*len(graph)
    for u, successors in enumerate(graph):
        for v in successors:
            parents[v] = u
    leaves = [v for v in range(len(graph)) if not graph[v]]
    def in_path(v, leaf):
        w = leaf
        while w >= 0:
            if w == v:
                return True
            w = parents[w]
        return False
    def go(node, hypotheses, left):
        if left == 0:
            assert isinstance(node, int)
            assert len(hypotheses) == 1 and node == hypotheses[0]
            return 1
        assert isinstance(node, tuple)
        query, (zero, one) = node
        neg = [h for h in hypotheses if not in_path(query, h)]
        pos = [h for h in hypotheses if in_path(query, h)]
        assert neg and pos
        return go(zero, neg, left-1) + go(one, pos, left-1)
    paths = go(cert, leaves, depth)
    assert paths == 2**depth
    if depth <= 3:
        assert ld_exact(graph) == depth
    assert len(graph) == 3*(2**(depth-1))
    assert len(leaves) == 2**depth
    assert len(graph)-len(leaves) == 2**(depth-1)
    print('CERTIFICATE',depth,'vertices',len(graph),'leaves',len(leaves),'paths',paths)


def main():
    # A separate recurrence, not the structural bound, computes exact dimensions.
    for n, shapes in enumerated_shapes(12):
        observed = defaultdict(int)
        maxdim = 0
        for shape in shapes:
            graph = materialize(shape)
            leaves = sum(not xs for xs in graph)
            internal = n - leaves
            d = ld_exact(graph)
            observed[(internal, leaves)] = max(observed[(internal, leaves)], d)
            maxdim = max(maxdim, d)
        for (internal, leaves), d in observed.items():
            expected = 0 if internal == 0 else min(leaves.bit_length()-1, internal.bit_length())
            assert d == expected, (n, internal, leaves, d, expected)
        expected_n = 0 if n < 3 else 1 + int(log2(n / 3))
        assert maxdim == expected_n, (n, maxdim, expected_n)
        print('ENUM',n,'rooted_unlabeled',len(shapes),'parameter_pairs',len(observed),'max_dimension',maxdim)
    for d in range(1, 6):
        graph, root, cert = build_extremizer(d)
        verify_certificate(graph, root, cert, d)
    print('ALL_EXACT_CHECKS_PASS')


if __name__ == '__main__':
    main()
