#!/usr/bin/env python3
from collections import Counter

def xpoints(n):
    return [(i,a) for i in range(n+1) for a in (0,1)]

def xleq(x,y):
    return x==y or x[0] < y[0]

def pleq(p,q):
    return xleq(p[0],q[0]) and xleq(p[1],q[1])

def core_points(n):
    return [((i,0),(i,1)) for i in range(n+1)] + [((i,1),(i,0)) for i in range(n+1)]

def check(n):
    X=xpoints(n)
    pts=[(x,y) for x in X for y in X if x!=y]
    core=set(core_points(n))
    order=[p for p in pts if p[0][0]!=p[1][0]]
    # xpoints and pts are already lexicographic in (i,a,j,b).
    live=set(pts)
    assert len(pts)==(2*n+2)*(2*n+1)
    assert len(core)==2*n+2
    assert len(order)==4*n*(n+1)
    for p in order:
        assert p in live
        i,a=p[0]; j,b=p[1]
        if i<j:
            witness=((i,a),(i,1-a))
        else:
            witness=((j,1-b),(j,b))
        assert witness in live and witness!=p and pleq(witness,p)
        lower=[q for q in live if q!=p and pleq(q,p)]
        assert lower
        assert all(pleq(q,witness) for q in lower), (n,p,witness,lower)
        live.remove(p)
    assert live==core
    # The surviving order is exactly X_n: at each level there are two
    # incomparable orientations, and everything at a lower level is below
    # everything at a higher level.
    for p in core:
        for q in core:
            ip=p[0][0]; iq=q[0][0]
            expected = (p==q) or (ip<iq)
            assert pleq(p,q)==expected
    # Core has no beat points when n>=1.
    for p in core:
        lo=[q for q in core if q!=p and pleq(q,p)]
        up=[q for q in core if q!=p and pleq(p,q)]
        has_max=any(all(pleq(q,m) for q in lo) for m in lo)
        has_min=any(all(pleq(m,q) for q in up) for m in up)
        assert not has_max and not has_min
    return len(pts),len(order),len(core)

out=[]
for n in range(2,11):
    out.append((n,)+check(n))
print("VERIFY_OK " + " ".join(f"n={n}:points={p},deletions={d},core={c}" for n,p,d,c in out))
