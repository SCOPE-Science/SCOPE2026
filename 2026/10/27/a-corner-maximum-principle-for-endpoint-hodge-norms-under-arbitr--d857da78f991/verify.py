"""Exact-rational checks for endpoint norms under edge-path subdivision.
Only Python's standard library is required; proof of the general theorem is analytic.
"""
from fractions import Fraction as F
from itertools import product
from collections import deque

def inverse(a):
    n=len(a)
    if not n:return []
    A=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None:raise ArithmeticError('singular Gram matrix')
        A[j],A[k]=A[k],A[j]
        z=A[j][j];A[j]=[x/z for x in A[j]]
        for i in range(n):
            if i!=j:
                z=A[i][j]
                if z:A[i]=[u-z*v for u,v in zip(A[i],A[j])]
    return [row[n:] for row in A]

def matmul(a,b):
    if not a:return []
    if not b:return [[] for _ in a]
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a):return list(map(list,zip(*a))) if a else []

def cycle_basis(n,edges):
    m=len(edges);p=list(range(n))
    def root(a):
        while p[a]!=a:a=p[a]
        return a
    forest=[]; chords=[]
    for j,(a,b) in enumerate(edges):
        ra,rb=root(a),root(b)
        if ra!=rb:p[ra]=rb;forest.append(j)
        else:chords.append(j)
    if not chords:return [[ ] for _ in range(m)]
    adj=[[] for _ in range(n)]
    for j in forest:
        a,b=edges[j];adj[a].append((b,j,1));adj[b].append((a,j,-1))
    basis=[]
    for j in chords:
        a,b=edges[j];z=[F(0)]*m;z[j]=F(1)
        todo=deque([b]); prev={b:None}
        while todo and a not in prev:
            v=todo.popleft()
            for w,i,sign in adj[v]:
                if w not in prev:prev[w]=(v,i,sign);todo.append(w)
        v=a
        while v!=b:
            u,i,sign=prev[v];z[i]=F(sign);v=u
        basis.append(z)
    return transpose(basis)

def H_of(n,edges,lengths):
    m=len(edges);B=cycle_basis(n,edges)
    if not B[0]:return [[F(0)]*m for _ in range(m)]
    T=transpose(B);G=[[sum((T[i][h]*F(lengths[h])*B[h][j] for h in range(m)),F(0)) for j in range(len(T))] for i in range(len(T))]
    return matmul(matmul(B,inverse(G)),T)

def norms(n,edges,lengths):
    h=H_of(n,edges,lengths);m=len(edges)
    a=[sum((F(lengths[g])*abs(h[g][f]) for g in range(m)),F(0)) for f in range(m)]
    return max(a,default=F(0)),max((1+a[f]-2*h[f][f] for f in range(m)),default=F(0))

def direct_projection(n,edges):
    # Incidence rank n-1. Ground vertex n-1.
    m=len(edges);D=[[F(0)]*m for _ in range(n-1)]
    for j,(a,b) in enumerate(edges):
        if a<n-1:D[a][j]=F(1)
        if b<n-1:D[b][j]=-F(1)
    DT=transpose(D);L=matmul(D,DT)
    Q=matmul(matmul(DT,inverse(L)),D)
    C=[[F(i==j)-Q[i][j] for j in range(m)] for i in range(m)]
    return max((sum(abs(C[i][j]) for i in range(m)) for j in range(m)),default=F(0)),max((sum(abs(Q[i][j]) for i in range(m)) for j in range(m)),default=F(0))

def expanded(n,edges,r):
    out=[];v=n
    for (a,b),k in zip(edges,r):
        last=a
        for _ in range(k-1):out.append((last,v));last=v;v+=1
        out.append((last,b))
    return v,out

def check():
    graphs=[(3,[(0,1),(1,2),(0,2)]),
            (4,[(0,1),(0,2),(1,2),(0,3),(1,3)]),
            (4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
            (4,[(0,1),(1,2),(2,3),(0,3)]),
            (5,[(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]),
            (5,[(0,1),(1,2),(2,0),(2,3),(3,4)]),
            (6,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,3)])]
    cases=0; interiors=0; corners=0
    for n,edges in graphs:
        m=len(edges)
        tests=[[1]*m,[2]*m,[1+(i%2) for i in range(m)],[1+(i%3) for i in range(m)]]
        for r in tests:
            v,ed=expanded(n,edges,r)
            assert norms(n,edges,r)==direct_projection(v,ed),(n,edges,r)
            cases+=1
        for i in range(m):
            for r0 in tests[:3]:
                vals=[]
                for t in [F(1),F(3,2),F(2),F(5,2),F(3),F(4)]:
                    rr=[F(x) for x in r0];rr[i]=t;vals.append(norms(n,edges,rr))
                for jj in [1,3]:
                    left,right=(0,2) if jj==1 else (2,4)
                    for a in [0,1]:assert vals[jj][a]<=max(vals[left][a],vals[right][a])
                    interiors+=1
        if m<=6:
            allvals=[]
            for r in product([1,2,3],repeat=m):allvals.append((r,norms(n,edges,r)))
            best=[]
            for a in [0,1]:
                endpoint=max(v[a] for r,v in allvals if all(x in (1,3) for x in r))
                assert all(v[a]<=endpoint for r,v in allvals)
                best.append(endpoint)
            corners+=len(allvals)
    n,edges=graphs[1]
    # Shared hub edge is (0,1); the diamond norm dips precisely at k=2.
    for k in range(1,18):
        r=[k,1,1,1,1];C,_=norms(n,edges,r)
        predicted=max(F(k+2,k+1),F(3*k+2,2*(k+1)))
        assert C==predicted,(k,C,predicted)
    assert norms(n,edges,[1]*5)[0]==F(3,2)
    assert norms(n,edges,[2,1,1,1,1])[0]==F(4,3)
    assert norms(n,edges,[3,1,1,1,1])[0]==F(11,8)
    print('PASS direct_projection_cases=%d midpoint_pairs=%d box_instances=%d diamond_lengths=17' %(cases,interiors,corners))

if __name__=='__main__':check()
