#!/usr/bin/env python3
"""Exact reproducibility of a 26-coordinate binary plane code's coset spectrum.
Python standard library only. Run: python3 verify.py
"""
from collections import Counter, deque
from itertools import combinations
from math import factorial
from pathlib import Path
import csv

N = 13
D = frozenset((0, 1, 3, 9))
MASK = (1 << N) - 1
A = tuple(sum(1 << i for i in range(N) if (j-i) % N not in D)
          for j in range(N))
COLS = tuple(1 << i for i in range(N)) + A
T = tuple((i+1) % N for i in range(N))
U = tuple((3*i) % N for i in range(N))
P = (0, 7, 4, 10, 1, 3, 6, 12, 9, 8, 5, 2, 11)
PERMS = (T, U, P)


def bit_permute(v, p):
    out = 0
    for i in range(N):
        if v & (1 << i):
            out ^= 1 << p[i]
    return out


def duality(v):
    out = 0
    for i in range(N):
        if (v >> i) & 1:
            out ^= A[-i % N]
    return out


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def collineation_count():
    identity = tuple(range(N))
    visited = {identity}
    queue = [identity]
    for perm in queue:
        for gen in PERMS:
            result = compose(gen, perm)
            if result not in visited:
                visited.add(result)
                queue.append(result)
    return len(visited)


def verify_incidence_and_symmetry():
    assert len(set(COLS)) == 26
    for i in range(N):
        assert A[i].bit_count() == 9
        for j in range(N):
            assert ((A[i] & A[j]).bit_count() % 2) == int(i == j)
    for i in range(N):
        for j in range(i+1, N):
            assert len({(i+d) % N for d in D} & {(j+d) % N for d in D}) == 1
    for perm in PERMS:
        assert tuple(sorted(perm)) == tuple(range(N))
        images = tuple(bit_permute(A[j], perm) for j in range(N))
        assert set(images) == set(A)
        assert set(bit_permute(c, perm) for c in COLS) == set(COLS)
    assert set(duality(c) for c in COLS) == set(COLS)
    assert all(duality(duality(1 << i)) == 1 << i for i in range(N))
    assert collineation_count() == 5616
    # All collineations preserve the point block; duality exchanges the blocks.
    # Hence generated 26-coordinate symmetry group has order 2*5616.


def distance_and_multiplicity_bfs():
    distance = [-1] * (1 << N)
    paths = [0] * (1 << N)
    distance[0] = 0
    paths[0] = 1
    todo = deque([0])
    while todo:
        x = todo.popleft()
        for col in COLS:
            y = x ^ col
            if distance[y] < 0:
                distance[y] = distance[x] + 1
                paths[y] = paths[x]
                todo.append(y)
            elif distance[y] == distance[x] + 1:
                paths[y] += paths[x]
    assert min(distance) == 0
    assert max(distance) == 5
    assert all(paths[i] % factorial(distance[i]) == 0 for i in range(1 << N))
    return distance, [paths[i] // factorial(distance[i]) for i in range(1 << N)]


def independently_count_minimum_error_patterns(distance, multiplicity):
    # Enumerate every unordered coordinate-error set with <=5 coordinates.
    # No graph paths or shortest-path recurrences enter this calculation.
    min_distance = [99] * (1 << N)
    count = [0] * (1 << N)
    min_distance[0], count[0] = 0, 1
    for k in range(1, 6):
        for locations in combinations(COLS, k):
            syndrome = 0
            for c in locations:
                syndrome ^= c
            if k < min_distance[syndrome]:
                min_distance[syndrome], count[syndrome] = k, 1
            elif k == min_distance[syndrome]:
                count[syndrome] += 1
    assert min_distance == distance
    assert count == multiplicity


def calculate_orbits(distance, multiplicity):
    unseen = set(range(1 << N))
    rows = []
    for dist in range(6):
        for s in range(1 << N):
            if s not in unseen:
                continue
            if distance[s] != dist:
                continue
            orbit = {s}
            todo = [s]
            for x in todo:
                ys = [bit_permute(x, p) for p in PERMS] + [duality(x)]
                for y in ys:
                    if y not in orbit:
                        orbit.add(y)
                        todo.append(y)
            assert orbit <= unseen
            assert all(distance[y] == dist and multiplicity[y] == multiplicity[s]
                       for y in orbit)
            unseen.difference_update(orbit)
            rows.append((dist, len(orbit), min(orbit), multiplicity[s]))
    assert not unseen
    return sorted(rows, key=lambda row: (row[0], -row[1], row[2]))


def code_weight_spectrum():
    c = Counter()
    for u in range(1 << N):
        v = 0
        for j in range(N):
            v |= ((u & A[j]).bit_count() % 2) << j
        c[(u | (v << N)).bit_count()] += 1
    assert dict(c) == {0: 1, 6: 52, 8: 390, 10: 1313, 12: 2340,
                       14: 2340, 16: 1313, 18: 390, 20: 52, 26: 1}


def main():
    verify_incidence_and_symmetry()
    code_weight_spectrum()
    distance, multiplicity = distance_and_multiplicity_bfs()
    independently_count_minimum_error_patterns(distance, multiplicity)
    assert [distance.count(j) for j in range(6)] == [1,26,325,2080,3770,1990]
    assert {k: dict(Counter(multiplicity[s] for s in range(1 << N)
                            if distance[s] == k)) for k in range(6)} == {
        0: {1: 1}, 1: {1: 26}, 2: {1: 325},
        3: {1: 1560, 2: 520},
        4: {1: 468, 3: 1404, 5: 1898},
        5: {10: 117, 18: 1872, 26: 1}}
    rows = calculate_orbits(distance, multiplicity)
    assert len(rows) == 22
    assert [sum(x[1] for x in rows if x[0] == j) for j in range(6)] == [1,26,325,2080,3770,1990]
    assert [sum(x[0] == j for x in rows) for j in range(6)] == [1,1,3,5,7,5]
    stored_table = Path(__file__).with_name('ORBIT_TABLE.csv').read_text(encoding='utf-8')
    from io import StringIO
    parsed = [(int(a), int(b), int(c), int(d)) for a, b, c, d in
              list(csv.reader(StringIO(stored_table)))[1:]]
    assert parsed == rows
    assert sum(j*distance.count(j) for j in range(6)) == 31946
    print('VERIFY_OK', 'codewords=8192', 'cosets=8192', 'covering_radius=5',
          'deep_cosets=1990', 'coset_orbits=22', 'automorphisms=11232')


if __name__ == '__main__':
    main()
