"""Exact finite spot checks for the finite-metric bounded-Lipschitz extreme-point criterion.
Publicly reproducible; no external dependencies or services.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from collections import deque
import random


def q(x):
    return Q(str(x))


def norm_data(f, d):
    n=len(f)
    a=max(map(abs, f))
    ell=max(abs(f[i]-f[j])/d[i][j] for i,j in combinations(range(n), 2)) if n>1 else Q(0)
    return a,ell


def rank(A):
    A=[list(map(Q,row)) for row in A]
    if not A:return 0
    n=len(A[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        v=A[r][c]; A[r]=[x/v for x in A[r]]
        for i in range(r+1,len(A)):
            if A[i][c]:
                v=A[i][c]
                A[i]=[x-v*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==n:break
    return r


def result(f,d):
    n=len(f)
    a,L=norm_data(f,d)
    if a+L != 1:raise ValueError('normalize first')
    if not L:
        return all(x==1 for x in f) or all(x==-1 for x in f),n,n
    anchors=[(i,1 if f[i]>0 else -1) for i in range(n) if abs(f[i])==a]
    edges=[(i,j) for i,j in combinations(range(n),2) if abs(f[i]-f[j])==L*d[i][j]]
    g=[[] for _ in range(n)]
    for i,j in edges:g[i].append(j);g[j].append(i)
    comp=[-1]*n
    for v in range(n):
        if comp[v]!=-1:continue
        k=v
        z=len({c for c in comp if c!=-1})
        comp[v]=z
        stack=[v]
        while stack:
            p=stack.pop()
            for w in g[p]:
                if comp[w]==-1:comp[w]=z;stack.append(w)
    ac={c:set() for c in comp}
    for i,s in anchors:ac[comp[i]].add(s)
    graph_face_dim=sum(not bool(v) for v in ac.values())+int(not any(v=={-1,1} for v in ac.values()))
    graph_answer=(graph_face_dim==0)
    # Independently construct all active product-facet normals and compute their rank.
    rows=[]
    for i,s in anchors:
        for u,v in edges:
            if f[u]<f[v]:u,v=v,u
            row=[Q(0)]*n
            row[i]+=s;row[u]+=1/d[u][v];row[v]-=1/d[u][v]
            rows.append(row)
    linear_face_dim=n-rank(rows)
    if graph_face_dim != linear_face_dim:
        raise AssertionError(('mismatch',f,d,graph_face_dim,linear_face_dim,edges,ac))
    return graph_answer, graph_face_dim,len(anchors)


def metric_line(values):
    return [[abs(x-y) for y in values] for x in values]


def metric_random(n,rng):
    # Shortest-path metrics of connected weighted random graphs.
    d=[[Q(0) if i==j else Q(999) for j in range(n)] for i in range(n)]
    for i in range(n-1):
        d[i][i+1]=d[i+1][i]=Q(rng.randrange(1,5))
    for i,j in combinations(range(n),2):
        if rng.randrange(3)==0:
            d[i][j]=d[j][i]=min(d[i][j],Q(rng.randrange(1,6)))
    for k in range(n):
        for i in range(n):
            for j in range(n): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d


def main():
    expected=[
        (['0','3/2','5/2','4'], ['1/2','-1/4','1/4','-1/2'], True),
        (['0','3/2','2','4'], ['1/2','-1/4','0','-1/2'], False),
    ]
    tests=0; positives=0
    for points, values, want in expected:
        d=metric_line([Q(x) for x in points]);f=[Q(x) for x in values]
        got,*_=result(f,d)
        assert got==want,(got,want)
        print('Hille--Theewis finite example:',points,got,'expected',want)
        tests+=1;positives+=got
    for n in (2,3,4,5,6):
        p=list(map(Q,range(n)))
        d=metric_line(p)
        L=Q(2,n+1); a=1-L
        f=[-a+L*t for t in p]
        got,*_=result(f,d)
        assert got
        tests+=1;positives+=1
    rng=random.Random(467219)
    for n in (2,3,4,5,6):
        for t in range(10):
            d=metric_random(n,rng)
            for vec in product((-2,-1,0,1,2),repeat=n):
                if not any(vec):continue
                # bounded sample n<=4 exhaustive; n>4 bounded first 2000
                if n>4 and (tests%23 == 0): pass
                f=list(map(Q,vec));a,L=norm_data(f,d)
                f=[x/(a+L) for x in f]
                got,*_=result(f,d)
                tests+=1;positives+=got
                if n>=5 and tests%2000==0:break
    print('PASS exact minimal-face dimension versus tight-component formula')
    print('tested_boundary_configurations',tests,'classified_extreme',positives)

if __name__=='__main__':main()
