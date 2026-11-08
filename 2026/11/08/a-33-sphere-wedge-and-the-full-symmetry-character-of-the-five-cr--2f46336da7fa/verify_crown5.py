#!/usr/bin/env python3
"""Standalone finite proof checks for a perfect-matching complex and its symmetry character.

Only Python's standard library is used. All simplices and Hasse incidences are enumerated.
The mathematical conclusion uses the elementary discrete Morse theorem and the
simplicial Lefschetz trace identity.
"""
import collections
import functools
import itertools
import math

N = 5
EDGES = tuple((i, j) for i in range(N) for j in range(N) if i != j)
EDGE_INDEX = {e: k for k, e in enumerate(EDGES)}


def derangements():
    return [p for p in itertools.permutations(range(N)) if all(i != p[i] for i in range(N))]


def facets_from_permutations():
    return {sum(1 << EDGE_INDEX[i, p[i]] for i in range(N)) for p in derangements()}


def facets_from_bipartite_dfs():
    answer = set()
    def search(row, used_cols, bits):
        if row == N:
            answer.add(bits)
            return
        for col in range(N):
            if col != row and not (used_cols >> col) & 1:
                search(row + 1, used_cols | (1 << col), bits | (1 << EDGE_INDEX[row, col]))
    search(0, 0, 0)
    return answer


def all_faces(facets):
    out = {0}
    for facet in facets:
        x = facet
        while x:
            out.add(x)
            x = (x - 1) & facet
    return out


def admissible_by_extension(bits):
    # Independent membership predicate: check vertex-disjointness, then
    # dynamically solve the residual bipartite perfect-matching problem.
    used_rows = 0
    used_cols = 0
    for k, (row, col) in enumerate(EDGES):
        if not ((bits >> k) & 1):
            continue
        if (used_rows >> row) & 1 or (used_cols >> col) & 1:
            return False
        used_rows |= 1 << row
        used_cols |= 1 << col
    free = tuple(row for row in range(N) if not ((used_rows >> row) & 1))
    remaining_cols = ((1 << N) - 1) & ~used_cols

    @functools.lru_cache(None)
    def can_extend(idx, cols):
        if idx == len(free):
            return cols == 0
        row = free[idx]
        for col in range(N):
            if row != col and ((cols >> col) & 1) and can_extend(idx + 1, cols ^ (1 << col)):
                return True
        return False
    return can_extend(0, remaining_cols)


def greedy_morse(faces, order):
    available = set(faces) - {0}
    pairs = []
    for bit in order:
        new = []
        for lower in sorted(available):
            if (lower >> bit) & 1:
                continue
            upper = lower | (1 << bit)
            if upper in available:
                new.append((lower, upper))
        for lower, upper in new:
            available.remove(lower)
            available.remove(upper)
        pairs.extend(new)
    return pairs, available


