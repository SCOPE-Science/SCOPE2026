#!/usr/bin/env python3
from itertools import combinations, product
from collections import deque
from math import prod

MAX_ORDER = 9

def compositions(n,k):
    if k==1:
        yield (n,); return
    for cuts in combinations(range(1,n),k-1):
        pts=(0,)+cuts+(n,)
        yield tuple(pts[i+1]-pts[i] for i in range(k))

def profiles_upto(nmax):
    for n in range(2,nmax+1):
        for na in range(1,n):
            nb=n-na
            for p in range(1,min(na,nb)+1):
                for a in compositions(na,p):
                    for b in compositions(nb,p):
                        yield a,b

def build(a,b):
    p=len(a); verts=[]; classes=[]
    A=[]; B=[]
    for i,s in enumerate(a):
        block=[]
        for q in range(s):
            block.append(len(verts)); verts.append(('A',i,q))
        A.append(block); classes.append(block)
    for j,s in enumerate(b):
        block=[]
        for q in range(s):
            block.append(len(verts)); verts.append(('B',j,q))
        B.append(block); classes.append(block)
    n=len(verts); adj=[set() for _ in range(n)]
    for i in range(p):
        for j in range(p):
            if j<=i:
                for u in A[i]:
                    for v in B[j]:
                        adj[u].add(v); adj[v].add(u)
    return verts,A,B,adj

def distances(adj):
    n=len(adj); D=[]
    for s in range(n):
        d=[None]*n; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v] is None:
                    d[v]=d[u]+1; q.append(v)
        assert all(x is not None for x in d)
        D.append(d)
    return D

def mmd(u,v,adj,D):
    d=D[u][v]
    return all(D[x][v]<=d for x in adj[u]) and all(D[y][u]<=d for y in adj[v])

def predicted_mmd(u,v,verts,A,B):
    if len(verts)==2:
        return True
    su,iu,_=verts[u]; sv,iv,_=verts[v]
    if su==sv:
        return iu==iv
    if su=='A': i,j=iu,iv
    else: i,j=iv,iu
    return j>i

def strongly_resolves(w,u,v,D):
    return D[w][u] == D[w][v] + D[v][u] or D[w][v] == D[w][u] + D[u][v]

def is_strong_set(mask,n,D):
    for u in range(n):
        for v in range(u+1,n):
            ok=False
            mm=mask
            while mm:
                lsb=mm & -mm; w=lsb.bit_length()-1; mm-=lsb
                if strongly_resolves(w,u,v,D):
                    ok=True; break
            if not ok: return False
    return True

def theorem(a,b):
    p=len(a); N=sum(a)+sum(b)
    if N==2:
        return 1,2
    return N-p-1, sum(prod(b[:t+1])*prod(a[t:]) for t in range(p))

profiles=0; subset_checks=0; mmd_checks=0; basis_checks=0
for a,b in profiles_upto(MAX_ORDER):
    verts,A,B,adj=build(a,b); n=len(verts); D=distances(adj)
    profiles += 1
    # Exact MMD graph structure.
    for u in range(n):
        for v in range(u+1,n):
            mmd_checks += 1
            got=mmd(u,v,adj,D); exp=predicted_mmd(u,v,verts,A,B)
            assert got==exp, (a,b,'MMD',u,v,got,exp)
    target,count_formula=theorem(a,b)
    count=0
    # Enumerate literal strong resolving sets at the claimed minimum and rule out all smaller sizes.
    for k in range(target+1):
        c=0
        for comb in combinations(range(n),k):
            subset_checks += 1
            mask=sum(1<<x for x in comb)
            if is_strong_set(mask,n,D): c+=1
        if k<target:
            assert c==0,(a,b,'too small',k,c,target)
        else:
            count=c
    basis_checks += count
    assert count==count_formula,(a,b,'basis count',count,count_formula,target)
print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} mmd_checks={mmd_checks} basis_checks={basis_checks} max_order={MAX_ORDER}')
