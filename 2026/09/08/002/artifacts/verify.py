"""Verifier for lane-38 artifacts (stdlib+numpy+sympy only). Runs in <30 s."""
import csv, json, sys
from collections import deque, defaultdict
import numpy as np
import sympy as sp

BASE='/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-38/output/artifacts'
# Fallback: relative to this file
import os
_here=os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(BASE):
    BASE=_here

def load_edges():
    adjs=[]
    with open(os.path.join(BASE,'catalog_edges.csv')) as f:
        r=csv.DictReader(f)
        for row in r:
            es=[]
            for tok in row['edge_list'].split(';'):
                u,v=tok.split('-'); es.append((int(u),int(v)))
            adj=[0]*18
            for u,v in es:
                adj[u]|=(1<<v); adj[v]|=(1<<u)
            adjs.append(adj)
    return adjs

def is_cubic(adj): return all(bin(adj[u]).count('1')==3 for u in range(18))
def is_connected(adj):
    seen=1<<0; stack=[0]
    while stack:
        u=stack.pop()
        for v in range(18):
            if ((adj[u]>>v)&1) and not ((seen>>v)&1):
                seen|=(1<<v); stack.append(v)
    return bin(seen).count('1')==18
def bipartition(adj):
    col=[-1]*18; col[0]=0; dq=deque([0])
    while dq:
        u=dq.popleft()
        for v in range(18):
            if (adj[u]>>v)&1:
                if col[v]==-1: col[v]=1-col[u]; dq.append(v)
                elif col[v]==col[u]: return None
    return col

def are_isomorphic(A,B):
    n=18
    nbrA=[[v for v in range(n) if (A[u]>>v)&1] for u in range(n)]
    nbrB=[[v for v in range(n) if (B[u]>>v)&1] for u in range(n)]
    seen=[False]*n; order=[]; dq=deque([0]); seen[0]=True
    while dq:
        u=dq.popleft(); order.append(u)
        for v in nbrA[u]:
            if not seen[v]: seen[v]=True; dq.append(v)
    if len(order)!=n: return False
    colA=[-1]*n; colA[0]=0; dq=deque([0])
    while dq:
        u=dq.popleft()
        for v in nbrA[u]:
            if colA[v]==-1: colA[v]=1-colA[u]; dq.append(v)
    colB=[-1]*n; colB[0]=0; dq=deque([0])
    while dq:
        u=dq.popleft()
        for v in nbrB[u]:
            if colB[v]==-1: colB[v]=1-colB[u]; dq.append(v)
    for flip in (0,1):
        for c0 in [v for v in range(n) if colB[v]==(colA[order[0]]^flip)]:
            f=[-1]*n; finv=[-1]*n; f[order[0]]=c0; finv[c0]=order[0]
            def dfs(k):
                if k==n: return True
                u=order[k]
                mapped=[f[w] for w in nbrA[u] if f[w]!=-1]
                if mapped:
                    s=set(nbrB[mapped[0]])
                    for x in mapped[1:]: s.intersection_update(nbrB[x])
                    cu=colA[u]^flip
                    clist=[v for v in s if finv[v]==-1 and colB[v]==cu]
                else:
                    cu=colA[u]^flip
                    clist=[v for v in range(n) if finv[v]==-1 and colB[v]==cu]
                for v in clist:
                    ok=True
                    for wi in range(k):
                        w=order[wi]
                        if ((A[u]>>w)&1)!=((B[v]>>f[w])&1): ok=False; break
                    if not ok: continue
                    f[u]=v; finv[v]=u
                    if dfs(k+1): return True
                    f[u]=-1; finv[v]=-1
                return False
            if dfs(1): return True
    return False

def bareiss_det(M):
    n=len(M); A=[r[:] for r in M]; sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            s=-1
            for i in range(k+1,n):
                if A[i][k]!=0: s=i; break
            if s==-1: return 0
            A[k],A[s]=A[s],A[k]; sign*=-1
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*A[k][k]-A[i][k]*A[k][j])//prev
            A[i][k]=0
        prev=A[k][k]
        if prev==0: return 0
    return sign*A[n-1][n-1]

