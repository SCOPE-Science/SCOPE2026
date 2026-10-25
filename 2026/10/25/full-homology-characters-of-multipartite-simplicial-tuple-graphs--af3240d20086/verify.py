"""Exact character checks for color-partite simplicial r-tupling graphs.

Run with Python 3 standard library only. All computations use integers.
"""
from itertools import combinations, product
from math import prod, comb
from random import Random


def vertices_and_edges(sizes, r):
    q = len(sizes)
    vertices = []
    for I in combinations(range(q), r):
        vertices.extend(tuple(zip(I, v)) for v in product(*(range(sizes[i]) for i in I)))
    index = {v: i for i, v in enumerate(vertices)}
    colors = [set(i for i, _ in v) for v in vertices]
    edges = [(i, j) for i in range(len(vertices)) for j in range(i + 1, len(vertices))
             if colors[i].isdisjoint(colors[j])]
    return vertices, index, edges


def perm_cycles(pi):
    unseen = set(range(len(pi)))
    cycles = []
    while unseen:
        a = min(unseen)
        c = []
        j = a
        while j in unseen:
            unseen.remove(j)
            c.append(j)
            j = pi[j]
        assert j == a
        cycles.append(c)
    return cycles


def fixed_cycles(pi, maps):
    ans = []
    for c in perm_cycles(pi):
        count = 0
        for v in range(len(maps[c[0]])):
            w, i = v, c[0]
            for _ in c:
                w = maps[i][w]
                i = pi[i]
            assert i == c[0]
            count += (w == v)
        ans.append((tuple(c), count))
    return ans


def formula(sizes, r, pi, maps):
    cycles = fixed_cycles(pi, maps)
    polynomial = [1] + [0] * r
    for c, f in cycles:
        other = polynomial[:]
        for d in range(len(c), r + 1):
            other[d] += f * polynomial[d - len(c)]
        polynomial = other
    fixed_v = polynomial[r]
    fixed_positive_edges = 0
    fixed_negative_edges = 0
    for ell in range(len(sizes)):
        if pi[ell] != ell:
            continue
        remaining = [(c, f) for c, f in cycles if ell not in c]
        product_fixed = prod(f for c, f in remaining)
        partpoly = [1] + [0] * r
        for c, f in remaining:
            new = partpoly[:]
            for d in range(len(c), r + 1):
                new[d] += partpoly[d - len(c)]
            partpoly = new
        assert partpoly[r] % 2 == 0
        fixed_positive_edges += product_fixed * (partpoly[r] // 2)
        if all(len(c) % 2 == 0 for c, f in remaining):
            fixed_negative_edges += product_fixed * (2 ** (len(remaining) - 1))
    return 1 - fixed_v + fixed_positive_edges - fixed_negative_edges, (fixed_v, fixed_positive_edges, fixed_negative_edges)


def direct(sizes, r, pi, maps, graph):
    vertices, index, edges = graph
    action = []
    for v in vertices:
        image = tuple(sorted((pi[i], maps[i][a]) for i, a in v))
        action.append(index[image])
    assert len(set(action)) == len(action)
    fixed_v = sum(i == action[i] for i in range(len(vertices)))
    positive_edges = sum(action[i] == i and action[j] == j for i, j in edges)
    negative_edges = sum(action[i] == j and action[j] == i for i, j in edges)
    return 1 - fixed_v + positive_edges - negative_edges, (fixed_v, positive_edges, negative_edges)


def test_case(sizes, r, tests, seed):
    q = len(sizes)
    assert q == 2*r+1 and r >= 2 and all(a >= 1 for a in sizes)
    graph = vertices_and_edges(sizes, r)
    v, _, e = graph
    assert len(v) == sum(prod(sizes[i] for i in I) for I in combinations(range(q), r))
    edge_count = sum(comb(2*r,r)//2 * prod(sizes[i] for i in range(q) if i != ell) for ell in range(q))
    assert len(e) == edge_count
    rng = Random(seed)
    for it in range(tests):
        pi = list(range(q))
        for size in set(sizes):
            group = [i for i, a in enumerate(sizes) if a == size]
            shuffled = group[:]
            rng.shuffle(shuffled)
            for i, j in zip(group, shuffled):
                pi[i] = j
        maps = []
        for i, a in enumerate(sizes):
            values = list(range(a))
            rng.shuffle(values)
            maps.append(values)
        a = formula(sizes, r, pi, maps)
        b = direct(sizes, r, pi, maps, graph)
        assert a == b, (sizes, pi, maps, a, b)
    identity = list(range(q))
    trivial_maps = [list(range(a)) for a in sizes]
    ident = formula(sizes,r,identity,trivial_maps)
    assert ident[0] == len(e) - len(v) + 1
    print('PASS', f'r={r}',f'sizes={sizes}',f'vertices={len(v)}',f'edges={len(e)}',f'H1rank={ident[0]}',f'actions={tests}')


if __name__ == '__main__':
    test_case([2]*5,2,220,12)
    test_case([2,3,2,3,1],2,130,19)
    test_case([1]*5,2,80,20)
    test_case([2]*7,3,65,21)
    # A color permutation with two transpositions yields a negative character.
    sizes=[2]*5; pi=[1,0,3,2,4]; maps=[[0,1] for _ in sizes]
    value, components = formula(sizes,2,pi,maps)
    assert (value, components) == (-7,(4,4,8))
    assert direct(sizes,2,pi,maps,vertices_and_edges(sizes,2)) == (value,components)
    print('PASS: two-pair block permutation character',value,'and (fixed vertices, +edges, -edges)',components)
