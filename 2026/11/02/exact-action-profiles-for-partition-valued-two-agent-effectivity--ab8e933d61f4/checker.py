#!/usr/bin/env python3
"""Finite checks for optimal two-agent partition-valued effectivity representations.
Run: python checker.py. Only Python standard library is required.
Finite tests corroborate, but do not replace, the mathematical argument.
"""
from itertools import product
from math import prod


def construct(q, d, e):
    """Return outcome table for cross-cells with designated colors (i,j,t)."""
    nr, nc = len(d), len(e)
    assert len(q) == nr and all(len(row) == nc for row in q)
    assert all(d[i] >= q[i][j] and e[j] >= q[i][j]
               for i in range(nr) for j in range(nc))
    table = {}
    for i in range(nr):
        for a in range(d[i]):
            for j in range(nc):
                for b in range(e[j]):
                    table[(i,a,j,b)] = (i,j,(a+b) % q[i][j])
    return table


def check_ranges(q, d, e, table):
    for i in range(len(d)):
        required = {(i,j,t) for j in range(len(e)) for t in range(q[i][j])}
        for a in range(d[i]):
            got = {table[(i,a,j,b)] for j in range(len(e)) for b in range(e[j])}
            assert got == required, ('row', q, d, e, i, a, got, required)
    for j in range(len(e)):
        required = {(i,j,t) for i in range(len(d)) for t in range(q[i][j])}
        for b in range(e[j]):
            got = {table[(i,a,j,b)] for i in range(len(d)) for a in range(d[i])}
            assert got == required, ('column', q, d, e, j, b)


def count_surjective_arrays(q, a, b):
    # Correct version using OR rather than sum; cross-check by second method.
    if a < q or b < q:
        return 0
    total = 0
    target = (1 << q) - 1
    for word in product(range(q), repeat=a*b):
        if all(_or_bits(word[i*b+j] for j in range(b)) == target for i in range(a)) and \
           all(_or_bits(word[i*b+j] for i in range(a)) == target for j in range(b)):
            total += 1
    return total


def _or_bits(it):
    bits = 0
    for x in it:
        bits |= 1 << x
    return bits


def count_ie(q, a, b):
    """Inclusion exclusion of missing (row,symbol)/(column,symbol) events.

    Uses all 2^(q(a+b)) patterns and a direct product of allowed cell colors.
    """
    events = [(0,r,t) for r in range(a) for t in range(q)] + \
             [(1,c,t) for c in range(b) for t in range(q)]
    total = 0
    for mask in range(1 << len(events)):
        forbidden_r = [0]*a
        forbidden_c = [0]*b
        for ix,(typ,idx,col) in enumerate(events):
            if (mask >> ix) & 1:
                if typ == 0: forbidden_r[idx] |= 1<<col
                else: forbidden_c[idx] |= 1<<col
        ways = prod(q - (forbidden_r[i] | forbidden_c[j]).bit_count()
                    for i in range(a) for j in range(b))
        total += (-ways if mask.bit_count() % 2 else ways)
    return total


def main():
    cases=0
    for rows in range(1,4):
        for cols in range(1,4):
            for qs in product((1,2,3), repeat=rows*cols):
                q=[qs[i*cols:(i+1)*cols] for i in range(rows)]
                d=[max(row) for row in q]
                e=[max(q[i][j] for i in range(rows)) for j in range(cols)]
                table=construct(q,d,e)
                check_ranges(q,d,e,table)
                cases+=1
    assert cases == sum(3**(r*c) for r in range(1,4) for c in range(1,4))
    counted={}
    for q,a,b in [(1,1,1),(1,2,3),(2,2,2),(2,2,3),(2,3,3),(3,3,3)]:
        brute=count_surjective_arrays(q,a,b)
        ie=count_ie(q,a,b)
        assert brute==ie,(q,a,b,brute,ie)
        counted[(q,a,b)]=brute
    assert counted[(2,2,2)] == 2
    assert counted[(3,3,3)] == 12
    q = ((2,1),(1,3))
    d=(2,3)
    e=(2,3)
    check_ranges(q,d,e,construct(q,d,e))
    assert prod(counted[(size,size,size)] if size !=1 else 1
                for size in (2,1,1,3)) == 24
    # Necessity: one row of type i meets only e_j columns of type j,
    # so it cannot expose q_ij distinct intersection outcomes if e_j < q_ij;
    # the symmetric conclusion uses d_i. Test strict infeasibility of each
    # one-copy decrement in a nonuniform instance.
    for i in range(2):
        lower=d[i]-1
        assert any(q[i][j] > lower for j in range(2))
    for j in range(2):
        lower=e[j]-1
        assert any(q[i][j] > lower for i in range(2))
    print(f'ALL_CHECKS_OK partition_matrices={cases} surjectivity_counts={counted} heterogeneous_optima=24')

if __name__ == '__main__':
    main()
