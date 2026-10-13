"""Exact finite corroboration; the general theorem rests on its proof."""
import itertools
import json

def graph(p, q, k):
    # Left attachment is 0, right attachment is p.
    adj = [set() for _ in range(p + q + k)]
    def edge(a, b):
        adj[a].add(b)
        adj[b].add(a)
    for base, length in [(0, p), (p, q)]:
        for i in range(length):
            edge(base + i, base + (i + 1) % length)
    connector = [0] + list(range(p + q, p + q + k)) + [p]
    for a, b in zip(connector, connector[1:]):
        edge(a, b)
    return adj

def refinement(adj, right):
    colors = [0] * len(adj)
    split = None
    for round_number in range(1, len(adj) + 2):
        keys = [(colors[v], tuple(sorted(colors[u] for u in neighbors)))
                for v, neighbors in enumerate(adj)]
        ids = {key: i for i, key in enumerate(dict.fromkeys(keys))}
        updated = [ids[key] for key in keys]
        if split is None and updated[0] != updated[right]:
            split = round_number
        if len(set(updated)) == len(set(colors)):
            return updated, split
        colors = updated
    raise AssertionError('refinement did not stabilize')

def expected_orbits(p, q, k):
    labels = []
    for base, length, kind in [(0, p, 'left'), (p, q, 'right')]:
        for i in range(length):
            if i == 0:
                labels.append(('attachment', 0 if p == q else kind))
            else:
                labels.append(('cycle' if p == q else kind, min(i, length - i)))
    for j in range(1, k + 1):
        labels.append(('connector', min(j, k + 1 - j) if p == q else j))
    return labels

def partition_pairs(labels):
    return {(i, j) for i in range(len(labels)) for j in range(i)
            if labels[i] == labels[j]}

def dumbbell_checks():
    orbit_checks = split_checks = balanced_checks = 0
    for p in range(3, 19):
        for q in range(3, 19):
            for k in range(51):
                colors, split = refinement(graph(p, q, k), p)
                refinable = partition_pairs(colors) == partition_pairs(expected_orbits(p, q, k))
                assert refinable == (not (p == q == k + 1)), (p, q, k)
                orbit_checks += 1
                if p != q:
                    assert split == min(p, q) + 1, (p, q, k, split)
                    split_checks += 1
                elif p == k + 1:
                    sizes = sorted(colors.count(c) for c in set(colors))
                    wanted = [2] + [6] * ((p - 1) // 2) + ([3] if p % 2 == 0 else [])
                    assert sizes == sorted(wanted), (p, sizes)
                    balanced_checks += 1
    return dict(orbit_checks=orbit_checks, split_checks=split_checks,
                balanced_partition_checks=balanced_checks)

if __name__ == '__main__':
    print(json.dumps(dumbbell_checks()))
