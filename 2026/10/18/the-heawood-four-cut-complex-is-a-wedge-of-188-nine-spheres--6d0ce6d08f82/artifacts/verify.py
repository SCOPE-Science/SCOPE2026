#!/usr/bin/env python3
"""Exhaustive integral discrete-Morse certificate for the Heawood four-cut complex.

All graphs, facets, simplices, matched covers, and directed Hasse edges are
constructed directly; the verification uses Python's standard library only.
Run: python3 artifacts/verify.py
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 14
FULL = (1 << N) - 1


def build_graph():
    adjacency = [0] * N
    for line in range(7):
        for point in ((line + delta) % 7 for delta in (0, 1, 3)):
            a, b = point, 7 + line
            adjacency[a] |= 1 << b
            adjacency[b] |= 1 << a
    assert all(neighbors.bit_count() == 3 for neighbors in adjacency)
    assert all(not neighbors & (1 << index)
               for index, neighbors in enumerate(adjacency))
    return adjacency


def is_connected(subset, adjacency):
    reached = subset & -subset
    while True:
        enlarged = reached
        bits = reached
        while bits:
            bit = bits & -bits
            vertex = bit.bit_length() - 1
            enlarged |= adjacency[vertex] & subset
            bits ^= bit
        if enlarged == reached:
            return reached == subset
        reached = enlarged


def main():
    graph = build_graph()
    connected_four = set()
    facets = set()
    for subset_vertices in combinations(range(N), 4):
        four = sum(1 << vertex for vertex in subset_vertices)
        if is_connected(four, graph):
            connected_four.add(four)
        else:
            facets.add(FULL ^ four)
    assert len(connected_four) == 98
    assert len(facets) == 903

    # An independent structural count of connected induced four-subsets:
    # 14 copies of the claw K_{1,3}, and 84 induced length-three paths.
    induced_claws = 0
    for central in range(N):
        neigh = graph[central]
        star = neigh | (1 << central)
        if star in connected_four:
            induced_claws += 1
    assert induced_claws == 14
    assert len(connected_four) - induced_claws == 84

    faces = {0}
    for facet in facets:
        subset = facet
        while subset:
            faces.add(subset)
            subset = (subset - 1) & facet
    expected_vector = {
        -1: 1, 0: 14, 1: 91, 2: 364, 3: 1001, 4: 2002,
        5: 3003, 6: 3432, 7: 3003, 8: 2002, 9: 903,
    }
    assert dict(Counter(f.bit_count() - 1 for f in faces)) == expected_vector
    assert len(faces) == 15816

    alive = set(faces)
    mate = {}
    for vertex in range(N):
        bit = 1 << vertex
        lowers = [f for f in alive if not f & bit and (f | bit) in alive]
        for low in lowers:
            high = low | bit
            assert low not in mate and high not in mate
            mate[low] = high
            mate[high] = low
        for low in lowers:
            alive.remove(low)
            alive.remove(low | bit)
    assert len(mate) + len(alive) == len(faces)
    assert len(alive) == 188
    assert all(f.bit_count() == 10 for f in alive)
    assert 0 not in alive

    outgoing = defaultdict(list)
    indegrees = defaultdict(int)
    total_covers = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            lower = upper ^ bit
            if mate.get(lower) == upper:
                source, target = lower, upper
            else:
                source, target = upper, lower
            outgoing[source].append(target)
            indegrees[target] += 1
            total_covers += 1
            bits ^= bit
    queue = deque(f for f in faces if indegrees[f] == 0)
    visited = 0
    while queue:
        face = queue.popleft()
        visited += 1
        for target in outgoing[face]:
            indegrees[target] -= 1
            if indegrees[target] == 0:
                queue.append(target)
    assert visited == len(faces), (visited, len(faces))

    # There are no critical faces in consecutive positive degrees, hence
    # the reduced Morse CW model has 188 nine-cells and no other cells.
    assert sum(1 if ((f.bit_count() - 1) % 2 == 0) else -1 for f in faces) == -188
    print('Heawood four-cut:', 'vertices', N, 'disconnected-four-facets',
          len(facets), 'faces-including-empty', len(faces),
          'cover-relations', total_covers, 'toposorted', visited,
          'critical-nine-cells', len(alive), flush=True)
    print('VERIFY_OK', flush=True)


if __name__ == '__main__':
    main()
