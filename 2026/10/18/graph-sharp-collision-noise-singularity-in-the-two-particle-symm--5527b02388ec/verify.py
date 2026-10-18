"""Exact finite-generator checks for a two-particle symmetric inclusion process.
Python 3 standard library only. This program checks finite witnesses; the theorem
for arbitrary graphs is established by the separate analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import isclose

def solve(A,b):
    n=len(b)
    M=[list(map(F,A[i]))+[F(b[i])] for i in range(n)]
    for j in range(n):
        pivot=next(k for k in range(j,n) if M[k][j])
        M[j],M[pivot]=M[pivot],M[j]
        q=M[j][j]
        M[j]=[v/q for v in M[j]]
        for i in range(n):
            if i!=j and M[i][j]:
                q=M[i][j]
                M[i]=[x-q*y for x,y in zip(M[i],M[j])]
    return [row[-1] for row in M]

def gen(n, edges, a):
    e={tuple(sorted(x)) for x in edges}
    ss=list(combinations_with_replacement(range(n),2))
    ids={pair:i for i,pair in enumerate(ss)}
    Q=[[F(0) for _ in ss] for _ in ss]
    for i, (x,y) in enumerate(ss):
        occ={x:1,y:1} if x!=y else {x:2}
        for u, nu in occ.items():
            for v in range(n):
                if (min(u,v),max(u,v)) not in e: continue
                rate=nu*(a+occ.get(v,0))
                new=dict(occ);new[u]-=1;new[v]=new.get(v,0)+1
                pair=tuple(sorted(k for k,t in new.items() for _ in range(t)))
                Q[i][ids[pair]]+=rate
        Q[i][i]=-sum(Q[i])
    pi=[(a+1)/(n*(n*a+1)) if x==y else 2*a/(n*(n*a+1)) for x,y in ss]
    return Q,pi,ss

def Vexact(n, edges, a):
    Q,pi,ss=gen(n,edges,a)
    for j in range(len(ss)):
        assert sum(pi[i]*Q[i][j] for i in range(len(ss)))==0
    p=(a+1)/(n*a+1)
    f=[F(int(x==y))-p for x,y in ss]
    M=[[-Q[i][j]+pi[j] for j in range(len(ss))] for i in range(len(ss))]
    h=solve(M,f)
    assert sum(pi[i]*h[i] for i in range(len(ss)))==0
    return sum(pi[i]*f[i]*h[i] for i in range(len(ss)))

def killed_green(n, edges):
    edge={tuple(sorted(x)) for x in edges}
    non=[pair for pair in combinations(range(n),2) if pair not in edge]
    if not non: return F(0)
    ids={pair:i for i,pair in enumerate(non)}
    K=[[F(0) for j in non] for i in non]
    for i,(x,y) in enumerate(non):
        for u,w in ((x,y),(y,x)):
            for v in range(n):
                if (min(u,v),max(u,v)) not in edge:continue
                pair=tuple(sorted((v,w)))
                K[i][i]-=1
                if pair in ids:K[i][ids[pair]]+=1
    g=solve([[-K[i][j] for j in range(len(non))] for i in range(len(non))],[F(1)]*len(non))
    assert all(x>0 for x in g)
    return F(2,n)*sum(g)

def cycle(n):return [(i,(i+1)%n) for i in range(n)]
def complete(n):return list(combinations(range(n),2))
def path(n):return [(i,i+1) for i in range(n-1)]
def star(n):return [(0,i) for i in range(1,n)]
def exact_cycle(n,a):
    return (a+1)*(n*(n*n-1)*a+(n-1)*(n-2)*(n-3))/(24*(n*a+1)**3)
def exact_complete(n,a):
    return F(n-1)*a*(a+1)/(2*(n*a+1)**3)

checks=0
for n in range(3,8):
    for a in (F(1,5),F(3,2)):
        result=Vexact(n,cycle(n),a)
        assert result==exact_cycle(n,a),(n,a,result)
        checks+=1
for n in range(3,7):
    for a in (F(1,7),F(2,3)):
        result=Vexact(n,complete(n),a)
        assert result==exact_complete(n,a),(n,a,result)
        checks+=1
for n in (3,4,5):
    for graph in (path(n),cycle(n),complete(n),star(n)):
        limit=killed_green(n,graph)
        for a in (F(1,10000),F(1,20000)):
            v=Vexact(n,graph,a)
            assert abs(float(v-limit))<0.008,(n,graph,a,v,limit)
            checks+=1
print('PASS:',checks,'full-generator exact-rational and singular-limit tests')
print('P4 zero-diffusivity integrated-covariance limit:',killed_green(4,path(4)))
print('C4 zero-diffusivity integrated-covariance limit:',killed_green(4,cycle(4)))
print('K4 zero-diffusivity integrated-covariance limit:',killed_green(4,complete(4)))
