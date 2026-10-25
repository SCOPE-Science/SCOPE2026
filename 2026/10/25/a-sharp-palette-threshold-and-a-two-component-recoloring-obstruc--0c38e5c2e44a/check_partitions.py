#!/usr/bin/env python3
"""Independent-set partition enumeration of Paley(13) five-colour recoloring."""
from collections import Counter, deque
from itertools import permutations

N = 13
SQUARES = {1, 3, 4, 9, 10, 12}
adjacency = [sum(1 << j for j in range(N) if (j - i) % N in SQUARES) for i in range(N)]
assert sum(a.bit_count() for a in adjacency) == 78
assert all(not (adjacency[i] & (1 << i)) for i in range(N))

independent = [mask for mask in range(1, 1 << N) if all(not (adjacency[i] & mask) for i in range(N) if mask >> i & 1)]
assert max(map(int.bit_count, independent)) == 3
by_first = [[mask for mask in independent if mask >> i & 1] for i in range(N)]

partitions = []
def partition(remaining, blocks):
    if not remaining:
        if len(blocks) == 5:
            partitions.append(tuple(blocks))
        return
    if len(blocks) >= 5:
        return
    first = (remaining & -remaining).bit_length() - 1
    for block in by_first[first]:
        if block & remaining == block:
            partition(remaining ^ block, blocks + [block])
partition((1 << N) - 1, [])
assert len(partitions) == 377

states = []
for parts in partitions:
    for order in permutations(range(5)):
        coloring = [0] * N
        for index, block in enumerate(parts):
            for i in range(N):
                if (block >> i) & 1:
                    coloring[i] = order[index]
        states.append(tuple(coloring))
assert len(states) == len(set(states)) == 45240
positions = {color: i for i, color in enumerate(states)}

neighbors = [[] for _ in states]
degree_by_size = Counter()
for idx, col in enumerate(states):
    arr = list(col)
    for v in range(N):
        forbidden = {col[w] for w in range(N) if adjacency[v] >> w & 1}
        for c in range(5):
            if c != col[v] and c not in forbidden:
                arr[v] = c
                neighbors[idx].append(positions[tuple(arr)])
        arr[v] = col[v]
    degree_by_size[(tuple(sorted(Counter(col).values())), len(neighbors[idx]))] += 1

edge_count = sum(map(len, neighbors)) // 2
assert edge_count == 98280
labels = [-1] * len(states)
components = []
for start in range(len(states)):
    if labels[start] >= 0:
        continue
    index = len(components)
    q = deque([start])
    labels[start] = index
    component = []
    while q:
        i = q.popleft()
        component.append(i)
        for j in neighbors[i]:
            if labels[j] < 0:
                labels[j] = index
                q.append(j)
    components.append(component)
assert sorted(map(len, components)) == [22620, 22620]

# The action of a global colour transposition is a graph automorphism.
# It interchanges the two components, so the S_5-action is its sign.
t = lambda col: tuple(1 if x == 0 else 0 if x == 1 else x for x in col)
assert all(labels[positions[t(col)]] != labels[i] for i, col in enumerate(states))
assert len({labels[i] for i in range(len(states))}) == 2

print('independent_number 3')
print('unlabelled_partitions', len(partitions))
print('proper_5_colorings', len(states))
print('recolor_edges', edge_count)
print('component_sizes', sorted(map(len, components)))
print('degree_by_color_class_partition', sorted((str(a), b, count) for (a,b),count in degree_by_size.items()))
print('global_transposition_swaps_components', True)
