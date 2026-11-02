#!/usr/bin/env python3
"""Direct chain-level verification for the 2-subset Kneser independence complex.
No external packages; generates every face from pairwise-intersecting edges.
"""
from itertools import combinations
from math import comb
from collections import defaultdict,Counter

def faces(n):
    vertices=list(combinations(range(n),2))
    triples=[tuple(sorted((vertices.index(tuple(sorted(e))) for e in combinations(t,2)))) for t in combinations(range(n),3)]
    facets=[tuple(vertices.index(e) for e in vertices if i in e) for i in range(n)]+triples
    ff=defaultdict(set)
    for f in facets:
        for k in range(1,len(f)+1):
            ff[k-1].update(combinations(sorted(f),k))
    return vertices, {k:sorted(v) for k,v in ff.items()}

def rank_mod(rows,p=101):
    rows=[list(map(lambda x:x%p, row)) for row in rows]
    if not rows:return 0
    nr,nc=len(rows),len(rows[0]);r=0
    for c in range(nc):
        pivot=next((i for i in range(r,nr) if rows[i][c]), None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        inv=pow(rows[r][c],-1,p)
        for j in range(c,nc):rows[r][j]=(rows[r][j]*inv)%p
        for i in range(r+1,nr):
            mult=rows[i][c]
            if mult:
                for j in range(c,nc):rows[i][j]=(rows[i][j]-mult*rows[r][j])%p
        r+=1
        if r==nr:break
    return r

def betti(n,ff):
    f=[len(ff.get(i,[])) for i in range(max(ff)+1)]
    ranks=[0]*(len(f)+1)
    for d in range(1,len(f)):
        lower={face:i for i,face in enumerate(ff[d-1])}
        mat=[[0]*f[d] for _ in range(f[d-1])]
        for col,face in enumerate(ff[d]):
            for i in range(d+1):
                low=face[:i]+face[i+1:]
                mat[lower[low]][col]=(-1)**i
        ranks[d]=rank_mod(mat)
    b=[f[d]-ranks[d]-ranks[d+1] for d in range(len(f))]
    return f,b

def sign(xs):
    return -1 if sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))%2 else 1

def signed_lefschetz(verts,ff,perm):
    index={v:i for i,v in enumerate(verts)}
    maps=[index[tuple(sorted((perm[a],perm[b])))] for a,b in verts]
    signed=[]
    for d in range(max(ff)+1):
        trace=0
        for f in ff[d]:
            g=[maps[i] for i in f]
            if sorted(g)==list(f):trace+=sign(g)
        signed.append(trace)
    return signed,sum((-1)**d*v for d,v in enumerate(signed))-1

def type_representatives(n):
    def parts(N,m=1):
        if not N:
            yield ()
        else:
            for k in range(m,N+1):
                for tail in parts(N-k,k):yield (k,)+tail
    for partition in parts(n):
        perm=list(range(n)); i=0
        for k in partition:
            cyc=list(range(i,i+k))
            for a,b in zip(cyc,cyc[1:]+cyc[:1]):perm[a]=b
            i+=k
        yield partition,perm

def expected(m):
    m1=m.count(1);m2=m.count(2);m3=m.count(3)
    z=m1-1
    return z*(z-1)*(z-2)//6-z*m2+m3

for n in (4,5,6,7):
    vv,ff=faces(n)
    f,b=betti(n,ff)
    assert b[0]==1 and b[1]==0 and b[2]==comb(n-1,3) and not any(b[3:]),(n,b)
    ntypes=0
    for typ,perm in type_representatives(n):
        traces,chi=signed_lefschetz(vv,ff,perm)
        assert chi==expected(typ),(n,typ,chi,expected(typ),traces)
        ntypes+=1
    print(f'n={n} f={f} betti={b} conjugacy_classes={ntypes} character_matches=YES')
print('DIRECT_CHAIN_CERTIFICATE_OK')