def verify_acyclic(faces, pairs):
    unmatched_faces = faces - {0}
    matched = dict(pairs)
    indegree = {f: 0 for f in unmatched_faces}
    adj = {f: [] for f in unmatched_faces}
    incidence_count = 0
    for lower in unmatched_faces:
        for bit in range(len(EDGES)):
            if (lower >> bit) & 1:
                continue
            upper = lower | (1 << bit)
            if upper not in unmatched_faces:
                continue
            incidence_count += 1
            # Reverse the selected Hasse edge, retain the other directions.
            source, dest = (lower, upper) if matched.get(lower) == upper else (upper, lower)
            adj[source].append(dest)
            indegree[dest] += 1
    queue = collections.deque(f for f, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        current = queue.popleft()
        visited += 1
        for next_face in adj[current]:
            indegree[next_face] -= 1
            if indegree[next_face] == 0:
                queue.append(next_face)
    assert visited == len(unmatched_faces), (visited, len(unmatched_faces))
    return incidence_count


def mod2_rank(columns):
    pivot = {}
    for column in columns:
        while column:
            head = column.bit_length() - 1
            if head in pivot:
                column ^= pivot[head]
            else:
                pivot[head] = column
                break
    return len(pivot)


def ranks_from_simplicial_boundaries(faces):
    levels = {d: sorted(f for f in faces if f.bit_count() == d + 1) for d in range(5)}
    ranks = []
    for d in range(1, 5):
        lower_index = {face: k for k, face in enumerate(levels[d - 1])}
        columns = []
        for face in levels[d]:
            column = 0
            for bit in range(len(EDGES)):
                if (face >> bit) & 1:
                    column ^= 1 << lower_index[face ^ (1 << bit)]
            columns.append(column)
        ranks.append(mod2_rank(columns))
    return ranks


def cycle_type(perm):
    seen = set()
    sizes = []
    for i in range(N):
        if i in seen:
            continue
        current = i
        size = 0
        while current not in seen:
            seen.add(current)
            size += 1
            current = perm[current]
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def fixed_face_orientation(face, edge_perm):
    verts = [bit for bit in range(len(EDGES)) if (face >> bit) & 1]
    transformed = [edge_perm[v] for v in verts]
    if set(verts) != set(transformed):
        return 0
    inversion_count = sum(transformed[i] > transformed[j]
                          for i in range(len(transformed))
                          for j in range(i + 1, len(transformed)))
    return -1 if inversion_count % 2 else 1


def reduced_h2_character(faces, perm, swap):
    # The identity of reduced Lefschetz numbers with top homology trace
    # applies because acyclic Morse reduction proves H~_k=0 except k=2.
    if swap:
        edge_perm = [EDGE_INDEX[perm[j], perm[i]] for i, j in EDGES]
    else:
        edge_perm = [EDGE_INDEX[perm[i], perm[j]] for i, j in EDGES]
    total = -1  # Augmented empty-face alternating trace.
    for face in faces:
        if face == 0:
            continue
        orientation = fixed_face_orientation(face, edge_perm)
        if orientation:
            total += (-1 if face.bit_count() % 2 == 0 else 1) * orientation
    return total


def partitions(number, max_part=None):
    if number == 0:
        yield ()
        return
    if max_part is None:
        max_part = number
    for first in range(min(number, max_part), 0, -1):
        for rest in partitions(number - first, first):
            yield (first,) + rest


def diagram(partition):
    return {(i, j) for i, width in enumerate(partition) for j in range(width)}


def rim_hook_removals(lam, size):
    for nu in partitions(sum(lam) - size):
        if len(nu) > len(lam) or any(nu[i] > lam[i] for i in range(len(nu))):
            continue
        cells = diagram(lam) - diagram(nu)
        if len(cells) != size:
            continue
        if any((i + 1, j) in cells and (i, j + 1) in cells and (i + 1, j + 1) in cells
               for i, j in cells):
            continue
        connected = {next(iter(cells))}
        queue = list(connected)
        while queue:
            i, j = queue.pop()
            for neighbor in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if neighbor in cells and neighbor not in connected:
                    connected.add(neighbor)
                    queue.append(neighbor)
        if connected == cells:
            height = len({i for i, j in cells})
            yield nu, (-1) ** (height - 1)


@functools.lru_cache(None)
def specht_character(lam, cycles):
    if not cycles:
        return int(not lam)
    return sum(sgn * specht_character(nu, cycles[1:])
               for nu, sgn in rim_hook_removals(lam, cycles[0]))


def main():
    facets_a = facets_from_permutations()
    facets_b = facets_from_bipartite_dfs()
    assert facets_a == facets_b and len(facets_a) == 44
    faces = all_faces(facets_a)
    assert len(faces) == 735
    face_vector = [sum(f.bit_count() == d + 1 for f in faces) for d in range(5)]
    assert face_vector == [20, 130, 320, 220, 44]
    for candidate in range(1 << len(EDGES)):
        assert (candidate in faces) == admissible_by_extension(candidate), candidate
    critical_expected = collections.Counter({0: 1, 2: 33})
    for order in (list(range(len(EDGES))), list(reversed(range(len(EDGES))))):
        pairs, critical = greedy_morse(faces, order)
        assert len(pairs) == 350
        assert collections.Counter(f.bit_count() - 1 for f in critical) == critical_expected
        assert verify_acyclic(faces, pairs) == 2320
    boundary_ranks = ranks_from_simplicial_boundaries(faces)
    assert boundary_ranks == [19, 111, 176, 44]
    # Complete characters, one value for every group element (120 x 2).
    chars = collections.defaultdict(lambda: {False: set(), True: set()})
    counts = collections.Counter()
    for perm in itertools.permutations(range(N)):
        typ = cycle_type(perm)
        counts[typ] += 1
        for swap in (False, True):
            chars[typ][swap].add(reduced_h2_character(faces, perm, swap))
    expected = {
        (5,): (24, 3, -1),
        (4, 1): (30, -1, -1),
        (3, 2): (20, 0, 0),
        (3, 1, 1): (20, 0, 0),
        (2, 2, 1): (15, 5, -3),
        (2, 1, 1, 1): (10, -3, -3),
        (1, 1, 1, 1, 1): (1, 33, 9),
    }
    for typ, (size, even, odd) in expected.items():
        assert counts[typ] == size
        assert chars[typ][False] == {even}
        assert chars[typ][True] == {odd}
    assert len(chars) == 7 and sum(counts.values()) == 120
    expected_plus = {(3, 2): 1, (3, 1, 1): 1, (2, 2, 1): 1,
                     (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 1}
    expected_minus = {(5,): 1, (3, 2): 1, (2, 2, 1): 1,
                      (1, 1, 1, 1, 1): 1}
    plus = {}
    minus = {}
    for lam in partitions(N):
        dot_plus = sum(size * (c0 + c1) * specht_character(lam, typ)
                       for typ, (size, c0, c1) in expected.items())
        dot_minus = sum(size * (c0 - c1) * specht_character(lam, typ)
                        for typ, (size, c0, c1) in expected.items())
        assert dot_plus % 240 == 0 and dot_minus % 240 == 0
        if dot_plus:
            plus[lam] = dot_plus // 240
        if dot_minus:
            minus[lam] = dot_minus // 240
    assert plus == expected_plus, plus
    assert minus == expected_minus, minus
    assert sum(counts[typ] * (chars[typ][False].pop() + chars[typ][True].pop())
               for typ in counts) == 0
    print('CROWN5_PERFECT_MATCHING_HOMOTOPY_AND_CHARACTER_VERIFIED')
    print('vertices_graph=10 edges_graph=20 perfect_matchings=44 complex_faces=735')
    print('f_vector=20,130,320,220,44')
    print('both_lex_morse=350_pairs,one_critical_vertex,33_critical_two_cells')
    print('hasse_incidences_each=2320 full_acyclicity=PASS')
    print('mod2_boundary_ranks=19,111,176,44')
    print('full_group_order=240 identity_character=33 swap_character=9')
    print('swap_even_dimension=21 swap_odd_dimension=12 full_group_invariants=0')
    print('specht_plus='+str(sorted(plus.items())))
    print('specht_minus='+str(sorted(minus.items())))


if __name__ == '__main__':
    main()
