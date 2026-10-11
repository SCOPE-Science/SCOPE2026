"""Exact check of the independence-complex homotopy calculation for SG(4,2).

Uses only Python's standard library. Vertices are lexicographically sorted
stable four-subsets of {1,...,10}, indexed from zero.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

PIVOTS = (12, 9, 3, 21, 19, 13, 11, 18, 17, 15, 5, 8, 2, 7, 0, 4)
EXPECTED_F_VECTOR = (25, 240, 1160, 3140, 5079, 5160, 3370, 1380, 320, 32)
EXPECTED_CRITICAL = {11008: 3, 98690: 4, 8405089: 4}


def construct():
    vertices = tuple(s for s in combinations(range(1, 11), 4)
                     if all((a % 10 + 1) not in s for a in s))
    assert len(vertices) == 25 and len(set(vertices)) == 25
    adjacent = tuple(sum(1 << j for j, t in enumerate(vertices)
                         if i != j and set(s).isdisjoint(t))
                     for i, s in enumerate(vertices))
    assert all((adjacent[i] >> j) & 1 == (adjacent[j] >> i) & 1
               for i in range(25) for j in range(25))
    assert sum(x.bit_count() for x in adjacent) == 120
    faces = [0]
    for i in range(25):
        bit = 1 << i
        faces.extend(s | bit for s in tuple(faces) if not (s & adjacent[i]))
    assert len(faces) == len(set(faces))
    all_faces = set(faces)
    count = Counter(x.bit_count() - 1 for x in all_faces if x)
    assert tuple(count[d] for d in range(10)) == EXPECTED_F_VECTOR
    assert len(all_faces) == 19907
    return vertices, adjacent, all_faces


def incidence(b, a):
    removed = b ^ a
    assert removed.bit_count() == 1 and a & b == a
    return -1 if (a & (removed - 1)).bit_count() % 2 else 1


def run():
    vertices, adjacent, all_faces = construct()
    remainder = set(all_faces)
    pairs = []
    for pivot in PIVOTS:
        bit = 1 << pivot
        stage = [(a, a | bit) for a in remainder
                 if not (a & bit) and a | bit in remainder]
        for lower, upper in stage:
            assert lower in remainder and upper in remainder
            assert lower.bit_count() + 1 == upper.bit_count()
            remainder.remove(lower)
            remainder.remove(upper)
        pairs.extend(stage)
    assert len(pairs) == 9952
    assert len(remainder) == 3
    assert {x: x.bit_count() - 1 for x in remainder} == EXPECTED_CRITICAL
    pair_set = set(pairs)
    assert len(pair_set) == len(pairs)
    empty_pairs = [(a,b) for a,b in pairs if a == 0]
    assert len(empty_pairs) == 1
    ordinary_pairs = [(a,b) for a,b in pairs if a != 0]
    ordinary_critical = set(remainder) | {empty_pairs[0][1]}
    assert len(ordinary_pairs) == 9951
    assert Counter(c.bit_count() - 1 for c in ordinary_critical) == {0:1, 3:1, 4:2}

    # Reverse just the paired Hasse incidences. Topological sorting
    # establishes that the resulting complete directed graph is acyclic.
    indegree = {x: 0 for x in all_faces}
    outgoing = defaultdict(list)
    incidences = 0
    for upper in all_faces:
        for j in range(25):
            if not (upper >> j & 1):
                continue
            lower = upper ^ (1 << j)
            incidences += 1
            if (lower, upper) in pair_set:
                source, target = lower, upper
            else:
                source, target = upper, lower
            outgoing[source].append(target)
            indegree[target] += 1
    ready = deque(u for u, deg in indegree.items() if deg == 0)
    examined = 0
    while ready:
        u = ready.popleft()
        examined += 1
        for v in outgoing[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                ready.append(v)
    assert incidences == 110730
    assert examined == len(all_faces)
    # Delete the empty face and its incident edge: the resulting oriented
    # Hasse graph is the ordinary, not augmented, acyclic matching.
    assert all(x != 0 for x in ordinary_critical)

    # Compute both integral cellular attaching degrees. In dimension 3,
    # any matched upper face projects to zero; for a matched lower face,
    # eliminate the corresponding pivot in its matched 4-cell boundary.
    # The matching is acyclic, so every recursion terminates.
    lower_to_upper = dict(pairs)
    matched_upper = {b for _, b in pairs}
    unique_critical_3 = next(x for x in remainder if x.bit_count() == 4)
    critical_4 = sorted(x for x in remainder if x.bit_count() == 5)

    @lru_cache(maxsize=None)
    def project_3(face):
        assert face.bit_count() == 4
        if face in matched_upper:
            return 0
        if face in remainder:
            assert face == unique_critical_3
            return 1
        b = lower_to_upper[face]
        assert b.bit_count() == 5
        return -incidence(b, face) * sum(
            incidence(b, b ^ (1 << j)) * project_3(b ^ (1 << j))
            for j in range(25) if b >> j & 1 and (b ^ (1 << j)) != face
        )

    attaching = [sum(incidence(h, h ^ (1 << j)) *
                     project_3(h ^ (1 << j))
                     for j in range(25) if h >> j & 1)
                 for h in critical_4]
    assert attaching == [0, 0], attaching
    # The remaining CW complex has one implicit base point, one 3-cell,
    # and two 4-cells. With zero attaching degrees, maps S^3 -> S^3
    # are nullhomotopic because pi_3(S^3) is Z.
    print('VERIFY_HOMOTOPY_OK vertices=25 edges=60 faces=19907 '
          'pairs=9951 critical=1x0+1x3+2x4 incidences=110730 '
          'attaching=[0,0]')


if __name__ == '__main__':
    run()
