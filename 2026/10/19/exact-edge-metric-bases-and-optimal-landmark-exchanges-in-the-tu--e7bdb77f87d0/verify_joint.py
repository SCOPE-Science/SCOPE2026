#!/usr/bin/env python3
"""Check the joint degree–eccentricity census from the exchange certificates."""
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path
import sys


def read_int_rows(path):
    return [tuple(map(int, line.split(','))) for line in path.read_text(encoding='ascii').splitlines()]


def main():
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    bases = read_int_rows(directory / 'basis_states.txt')
    assert len(bases) == 4560 and bases == sorted(set(bases))
    assert all(len(s) == 5 and 0 <= s[0] and s[-1] < 30 and tuple(sorted(set(s))) == s for s in bases)

    # Distinct five-element sets are adjacent iff they share a four-element subset.
    bucket = defaultdict(list)
    for i, base in enumerate(bases):
        for sub in combinations(base, 4):
            bucket[sub].append(i)
    edges = sorted(edge for group in bucket.values() for edge in combinations(group, 2))
    assert len(edges) == 37320 and edges == sorted(read_int_rows(directory / 'exchange_edges.txt'))
    adj = [[] for _ in bases]
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)

    joint, distance_seven = Counter(), []
    for i, row in enumerate(adj):
        dist = [-1] * len(bases)
        dist[i] = 0
        todo = deque([i])
        while todo:
            v = todo.popleft()
            for w in adj[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    todo.append(w)
        assert min(dist) == 0
        joint[len(row), max(dist)] += 1
        distance_seven.extend((i, j) for j in range(i+1, len(bases)) if dist[j] == 7)

    assert joint == {(13, 6): 720, (17, 6): 3120, (17, 7): 720}
    assert len(distance_seven) == 360
    assert distance_seven == sorted(read_int_rows(directory / 'distance_7_pairs.txt'))
    for (degree, eccentricity), count in sorted(joint.items()):
        print(f'degree {degree} eccentricity {eccentricity} bases {count}')
    print(f'distance_7_unordered_pairs {len(distance_seven)}')


if __name__ == '__main__':
    main()
