#!/usr/bin/env python3
"""Exact small-field and finite Frobenius-combinatorial checks of a Fermat quartic line divisor.

This code verifies the finite incidence calculations and tests rational-point formulas.
The characteristic-independent geometric and Picard-theoretic arguments are given
in RESULT.md; these finite tests are not substituted for those arguments.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

MOD = 17
ZETA8 = 2  # 2**4 = -1 modulo 17; 2 has multiplicative order 8.
PAIRS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
ODD = (1, 3, 5, 7)


def rank_basis(vectors, p=MOD):
    a = [list(row) for row in zip(*vectors)]
    nrow, ncol = len(a), len(vectors)
    piv, r = [], 0
    for c in range(ncol):
        k = next((i for i in range(r, nrow) if a[i][c] % p), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [x * inv % p for x in a[r]]
        for i in range(nrow):
            if i != r and a[i][c] % p:
                mul = a[i][c]
                a[i] = [(x - mul * y) % p for x, y in zip(a[i], a[r])]
        piv.append(c)
        r += 1
        if r == nrow:
            break
    return a, piv


def intersection(u, v, s, t):
    A, piv = rank_basis((u, v, s, t))
    if len(piv) == 4:
        return None
    assert len(piv) == 3, ('incorrect line rank', piv)
    free = next(j for j in range(4) if j not in piv)
    x = [0] * 4
    x[free] = 1
    for row, col in enumerate(piv):
        x[col] = -A[row][free] % MOD
    pt = tuple((x[0] * u[i] + x[1] * v[i]) % MOD for i in range(4))
    assert any(pt)
    first = next(z for z in pt if z)
    return tuple(z * pow(first, -1, MOD) % MOD for z in pt)


def make_lines():
    out = []
    for typ, ((a, b), (c, d)) in enumerate(PAIRS):
        for i in ODD:
            for j in ODD:
                u, v = [0]*4, [0]*4
                u[a], u[b] = 1, pow(ZETA8, i, MOD)
                v[c], v[d] = 1, pow(ZETA8, j, MOD)
                out.append((typ, i, j, tuple(u), tuple(v)))
    return out


def orbit_spectrum(elements, fn):
    unseen = set(elements)
    result = Counter()
    while unseen:
        first = next(iter(unseen))
        v, orbit = first, []
        while v not in orbit:
            assert v in unseen
            unseen.remove(v)
            orbit.append(v)
            v = fn(v)
        assert v == first
        result[len(orbit)] += 1
    return dict(sorted(result.items()))


def check_geometry():
    lines = make_lines()
    assert len(lines) == 48
    points = defaultdict(set)
    intersecting = 0
    between = Counter()
    for i, j in combinations(range(48), 2):
        p = intersection(lines[i][3], lines[i][4], lines[j][3], lines[j][4])
        if p is not None:
            points[p].update((i,j))
            intersecting += 1
            between[tuple(sorted((lines[i][0], lines[j][0])))] += 1
    # Every incidence line is contained in the Fermat quartic.
    assert all(all(sum(z**4 for z in v) % MOD == 0 for v in (L[3], L[4])) for L in lines)
    assert intersecting == 336
    assert dict(Counter(map(len, points.values()))) == {2:192, 4:24}
    assert len(points) == 216
    assert between[(0, 0)] == between[(1, 1)] == between[(2, 2)] == 48
    assert between[(0, 1)] == between[(0, 2)] == between[(1, 2)] == 64
    assert all(sum(i in x for x in points.values()) == 10 for i in range(48))
    # Every incidence set describes one geometric intersection point.
    P = {frozenset(S) for S in points.values()}
    assert len(P) == 216
    line_key = {L[:3]: i for i,L in enumerate(lines)}
    # Bipartite normalization-incidence graph with components and singularities as vertices.
    graph = defaultdict(set)
    for S in P:
        for i in S:
            graph[('line', i)].add(('sing', S))
            graph[('sing', S)].add(('line', i))
    assert len(graph) == 264
    assert sum(map(len, graph.values())) == 960
    seen = {('line', 0)}
    queue = deque(seen)
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    assert len(seen) == len(graph)
    E = sum(map(len, graph.values())) // 2
    b1 = E - len(graph) + 1
    assert E == 480 and b1 == 217
    delta = 192 + 24*6
    assert delta - 48 + 1 == 289
    unipotent = 24*3
    assert unipotent == 72 and unipotent+b1 == 289
    print('GEOMETRY_OK lines=48 nodes=192 ordinary_fourfold=24 singular_points=216 pair_intersections=336')
    print('GENUS_OK arithmetic_genus=289 graph_vertices=264 graph_edges=480 graph_b1=217 unipotent_dim=72')
    for qmod in (1,3,5,7):
        perm = {i:line_key[(L[0], L[1]*qmod%8, L[2]*qmod%8)] for i,L in enumerate(lines)}
        def sigma(S):return frozenset(perm[i] for i in S)
        assert all(sigma(S) in P for S in P)
        line_spec = orbit_spectrum(range(48), lambda i:perm[i])
        point_spec = orbit_spectrum(P, sigma)
        if qmod == 1:
            assert line_spec == {1:48} and point_spec == {1:216}
        else:
            assert line_spec == {2:24} and point_spec == {2:108}
            assert all(perm[i] != i for i in range(48))
            assert all(sigma(S) != S for S in P)
            # Free degree-two quotient has rank 240-132+1=109; its
            # integral cycle lattice has Z_trivial + Z[C2]^(109-1).
            assert E//2-(len(graph)//2)+1 == 109
        print('FROBENIUS_OK q_mod_8={} line_orbits={} singular_orbits={}'.format(qmod,line_spec,point_spec))
    return P


def count_rational_points(q):
    # Set-theoretic locus: union over the three pairings of two binomial quartics.
    # Enumerate every projective point, with first nonzero coordinate normalized to 1.
    powers = [pow(i, 4, q) for i in range(q)]
    hits = 0
    for first in range(4):
        tail_len = 3-first
        from itertools import product
        for tail in product(range(q),repeat=tail_len):
            x = (0,)*first + (1,) + tail
            if any((powers[x[a]]+powers[x[b]])%q == 0 and
                   (powers[x[c]]+powers[x[d]])%q == 0
                   for (a,b),(c,d) in PAIRS):
                hits += 1
    return hits


def verify_points():
    for q in (5,7,11,13,17,19,23,41):
        actual = count_rational_points(q)
        predicted = 48*q-216 if q%8==1 else 0
        assert actual == predicted,(q,actual,predicted)
        print('POINT_COUNT_OK field={} actual={} predicted={}'.format(q,actual,predicted))

if __name__ == '__main__':
    check_geometry()
    verify_points()
    print('VERIFY_OK')
