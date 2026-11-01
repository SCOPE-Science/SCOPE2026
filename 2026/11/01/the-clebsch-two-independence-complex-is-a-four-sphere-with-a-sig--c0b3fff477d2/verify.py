#!/usr/bin/env python3
"""Self-contained exact finite certificate for the 2-independence complex of the Clebsch graph.

Run with Python 3.10 or later: python verify.py
No third-party packages are required.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 16
SHIFTS = (1, 2, 4, 8, 15)
NEIGHBORS = tuple(sum(1 << (v ^ d) for d in SHIFTS) for v in range(N))


def is_face(s):
    """Every induced component has size <= 2 iff every induced degree <= 1."""
    t = s
    while t:
        bit = t & -t
        t ^= bit
        if (NEIGHBORS[bit.bit_length() - 1] & s).bit_count() > 1:
            return False
    return True


def boundary(face):
    """Simplicial oriented boundary with ascending vertex order."""
    answer = []
    t = face
    pos = 0
    while t:
        bit = t & -t
        t -= bit
        answer.append((face ^ bit, -1 if pos % 2 else 1))
        pos += 1
    return answer


def determinant(matrix):
    """Exact Bareiss determinant on a square integer matrix."""
    a = [list(row) for row in matrix]
    n = len(a)
    sign = 1
    prev = 1
    if n == 0:
        return 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((j for j in range(k+1, n) if a[j][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                top = a[i][j] * pivot - a[i][k] * a[k][j]
                assert top % prev == 0
                a[i][j] = top // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def f2_rank(columns):
    pivots = {}
    for col in columns:
        v = col
        while v:
            k = v.bit_length() - 1
            if k not in pivots:
                pivots[k] = v
                break
            v ^= pivots[k]
    return len(pivots)


def main():
    # Establish graph identification independently of any homology calculation.
    assert all(NEIGHBORS[v].bit_count() == 5 for v in range(N))
    for i in range(N):
        assert (NEIGHBORS[i] & (1 << i)) == 0
        for j in range(i+1, N):
            is_edge = bool(NEIGHBORS[i] & (1 << j))
            assert is_edge == bool(NEIGHBORS[j] & (1 << i))
            assert (NEIGHBORS[i] & NEIGHBORS[j]).bit_count() == (0 if is_edge else 2)
    graph_edges = sum(m.bit_count() for m in NEIGHBORS)//2
    assert graph_edges == 40

    faces = {s for s in range(1 << N) if is_face(s)}
    assert 0 in faces
    assert len(faces) == 2143
    counts = Counter(s.bit_count() - 1 for s in faces)
    assert dict(sorted(counts.items())) == {
        -1: 1, 0: 16, 1: 120, 2: 400, 3: 660,
        4: 576, 5: 280, 6: 80, 7: 10,
    }
    for face in faces:
        t = face
        while t:
            bit = t & -t
            t -= bit
            assert (face ^ bit) in faces

    # Successive element matchings, using order 0,...,15; empty face paired initially.
    left = set(faces)
    pairs = []
    for i in range(N):
        bit = 1 << i
        for lower in sorted(s for s in left if not (s & bit)):
            upper = lower | bit
            if lower in left and upper in left:
                pairs.append((lower, upper))
                left.remove(lower)
                left.remove(upper)
    assert len(pairs) == 1066
    assert (0, 1) in pairs
    assert Counter(s.bit_count()-1 for s in left) == {3: 5, 4: 6}

    # Work on the ordinary nonempty face poset: retain vertex 0 as critical.
    nonempty = faces - {0}
    nonempty_pairs = [(a, b) for a, b in pairs if a != 0]
    paired_up = dict(nonempty_pairs)
    paired_down = {b: a for a, b in nonempty_pairs}
    assert len(nonempty_pairs) == 1065
    assert len(paired_down) == len(paired_up)
    assert all(a not in paired_down and b not in paired_up for a, b in nonempty_pairs)
    critical = nonempty - set(paired_up) - set(paired_down)
    assert Counter(s.bit_count()-1 for s in critical) == {0: 1, 3: 5, 4: 6}
    assert 1 in critical

    # Orient all face-poset Hasse covers downward except matched edges upward.
    indeg = {s: 0 for s in nonempty}
    outgoing = defaultdict(list)
    incidence_count = 0
    for upper in nonempty:
        if upper.bit_count() == 1:
            continue
        for lower, _ in boundary(upper):
            incidence_count += 1
            a, b = ((lower, upper) if paired_up.get(lower) == upper
                    else (upper, lower))
            outgoing[a].append(b)
            indeg[b] += 1
    ready = deque(sorted(s for s, d in indeg.items() if d == 0))
    seen = 0
    while ready:
        v = ready.popleft()
        seen += 1
        for w in outgoing[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                ready.append(w)
    assert incidence_count == 9280
    assert seen == len(nonempty) == 2142, 'Acyclicity failed'

    # Exact algebraic Morse projection in degree three.
    # A paired lower (3)-simplex is eliminated using its (4)-coface.
    crit3 = sorted(s for s in critical if s.bit_count() == 4)
    crit4 = sorted(s for s in critical if s.bit_count() == 5)

    @lru_cache(None)
    def project_3(s):
        if s in critical:
            return {s: 1}
        if s not in paired_up:
            return {}
        upper = paired_up[s]
        assert upper.bit_count() == 5
        pivot = next(c for facet, c in boundary(upper) if facet == s)
        acc = defaultdict(int)
        for facet, coef in boundary(upper):
            if facet == s:
                continue
            for target, value in project_3(facet).items():
                acc[target] -= pivot * coef * value
        return {k: v for k, v in acc.items() if v}

    matrix = [[0 for _ in crit4] for _ in crit3]
    for j, upper in enumerate(crit4):
        acc = defaultdict(int)
        for facet, coef in boundary(upper):
            for target, value in project_3(facet).items():
                acc[target] += coef * value
        for i, simplex in enumerate(crit3):
            matrix[i][j] = acc[simplex]
    expected = [
        [-1, 0, 0, 0, 0, -1],
        [1, 1, 0, 0, 0, 0],
        [0, -1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, -1],
    ]
    assert matrix == expected
    minor = determinant([row[:5] for row in matrix])
    assert abs(minor) == 1

    # Independent full-complex mod-two boundary computation; no Morse matching.
    simplices_by_size = {k: sorted(s for s in nonempty if s.bit_count() == k)
                         for k in range(1, 9)}
    ranks = {1: 0}
    for k in range(2, 9):
        indices = {face: i for i, face in enumerate(simplices_by_size[k-1])}
        cols = []
        for upper in simplices_by_size[k]:
            col = 0
            for lower, _ in boundary(upper):
                col ^= 1 << indices[lower]
            cols.append(col)
        ranks[k] = f2_rank(cols)
    ranks[9] = 0
    homology = {}
    for k in range(1, 9):
        dim = k-1
        betti = len(simplices_by_size[k]) - ranks[k] - ranks[k+1]
        if dim == 0:
            betti -= 1
        if betti:
            homology[dim] = betti
    assert homology == {4: 1}, homology

    facets = [s for s in nonempty if all(
        (s & (1 << i)) or (s | (1 << i)) not in faces
        for i in range(N))]
    facet_dims = dict(sorted(Counter(s.bit_count()-1 for s in facets).items()))
    euler_reduced = sum((-1 if (s.bit_count()-1) % 2 else 1) for s in faces)
    assert euler_reduced == 1
    # The full automorphism group is 2^4 ⋊ S5. Each vertex at distance two
    # from 0 is a different sum of two of the five neighbors of 0; hence a
    # graph automorphism is determined by the image of 0 and the permutation
    # it induces on its five neighbors. All 16*120 possible choices occur.
    pair_sums = {SHIFTS[i] ^ SHIFTS[j]
                 for i in range(5) for j in range(i+1, 5)}
    assert len(pair_sums) == 10
    assert pair_sums == set(range(16)) - {0} - set(SHIFTS)

    def linear_from_generator_permutation(pi):
        images = [SHIFTS[pi[i]] for i in range(4)]
        return tuple(
            (images[0] if x & 1 else 0) ^
            (images[1] if x & 2 else 0) ^
            (images[2] if x & 4 else 0) ^
            (images[3] if x & 8 else 0)
            for x in range(16))

    def check_automorphism(map_vertices):
        assert set(map_vertices) == set(range(16))
        for i in range(16):
            for j in range(16):
                assert bool(NEIGHBORS[i] & (1 << j)) == bool(
                    NEIGHBORS[map_vertices[i]] & (1 << map_vertices[j]))

    def reduced_lefschetz(map_vertices):
        """Alternating trace on the augmented integral simplicial chains."""
        result = -1  # degree-minus-one augmented empty simplex
        contributions = defaultdict(int)
        contributions[-1] = -1
        for simplex in nonempty:
            vertices = [i for i in range(16) if simplex & (1 << i)]
            image_vertices = [map_vertices[i] for i in vertices]
            if set(image_vertices) != set(vertices):
                continue
            inversion_parity = sum(
                image_vertices[i] > image_vertices[j]
                for i in range(len(vertices)) for j in range(i+1,len(vertices))) % 2
            dimension = len(vertices)-1
            term = -1 if (dimension + inversion_parity) % 2 else 1
            contributions[dimension] += term
            result += term
        return result, dict(sorted(contributions.items()))

    for d in (1, 2, 4, 8):
        move = tuple(x ^ d for x in range(16))
        check_automorphism(move)
        tr, _ = reduced_lefschetz(move)
        assert tr == 1, (d, tr)
    swap = linear_from_generator_permutation((1, 0, 2, 3, 4))
    check_automorphism(swap)
    swap_trace, swap_terms = reduced_lefschetz(swap)
    assert swap_trace == -1
    cycle = linear_from_generator_permutation((1, 2, 3, 4, 0))
    check_automorphism(cycle)
    assert reduced_lefschetz(cycle)[0] == 1
    # Since the only nonzero reduced integral homology is Z in degree 4,
    # reduced Lefschetz numbers equal action on that free rank-one group.
    # Translations act +1; a generating S5 transposition acts -1.

    print('CLEBSCH_TWO_INDEPENDENCE_S4_OK')
    print('graph: vertices=16 edges=40 strongly_regular=(16,5,0,2)')
    print('faces_including_empty=2143 f_vector_by_dimension=' + str(dict(sorted(counts.items()))))
    print('ordinary_face_poset: faces=2142 incidences=9280 matched_pairs=1065')
    print('critical_cells={0:1,3:5,4:6} acyclic_toposort=2142')
    print('signed_integer_Morse_boundary_5x6=' + str(matrix))
    print('leading_5x5_minor_determinant=' + str(minor))
    print('independent_mod2_reduced_homology=' + str(homology))
    print('reduced_Euler_characteristic=' + str(euler_reduced))
    print('facet_dimension_counts=' + str(facet_dims))
    print('full_automorphism_group_order=1920 generators=(F2^4,S5)')
    print('four_translation_generator_H4_traces=[1,1,1,1]')
    print('S5_transposition_H4_trace=' + str(swap_trace) + ' signed_fixed_face_terms=' + str(swap_terms))
    print('S5_five_cycle_H4_trace=1')
    print('integral_H4_character=sign_of_S5_factor')


if __name__ == '__main__':
    main()
