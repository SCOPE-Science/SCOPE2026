#!/usr/bin/env python3
from collections import defaultdict

def crown(n):
    assert n >= 2
    N = 2*n
    leq = [[False]*N for _ in range(N)]
    for x in range(N): leq[x][x] = True
    for i in range(n):
        leq[i][n+i] = True
        leq[i][n+((i-1)%n)] = True
    return leq

def induced(points, base_leq):
    m=len(points)
    L=[[False]*m for _ in range(m)]
    for i,p in enumerate(points):
        for j,q in enumerate(points):
            if isinstance(p, tuple):
                L[i][j] = base_leq[p[0]][q[0]] and base_leq[p[1]][q[1]]
            else:
                L[i][j] = base_leq[p][q]
    return L

def beat_core(points, leq):
    active=list(range(len(points)))
    deletions=[]
    while True:
        hit=None
        for x in active:
            upper=[y for y in active if y!=x and leq[x][y]]
            for w in upper:
                if all(leq[w][z] for z in upper):
                    hit=(x,'up',w); break
            if hit: break
            lower=[y for y in active if y!=x and leq[y][x]]
            for w in lower:
                if all(leq[z][w] for z in lower):
                    hit=(x,'down',w); break
            if hit: break
        if hit is None: break
        deletions.append(hit)
        active.remove(hit[0])
    return active,deletions

def rank_gf2(cols):
    piv={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x
                break
    return len(piv)

def betti_order_complex(points, leq):
    n=len(points)
    edges=[]
    for i in range(n):
        for j in range(n):
            if i!=j and leq[i][j]: edges.append((i,j))
    eidx={e:k for k,e in enumerate(edges)}
    up=defaultdict(list)
    for a,b in edges: up[a].append(b)
    tris=[]
    for a,b in edges:
        for c in up[b]: tris.append((a,b,c))
    r1=rank_gf2([(1<<a)|(1<<b) for a,b in edges])
    d2=[]
    for a,b,c in tris:
        d2.append((1<<eidx[(a,b)])|(1<<eidx[(b,c)])|(1<<eidx[(a,c)]))
    r2=rank_gf2(d2)
    return (n,len(edges),len(tris)), (n-r1, len(edges)-r1-r2, len(tris)-r2)

def check(n):
    C=crown(n); N=2*n
    F=[(x,y) for x in range(N) for y in range(N) if x!=y]
    LF=induced(F,C)
    assert len(F)==2*n*(2*n-1)
    # projection order-preserving
    for i,p in enumerate(F):
        for j,q in enumerate(F):
            if LF[i][j]: assert C[p[0]][q[0]]
    fiber_sizes=[]
    fiber_deletions=[]
    for x in range(N):
        U=[u for u in range(N) if C[u][x]]
        P=[(u,v) for u in U for v in range(N) if u!=v]
        LP=induced(P,C)
        core,ds=beat_core(P,LP)
        assert len(core)==1, (n,x,len(core))
        fiber_sizes.append(len(P))
        fiber_deletions.append(len(ds))
    fvec,betti=betti_order_complex(F,LF)
    assert betti==(1,1,0), (n,betti)
    return len(F), tuple(sorted(set(fiber_sizes))), fvec, betti

rows=[]
for n in range(2,13):
    rows.append((n,)+check(n))
print('VERIFY_OK')
for row in rows:
    print('n=%d points=%d fiber_sizes=%s fvec=%s betti_F2=%s' % row)
