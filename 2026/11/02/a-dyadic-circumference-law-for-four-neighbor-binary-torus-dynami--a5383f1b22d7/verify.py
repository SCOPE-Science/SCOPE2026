#!/usr/bin/env python3
"""Exact finite GF(2) tests for four-neighbor torus evolution; stdlib only."""
from collections import Counter


def rank2(rows):
    pivots = {}
    for w in rows:
        while w:
            i = w.bit_length() - 1
            if i not in pivots:
                pivots[i] = w
                break
            w ^= pivots[i]
    return len(pivots)


def times(A, B):
    out = []
    for w in A:
        r = 0
        while w:
            lb = w & -w
            r ^= B[lb.bit_length()-1]
            w -= lb
        out.append(r)
    return out


def adjacency(m,n):
    rows = []
    for i in range(m):
        for j in range(n):
            s = 0
            for u,v in (((i-1)%m,j),((i+1)%m,j),(i,(j-1)%n),(i,(j+1)%n)):
                s ^= 1 << (u*n+v)
            rows.append(s)
    return rows


def step(x,A):
    y=0
    while x:
        lb=x&-x
        y ^= A[lb.bit_length()-1]
        x-=lb
    return y


def first_periodic_time(x,A):
    visited={}
    t=0
    while x not in visited:
        visited[x]=t
        x=step(x,A)
        t+=1
    return visited[x]


def predicted(m,n):
    d = n&-n
    ell = max(m,d)//2
    c = 2*min(m,d)
    periodic_dim = m*(n-d)
    counts = [1<<periodic_dim]
    for t in range(1,ell+1):
        counts.append((1<< (periodic_dim+c*(t-1)))*((1<<c)-1))
    assert sum(counts)==1<<(m*n)
    return d,ell,c,periodic_dim,counts


def verify():
    matrices=0
    for m in (4,8,16):
        for n in (3,4,5,6,7,8,9,10,12,14,15,16,18,20,24):
            if m*n>200:continue
            d,L,c,r,expected=predicted(m,n)
            A=adjacency(m,n)
            cur=[1<<i for i in range(m*n)]
            for t in range(L+3):
                got=rank2(cur)
                want=r+c*max(0,L-t)
                assert got==want, ('rank',m,n,t,got,want)
                cur=times(cur,A)
            matrices+=1
    checked=0
    for m,n in ((4,3),(4,4)):
        A=adjacency(m,n)
        d,L,c,r,expected=predicted(m,n)
        counts=Counter(first_periodic_time(x,A) for x in range(1<<(m*n)))
        assert [counts.get(t,0) for t in range(L+1)]==expected, ('micro',m,n,counts,expected)
        assert all(t<=L for t in counts)
        checked+=1<<(m*n)
    for n in (5,6,7,8,9):
        m=4
        A=adjacency(m,n)
        d,L,c,r,expected=predicted(m,n)
        for x in range(500):
            assert first_periodic_time(x,A)<=L
    print('TORUS_4NEIGHBOR_GF2_VERIFY_OK')
    print('GF2_rank_power_rectangles',matrices)
    print('individually_classified_labelled_initial_states',checked)
    print('additional_sampled_configurations',2500)
    print('sample_exact_shells_m4_n3',predicted(4,3)[-1])
    print('sample_exact_shells_m4_n4',predicted(4,4)[-1])

if __name__=='__main__':verify()
