#!/usr/bin/env python3
"""Reproducible exact check for the C7 x K3 independence-complex theorem.

Requires only the Python standard library. All chain calculations use Z.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations

ROWS, COLORS = 7, 3
NV = ROWS * COLORS


def neighbors():
    adj = [0] * NV
    for r in range(ROWS):
        for c in range(COLORS):
            v = r * COLORS + c
            for s in ((r - 1) % ROWS, (r + 1) % ROWS):
                for d in range(COLORS):
                    if c != d:
                        adj[v] |= 1 << (s * COLORS + d)
    return adj


def enumerate_faces(adj):
    faces = [0]
    for v in range(NV):
        bit = 1 << v
        faces += [x | bit for x in faces if (x & adj[v]) == 0]
    return faces


def faces_boundary(face):
    """Signed simplicial boundary, in increasing vertex order."""
    return {face ^ (1 << v): (-1) ** ((face & ((1 << v) - 1)).bit_count())
            for v in range(NV) if face & (1 << v)}


def matching(faces):
    unmatched = set(faces)
    lower_to_upper = {}
    upper_to_lower = {}
    # Examine all vertices color-first, then cyclic position.
    for c in range(COLORS):
        for r in range(ROWS):
            v = r * COLORS + c
            bit = 1 << v
            pairs = [x for x in unmatched
                     if not (x & bit) and (x | bit) in unmatched]
            for x in pairs:
                unmatched.remove(x)
                unmatched.remove(x | bit)
                lower_to_upper[x] = x | bit
                upper_to_lower[x | bit] = x
    return unmatched, lower_to_upper, upper_to_lower


def check_acyclic(faces, lower_to_upper):
    # Orient each Hasse edge upwards only when matched.
    all_nonempty = set(faces) - {0}
    indegree = {x: 0 for x in all_nonempty}
    outgoing = defaultdict(list)
    incidence_count = 0
    for hi in all_nonempty:
        for lo in faces_boundary(hi):
            if lo == 0:
                continue
            incidence_count += 1
            if lower_to_upper.get(lo) == hi:
                a, b = lo, hi
            else:
                a, b = hi, lo
            outgoing[a].append(b)
            indegree[b] += 1
    queue = deque(x for x in all_nonempty if indegree[x] == 0)
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in outgoing[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert visited == len(all_nonempty), 'matching is cyclic'
    return incidence_count


def chain_boundary(chain):
    boundary = Counter()
    for simplex, value in chain.items():
        for face, incidence in faces_boundary(simplex).items():
            boundary[face] += value * incidence
    return {x: y for x, y in boundary.items() if y}


def action(simplex, permutation):
    target = [permutation[v] for v in range(NV) if simplex & (1 << v)]
    inversions = sum(a > b for i, a in enumerate(target) for b in target[i + 1:])
    return sum(1 << v for v in target), (-1) ** inversions


def permutation_sign(p):
    inversions = sum(a > b for i, a in enumerate(p) for b in p[i + 1:])
    return (-1) ** inversions


def standard_character(p):
    return sum(p[i] == i for i in range(len(p))) - 1


def main():
    adj = neighbors()
    faces = enumerate_faces(adj)
    assert len(faces) == len(set(faces)) == 5282
    assert set(faces) == {0} | set(faces[1:])
    f_vector = dict(sorted(Counter(x.bit_count() - 1 for x in faces).items()))
    assert f_vector == {-1: 1, 0: 21, 1: 168, 2: 658,
                        3: 1365, 4: 1554, 5: 1022,
                        6: 402, 7: 84, 8: 7}
    critical_aug, matched_low, matched_high = matching(faces)
    assert 0 in matched_low
    removed_vertex = matched_low.pop(0)
    assert matched_high.pop(removed_vertex) == 0
    critical = critical_aug | {removed_vertex}
    counts = dict(sorted(Counter(x.bit_count() - 1 for x in critical).items()))
    assert counts == {0: 1, 3: 1, 4: 3}
    assert len(matched_low) == len(matched_high) == 2638
    incidences = check_acyclic(faces, matched_low)

    crit3, = [x for x in critical if x.bit_count() == 4]
    crit4 = [x for x in critical if x.bit_count() == 5]
    @lru_cache(None)
    def projected_coefficient(simplex):
        """Integral Morse projection of a degree-three simplex."""
        if simplex == crit3:
            return 1
        if simplex in matched_high:
            return 0
        mate = matched_low[simplex]
        incidence = faces_boundary(mate)[simplex]
        return sum(-incidence * coef * projected_coefficient(face)
                   for face, coef in faces_boundary(mate).items()
                   if face != simplex)

    for cell in faces:
        if cell.bit_count() == 5:
            assert sum(incidence * projected_coefficient(face)
                       for face, incidence in faces_boundary(cell).items()) == 0

    # Lift the single critical 3-cell to an integral original simplicial cycle.
    paired_lower2 = {x for x in matched_low if x.bit_count() == 3}
    dependencies = {
        x: {y for y in faces_boundary(matched_low[x])
            if y != x and y in paired_lower2}
        for x in paired_lower2
    }
    incoming = {x: 0 for x in paired_lower2}
    for successors in dependencies.values():
        for y in successors:
            incoming[y] += 1
    queue = deque(x for x in incoming if incoming[x] == 0)
    order = []
    while queue:
        x = queue.popleft()
        order.append(x)
        for y in dependencies[x]:
            incoming[y] -= 1
            if incoming[y] == 0:
                queue.append(y)
    assert len(order) == len(paired_lower2)
    cycle = Counter({crit3: 1})
    boundary = Counter(chain_boundary(cycle))
    for x in order:
        coeff = boundary[x]
        if coeff == 0:
            continue
        mate = matched_low[x]
        coefficient = -coeff * faces_boundary(mate)[x]
        cycle[mate] += coefficient
        for face, incidence in faces_boundary(mate).items():
            boundary[face] += coefficient * incidence
    cycle = {x: y for x, y in cycle.items() if y}
    assert not any(boundary.values())
    assert not chain_boundary(cycle)
    assert len(cycle) == 16
    assert sum(v * projected_coefficient(x) for x, v in cycle.items()) == 1

    def homology_character3(perm):
        return sum(v * sign * projected_coefficient(image)
                   for simplex, v in cycle.items()
                   for image, sign in [action(simplex, perm)])

    def reduced_lefschetz(perm):
        total = -1  # Empty face contributes (-1)^(-1).
        for simplex in faces[1:]:
            image, sign = action(simplex, perm)
            if image == simplex:
                total += (-1) ** (simplex.bit_count() - 1) * sign
        return total

    character_table = {}
    for reflected in (False, True):
        for k in range(7):
            for cp in permutations(range(COLORS)):
                perm = tuple(((k - r if reflected else k + r) % 7) * COLORS + cp[c]
                             for r in range(7) for c in range(COLORS))
                for i in range(NV):
                    transported = sum(1 << perm[j] for j in range(NV) if adj[i] & (1 << j))
                    assert transported == adj[perm[i]]
                chi3 = homology_character3(perm)
                chi4 = reduced_lefschetz(perm) + chi3
                expected3 = (-1 if reflected else 1) * permutation_sign(cp)
                expected4 = permutation_sign(cp) + standard_character(cp)
                assert chi3 == expected3, (reflected, k, cp, chi3)
                assert chi4 == expected4, (reflected, k, cp, chi4)
                key = (reflected, tuple(sorted(Counter(cp).items())))
                character_table[(reflected, k, cp)] = (chi3, chi4)
    assert len(character_table) == 84
    assert (sum(x[0] for x in character_table.values()),
            sum(x[1] for x in character_table.values())) == (0, 0)

    print('F_VECTOR', f_vector)
    print('Hasse incidences', incidences)
    print('Morse pairs', len(matched_low), 'critical', counts)
    print('critical three-to-four attaching degrees', [0, 0, 0])
    print('lifted integer 3-cycle nonzero terms', len(cycle))
    print('checked group elements', len(character_table))
    print('D7 reflection x S3 conjugacy-class (id, swap, 3cycle) characters:')
    for reflected in (False, True):
        for cp in ((0, 1, 2), (1, 0, 2), (1, 2, 0)):
            print(reflected, cp, character_table[(reflected, 0, cp)])
    print('VERIFIED')

if __name__ == '__main__':
    main()
