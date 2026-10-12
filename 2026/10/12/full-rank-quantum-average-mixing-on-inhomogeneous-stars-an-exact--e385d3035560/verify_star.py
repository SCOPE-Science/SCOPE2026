#!/usr/bin/env python3
"""Independent spectral and exact-arithmetic checks for weighted-star Cesàro mixing."""
from fractions import Fraction
from random import Random
import numpy as np
from scipy.linalg import eigh

rng=Random(40519)
exact_cases=0; numeric_cases=0; entries=0; max_error=0.0

def formula(gs,delta):
    a=np.array(gs,dtype=float); w=(a*a)/float(a@a)
    s=float(a@a)/(delta*delta+4*float(a@a)); m=len(gs)
    M=np.zeros((m+1,m+1),dtype=float)
    M[0,0]=1-2*s
    M[0,1:]=M[1:,0]=2*s*w
    M[1:,1:]=np.diag(1-2*w)+2*(1-s)*np.outer(w,w)
    return M

def exact_rank(mat):
    a=[list(x) for x in mat]; n=len(a); rank=0
    for col in range(n):
        piv=next((i for i in range(rank,n) if a[i][col]),None)
        if piv is None:continue
        a[rank],a[piv]=a[piv],a[rank]
        v=a[rank][col]
        for j in range(col,n):a[rank][j]/=v
        for i in range(n):
            if i==rank:continue
            v=a[i][col]
            if v:
                for j in range(col,n):a[i][j]-=v*a[rank][j]
        rank+=1
    return rank

def exact_formula(gs,delta):
    gg=sum(x*x for x in gs); w=[Fraction(x*x,gg) for x in gs]
    s=Fraction(gg,delta*delta+4*gg); n=len(gs)+1
    M=[[Fraction(0) for _ in range(n)]for _ in range(n)]
    M[0][0]=1-2*s
    for i in range(n-1):
        M[0][i+1]=M[i+1][0]=2*s*w[i]
        for j in range(n-1):
            M[i+1][j+1]=(Fraction(1-2*w[i]) if i==j else Fraction(0)) +2*(1-s)*w[i]*w[j]
    return M

for m in range(1,10):
    for z in range(45):
        gs=[rng.randint(1,7) for _ in range(m)]; delta=rng.randint(-8,8)
        A=np.zeros((m+1,m+1),dtype=float); A[0,0]=delta;A[0,1:]=A[1:,0]=gs
        eig,V=eigh(A)
        M=np.zeros_like(A)
        groups=[]
        for i,l in enumerate(eig):
            if groups and abs(l-groups[-1][0])<1e-9:groups[-1][1].append(i)
            else:groups.append([l,[i]])
        for _,ix in groups:
            E=V[:,ix]@V[:,ix].T
            M+=E*E
        F=formula(gs,delta)
        err=float(np.max(np.abs(M-F)));max_error=max(max_error,err)
        assert err<3e-12, (m,gs,delta,err)
        entries+=(m+1)**2;numeric_cases+=1
        if m<=7:
            ex=exact_formula(gs,delta)
            rank=exact_rank(ex)
            expected=(2 if delta!=0 else 1) if m==1 else ((3 if delta!=0 and gs[0]!=gs[1] else 2) if m==2 else m+1)
            assert rank==expected, (m,gs,delta,rank,expected)
            exact_cases+=1
            assert abs(float(sum(ex[0]))-1)<1e-12
print(f'VERIFY_OK exact_rank_profiles={exact_cases} independent_spectral_profiles={numeric_cases} matrix_entries={entries} max_entry_error={max_error:.3e}')
