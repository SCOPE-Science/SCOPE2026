#!/usr/bin/env python3
"""Exact, self-contained finite certificate for the Clebsch induced-forest filtration.
Requires Python 3.9+ standard library only; run: python verify.py
The adjacent certificate JSON must be in the same directory.
"""
import collections
import json
from functools import lru_cache
from pathlib import Path

N = 16
GENERATORS = (1, 2, 4, 8, 15)
NEIGHBORS = [sum(1 << (v ^ step) for step in GENERATORS) for v in range(N)]
ORDERS = {
    0: (13, 1, 2, 6, 10, 11, 3, 0, 8, 12, 4, 9, 5, 14, 15, 7),
    1: (0, 3, 10, 12, 5, 4, 14, 15, 2, 11, 13, 8, 7, 6, 1, 9),
    2: (9, 5, 15, 3, 0, 14, 11, 7, 8, 2, 6, 12, 13, 4, 1, 10),
    3: (6, 13, 2, 1, 8, 3, 11, 9, 12, 5, 4, 15, 7, 14, 0, 10),
    4: (15, 0, 1, 6, 14, 2, 5, 8, 13, 10, 9, 12, 3, 7, 11, 4),
    5: (4, 12, 15, 2, 3, 13, 1, 9, 11, 10, 8, 0, 5, 7, 6, 14),
}
EXPECTED = {
    0: (392, 1200, 191, {0: 1, 3: 9}),
    1: (2142, 9280, 1070, {0: 1, 4: 1}),
    2: (7262, 36160, 3628, {0: 1, 3: 2, 4: 3}),
    3: (12542, 68560, 6270, {0: 1, 4: 1}),
    4: (13822, 77520, 6910, {0: 1, 4: 1}),
    5: (13838, 77616, 6911, {0: 1, 5: 15}),
}


def forest_via_components(mask):
    vertices = [v for v in range(N) if mask & (1 << v)]
    deg = [(NEIGHBORS[v] & mask).bit_count() for v in vertices]
    maximum = max(deg, default=0)
    edge_count = sum(deg) // 2
    components = 0
    seen = 0
    for v in vertices:
        if seen & (1 << v):
            continue
        components += 1
        todo = [v]
        seen |= 1 << v
        while todo:
            w = todo.pop()
            remaining = NEIGHBORS[w] & mask & ~seen
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                seen |= bit
                todo.append(bit.bit_length() - 1)
    return edge_count == len(vertices) - components, maximum


def forest_via_unionfind(mask):
    parent = list(range(N))

    def root(u):
        while parent[u] != u:
            u = parent[u]
        return u

    maxdegree = 0
    for u in range(N):
        if not mask & (1 << u):
            continue
        neighbors = NEIGHBORS[u] & mask
        maxdegree = max(maxdegree, neighbors.bit_count())
        for v in range(u + 1, N):
            if not neighbors & (1 << v):
                continue
            a, b = root(u), root(v)
            if a == b:
                return False, maxdegree
            parent[a] = b
    return True, maxdegree


@lru_cache(None)
def signed_boundary(mask):
    return tuple((mask ^ (1 << v), (-1) ** k)
                 for k, v in enumerate(u for u in range(N) if mask & (1 << u)))


def match_and_check(faces, order):
    remaining = set(faces)
    pairs = []
    for v in order:
        bit = 1 << v
        for lower in faces:
            upper = lower | bit
            if not lower & bit and lower in remaining and upper in remaining:
                assert upper.bit_count() == lower.bit_count() + 1
                pairs.append((lower, upper))
                remaining.remove(lower)
                remaining.remove(upper)
    lower_to_upper = dict(pairs)
    upper_to_lower = {higher: lower for lower, higher in pairs}
    assert len(pairs) == len(lower_to_upper) == len(upper_to_lower)
    assert not (set(lower_to_upper) & set(upper_to_lower))
    index = {mask: j for j, mask in enumerate(faces)}
    indegree = [0] * len(faces)
    arrows = [[] for _ in faces]
    count = 0
    for higher in faces:
        for lower, _ in signed_boundary(higher):
            if lower not in index:
                continue
            count += 1
            if lower_to_upper.get(lower) == higher:
                i, j = index[higher], index[lower]
            else:
                i, j = index[lower], index[higher]
            arrows[i].append(j)
            indegree[j] += 1
    queue = collections.deque(i for i, value in enumerate(indegree) if value == 0)
    traversed = 0
    while queue:
        i = queue.popleft()
        traversed += 1
        for j in arrows[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)
    assert traversed == len(faces), 'Directed Hasse graph contains a cycle'
    counts = dict(sorted(collections.Counter(mask.bit_count() - 1 for mask in remaining).items()))
    return pairs, remaining, lower_to_upper, upper_to_lower, count, counts


