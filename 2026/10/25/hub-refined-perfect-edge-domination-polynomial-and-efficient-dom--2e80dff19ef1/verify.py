"""Independent finite checks of the cycle-bouquet PED enumerator and DIM counts.

Run: python3 verify.py
Uses only the Python standard library. This is corroboration, not a proof of
statements covering unbounded cycle lengths or unbounded numbers of petals.
"""
from collections import Counter
from itertools import product
from math import comb


def f(n):
    assert n >= 0
    return Counter({n - 2*j: comb(n - 2*j + 1, j)
                    for j in range((n+1)//3+1)})


def mul(a, b):
    out = Counter()
    for i, x in a.items():
        for j, y in b.items():
            out[i+j] += x*y
    return +out


def shift(a, d, scalar=1):
    return Counter({i+d: scalar*v for i, v in a.items()})


def g(n):
    return Counter({1: 1}) if n == 1 else shift(f(n-2), 2)


def j(n):
    return Counter({0: 1}) if n == 1 else shift(f(n-2), 1)


def h(n):
    if n <= 2:
        return Counter()
    return Counter({1: 1}) if n == 3 else shift(f(n-4), 2)


def formula(lengths):
    n = [length-2 for length in lengths]
    res = Counter()
    a = Counter({0: 1})
    for v in n:
        a = mul(a, g(v))
    for d, c in a.items():
        res[(d, 0)] += c
    for i, v in enumerate(n):
        a = shift(j(v), 1, 2)
        for t, w in enumerate(n):
            if t != i:
                a = mul(a, h(w))
        for d, c in a.items():
            res[(d, 1)] += c
    a = Counter({0: 1})
    for v in n:
        a = mul(a, f(v))
    for d, c in a.items():
        res[(d + 2*len(n), 2*len(n))] += c
    return +res


def construct_edges(lengths):
    edges, spokes = [], []
    next_vertex = 1
    for length in lengths:
        vertices = [0] + list(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        for idx in range(length):
            a, b = vertices[idx], vertices[(idx+1) % length]
            edges.append((min(a,b),max(a,b)))
            spokes.append(a == 0 or b == 0)
    return edges, spokes


def enumerate_ped(lengths):
    edges, spokes = construct_edges(lengths)
    m = len(edges)
    neighbor_masks = []
    for i, (a,b) in enumerate(edges):
        mask = 0
        for j, (c,d) in enumerate(edges):
            if i != j and (a == c or a == d or b == c or b == d):
                mask |= 1<<j
        neighbor_masks.append(mask)
    spoke_mask = sum((1<<i) for i, sp in enumerate(spokes) if sp)
    ped = Counter()
    dim = 0
    for subset in range(1<<m):
        if all(((subset>>i)&1) or (subset & neighbor_masks[i]).bit_count() == 1
               for i in range(m)):
            key = (subset.bit_count(), (subset & spoke_mask).bit_count())
            ped[key] += 1
            if all((subset & neighbor_masks[i]) == 0
                   for i in range(m) if (subset>>i)&1):
                dim += 1
    return +ped, dim


def predicted_dim(lengths):
    all_zero = all(length % 3 == 0 for length in lengths)
    singleton = sum(lengths[i] % 3 == 0
                    and all(lengths[j] % 3 == 2 for j in range(len(lengths)) if j != i)
                    for i in range(len(lengths)))
    return int(all_zero)+2*singleton


def main():
    checks, total_ped, total_dim, max_edges = 0, 0, 0, 0
    for k in range(2, 5):
        for lengths in product(range(3, 8), repeat=k):
            if sum(lengths) > 15:
                continue
            observed, dims = enumerate_ped(lengths)
            expected = formula(lengths)
            assert observed == expected, ('PED', lengths, expected, observed)
            assert dims == predicted_dim(lengths), ('DIM', lengths, dims, predicted_dim(lengths))
            assert all(hub in (0,1,2*k) for _,hub in observed), ('hub', lengths)
            checks += 1
            total_ped += sum(observed.values())
            total_dim += dims
            max_edges = max(max_edges, sum(lengths))
    assert checks > 100
    print(f'VERIFY_OK graphs={checks} ped_sets={total_ped} dim_sets={total_dim} max_edges={max_edges}')
    for lengths in ((3,3), (3,4), (3,5), (4,4), (5,5,5), (3,5,6), (7,7)):
        print('EXAMPLE', lengths, sorted(formula(lengths).items()))


if __name__ == '__main__':
    main()
