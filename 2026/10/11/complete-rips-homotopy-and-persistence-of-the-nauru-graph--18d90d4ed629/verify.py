#!/usr/bin/env python3
"""Reproduce a finite graph-metric homotopy calculation using Python standard library."""
import collections
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
N = 12
V = tuple(range(2 * N))
A = frozenset([1, 3, 5, 7, 9, 11, 12, 14, 16, 18, 20, 22])
B = frozenset(V) - A


def graph():
    adj = {v: set() for v in V}
    for i in range(N):
        for u, v in ((i, (i + 1) % N), (i, i + N),
                     (i + N, N + (i + 5) % N)):
            adj[u].add(v)
            adj[v].add(u)
    return adj


def distances(adj):
    ds = {}
    for source in V:
        d = {source: 0}
        q = collections.deque([source])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in d:
                    d[w] = d[u] + 1
                    q.append(w)
        assert len(d) == len(V)
        ds[source] = d
    return ds


def faces(dist, radius, vertices=V, upper_size=5):
    result = set()
    for size in range(1, upper_size + 1):
        for t in itertools.combinations(sorted(vertices), size):
            if all(dist[u][v] <= radius for u, v in itertools.combinations(t, 2)):
                result.add(t)
    return result


def boundary(t):
    return {t[:i] + t[i + 1:]: 1 if i % 2 == 0 else -1
            for i in range(len(t))}


def closed_orientable_torus(cplx):
    vs = sorted(x[0] for x in cplx if len(x) == 1)
    edges = sorted(x for x in cplx if len(x) == 2)
    triangles = sorted(x for x in cplx if len(x) == 3)
    assert len(vs) == 12 and len(edges) == 36 and len(triangles) == 24
    assert all(len(x) <= 3 for x in cplx)
    incidences = collections.defaultdict(list)
    for j, triangle in enumerate(triangles):
        for e, sign in boundary(triangle).items():
            incidences[e].append((j, sign))
    assert all(len(incidences[e]) == 2 for e in edges)
    adjacency = {v: set() for v in vs}
    for u, w in edges:
        adjacency[u].add(w)
        adjacency[w].add(u)
    reached = {vs[0]}
    frontier = [vs[0]]
    while frontier:
        u = frontier.pop()
        for x in adjacency[u]:
            if x not in reached:
                reached.add(x)
                frontier.append(x)
    assert reached == set(vs)
    for v in vs:
        lv = {u: set() for u in adjacency[v]}
        for t in triangles:
            if v in t:
                u, w = (x for x in t if x != v)
                lv[u].add(w)
                lv[w].add(u)
        assert len(lv) == 6 and all(len(q) == 2 for q in lv.values())
        link_seen = {next(iter(lv))}
        qq = list(link_seen)
        while qq:
            z = qq.pop()
            for w in lv[z] - link_seen:
                link_seen.add(w)
                qq.append(w)
        assert len(link_seen) == 6
    signs = {0: 1}
    stack = [0]
    while stack:
        j = stack.pop()
        for e, q in boundary(triangles[j]).items():
            for other, p in incidences[e]:
                if other == j:
                    continue
                wanted = -signs[j] * q * p
                if other not in signs:
                    signs[other] = wanted
                    stack.append(other)
                else:
                    assert signs[other] == wanted
    assert len(signs) == len(triangles)
    assert len(vs) - len(edges) + len(triangles) == 0
    # Connected closed orientable surface with Euler characteristic zero is a torus.
    return True


def add_chain(chain, face, coefficient):
    value = chain.get(face, 0) + coefficient
    if value:
        chain[face] = value
    elif face in chain:
        del chain[face]


def projected_boundaries(steps):
    output = []
    for i, step in enumerate(steps):
        if step['type'] != 'critical':
            continue
        c = boundary(tuple(step['face']))
        for st in steps[i + 1:]:
            if st['type'] != 'pair':
                continue
            f = tuple(st['free_face'])
            t = tuple(st['coface'])
            if len(f) == 2 and len(t) == 3 and f in c:
                z = c.pop(f)
                bt = boundary(t)
                assert bt[f] in (-1, 1)
                for e, s in bt.items():
                    if e != f:
                        add_chain(c, e, -z * s * bt[f])
            if len(f) == 1 and len(t) == 2:
                assert t not in c
        assert all(len(e) == 2 and set(e) <= A for e in c)
        output.append(c)
    return output


