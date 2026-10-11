"""Exact finite certificate for the independence complex of C7 x K4.

Only the Python 3 standard library is required. All integers are exact.
Graph vertices have indices 4*i+j, 0<=i<7, 0<=j<4.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

CYCLE = 7
COLORS = 4
N = CYCLE * COLORS
VERTICES = [(i, j) for i in range(CYCLE) for j in range(COLORS)]


def graph_neighbors():
    return [sum(1 << b for b, (u, d) in enumerate(VERTICES)
                if (i - u) % CYCLE in (1, CYCLE-1) and c != d)
            for i, c in VERTICES]


def all_nonempty_independent_faces(neighbors):
    faces = set()

    def walk(available, selected):
        if selected:
            faces.add(selected)
        while available:
            bit = available & -available
            available ^= bit
            v = bit.bit_length() - 1
            walk(available & ~neighbors[v], selected | bit)

    walk((1 << N) - 1, 0)
    return faces


def match_faces(faces):
    unmatched = set(faces)
    mate = {}
    for vertex in range(N):
        bit = 1 << vertex
        lower_faces = [s for s in unmatched
                       if not (s & bit) and (s | bit) in unmatched]
        for lower in lower_faces:
            higher = lower | bit
            assert lower in unmatched and higher in unmatched
            unmatched.remove(lower)
            unmatched.remove(higher)
            mate[lower] = higher
            mate[higher] = lower
    return mate, unmatched


def boundary(simplex):
    """Oriented boundary, vertex indices in increasing order."""
    sign = 1
    bits = simplex
    while bits:
        bit = bits & -bits
        bits ^= bit
        yield simplex ^ bit, sign
        sign = -sign


def check_directed_hasse_acyclic(faces, mate):
    indegree = {s: 0 for s in faces}
    directed = defaultdict(list)
    incidences = 0
    for upper in faces:
        if upper.bit_count() == 1:
            continue
        for lower, _ in boundary(upper):
            if mate.get(lower) == upper:
                start, end = lower, upper  # reverse matching incidences
            else:
                start, end = upper, lower
            directed[start].append(end)
            indegree[end] += 1
            incidences += 1
    queue = deque(s for s in faces if indegree[s] == 0)
    processed = 0
    while queue:
        current = queue.popleft()
        processed += 1
        for next_face in directed[current]:
            indegree[next_face] -= 1
            if indegree[next_face] == 0:
                queue.append(next_face)
    assert processed == len(faces), (processed, len(faces))
    return incidences


def integral_morse_boundary(mate, critical):
    critical_3 = sorted(s for s in critical if s.bit_count() == 4)
    critical_4 = sorted(s for s in critical if s.bit_count() == 5)
    critical_3_index = {s: i for i, s in enumerate(critical_3)}

    @lru_cache(None)
    def project_three(face):
        """Signed gradient paths from a three-simplex to critical three-cells.

        For a lower matched 3-face, eliminate the incident 4-cell using
        its oriented boundary coefficient (always +1 or -1).
        A three-face paired as an upper face of a two-simplex projects to zero.
        Termination follows from the complete directed-Hasse acyclicity test.
        """
        if face in critical_3_index:
            return {critical_3_index[face]: 1}
        partner = mate[face]
        if partner.bit_count() == 3:  # (2,3) matched pair
            return {}
        assert partner.bit_count() == 5  # (3,4) matched pair
        incidence = dict(boundary(partner))[face]
        coefficient = defaultdict(int)
        for other, sign in boundary(partner):
            if other == face:
                continue
            for idx, value in project_three(other).items():
                coefficient[idx] -= incidence * sign * value
        return {i: v for i, v in coefficient.items() if v != 0}

    matrix = [[0] * len(critical_4) for _ in critical_3]
    for j, upper in enumerate(critical_4):
        for lower, sign in boundary(upper):
            for i, value in project_three(lower).items():
                matrix[i][j] += sign * value
    return critical_3, critical_4, matrix


def integer_unit_reduction(matrix):
    """Smith reduction by integer-unimodular operations, no divisions.

    Because every pivot actually encountered is a unit, the final diagonal
    proves both the integral elementary divisors and the exact rank.
    """
    a = [list(row) for row in matrix]
    h, w = len(a), len(a[0])
    pivots = 0
    for k in range(min(h, w)):
        pair = next(((i, j) for i in range(k, h) for j in range(k, w)
                     if abs(a[i][j]) == 1), None)
        if pair is None:
            assert all(a[i][j] == 0 for i in range(k, h)
                       for j in range(k, w))
            break
        i, j = pair
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        if a[k][k] == -1:
            a[k] = [-v for v in a[k]]
        for i in range(h):
            if i != k and a[i][k]:
                factor = a[i][k]
                a[i] = [u - factor * v for u, v in zip(a[i], a[k])]
        for j in range(w):
            if j != k and a[k][j]:
                factor = a[k][j]
                for row in a:
                    row[j] -= factor * row[k]
        pivots += 1
    for i in range(h):
        for j in range(w):
            assert a[i][j] == (1 if i == j and i < pivots else 0)
    return pivots


def mod_two_homology(faces):
    """Independently reduce every full simplicial boundary matrix over F2."""
    by_dim = defaultdict(list)
    for s in faces:
        by_dim[s.bit_count() - 1].append(s)
    for row in by_dim.values():
        row.sort()
    ranks = {}
    for k in range(1, max(by_dim) + 1):
        lower_index = {s: j for j, s in enumerate(by_dim[k-1])}
        pivot_columns = {}
        for upper in by_dim[k]:
            col = 0
            for lower, _ in boundary(upper):
                col ^= 1 << lower_index[lower]
            while col:
                high = col.bit_length() - 1
                if high not in pivot_columns:
                    pivot_columns[high] = col
                    break
                col ^= pivot_columns[high]
        ranks[k] = len(pivot_columns)
    betti = {k: len(row) - ranks.get(k, 0) - ranks.get(k + 1, 0)
             for k, row in by_dim.items()}
    assert betti == {0: 1, 1: 0, 2: 0, 3: 3, 4: 6,
                     5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, betti
    return betti


def main():
    neighbors = graph_neighbors()
    assert len(neighbors) == N
    assert all(not neighbors[v] & (1 << v) for v in range(N))
    assert all(bool(neighbors[v] & (1 << w)) == bool(neighbors[w] & (1 << v))
               for v in range(N) for w in range(N))
    faces = all_nonempty_independent_faces(neighbors)
    assert len(faces) == 36068
    assert all((s & neighbors[b.bit_length() - 1]) == 0
               for s in faces for b in (1 << v for v in range(N) if s & (1 << v)))
    mate, critical = match_faces(faces)
    assert len(mate) == 36046
    assert len(critical) == 22
    assert len(set(mate) | critical) == len(faces)
    assert set(mate).isdisjoint(critical)
    assert all(mate[mate[s]] == s and abs(s.bit_count()-mate[s].bit_count()) == 1
               for s in mate)
    assert Counter(s.bit_count()-1 for s in critical) == {0: 1, 3: 9, 4: 12}
    directed_edges = check_directed_hasse_acyclic(faces, mate)
    assert directed_edges == 218008
    c3, c4, matrix = integral_morse_boundary(mate, critical)
    assert len(c3) == 9 and len(c4) == 12
    unit_rank = integer_unit_reduction(matrix)
    assert unit_rank == 6
    betti = mod_two_homology(faces)
    assert betti[3] == 3 and betti[4] == 6
    print('VERIFY_OK faces=36068 pairs=18023 critical=1x0+9x3+12x4 '
          'incidences=218008 integer_smith=1x6+0 mod2_b3=3 mod2_b4=6')


if __name__ == '__main__':
    main()