def f2_morse_matrix(f2_critical, lo, hi):
    @lru_cache(None)
    def projection(mask):
        if mask in hi:
            return {}
        if mask in f2_critical:
            return {mask: 1}
        upper = lo[mask]
        coefficient = next(c for sub, c in signed_boundary(upper) if sub == mask)
        result = collections.Counter()
        for sub, sign in signed_boundary(upper):
            if sub == mask:
                continue
            for critical, value in projection(sub).items():
                result[critical] -= coefficient * sign * value
        return {m: v for m, v in result.items() if v}

    rows = sorted(m for m in f2_critical if m.bit_count() == 4)
    cols = sorted(m for m in f2_critical if m.bit_count() == 5)
    assert len(rows) == 2 and len(cols) == 3
    matrix = [[sum(sign * projection(face).get(r, 0)
                   for face, sign in signed_boundary(col))
               for col in cols] for r in rows]
    assert matrix == [[-1, -1, 0], [-1, 0, -1]], matrix
    # Unit minor: integral boundary is surjective, no torsion; kernel is Z.
    assert abs(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) == 1
    return matrix


def verify_cycle_and_cocycle(stage1, stage4):
    certificate = json.loads(Path(__file__).with_name('cycle_cocycle.json').read_text('utf-8'))
    assert certificate['graph'] == 'Clebsch-F2^4-XOR-1,2,4,8,15'
    z = dict(certificate['cycle'])
    phi = dict(certificate['cochain'])
    assert len(z) == len(certificate['cycle']) == 96
    assert len(phi) == len(certificate['cochain']) == 143
    assert all(m in stage1 and m.bit_count() == 5 and abs(n) == 1 for m, n in z.items())
    assert all(m in stage4 and m.bit_count() == 5 and abs(n) == 1 for m, n in phi.items())
    boundary_coefficients = collections.Counter()
    for simplex, coefficient in z.items():
        for face, sign in signed_boundary(simplex):
            boundary_coefficients[face] += coefficient * sign
    assert not any(boundary_coefficients.values()), 'Witness is not an integral 4-cycle'
    checked_5 = 0
    for simplex in stage4:
        if simplex.bit_count() == 6:
            checked_5 += 1
            assert sum(sign * phi.get(face, 0) for face, sign in signed_boundary(simplex)) == 0
    assert checked_5 == 4360, checked_5
    value = sum(coefficient * phi.get(simplex, 0) for simplex, coefficient in z.items())
    assert value == -1, value
    return checked_5, value


def main():
    assert all(NEIGHBORS[u].bit_count() == 5 for u in range(N))
    assert all((NEIGHBORS[u] >> v & 1) == (NEIGHBORS[v] >> u & 1)
               for u in range(N) for v in range(N))
    for u in range(N):
        for v in range(u + 1, N):
            common = (NEIGHBORS[u] & NEIGHBORS[v]).bit_count()
            assert common == (0 if NEIGHBORS[u] & (1 << v) else 2)
    stages = [[] for _ in range(6)]
    for mask in range(1, 1 << N):
        is_forest, maxdegree = forest_via_components(mask)
        alternate, altdegree = forest_via_unionfind(mask)
        assert is_forest == alternate
        if not is_forest:
            continue
        assert maxdegree == altdegree
        for d in range(maxdegree, 6):
            stages[d].append(mask)
    stage_sets = [set(faces) for faces in stages]
    assert all(stage_sets[d].issubset(stage_sets[d + 1]) for d in range(5))
    for d, faces in enumerate(stages):
        assert all(mask in stage_sets[d] for mask in faces)
        pairs, critical, lower, upper, arrows, counts = match_and_check(faces, ORDERS[d])
        assert (len(faces), arrows, len(pairs), counts) == EXPECTED[d], (d, counts)
        if d == 2:
            matrix = f2_morse_matrix(critical, lower, upper)
            print('F2_MORSE_BOUNDARY=' + str(matrix).replace(' ', ''))
        print(f'STAGE_{d}: faces={len(faces)} pairs={len(pairs)} '
              f'incidences={arrows} critical={counts} ACYCLIC_OK')
    tested, degree = verify_cycle_and_cocycle(stage_sets[1], stage_sets[4])
    print(f'PERSISTENT_4_CYCLE: length=96 cochain_support=143 '
          f'five_simplices_checked={tested} evaluation={degree} OK')
    print('INTEGRAL_HOMOTOPY: F0=9*S3, F1=F2=F3=F4=S4, F5=15*S5')
    print('PERSISTENCE: H3=[0,1)x9; H4=[1,5)x1; H5=[5,infinity)x15')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
