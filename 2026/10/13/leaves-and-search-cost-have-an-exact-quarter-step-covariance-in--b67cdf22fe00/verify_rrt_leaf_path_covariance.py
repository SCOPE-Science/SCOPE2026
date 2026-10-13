#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import factorial

def harmonic(m):
    return sum((Fraction(1,k) for k in range(1,m+1)), Fraction(0))

def enumerate_rrt(n):
    total=sl=sp=sq=sl2=slp=0
    for choices in product(*[range(j) for j in range(1,n)]):
        parent=[None]+list(choices); children=[0]*n; depth=[0]*n
        for j in range(1,n):
            p=parent[j]; children[p]+=1; depth[j]=depth[p]+1
        leaves=[v for v in range(n) if children[v]==0]
        L=len(leaves); P=sum(depth); Q=sum(depth[v] for v in leaves)
        total+=1; sl+=L; sp+=P; sq+=Q; sl2+=L*L; slp+=L*P
    return total,sl,sp,sq,sl2,slp

def run():
    sizes=trees=first=covs=vars_=slopes=0; prev=None
    for n in range(2,11):
        total,sl,sp,sq,sl2,slp=enumerate_rrt(n); assert total==factorial(n-1); trees+=total; sizes+=1
        EL=Fraction(sl,total); EP=Fraction(sp,total); EQ=Fraction(sq,total); H=harmonic(n-1)
        assert EL==Fraction(n,2); assert EP==n*H-(n-1); assert EQ==Fraction(n,2)*H-Fraction(n-2,4); first+=3
        cov=Fraction(slp,total)-EL*EP; assert cov==-Fraction(n-2,4); covs+=1
        if prev is not None: assert cov-prev==-Fraction(1,4)
        prev=cov
        if n>=3:
            varL=Fraction(sl2,total)-EL*EL; assert varL==Fraction(n,12); vars_+=1
            assert cov/varL==-Fraction(3*(n-2),n); slopes+=1
    print(f"VERIFY_OK sizes={sizes} trees={trees} first_moment_checks={first} covariance_checks={covs} leaf_variance_checks={vars_} slope_checks={slopes}")
if __name__=='__main__': run()
