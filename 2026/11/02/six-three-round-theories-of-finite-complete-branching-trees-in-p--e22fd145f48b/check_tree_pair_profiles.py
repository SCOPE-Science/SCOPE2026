"""Checks the three-move tree-pair extension lemma on finite instances.

The infinite claim is established by the separate combinatorial proof; this
code checks its local pattern formulas without assuming logical equivalence.
"""
from collections import deque
from verify_full_tree_rank3 import complete_tree


def distances(adj, x):
    dist = [-1] * len(adj)
    dist[x] = 0
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for u in adj[v]:
            if dist[u] < 0:
                dist[u] = dist[v] + 1
                queue.append(u)
    return dist


def check_pair_formula(b, h):
    adj = complete_tree(b, h)
    n = len(adj)
    assert n > 2 * (b + 1) + 2
    dists = [distances(adj, x) for x in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y:
                continue
            d = dists[x][y]
            observed = {
                ((z in adj[x]), (z in adj[y]))
                for z in range(n) if z != x and z != y
            }
            predicted = {(False, False)}
            if d == 2:
                predicted.add((True, True))
            if d >= 3 or len(adj[x]) >= 2:
                predicted.add((True, False))
            if d >= 3 or len(adj[y]) >= 2:
                predicted.add((False, True))
            assert observed == predicted, (b, h, x, y, d, observed, predicted)
    return n


def check_four_point_types(b, h):
    adj = complete_tree(b, h)
    dd = [distances(adj, x) for x in range(len(adj))]
    patterns = set()
    for x in range(len(adj)):
        if len(adj[x]) == 1:
            label = 'leaf'
        else:
            has_leaf_at_one = any(len(adj[y]) == 1 for y in range(len(adj)) if dd[x][y] == 1)
            has_leaf_at_two = any(len(adj[y]) == 1 for y in range(len(adj)) if dd[x][y] == 2)
            label = ('internal', has_leaf_at_one, has_leaf_at_two)
            assert not (has_leaf_at_one and has_leaf_at_two)
        patterns.add(label)
    assert patterns == {'leaf', ('internal', True, False),
                        ('internal', False, True), ('internal', False, False)}


if __name__ == '__main__':
    for b, h in ((2, 3), (3, 3), (4, 3), (2, 4), (3, 4), (2, 5)):
        n = check_pair_formula(b, h)
        check_four_point_types(b, h)
        print('LOCAL_PAIR_PROFILE_OK', b, h, n)
    print('FOUR_POINTED_TYPES_OK')
