#!/usr/bin/env python3
"""Reproduce a sharp tree-character-spectrum collision using Python 3 stdlib only."""
from collections import Counter
from functools import lru_cache

A = ((0,1),(0,6),(0,9),(1,2),(1,5),(2,3),(3,4),(6,7),(7,8))
B = ((0,1),(0,7),(1,2),(1,5),(2,3),(2,4),(5,6),(7,8),(8,9))
EXPECTED = {(0,0):1,(1,1):9,(2,1):10,(2,2):26,(3,1):2,(3,2):54,
            (3,3):28,(4,2):35,(4,3):82,(4,4):9,(5,2):7,(5,3):86,
            (5,4):33,(6,3):38,(6,4):46,(7,3):6,(7,4):30,(8,4):9,(9,4):1}
EXPECTED_TREE_COUNTS = [1,1,1,2,3,6,11,23,47,106]


def canonical(n, edges):
    adj = [set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    active = set(range(n))
    while len(active)>2:
        leaves={i for i in active if len(adj[i]&active)<=1}
        active-=leaves
    def rooted(v,parent):
        children = sorted(rooted(w,v) for w in adj[v] if w != parent)
        return '('+''.join(children)+')'
    centers=sorted(active)
    if len(centers)==1:return rooted(centers[0],-1)
    a,b=centers
    return '('+''.join(sorted((rooted(a,b),rooted(b,a))))+')'


def tree_families(nmax=10):
    prev=[(1,())]
    counts=[]
    for n in range(1,nmax+1):
        if n>1:
            seen={}
            for k,edges in prev:
                assert k==n-1
                for v in range(k):
                    new=edges+((v,k),)
                    seen.setdefault(canonical(n,new),(n,new))
            prev=list(seen.values())
        counts.append(len(prev))
        yield n,prev,counts


def matching_profile(n,edges):
    m=len(edges)
    conflicts=[]
    for a,b in edges:
        conflicts.append(sum(1<<j for j,(c,d) in enumerate(edges)
                             if a in (c,d) or b in (c,d)))
    @lru_cache(None)
    def match(mask):
        if not mask:return 0
        low=mask & -mask; i=low.bit_length()-1
        return max(match(mask^low),1+match(mask & ~conflicts[i]))
    c=Counter((mask.bit_count(),match(mask)) for mask in range(1<<m))
    assert sum(c.values())==2**m
    return tuple(sorted(c.items()))


def diameter(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    best=0
    for src in range(n):
        dist={src:0};q=[src]
        for u in q:
            for v in adj[u]:
                if v not in dist:dist[v]=dist[u]+1;q.append(v)
        assert len(dist)==n
        best=max(best,max(dist.values()))
    return best


def rank_mod(mat,p):
    a=[[v%p for v in row] for row in mat]
    n=len(a);r=0
    for c in range(n):
        pivot=next((i for i in range(r,n) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c],-1,p)
        for j in range(c,n):a[r][j]=(a[r][j]*inv)%p
        for i in range(n):
            if i!=r and a[i][c]:
                t=a[i][c]
                for j in range(c,n):a[i][j]=(a[i][j]-t*a[r][j])%p
        r+=1
    return r


def sample_ranks(n,edges):
    # All 512 zero/nonzero supports, coefficients 1, over two odd fields.
    e=list(edges)
    for p in (3,5):
        for mask in range(1<<len(e)):
            a=[[0]*n for _ in range(n)]
            for j,(u,v) in enumerate(e):
                if mask>>j & 1:a[u][v]=1;a[v][u]=-1
            # Independent matching recursion on vertex bitmask and chosen edges.
            chosen=[edge for j,edge in enumerate(e) if mask>>j & 1]
            @lru_cache(None)
            def M(vertices):
                if not vertices:return 0
                low=vertices & -vertices;u=low.bit_length()-1
                out=M(vertices^low)
                for x,y in chosen:
                    if u in (x,y):
                        v=y if x==u else x
                        if vertices>>v & 1:out=max(out,1+M(vertices^low^(1<<v)))
                return out
            assert rank_mod(a,p)==2*M((1<<n)-1),(p,mask)


def main():
    assert canonical(10,A)!=canonical(10,B)
    assert sorted((diameter(10,A),diameter(10,B)))==[6,7]
    a=dict(matching_profile(10,A));b=dict(matching_profile(10,B))
    assert a==b==EXPECTED
    counts=[];collisions=[]
    for n,trees,cs in tree_families(10):
        counts=cs
        seen={}
        for size,edges in trees:
            key=matching_profile(size,edges)
            if key in seen:collisions.append((n,seen[key],edges))
            else:seen[key]=edges
        print('tree order',n,'isomorphism classes',len(trees),'matching-support collisions',sum(c[0]==n for c in collisions))
    assert counts==EXPECTED_TREE_COUNTS,counts
    assert len(collisions)==1 and collisions[0][0]==10,collisions
    c1,c2=collisions[0][1:]
    assert {canonical(10,c1),canonical(10,c2)}=={canonical(10,A),canonical(10,B)}
    sample_ranks(10,A)
    sample_ranks(10,B)
    print('Common nonzero coefficients (edge count, matching number, frequency):')
    for (k,r),v in sorted(EXPECTED.items()):print(k,r,v)
    for q in (3,5,7):
        count=[sum(v*(q-1)**k for (k,s),v in EXPECTED.items() if r==s)*q**(10-2*r) for r in range(5)]
        assert sum(c*q**(2*r) for r,c in enumerate(count))==q**19
        print('q',q,'character degrees 1,q,q^2,q^3,q^4 multiplicities',count)
    print('VERIFY_OK')

if __name__=='__main__':main()
