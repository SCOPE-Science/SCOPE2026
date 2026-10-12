#!/usr/bin/env python3
"""Self-contained finite checks for the random permutation-copula fluctuation theorem.

No finite calculation establishes the functional central limit theorem; its proof is analytic.
"""
import itertools
import math
import random


def A(k, r, x):
    return max(0., min(1., k*x-r+1.))


def cop(k, perm, u, v):
    return sum(A(k, r, u)*A(k, perm[r-1], v) for r in range(1,k+1))/k


def kernel(k, a, b):
    return sum((A(k, r, a)-a)*(A(k, r, b)-b) for r in range(1,k+1))/k


def random_cov(k, points):
    perms=list(itertools.permutations(range(1,k+1)))
    arr=[[cop(k,p,*pt)-pt[0]*pt[1] for pt in points] for p in perms]
    actual=[[sum(row[i]*row[j] for row in arr)/len(arr) for j in range(len(points))]
            for i in range(len(points))]
    expected=[[kernel(k,points[i][0],points[j][0])*
               kernel(k,points[i][1],points[j][1])/(k-1)
               for j in range(len(points))] for i in range(len(points))]
    err=max(abs(actual[i][j]-expected[i][j]) for i in range(len(points))
            for j in range(len(points)))
    return perms,arr,err


def verify():
    random.seed(260313953)
    pairs=0
    maxerr=0.
    for k in range(2,7):
        pts=[(i/k,j/k) for i,j in [(1,1),(k-1,1),(1,k-1),(k-1,k-1)]]
        pts.extend([(0.137,0.791), (0.433,0.269), (0.75,0.5)])
        _,_,err=random_cov(k,pts)
        assert err<5e-14,(k,err)
        pairs+=len(pts)**2
        maxerr=max(maxerr,err)
        for a in [0.,0.057,0.2,0.51,0.85,1.]:
            for b in [0.,0.13,0.35,0.72,0.9,1.]:
                e=(min(a,b)-a*b)-kernel(k,a,b)
                assert -2e-14<=e<=1/(4*k)+2e-14,(k,a,b,e)
    print('Exact permutation covariance checked for k=2..6:',pairs,'pairs, max error=',maxerr)
    spectrum=0
    for k in range(2,10):
        for mode in range(1,k):
            l=1/(4*k*math.sin(mode*math.pi/(2*k))**2)
            for i in range(1,k):
                lhs=sum((min(i,j)/k-i*j/(k*k))*math.sin(mode*math.pi*j/k)
                        for j in range(1,k))
                rhs=l*math.sin(mode*math.pi*i/k)
                assert abs(lhs-rhs)<5e-13,(k,mode,i,lhs,rhs)
                spectrum+=1
    print('Discrete sine-eigenpair identities checked:',spectrum)
    for k in [4,5,6]:
        m=math.factorial(k)
        pts=[(.5,.5),(.4,.7)]
        perms,arr,_=random_cov(k,pts)
        weights=[row[0] for row in arr]
        samples=[]
        rng=random.Random(124521+k)
        for _ in range(3500):
            # Exponential representation of a uniform simplex point.
            E=[rng.expovariate(1.0) for _ in range(m)]
            val=math.sqrt((m+1)*(k-1))*sum(e*w for e,w in zip(E,weights))/sum(E)
            samples.append(val)
        mean=sum(samples)/len(samples)
        variance=sum((x-mean)**2 for x in samples)/len(samples)
        fourth=sum((x-mean)**4 for x in samples)/len(samples)/(variance*variance)
        theory=kernel(k,.5,.5)**2
        assert abs(mean)<.09,(k,mean)
        assert abs(variance/theory-1)<.14,(k,variance,theory)
        if k>=5:
            assert abs(fourth-3)<1.0,(k,fourth)
        print('k=',k,'n=',m,'scaled variance=',round(variance,6),
              'exact variance=',round(theory,6),'kurtosis=',round(fourth,4))
    print('All finite checks passed. Functional convergence requires the written proof.')

if __name__=='__main__':
    verify()
