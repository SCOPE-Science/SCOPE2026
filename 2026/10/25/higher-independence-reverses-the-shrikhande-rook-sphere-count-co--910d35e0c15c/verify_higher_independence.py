#!/usr/bin/env python3
"""Exact, finite check of four higher-independence discrete-Morse complexes.

The vertex labels are 4*a+b for (a,b) in Z_4 x Z_4.
Requires only Python >= 3.10; makes no network calls.
"""
from collections import Counter, deque
from itertools import combinations

N = 16
PERMUTATION = (9, 2, 13, 7, 12, 6, 15, 14, 8, 3, 0, 10, 4, 1, 11, 5)
EXPECTED = {
    ("Shrikhande", 1): {0: 1, 2: 23},
    ("Shrikhande", 2): {0: 1, 3: 57},
    ("Rook", 1): {0: 1, 2: 15},
    ("Rook", 2): {0: 1, 3: 105},
}
FACE_COUNTS = {
    ("Shrikhande", 1): {0: 1, 1: 16, 2: 72, 3: 96, 4: 16},
    ("Shrikhande", 2): {0: 1, 1: 16, 2: 120, 3: 384, 4: 544, 5: 240, 6: 32},
    ("Rook", 1): {0: 1, 1: 16, 2: 72, 3: 96, 4: 24},
    ("Rook", 2): {0: 1, 1: 16, 2: 120, 3: 384, 4: 528, 5: 144},
}
FACETS = {
    ("Shrikhande", 1): {2: 32, 3: 16},
    ("Shrikhande", 2): {3: 64, 4: 48, 5: 32},
    ("Rook", 1): {3: 24},
    ("Rook", 2): {3: 96, 4: 144},
}

def adjacency(name):
    result = []
    steps = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    for v in range(N):
        x, y = divmod(v, 4)
        neighbors = 0
        for u in range(N):
            if u == v:
                continue
            a, b = divmod(u, 4)
            if ((name == "Shrikhande" and ((a - x) % 4, (b - y) % 4) in steps)
                or (name == "Rook" and (a == x or b == y))):
                neighbors |= 1 << u
        result.append(neighbors)
    assert all(x.bit_count() == 6 for x in result)
    assert all(bool((result[v] >> u) & 1) == bool((result[u] >> v) & 1)
               for u in range(N) for v in range(N))
    assert all((result[u] & result[v]).bit_count() == 2
               for u in range(N) for v in range(u + 1, N))
    return result

def face_by_components(s, nbrs, r):
    if r == 1:
        return all(not (nbrs[v] & s) for v in range(N) if s & (1 << v))
    # All connected components have at most two vertices iff maximum induced degree <= 1.
    return all((nbrs[v] & s).bit_count() <= 1 for v in range(N) if s & (1 << v))

def minimal_nonfaces(nbrs, r):
    if r == 1:
        return {((1 << u) | (1 << v))
                for u in range(N) for v in range(u + 1, N) if nbrs[u] & (1 << v)}
    return {((1 << v) | (1 << u) | (1 << w))
            for v in range(N)
            for u, w in combinations([a for a in range(N) if nbrs[v] & (1 << a)], 2)}

def enumerate_faces(nbrs, r):
    forbidden = minimal_nonfaces(nbrs, r)
    # Verify independent predicate implementations on all 2^16 vertex subsets.
    result = []
    for subset in range(1 << N):
        a = face_by_components(subset, nbrs, r)
        b = not any((subset & f) == f for f in forbidden)
        assert a == b, (r, subset)
        if a:
            result.append(subset)
    assert result and result[0] == 0
    return result

def greedy_matching(faces):
    available = set(faces) - {0}  # use the ordinary, non-augmented face poset
    matching = {}
    for v in PERMUTATION:
        bit = 1 << v
        for low in faces:  # numeric bitmask order, not a set iteration
            if low & bit or low not in available:
                continue
            high = low | bit
            if high in available:
                assert low.bit_count() + 1 == high.bit_count()
                available.remove(low)
                available.remove(high)
                matching[low] = high
    assert len(available) + 2 * len(matching) == len(faces) - 1
    return available, matching

def verify_acyclicity(faces, matching):
    # In the oriented Hasse diagram matched cover edges point upward;
    # all others point downward. The empty face is omitted.
    nonempty = [f for f in faces if f]
    indegree = {face: 0 for face in nonempty}
    arrows = {face: [] for face in nonempty}
    covers = 0
    for high in nonempty:
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            low = high ^ bit
            if low == 0:
                continue
            covers += 1
            if matching.get(low) == high:
                tail, head = low, high
            else:
                tail, head = high, low
            arrows[tail].append(head)
            indegree[head] += 1
    queue = deque(x for x in nonempty if indegree[x] == 0)
    removed = 0
    while queue:
        face = queue.popleft()
        removed += 1
        for nxt in arrows[face]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    assert removed == len(nonempty), f"directed cycle: {len(nonempty) - removed} faces"
    return covers

def verify_one(name, r):
    nbrs = adjacency(name)
    faces = enumerate_faces(nbrs, r)
    hist = Counter(s.bit_count() for s in faces)
    assert dict(hist) == FACE_COUNTS[name, r], (name, r, hist)
    allowed = set(faces)
    facet_hist = Counter(s.bit_count() - 1 for s in faces if s and
                         not any(not (s & (1 << v)) and (s | (1 << v)) in allowed
                                 for v in range(N)))
    assert dict(facet_hist) == FACETS[name, r], (name, r, facet_hist)
    critical, pairs = greedy_matching(faces)
    critical_hist = Counter(s.bit_count() - 1 for s in critical)
    assert dict(critical_hist) == EXPECTED[name, r], (name, r, critical_hist)
    covers = verify_acyclicity(faces, pairs)
    # Reduced Euler characteristic uses the empty simplex with degree -1.
    reduced_euler = -sum(((-1) ** k) * n for k, n in hist.items())
    expected_reduced_euler = sum(((-1) ** dim) * num
                                  for dim, num in critical_hist.items() if dim != 0)
    assert reduced_euler == expected_reduced_euler
    return (len(faces) - 1, len(pairs), critical_hist, covers, reduced_euler, facet_hist)

def main():
    assert len(PERMUTATION) == N and set(PERMUTATION) == set(range(N))
    for name in ("Shrikhande", "Rook"):
        for r in (1, 2):
            count, pairs, crit, covers, chi, facets = verify_one(name, r)
            print(f"{name} r={r}: nonempty_faces={count}, matched_pairs={pairs}, "
                  f"critical={dict(sorted(crit.items()))}, covers={covers}, "
                  f"reduced_chi={chi}, facet_dimensions={dict(sorted(facets.items()))}")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
