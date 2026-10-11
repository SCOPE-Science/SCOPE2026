"""Finite consistency checks for the three-cut character formula on girth-five graphs.

Requires Python 3.10+ standard library only. Generic proof for arbitrary orders is
contained in RESULT.md; these computations do not replace that proof.
"""
from itertools import combinations, permutations
from collections import defaultdict
from math import comb


def inversion_sign(a):
    return -1 if sum(a[i] > a[j] for i in range(len(a)) for j in range(i + 1, len(a))) % 2 else 1


def graph_cycle(n):
    return n, {frozenset((i, (i + 1) % n)) for i in range(n)}


def graph_path(n):
    return n, {frozenset((i, i + 1)) for i in range(n - 1)}


def graph_petersen():
    vs = list(combinations(range(5), 2))
    return 10, {frozenset((i, j)) for i in range(10) for j in range(i + 1, 10) if set(vs[i]).isdisjoint(vs[j])}


def graph_heawood():
    return 14, {frozenset((i, 7 + j)) for i in range(7) for j in range(7) if (i - j) % 7 in (0, 1, 3)}


def graph_two_cycles5():
    return 10, ({frozenset((i, (i + 1) % 5)) for i in range(5)} |
                {frozenset((5 + i, 5 + (i + 1) % 5)) for i in range(5)})


def graph_cycle5_isolated2():
    return 7, {frozenset((i, (i + 1) % 5)) for i in range(5)}


def graph_star():
    return 7, {frozenset((0, i)) for i in range(1, 7)}


def groups(name, n):
    if name == 'cycle7':
        return [tuple((a * x + b) % n for x in range(n)) for a in (1, -1) for b in range(n)]
    if name == 'path7':
        return [tuple(range(n)), tuple(n - 1 - x for x in range(n))]
    if name == 'petersen':
        pairs = list(combinations(range(5), 2))
        look = {x: i for i, x in enumerate(pairs)}
        return [tuple(look[tuple(sorted((p[x], p[y])))] for x, y in pairs) for p in permutations(range(5))]
    if name == 'heawood':
        result = []
        for b in range(7):
            result.append(tuple((i + b) % 7 for i in range(7)) + tuple(7 + (j + b) % 7 for j in range(7)))
            result.append(tuple(7 + (-i + b) % 7 for i in range(7)) + tuple((-j + b) % 7 for j in range(7)))
        return result
    if name == 'two_cycles5':
        actions = [tuple((a*x+b) % 5 for x in range(5)) for a in (1, -1) for b in range(5)]
        result = []
        for u in actions:
            for v in actions:
                for swap in (False, True):
                    if not swap:
                        result.append(tuple(u[i] for i in range(5)) + tuple(5+v[i] for i in range(5)))
                    else:
                        result.append(tuple(5+u[i] for i in range(5)) + tuple(v[i] for i in range(5)))
        return result
    if name == 'cycle5_isolated2':
        actions = [tuple((a*x+b) % 5 for x in range(5)) for a in (1, -1) for b in range(5)]
        return [tuple(p) + (i,j) for p in actions for (i,j) in [(5,6),(6,5)]]
    if name == 'star7':
        return [tuple([0] + [p[i] + 1 for i in range(6)]) for p in
                [tuple(range(6)), (1, 0, 2, 3, 4, 5), (1, 2, 3, 4, 5, 0), (1, 0, 3, 2, 5, 4)]]
    raise KeyError(name)


def signed_fix(g, face):
    a = tuple(sorted(face))
    mapped = tuple(g[x] for x in a)
    if set(mapped) != set(a):
        return 0
    return inversion_sign(mapped)


def rank_binary(columns):
    pivots = {}
    for v in columns:
        while v:
            p = v.bit_length() - 1
            if p not in pivots:
                pivots[p] = v
                break
            v ^= pivots[p]
    return len(pivots)


