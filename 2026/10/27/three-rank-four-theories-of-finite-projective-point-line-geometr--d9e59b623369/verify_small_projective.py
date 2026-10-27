"""Independent literal enumeration of rank-four first-order Hintikka types.
For the small binary and ternary projective planes only. Pure Python.
"""
from itertools import product

def geometry(q):
    m=3; seen=set()
    for coords in product(range(q),repeat=m):
        if not any(coords):continue
        lead=next(x for x in coords if x)
        inv=next(v for v in range(1,q) if v*lead%q==1)
        seen.add(tuple(x*inv%q for x in coords))
    points=sorted(seen); idx={v:i for i,v in enumerate(points)}
    lines=set()
    for a in points:
        for b in points:
            if a==b:continue
            pts=set()
            for u,v in product(range(q),repeat=2):
                w=tuple((u*a[k]+v*b[k])%q for k in range(3))
                if not any(w):continue
                lead=next(x for x in w if x)
                inv=next(c for c in range(1,q) if c*lead%q==1)
                pts.add(idx[tuple(x*inv%q for x in w)])
            lines.add(tuple(sorted(pts)))
    lines=sorted(lines)
    n=len(points); N=n+len(lines)
    edges={(p,n+j) for j,L in enumerate(lines) for p in L}
    return n,N,edges

def simple_code(t,n,edges):
    sorts=tuple(int(x>=n) for x in t)
    eq=tuple(t[i]==t[j] for i in range(4) for j in range(i+1,4))
    inc=tuple((min(t[i],t[j]),max(t[i],t[j])) in edges for i in range(4) for j in range(i+1,4))
    return sorts,eq,inc

def fingerprint(q):
    n,N,edges=geometry(q)
    d0={}
    for a in range(N):
        for b in range(N):
            for c in range(N):
                d0[a,b,c]=frozenset(simple_code((a,b,c,z),n,edges) for z in range(N))
    d1={(a,b):frozenset(d0[a,b,c] for c in range(N)) for a in range(N) for b in range(N)}
    d2={a:frozenset(d1[a,b] for b in range(N)) for a in range(N)}
    return frozenset(d2.values()),N

if __name__=='__main__':
    f2,n2=fingerprint(2)
    f3,n3=fingerprint(3)
    assert n2==14 and n3==26
    assert f2!=f3
    print('PG(2,2) vs PG(2,3): DIFFERENT rank-four types (literal recursion); VERIFY_OK')
