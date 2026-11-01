#!/usr/bin/env python3
"""Exact finite simplicial and integral-chain verification for a truncated tetrahedron.
Usage: python3 verify.py (from any working directory); Python standard library only.
"""
import collections
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
LABELS = [(a, b) for a in range(4) for b in range(4) if a != b]
POINTS = [tuple(2 * BASE[a][j] + BASE[b][j] for j in range(3)) for a, b in LABELS]
N = len(POINTS)
IDS = {p: i for i, p in enumerate(LABELS)}
D = [[sum((POINTS[i][h] - POINTS[j][h]) ** 2 for h in range(3))
      for j in range(N)] for i in range(N)]


def subset(mask):
    return tuple(i for i in range(N) if (mask >> i) & 1)


def mask(vertices):
    return sum(1 << x for x in vertices)


def complex_at(squared_scale):
    return {m for m in range(1, 1 << N)
            if all(D[i][j] <= squared_scale
                   for i, j in itertools.combinations(subset(m), 2))}


def fvector(faces):
    c = collections.Counter(m.bit_count() - 1 for m in faces)
    return tuple(c[i] for i in range(max(c) + 1))


def verify_matching(s, expected):
    F = complex_at(s)
    cert = json.loads((HERE / 'certificates' / ('tt%d_certificate.json' % s)).read_text())
    assert len(cert['vertices']) == N
    assert [(a, b) for a, b, _ in cert['vertices']] == LABELS
    pairs = [(mask(a), mask(b)) for a, b in cert['pairs']]
    critical = [mask(c) for c in cert['critical']]
    assert len(pairs) == expected['pairs']
    assert len(set(critical)) == len(critical)
    seen = set()
    match_set = set()
    for lower, upper in pairs:
        assert lower in F and upper in F and lower & upper == lower
        assert upper.bit_count() == lower.bit_count() + 1
        assert lower not in seen and upper not in seen
        seen.add(lower); seen.add(upper)
        match_set.add((lower, upper))
    assert set(critical) == (F - seen)
    assert collections.Counter(m.bit_count() - 1 for m in critical) == expected['critical']
    # Forman directed Hasse diagram: reverse precisely the matched incidences.
    nxt = {m: [] for m in F}
    indeg = {m: 0 for m in F}
    for upper in F:
        for j in subset(upper):
            lower = upper ^ (1 << j)
            if lower not in F:
                continue
            src, dst = (lower, upper) if (lower, upper) in match_set else (upper, lower)
            nxt[src].append(dst); indeg[dst] += 1
    q = collections.deque(v for v in F if indeg[v] == 0)
    count = 0
    while q:
        v = q.popleft(); count += 1
        for u in nxt[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)
    assert count == len(F), 'Directed matching cycle'
    print('MORSE scale_squared=%d faces=%s pairs=%d critical=%s acyclic=True' %
          (s, fvector(F), len(pairs), dict(sorted(expected['critical'].items()))))


def sub(u, v):
    return tuple(u[j] - v[j] for j in range(3))


def dot(u, v):
    return sum(u[j] * v[j] for j in range(3))


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def outward(order):
    xyz = [POINTS[k] for k in order]
    center = tuple(sum(pt[j] for pt in xyz) for j in range(3))
    prod = dot(cross(sub(xyz[1], xyz[0]), sub(xyz[2], xyz[0])), center)
    assert prod != 0
    return order if prod > 0 else [order[0]] + list(reversed(order[1:]))


def oriented_triangle(t):
    parity = sum(t[i] > t[j] for i in range(3) for j in range(i + 1, 3))
    return tuple(sorted(t)), -1 if parity % 2 else 1


def surface_cycle():
    # Outward-oriented boundary: four triangular truncations and four hexagons.
    # Each regular hexagon is triangulated by its three short ears and central triangle.
    Z = collections.defaultdict(int)
    for a in range(4):
        order = outward([IDS[a, b] for b in range(4) if a != b])
        simplex, sign = oriented_triangle(order); Z[simplex] += sign
    for excluded in range(4):
        a, b, c = [k for k in range(4) if k != excluded]
        order = outward([IDS[a, b], IDS[b, a], IDS[b, c],
                         IDS[c, b], IDS[c, a], IDS[a, c]])
        for j in ([0, 1, 2], [0, 2, 4], [2, 3, 4], [4, 5, 0]):
            simplex, sign = oriented_triangle([order[k] for k in j]); Z[simplex] += sign
    return {k: v for k, v in Z.items() if v}


def boundary(chain):
    b = collections.defaultdict(int)
    for simplex, coeff in chain.items():
        for j in range(len(simplex)):
            b[simplex[:j] + simplex[j+1:]] += coeff * ((-1) ** j)
    return {k: v for k, v in b.items() if v}


