#!/usr/bin/env python3
"""Exact self-contained verification of the four-cube induced-forest complex."""
import collections
import csv
import hashlib
import itertools
import os
import json
import sys
from functools import lru_cache

N = 16
EDGES = tuple((u, v) for u in range(N) for v in range(u + 1, N)
              if (u ^ v).bit_count() == 1)
assert len(EDGES) == 32
NEIGHBORS = tuple(sum(1 << v for u, v in EDGES if u == w) +
                  sum(1 << u for u, v in EDGES if v == w)
                  for w in range(N))

def is_forest_union_find(mask):
    parent = list(range(N))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for u, v in EDGES:
        if mask & (1 << u) and mask & (1 << v):
            a, b = root(u), root(v)
            if a == b:
                return False
            parent[a] = b
    return True

def is_forest_components(mask):
    # Independently use the cyclomatic number |E|-|V|+components.
    edge_count = sum(bool(mask & (1 << u) and mask & (1 << v)) for u, v in EDGES)
    todo = mask
    components = 0
    while todo:
        components += 1
        seed = todo & -todo
        todo ^= seed
        frontier = seed
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            u = bit.bit_length() - 1
            new = NEIGHBORS[u] & todo
            frontier |= new
            todo ^= new
    return edge_count == mask.bit_count() - components

def determinant_small(a):
    n = len(a)
    if n == 0:
        return 1
    if n == 1:
        return a[0][0]
    return sum(((-1) ** j) * z * determinant_small(
        [[a[i][k] for k in range(n) if k != j] for i in range(1, n)])
        for j, z in enumerate(a[0]) if z)


def gf2_boundary_rank(by_size, k):
    """Rank of simplicial boundary C_k -> C_(k-1) over F_2."""
    if k == 0:
        return 0
    rows = {m: j for j, m in enumerate(by_size[k])}
    pivots = {}
    for m in by_size[k + 1]:
        col = 0
        s = m
        while s:
            bit = s & -s
            s -= bit
            col ^= 1 << rows[m ^ bit]
        while col:
            r = col.bit_length() - 1
            if r not in pivots:
                pivots[r] = col
                break
            col ^= pivots[r]
    return len(pivots)

