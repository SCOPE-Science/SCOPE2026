#!/usr/bin/env python3
"""Finite semantic checks for depth-synchronization in full neighborhood products.

No external packages; use `python3 verify.py`. The infinite statements rely on
proofs, not on these bounded tests.
"""
from itertools import product
from random import Random


def powerset_masks(n):
    return range(1 << n)


def all_cores(n):
    return product(powerset_masks(n), repeat=n)


def box_core(cores, subset):
    return sum((1 << x) for x, core in enumerate(cores) if core & ~subset == 0)


def cart_core(cores_a, cores_b, x, y):
    ny = len(cores_b)
    return sum((1 << (i * ny + j))
               for i in range(len(cores_a)) if (cores_a[x] >> i) & 1
               for j in range(ny) if (cores_b[y] >> j) & 1)


def product_box(cores_a, cores_b, subset):
    ny = len(cores_b)
    return sum((1 << (x * ny + y))
               for x in range(len(cores_a)) for y in range(ny)
               if cart_core(cores_a, cores_b, x, y) & ~subset == 0)


def union_cylinders(a, b, nx, ny):
    return sum((1 << (x * ny + y)) for x in range(nx) for y in range(ny)
               if ((a >> x) & 1) or ((b >> y) & 1))


def check_product(ca, cb, depth=7):
    nx, ny = len(ca), len(cb)
    a = b = p = 0
    for k in range(depth + 1):
        assert p == union_cylinders(a, b, nx, ny), ('sync', ca, cb, k)
        if k < depth:
            a = box_core(ca, a)
            b = box_core(cb, b)
            p = product_box(ca, cb, p)


def relation_box(R, subset, size):
    return sum((1 << x) for x in range(size) if all((subset >> y) & 1
               for u, y in R if u == x))


def transitive(R, size):
    return all((x, z) in R for x, y in R for w, z in R if y == w)


def depth_witness(n):
    # q = n, strict forward order on a length-n chain, plus a disjoint loop.
    q = n
    worlds = range(n + 1)
    chain = {(i, j) for i in range(n) for j in range(i + 1, n)}
    R1 = chain | {(q, q)}
    R2 = set(R1)
    R = chain | {(q, q), (0, q)}
    assert all(transitive(rel, n + 1) for rel in (R1, R2, R))
    assert {(x, z) for x, y in R1 for w, z in R2 if y == w} <= R
    assert {(x, z) for x, y in R2 for w, z in R1 if y == w} <= R
    cur1 = cur2 = cur = 0
    for k in range(n + 3):
        rhs = cur1 | cur2
        if k < n:
            assert cur == rhs, (n, k, 'earlier axiom fails')
        elif k == n:
            assert ((rhs >> 0) & 1) and not ((cur >> 0) & 1)
            assert ((cur ^ rhs) & (1 << 0)), (n, k, 'no root failure')
        cur1 = relation_box(R1, cur1, n + 1)
        cur2 = relation_box(R2, cur2, n + 1)
        cur = relation_box(R, cur, n + 1)
    return len(R), len(R1)


def main():
    tests = 0
    for nx, ny in ((1, 1), (1, 2), (2, 2), (3, 2)):
        for ca in all_cores(nx):
            for cb in all_cores(ny):
                check_product(ca, cb)
                tests += 1
    rng = Random(260631852)
    for _ in range(300):
        ca = tuple(rng.randrange(8) for _ in range(3))
        cb = tuple(rng.randrange(8) for _ in range(3))
        check_product(ca, cb)
        tests += 1
    witnesses = [depth_witness(n) for n in range(1, 17)]
    print(f'VERIFY_OK: {tests} finite filter-product pairs, ranks 0..7; '
          f'16 transitive counterframes, ranks 0..n+2; '
          f'last witness edges R/R1={witnesses[-1]}')


if __name__ == '__main__':
    main()
