#!/usr/bin/env python3
"""Exact finite certificate for the intrinsic graph Čech filtration of a truncated tetrahedron.

Requires only Python 3 standard library. Run `python3 verify_cech.py`.
Uses complete face enumeration, discrete-Morse cycle testing, signed gradient-path
boundary reduction, an integral unit minor, and independent mod-2 homology.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, permutations

VERTICES = [(a, b) for a in range(4) for b in range(4) if a != b]
N = len(VERTICES)
INDEX = {v: i for i, v in enumerate(VERTICES)}
EDGES = sorted((i, j) for i in range(N) for j in range(i + 1, N)
               if VERTICES[i][0] == VERTICES[j][0]
               or VERTICES[i] == VERTICES[j][::-1])
ADJ = [[] for _ in range(N)]
for i, j in EDGES:
    ADJ[i].append(j)
    ADJ[j].append(i)
assert N == 12 and len(EDGES) == 18
assert all(len(a) == 3 for a in ADJ)

DIST = []
for s in range(N):
    row = [-1] * N
    row[s] = 0
    todo = deque([s])
    while todo:
        u = todo.popleft()
        for v in ADJ[u]:
            if row[v] < 0:
                row[v] = row[u] + 1
                todo.append(v)
    assert -1 not in row
    DIST.append(row)
assert max(map(max, DIST)) == 3
assert all(DIST[i][j] == DIST[j][i] for i in range(N) for j in range(N))


def powerset_faces(maximal):
    faces = {0}
    for f in maximal:
        s = f
        while s:
            faces.add(s)
            s = (s - 1) & f
    return faces


def complex_at(r):
    assert isinstance(r, int) and 0 <= r <= 6
    if r == 0:
        generators = [1 << v for v in range(N)]
    elif r % 2 == 0:
        radius = r // 2
        generators = [sum(1 << w for w in range(N) if DIST[v][w] <= radius)
                      for v in range(N)]
    else:
        radius = r // 2
        generators = [sum(1 << w for w in range(N)
                          if min(DIST[a][w], DIST[b][w]) <= radius)
                      for a, b in EDGES]
    maximal = sorted(f for f in set(generators)
                     if not any(f != g and (f & g) == f for g in generators))
    faces = powerset_faces(maximal)
    return maximal, faces


def morse_matching(faces):
    """Deterministic sequential cone-on-vertex matching, followed by an
    independent exhaustive acyclicity check (so no abstract acyclicity
    assumption is needed). Empty face is excluded from Morse theory.
    """
    unused = set(faces) - {0}
    pairs = []
    for v in range(N):
        for f in sorted(unused, key=lambda m: (m.bit_count(), m)):
            upper = f | (1 << v)
            if f not in unused or (f & (1 << v)) or upper not in unused:
                continue
            assert f in unused and upper in unused
            assert (upper ^ f).bit_count() == 1
            unused.remove(f)
            unused.remove(upper)
            pairs.append((f, upper))
    assert len(unused) + 2 * len(pairs) == len(faces) - 1
    assert not (unused & set(a for a, b in pairs))
    assert not (unused & set(b for a, b in pairs))
    return pairs, unused


def test_hasse_acyclic(faces, pairs):
    paired = set(pairs)
    nodes = faces - {0}
    indegree = {f: 0 for f in nodes}
    arrows = defaultdict(list)
    total = 0
    for higher in nodes:
        bits = [i for i in range(N) if higher & (1 << i)]
        for i in bits:
            lower = higher ^ (1 << i)
            if lower == 0:
                continue
            a, b = ((lower, higher) if (lower, higher) in paired
                    else (higher, lower))
            arrows[a].append(b)
            indegree[b] += 1
            total += 1
    Q = deque(f for f in indegree if indegree[f] == 0)
    nvisited = 0
    while Q:
        a = Q.popleft()
        nvisited += 1
        for b in arrows[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                Q.append(b)
    assert nvisited == len(nodes), 'Morse matching has a closed gradient path'
    return total


def oriented_boundary(mask):
    return [(mask ^ (1 << v), -1 if pos % 2 else 1)
            for pos, v in enumerate(i for i in range(N) if mask & (1 << i))]


def morse_boundary(pairs, critical):
    low_to_high = {a: b for a, b in pairs}
    upper = set(low_to_high.values())
    bydim = defaultdict(list)
    for f in sorted(critical):
        bydim[f.bit_count() - 1].append(f)

    @lru_cache(None)
    def reduce_lower(face):
        if face in critical:
            return {face: 1}
        if face in upper:
            return {}
        assert face in low_to_high
        matchupper = low_to_high[face]
        bd = dict(oriented_boundary(matchupper))
        incidence = bd.pop(face)
        assert abs(incidence) == 1
        acc = Counter()
        for other, sign in bd.items():
            for c, weight in reduce_lower(other).items():
                acc[c] -= incidence * sign * weight
        return {x: z for x, z in acc.items() if z}

    output = {}
    for dim in sorted(bydim):
        if dim < 1:
            continue
        rows = bydim[dim - 1]
        cols = bydim[dim]
        loc = {x: i for i, x in enumerate(rows)}
        matrix = [[0] * len(cols) for _ in rows]
        for j, cell in enumerate(cols):
            for face, sign in oriented_boundary(cell):
                for x, mult in reduce_lower(face).items():
                    assert x in loc
                    matrix[loc[x]][j] += sign * mult
        output[dim] = matrix
    return output, bydim


def rank_rationals(matrix):
    if not matrix or not matrix[0]:
        return 0
    A = [[Fraction(v) for v in row] for row in matrix]
    m, n = len(A), len(A[0])
    lead = 0
    for c in range(n):
        pivot = next((i for i in range(lead, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[lead], A[pivot] = A[pivot], A[lead]
        z = A[lead][c]
        for j in range(c, n):
            A[lead][j] /= z
        for i in range(lead + 1, m):
            z = A[i][c]
            if z:
                for j in range(c, n):
                    A[i][j] -= z * A[lead][j]
        lead += 1
        if lead == m:
            break
    return lead


def determinant(M):
    n = len(M)
    if n == 0:
        return 1
    assert all(len(row) == n for row in M)
    ans = 0
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        prod = 1
        for i, j in enumerate(p):
            prod *= M[i][j]
        ans += -prod if inv % 2 else prod
    return ans


def rank_mod2_boundary(faces, dimension):
    """Independent simplicial-boundary elimination over F2, not using a matching."""
    rows = sorted(f for f in faces if f.bit_count() == dimension)
    cols = sorted(f for f in faces if f.bit_count() == dimension + 1)
    rowix = {f: i for i, f in enumerate(rows)}
    echelon = {}
    for cell in cols:
        vec = 0
        for face, _ in oriented_boundary(cell):
            vec ^= 1 << rowix[face]
        while vec:
            pivot = vec.bit_length() - 1
            if pivot not in echelon:
                echelon[pivot] = vec
                break
            vec ^= echelon[pivot]
    return len(echelon)


EXPECTED = {
    0: ({0: 12}, {0: 12}, 12, 0),
    1: ({0: 12, 1: 18}, {0: 1, 1: 7}, 18, 11),
    2: ({0: 12, 1: 42, 2: 40, 3: 12}, {0: 1, 1: 3}, 12, 51),
    3: ({0: 12, 1: 66, 2: 148, 3: 126, 4: 48, 5: 6},
        {0: 1, 2: 9}, 18, 198),
    4: ({0: 12, 1: 66, 2: 220, 3: 486, 4: 552, 5: 322, 6: 96, 7: 12},
        {0: 1, 3: 15, 4: 8}, 12, 871),
    5: ({0: 12, 1: 66, 2: 220, 3: 495, 4: 792, 5: 924, 6: 792,
         7: 465, 8: 148, 9: 18}, {0: 1, 7: 5}, 18, 1963),
    6: ({0: 12, 1: 66, 2: 220, 3: 495, 4: 792, 5: 924, 6: 792,
         7: 495, 8: 220, 9: 66, 10: 12, 11: 1}, {0: 1}, 1, 2047),
}
BETTI = {
    0: {0: 11},
    1: {1: 7},
    2: {1: 3},
    3: {2: 9},
    4: {3: 11, 4: 4},
    5: {7: 5},
    6: {},
}


def verify():
    previous_faces = set()
    for r in range(7):
        facets, faces = complex_at(r)
        fvec = Counter(f.bit_count() - 1 for f in faces if f)
        pairs, critical = morse_matching(faces)
        critvec = Counter(f.bit_count() - 1 for f in critical)
        ef, ec, nfac, npairs = EXPECTED[r]
        assert fvec == ef, (r, fvec)
        assert critvec == ec, (r, critvec)
        assert len(facets) == nfac and len(pairs) == npairs
        assert previous_faces <= faces, 'filtration not nested'
        previous_faces = faces
        hasse = test_hasse_acyclic(faces, pairs)
        matrices, bydim = morse_boundary(pairs, critical)
        # For each nontrivial differential, compute exact integral information.
        for d, mat in matrices.items():
            if r == 4 and d == 4:
                assert len(mat) == 15 and all(len(row) == 8 for row in mat)
                assert rank_rationals(mat) == 4
                # A unit minor plus rank four forces four unit Smith factors.
                minor = [[mat[i][j] for j in (2, 3, 4, 5)]
                         for i in (0, 1, 2, 4)]
                assert determinant(minor) == 1
                assert sum(v != 0 for row in mat for v in row) == 30
            else:
                assert all(not v for row in mat for v in row), (r, d)
        # Check the homology from the raw original simplicial chain complex,
        # independently of Forman's matching and integer Morse reduction.
        ranks = {d: rank_mod2_boundary(faces, d)
                 for d in range(1, max(fvec) + 1)}
        b = {}
        for d, nfaces in sorted(fvec.items()):
            betti = nfaces - ranks.get(d, 0) - ranks.get(d + 1, 0)
            if d == 0:
                betti -= 1
            assert betti >= 0
            if betti:
                b[d] = betti
        assert b == BETTI[r], (r, b)
        print('r', r, 'facets', len(facets), 'faces', len(faces)-1,
              'hasse', hasse, 'pairs', len(pairs),
              'critical', sorted(critvec.items()), 'betti', sorted(b.items()))
    # Every new edge in C_2 but absent from C_1 has distance two, hence its
    # endpoints have a common neighbor w. The Čech triangle {u,w,v} reduces
    # the new edge to an edge-path in C_1, proving H_1(C_1)->H_1(C_2) onto.
    r1 = complex_at(1)[1]
    r2 = complex_at(2)[1]
    for edge in (f for f in r2 if f.bit_count() == 2 and f not in r1):
        u, v = [i for i in range(N) if edge & (1 << i)]
        assert DIST[u][v] == 2
        witnesses = [w for w in range(N) if DIST[u][w] == 1 and DIST[v][w] == 1]
        assert witnesses
        assert any(edge | (1 << w) in r2 for w in witnesses)
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
