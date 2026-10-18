#!/usr/bin/env python3
"""Reconstruct the reduced cellular Morse certificate for the graph K_{3,4}.

Vertices 0,1,2 form one class, vertices 3,4,5,6 the other.
An oriented edge (u,v) means the discrete vector pair (u,{u,v}).
Only the Python standard library is required.
"""
from collections import Counter, deque
from functools import lru_cache

LEFT = range(3)
RIGHT = range(3, 7)
EDGES = [(u, v) for u in LEFT for v in RIGHT]
ARCS = [a for e in EDGES for a in (e, e[::-1])]


def all_faces():
    result = []
    parents = [-1] * 7

    def extend(i, mask, used_origins):
        if i == len(ARCS):
            result.append(mask)
            return
        extend(i + 1, mask, used_origins)
        u, v = ARCS[i]
        if (used_origins >> u) & 1 or (mask >> (i ^ 1)) & 1:
            return
        w = v
        while w >= 0 and w != u:
            w = parents[w]
        if w == u:
            return
        parents[u] = v
        extend(i + 1, mask | (1 << i), used_origins | (1 << u))
        parents[u] = -1

    extend(0, 0, 0)
    return result


def greedy_matching(faces):
    unmatched = set(faces) - {0}
    pairs = []
    for k in range(len(ARCS)):
        bit = 1 << k
        for f in faces:
            if not f or f not in unmatched or f & bit:
                continue
            g = f | bit
            if g in unmatched:
                unmatched.remove(f)
                unmatched.remove(g)
                pairs.append((f, g))
    return unmatched, pairs


def acyclicity_check(faces, pairs):
    # The Hasse arrows run downward, except that matched edges run upward.
    up = dict(pairs)
    vertices = set(faces) - {0}
    outgoing = {u: [] for u in vertices}
    indeg = {u: 0 for u in vertices}
    edge_count = 0
    for large in vertices:
        m = large
        while m:
            bit = m & -m
            m ^= bit
            small = large ^ bit
            if not small:
                continue
            if up.get(small) == large:
                src, dst = small, large
            else:
                src, dst = large, small
            outgoing[src].append(dst)
            indeg[dst] += 1
            edge_count += 1
    queue = deque(x for x in vertices if indeg[x] == 0)
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in outgoing[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                queue.append(y)
    assert visited == len(vertices), (visited, len(vertices))
    return visited, edge_count


def incidence(high, low):
    bit = high ^ low
    assert bit and bit & (bit - 1) == 0
    return -1 if (low & (bit - 1)).bit_count() % 2 else 1


def morse_boundary(critical, pairs):
    up = dict(pairs)
    lows = sorted(u for u in critical if u.bit_count() == 5)
    highs = sorted(u for u in critical if u.bit_count() == 6)
    assert len(lows) == 2 and len(highs) == 434
    position = {u: i for i, u in enumerate(lows)}

    @lru_cache(None)
    def project(face):
        if face in position:
            return (1, 0) if position[face] == 0 else (0, 1)
        if face not in up:
            return (0, 0)  # paired downward, hence absent in Morse chains
        upper = up[face]
        assert upper.bit_count() == 6
        factor = incidence(upper, face)
        a = b = 0
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            other = upper ^ bit
            if other == face:
                continue
            x, y = project(other)
            c = -factor * incidence(upper, other)
            a += c * x
            b += c * y
        return a, b

    columns = []
    for top in highs:
        a = b = 0
        bits = top
        while bits:
            bit = bits & -bits
            bits -= bit
            low = top ^ bit
            x, y = project(low)
            sign = incidence(top, low)
            a += sign * x
            b += sign * y
        columns.append((a, b))
    assert lows == [1198084, 4331524]
    assert 1198240 in highs and 4331680 in highs
    c0 = columns[highs.index(1198240)]
    c1 = columns[highs.index(4331680)]
    assert c0 == (-1, 0) and c1 == (0, 1)
    assert sum(bool(a) + bool(b) for a, b in columns) == 22
    assert all(x in (-1, 0, 1) for c in columns for x in c)
    return lows, highs, columns


def main():
    faces = all_faces()
    fvector = Counter(f.bit_count() for f in faces)
    assert len(faces) == 12800 and len(set(faces)) == 12800
    assert [fvector[k] for k in range(7)] == [1, 24, 234, 1192, 3357, 4968, 3024]
    critical, pairs = greedy_matching(faces)
    assert len(pairs) == 6181
    assert Counter(x.bit_count() - 1 for x in critical) == {0: 1, 4: 2, 5: 434}
    assert 1 in critical
    visited, edges = acyclicity_check(faces, pairs)
    lows, highs, columns = morse_boundary(critical, pairs)
    # The displayed two columns form a determinant -1. The remaining
    # cellular 5-attaching maps can be cleared by integral basis changes.
    assert len(highs) - len(lows) == 432
    print("VERIFY_OK faces=12800 matched_pairs=6181 critical=(1,2,434)")
    print(f"HASSE_ACYCLIC visited={visited} edges={edges}")
    print("MORSE_BOUNDARY pivot_rows=[1198084,4331524] pivot_columns=[1198240,4331680] matrix=[[-1,0],[0,1]]")
    print("HOMOTOPY wedge_of_432_S5")


if __name__ == "__main__":
    main()
