"""Exact certificate for the first maximal-independent-set VC/Littlestone gap on forests.

Requires only Python 3.9+. Enumerates all unlabelled trees on <=8 vertices.
A maximal independent set is encoded by its binary membership mask.
"""
from functools import lru_cache

COUNTS = (1, 1, 1, 2, 3, 6, 11, 23)
SPIDER_EDGES = ((0, 1), (0, 2), (2, 3), (0, 4), (4, 5), (5, 6), (6, 7))


def canonical_tree(n, edges):
    neighbors = [set() for _ in range(n)]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)

    def root_code(v, parent):
        subtrees = sorted(root_code(w, v) for w in neighbors[v] if w != parent)
        return '(' + ''.join(subtrees) + ')'

    alive = set(range(n))
    while len(alive) > 2:
        leaves = {v for v in alive if len(neighbors[v] & alive) <= 1}
        alive -= leaves
    centers = sorted(alive)
    if len(centers) == 1:
        return '{' + root_code(centers[0], -1) + '}'
    left, right = centers
    parts = sorted((root_code(left, right), root_code(right, left)))
    return '[' + ''.join(parts) + ']'


def all_trees_through(order):
    classes = {1: {canonical_tree(1, ()): ()}}
    for n in range(2, order + 1):
        next_classes = {}
        for old_edges in classes[n - 1].values():
            for v in range(n - 1):
                new_edges = old_edges + ((v, n - 1),)
                code = canonical_tree(n, new_edges)
                next_classes.setdefault(code, new_edges)
        classes[n] = next_classes
    return classes


def maximal_independent_masks(n, edges):
    neighbors = [0] * n
    for a, b in edges:
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a
    result = []
    for s in range(1 << n):
        if any((s >> i) & 1 and (s & neighbors[i]) for i in range(n)):
            continue
        if any(not ((s >> i) & 1) and not (s & neighbors[i]) for i in range(n)):
            continue
        result.append(s)
    return tuple(result)


def vc_dimension(n, masks):
    maximum = 0
    for support in range(1 << n):
        k = support.bit_count()
        if k > maximum and (1 << k) <= len(masks):
            traces = {s & support for s in masks}
            if len(traces) == (1 << k):
                maximum = k
    return maximum


def littlestone_dimension(n, masks):
    @lru_cache(None)
    def rank(remaining):
        if remaining.bit_count() <= 1:
            return 0
        best = 0
        for v in range(n):
            yes = sum(1 << i for i, s in enumerate(masks)
                      if (remaining >> i) & 1 and (s >> v) & 1)
            no = remaining & ~yes
            if yes and no:
                best = max(best, 1 + min(rank(no), rank(yes)))
        return best
    return rank((1 << len(masks)) - 1)


def depth_three_witness(n, masks):
    @lru_cache(None)
    def rank(remaining):
        if remaining.bit_count() <= 1:
            return 0
        choices = []
        for v in range(n):
            yes = sum(1 << i for i, s in enumerate(masks)
                      if (remaining >> i) & 1 and (s >> v) & 1)
            no = remaining & ~yes
            if yes and no:
                choices.append(1 + min(rank(no), rank(yes)))
        return max(choices, default=0)

    def build(remaining, level):
        if level == 0:
            assert remaining.bit_count() == 1
            return next(i for i in range(len(masks)) if (remaining >> i) & 1)
        for v in range(n):
            yes = sum(1 << i for i, s in enumerate(masks)
                      if (remaining >> i) & 1 and (s >> v) & 1)
            no = remaining & ~yes
            if yes and no and rank(yes) >= level - 1 and rank(no) >= level - 1:
                return (v, build(no, level - 1), build(yes, level - 1))
        raise AssertionError('no witness')

    result = build((1 << len(masks)) - 1, 3)
    seen = []
    def test(node, decisions):
        if isinstance(node, int):
            seen.append(node)
            for v, answer in decisions:
                assert (masks[node] >> v) & 1 == answer
            return
        v, no, yes = node
        test(no, decisions + ((v, 0),))
        test(yes, decisions + ((v, 1),))
    test(result, ())
    assert len(seen) == 8 and set(seen) == set(range(8))
    return result


def main():
    classes = all_trees_through(8)
    assert tuple(len(classes[n]) for n in range(1, 9)) == COUNTS
    exceptional = []
    for n in range(1, 9):
        pairs = []
        for code, edges in classes[n].items():
            masks = maximal_independent_masks(n, edges)
            vc = vc_dimension(n, masks)
            lit = littlestone_dimension(n, masks)
            assert vc <= lit <= (len(masks).bit_length() - 1)
            pairs.append((vc, lit))
            if lit > vc:
                exceptional.append((n, code, vc, lit, len(masks)))
        print('n=%d trees=%d gaps=%d dimension_pairs=%s' %
              (n, len(pairs), sum(a < b for a, b in pairs), sorted(set(pairs))))
    code = canonical_tree(8, SPIDER_EDGES)
    assert exceptional == [(8, code, 2, 3, 8)], exceptional
    masks = maximal_independent_masks(8, SPIDER_EDGES)
    assert len(masks) == 8
    support = (1 << 0) | (1 << 5)
    assert {s & support for s in masks} == {0, 1 << 0, 1 << 5, support}
    assert all(len({s & q for s in masks}) < 8
               for q in range(256) if q.bit_count() == 3)
    witness = depth_three_witness(8, masks)
    print('exceptional=spider(1,2,4), vc=2, ldim=3, mis_count=8')
    print('maximal_independent_masks=', list(masks))
    print('depth_three_witness=', witness)
    print('FOREST_MIS_FIRST_GAP_PASS')


if __name__ == '__main__':
    main()