def adj_mat(adj):
    A=np.zeros((18,18),dtype=int)
    for u in range(18):
        for v in range(18):
            if (adj[u]>>v)&1: A[u,v]=1
    return A

def charpoly_interp(adj):
    A=adj_mat(adj).tolist(); n=18; pts=list(range(19)); vals=[]
    for t in pts:
        M=[[(t if i==j else 0)-A[i][j] for j in range(n)] for i in range(n)]
        vals.append(bareiss_det(M))
    V=sp.Matrix([[sp.Integer(t)**j for j in range(19)] for t in pts])
    b=sp.Matrix([sp.Integer(v) for v in vals])
    cr=V.LUsolve(b)
    return tuple(reversed([int(x) for x in cr]))

def main():
    adjs=load_edges()
    assert len(adjs)==149, len(adjs)
    print(f"[1/5] loaded {len(adjs)} graphs")
    for i,a in enumerate(adjs):
        assert is_cubic(a) and is_connected(a) and bipartition(a) is not None
        c=bipartition(a); assert sorted([c.count(0),c.count(1)])==[9,9]
    print("[2/5] stratum checks pass (cubic/connected/bipartite 9+9)")
    # polys
    with open(os.path.join(BASE,'polys.csv')) as f:
        r=list(csv.DictReader(f))
        polys=[tuple(int(r[i][f'c{k}']) for k in range(19)) for i in range(149)]
    # spot-check 10 via Bareiss + full check via sympy quickly? do Bareiss for all (3 s)
    for i,a in enumerate(adjs):
        c2=charpoly_interp(a)
        assert c2==polys[i], f"poly mismatch {i}"
        if (i+1)%50==0: print(f"  exact poly {i+1}/149 ok")
    print("[3/5] exact polys verified (Bareiss+interp matches stored SymPy polys)")
    # float spectra + partition agreement
    with open(os.path.join(BASE,'spectra_float.csv')) as f:
        r=list(csv.DictReader(f))
        specs=[tuple(float(r[i][f'e{k}']) for k in range(18)) for i in range(149)]
    recom=[tuple(sorted(np.linalg.eigvalsh(adj_mat(a).astype(float)).tolist())) for a in adjs]
    for i in range(149):
        assert max(abs(x-y) for x,y in zip(specs[i],recom[i]))<1e-9
    def pairs(classes):
        s=set()
        for v in classes.values():
            for x in range(len(v)):
                for y in range(x+1,len(v)): s.add((min(v[x],v[y]),max(v[x],v[y])))
        return s
    ce=defaultdict(list)
    for i,p in enumerate(polys): ce[p].append(i)
    # float classes tol 1e-6
    parent=list(range(149))
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for i in range(149):
        for j in range(i+1,149):
            if max(abs(a-b) for a,b in zip(recom[i],recom[j]))<1e-6:
                ri,rj=find(i),find(j)
                if ri!=rj: parent[rj]=ri
    cf=defaultdict(list)
    for i in range(149): cf[find(i)].append(i)
    assert pairs(ce)==pairs(cf), "partition mismatch"
    print(f"[4/5] dual-pipeline partition agrees: {len(ce)} exact classes, {sum(1 for v in ce.values() if len(v)>1)} non-singleton, pairs={len(pairs(ce))}")
    # minimal pair non-iso
    with open(os.path.join(BASE,'minimal_pair.json')) as f: mp=json.load(f)
    a,b=mp['member_a_id'],mp['member_b_id']
    assert polys[a]==polys[b]
    assert max(abs(x-y) for x,y in zip(recom[a],recom[b]))<1e-6
    assert not are_isomorphic(adjs[a],adjs[b])
    print(f"[5/5] minimal pair ({a},{b}) shares poly, spectra agree <1e-6, exhaustive search confirms non-iso")
    print("VERIFY OK")

if __name__=='__main__':
    main()
