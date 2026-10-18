"""Finite exhaustive corroboration of equal-arm theta edge-general-position sets.

Run: python3 theta_verify.py
The accompanying mathematical proof, not these finite tests, establishes the theorem.
"""

from collections import deque
from itertools import combinations, product


def graph(m, length):
    if m < 3 or length < 2:
        raise ValueError('m>=3 and length>=2 required')
    adj = {0: [], 1: []}
    edges = []
    for arm in range(m):
        verts = [0] + [(arm, j) for j in range(1, length)] + [1]
        for j in range(length):
            x, y = verts[j:j + 2]
            idx = len(edges)
            edges.append((x, y))
            adj.setdefault(x, []).append((y, idx))
            adj.setdefault(y, []).append((x, idx))
    return adj, edges


def shortest_path_edge_masks(m, length):
    adj, edges = graph(m, length)
    vertices = list(adj)
    paths = set()
    for index, source in enumerate(vertices):
        distance = {source: 0}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, _ in adj[u]:
                if v not in distance:
                    distance[v] = distance[u] + 1
                    queue.append(v)

        def enumerate_backtracks(v, path_mask):
            if v == source:
                paths.add(path_mask)
                return
            for w, e in adj[v]:
                if distance[w] == distance[v] - 1:
                    enumerate_backtracks(w, path_mask | (1 << e))

        for target in vertices[index + 1:]:
            enumerate_backtracks(target, 0)
    return tuple(paths)


def feasible(edge_mask, geodesics):
    return all((edge_mask & path_mask).bit_count() <= 2 for path_mask in geodesics)


def predicted_sets(m, length):
    answers = set()
    for a in range(1, length // 2 + 1):
        b = length + 1 - a
        bits = 0
        for arm in range(m):
            for j in (a, b):
                bits |= 1 << (arm * length + j - 1)
        answers.add(bits)
    return answers


def exhaustive_maximum_sets(m, length, geodesics):
    edges = m * length
    answers = set()
    for chosen in combinations(range(edges), 2 * m):
        mask = sum(1 << edge for edge in chosen)
        if feasible(mask, geodesics):
            answers.add(mask)
    return answers


def all_two_per_arm(m, length, geodesics):
    choices = []
    for arm in range(m):
        choices.append([sum(1 << (arm * length + j - 1) for j in pair)
                        for pair in combinations(range(1, length + 1), 2)])
    answers = set()
    for candidate in product(*choices):
        mask = 0
        for arm_mask in candidate:
            mask |= arm_mask
        if feasible(mask, geodesics):
            answers.add(mask)
    return answers


def main():
    checked_path_sets = 0
    full_instances = 0
    arm_instances = 0
    constructed_instances = 0
    for m, length in ((3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (5, 2)):
        geo = shortest_path_edge_masks(m, length)
        observed = exhaustive_maximum_sets(m, length, geo)
        assert observed == predicted_sets(m, length), (m, length)
        checked_path_sets += len(geo)
        full_instances += 1
    for m, lengths in ((3, range(2, 8)), (4, range(2, 6)), (5, range(2, 5))):
        for length in lengths:
            geo = shortest_path_edge_masks(m, length)
            observed = all_two_per_arm(m, length, geo)
            assert observed == predicted_sets(m, length), (m, length)
            checked_path_sets += len(geo)
            arm_instances += 1
    for m in range(3, 8):
        for length in range(2, 13):
            geo = shortest_path_edge_masks(m, length)
            for mask in predicted_sets(m, length):
                assert feasible(mask, geo), (m, length)
                constructed_instances += 1
            checked_path_sets += len(geo)
    print('PASS: full edge-subset maxima on', full_instances, 'graphs')
    print('PASS: all two-per-arm candidates on', arm_instances, 'graphs')
    print('PASS: every predicted construction on', constructed_instances, 'parameter/position instances')
    print('Checked', checked_path_sets, 'geodesic masks (with repetitions across tests)')


if __name__ == '__main__':
    main()
