#!/usr/bin/env python3
"""Exact and asymptotic checks for layered-poset order-polytope covariance."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial, lgamma, log, exp, pi, sqrt


def covariance_formula(sizes):
    n=sum(sizes)
    groups=[]; start=1
    for size in sizes:
        groups.append(list(range(start,start+size)))
        start+=size
    def second(r,s):
        return F(min(r,s)*(max(r,s)+1),(n+1)*(n+2))
    def means(g):
        return sum((F(r,n+1) for r in g),F())/len(g)
    C=[]
    for i in range(n):
        row=[]
        # rank distributions: labels are sequential groups; assignments uniform within group
        gi=next(g for g in groups if i < sum(sizes[:groups.index(g)+1]))
        for j in range(n):
            gj=next(g for g in groups if j < sum(sizes[:groups.index(g)+1]))
            if i==j:
                m2=sum((second(r,r) for r in gi),F())/len(gi)
            elif gi==gj:
                m2=sum((second(r,s) for r in gi for s in gi if r!=s),F())/(len(gi)*(len(gi)-1))
            else:
                m2=sum((second(r,s) for r in gi for s in gj),F())/(len(gi)*len(gj))
            row.append(m2-means(gi)*means(gj))
        C.append(row)
    return C


def covariance_independent(sizes):
    n=sum(sizes)
    bounds=[]; a=0
    for s in sizes: bounds.append((a,a+s)); a+=s
    valid=[]
    for perm in permutations(range(1,n+1)):
        if all(set(perm[lo:hi])==set(range(lo+1,hi+1)) for lo,hi in bounds):
            valid.append(perm)
    assert len(valid)==__import__('math').prod(factorial(x) for x in sizes)
    means=[F() for _ in range(n)]; m2=[[F() for _ in range(n)] for _ in range(n)]
    for perm in valid:
        for i in range(n):
            means[i]+=F(perm[i],n+1)
            for j in range(n):
                r,s=perm[i],perm[j]
                m2[i][j]+=F(min(r,s)*(max(r,s)+1),(n+1)*(n+2))
    count=len(valid)
    means=[x/count for x in means]
    return [[m2[i][j]/count-means[i]*means[j] for j in range(n)] for i in range(n)]


def det(M):
    A=[list(row) for row in M]; n=len(A); ans=F(1)
    for i in range(n):
        piv=next((r for r in range(i,n) if A[r][i]),None)
        if piv is None:return F(0)
        if piv!=i:A[i],A[piv]=A[piv],A[i];ans=-ans
        v=A[i][i];ans*=v
        for j in range(i+1,n):
            coeff=A[j][i]/v
            for k in range(i,n): A[j][k]-=coeff*A[i][k]
    return ans


def compact_det(sizes):
    n=sum(sizes)
    C=covariance_formula(sizes)
    # block group means covariance with rational normalization:
    # det B = prod n_i * det Cov(group averages).
    a=0; means=[]
    for s in sizes:
        means.append(tuple(range(a,a+s))); a+=s
    B=[[sum((C[r][s] for r in G for s in H),F())/(len(G)*len(H)) for H in means] for G in means]
    value=det(B)
    for s in sizes:value*=s
    for s in sizes:
        if s>1: value*=F((s+1)*(s+2),12*(n+1)*(n+2))**(s-1)
    return value


def two_layer_det(p,q):
    n=p+q
    t=F((p+1)*(q+1)*(2*p*q+n+2),72*(n+1)**2*(n+2)**2)
    return t*F((p+1)*(p+2),12*(n+1)*(n+2))**(p-1)*F((q+1)*(q+2),12*(n+1)*(n+2))**(q-1)


def isotropic_log12(sizes):
    n=sum(sizes)
    if len(sizes)!=2:raise ValueError('use two-layer exact formula here')
    p,q=sizes
    t=(p+1)*(q+1)*(2*p*q+n+2)/(72*(n+1)**2*(n+2)**2)
    a=(p+1)*(p+2)/(12*(n+1)*(n+2))
    b=(q+1)*(q+2)/(12*(n+1)*(n+2))
    log_det=(p-1)*log(a)+(q-1)*log(b)+log(t)
    logvol=lgamma(p+1)+lgamma(q+1)-lgamma(n+1)
    return log(12)+(log_det-2*logvol)/n

checks=0
for sizes in [(1,1),(1,2),(2,1),(2,2),(3,2),(2,3),(1,1,2),(2,1,2),(1,2,1),(2,2,2),(1,1,1,2)]:
    A=covariance_formula(sizes)
    B=covariance_independent(sizes)
    assert A==B, (sizes,'moment mismatch')
    assert det(A)==compact_det(sizes),(sizes,'det mismatch')
    if len(sizes)==2:
        assert det(A)==two_layer_det(*sizes),(sizes,'2-level det mismatch')
    checks+=1

for p,q in [(5,5),(10,10),(50,50),(200,200),(1000,1000),(5,45),(10,90),(50,450),(200,1800)]:
    n=p+q; a=p/n;b=q/n
    offset=n*isotropic_log12((p,q))+log(n)
    predicted=3+log(2/(pi*a*b))
    print(f'asymptotic n={n} parts={p},{q} observed_constant={offset:.9f} limiting_constant={predicted:.9f} discrepancy={offset-predicted:.9f}')
    if n>=400:assert abs(offset-predicted)<0.20
    checks+=1
print('CHECK_OK',checks)

def det_float(M):
    A=[list(map(float,r)) for r in M];m=len(A);ans=1.
    for i in range(m):
        v=A[i][i];ans*=v
        for j in range(i+1,m):
            c=A[j][i]/v
            for t in range(i,m):A[j][t]-=c*A[i][t]
    return ans


def group_mean_gram(sizes):
    n=sum(sizes);coeff=[];lo=0
    for s in sizes:
        hi=lo+s
        coeff.append([1. if t<=lo else (hi-t+1)/s if t<=hi else 0. for t in range(1,n+2)])
        lo=hi
    D=(n+1)**2*(n+2)
    sums=list(map(sum,coeff))
    return [[sqrt(sizes[i]*sizes[j])*((n+1)*sum(x*y for x,y in zip(coeff[i],coeff[j]))-sums[i]*sums[j])/D for j in range(len(sizes))] for i in range(len(sizes))]


def asymptotic_C(alphas):
    starts=[];x=0
    for a in alphas: starts.append(x);x+=a
    mus=[x+a/2 for x,a in zip(starts,alphas)]
    return [[sqrt(alphas[i]*alphas[j])*(mus[min(i,j)]*(1-mus[max(i,j)])-(alphas[i]/6 if i==j else 0)) for j in range(len(alphas))] for i in range(len(alphas))]


def log_12L2_general(sizes):
    n=sum(sizes);B=group_mean_gram(sizes)
    ldet=log(det_float(B))
    for s in sizes:
        ldet+=(s-1)*log((s+1)*(s+2)/(12*(n+1)*(n+2)))
    lvol=sum(lgamma(s+1) for s in sizes)-lgamma(n+1)
    return log(12)+(ldet-2*lvol)/n

for sizes in [(3,4,5),(20,30,50),(100,150,250),(500,750,1250),(5,8,9,10),(40,60,90,110),(80,120,180,220)]:
    n=sum(sizes);k=len(sizes);alpha=[x/n for x in sizes]
    C=asymptotic_C(alpha)
    assert det_float(C)>0
    asym=3*(k-1)-(k-1)*log(2*pi)+k*log(12)+log(det_float(C))-3*sum(map(log,alpha))
    obs=n*log_12L2_general(sizes)+(k-1)*log(n)
    print(f'layers={sizes} observed={obs:.9f} predicted={asym:.9f} residual={obs-asym:.9f}')
    if n>400: assert abs(obs-asym)<0.4
    checks+=1
print('CHECK_OK_MULTILAYER',checks)
