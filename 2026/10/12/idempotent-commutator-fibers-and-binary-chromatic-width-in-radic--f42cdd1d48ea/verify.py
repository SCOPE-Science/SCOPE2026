"""Exact small-field verification of idempotent-commutator fibers.

The symbolic proof handles arbitrary finite loopless multiquivers and fields;
these exhaustive checks independently test the multiplication and state-sum.
"""
from itertools import product
from collections import Counter


def add(a, b, q):
    if q == 4:
        return a ^ b
    return (a + b) % q


def neg(a, q):
    return a if q == 4 else (-a) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    result = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                result ^= (1 << (i + j))
    if result & 8:
        result ^= 0b1110  # x^3=x^2+x
    if result & 4:
        result ^= 0b111  # x^2=x+1
    return result


def product_in_algebra(a, b, nv, edges, q):
    result = [mul(a[i], b[i], q) for i in range(nv)]
    for j, (u, v) in enumerate(edges):
        result.append(add(mul(a[u], b[nv+j], q), mul(a[nv+j], b[v], q), q))
    return tuple(result)


def comm(a, b, nv, edges, q):
    xy = product_in_algebra(a, b, nv, edges, q)
    yx = product_in_algebra(b, a, nv, edges, q)
    return tuple(add(x, neg(y, q), q) for x, y in zip(xy, yx))


def formula(z, nv, edges, q):
    total = 0
    for labels in product(range(4), repeat=nv):
        good = True
        differing = 0
        for j, (u, v) in enumerate(edges):
            delta = labels[u] ^ labels[v]
            if z[j] != 0 and delta != 3:
                good = False
                break
            differing += (delta != 0)
        if good:
            total += q**differing
    return total


def chromatic(edges, nv):
    es = set(tuple(sorted(edge)) for edge in edges)
    for colors in range(1, nv + 1):
        if any(all(z[u] != z[v] for u, v in es) for z in product(range(colors), repeat=nv)):
            return colors
    raise AssertionError


def verify_case(q, nv, edges):
    nm = len(edges)
    all_el = product(range(q), repeat=nv+nm)
    idem = []
    for a in all_el:
        if product_in_algebra(a, a, nv, edges, q) == a:
            idem.append(a)
    measured = Counter(comm(a, b, nv, edges, q) for a in idem for b in idem)
    assert all(x[:nv] == (0,) * nv for x in measured)
    for z in product(range(q), repeat=nm):
        expected = formula(z, nv, edges, q)
        assert measured[((0,) * nv) + z] == expected, (q, nv, edges, z, measured[((0,) * nv)+z], expected)
        support = [edges[j] for j in range(nm) if z[j]]
        chi = chromatic(support, nv)
        assert (expected > 0) == (chi <= 2)
    assert sum(measured.values()) == len(idem)**2
    print('PASS', 'q', q, 'vertices', nv, 'edges', edges, 'idempotents', len(idem), 'tested_targets', q**nm)


def verify_sum_width_binary():
    q, nv = 2, 3
    edges = [(0,1), (1,2), (0,2)]
    idem = [a for a in product(range(2), repeat=6) if product_in_algebra(a,a,nv,edges,q)==a]
    outputs = set(comm(a,b,nv,edges,q)[nv:] for a in idem for b in idem)
    assert (1,1,1) not in outputs
    double = set(tuple(add(x,y,q) for x,y in zip(a,b)) for a in outputs for b in outputs)
    assert len(double)==8
    print('PASS binary triangle width: 1+1+1 needs exactly two idempotent commutators')


if __name__ == '__main__':
    samples = [
        (2, 2, [(0,1)]),
        (3, 2, [(0,1)]),
        (4, 2, [(0,1)]),
        (3, 2, [(0,1),(0,1)]),
        (4, 2, [(0,1),(1,0)]),
        (2, 3, [(0,1),(1,2),(0,2)]),
        (3, 3, [(0,1),(1,2),(0,2)]),
        (4, 3, [(0,1),(1,2),(0,2)]),
        (2, 4, [(0,1),(1,2),(2,3)]),
        (2, 3, []),
    ]
    for sample in samples:
        verify_case(*sample)
    verify_sum_width_binary()
    print('VERIFY_OK')
