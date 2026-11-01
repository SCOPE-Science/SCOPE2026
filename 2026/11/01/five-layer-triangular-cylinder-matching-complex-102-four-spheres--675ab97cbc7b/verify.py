"""Reproducible finite proof certificate for the matching complex of C3 square P5.

Python 3 standard library only.  All simplices and codimension-one
incidences of the finite complex are checked, not sampled.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import permutations

N = 5
PIVOT_ORDER = (2, 1, 3, 25, 6, 23, 24, 16, 22, 12, 21, 15, 7,
               10, 18, 17, 14, 11, 8, 5, 20, 19, 4, 9, 13, 0, 26)
EXPECTED_F = (27, 279, 1399, 3558, 4338, 2100, 276)
EXPECTED_CLASS_CHARACTERS = {(0, 0): 102, (1, 0): 0, (2, 0): 0,
                             (0, 1): 12, (1, 1): 2, (2, 1): 0}


def grid_edges():
    es = set()
    for c in range(N):
        for r in range(3):
            es.add(tuple(sorted(((r, c), ((r + 1) % 3, c)))))
    for c in range(N - 1):
        for r in range(3):
            es.add(((r, c), (r, c + 1)))
    return tuple(sorted(es))


def enumerate_matching_faces(edges):
    # A matching is uniquely generated when its last edge is introduced.
    fs = [0]
    used = [sum(1 << j for j, (a, b) in enumerate(edges)
                if a in e or b in e) for e in edges]
    for i in range(len(edges)):
        fs += [mask | (1 << i) for mask in fs[:] if not mask & used[i]]
    assert len(fs) == len(set(fs))
    return set(fs)


def independent_matching_polynomial(edges):
    # Independent vertex-deletion recurrence, not simplex enumeration.
    vs = sorted(set(v for e in edges for v in e))
    idx = {v: i for i, v in enumerate(vs)}
    adj = [0] * len(vs)
    for a, b in edges:
        x, y = idx[a], idx[b]
        adj[x] |= 1 << y
        adj[y] |= 1 << x

    @lru_cache(None)
    def poly(mask):
        if mask == 0:
            return (1,)
        p = (mask & -mask).bit_length() - 1
        rest = mask & ~(1 << p)
        v = list(poly(rest))
        near = rest & adj[p]
        while near:
            q = (near & -near).bit_length() - 1
            near &= near - 1
            sub = poly(rest & ~(1 << q))
            if len(v) < len(sub) + 1:
                v += [0] * (len(sub) + 1 - len(v))
            for k, val in enumerate(sub):
                v[k + 1] += val
        return tuple(v)
    return poly((1 << len(vs)) - 1)


def gradient_matching(nonempty_faces):
    unpaired = set(nonempty_faces)
    pairs = []
    for pivot in PIVOT_ORDER:
        for low in sorted(z for z in unpaired if not z & (1 << pivot)):
            high = low | (1 << pivot)
            if low in unpaired and high in unpaired:
                assert high.bit_count() == low.bit_count() + 1
                unpaired.remove(low)
                unpaired.remove(high)
                pairs.append((low, high))
    return unpaired, pairs


def verify_full_gradient_dag(nonempty_faces, pairs):
    ordered = sorted(nonempty_faces)
    pos = {f: i for i, f in enumerate(ordered)}
    directed = [[] for _ in ordered]
    indeg = [0] * len(ordered)
    paired = set(pairs)
    assert len(paired) == len(pairs)
    assert len(set(x for p in pairs for x in p)) == 2 * len(pairs)
    incidences = 0
    for high in ordered:
        bits = high
        while bits:
            lowest = bits & -bits
            bits -= lowest
            low = high ^ lowest
            if low == 0:
                continue
            assert low in pos
            u, v = ((pos[low], pos[high]) if (low, high) in paired
                    else (pos[high], pos[low]))
            directed[u].append(v)
            indeg[v] += 1
            incidences += 1
    queue = deque(i for i, x in enumerate(indeg) if x == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in directed[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    assert visited == len(ordered), 'Gradient cycle present'
    return incidences


def edge_permutation(edges, rows, reverse):
    ids = {e: i for i, e in enumerate(edges)}
    return tuple(ids[tuple(sorted((rows[r], N - 1 - c if reverse else c)
                                  for r, c in e))] for e in edges)


def permutation_sign(sequence):
    inversions = sum(sequence[i] > sequence[j]
                     for i in range(len(sequence))
                     for j in range(i + 1, len(sequence)))
    return -1 if inversions % 2 else 1


def homology_character_from_faces(faces, perm):
    # H~_4 is the only nonzero reduced group, hence the reduced
    # Lefschetz trace is its character.
    euler_trace = -1  # augmented empty face in degree -1
    for face in faces:
        inds = [i for i in range(len(perm)) if face & (1 << i)]
        moved = [perm[i] for i in inds]
        if set(moved) != set(inds):
            continue
        loc = {j: k for k, j in enumerate(sorted(moved))}
        orientation = permutation_sign([loc[j] for j in moved])
        euler_trace += (-1 if (len(inds) - 1) % 2 else 1) * orientation
    return euler_trace


def homology_character_from_edge_orbits(edges, perm):
    # Independent check: invariant matchings are disjoint unions of full
    # permutation orbits of edges.  Each selected orbit contributes -1
    # to its reduced Lefschetz weight.
    visited = set()
    permitted_orbits = []
    for i in range(len(edges)):
        if i in visited:
            continue
        cyc, j = [], i
        while j not in visited:
            visited.add(j)
            cyc.append(j)
            j = perm[j]
        ends = [v for k in cyc for v in edges[k]]
        if len(ends) == len(set(ends)):
            permitted_orbits.append(set(ends))
    m = len(permitted_orbits)
    conflicts = [0] * m
    for i in range(m):
        for j in range(m):
            if i != j and permitted_orbits[i] & permitted_orbits[j]:
                conflicts[i] |= 1 << j

    @lru_cache(None)
    def alternating_independent_sets(mask):
        if not mask:
            return 1
        k = (mask & -mask).bit_length() - 1
        return (alternating_independent_sets(mask & ~(1 << k))
                - alternating_independent_sets(mask & ~(1 << k) & ~conflicts[k]))
    return -alternating_independent_sets((1 << m) - 1)


def symmetry_check(edges, faces):
    # Classes of S3: identity, transposition, three-cycle.
    byclass = {}
    for rows in permutations(range(3)):
        if rows == (0, 1, 2):
            cls = 0
        elif sum(rows[i] == i for i in range(3)) == 1:
            cls = 1
        else:
            cls = 2
        for reverse in (0, 1):
            perm = edge_permutation(edges, rows, reverse)
            assert sorted(perm) == list(range(len(edges)))
            a = homology_character_from_faces(faces, perm)
            b = homology_character_from_edge_orbits(edges, perm)
            assert a == b
            assert a == EXPECTED_CLASS_CHARACTERS[(cls, reverse)]
            byclass[(cls, reverse)] = a
    assert len(byclass) == 6
    # Character inner products against every irreducible of S3 x C2.
    sizes = (1, 3, 2)
    irreps = {'trivial': (1, 1, 1), 'sign': (1, -1, 1),
              'standard': (2, 0, -1)}
    output = {}
    for name, char in irreps.items():
        for eig in (1, -1):
            numerator = sum(sizes[i] * char[i]
                            * (byclass[(i, 0)] + eig * byclass[(i, 1)])
                            for i in range(3))
            assert numerator % 12 == 0
            output[(name, eig)] = numerator // 12
    assert output == {('trivial', 1): 10, ('trivial', -1): 7,
                      ('sign', 1): 9, ('sign', -1): 8,
                      ('standard', 1): 19, ('standard', -1): 15}
    assert sum(output[(name, eig)] * (2 if name == 'standard' else 1)
               for name, eig in output) == 102
    return output


def main():
    edges = grid_edges()
    assert len(edges) == 27 and len(set(v for e in edges for v in e)) == 15
    fs = enumerate_matching_faces(edges)
    assert independent_matching_polynomial(edges) == (1,) + EXPECTED_F
    assert len(fs) == 11978
    nonempty = fs - {0}
    assert tuple(Counter(z.bit_count() - 1 for z in nonempty)[k]
                 for k in range(7)) == EXPECTED_F
    assert sum((-1) ** k * n for k, n in enumerate(EXPECTED_F)) - 1 == 102
    crit, pairs = gradient_matching(nonempty)
    assert len(pairs) == 5937
    assert Counter(x.bit_count() - 1 for x in crit) == {0: 1, 4: 102}
    incidences = verify_full_gradient_dag(nonempty, pairs)
    assert incidences == 55209
    reps = symmetry_check(edges, nonempty)
    print('VERIFY_OK edges=27 faces=11977 incidences=55209 pairs=5937',
          'critical=(1 in degree 0, 102 in degree 4)',
          'symmetry=all_12_automorphisms', flush=True)
    return reps


if __name__ == '__main__':
    main()
