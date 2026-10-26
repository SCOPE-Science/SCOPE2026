#!/usr/bin/env python3
"""Exact norm-three generator census in the Hurwitz integer order.

Requires only the Python standard library. All tests use exact integers.
"""
from itertools import product
from collections import Counter


def candidates(n):
    bound = 2 * n
    return [u for u in product(range(-bound, bound + 1), repeat=4)
            if sum(t * t for t in u) == 4 * n
            and all(t % 2 == u[0] % 2 for t in u)]


def mul(u, v):
    a, b, c, d = u
    e, f, g, h = v
    # u and v represent twice the quaternion; result represents four times uv.
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)


def basis_coeffs(w, denominator):
    # w/denominator in the basis (1,i,j,(1+i+j+k)/2).
    a, b, c, d = w
    nums = (a-d, b-d, c-d, 2*d)
    assert all(t % denominator == 0 for t in nums)
    return tuple(t // denominator for t in nums)


def det3(a, b, c):
    return (a[0] * (b[1]*c[2] - b[2]*c[1])
            - a[1] * (b[0]*c[2] - b[2]*c[0])
            + a[2] * (b[0]*c[1] - b[1]*c[0]))


def index_via_lattice(u, v):
    a = basis_coeffs(u, 2)[1:]
    b = basis_coeffs(v, 2)[1:]
    c = basis_coeffs(mul(u, v), 4)[1:]
    # First column is the identity in the integral basis.
    return abs(det3(a, b, c))


def index_via_commutator(u, v):
    q = sum((u[i]*v[j] - u[j]*v[i])**2
            for i, j in ((1, 2), (1, 3), (2, 3)))
    assert q % 8 == 0
    return q // 8


def main():
    elements = candidates(3)
    assert len(elements) == 96
    assert len(candidates(1)) == 24  # the Hurwitz unit group
    assert Counter(abs(u[0]) for u in elements) == {3: 16, 2: 24, 1: 48, 0: 8}
    traces = Counter()
    partners = Counter()
    all_indices = Counter()
    for u in elements:
        for v in elements:
            det = index_via_lattice(u, v)
            assert det == index_via_commutator(u, v)
            all_indices[det] += 1
            if det == 1:
                traces[abs(u[0])] += 1
                partners[u] += 1
    assert sum(all_indices.values()) == 9216
    assert all_indices[1] == 960
    assert traces == {3: 576, 2: 192, 1: 192}
    expected = {3: 36, 2: 8, 1: 4, 0: 0}
    assert all(partners[u] == expected[abs(u[0])] for u in elements)
    # A pair generating the whole noncommutative algebra has central unit
    # stabilizer {+1,-1}. Every inner unit orbit therefore has size 24/2.
    assert all(traces[k] % 12 == 0 for k in traces)
    assert sum(traces.values()) // 12 == 80
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
