#!/usr/bin/env python3
"""Reproduce finite checks for join preservation versus the Boolean symmetric-difference law.

Boolean algebras P({0,...,n-1}) are represented by bit masks 0,...,2**n-1.
This is a finite sanity check; the proof for arbitrary Boolean algebras is symbolic.
"""
from itertools import product


def star(f):
    s = len(f)
    return all((f[x] ^ f[y]) & ~f[z] == 0
               for x in range(s) for y in range(s) for z in range(s)
               if ((x ^ y) & ~z) == 0)


def joins(f):
    s = len(f)
    return all(f[x | y] == (f[x] | f[y])
               for x in range(s) for y in range(s))


def monotone_boolean_functions(n):
    s = 1 << n
    return [tuple((truth >> x) & 1 for x in range(s))
            for truth in range(1 << s)
            if all(((x & y) != x) or ((truth >> x) & 1) <= ((truth >> y) & 1)
                   for x in range(s) for y in range(s))]


def check_small():
    for n in (1, 2):
        s = 1 << n
        count = 0
        for f in product(range(s), repeat=s):
            a, b = star(f), joins(f)
            assert a == b, (n, f, a, b)
            count += a
        assert count == (s + 1) ** n
        print('B_%d all %d functions: %d satisfy both' % (n, s ** s, count))

    # On B_3, star implies monotonicity by the general proof.
    # Every monotone map is specified by three monotone Boolean outputs.
    n = 3
    s = 1 << n
    components = monotone_boolean_functions(n)
    assert len(components) == 20
    count = 0
    for components_triple in product(components, repeat=n):
        f = tuple(sum(components_triple[j][x] << j for j in range(n))
                  for x in range(s))
        a, b = star(f), joins(f)
        assert a == b
        count += a
    assert count == (s + 1) ** n == 729
    print('B_3 all %d monotone functions: %d satisfy both' %
          (len(components) ** n, count))

    # Test exactly the operation printed in Example 2.2 of arXiv:2603.17724v1.
    # Atom masks 1,2,4 represent the singleton sets {1},{2},{3}.
    f = tuple(7 if x == 5 else x for x in range(8))
    x, y, z = 5, 1, 4
    assert x ^ y == z
    assert f[x] ^ f[y] == 6
    assert f[z] == 4
    assert (6 & ~4) != 0  # Published operation violates the law.
    assert not star(f) and not joins(f)
    print('printed example: x={1,3}, y={1}, z={3}; output symmetric difference {2,3} is not <= {3}')
    print('VERIFY_OK')


if __name__ == '__main__':
    check_small()
