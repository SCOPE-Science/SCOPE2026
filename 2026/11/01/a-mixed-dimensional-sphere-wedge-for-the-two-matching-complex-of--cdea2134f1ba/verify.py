#!/usr/bin/env python3
"""Exact finite verification for the two-matching complex of K_(4,5).

Standard-library only. Faces are row-major bit masks for edges (r,c),
0<=r<4, 0<=c<5. All integer computations are exact.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

ROWS, COLS = 4, 5
N = ROWS * COLS
EXPECTED_F = (20, 190, 1080, 3900, 8880, 12120, 8760, 2490)
EXPECTED_RANKS_F2 = (19, 171, 909, 2991, 5889, 6231, 2487)


def valid(mask):
    for r in range(ROWS):
        if ((mask >> (r * COLS)) & ((1 << COLS) - 1)).bit_count() > 2:
            return False
    for c in range(COLS):
        if sum((mask >> (r * COLS + c)) & 1 for r in range(ROWS)) > 2:
            return False
    return True


def enumerate_faces():
    # Every subset of the 20 original edges is considered, including invalid sets.
    faces = [mask for mask in range(1, 1 << N) if valid(mask)]
    faces_by_dimension = defaultdict(list)
    for f in faces:
        faces_by_dimension[f.bit_count() - 1].append(f)
    assert tuple(map(lambda d: len(faces_by_dimension[d]), range(8))) == EXPECTED_F
    assert len(faces) == 37440
    face_set = set(faces)
    # Full independent check that every maximal face has eight selected edges.
    facets = Counter()
    for f in faces:
        if not any((f | (1 << j)) in face_set for j in range(N) if not (f >> j) & 1):
            facets[f.bit_count() - 1] += 1
    assert facets == {7: 2490}, facets
    print('FACES_OK', EXPECTED_F, 'facets', dict(facets))
    return faces, face_set, faces_by_dimension


def construct_matching(faces, face_set):
    # Lexicographic sequence of elementary toggling matchings on remaining faces.
    remaining = set(faces)
    up, down = {}, {}
    for j in range(N):
        bit = 1 << j
        for f in faces:
            if f not in remaining or f & bit:
                continue
            g = f | bit
            if g in remaining:
                remaining.remove(f)
                remaining.remove(g)
                up[f] = g
                down[g] = f
    assert len(up) == 18697
    critical = defaultdict(list)
    for f in sorted(remaining):
        critical[f.bit_count() - 1].append(f)
    counts = {d: len(v) for d, v in critical.items()}
    assert counts == {0: 1, 6: 42, 7: 3}, counts
    assert len(faces) == len(up) * 2 + sum(counts.values())
    print('MATCHING_OK', len(up), 'critical', counts)
    return up, down, critical


def check_acyclic(faces, face_set, up):
    # Direct graph verification: matched Hasse edge low->high, all others high->low.
    indeg = {f: 0 for f in faces}
    incidences = 0
    for upper in faces:
        for j in range(N):
            bit = 1 << j
            if not upper & bit:
                continue
            lower = upper ^ bit
            if lower not in face_set:
                continue
            if up.get(lower) == upper:
                destination = upper
            else:
                destination = lower
            indeg[destination] += 1
            incidences += 1

    queue = deque(f for f in faces if indeg[f] == 0)
    traversed = 0
    while queue:
        f = queue.popleft()
        traversed += 1
        for j in range(N):
            bit = 1 << j
            neighbor = f ^ bit
            if neighbor not in face_set:
                continue
            if f & bit:
                # An outgoing downward arrow exists only for an unmatched edge.
                if up.get(neighbor) == f:
                    continue
            else:
                # An outgoing upward arrow exists only for a matched edge.
                if up.get(f) != neighbor:
                    continue
            indeg[neighbor] -= 1
            assert indeg[neighbor] >= 0
            if indeg[neighbor] == 0:
                queue.append(neighbor)
    assert traversed == len(faces), (traversed, len(faces))
    assert incidences == 217580
    print('ACYCLIC_OK', traversed, incidences)


def integer_morse_boundary(up, down, critical):
    # Only critical 7-to-6 attaching degrees could be nonzero.
    bottom = {f: k for k, f in enumerate(critical[6])}

    @lru_cache(maxsize=None)
    def reduce_six_face(f):
        if f in bottom:
            return {bottom[f]: 1}
        if f in down:
            # A 6-face paired with a 5-face contributes no critical 6-cell.
            return {}
        assert f in up and up[f].bit_count() == 8
        upper = up[f]
        added_bit = upper ^ f
        assert added_bit.bit_count() == 1
        added_pos = added_bit.bit_length() - 1
        inc = -1 if (upper & (added_bit - 1)).bit_count() % 2 else 1
        result = defaultdict(int)
        for j in range(N):
            bit = 1 << j
            if not (upper & bit) or j == added_pos:
                continue
            other = upper ^ bit
            sign = -1 if (upper & (bit - 1)).bit_count() % 2 else 1
            for i, value in reduce_six_face(other).items():
                result[i] -= inc * sign * value
        return {i: value for i, value in result.items() if value}

    cols = []
    for upper in critical[7]:
        col = defaultdict(int)
        for j in range(N):
            bit = 1 << j
            if not upper & bit:
                continue
            face = upper ^ bit
            sign = -1 if (upper & (bit - 1)).bit_count() % 2 else 1
            for i, value in reduce_six_face(face).items():
                col[i] += sign * value
        cols.append([col[i] for i in range(len(bottom))])
    assert len(cols) == 3 and all(len(col) == 42 for col in cols)
    assert all(value == 0 for col in cols for value in col), cols
    print('INTEGRAL_MORSE_OK', '42x3 zero attaching matrix', 'recursive_states', reduce_six_face.cache_info().currsize)


def independent_raw_mod2_check(by_dim):
    # Original simplicial chain complex, not the Morse complex.
    ranks = {}
    for d in range(1, 8):
        low = {f: i for i, f in enumerate(by_dim[d - 1])}
        echelon = {}
        for upper in by_dim[d]:
            boundary = 0
            for j in range(N):
                if upper & (1 << j):
                    boundary ^= 1 << low[upper ^ (1 << j)]
            while boundary:
                pivot = boundary.bit_length() - 1
                if pivot not in echelon:
                    echelon[pivot] = boundary
                    break
                boundary ^= echelon[pivot]
        ranks[d] = len(echelon)
    actual_ranks = tuple(ranks[d] for d in range(1, 8))
    assert actual_ranks == EXPECTED_RANKS_F2, actual_ranks
    reduced_betti = [len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0) - (d == 0)
                     for d in range(8)]
    assert reduced_betti == [0, 0, 0, 0, 0, 0, 42, 3]
    print('RAW_MOD2_OK', actual_ranks, 'reduced_betti', reduced_betti)


def main():
    faces, face_set, by_dim = enumerate_faces()
    up, down, critical = construct_matching(faces, face_set)
    check_acyclic(faces, face_set, up)
    integer_morse_boundary(up, down, critical)
    independent_raw_mod2_check(by_dim)
    print('HOMOTOPY_OK', '42 copies of S6 wedge 3 copies of S7')
    print('ALL_VERIFY_OK')


if __name__ == '__main__':
    main()