def greedy_sphere_collapse():
    faces = complex_at(32)
    pairs = []
    while True:
        maximal = [m for m in faces if not any((m | (1 << j)) in faces for j in range(N) if not (m >> j) & 1)]
        maximal.sort(key=lambda m: (-m.bit_count(), subset(m)))
        choice = None
        for upper in maximal:
            for j in subset(upper):
                lower = upper ^ (1 << j)
                immediate = sum((lower | (1 << k)) in faces for k in range(N) if not (lower >> k) & 1)
                if lower in faces and immediate == 1:
                    choice = lower, upper
                    break
            if choice is not None:
                break
        if choice is None:
            break
        lo, up = choice
        assert lo in faces and up in faces
        pairs.append(choice)
        faces.remove(lo); faces.remove(up)
    return faces, pairs


def verify_inclusion():
    Z = surface_cycle()
    assert len(Z) == 20 and set(Z.values()) <= {-1, 1}
    assert not boundary(Z)
    F24 = complex_at(24)
    assert all(mask(t) in F24 for t in Z)
    core, pairs = greedy_sphere_collapse()
    triangles = {subset(m) for m in core if m.bit_count() == 3}
    edges = {subset(m) for m in core if m.bit_count() == 2}
    vertices = {subset(m) for m in core if m.bit_count() == 1}
    assert (len(vertices), len(edges), len(triangles)) == (10, 24, 16)
    assert len(pairs) == 146
    # A closed connected 2-manifold of Euler characteristic 2 is a sphere.
    for edge in edges:
        assert sum(set(edge) <= set(tri) for tri in triangles) == 2
    for (v,) in vertices:
        link_edges = [tuple(j for j in tri if j != v) for tri in triangles if v in tri]
        linkverts = set(itertools.chain.from_iterable(link_edges))
        assert len(link_edges) == len(linkverts)
        degree = collections.Counter(x for e in link_edges for x in e)
        assert all(degree[u] == 2 for u in linkverts)
        todo = [next(iter(linkverts))]; seen = set(todo)
        while todo:
            w = todo.pop()
            for e in link_edges:
                if w in e:
                    z = e[1] if w == e[0] else e[0]
                    if z not in seen:
                        seen.add(z); todo.append(z)
        assert seen == linkverts
    todo = [next(iter(vertices))[0]]; seen = set(todo)
    while todo:
        w = todo.pop()
        for edge in edges:
            if w in edge:
                z = edge[1] if w == edge[0] else edge[0]
                if z not in seen:
                    seen.add(z); todo.append(z)
    assert len(seen) == len(vertices)
    assert len(vertices) - len(edges) + len(triangles) == 2
    # Elementary-collapse chain retraction: when a free triangular face
    # sigma belongs to a unique tetrahedron tau, subtract its coefficient
    # times boundary(tau) divided by its incidence sign in that boundary.
    T = dict(Z)
    for lo, up in pairs:
        if lo.bit_count() == 3:
            sigma = subset(lo)
            tau = subset(up)
            coeff = T.get(sigma, 0)
            if coeff:
                missing = next(j for j in tau if not (lo >> j) & 1)
                incidence = (-1) ** tau.index(missing)
                for j in range(4):
                    face = tau[:j] + tau[j+1:]
                    T[face] = T.get(face, 0) - coeff * incidence * ((-1) ** j)
                    if T[face] == 0:
                        del T[face]
        elif lo.bit_count() == 2:
            assert T.get(subset(up), 0) == 0
    assert not boundary(T)
    assert set(T) == triangles and {abs(c) for c in T.values()} == {1}
    print('INCLUSION boundary_cycle=20 collapse_pairs=146 core=(10,24,16) sphere=True image_primitive=True')


def main():
    counts = collections.Counter(D[i][j] for i in range(N) for j in range(i+1,N))
    assert dict(sorted(counts.items())) == {8:18,24:24,32:12,40:12}
    assert len(POINTS) == len(set(POINTS)) == 12
    print('DISTANCES_SQUARED', dict(sorted(counts.items())), 'unit_edge_normalization=divide_by_sqrt8')
    for s, vals in [(8, (12,18,4)),(24,(12,42,48,12)),(32,(12,54,112,108,48,8))]:
        assert fvector(complex_at(s)) == vals
    verify_matching(8, {'pairs':15, 'critical':{0:1,1:3}})
    verify_matching(24, {'pairs':54, 'critical':{0:1,2:5}})
    verify_matching(32, {'pairs':170, 'critical':{0:1,2:1}})
    assert len(complex_at(40)) == 2**N-1
    verify_inclusion()
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
