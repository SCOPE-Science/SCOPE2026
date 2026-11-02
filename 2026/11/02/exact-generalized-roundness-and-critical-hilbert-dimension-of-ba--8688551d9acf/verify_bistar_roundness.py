#!/usr/bin/env python3
"""Independent finite checks for the balanced double-star metric theorem.

Uses only Python's standard library. Finite checks corroborate, but do not
replace, the analytic all-orders proof.
"""
from collections import deque
from fractions import Fraction
from math import log
from random import Random


def metric(q):
    n = 2*q+2
    graph=[[] for _ in range(n)]
    def link(i,j):
        graph[i].append(j); graph[j].append(i)
    link(0,1)
    for j in range(q):
        link(0,2+j); link(1,2+q+j)
    dist=[]
    for start in range(n):
        d=[-1]*n; d[start]=0; queue=deque([start])
        while queue:
            v=queue.popleft()
            for w in graph[v]:
                if d[w]<0:
                    d[w]=d[v]+1; queue.append(w)
        assert -1 not in d
        dist.append(d)
    for i in range(n):
        for j in range(n):
            expect=0 if i==j else (1 if {i,j}=={0,1} else
                (1 if (i==0 and 2<=j<2+q or j==0 and 2<=i<2+q or
                       i==1 and j>=2+q or j==1 and i>=2+q) else
                 (2 if (i<2 and j>=2 or j<2 and i>=2 or
                         i>=2 and j>=2 and ((i<2+q)==(j<2+q))) else 3)))
            assert dist[i][j]==expect, (q,i,j,dist[i][j],expect)
    return dist


def critical(q):
    def phi(p):
        return (1.5)**p-1-2**(-p)
    left,right=1.,2.
    for _ in range(100):
        mid=(left+right)/2
        if phi(mid)<1/q: left=mid
        else: right=mid
    return (left+right)/2


def exact_block_check(q,D,rng):
    n=len(D)
    for p in (1,2,3):
        t=2**p;u=3**p
        for trial in range(10):
            x=[rng.randrange(-5,6) for _ in range(n-1)]
            x.append(-sum(x))
            direct=sum(x[i]*x[j]*D[i][j]**p for i in range(n) for j in range(n))
            LA=[Fraction(z) for z in x[2:2+q]]
            LB=[Fraction(z) for z in x[2+q:]]
            aa=sum(LA)/q; ab=sum(LB)/q
            aS=(aa+ab)/2; aA=(aa-ab)/2
            bS=Fraction(x[0]+x[1],2); bA=Fraction(x[0]-x[1],2)
            assert bS==-q*aS
            residual=-t*(sum((z-aa)**2 for z in LA)+sum((z-ab)**2 for z in LB))
            symmetric=2*q*(q*u-(q+1)*t-q)*aS*aS
            antisymmetric=2*(q*((q-1)*t-q*u)*aA*aA +
                             2*q*(1-t)*aA*bA -bA*bA)
            assert residual+symmetric+antisymmetric==direct,(q,p,trial)


def main():
    rng=Random(241003)
    for q in range(1,13):
        D=metric(q)
        exact_block_check(q,D,rng)
        p=critical(q);t=2**p;u=3**p
        f=q*u-(q+1)*t-q
        g=q*u+(q+1)*t-q*t*t-q
        assert abs(f)<5e-12
        if q==1:
            assert abs(p-2)<1e-12 and abs(g)<1e-11
        else:
            assert 1<p<2 and g>0, (q,p,g)
            assert t<2+2/q
            # The all-leaf-plus, both-hub-minus equality vector.
            coeff=[-q,-q]+[1]*(2*q)
            row=[sum(D[i][j]**p*coeff[j] for j in range(len(D))) for i in range(len(D))]
            assert abs(sum(coeff[i]*row[i] for i in range(len(D))))<1e-8*(2*q+2)
        print('METRIC_AND_BLOCK_OK q=',q,'vertices=',2*q+2,'critical=',format(p,'.12f'))
    alpha=2/(3*log(3)-2*log(2))
    for q in (100,1000,10000):
        p=critical(q)
        assert abs(q*(p-1)-alpha)<2/q, (q,p,alpha)
    print('ASYMPTOTIC_OK coefficient=',format(alpha,'.12f'))
    print('ALL_BALANCED_BISTAR_ROUNDNESS_CHECKS_OK')

if __name__=='__main__':main()
