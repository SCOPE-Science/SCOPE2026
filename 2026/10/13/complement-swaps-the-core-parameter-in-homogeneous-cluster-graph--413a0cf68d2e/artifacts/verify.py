#!/usr/bin/env python3
import itertools, math

def graph_cluster(m,n):
    N=m*n
    def edge(a,b): return a!=b and a//n==b//n
    return N, edge

def complement_edge(edge):
    return lambda a,b: a!=b and not edge(a,b)

def is_hom(f,N,edge):
    for a in range(N):
        for b in range(a+1,N):
            if edge(a,b) and not edge(f[a],f[b]):
                return False
    return True

def image_ranks(N,edge):
    out=set()
    for f in itertools.product(range(N), repeat=N):
        if is_hom(f,N,edge): out.add(len(set(f)))
    return out

def automorphisms(m,n):
    # Explicit wreath product permutations.
    out=[]
    for cp in itertools.permutations(range(m)):
        for inners in itertools.product(list(itertools.permutations(range(n))), repeat=m):
            p=[None]*(m*n)
            for c in range(m):
                for j in range(n):
                    p[c*n+j]=cp[c]*n+inners[c][j]
            out.append(tuple(p))
    return out

def orbit_count_injective(m,n,k):
    N=m*n
    A=automorphisms(m,n)
    unseen=set(itertools.permutations(range(N),k))
    c=0
    while unseen:
        t=unseen.pop(); c+=1
        orb={tuple(p[x] for x in t) for p in A}
        unseen.difference_update(orb)
    return c

def restricted_partitions(k,m,n):
    # RGS enumeration: at most m blocks, each block size <=n.
    if k==0: return 1
    ans=0
    def rec(a,maxv,counts):
        nonlocal ans
        i=len(a)
        if i==k:
            ans+=1; return
        for v in range(maxv+2):
            if v>=m: break
            if v>maxv+1: break
            if v==maxv+1 and v!=0:
                pass
            if v>maxv+1: continue
            if v<len(counts) and counts[v]>=n: continue
            nc=list(counts)
            if v==len(nc): nc.append(1)
            else: nc[v]+=1
            rec(a+[v], max(maxv,v), nc)
    rec([0],0,[1]) if k>1 else None
    return ans if k>1 else 1

checks=0
for m,n in [(2,2),(2,3),(3,2)]:
    N,e=graph_cluster(m,n)
    re=image_ranks(N,e)
    pred=set(range(n,m*n+1,n))
    assert re==pred,(m,n,re,pred); checks+=1
    ce=complement_edge(e)
    re2=image_ranks(N,ce)
    pred2=set(range(m,m*n+1))
    assert re2==pred2,(m,n,re2,pred2); checks+=1
    A=automorphisms(m,n)
    # Wreath size and complement invariance.
    assert len(A)==math.factorial(m)*(math.factorial(n)**m); checks+=1
    for p in A:
        for a in range(N):
            for b in range(a+1,N):
                assert e(a,b)==e(p[a],p[b]); checks+=1
                assert ce(a,b)==ce(p[a],p[b]); checks+=1
    for k in range(1,min(4,N)+1):
        oc=orbit_count_injective(m,n,k)
        rp=restricted_partitions(k,m,n)
        assert oc==rp,(m,n,k,oc,rp); checks+=1

print(f'VERIFY_OK {checks} exact assertions')
