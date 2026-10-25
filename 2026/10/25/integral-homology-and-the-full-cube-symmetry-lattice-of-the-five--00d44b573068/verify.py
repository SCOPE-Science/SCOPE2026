#!/usr/bin/env python3
"""Finite integral chain and symmetry checks for the five-cube independence complex.

Run with Python 3.9+; standard library only. All faces, matchings, cycle
chains, and signed projections are reconstructed, not loaded from data files.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations, product

D = 5
N = 1 << D
ADJ = tuple(sum(1 << (x ^ (1 << k)) for k in range(D)) for x in range(N))


def enumerate_faces():
    out = set()

    def dfs(remaining, chosen):
        if not remaining:
            out.add(chosen)
            return
        bit = remaining & -remaining
        vertex = bit.bit_length() - 1
        dfs(remaining ^ bit, chosen)
        dfs(remaining & ~(bit | ADJ[vertex]), chosen | bit)

    dfs((1 << N) - 1, 0)
    return out


def matching(nonempty):
    available = set(nonempty)
    upward, downward = {}, {}
    pivots = sorted(range(N), key=lambda v: v.bit_count() & 1)
    for v in pivots:
        bit = 1 << v
        # The order within a stage has no effect: a pair differs in this bit.
        for face in tuple(available):
            coface = face | bit
            if not (face & bit) and face in available and coface in available:
                available.remove(face)
                available.remove(coface)
                upward[face] = coface
                downward[coface] = face
    return available, upward, downward


def check_acyclic(nonempty, upward, downward):
    indeg = {face: 0 for face in nonempty}
    incidences = 0
    for face in nonempty:
        rest = face
        while rest:
            bit = rest & -rest
            rest ^= bit
            lower = face ^ bit
            if not lower:
                continue
            incidences += 1
            if downward.get(face) == lower:
                indeg[face] += 1
            else:
                indeg[lower] += 1
    queue = deque(x for x, degree in indeg.items() if degree == 0)
    visited = 0
    while queue:
        face = queue.popleft()
        visited += 1
        rest = face
        while rest:
            bit = rest & -rest
            rest ^= bit
            lower = face ^ bit
            if not lower or downward.get(face) == lower:
                continue
            indeg[lower] -= 1
            if indeg[lower] == 0:
                queue.append(lower)
        if face in upward:
            higher = upward[face]
            indeg[higher] -= 1
            if indeg[higher] == 0:
                queue.append(higher)
    assert visited == len(nonempty), (visited, len(nonempty))
    return incidences


def signed_boundary(face):
    rest = face
    j = 0
    while rest:
        bit = rest & -rest
        rest ^= bit
        yield face ^ bit, (-1 if j & 1 else 1)
        j += 1


def sphere_edges(k, parity):
    edges = []
    for x in range(N):
        if x & (1 << k):
            continue
        base = (x & ((1 << k) - 1)) | ((x >> (k + 1)) << k)
        if base.bit_count() % 2 == parity:
            edges.append((x, x ^ (1 << k)))
    assert len(edges) == 8
    # Distinct edges of this list have no cross-edges in the five-cube.
    for i in range(8):
        for j in range(i + 1, 8):
            assert all(not (ADJ[u] & (1 << v)) for u in edges[i] for v in edges[j])
    return edges


def sphere_cycle(k, parity, nonempty):
    edges = sphere_edges(k, parity)
    result = defaultdict(int)
    for choices in product((0, 1), repeat=8):
        vertices = [edges[i][choices[i]] for i in range(8)]
        simplex = sum(1 << v for v in vertices)
        assert simplex in nonempty and simplex.bit_count() == 8
        inversions = sum(vertices[i] > vertices[j]
                         for i in range(8) for j in range(i + 1, 8))
        result[simplex] += (-1) ** (sum(choices) + inversions)
    assert len(result) == 256 and set(result.values()) <= {1, -1}
    boundary = defaultdict(int)
    for simplex, coefficient in result.items():
        for facet, sign in signed_boundary(simplex):
            boundary[facet] += coefficient * sign
    assert all(val == 0 for val in boundary.values())
    return result


def determinant_exact(A):
    A = [list(row) for row in A]
    n = len(A)
    sign = 1
    last = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            m = next((i for i in range(k + 1, n) if A[i][k]), None)
            if m is None:
                return 0
            A[k], A[m] = A[m], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = A[i][j] * pivot - A[i][k] * A[k][j]
                assert numerator % last == 0
                A[i][j] = numerator // last
            A[i][k] = 0
        last = pivot
    return sign * A[n - 1][n - 1]


def morse_projection(critical, upward, downward):
    degree_seven = sorted(f for f in critical if f.bit_count() == 8)
    targets = {f: j for j, f in enumerate(degree_seven)}

    @lru_cache(maxsize=None)
    def project(face):
        if face in targets:
            return ((targets[face], 1),)
        if face in downward:
            return ()
        assert face in upward
        coface = upward[face]
        facets = dict(signed_boundary(coface))
        pivot_sign = facets[face]
        accum = defaultdict(int)
        for other, sign in facets.items():
            if other == face:
                continue
            for j, value in project(other):
                accum[j] -= pivot_sign * sign * value
        return tuple(sorted((j, v) for j, v in accum.items() if v))

    return project


def apply(x, perm, translation):
    return translation ^ sum(((x >> i & 1) << perm[i]) for i in range(D))


def sign_perm(values):
    inversions = sum(values[i] > values[j]
                     for i in range(len(values))
                     for j in range(i + 1, len(values)))
    return -1 if inversions & 1 else 1


def check_sphere_symmetry(perm, translation):
    for k in range(D):
        target = perm[k]
        shifted = sum((translation >> j) & 1 for j in range(D) if j != target) & 1
        for parity in (0, 1):
            source = sphere_edges(k, parity)
            dest = sphere_edges(target, parity ^ shifted)
            factors = []
            flips = 0
            for a, b in source:
                aa = apply(a, perm, translation)
                bb = apply(b, perm, translation)
                assert aa ^ bb == (1 << target)
                flips += int(bool(aa & (1 << target)))
                factors.append(dest.index((min(aa, bb), max(aa, bb))))
            assert sign_perm(factors) * (-1) ** flips == 1


def lefschetz_independence_poly(perm, translation):
    """I(-1) of the graph of allowed permutation orbits of Q5 vertices."""
    visited = set()
    orbits = []
    for v in range(N):
        if v in visited:
            continue
        orbit = []
        x = v
        while x not in visited:
            orbit.append(x)
            visited.add(x)
            x = apply(x, perm, translation)
        assert x == v
        mask = sum(1 << z for z in orbit)
        if not any(ADJ[z] & (mask ^ (1 << z)) for z in orbit):
            orbits.append(orbit)
    n = len(orbits)
    conflict = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if any(ADJ[x] & (1 << y) for x in orbits[i] for y in orbits[j]):
                conflict[i] |= 1 << j
                conflict[j] |= 1 << i

    @lru_cache(None)
    def p(mask):
        if mask == 0:
            return 1
        bit = mask & -mask
        i = bit.bit_length() - 1
        return p(mask ^ bit) - p(mask & ~(bit | conflict[i]))
    return p((1 << n) - 1)


def expected_high_trace(perm, translation):
    count = 0
    for k in range(D):
        if perm[k] == k:
            shifted = sum((translation >> j) & 1 for j in range(D) if j != k) & 1
            if not shifted:
                count += 2
    return count


def main():
    allfaces = enumerate_faces()
    nonempty = allfaces - {0}
    f = Counter(face.bit_count() - 1 for face in nonempty)
    assert len(allfaces) == 254475
    assert [f[k] for k in range(16)] == [
        32, 416, 2880, 11760, 29856, 48960, 54304, 44240,
        29920, 17952, 9088, 3672, 1120, 240, 32, 2]
    assert sum((-1) ** dim * count for dim, count in f.items()) == -10
    # The reduced Euler characteristic subtracts one for the connected component.
    assert sum((-1) ** dim * count for dim, count in f.items()) - 1 == -11
    critical, up, down = matching(nonempty)
    counts = Counter(face.bit_count() - 1 for face in critical)
    assert counts == Counter({0: 1, 5: 1, 7: 10})
    assert len(up) == len(down) == 127231
    assert len(critical) + 2 * len(up) == len(nonempty)
    incidences = check_acyclic(nonempty, up, down)
    assert incidences == 1844864
    proj = morse_projection(critical, up, down)
    matrix = []
    for k in range(D):
        for parity in (0, 1):
            cycle = sphere_cycle(k, parity, nonempty)
            coefficients = defaultdict(int)
            for face, weight in cycle.items():
                for i, coeff in proj(face):
                    coefficients[i] += weight * coeff
            matrix.append([coefficients[i] for i in range(10)])
    determinant = determinant_exact(matrix)
    assert determinant == -1
    groups_checked = 0
    for perm in permutations(range(D)):
        perm_sign = sign_perm(perm)
        for translation in range(1 << D):
            check_sphere_symmetry(perm, translation)
            expected_low = perm_sign * (-1) ** translation.bit_count()
            got_reduced_poly = lefschetz_independence_poly(perm, translation)
            assert got_reduced_poly == expected_high_trace(perm, translation) + expected_low
            groups_checked += 1
    assert groups_checked == 3840
    print('FACES_WITH_EMPTY', len(allfaces))
    print('F_VECTOR', ','.join(str(f[i]) for i in range(16)))
    print('MATCHING_PAIRS', len(up))
    print('CRITICAL', dict(sorted(counts.items())))
    print('HASSE_INCIDENCES', incidences)
    print('TOPOLOGICAL_SORT', len(nonempty))
    print('INTEGRAL_CARRIER_DETERMINANT', determinant)
    print('SYMMETRIES_CHECKED', groups_checked)
    print('HOMOLOGY_RANKS H5=1 H7=10; OTHER_REDUCED=0')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
