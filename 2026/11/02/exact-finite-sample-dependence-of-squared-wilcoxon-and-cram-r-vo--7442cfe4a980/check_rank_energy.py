#!/usr/bin/env python3
"""Exact, finite tests of rank-area/CvM mixed-moment identities.
Scientific claims and derivations are contained in RESULT.md; tests are diagnostics.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def formulas(a,b):
    N=a+b; h=a*b
    mean_w2=F(h*(N+1),12)
    # E T = (N+1)/(6*N), because Var of S_t = a*b*t*(N-t)/(N-1)
    mean_t=F(N+1,6*N)
    cov=F((N+1)*(h*(3*N+4)-N*(2*N+1)),180*N)
    var_w2=F(h*(N+1)*(h*(5*N+8)-3*N*(N+1)),360)
    var_t=F((N+1)*(h*(4*N+4)-3*N*N),180*h*N*N)
    return mean_w2, mean_t, cov, var_w2, var_t


def enumeration(a,b):
    N=a+b; total=comb(N,a)
    w2s=[];ts=[]
    for inds in combinations(range(1,N+1),a):
        W=F(sum(inds))-F(a*(N+1),2)
        prefix=0;Q=0;it=iter(inds);next_one=next(it,None)
        for t in range(1,N):
            if next_one==t:
                prefix+=1;next_one=next(it,None)
            z=N*prefix-a*t
            Q+=z*z
        w2s.append(W*W)
        ts.append(F(Q,a*b*N*N))
    ew=sum(w2s)/total; et=sum(ts)/total
    cov=sum(x*y for x,y in zip(w2s,ts))/total-ew*et
    vw=sum(x*x for x in w2s)/total-ew*ew
    vt=sum(x*x for x in ts)/total-et*et
    return ew,et,cov,vw,vt


def main():
    assertions=0
    for N in range(3,12):
        for a in range(1,N):
            b=N-a
            observed=enumeration(a,b)
            expected=formulas(a,b)
            for i,(left,right) in enumerate(zip(observed,expected)):
                assert left==right,(N,a,i,left,right)
                assertions+=1
            assert expected[2]>0;assert expected[3]>0;assert expected[4]>0
            assertions+=3
            V=expected
            # identity Corr=1 iff one group is singleton, all groups positive
            determinant=V[3]*V[4]-V[2]**2
            assert (determinant==0)==(min(a,b)==1)
            assertions+=1
    print('PASS: exact enumeration N=3..11, every 1<=a<N;',assertions,'rational assertions')

if __name__=='__main__':main()
