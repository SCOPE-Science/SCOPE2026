#!/usr/bin/env python3
"""Finite stress test for the complete-multipartite spectral-bipartiteness theorem.
Pure Python standard library; this is corroborative, not the infinite proof.
"""
from itertools import combinations_with_replacement
from math import sqrt

TOL=2e-9

def jacobi_eigenvalues(a):
    a=[list(map(float,row)) for row in a]
    n=len(a)
    if n==1: return [a[0][0]]
    for _ in range(100*n*n):
        p=q=0; best=0.0
        for i in range(n):
            for j in range(i+1,n):
                v=abs(a[i][j])
                if v>best:
                    best=v; p=i; q=j
        if best < 1e-13:
            break
        app=a[p][p]; aqq=a[q][q]; apq=a[p][q]
        tau=(aqq-app)/(2.0*apq)
        t=(1.0 if tau>=0 else -1.0)/(abs(tau)+sqrt(1.0+tau*tau))
        c=1.0/sqrt(1.0+t*t); s=t*c
        for k in range(n):
            if k==p or k==q: continue
            akp=a[k][p]; akq=a[k][q]
            a[k][p]=a[p][k]=c*akp-s*akq
            a[k][q]=a[q][k]=s*akp+c*akq
        a[p][p]=c*c*app-2*s*c*apq+s*s*aqq
        a[q][q]=s*s*app+2*s*c*apq+c*c*aqq
        a[p][q]=a[q][p]=0.0
    return sorted((a[i][i] for i in range(n)), reverse=True)

def parts_nondec(total,r,lo=1):
    if r==1:
        if total>=lo: yield (total,)
        return
    for x in range(lo,total//r+1):
        for rest in parts_nondec(total-x,r-1,x):
            yield (x,)+rest

def quotient(parts):
    r=len(parts)
    return [[0.0 if i==j else sqrt(parts[i]*parts[j]) for j in range(r)] for i in range(r)]

parameter_cases=0
partition_cases=0
equality_cases=0
max_abs_error=0.0
for r in range(3,8):
    for N in range(r,19):
        parameter_cases+=1
        seen_eq=0
        for p in parts_nondec(N,r):
            partition_cases+=1
            ev=jacobi_eigenvalues(quotient(p))
            b=ev[0]+ev[-1]
            if b < (r-2)-TOL:
                raise AssertionError((N,r,p,b,r-2))
            is_split=(p[:-1]==(1,)*(r-1))
            is_eq=abs(b-(r-2))<1e-7
            if is_eq != is_split:
                raise AssertionError(("equality",N,r,p,b,is_split))
            if is_eq:
                seen_eq+=1; equality_cases+=1
                L=N-r+1
                disc=(r-2)**2+4*(r-1)*L
                rp=((r-2)+sqrt(disc))/2
                rm=((r-2)-sqrt(disc))/2
                err=max(abs(ev[0]-rp),abs(ev[-1]-rm))
                max_abs_error=max(max_abs_error,err)
        if seen_eq!=1:
            raise AssertionError(("unique split",N,r,seen_eq))
print("ALL CHECKS PASSED; parameter_cases=%d; partition_cases=%d; equality_cases=%d; max_order=18; max_parts=7; max_split_root_error=%.3g" % (parameter_cases,partition_cases,equality_cases,max_abs_error))
