#!/usr/bin/env python3
"""Exact feedback-vertex-set transition census for the four-cube."""
from collections import Counter, deque
from itertools import combinations
import json

N = 16
ALL = (1 << N) - 1
EDGES = tuple((u, u ^ (1 << i)) for u in range(N) for i in range(4)
              if u < (u ^ (1 << i)))


def is_feedback_set(removed):
    retained = ALL ^ removed
    root = list(range(N))
    def find(x):
        while root[x] != x:
            x = root[x]
        return x
    for u, v in EDGES:
        if (retained >> u) & 1 and (retained >> v) & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            root[ru] = rv
    return True


def main():
    # Degree-four edge counting implies every feedback vertex set has size at least six.
    states = {6: [], 7: [], 8: []}
    for mask in range(1 << N):
        size = mask.bit_count()
        if size in states and is_feedback_set(mask):
            states[size].append(mask)
    assert len(states[6]) == 8
    present = {mask for size in states for mask in states[size]}
    adj = {mask: [] for mask in present}
    edge_levels = Counter()
    for mask in present:
        if mask.bit_count() == 8:
            continue
        for x in range(N):
            if not (mask >> x) & 1:
                upper = mask | (1 << x)
                if upper in present:
                    adj[mask].append(upper)
                    adj[upper].append(mask)
                    edge_levels[(mask.bit_count(), upper.bit_count())] += 1

    def component_sizes(cap):
        unseen = {mask for size in (6, 7, 8) if size <= cap for mask in states[size]}
        sizes = []
        while unseen:
            start = next(iter(unseen))
            unseen.remove(start)
            queue = [start]
            total = 0
            for item in queue:
                total += 1
                for other in adj[item]:
                    if other in unseen and other.bit_count() <= cap:
                        unseen.remove(other)
                        queue.append(other)
            sizes.append(total)
        return dict(sorted(Counter(sizes).items()))

    mins = sorted(states[6])
    def bfs(start):
        dst = {start: 0}
        parent = {start: None}
        todo = deque([start])
        while todo:
            mask = todo.popleft()
            for other in adj[mask]:
                if other not in dst:
                    dst[other] = dst[mask] + 1
                    parent[other] = mask
                    todo.append(other)
        return dst, parent

    path = (('add', 2), ('add', 7), ('remove', 6), ('add', 4),
            ('remove', 5), ('add', 11), ('remove', 3), ('add', 8),
            ('remove', 10), ('add', 13), ('remove', 9), ('remove', 12))
    walk = sum(1 << v for v in (3, 5, 6, 9, 10, 12))
    for action, vertex in path:
        before = walk
        if action == 'add':
            assert not (walk & (1 << vertex))
            walk |= 1 << vertex
        else:
            assert walk & (1 << vertex)
            walk ^= 1 << vertex
        assert 6 <= walk.bit_count() <= 8 and is_feedback_set(walk)
        assert walk in adj[before]
    assert walk == sum(1 << v for v in (2, 4, 7, 8, 11, 13))

    dist = {}
    for m in mins:
        dst, _ = bfs(m)
        assert len(dst) == len(present)
        for n in mins:
            if m < n:
                typ = 'same_parity' if (m & n) else 'opposite_parity'
                dist.setdefault(typ, []).append(dst[n])

    even = {v for v in range(N) if v.bit_count() % 2 == 0}
    odd = set(range(N)) - even
    predicted = {
        sum(1 << x for x in side if x not in (a, a ^ 15))
        for side in (even, odd)
        for a in side
    }
    assert set(mins) == predicted

    out = {
        'vertices': 16,
        'cube_edges': len(EDGES),
        'minimum_feedback_size': 6,
        'minimum_sets': mins,
        'layer_counts': {str(k): len(v) for k, v in states.items()},
        'tar_edges': {f'{a}-{b}': count for (a, b), count in sorted(edge_levels.items())},
        'components_cap_6': {str(k):v for k,v in component_sizes(6).items()},
        'components_cap_7': {str(k):v for k,v in component_sizes(7).items()},
        'components_cap_8': {str(k):v for k,v in component_sizes(8).items()},
        'min_set_pair_distance': {k:dict(sorted(Counter(v).items())) for k,v in dist.items()}
    }
    print(json.dumps(out, sort_keys=True))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
