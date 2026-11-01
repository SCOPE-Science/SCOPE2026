#!/usr/bin/env python3
"""Exact binary checks for two-feedback hypercube neighbor-XOR dynamics.

Uses Python integer bitsets and integer Gaussian elimination; no dependencies.
The exact theorem is proved separately; these finite checks are corroboration.
"""
from collections import Counter


def gf2rank(vectors):
    pivots = {}
    for v in vectors:
        while v:
            p = v.bit_length()-1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)


def update(v, d, j):
    """The feedback vertices have binary labels 0 and (2**j-1)."""
    r = 0
    y = v
    while y:
        low = y & -y
        u = low.bit_length()-1
        for k in range(d):
            r ^= 1 << (u ^ (1 << k))
        y ^= low
    r ^= v & 1
    r ^= v & (1 << ((1 << j)-1))
    return r


def columns(d,j,steps, shifted=False):
    n=1<<d
    vecs=[1<<v for v in range(n)]
    ranks=[]
    for _ in range(steps):
        vecs=[update(v,d,j) ^ (v if shifted else 0) for v in vecs]
        ranks.append(gf2rank(vecs))
    return ranks


def fixed_dimension(d,j,k,trim=0):
    n=1<<d
    im=[]
    for u in range(n):
        v=1<<u
        for _ in range(trim): v=update(v,d,j)
        im.append(v)
    dim=gf2rank(im)
    deviations=[]
    for v in im:
        w=v
        for _ in range(k): w=update(w,d,j)
        deviations.append(w ^ v)
    return dim-gf2rank(deviations)


def predicted(d,j):
    n=1<<d; h=n//2
    if d%2==0 and j==1:
        return [h+2,4,4,4,4,4],None,{1:0,2:0,3:2,6:4},2
    if d%2==0:
        return [h+2,4,2,2,2,2],None,{1:2,2:2,3:2,6:2},3
    if j==1:
        return [n-1,n-2,n-2,n-2,n-2,n-2],[h+2,4,3,2,2],{1:h-2,2:n-4,4:n-2},2
    return [n]*6,None,{1:h-2,2:n-4,3:h+2,6:n},0


def exhaustive(d,j):
    n=1<<d
    outcomes=Counter()
    for x in range(1<<n):
        seen={}
        v=x; t=0
        while v not in seen:
            seen[v]=t
            v=update(v,d,j)
            t+=1
            assert t<=12, ('unexpected long trajectory',d,j,x)
        T=seen[v]
        p=t-T
        outcomes[T,p]+=1
    return outcomes


def check():
    tested=0
    for d in range(3,9):
        for j in range(1,d+1):
            powers, shifted, fixed, transient = predicted(d,j)
            actual=columns(d,j,6)
            assert actual==powers,(d,j,'ranks',actual,powers)
            if shifted is not None:
                actual_shift=columns(d,j,5,True)
                assert actual_shift==shifted,(d,j,'shifted',actual_shift,shifted)
            trim=transient
            for k,expect in fixed.items():
                actual_dim=fixed_dimension(d,j,k,trim)
                assert actual_dim==expect,(d,j,k,actual_dim,expect)
            tested+=1
    samples=0
    for d,j in ((3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(4,4)):
        outcomes=exhaustive(d,j)
        n=1<<d;h=n//2
        by_t=Counter()
        by_p=Counter()
        for (t,p),c in outcomes.items():
            by_t[t]+=c
            if t==0:by_p[p]+=c
        if d%2==0 and j==1:
            cumulative=lambda t:2**(4+(h-2)*min(t,2))
            expected_per={1:1,3:3,6:12}
        elif d%2==0:
            cumulative=lambda t:2**(2+2*min(t,3)+(h-4)*min(t,2))
            expected_per={1:4}
        elif j==1:
            cumulative=lambda t:2**(n-2+min(t,2))
            expected_per={1:2**(h-2),2:2**(n-4)-2**(h-2),4:2**(n-2)-2**(n-4)}
        else:
            cumulative=lambda t:2**n
            expected_per={1:2**(h-2),2:2**(n-4)-2**(h-2),3:2**(h+2)-2**(h-2),6:2**n-2**(n-4)-2**(h+2)+2**(h-2)}
        last=0
        for t in range(0,4):
            goal=cumulative(t)-last
            assert by_t[t]==goal,('transient',d,j,t,by_t[t],goal)
            last=cumulative(t)
        assert sum(by_t.values())==2**n
        assert {k:v for k,v in by_p.items() if v}==expected_per,('period populations',d,j,by_p,expected_per)
        samples+=1<<n
    print('TWO_FEEDBACK_HYPERCUBE_CHECKS_PASSED')
    print('Dimension-distance pairs:',tested)
    print('Exhaustively checked labelled configurations:',samples)
    print('Dimensions: 3 to 8; exact rank and fixed-space dimensions checked.')

if __name__=='__main__':check()
