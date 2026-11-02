#!/usr/bin/env python3
"""Exact finite checks for triangle / induced-open-wedge covariance laws."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

def q(m, N, k):
    if m < k:
        return Fraction(0)
    a = Fraction(1)
    for j in range(k):
        a *= Fraction(m-j, N-j)
    return a

def fixed_formula(n, m):
    N, B = comb(n,2), comb(n,3)
    a = B - 1 - 3*(n-3)
    qq = lambda k:q(m,N,k)
    return B*(6*(n-3)*(qq(4)-qq(5)) + 3*a*(qq(5)-qq(6)) - 3*B*qq(3)*(qq(2)-qq(3)))

def fixed_factor(n, m):
    N, B = comb(n,2),comb(n,3)
    den = (n+1)*(n+2)*(n*n-n-10)*(n*n-n-8)*(n*n-n-4)
    G = m*(n*n-3*n-8) + (n-1)*(n*n-n-4)
    return -Fraction(48*B*(N-m)*(N-1-m)*G,den)*q(m,N,3)

def binomial_formula(n,p):
    return 3*comb(n,3)*p**4*(1-p)*((n-3)*(2-3*p)-p)

def enumerate_exact(n):
    edges=list(combinations(range(n),2)); triples=list(combinations(range(n),3)); N=len(edges)
    emap={e:j for j,e in enumerate(edges)}
    masks=[sum(1<<emap[e] for e in combinations(t,2)) for t in triples]
    accum=defaultdict(lambda:[0,0,0,0])
    snapshots=[]
    for bits in range(1<<N):
        m=bits.bit_count(); t=w=0
        for mask in masks:
            k=(bits&mask).bit_count()
            t += (k==3); w += (k==2)
        c=accum[m];c[0]+=1;c[1]+=t;c[2]+=w;c[3]+=t*w
        snapshots.append((m,t,w))
    checks=0
    for m,(count,st,sw,stw) in accum.items():
        assert count==comb(N,m)
        cov=Fraction(stw,count)-Fraction(st*sw,count*count)
        assert cov==fixed_formula(n,m),(n,m,cov,fixed_formula(n,m))
        assert cov==fixed_factor(n,m),(n,m,cov,fixed_factor(n,m))
        assert (cov<0)==(3<=m<=N-2),(n,m,cov)
        checks+=3
    for p in (Fraction(1,5),Fraction(1,2),Fraction(3,4)):
        E_t=E_w=E_tw=Fraction(0)
        for m,t,w in snapshots:
            wt=p**m*(1-p)**(N-m)
            E_t +=wt*t; E_w +=wt*w; E_tw+=wt*t*w
        assert E_tw-E_t*E_w==binomial_formula(n,p)
        checks+=1
    return len(snapshots),checks

if __name__=='__main__':
    total=checks=0
    for n in (4,5,6):
        num, count=enumerate_exact(n)
        total+=num; checks+=count
        print('n=',n,'graphs=',num,'checks=',count)
    for n in range(4,41):
        N=comb(n,2)
        for m in range(N+1):
            assert fixed_formula(n,m)==fixed_factor(n,m)
            assert (fixed_factor(n,m)<0)==(3<=m<=N-2)
            checks+=2
    print('PASS graphs=',total,'identities=',checks)
