#!/usr/bin/env python3
"""Finite exact and numerical checks for complete-pair-complement semigroups.
Only Python's standard library is required. Finite checks supplement the proof.
"""
from fractions import Fraction as F
import math

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def matpow(A,k):
    n=len(A); res=[[F(i==j) for j in range(n)] for i in range(n)]
    for _ in range(k):res=matmul(res,A)
    return res

def kernel(n,s,t,i,j):
    a=math.exp(-t*(n-2)**s)
    b=math.exp(-t*n**s)
    return (1-b)/n + ((a+b)/2 if i==j else (-a+b)/2 if j==(i^1) else 0)

def exp_taylor(A):
    n=len(A); ans=[[float(i==j) for j in range(n)] for i in range(n)]
    term=[[float(i==j) for j in range(n)] for i in range(n)]
    for k in range(1,55):
        term=matmul(term,A)
        for i in range(n):
            for j in range(n):
                term[i][j]/=k
                ans[i][j]+=term[i][j]
    return ans

for n in range(4,18,2):
    J=[[F(1) for j in range(n)] for i in range(n)]
    I=[[F(i==j) for j in range(n)] for i in range(n)]
    R=[[F(j==(i^1)) for j in range(n)] for i in range(n)]
    L=[[(n-1)*I[i][j]-J[i][j]+R[i][j] for j in range(n)] for i in range(n)]
    P0=[[F(1,n) for j in range(n)] for i in range(n)]
    Pm=[[(I[i][j]-R[i][j])/2 for j in range(n)] for i in range(n)]
    Pp=[[(I[i][j]+R[i][j])/2-P0[i][j] for j in range(n)] for i in range(n)]
    for Q,lmb in [(P0,0),(Pm,n-2),(Pp,n)]:
        QQ=matmul(Q,Q); LQ=matmul(L,Q)
        for i in range(n):
            for j in range(n):
                check(QQ[i][j]==Q[i][j],f'idempotent {n}')
                check(LQ[i][j]==lmb*Q[i][j],f'spectral {n}')
    for k in (1,2,3):
        Lk=matpow(L,k)
        for u in (0.05,0.2,0.5,1.0):
            t=u/n**k
            e=exp_taylor([[-float(Lk[i][j])*t for j in range(n)] for i in range(n)])
            for i in range(n):
                for j in range(n):
                    check(abs(e[i][j]-kernel(n,k,t,i,j))<3e-12,('exp',n,k,u,i,j,e[i][j],kernel(n,k,t,i,j)))
    for s in (.25,.75,1.0,1.01,1.1,1.5,2.0,3.5,5.0):
        for u in (.00001,.01,.2,.6,1.2,3,10):
            t=u/n**s
            M=[[kernel(n,s,t,i,j) for j in range(n)] for i in range(n)]
            a=math.exp(-t*(n-2)**s); b=math.exp(-t*n**s)
            FF=n*a-(n-2)*b-2
            predicted=1+max(0,FF)/n
            for i in range(n):
                check(abs(sum(M[i])-1)<3e-14,('rowsum',n,s,u))
                check(abs(sum(abs(x) for x in M[i])-predicted)<3e-14,('endpoint',n,s,u))
                for j in range(n):
                    if j!=(i^1):check(M[i][j]>=-1e-14,('other negative',n,s,u))
            if s<=1:
                check(FF<=1e-10,('subordination',n,s,u))
            if s>1:
                D=n**s-(n-2)**s
                tstar=(s-1)*math.log(n/(n-2))/D
                astar=math.exp(-(n-2)**s*tstar)
                peak=n*(1-((n-2)/n)**s)*astar-2
                check(peak>0,('peak',n,s))
                check(FF<=peak+1e-10,('peak bound',n,s,u))
                check(tstar>0,('positive time',n,s))
for n in (4,6,12,30,100,1000):
    for s in (1.25,2,3,5):
        q=n/(n-2); d=n**s-(n-2)**s
        tstar=(s-1)*math.log(q)/d
        F=lambda t:n*math.exp(-(n-2)**s*t)-(n-2)*math.exp(-n**s*t)-2
        lo=tstar; hi=max(10*tstar,10/n**s)
        while F(hi)>0:hi*=2
        for _ in range(65):
            mid=(lo+hi)/2
            if F(mid)>0:lo=mid
            else:hi=mid
        root=(lo+hi)/2
        check(root>tstar and abs(F(root))<1e-9,('root',n,s))
        if n>=100:
            asympt=2*(s*math.exp(-(s-1)/s)-1)
            peak=n*(1-q**(-s))*math.exp(-(n-2)**s*tstar)-2
            check(abs(peak-asympt)<0.15,('limit',n,s,peak,asympt))
print('PASS:',checks,'assertions')
