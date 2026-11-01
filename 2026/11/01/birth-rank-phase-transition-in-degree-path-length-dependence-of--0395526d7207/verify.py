#!/usr/bin/env python3
"""Exact checks for the finite-sample covariance formula (Python standard library)."""
import itertools
from fractions import Fraction
from math import factorial, log, sqrt

def formula(n,j):
    return Fraction(n,j)-1+sum((Fraction(1,s)-Fraction(n,s*s) for s in range(j,n)),Fraction(0))

def check_exhaustive(n):
    samples=[]
    for parents in itertools.product(*(range(1,t) for t in range(2,n+1))):
        dep=[0]*(n+1)
        child=[0]*(n+1)
        for t,p in enumerate(parents,2):
            dep[t]=dep[p]+1
            child[p]+=1
        samples.append((sum(dep),child))
    den=len(samples)
    mean_t=Fraction(sum(t for t,_ in samples),den)
    checks=0
    for j in range(1,n+1):
        mean_d=Fraction(sum(d[j] for _,d in samples),den)
        mixed=Fraction(sum(t*d[j] for t,d in samples),den)
        assert mixed-mean_t*mean_d==formula(n,j),(n,j)
        checks+=1
    return den,checks

if __name__=='__main__':
    tested=0
    for n in range(3,9):
        configurations,checks=check_exhaustive(n)
        tested+=checks
        print('n=%d histories=%d exact covariance identities=%d'%(n,configurations,checks))
    for n in range(3,501):
        f=[Fraction(0)]*(n+1)
        for j in range(n-1,0,-1):
            f[j]=f[j+1]-Fraction(n-j*(j+1),j*j*(j+1))
        f=f[1:]
        assert f[0]<0 and f[n-2]>0 and f[-1]==0
        assert all(f[j]-f[j-1] == Fraction(n-(j)*(j+1),j*j*(j+1)) for j in range(1,n))
        first=next(j for j in range(1,n) if f[j-1]>0)
        assert all(x<=0 for x in f[:first-1])
        assert all(x>0 for x in f[first-1:n-1])
        tested+=n+3
    print('All exact checks passed:',tested)
