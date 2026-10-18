#!/usr/bin/env python3
"""Exact finite certificate for the clique-free complex of the triangular graph on six points.
Run: python3 verify.py (standard-library Python 3; no external data required).
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial, gcd

ORDER = (13, 1, 7, 5, 12, 9, 2, 14, 4, 6, 11, 0, 8, 10, 3)


def edges_and_faces(n=6):
    edges = list(combinations(range(n), 2))
    forbidden = [sum(1 << j for j in triple)
                 for triple in combinations(range(len(edges)), 3)
                 if all(set(edges[a]) & set(edges[b])
                        for a, b in combinations(triple, 2))]
    faces = {mask for mask in range(1 << len(edges))
             if all(mask & bad != bad for bad in forbidden)}
    return edges, forbidden, faces


def match_by_pivots(faces, order):
    unpaired = set(faces)
    pairs = []
    for pivot in order:
        bit = 1 << pivot
        for low in sorted(unpaired, key=lambda z: (z.bit_count(), z)):
            high = low | bit
            if not (low & bit) and low in unpaired and high in unpaired:
                pairs.append((low, high))
                unpaired.remove(low)
                unpaired.remove(high)
    return unpaired, pairs


def acyclic(faces, pairs):
    flipped = set(pairs)
    indegree = {face: 0 for face in faces}
    forward = {face: [] for face in faces}
    for high in faces:
        for pos in range(high.bit_length()):
            if high & (1 << pos):
                low = high ^ (1 << pos)
                if low not in faces:
                    continue
                source, target = (high, low) if (low, high) in flipped else (low, high)
                forward[source].append(target)
                indegree[target] += 1
    todo = deque(x for x, k in indegree.items() if k == 0)
    visited = 0
    while todo:
        source = todo.popleft()
        visited += 1
        for target in forward[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                todo.append(target)
    return visited == len(faces)


def boundary(simplex):
    vertices = [i for i in range(simplex.bit_length()) if simplex & (1 << i)]
    return [(simplex ^ (1 << v), (-1) ** j) for j, v in enumerate(vertices)]


def critical_boundary(critical, pairs):
    # In degree 4 -> 3, matched pairs between degrees 3 and 4 are eliminated.
    low_up = {low: high for low, high in pairs
              if low.bit_count() == 4 and high.bit_count() == 5}
    critical_3 = [f for f in critical if f.bit_count() == 4]
    critical_4 = sorted(f for f in critical if f.bit_count() == 5)
    assert len(critical_3) == 1 and len(critical_4) == 27
    target = critical_3[0]

    @lru_cache(None)
    def coefficient(face):
        if face == target:
            return 1
        if face not in low_up:
            return 0
        upper = low_up[face]
        inc = dict(boundary(upper))
        denominator = inc[face]
        assert denominator in (-1, 1)
        return -sum(s * coefficient(f) for f, s in inc.items() if f != face) // denominator

    vector = [sum(s * coefficient(f) for f, s in boundary(h))
              for h in critical_4]
    return vector


def cycles(p):
    visited = set()
    lengths = []
    for i in range(len(p)):
        if i not in visited:
            j = i
            length = 0
            while j not in visited:
                visited.add(j)
                j = p[j]
                length += 1
            lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def sign_on_subset(images):
    inversions = sum(images[i] > images[j]
                     for i in range(len(images)) for j in range(i + 1, len(images)))
    return -1 if inversions % 2 else 1


def character_on_faces(perm, edges, faces):
    labels = {edge: i for i, edge in enumerate(edges)}
    action = [labels[tuple(sorted((perm[a], perm[b])))] for a, b in edges]
    signed_sum = 0
    for face in faces:
        source = [i for i in range(len(edges)) if face & (1 << i)]
        target = [action[i] for i in source]
        if set(target) == set(source):
            signed_sum += (-1) ** len(source) * sign_on_subset(target)
    # Reduced Lefschetz trace is minus signed_sum. Only reduced H_4 survives.
    return -signed_sum


def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    if largest is None:
        largest = n
    for first in range(min(n, largest), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def rim_hooks(shape, size):
    left = sum(shape) - size
    if left < 0:
        return
    for inner in partitions(left):
        if len(inner) > len(shape) or any(inner[i] > shape[i] for i in range(len(inner))):
            continue
        boxes = {(i, j) for i, width in enumerate(shape)
                 for j in range(inner[i] if i < len(inner) else 0, width)}
        if not boxes:
            yield inner, 1
            continue
        reached = {next(iter(boxes))}
        queue = list(reached)
        while queue:
            i, j = queue.pop()
            for neighbor in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if neighbor in boxes and neighbor not in reached:
                    reached.add(neighbor)
                    queue.append(neighbor)
        if len(reached) != len(boxes):
            continue
        if any((i + 1, j) in boxes and (i, j + 1) in boxes
               and (i + 1, j + 1) in boxes for i, j in boxes):
            continue
        yield inner, (-1) ** (len({i for i, _ in boxes}) - 1)


@lru_cache(None)
def specht_character(shape, cycle_type):
    if not cycle_type:
        return int(not shape)
    return sum(s * specht_character(inner, cycle_type[1:])
               for inner, s in rim_hooks(shape, cycle_type[0]))


def gf2_rank(columns):
    basis = {}
    for v in columns:
        while v:
            pivot = v.bit_length() - 1
            if pivot in basis:
                v ^= basis[pivot]
            else:
                basis[pivot] = v
                break
    return len(basis)


def check_raw_boundary_ranks(faces):
    by_size = defaultdict(list)
    for face in faces:
        by_size[face.bit_count()].append(face)
    # Compare the raw mod-two Betti numbers to the reduction.
    ranks = {}
    for cardinality in range(2, 7):
        lower = {face: i for i, face in enumerate(by_size[cardinality-1])}
        columns = [sum(1 << lower[sub] for sub, s in boundary(face))
                   for face in by_size[cardinality]]
        ranks[cardinality-1] = gf2_rank(columns)
    rank_aug = 1
    assert ranks == {1: 14, 2: 91, 3: 284, 4: 391, 5: 60}, ranks
    assert len(by_size[5]) - ranks[4] - ranks[5] == 26
    assert len(by_size[4]) - ranks[3] - ranks[4] == 0
    assert len(by_size[3]) - ranks[2] - ranks[3] == 0
    assert len(by_size[2]) - ranks[1] - ranks[2] == 0
    assert len(by_size[1]) - rank_aug - ranks[1] == 0
    return ranks


def run():
    edges, forbidden, faces = edges_and_faces()
    sizes = Counter(face.bit_count() for face in faces)
    assert len(edges) == 15 and len(forbidden) == 80
    assert [sizes[i] for i in range(7)] == [1, 15, 105, 375, 675, 477, 60], sizes
    critical, pairs = match_by_pivots(faces, ORDER)
    assert len(pairs) == 840 and len(critical) == 28
    assert Counter(face.bit_count()-1 for face in critical) == {3: 1, 4: 27}
    assert acyclic(faces, pairs)
    assert len([pair for pair in pairs if pair[0] == 0]) == 1
    assert acyclic(faces - {0}, [pair for pair in pairs if pair[0] != 0])
    vector = critical_boundary(critical, pairs)
    assert gcd(*vector) == 1
    assert Counter(vector) == {0: 21, 1: 5, -1: 1}, vector
    ranks = check_raw_boundary_ranks(faces)
    claimed = {(6,): 1, (5, 1): 1, (4, 2): 2, (4, 1, 1): 0,
               (3, 3): -1, (3, 2, 1): 1, (3, 1, 1, 1): -1,
               (2, 2, 2): 4, (2, 2, 1, 1): 2, (2, 1, 1, 1, 1): 4,
               (1, 1, 1, 1, 1, 1): 26}
    seen = Counter()
    for perm in permutations(range(6)):
        cycle = cycles(perm)
        trace = character_on_faces(perm, edges, faces)
        assert trace == claimed[cycle], (perm, cycle, trace)
        predicted = (specht_character((6,), cycle)
                     + specht_character((4, 2), cycle)
                     + specht_character((3, 2, 1), cycle))
        assert predicted == trace, (cycle, trace, predicted)
        seen[cycle] += 1
    assert sum(seen.values()) == factorial(6)
    print('PASS: 15 edges; 80 forbidden triples; 1708 augmented faces.')
    print('PASS: 840 acyclic pairs; one critical 3-cell and 27 critical 4-cells.')
    print('PASS: critical integral degree vector', vector, 'has gcd 1.')
    print('PASS: raw GF(2) boundary ranks', ranks, 'verify rank 26 in degree four.')
    print('PASS: all 720 automorphisms have prescribed Lefschetz characters.')
    print('PASS: all characters equal (6) + (4,2) + (3,2,1).')
    print('CHARACTERS:', sorted(claimed.items(), reverse=True))

if __name__ == '__main__':
    run()