def examine(name, graph, check_ranks):
    n, edges = graph
    vertices = range(n)
    def edge(x, y):
        return frozenset((x, y)) in edges
    assert n >= 7
    assert all(sum(edge(a, b) for a, b in combinations(q, 2)) <= 2 for q in combinations(vertices, 3)), 'triangle'
    assert all(not (sum(edge(a,b) for a,b in combinations(q,2))>=4) for q in combinations(vertices,4)), '4-cycle'
    paths = []
    disconnected = []
    for t in combinations(vertices, 3):
        if sum(edge(a,b) for a,b in combinations(t,2)) == 2:
            paths.append(t)
        else:
            disconnected.append(t)
    assert len(paths) == sum(comb(sum(edge(v,w) for w in vertices if w != v), 2) for v in vertices)
    # A length-two path has a unique endpoint pair at distance two.
    pairs = []
    for t in paths:
        pair = [frozenset((a,b)) for a,b in combinations(t,2) if not edge(a,b)]
        assert len(pair) == 1
        pairs.append(pair[0])
    assert len(pairs) == len(set(pairs))
    beta = comb(n-1, 2) - len(paths)
    assert beta >= 0
    # Construct the ordinary cut complex from disconnected triples, independently.
    full = (1 << n) - 1
    face_set = {0}
    for t in disconnected:
        facet = full ^ sum(1 << x for x in t)
        sub = facet
        while True:
            face_set.add(sub)
            if sub == 0:
                break
            sub = (sub - 1) & facet
    d = n - 4
    assert max(m.bit_count() for m in face_set) == d + 1
    assert all(m in face_set for m in range(1 << n) if m.bit_count() <= d)
    assert sum(((-1)**(m.bit_count()-1)) for m in face_set if m) - 1 == (-1)**d * beta

    GG = groups(name, n)
    assert len(set(GG)) == len(GG)
    trace_data = []
    masks_by_size = defaultdict(list)
    for m in face_set:
        if m:
            masks_by_size[m.bit_count()].append(m)
    for g in GG:
        assert set(g) == set(vertices)
        assert {frozenset((g[a],g[b])) for a,b in (tuple(e) for e in edges)} == edges
        f = sum(g[v] == v for v in vertices)
        f2 = sum(g[g[v]] == v for v in vertices)
        edge_trace = (f*f - f2) // 2
        path_trace = sum(signed_fix(g,p) for p in paths)
        pred = inversion_sign(g) * (edge_trace - f + 1 - path_trace)
        delta_trace = -1
        for size, masks in masks_by_size.items():
            sign_degree = (-1) ** (size - 1)
            for m in masks:
                verts = tuple(i for i in vertices if m & (1 << i))
                delta_trace += sign_degree * signed_fix(g, verts)
        actual = delta_trace * ((-1) ** d)
        assert actual == pred, (name,g,pred,actual)
        trace_data.append((pred, f, f2, path_trace, inversion_sign(g)))
    assert trace_data[0][0] == beta, (name,trace_data[0][0],beta)

    if check_ranks:
        all_dim = [sorted(m for m in face_set if m.bit_count() == k) for k in range(1,d+2)]
        ranks = [0]
        for k in range(2,d+2):
            rows = {m:i for i,m in enumerate(all_dim[k-2])}
            columns = []
            for cell in all_dim[k-1]:
                v = 0
                for idx in range(n):
                    if cell >> idx & 1:
                        sub = cell ^ (1 << idx)
                        v ^= 1 << rows[sub]
                columns.append(v)
            ranks.append(rank_binary(columns))
        ranks.append(0)
        bettis = [len(all_dim[k]) - ranks[k] - ranks[k+1] for k in range(d+1)]
        assert bettis == [1] + [0]*(d-1) + [beta], (name, bettis)
    print(name, 'n=', n, 'm=', len(edges), 'length2paths=',len(paths),
          'facets=',len(disconnected), 'faces=',len(face_set)-1, 'beta=',beta,
          'automorphisms_checked=',len(GG), 'distinct_character_values=',sorted({x[0] for x in trace_data}),
          'ranks_checked=',check_ranks)


def main():
    examine('cycle7', graph_cycle(7), True)
    examine('path7', graph_path(7), True)
    examine('petersen', graph_petersen(), True)
    examine('heawood', graph_heawood(), False)
    examine('star7', graph_star(), True)
    examine('two_cycles5', graph_two_cycles5(), True)
    examine('cycle5_isolated2', graph_cycle5_isolated2(), True)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
