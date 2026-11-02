#!/usr/bin/env python3
"""Stand-alone checks for exact noisy-voter windmill correlations.

Python standard library only. The finite-state check constructs the one-site
update Markov chain independently of the reduced three-equation calculation.
"""
from fractions import Fraction as F
from itertools import product

assertions=0

def ok(c, detail=''):
    global assertions
    assertions+=1
    if not c: raise AssertionError(detail)

def formula(n,m,p):
    s=1-p
    a=s/(2+p*(m-2))
    b=s/(1+p*(m-1))
    A=F(1,m)+(1+(m-1)*a)/(n*m)
    B=F(m-1,m)+F(m-1,n*m)*a+F(n-1,n)*b
    u=s*A/(2-s*B)
    return (u,a*(1+u),b*u)

def solve(A,b):
    n=len(b)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        j=next(i for i in range(k,n) if M[i][k]!=0)
        M[k],M[j]=M[j],M[k]
        v=M[k][k]
        M[k]=[x/v for x in M[k]]
        for i in range(n):
            if i!=k:
                v=M[i][k]
                M[i]=[a-v*c for a,c in zip(M[i],M[k])]
    return [M[i][-1] for i in range(n)]

def independent_moments(n,m,p):
    s=1-p
    # Direct exact pair-balance equations, separately from the closed formula.
    # u: centered hub / rim, v: two different rims in one clique,
    # w: rims from two different cliques.
    M=[
        [2-s*F(m-1,m),-s*F(m-1,n*m),-s*F(n-1,n)],
        [-s,F(m)-s*(m-2),F(0)],
        [-s,F(0),F(m)-s*(m-1)]
    ]
    z=[s*(F(1,n*m)+F(1,m)),s,F(0)]
    return tuple(solve(M,z))

def full_chain(n,m,p):
    N=1+n*m
    ok(N<=7)
    adj=[list(range(1,N))]
    for i in range(n):
        for j in range(m):
            adj.append([0]+[1+i*m+k for k in range(m) if k!=j])
    T={}
    s=float(1-p)
    for mask in range(1<<N):
        transitions={mask:0.0}
        for i in range(N):
            z=sum(bool(mask&(1<<v)) for v in adj[i])
            prob_1=(float(p)/2+s*z/len(adj[i]))/N
            prob_0=1.0/N-prob_1
            m1=mask|(1<<i)
            m0=mask&~(1<<i)
            transitions[m1]=transitions.get(m1,0)+prob_1
            transitions[m0]=transitions.get(m0,0)+prob_0
        T[mask]=[(y,v) for y,v in transitions.items() if v]
    a=[0.0]*(1<<N);a[0]=1.0
    for _ in range(2500):
        b=[0.0]*(1<<N)
        for x,t in enumerate(a):
            if t:
                for y,v in T[x]: b[y]+=t*v
        if sum(abs(a[i]-b[i]) for i in range(len(a)))<1e-14:
            a=b;break
        a=b
    ok(abs(sum(a)-1)<1e-10)
    pairs=[(0,1),(1,2),(1,1+m)]
    return tuple(sum(t*((1 if mask & (1<<i) else -1)*(1 if mask & (1<<j) else -1)) for mask,t in enumerate(a)) for i,j in pairs)

for n,m,p in product(range(2,8),range(2,7),[F(1,10),F(1,4),F(2,5),F(3,4),F(9,10)]):
    u,v,w=formula(n,m,p)
    u2,v2,w2=independent_moments(n,m,p)
    ok((u,v,w)==(u2,v2,w2),(n,m,p,'moment equations'))
    ok(1>v>u>w>0,(n,m,p,'strict hierarchy'))
    b=(1-p)/(1+p*(m-1))
    ok(v-u==(1-(1-p)/(2+p*(m-2)))*(b-u),(n,m,p,'gap identity'))

for n,m,p in [(2,2,F(1,4)),(2,2,F(1,2)),(2,3,F(1,3)),(3,2,F(2,5))]:
    values=full_chain(n,m,p)
    expect=formula(n,m,p)
    for x,y in zip(values,expect):ok(abs(x-float(y))<2e-10,(n,m,p,x,y))

for m in [200,1000,5000]:
    n=m
    for lam in [F(1,2),F(2),F(5)]:
        u,v,w=formula(n,m,lam/(m*m))
        U=F(3)/(3+2*lam)
        V=(F(3)+lam)/(3+2*lam)
        ok(abs(float(u-U))<2/m)
        ok(abs(float(v-V))<2/m)
        ok(abs(float(w-U))<3/m)
    u,v,w=formula(n,m,F(2,m))
    ok(abs(float(v)-F(1,4))<3/m)
    ok(float(u)<4/m and float(w)<4/m)

for m in [2000,10000,40000]:
    n=m
    p=F(1,m)*F(1,int(m**0.5))
    u,v,w=formula(n,m,p)
    ok(float(u)<5/m**0.5)
    ok(abs(float(v)-0.5)<5/m**0.5)
    ok(float(w)<5/m**0.5)

print('VERIFY_OK',assertions)