def run():
    face_bool = bytearray(1 << N)
    faces = set()
    for m in range(1 << N):
        a = is_forest_union_find(m)
        assert a == is_forest_components(m), f"independent predicate disagreement: {m}"
        if a:
            faces.add(m)
            face_bool[m] = 1
    assert len(faces) == 25015
    fvector = tuple(sum(m.bit_count() == k for m in faces)
                    for k in range(N + 1))
    assert fvector[:11] == (1, 16, 120, 560, 1796, 4080, 6488, 6848, 4090, 1008, 8)
    assert not any(fvector[11:])
    print("GRAPH vertices=16 edges=32")
    print("FACE_PREDICATES agree_on=65536 faces_including_empty=25015")
    print("F_VECTOR face_sizes_0_to_10=", ",".join(map(str, fvector[:11])), sep="")

    unpaired = set(faces)
    match = {}
    pairs = []
    for v in range(N):
        bit = 1 << v
        # Sequential element matching: this step uses only unpaired faces.
        lows = [m for m in unpaired if not m & bit and m | bit in unpaired]
        for low in lows:
            high = low | bit
            unpaired.remove(low)
            unpaired.remove(high)
            match[low] = (high, "lower")
            match[high] = (low, "upper")
            pairs.append((low, high))
    assert len(pairs) == 12497
    critical6 = sorted(m for m in unpaired if m.bit_count() == 7)
    critical7 = sorted(m for m in unpaired if m.bit_count() == 8)
    assert len(unpaired) == 21 and len(critical6) == 15 and len(critical7) == 6
    print("MORSE pairs=12497 critical_6=15 critical_7=6 other_critical=0")

    # Verify acyclicity on the entire augmented Hasse diagram, not sampled paths.
    adjacency = [[] for _ in range(1 << N)]
    indegree = [0] * (1 << N)
    incidences = 0
    for high in faces:
        s = high
        while s:
            bit = s & -s
            s -= bit
            low = high ^ bit
            incidences += 1
            if match.get(low) == (high, "lower"):
                u, v = low, high
            else:
                u, v = high, low
            adjacency[u].append(v)
            indegree[v] += 1
    queue = collections.deque(x for x in faces if indegree[x] == 0)
    removed = 0
    while queue:
        u = queue.popleft()
        removed += 1
        for v in adjacency[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    assert removed == len(faces), (removed, len(faces))
    print(f"ACYCLIC directed_incidences={incidences} vertices_sorted={removed}")

    index6 = {m: j for j, m in enumerate(critical6)}
    sys.setrecursionlimit(100000)
    @lru_cache(None)
    def proj(m):
        if m in index6:
            return {index6[m]: 1}
        high, role = match[m]
        if role == "upper":
            return {}
        vertices = [i for i in range(N) if high & (1 << i)]
        matched_vertex = (high ^ m).bit_length() - 1
        pivot = vertices.index(matched_vertex)
        out = collections.defaultdict(int)
        for j, vertex in enumerate(vertices):
            if j == pivot:
                continue
            coefficient = (-1) ** (j + pivot + 1)
            for row, value in proj(high ^ (1 << vertex)).items():
                out[row] += coefficient * value
        return {row: value for row, value in out.items() if value}

    boundary = [[0 for _ in critical7] for _ in critical6]
    for col, m in enumerate(critical7):
        vertices = [i for i in range(N) if m & (1 << i)]
        for j, vertex in enumerate(vertices):
            for row, value in proj(m ^ (1 << vertex)).items():
                boundary[row][col] += (-1) ** j * value
    chosen = (1, 2, 3, 4, 6, 8)
    minor = determinant_small([boundary[r] for r in chosen])
    assert minor == -1, minor
    print("MORSE_BOUNDARY rows_critical_dim6=15 cols_critical_dim7=6")
    print("MORSE_BOUNDARY_MATRIX=" + json.dumps(boundary, separators=(",", ":")))
    print("UNIMODULAR_6x6_MINOR row_indices=" + ",".join(map(str, chosen)) + " determinant=-1")
    print("INTEGRAL_HOMOTOPY wedge_count=9 sphere_dimension=6")

    # Full ordinary simplicial boundary ranks, independent of the Morse differential.
    by_size = {k: sorted(m for m in faces if m.bit_count() == k) for k in range(11)}
    ranks = [gf2_boundary_rank(by_size, k) for k in range(1, 10)]
    # rank(d_k) for k=1,...,9 where dimension=k.
    assert ranks == [15, 105, 455, 1341, 2739, 3749, 3090, 1000, 8], ranks
    print("GF2_BOUNDARY_RANKS d_1_to_d_9=" + ",".join(map(str, ranks)))

    # Complete B4 character through the simplicial Lefschetz formula.
    # A g-invariant face is a union of vertex-permutation cycles.
    # For such a union, (-1)^|face| times its orientation sign is (-1)^#cycles.
    output = []
    char_histogram = collections.Counter()
    for perm in itertools.permutations(range(4)):
        for translation in range(16):
            permutation = [translation ^ sum(((v >> i) & 1) << perm[i]
                                              for i in range(4)) for v in range(N)]
            cycle_masks = []
            visited = set()
            for i in range(N):
                if i in visited:
                    continue
                j = i
                mask = 0
                while j not in visited:
                    visited.add(j)
                    mask |= 1 << j
                    j = permutation[j]
                cycle_masks.append(mask)
            reduced_lefschetz = 0
            for cycle_subset in range(1 << len(cycle_masks)):
                face = 0
                for i, block in enumerate(cycle_masks):
                    if cycle_subset & (1 << i):
                        face |= block
                if face_bool[face]:
                    reduced_lefschetz -= (-1) ** cycle_subset.bit_count()
            character = reduced_lefschetz
            char_histogram[character] += 1
            output.append(("".join(str(i) for i in perm), translation, character))
    assert len(output) == 384
    assert dict(char_histogram) == {9: 2, -3: 20, -1: 120, 0: 128, 1: 90, 3: 24}, char_histogram
    assert sum(chi * count for chi, count in char_histogram.items()) == 0
    print("B4_CHARACTER_DISTRIBUTION=" + json.dumps(sorted(char_histogram.items())))
    print("B4_FIXED_VECTORS=0")
    if len(sys.argv) > 1:
        path = sys.argv[1]
        header = ["coordinate_permutation", "xor_translation", "H6_trace"]
        expected = [header] + [[a, str(b), str(c)] for a, b, c in output]
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", newline="") as inp:
                actual = list(csv.reader(inp))
            assert actual == expected, "existing character table differs from recomputation"
        else:
            with open(path, "w", encoding="utf-8", newline="") as out:
                writer = csv.writer(out, lineterminator="\n")
                writer.writerows(expected)
        with open(path, "rb") as inp:
            table_hash = hashlib.sha256(inp.read()).hexdigest()
        print("CHARACTER_TABLE_SHA256=" + table_hash)
    print("VERIFY_OK")

if __name__ == "__main__":
    run()
