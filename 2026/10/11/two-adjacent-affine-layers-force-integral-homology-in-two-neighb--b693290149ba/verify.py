#!/usr/bin/env python3
"""Exact incidence and finite-field chain verification for two adjacent affine layers."""
from itertools import product, combinations
from collections import deque

def rank_mod(columns, p):
    piv={}
    for col in columns:
        c={i:(a%p) for i,a in col.items() if a%p}
        while c:
            j=max(c)
            if j not in piv:
                pivot=c[j]
                inv=pow(pivot,-1,p)
                piv[j]={i:(v*inv)%p for i,v in c.items() if v%p}
                break
            mul=c[j]
            for i,v in piv[j].items():
                val=(c.get(i,0)-mul*v)%p
                if val:c[i]=val
                else:c.pop(i,None)
    return len(piv)

def make_complex(n,q):
    vertices=[(i,x) for i in range(n) for x in range(q)]
    faces=[[] for _ in range(n)]
    for k in range(1,n):
        for support in combinations(range(n),k):
            for xs in product(range(q),repeat=k):
                faces[k-1].append(tuple((i,x) for i,x in zip(support,xs)))
    for xs in product(range(q),repeat=n):
        if sum(xs)%q in (0,1):faces[n-1].append(tuple(enumerate(xs)))
    return faces

def check(n,q):
    faces=make_complex(n,q)
    facets=faces[-1]
    idfacet={f:j for j,f in enumerate(facets)}
    edges=[set() for _ in facets]
    partial={}
    for j,f in enumerate(facets):
        for t in range(n):
            part=f[:t]+f[t+1:]
            partial.setdefault(part,[]).append(j)
    assert all(len(ids)==2 for ids in partial.values())
    for ids in partial.values():
        a,b=ids
        edges[a].add(b);edges[b].add(a)
    seen={0};dq=deque([0])
    while dq:
        for v in edges[dq.popleft()]:
            if v not in seen:seen.add(v);dq.append(v)
    assert len(seen)==len(facets)
    z=[sum(x for _,x in f)%q for f in facets]
    assert all(z[i]!=z[j] for i in range(len(edges)) for j in edges[i])
    ranks=[]
    for prime in (2,3,5):
        dim=[]
        for k in range(n):
            if not k:ranks_k=0
            else:
                ids={f:i for i,f in enumerate(faces[k-1])}
                cols=[]
                for f in faces[k]:
                    col={ids[f[:j]+f[j+1:]]:(-1)**j for j in range(k+1)}
                    cols.append(col)
                ranks_k=rank_mod(cols,prime)
            dim.append(ranks_k)
        betas=[len(faces[k])-dim[k]- (dim[k+1] if k+1<n else 0) for k in range(n)]
        betas[0]-=1
        target=[0]*n
        target[-1]=1
        target[-2]=(q-2)*q**(n-1)-(q-1)**n+1
        if n==2:target[0]=0 # H0 is zero, top degree one
        assert betas==target,(n,q,prime,betas,target)
        assert dim[-1]==2*q**(n-1)-1
        ranks.append((prime,betas))
    return len(facets),len(partial),ranks

if __name__=='__main__':
    count=0
    for n in range(2,5):
        for q in range(2,6):
            facets,partials,_=check(n,q)
            print(f'n={n} q={q}: facets={facets}, codimension-one faces={partials}, homology_verified=F2,F3,F5')
            count+=1
    print('VERIFY_OK',count,'exact complexes; connectivity, codimension-one incidences and three characteristics')