def check_certificate(K, Ka):
    cert = json.loads((ROOT / 'collapse_certificate.json').read_text(encoding='utf-8'))
    active = set(K)
    pairs = []
    critical = []
    for st in cert['steps']:
        if st['type'] == 'critical':
            q = tuple(st['face'])
            assert q in active and q not in Ka and len(q) == 3
            assert not any(len(t) > len(q) and set(q).issubset(t) for t in active)
            active.remove(q)
            critical.append(q)
        else:
            assert st['type'] == 'pair'
            f = tuple(st['free_face'])
            t = tuple(st['coface'])
            assert f in active and t in active and f not in Ka
            assert len(f) + 1 == len(t) and set(f).issubset(t)
            assert not any(len(s) > len(t) and set(t).issubset(s) for s in active)
            assert sum(len(s) == len(t) and set(f).issubset(s) for s in active) == 1
            active.remove(f)
            active.remove(t)
            pairs.append((f, t))
    assert active == Ka
    assert len(pairs) == 96 and len(critical) == 12
    assert collections.Counter((len(f), len(t)) for f, t in pairs) == {(1, 2): 12, (2, 3): 60, (3, 4): 24}
    assert all(len(t) == 3 for t in critical)
    assert cert['critical_2faces'] == [list(t) for t in critical]
    assert cert['pairs'] == [{'free_face':list(f),'coface':list(t)} for f,t in pairs]
    ba = sorted(t for t in Ka if len(t) == 3)
    assert cert['A_triangles'] == [list(t) for t in ba]
    out = projected_boundaries(cert['steps'])
    assert len(cert['bounding_2chains']) == len(out)
    for target, coeffs in zip(out, cert['bounding_2chains']):
        assert len(coeffs) == 24 and all(isinstance(x, int) for x in coeffs)
        result = {}
        for z, triangle in zip(coeffs, ba):
            for e, sign in boundary(triangle).items():
                add_chain(result, e, z * sign)
        assert result == target, (result, target)
    # The 12 extra two-cell attaching loops are nullhomologous in the torus.
    # Since the fundamental group of a torus is abelian, they are nullhomotopic.
    return len(pairs), len(critical)


def betti_mod2(cplx):
    layers = [sorted(x for x in cplx if len(x) == j)
              for j in range(1, max(len(x) for x in cplx) + 1)]
    ranks = [0]
    for j in range(1, len(layers)):
        indices = {f: i for i, f in enumerate(layers[j - 1])}
        pivots = {}
        for face in layers[j]:
            col = 0
            for e in boundary(face):
                col ^= (1 << indices[e])
            while col:
                ix = col.bit_length() - 1
                if ix in pivots:
                    col ^= pivots[ix]
                else:
                    pivots[ix] = col
                    break
        ranks.append(len(pivots))
    betti = [len(layers[j]) - ranks[j] - (ranks[j + 1] if j + 1 < len(ranks) else 0)
             for j in range(len(layers))]
    return [len(layer) for layer in layers], betti


def main():
    adj = graph()
    assert all(len(adj[v]) == 3 for v in V)
    assert all(adj[v] <= (B if v in A else A) for v in V)
    d = distances(adj)
    assert max(max(q.values()) for q in d.values()) == 4
    assert collections.Counter(d[0].values()) == {0: 1, 1: 3, 2: 6, 3: 9, 4: 5}
    K = faces(d, 2, upper_size=5)
    Ka = {f for f in K if set(f) <= A}
    Kb = {f for f in K if set(f) <= B}
    assert collections.Counter(len(f) - 1 for f in K) == {0:24, 1:108, 2:120, 3:24}
    assert not any(len(f) == 5 for f in K)
    assert closed_orientable_torus(Ka)
    assert closed_orientable_torus(Kb)
    pairs,critical = check_certificate(K,Ka)
    assert [betti_mod2(Ka), betti_mod2(Kb)] == [([12,36,24],[1,2,1])]*2
    assert betti_mod2(K) == ([24,108,120,24],[1,2,13,0])
    # Every cross-part pair has odd distance and the graph has diameter 4.
    assert all(d[u][v] in (1,3) for u in A for v in B)
    assert all(d[u][v] in (2,4) for part in (A,B)
               for u,v in itertools.combinations(sorted(part),2))
    # The scale-three Rips complex is exactly the join of the two torus triangulations.
    K3 = {tuple(sorted(x+y)) for x in [()] + sorted(Ka)
          for y in [()] + sorted(Kb) if x or y}
    assert len(K3) == 5328
    assert all(all(d[u][v] <= 3 for u,v in itertools.combinations(f,2)) for f in K3)
    # Conversely, every scale-three clique is the union of cliques within the parts.
    # Within a part the scale-three edges coincide with its scale-two edges.
    assert all((d[u][v] <= 3) == (d[u][v] <= 2)
               for part in (A,B) for u,v in itertools.combinations(sorted(part),2))
    assert betti_mod2(K3) == ([24,216,912,1872,1728,576],[1,0,0,4,4,1])
    # At radius one the original 36-edge graph has cycle rank 36-24+1 = 13.
    assert len({(u,v) for u in V for v in adj[u] if u<v}) == 36
    print(f'VERIFY_OK vertices=24 radius2_faces=276 relative_pairs={pairs} critical_2cells={critical} radius3_faces=5328')

if __name__ == '__main__':
    main()
