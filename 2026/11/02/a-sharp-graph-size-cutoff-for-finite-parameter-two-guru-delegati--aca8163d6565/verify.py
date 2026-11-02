"""Exact-rational checks of two-sink ranked-delegation absorption.

Usage: python3 check_ranked_delegation.py
No external Python dependencies.
"""
from fractions import Fraction as F
from random import Random


def solve(a, b):
    n = len(b)
    a = [[F(v) for v in row] for row in a]
    b = [F(v) for v in b]
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        b[k], b[pivot] = b[pivot], b[k]
        c = a[k][k]
        a[k] = [z/c for z in a[k]]
        b[k] /= c
        for i in range(n):
            if i != k:
                c = a[i][k]
                if c:
                    a[i] = [z-c*t for z,t in zip(a[i],a[k])]
                    b[i] -= c*b[k]
    return b


def adjacency(n, edges):
    neigh = [set() for _ in range(n)]
    for u,v in edges:
        assert u!=v
        neigh[u].add(v)
        neigh[v].add(u)
    return neigh


def independent_absorption(neigh, u, v, eps):
    n=len(neigh)
    a=[[F(0) for _ in range(n)] for _ in range(n)]
    b=[F(0) for _ in range(n)]
    alpha=eps
    beta=eps**2
    for x in range(n):
        a[x][x] = len(neigh[x])+(alpha if x==u else 0)+(beta if x==v else 0)
        for y in neigh[x]:a[x][y]-=1
        if x==u:b[x]=alpha
    return solve(a,b)


def grounded_voltage(neigh,u,v):
    n=len(neigh)
    idx=[x for x in range(n) if x!=v]
    a=[];b=[]
    for x in idx:
        a.append([(len(neigh[x]) if x==y else -int(y in neigh[x])) for y in idx])
        b.append(int(x==u))
    result=solve(a,b)
    g=[F(0)]*n
    for x,t in zip(idx,result):g[x]=t
    return g


def check_instance(neigh, u, v, eps):
    direct=independent_absorption(neigh,u,v,eps)
    g=grounded_voltage(neigh,u,v)
    R=g[u]
    asserted=[(1+eps**2*t)/(1+eps+eps**2*R) for t in g]
    assert direct==asserted, (neigh,u,v,eps,direct,asserted)
    assert min(g)==0 and max(g)==R
    assert max(1-h for h in direct)==(eps+eps**2*R)/(1+eps+eps**2*R)
    n=len(neigh)
    assert R<=n-1
    return 1


def broom(L,K):
    n=L+1+K
    return adjacency(n, [(i,i+1) for i in range(L)]+[(L,L+1+j) for j in range(K)])


def run():
    rng=Random(30619)
    k=0
    for n in range(2,10):
        for _ in range(35):
            edges=set()
            for i in range(1,n):
                j=rng.randrange(i)
                edges.add((j,i))
            for i in range(n):
                for j in range(i+1,n):
                    if rng.randrange(4)==0:edges.add((i,j))
            ng=adjacency(n,edges)
            u,v=rng.sample(range(n),2)
            for eps in [F(1,2),F(1,3),F(1,7)]:
                k+=check_instance(ng,u,v,eps)
    assert k==840
    for N in range(2,15):
        ng=adjacency(N,[(i,i+1) for i in range(N-1)])
        g=grounded_voltage(ng,0,N-1)
        assert g[0]==N-1
        for eps in [F(1,2),F(1,5)]:
            h=independent_absorption(ng,0,N-1,eps)
            assert 1-h[-1]==(eps+eps**2*(N-1))/(1+eps+eps**2*(N-1))
    ng=broom(8,4)
    a=sum(independent_absorption(ng,0,8,F(1,2)))+1
    b=len(ng)+2-a
    assert (a,b)==(F(51,7),F(54,7)),(a,b)
    for m in [2,3,4,5,8,10,20,50]:
        eps=F(1,m)
        L=4*m*m
        N=2*L+1
        total=F(N)+eps**2*F(L*(L+1),2)
        total/= 1+eps+eps**2*L
        a=1+total
        b=N+2-a
        assert b>a
        print('m=%d L=%d A_share=%s B_share=%s' %(m,L,str(a/F(N+2)),str(b/F(N+2))))
    print('PASS: %d exact two-sink graph/parameter comparisons; sharp path bound, finite broom and eight large broom formula checks.' %k)

if __name__=='__main__':run()
