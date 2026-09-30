#!/usr/bin/env python3
from itertools import combinations


def vertices(n):
    return tuple(range(1 << n))


def edges(n):
    out = []
    for u in vertices(n):
        for i in range(n):
            v = u ^ (1 << i)
            if u < v:
                out.append((u, v))
    return tuple(out)


def hamming(a, b):
    return (a ^ b).bit_count()


def edge_distance(s, edge):
    u, v = edge
    return min(hamming(s, u), hamming(s, v))


def is_vertex_cover(S, E):
    S = set(S)
    return all(u in S or v in S for u, v in E)


def edge_resolves(S, E):
    seen = set()
    for e in E:
        sig = tuple(edge_distance(s, e) for s in S)
        if sig in seen:
            return False
        seen.add(sig)
    return True


def exact_minimum(n):
    V = vertices(n)
    E = edges(n)
    for k in range(len(V) + 1):
        count = 0
        for S in combinations(V, k):
            if is_vertex_cover(S, E) and edge_resolves(S, E):
                count += 1
        if count:
            return k, count
    raise AssertionError('no dominant edge metric generator')


def parity_class(n, parity):
    return tuple(v for v in vertices(n) if v.bit_count() % 2 == parity)


expected = {1: (1, 2), 2: (3, 4), 3: (4, 2), 4: (8, 2)}
for n in range(1, 5):
    got = exact_minimum(n)
    assert got == expected[n], (n, got, expected[n])
    print(f'EXACT n={n} minimum={got[0]} basis_count={got[1]}')

for n in range(3, 11):
    E = edges(n)
    for parity in (0, 1):
        S = parity_class(n, parity)
        assert len(S) == 1 << (n - 1)
        assert is_vertex_cover(S, E)
        assert edge_resolves(S, E)
    print(f'PARITY_OK n={n} size={1 << (n - 1)}')

print('VERIFY_OK')
