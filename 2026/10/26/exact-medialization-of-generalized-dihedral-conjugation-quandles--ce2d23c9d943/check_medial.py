#!/usr/bin/env python3
"""Finite exhaustive medial-congruence computations for generalized-dihedral quandles."""
from itertools import product
from math import prod, gcd


def check(moduli):
    zero = tuple(0 for _ in moduli)
    A = list(product(*(range(m) for m in moduli)))
    def add(x, y):
        return tuple((a+b) % m for a, b, m in zip(x, y, moduli))
    def neg(x):
        return tuple((-a) % m for a, m in zip(x, moduli))
    def inverse(g):
        a, parity = g
        return (neg(a) if parity == 0 else a, parity)
    def multiply(g, h):
        a, p = g
        b, q = h
        return (add(a, neg(b) if p else b), p ^ q)
    group = [(a, p) for p in (0, 1) for a in A]
    size = len(group)
    idx = {g:i for i,g in enumerate(group)}
    def conjugate(g,h):
        return multiply(multiply(inverse(h),g),h)
    op = [[idx[conjugate(x,y)] for y in group] for x in group]
    inverse_op = [[None]*size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            assert inverse_op[op[x][y]][y] is None
            inverse_op[op[x][y]][y] = x
    assert all(z is not None for row in inverse_op for z in row)
    parent = list(range(size))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x,y):
        x,y=root(x),root(y)
        if x==y:return False
        parent[y]=x
        return True
    for a in range(size):
        for b in range(size):
            ab = op[a][b]
            for c in range(size):
                ac = op[a][c]
                for d in range(size):
                    union(op[ab][op[c][d]], op[ac][op[b][d]])
    while True:
        changed=False
        for a in range(size):
            for b in range(a):
                if root(a)!=root(b):continue
                for c in range(size):
                    changed |= union(op[a][c], op[b][c])
                    changed |= union(op[c][a], op[c][b])
                    changed |= union(inverse_op[a][c], inverse_op[b][c])
                    changed |= union(inverse_op[c][a], inverse_op[c][b])
        if not changed:break
    keys = []
    for a,p in group:
        if p == 0:
            keys.append((p,a))
        else:
            keys.append((p,tuple(x % gcd(m,4) for x,m in zip(a,moduli))))
    for a in range(size):
        for b in range(size):
            assert (root(a)==root(b)) == (keys[a]==keys[b]), (moduli,a,b)
    actual = len({root(i) for i in range(size)})
    expected = prod(moduli) + prod(gcd(m,4) for m in moduli)
    assert actual==expected
    return actual

if __name__=='__main__':
    tests = [(n,) for n in range(1,14)] + [
        (2,2), (2,3), (2,4), (2,5), (3,3), (3,4),
        (4,4), (2,2,2), (2,2,3), (2,3,3), (2,2,4),
    ]
    for moduli in tests:
        result=check(moduli)
        print(f'{moduli}: {result} classes')
    print(f'VERIFY_OK: {len(tests)} complete quotient computations')
