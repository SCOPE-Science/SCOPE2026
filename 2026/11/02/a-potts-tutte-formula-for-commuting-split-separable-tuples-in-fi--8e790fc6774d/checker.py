#!/usr/bin/env python3
"""Independent small-case enumeration for split-polynomial commuting tuples in incidence algebras.

Uses only the Python standard library.  All tested examples use prime fields;
no assumptions about the closed counting formula enter the direct enumeration.
"""
from itertools import product
from collections import Counter


def closure(n, cover_edges):
    less = {(i, i) for i in range(n)} | set(cover_edges)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i, k) in less and (k, j) in less:
                    less.add((i, j))
    assert all(i <= j for i, j in less), 'numbering must be a linear extension'
    return sorted(less)


def mul(a, b, n, p):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n)) % p
                 for i in range(n) for j in range(n))


def sub_scalar(a, scalar, n, p):
    return tuple((a[i*n+j] - (scalar if i == j else 0)) % p
                 for i in range(n) for j in range(n))


def polynomial_zero(a, roots, n, p):
    ident = tuple(int(i == j) for i in range(n) for j in range(n))
    v = ident
    for r in roots:
        v = mul(v, sub_scalar(a, r, n, p), n, p)
    return not any(v)


def potts_count(n, edges, p, colors):
    return sum(p ** sum(labels[i] != labels[j] for i, j in edges)
               for labels in product(range(colors), repeat=n))


def brute_count(n, covers, p, roots, arity):
    basis = closure(n, covers)
    strict = [(i,j) for i,j in basis if i < j]
    legal = []
    for vals in product(range(p), repeat=len(basis)):
        a = [0] * (n*n)
        for (i,j),v in zip(basis,vals):
            a[i*n+j] = v
        a = tuple(a)
        if polynomial_zero(a, roots, n, p):
            legal.append(a)
    if arity == 1:
        direct = len(legal)
    elif arity == 2:
        direct = sum(mul(a,b,n,p) == mul(b,a,n,p) for a in legal for b in legal)
    else:
        raise ValueError('Only arities 1 and 2 are used by direct tests')
    expected = potts_count(n, strict, p, len(roots)**arity)
    if direct != expected:
        raise AssertionError((n,covers,p,roots,arity,direct,expected,len(legal)))
    return direct,len(legal),len(strict)


def main():
    cases = [
        ('chain2', 2, [(0,1)], [2,3,5], (0,1), [1,2]),
        ('chain3', 3, [(0,1),(1,2)], [2,3,5], (0,1), [1,2]),
        ('forkV', 3, [(0,1),(0,2)], [2,3,5], (0,1), [1,2]),
        ('forkLambda', 3, [(0,2),(1,2)], [2,3], (0,1), [1,2]),
        ('diamond4', 4, [(0,1),(0,2),(1,3),(2,3)], [2], (0,1), [1,2]),
        ('isolated3', 3, [], [2,3], (0,1), [1,2]),
        ('chain2_three_roots', 2, [(0,1)], [3], (0,1,2), [1,2]),
        ('forkV_three_roots', 3, [(0,1),(0,2)], [3], (0,1,2), [1,2]),
    ]
    count = 0
    maxsize = 0
    for name,n,covers,fields,roots,arities in cases:
        for p in fields:
            for m in arities:
                actual,legal,e = brute_count(n,covers,p,roots,m)
                count += 1
                maxsize = max(maxsize,actual)
                print(f'{name} p={p} roots={len(roots)} arity={m} legal={legal} comparable={e} count={actual}')
    print(f'INCIDENCE_SPLIT_TUPLE_POTTS_OK {count} {maxsize}')


if __name__ == '__main__':
    main()
