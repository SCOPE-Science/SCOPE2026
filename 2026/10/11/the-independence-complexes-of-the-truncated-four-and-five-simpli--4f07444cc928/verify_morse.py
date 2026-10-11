"""Reproducible integral discrete-Morse verification for truncated simplex graphs.

Run: python verify_morse.py
Python standard library only; exhaustive for n = 5 and n = 6.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations


def graph(n):
    arcs = [(a, b) for a in range(n) for b in range(n) if a != b]
    position = {arc: j for j, arc in enumerate(arcs)}
    edges = set()
    for a in range(n):
        targets = [b for b in range(n) if b != a]
        for b, c in combinations(targets, 2):
            edges.add(tuple(sorted((position[a, b], position[a, c]))))
    for a, b in combinations(range(n), 2):
        edges.add(tuple(sorted((position[a, b], position[b, a]))))
    assert len(arcs) == n * (n - 1)
    assert len(edges) == n * (n - 1) * (n - 2) // 2 + n * (n - 1) // 2
    return arcs, edges


def simplices(vertex_count, edges):
    neighbors = [0] * vertex_count
    for a, b in edges:
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a
    faces = []
    def descend(available, sigma):
        if sigma:
            faces.append(sigma)
        while available:
            bit = available & -available
            available ^= bit
            j = bit.bit_length() - 1
            descend(available & ~neighbors[j], sigma | bit)
    descend((1 << vertex_count) - 1, 0)
    return set(faces)


def oriented_faces(sigma):
    bitset = sigma
    position = 0
    while bitset:
        bit = bitset & -bitset
        bitset ^= bit
        lower = sigma ^ bit
        if lower:
            yield lower, (1 if position % 2 == 0 else -1)
        position += 1


def analyze(n):
    arcs, edges = graph(n)
    faces = simplices(len(arcs), edges)
    vector = [sum(x.bit_count() == k + 1 for x in faces) for k in range(n)]
    pairs = []
    available = set(faces)
    lower_to_upper = {}
    upper_to_lower = {}
    # Ordered pivot toggles on the remaining faces. All pairs are facet incidences.
    for j in range(len(arcs)):
        bit = 1 << j
        this_pivot = [(s, s | bit) for s in available
                      if not (s & bit) and (s | bit) in available]
        for low, up in this_pivot:
            assert low.bit_count() + 1 == up.bit_count()
            available.remove(low)
            available.remove(up)
            lower_to_upper[low] = up
            upper_to_lower[up] = low
        pairs.extend(this_pivot)
    critical = defaultdict(list)
    for x in available:
        critical[x.bit_count() - 1].append(x)
    for k in critical:
        critical[k].sort()
    # Complete acyclicity test: unmatched Hasse arrows descend, matched arrows ascend.
    directed = defaultdict(list)
    indegree = defaultdict(int)
    incidences = 0
    for upper in faces:
        for lower, _ in oriented_faces(upper):
            assert lower in faces
            if lower_to_upper.get(lower) == upper:
                directed[lower].append(upper)
                indegree[upper] += 1
            else:
                directed[upper].append(lower)
                indegree[lower] += 1
            incidences += 1
    q = deque(v for v in faces if indegree[v] == 0)
    visited = 0
    while q:
        x = q.popleft()
        visited += 1
        for y in directed[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    assert visited == len(faces), 'matched Hasse orientation is cyclic'
    low_dim = n - 2
    high_dim = n - 1
    assert set(critical) == {0, low_dim, high_dim}
    rows = critical[low_dim]
    cols = critical[high_dim]

    @lru_cache(maxsize=None)
    def project(facet):
        # Sum over signed gradient paths ending at critical low-dimensional cells.
        if facet in available:
            return {facet: 1}
        if facet in upper_to_lower:
            return {}
        paired_upper = lower_to_upper[facet]
        incidence = next(c for g, c in oriented_faces(paired_upper) if g == facet)
        out = defaultdict(int)
        for other, c in oriented_faces(paired_upper):
            if other == facet:
                continue
            for t, weight in project(other).items():
                out[t] -= incidence * c * weight
        return {t: weight for t, weight in out.items() if weight}

    row_index = {r: j for j, r in enumerate(rows)}
    matrix = [[0] * len(cols) for _ in rows]
    for col_index, upper in enumerate(cols):
        for facet, c in oriented_faces(upper):
            for t, weight in project(facet).items():
                assert t in row_index
                matrix[row_index[t]][col_index] += c * weight
    # Rank one with a unit coefficient gives Smith diagonal (1,0,...,0).
    assert any(abs(a) == 1 for row in matrix for a in row)
    first = next(i for i, row in enumerate(matrix) if any(row))
    j = next(j for j, x in enumerate(matrix[first]) if x)
    pivot = matrix[first][j]
    assert abs(pivot) == 1
    for i, row in enumerate(matrix):
        for k, x in enumerate(row):
            assert x * pivot == matrix[i][j] * matrix[first][k], 'Morse matrix has rank > 1'
    assert {x for row in matrix for x in row} <= {-1, 0, 1}
    assert len(pairs) * 2 + len(available) == len(faces)
    betti_low = len(rows) - 1
    betti_high = len(cols) - 1
    expected = {5: ([20, 150, 520, 815, 444], 959, 7340, 5, 23),
                6: ([30, 360, 2200, 7170, 11700, 7360], 13922, 138660, 6, 967)}
    evec, epairs, eincidences, elow, ehigh = expected[n]
    assert (vector, len(pairs), incidences, betti_low, betti_high) == \
           (evec, epairs, eincidences, elow, ehigh)
    nonzero_cols = sum(any(row[j] for row in matrix) for j in range(len(cols)))
    print('n=%d vertices=%d graph_edges=%d f=%s simplices=%d' %
          (n, len(arcs), len(edges), vector, len(faces)))
    print('matching_pairs=%d incidence_arrows=%d acyclic=%s' %
          (len(pairs), incidences, visited == len(faces)))
    print('critical=%s Morse_boundary=%dx%d rank=1 Smith_unit=1 nonzero_columns=%d' %
          (dict((k, len(v)) for k, v in sorted(critical.items())),
           len(rows), len(cols), nonzero_cols))
    print('homotopy_spheres: %d copies S^%d; %d copies S^%d' %
          (betti_low, low_dim, betti_high, high_dim))


if __name__ == '__main__':
    for number in (5, 6):
        analyze(number)
    print('MORSE VERIFICATION PASSED')
