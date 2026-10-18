"""Reproduce finite exact checks of root-protection influence in weighted recursive trees."""
from fractions import Fraction
from itertools import product
from math import factorial

def lam(N, theta):
    # Ewens weighted permutation polynomial: derangements by cycle count.
    if N == 0:
        return Fraction(1)
    if N == 1:
        return Fraction(0)
    D0 = [0]*(N+1); D0[0]=1
    D1 = [0]*(N+1)
    for n in range(2,N+1):
        D2=[0]*(N+1)
        for k in range(1,n+1):
            D2[k]=(n-1)*(D1[k]+D0[k-1])
        D0,D1 = D1,D2
    weighted=sum(D1[k]*theta**k for k in range(N+1))
    normal=Fraction(1)
    for j in range(N): normal*=theta+j
    return weighted/normal

def test(N,theta):
    assert N>=2
    normal=Fraction(1)
    for i in range(2,N+1):normal*=theta+i-1
    prob_H=Fraction(0); prob_B={i:Fraction(0) for i in range(2,N+1)}
    prob_BH={i:Fraction(0) for i in range(2,N+1)}
    for parents in product(*(range(i) for i in range(2,N+1))):
        # 0 means root, 1..i-1 means one earlier branch member.
        B={i:(parents[i-2]==0) for i in range(2,N+1)}
        w=theta**sum(B.values())/normal
        roots={1:1}
        for i in range(2,N+1):
            roots[i] = i if B[i] else roots[parents[i-2]]
        sizes={}
        for r in roots.values():sizes[r]=sizes.get(r,0)+1
        H=all(v>=2 for v in sizes.values())
        if H: prob_H+=w
        for i in range(2,N+1):
            if B[i]:prob_B[i]+=w
            if H and B[i]:prob_BH[i]+=w
    assert prob_H == lam(N,theta),('lam',N,theta,prob_H,lam(N,theta))
    assert all(prob_B[i] == theta/(theta+i-1) for i in prob_B)
    ctotal=Fraction(0)
    for i in prob_B:
        p=prob_B[i]; cov=prob_BH[i]-p*prob_H
        assert cov<0,('strict',N,theta,i,cov)
        ctotal+=cov
        delta=-cov/(p*(1-p))
        lead=(theta+i-1)/(theta+N-1)*lam(N-1,theta)
        bound=theta/(theta+N-1)*(theta+i-1)/(theta+i-2)
        assert lead<=delta<=lead+bound,('influence bound',N,theta,i,delta,lead,bound)
    # Cov(K,H) by exponential-family derivative equals sum local covariances.
    return ctotal

count=0
for theta in (Fraction(1,2),Fraction(1),Fraction(2)):
    for N in range(2,9):
        cov=test(N,theta)
        count+=2*N
print('PASSED:',count,'exact conservation, strict sign, and influence-bound assertions')
