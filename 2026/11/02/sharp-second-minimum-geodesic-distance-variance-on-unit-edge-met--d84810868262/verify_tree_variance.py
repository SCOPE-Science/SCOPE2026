#!/usr/bin/env python3
"""Independent finite checks for exact geodesic-distance variance bounds on unit-edge metric trees.
Uses only the Python standard library. Finite checks are not a proof for unbounded tree size.
"""
from collections import deque
from fractions import Fraction as Q
from itertools import product
from random import Random


def edges_from_prufer(seq):
    n = len(seq) + 2
    degree = [1]*n
    for x in seq: degree[x] += 1
    e = []
    for x in seq:
        leaf = min(v for v in range(n) if degree[v] == 1)
        e.append((leaf, x)); degree[leaf] -= 1; degree[x] -= 1
    a,b = [v for v in range(n) if degree[v] == 1]
    e.append((a,b))
    return e


def edge_distances(edges):
    m = len(edges)
    # Build the line graph from edge endpoints, without using the variance theorem.
    adj = [[] for _ in edges]
    for i in range(m):
        for j in range(i+1,m):
            if set(edges[i]) & set(edges[j]):
                adj[i].append(j);adj[j].append(i)
    matrix = [[-1]*m for _ in edges]
    for i in range(m):
        row = matrix[i];row[i]=0
        todo=deque([i])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if row[w]<0: row[w]=row[v]+1;todo.append(w)
    assert all(d>=0 for row in matrix for d in row)
    return matrix


def distance_moments(edges):
    m=len(edges)
    matrix=edge_distances(edges)
    # Direct exact 2-dimensional integration by edge-pair classes.
    # On different edges, the route consists of d_L-1 full intervening edges
    # and two independent Uniform(0,1) terminal portions. On the same edge,
    # the distance is |U-V|, with moments 1/3 and 1/6.
    s1=s2=Q(0)
    for i in range(m):
        for j in range(m):
            d=matrix[i][j]
            if i==j: s1+=Q(1,3);s2+=Q(1,6)
            else: s1+=d;s2+=d*d+Q(1,6)
    mean=s1/(m*m); second=s2/(m*m)
    return mean,second,second-mean*mean,matrix


def predicted(m):
    q=Q(2*(m-2),m*m)
    vs=Q(1,6)+Q(1,3*m)-Q(4,9*m*m)
    return vs, vs+q*(1-q)+Q(4,3*m)*q


def degrees(edges):
    d=[0]*(len(edges)+1)
    for a,b in edges:d[a]+=1;d[b]+=1
    return sorted(d,reverse=True)


def check(edges):
    m=len(edges)
    mean,second,var,mat=distance_moments(edges)
    vs,vq=predicted(m)
    ds=degrees(edges)
    star=(ds[0]==m)
    quasi=(ds[:2]==[m-1,2])
    if star: assert var==vs
    else:
        assert var>=vq, ('lower-bound failure',edges,var,vq)
        assert (var==vq)==quasi, ('equality failure',edges,var,vq,ds)
    # Check the independent nonnegative variance-excess identity.
    b=[int(i!=j) for i in range(m) for j in range(m)]
    z=[mat[i][j]-int(i!=j) for i in range(m) for j in range(m)]
    assert min(z)>=0
    mu=sum(z,Q(0))/len(z)
    vz=sum((Q(x)-mu)**2 for x in z)/len(z)
    assert var-vs == vz+Q(4,3*m)*mu
    return var



def quadrature_check(edges, N=40):
    # Separate direct shortest-route geometry, without the line-graph formula.
    n=len(edges)+1; adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    dv=[]
    for a in range(n):
        row=[-1]*n;row[a]=0;queue=deque([a])
        while queue:
            x=queue.popleft()
            for y in adj[x]:
                if row[y]<0:row[y]=row[x]+1;queue.append(y)
        dv.append(row)
    S1=S2=0.0
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            for h in range(N):
                u=(h+0.5)/N
                for k in range(N):
                    v=(k+0.5)/N
                    if i==j: dist=abs(u-v)
                    else:
                        dist=min(u+dv[a][c]+v, u+dv[a][d]+1-v,
                                 1-u+dv[b][c]+v, 1-u+dv[b][d]+1-v)
                    S1+=dist;S2+=dist*dist
    w=1.0/(len(edges)**2*N**2); vq=S2*w-(S1*w)**2
    exact=distance_moments(edges)[2]
    assert abs(vq-float(exact))<0.002,(edges,vq,exact)


def run():
    total=0
    for n in range(4,8):
        minimum_nonstar=None
        star_count=0
        quasi_count=0
        for s in product(range(n),repeat=n-2):
            e=edges_from_prufer(s)
            v=check(e)
            d=degrees(e)
            if d[0]==n-1:star_count+=1
            else:
                if minimum_nonstar is None or v<minimum_nonstar: minimum_nonstar=v
            if d[:2]==[n-2,2]:quasi_count+=1
            total+=1
        m=n-1
        assert minimum_nonstar==predicted(m)[1]
        assert star_count>0 and quasi_count>0
    rng=Random(22122026)
    for n in range(8,21):
        for j in range(100):
            check(edges_from_prufer(tuple(rng.randrange(n) for _ in range(n-2))))
            total+=1
    # Independent shortest-route midpoint quadrature on four geometries.
    examples=[[(0,1),(0,2),(0,3)],
              [(0,1),(0,2),(0,3),(3,4)],
              [(j,j+1) for j in range(7)],
              edges_from_prufer((1,3,1,5,3))]
    for edges in examples:quadrature_check(edges)
    print(f'VERIFY_OK {total} exact Prüfer-coded trees plus four direct shortest-route quadratures; n=4..7 exhaustive, n=8..20 seeded samples')

if __name__=='__main__':run()
