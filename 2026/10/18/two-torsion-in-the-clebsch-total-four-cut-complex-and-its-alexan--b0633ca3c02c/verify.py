#!/usr/bin/env python3
"""Exact finite verification of total four-cut topology for the Clebsch graph.

All faces are represented by sixteen-bit nonnegative integers. The program
performs exhaustive enumeration, builds two Alexander-dual face posets,
checks complete discrete-Morse acyclicity, and computes integral Morse
boundary coefficients by signed gradient-path recursion.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 16
GEN = (1, 2, 4, 8, 15)
FULL = (1 << N) - 1


def vertices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def downward_closure(facets):
    faces = {0}
    for facet in facets:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub - 1) & facet
    return faces


def element_matching(faces):
    unmatched = set(faces)
    lower_to_upper = {}
    for v in range(N):
        bit = 1 << v
        for low in sorted(f for f in unmatched if not (f & bit)):
            high = low | bit
            if low in unmatched and high in unmatched:
                unmatched.remove(low)
                unmatched.remove(high)
                lower_to_upper[low] = high
    assert len(unmatched) + 2 * len(lower_to_upper) == len(faces)
    return lower_to_upper, unmatched


def verify_acyclic(faces, pairs):
    # Matched covers are directed low -> high, other covers high -> low.
    indegree = {f: 0 for f in faces}
    covers = 0
    for high in faces:
        for v in vertices(high):
            low = high ^ (1 << v)
            assert low in faces
            if pairs.get(low) == high:
                indegree[high] += 1
            else:
                indegree[low] += 1
            covers += 1
    queue = deque(f for f, d in indegree.items() if d == 0)
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for v in vertices(node):
            low = node ^ (1 << v)
            if pairs.get(low) != node:
                indegree[low] -= 1
                if indegree[low] == 0:
                    queue.append(low)
        high = pairs.get(node)
        if high is not None:
            indegree[high] -= 1
            if indegree[high] == 0:
                queue.append(high)
    assert visited == len(faces), (visited, len(faces))
    return covers


def morse_boundary(pairs, critical, low_degree):
    # Project an ordinary simplicial boundary to unmatched cells, cancelling
    # matched units. The coefficient of lower face low in upper high equals
    # (-1)^(position of the omitted vertex of high).
    target = sorted(f for f in critical if f.bit_count() - 1 == low_degree)
    source = sorted(f for f in critical if f.bit_count() - 1 == low_degree + 1)
    target_idx = {f: i for i, f in enumerate(target)}
    matched_upper = set(pairs.values())

    @lru_cache(maxsize=None)
    def project(face):
        if face in target_idx:
            return {target_idx[face]: 1}
        if face in matched_upper:
            return {}
        if face not in pairs:
            raise AssertionError(('unmatched unindexed face', face))
        upper = pairs[face]
        vs = tuple(vertices(upper))
        omitted = (upper ^ face).bit_length() - 1
        position = vs.index(omitted)
        # Canceled boundary relation: [face] = -inc(face,upper)^-1
        # * sum_{other facets} inc(other,upper) [other].
        expansion = {}
        for j, v in enumerate(vs):
            if j == position:
                continue
            sign = (-1 if (position + j) % 2 == 0 else 1)
            for i, n in project(upper ^ (1 << v)).items():
                expansion[i] = expansion.get(i, 0) + sign * n
        return {i: n for i, n in expansion.items() if n}

    matrix_columns = []
    for upper in source:
        vec = [0] * len(target)
        for j, v in enumerate(vertices(upper)):
            for i, n in project(upper ^ (1 << v)).items():
                vec[i] += ((-1) ** j) * n
        matrix_columns.append(vec)
    return target, source, matrix_columns


def analyze(faces, label, expected_counts, expected_critical, expected_diffs):
    f_counts = dict(sorted(Counter(f.bit_count()-1 for f in faces).items()))
    assert f_counts == expected_counts, (label, f_counts)
    pairs, critical = element_matching(faces)
    critical_counts = dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
    assert critical_counts == expected_critical, (label, critical_counts)
    assert 0 in pairs and pairs[0] != 0  # augmented matching; no spurious (-1) cell
    covers = verify_acyclic(faces, pairs)
    print(f'{label}: face_counts={f_counts}')
    print(f'{label}: faces={len(faces)}, cover_relations={covers}, pairs={len(pairs)}, critical={critical_counts}')
    for degree, want in expected_diffs.items():
        target, source, actual = morse_boundary(pairs, critical, degree)
        assert actual == want, (label, degree, actual)
        print(f'{label}: integral_Morse_boundary_{degree+1}_to_{degree}={actual}')
    return f_counts


def main():
    adjacency = {v: {v ^ step for step in GEN} for v in range(N)}
    assert all(len(adjacency[v]) == 5 for v in range(N))
    assert all(u in adjacency[v] for u in range(N) for v in adjacency[u])
    independent4 = []
    independent5 = []
    for size, found in ((4, independent4), (5, independent5)):
        for tup in combinations(range(N), size):
            if all(v not in adjacency[u] for u,v in combinations(tup,2)):
                found.append(sum(1 << v for v in tup))
    assert len(independent4) == 120 and len(independent5) == 16
    print(f'graph: vertices=16, degree=5, independent_4_sets={len(independent4)}, independent_5_sets={len(independent5)}')

    total4 = downward_closure(FULL ^ indep for indep in independent4)
    bounded4 = {mask for mask in range(1 << N)
                if not any((mask & ind) == ind for ind in independent4)}
    assert all(((FULL ^ mask) not in total4) == (mask in bounded4)
               for mask in range(1 << N))

    k = analyze(total4, 'TOTAL4',
                {-1:1, 0:16, 1:120, 2:560, 3:1820, 4:4368,
                 5:8008, 6:11440, 7:12270, 8:9040, 9:4096, 10:1056, 11:120},
                {6:1, 7:1, 8:45}, {6:[[2]], 7:[[0]]*45})
    l = analyze(bounded4, 'BOUNDED4',
                {-1:1, 0:16, 1:120, 2:560, 3:1700, 4:3312,
                 5:3912, 6:2400, 7:600},
                {5:45, 6:1, 7:1}, {5:[[0]*45], 6:[[-2]]})

    assert sum((-1)**d*n for d,n in k.items() if d>=0) - 1 == 45
    assert sum((-1)**d*n for d,n in l.items() if d>=0) - 1 == -45
    print('HOMOLOGY: TOTAL4 H6=Z/2, H8=Z^45; other reduced integral groups zero')
    print('HOMOLOGY: BOUNDED4 H5=Z^45, H6=Z/2; other reduced integral groups zero')
    print('CONNECTIVITY: TOTAL4 is 5-connected; BOUNDED4 is 4-connected')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
