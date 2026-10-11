"""Exact integral Morse certificate for the open-neighborhood complex of Paley(17).

Run with Python 3.10+: python verify_morse.py
No nonstandard packages are required.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import hashlib
import json

P = 17
RESIDUES = {pow(i, 2, P) for i in range(1, P)}
NEIGHBORS = [sum(1 << j for j in range(P) if (j-i) % P in RESIDUES)
             for i in range(P)]


def dimension(s):
    return s.bit_count() - 1


def boundary(s):
    """Signed simplicial boundary, vertices oriented in ascending order."""
    sign = 1
    for i in range(P):
        if s & (1 << i):
            yield (s ^ (1 << i), sign)
            sign = -sign


def make_faces():
    all_faces = set()
    for hood in NEIGHBORS:
        sub = hood
        while sub:
            all_faces.add(sub)
            sub = (sub - 1) & hood
    return all_faces


def match_by_vertex_toggle(faces):
    remaining = set(faces)
    matching = {}
    for vertex in range(P):
        bit = 1 << vertex
        for lower in sorted(remaining, key=lambda s: (s.bit_count(), s)):
            upper = lower | bit
            if lower in remaining and not (lower & bit) and upper in remaining:
                matching[lower] = upper
                remaining.remove(lower)
                remaining.remove(upper)
    return remaining, matching


def assert_acyclic(faces, matching):
    indegree = {s: 0 for s in faces}
    arrows = {s: [] for s in faces}
    incidences = 0
    for s in faces:
        if dimension(s) == 0:
            continue
        for t, _ in boundary(s):
            if matching.get(t) == s:
                a, b = t, s
            else:
                a, b = s, t
            arrows[a].append(b)
            indegree[b] += 1
            incidences += 1
    todo = deque(s for s, d in indegree.items() if not d)
    examined = 0
    while todo:
        s = todo.popleft()
        examined += 1
        for t in arrows[s]:
            indegree[t] -= 1
            if indegree[t] == 0:
                todo.append(t)
    assert examined == len(faces), ('directed cycle', examined, len(faces))
    return incidences


def integral_morse_matrix(critical, matching):
    critical_two = sorted(s for s in critical if dimension(s) == 2)
    critical_three = sorted(s for s in critical if dimension(s) == 3)
    all_critical_two = set(critical_two)
    upper_matched_two = {upper for lower, upper in matching.items()
                         if dimension(upper) == 2}

    @lru_cache(None)
    def gradient_expand(t):
        if t in all_critical_two:
            return {t: 1}
        if t in upper_matched_two:
            return {}
        if t not in matching:
            raise AssertionError(('unexpected unmatched face', t))
        upper = matching[t]
        incidence = dict(boundary(upper))
        pivot = incidence.pop(t)
        assert abs(pivot) == 1
        acc = defaultdict(int)
        for face, coefficient in incidence.items():
            for root, multiplicity in gradient_expand(face).items():
                acc[root] -= (coefficient // pivot) * multiplicity
        return {root: value for root, value in acc.items() if value}

    matrix = [[0] * len(critical_three) for _ in critical_two]
    row_index = {s: i for i, s in enumerate(critical_two)}
    for col, simplex in enumerate(critical_three):
        for face, sign in boundary(simplex):
            for root, n in gradient_expand(face).items():
                matrix[row_index[root]][col] += sign * n
    return matrix, critical_two, critical_three


def det_bareiss(matrix):
    n = len(matrix)
    a = [list(row) for row in matrix]
    sign, old_pivot = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((r for r in range(k+1, n) if a[r][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for r in range(k+1, n):
            for c in range(k+1, n):
                v = a[r][c] * pivot - a[r][k] * a[k][c]
                assert v % old_pivot == 0
                a[r][c] = v // old_pivot
            a[r][k] = 0
        old_pivot = pivot
    return sign * a[n-1][n-1]


def rank_mod(matrix, prime):
    a = [[n % prime for n in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        candidate = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if candidate is None:
            continue
        a[pivot_row], a[candidate] = a[candidate], a[pivot_row]
        scale = pow(a[pivot_row][col], -1, prime)
        a[pivot_row] = [(v * scale) % prime for v in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row:
                multiple = a[r][col]
                if multiple:
                    a[r] = [(x-multiple*y) % prime for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def main():
    assert RESIDUES == {1,2,4,8,9,13,15,16}
    for x in range(P):
        assert NEIGHBORS[x].bit_count() == 8
        for y in range(P):
            if x != y:
                common = (NEIGHBORS[x] & NEIGHBORS[y]).bit_count()
                adjacent = bool(NEIGHBORS[x] & (1 << y))
                assert common == (3 if adjacent else 4)
    faces = make_faces()
    face_vector = [sum(dimension(s) == k for s in faces) for k in range(8)]
    assert face_vector == [17,136,612,1122,952,476,136,17]
    critical, matching = match_by_vertex_toggle(faces)
    assert len(matching) == 1711
    profile = dict(Counter(dimension(s) for s in critical))
    assert profile == {0:1,2:5,3:40}, profile
    incidences = assert_acyclic(faces, matching)
    assert incidences == 15300
    matrix, crit_two, crit_three = integral_morse_matrix(critical, matching)
    assert len(matrix) == 5 and all(len(row) == 40 for row in matrix)
    assert sum(n != 0 for row in matrix for n in row) == 99
    cols5 = [0, 1, 3, 4, 8]
    minor5 = det_bareiss([[matrix[r][c] for c in cols5] for r in range(5)])
    assert minor5 == -3
    rows4, cols4 = [0,1,2,3], [0,1,4,8]
    minor4 = det_bareiss([[matrix[r][c] for c in cols4] for r in rows4])
    assert minor4 == -1
    assert rank_mod(matrix, 3) == 4
    assert rank_mod(matrix, 2) == 5
    assert rank_mod(matrix, 5) == 5
    digest = hashlib.sha256(json.dumps(matrix,separators=(',',':')).encode('ascii')).hexdigest()
    print('Paley(17) open-neighborhood complex: exact integral Morse certificate')
    print('quadratic residues:', sorted(RESIDUES))
    print('faces:', len(faces), 'f-vector:', face_vector)
    print('matched pairs:', len(matching), 'critical profile:', profile)
    print('acyclic incidences:', incidences)
    print('critical two-cell masks:', crit_two)
    print('critical three-cell masks:', crit_three)
    print('matrix dimensions: 5 x 40; nonzero entries: 99')
    print('Morse boundary SHA256 (compact JSON rows):', digest)
    print('minor-5 columns [0,1,3,4,8], determinant:', minor5)
    print('minor-4 rows [0,1,2,3], columns [0,1,4,8], determinant:', minor4)
    print('rank modulo 3 = 4; modulo 2 = 5; modulo 5 = 5')
    print('integral Smith diagonal: 1,1,1,1,3')
    print('homotopy: M(Z/3,2) wedge 35 copies of S^3')

if __name__ == '__main__':
    main()
