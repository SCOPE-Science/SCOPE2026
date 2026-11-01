#!/usr/bin/env python3
"""Standalone GF(2) edge-neighbor parity checker for line graphs of cubes.
Usage: python linecube_check_new.py
No external packages are used.
"""
from random import Random

def edges_of_cube(d):
    return [(u,u^(1<<i)) for u in range(1<<d) for i in range(d) if not ((u>>i)&1)]

def direct_update(d,es,x):
    output=0
    for i,(u,v) in enumerate(es):
        parity=0
        for j,(a,b) in enumerate(es):
            if i!=j and (u==a or u==b or v==a or v==b):
                parity ^= (x>>j)&1
        output |= parity<<i
    return output

def bit_rows(d,es):
    incident=[[] for _ in range(1<<d)]
    for j,(u,v) in enumerate(es):
        incident[u].append(j);incident[v].append(j)
    rows=[]
    for i,(u,v) in enumerate(es):
        row=0
        for j in incident[u]+incident[v]:
            if j!=i: row ^= 1<<j
        rows.append(row)
    return rows

def apply(rows,x):
    y=0
    for i,row in enumerate(rows):
        y |= ((row&x).bit_count()&1)<<i
    return y

def matrix_product(A,B):
    C=[]
    for a in A:
        result=0
        while a:
            k=(a&-a).bit_length()-1
            result ^=B[k]
            a&=a-1
        C.append(result)
    return C

def rank(rows):
    basis={}
    for row in rows:
        while row:
            pivot=row.bit_length()-1
            if pivot in basis: row^=basis[pivot]
            else: basis[pivot]=row;break
    return len(basis)

def check(d, rng):
    es=edges_of_cube(d);m=len(es);n=1<<d
    assert len(set(tuple(sorted(e)) for e in es))==m
    rows=bit_rows(d,es)
    square=matrix_product(rows,rows);cube=matrix_product(square,rows)
    assert not any(cube)
    r1=rank(rows);r2=rank(square)
    assert r1==n-2,(d,r1,n-2)
    assert r2==n//2-2,(d,r2,n//2-2)
    bs=(n//2-2,2,(d-3)*n//2+2)
    assert 3*bs[0]+2*bs[1]+bs[2]==m
    inputs=list(range(1<<m)) if m<=12 else [rng.getrandbits(m) for _ in range(900 if d==4 else 160 if d==5 else 40 if d==6 else 12)]
    first=[0,0,0,0]
    for x in inputs:
        a=apply(rows,x)
        assert a==direct_update(d,es,x)
        b=apply(rows,a)
        c=apply(rows,b)
        assert not c
        assert a==apply(rows,x)
        t=0 if x==0 else 1 if a==0 else 2 if b==0 else 3
        first[t]+=1
    if m<=12:
        e1=q1=2**(m-r1)
        e2=2**(m-r2)
        assert first==[1,e1-1,e2-e1,2**m-e2],(d,first)
    print('d=%d vertices=%d edges=%d rank_1=%d rank_2=%d rank_3=0 blocks_3,2,1=%s tested=%d layers=%s'%
          (d,n,m,r1,r2,bs,len(inputs),first))

if __name__=='__main__':
    rng=Random(271828)
    for d in range(2,8):check(d,rng)
    print('LINE_CUBE_XOR_JORDAN_ALL_CHECKS_PASSED')
