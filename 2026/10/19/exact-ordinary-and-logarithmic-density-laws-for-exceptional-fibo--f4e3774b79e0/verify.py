#!/usr/bin/env python3
"""Independent finite-gap and entropy-density diagnostics for a Fibonacci rotation."""
from collections import Counter
from decimal import Decimal, localcontext
from math import log, sqrt
from bisect import bisect_left

PHI=(1+sqrt(5))/2
ALPHA=1/PHI
U=1/PHI
V=1/PHI**2
A=PHI**2/sqrt(5)
B=PHI/sqrt(5)
C=1/sqrt(5)
F=[0,1]
for _ in range(31): F.append(F[-1]+F[-2])

def profile(t,q):
    if q==1:
        return log(1+t)+(U-t)*A*log(A)+(V+t)*B*log(B)+t*C*log(C)
    s=(U-t)*A**q+(V+t)*B**q+t*C**q
    return log(1+t)-log(s)/(1-q)

def exact_deficit(N,q):
    # N=n+1 is the number of nonzero block probabilities.
    j=3
    while F[j+1]<=N: j+=1
    k=N-F[j]
    lengths=((F[j-1]-k,ALPHA**(j-2)),(F[j-2]+k,ALPHA**(j-1)),(k,ALPHA**j))
    if q==1:
        H=-sum(mult*p*log(p) for mult,p in lengths if mult)
    else:
        H=log(sum(mult*p**q for mult,p in lengths if mult))/(1-q)
    return log(N)-H

def root_of_level(q,theta,lo,hi):
    flo=profile(lo,q)-theta
    for _ in range(80):
        mid=(lo+hi)/2
        fm=profile(mid,q)-theta
        if flo*fm>0:
            lo=mid;flo=fm
        else: hi=mid
    return (lo+hi)/2

def t_peak(q):
    if q==1:
        Q=-A*log(A)+B*log(B)+C*log(C)
        return -1/Q-1
    s0=U*A**q+V*B**q
    s1=-A**q+B**q+C**q
    return ((1-q)*s0-s1)/(q*s1)

def finite_density(q,theta,cap):
    selected=0;harmonic=0.0
    for n in range(1,cap+1):
        if exact_deficit(n+1,q)>theta:
            selected+=1
            harmonic+=1/n
    return selected/cap,harmonic/log(cap)

def verify():
    gap_checks=0
    with localcontext() as ctx:
        ctx.prec=90
        alpha=(ctx.sqrt(Decimal(5))-1)/2
        eps=Decimal('1e-70')
        for j in range(3,14):
            for k in sorted(set([0,1,F[j-1]//3,F[j-1]//2,F[j-1]-1])):
                if not 0<=k<F[j-1]:continue
                N=F[j]+k
                pts=sorted([(Decimal(h)*alpha)%1 for h in range(N)])
                gaps=[pts[h+1]-pts[h] for h in range(N-1)]+[1+pts[0]-pts[-1]]
                kinds=(alpha**(j-2),alpha**(j-1),alpha**j)
                counts=Counter()
                for p in gaps:
                    match=[i for i,kk in enumerate(kinds) if abs(p-kk)<eps]
                    assert len(match)==1,(j,k,p,match)
                    counts[match[0]]+=1
                assert tuple(counts[h] for h in range(3))==(F[j-1]-k,F[j-2]+k,k)
                for q in (0.5,1,2,-1):
                    probabilities=[float(p) for p in gaps]
                    if q==1: H=-sum(pp*log(pp) for pp in probabilities)
                    else: H=log(sum(pp**q for pp in probabilities))/(1-q)
                    assert abs((log(N)-H)-exact_deficit(N,q))<2e-8,(j,k,q)
                gap_checks+=1
    density_checks=0
    for q in (0.5,1,2,4):
        t=t_peak(q)
        assert 0<t<U
        d=profile(0,q);m=profile(t,q)
        assert abs(profile(U,q)-d)<1e-12 and m>d
        theta=(d+m)/2
        left=root_of_level(q,theta,0,t)
        right=root_of_level(q,theta,t,U)
        L=right-left
        lower=PHI*L/(1+left)
        upper=PHI**2*L/(1+right)
        logarithmic=log((1+right)/(1+left))/log(PHI)
        assert 0<lower<logarithmic<upper<1
        # Sample near the two claimed extrema on a late Fibonacci block.
        base=F[23]
        for s,pred in ((1+left,lower),(1+right,upper)):
            cap=int(base*s)
            count_ratio,_=finite_density(q,theta,cap)
            assert abs(count_ratio-pred)<0.002,(q,s,pred,count_ratio)
            density_checks+=1
    print(f'VERIFY_OK {gap_checks} high-precision independent orbit-gap cylinders; {4*gap_checks} entropy comparisons; {density_checks} level-density boundary checks')

if __name__=='__main__':
    verify()
