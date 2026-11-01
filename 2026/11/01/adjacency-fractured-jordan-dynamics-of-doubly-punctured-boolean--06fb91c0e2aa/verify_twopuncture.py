#!/usr/bin/env python3
"""Independent finite characteristic-two matrix and state checks for doubly punctured cubes."""
from collections import Counter


def rank_gf2(rows):
    pivots = {}
    for row in rows:
        while row:
            k = row.bit_length()-1
            if k in pivots:
                row ^= pivots[k]
            else:
                pivots[k] = row
                break
    return len(pivots)


def matmul_gf2(a, b):
    out=[]
    for row in a:
        val=0
        while row:
            bit = row & -row
            val ^= b[bit.bit_length()-1]
            row ^= bit
        out.append(val)
    return out


def matrix(d, h):
    assert 2 <= d and 1 <= h <= d
    deleted={0, (1<<h)-1}
    vertices=[v for v in range(1<<d) if v not in deleted]
    pos={v:i for i,v in enumerate(vertices)}
    n=len(vertices)
    rows=[]
    for v in vertices:
        row=0
        for t in range(d):
            w=v ^ (1<<t)
            if w in pos:
                row |= 1 << pos[w]
        rows.append(row)
    return rows,vertices


def eig_jordan(blocks, eigenvalue):
    return [(size, mult) for (val,size,mult) in blocks if val==eigenvalue]


def expected(d,h):
    N=1<<d
    if d==2 and h==2: return [(0,1,2)]
    if d%2==0:
        if h==1: return [(0,2,N//2-2),(1,2,1)]
        return [(0,3,2),(0,2,N//2-4)]
    if h==1: return [(1,4,1),(1,2,N//2-3)]
    return [(0,1,2),(1,2,N//2-2)]


def expected_kernel(blocks,eigen,t):
    return sum(mult*min(size,t) for val,size,mult in blocks if val==eigen)


def rank_profile(d,h):
    B,_=matrix(d,h);n=len(B)
    blocks=expected(d,h)
    assert sum(size*mult for _,size,mult in blocks)==n
    for eigen in (0,1):
        Q=[row ^ (1<<i if eigen else 0) for i,row in enumerate(B)]
        power=[1<<i for i in range(n)]
        for t in range(1,6):
            power=matmul_gf2(power,Q)
            nullity=n-rank_gf2(power)
            expected_nullity=expected_kernel(blocks,eigen,t)
            assert nullity==expected_nullity, (d,h,eigen,t,nullity,expected_nullity)
    return n


def prediction(d,h,q=2):
    N=1<<d
    if d==2 and h==2:
        return {(0,1):1,(1,1):q*q-1}
    if d%2==0 and h>1:
        return {(0,1):1,(1,1):q**(N//2-2)-1,
                (2,1):q**(N-4)-q**(N//2-2),
                (3,1):q**(N-2)-q**(N-4)}
    if d%2==0 and h==1:
        m=N//2-2
        return {(0,1):q,(0,2):q*q-q,
                (1,1):q*(q**m-1),
                (1,2):(q*q-q)*(q**m-1),
                (2,1):q*(q**(2*m)-q**m),
                (2,2):(q*q-q)*(q**(2*m)-q**m)}
    if d%2==1 and h==1:
        fixed=q**(N//2-2);two=q**(N-4)-fixed
        return {(0,1):fixed,(0,2):two,(0,4):q**(N-2)-q**(N-4)}
    if d%2==1 and h>1:
        fixed=q**(N//2-2);two=q**(N-4)-fixed
        return {(0,1):fixed,(0,2):two,(1,1):(q*q-1)*fixed,
                (1,2):(q*q-1)*two}
    raise AssertionError


def iter_state(rows,mask):
    out=0
    for i,row in enumerate(rows):
        if ((row & mask).bit_count()&1):out|=1<<i
    return out


def orbit_of(mask,rows):
    hist={};v=mask
    while v not in hist:
        hist[v]=len(hist)
        v=iter_state(rows,v)
    return hist[v],len(hist)-hist[v]


def exhaustive(d,h):
    B,_=matrix(d,h);n=len(B)
    counts=Counter()
    for s in range(1<<n):
        counts[orbit_of(s,B)]+=1
    pred={k:v for k,v in prediction(d,h).items() if v}
    assert dict(counts)==pred, (d,h,dict(counts),pred)
    return 1<<n

if __name__=='__main__':
    matrices=0;vertices=0
    for d in range(2,9):
        for h in range(1,d+1):
            rank_profile(d,h)
            matrices+=1;vertices+=(1<<d)-2
    micro=0
    for d in range(2,5):
        for h in range(1,d+1):
            micro+=exhaustive(d,h)
    for d in range(2,9):
        N=1<<d
        for h in range(1,d+1):
            b=expected(d,h)
            assert sum(size*mul for _,size,mul in b)==N-2
    print('TWO_PUNCTURE_JORDAN_ALL_CHECKS_PASSED')
    print('dimension_distance_pairs',matrices)
    print('matrix_total_vertices_checked',vertices)
    print('exhaustive_initial_states',micro)
    print('tested_dimensions',list(range(2,9)))
