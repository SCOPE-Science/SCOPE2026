#!/usr/bin/env python3
"""Finite exact checks of the Stirling-complex automorphism character.

Enumerates every admissible product cube for listed small trees and verifies the
fixed-cell traces, Euler characteristic, and rational-character implications.
Only finite test cases are checked; the accompanying proof treats all trees.
"""
import itertools
import math
from collections import Counter


def sphere_count(m, n):
    return sum((-1) ** (m+a+1) * math.comb(m, a+1) * a**n
               for a in range(1, m))


def all_cells(m, edges, n):
    alphabet = tuple((0, i) for i in range(m)) + tuple((1, *sorted(e)) for e in edges)
    groups = [set() for _ in range(n-m+1)]
    for cube in itertools.product(alphabet, repeat=n):
        if {x[1] for x in cube if x[0] == 0} == set(range(m)):
            k = sum(x[0] for x in cube)
            groups[k].add(cube)
    return groups


def act(cube, perm):
    return tuple((0,perm[x[1]]) if x[0]==0
                 else (1, *sorted((perm[x[1]], perm[x[2]]))) for x in cube)


def rank_mod2(columns):
    pivots = {}
    for x in columns:
        while x:
            lead = x.bit_length()-1
            if lead in pivots: x ^= pivots[lead]
            else:
                pivots[lead] = x
                break
    return len(pivots)


def boundary_columns(high, low):
    lookup = {s: i for i,s in enumerate(low)}
    cols=[]
    for cube in high:
        val = 0
        for j,x in enumerate(cube):
            if x[0]==1:
                for v in x[1:]:
                    face=list(cube)
                    face[j]=(0,v)
                    val ^= (1<<lookup[tuple(face)])
        cols.append(val)
    return cols


def inspect_case(tag, m, edges, n, permutations, check_boundary=False):
    cells=all_cells(m,edges,n)
    counts=tuple(len(x) for x in cells)
    d=n-m
    f=sphere_count(m,n)
    chi=sum((-1)**i*c for i,c in enumerate(counts))
    assert chi == 1 + (-1)**d * f, (tag,chi, f)
    for p in permutations:
        assert tuple(sorted(p)) == tuple(range(m))
        assert {tuple(sorted((p[u],p[v]))) for u,v in edges} == {tuple(sorted(e)) for e in edges}
        fixed=sum((-1)**i * sum(act(c,p)==c for c in cells[i]) for i in range(d+1))
        expected=chi if all(p[i]==i for i in range(m)) else 0
        assert fixed==expected, (tag,p,fixed,expected)
        if expected==0:
            assert (-1)**d*(fixed-1)==(-1)**(d+1)
    if check_boundary:
        ranks=[rank_mod2(boundary_columns(list(cells[i]),list(cells[i-1]))) for i in range(1,d+1)]
        betti=[]
        for i,c in enumerate(counts):
            outgoing=ranks[i-1] if i else 0
            incoming=ranks[i] if i<d else 0
            betti.append(c-outgoing-incoming)
        assert betti == ([1]+[0]*(d-1)+[f] if d>0 else [f+1]), (tag,betti,f)
        print(tag, 'faces=',counts,'mod2_boundaries=',ranks,'betti=',betti,'sphere_count=',f)
    else:
        print(tag, 'faces=',counts,'Euler=',chi,'sphere_count=',f,'fixed-cell-traces=OK')


def p3():
    # P3: swap two endpoints; P4: reverse path; K1,3: S3 leaf permutations.
    inspect_case('path3_n3', 3, [(0,1),(0,2)], 3, [tuple(range(3)),(0,2,1)],True)
    inspect_case('path3_n4', 3, [(0,1),(0,2)], 4, [tuple(range(3)),(0,2,1)],True)
    inspect_case('path3_n5', 3, [(0,1),(0,2)], 5, [tuple(range(3)),(0,2,1)],True)
    perms=[(0,)+q for q in itertools.permutations((1,2,3))]
    inspect_case('star3_n4',4,[(0,1),(0,2),(0,3)],4,perms,True)
    inspect_case('star3_n5',4,[(0,1),(0,2),(0,3)],5,perms,True)
    inspect_case('path4_n5',4,[(0,1),(1,2),(2,3)],5,[(0,1,2,3),(3,2,1,0)],True)
    for r in range(2,7):
        m=r+1
        for n in range(m,m+6):
            f=sphere_count(m,n)
            eps=(-1)**(n-m+1)
            q,rem=divmod(f-eps,math.factorial(r))
            assert rem == 0 and q+eps>=0
    print('STIRLING_TREE_AUTOMORPHISM_CERTIFICATE_OK')

if __name__=='__main__':
    p3()
