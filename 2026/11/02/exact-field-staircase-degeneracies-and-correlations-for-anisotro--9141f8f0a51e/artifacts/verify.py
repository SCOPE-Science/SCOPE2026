"""Reproducible exact tests for the anisotropic rectangular rook Ising model.

The verification compares direct edge energies, degree-balanced formulas,
independent dynamic-programming microcanonical minima and correlations.
Matrices and vertices are all labelled; no external data is required.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd, comb
from itertools import combinations
import numpy as np


def balanced(m,n,K):
    qr,tr=divmod(K,m)
    qc,tc=divmod(K,n)
    return qr,tr,qc,tc


def ex_energy2(m,n,Jr,Jc,h2,K):
    qr,tr,qc,tc=balanced(m,n,K)
    a,b=2*qr-n,2*qc-m
    return (Jr*((m-tr)*a*a+tr*(a+2)**2-m*n)
            + Jc*((n-tc)*b*b+tc*(b+2)**2-m*n)
            - h2*(2*K-m*n))


def optimal(m,n,Jr,Jc,h2):
    vals=[ex_energy2(m,n,Jr,Jc,h2,K) for K in range(m*n+1)]
    low=min(vals)
    return low,{K for K,e in enumerate(vals) if e==low}


def direct(m,n,Jr,Jc,h2):
    N=m*n
    v=np.arange(1<<N,dtype=np.uint32)
    x=np.stack([1-2*((v>>k)&1).astype(np.int16) for k in range(N)],axis=1)
    ints=np.zeros((len(v),),dtype=np.int32)
    for a in range(N):
        i,j=divmod(a,n)
        for b in range(a+1,N):
            ii,jj=divmod(b,n)
            if i==ii:ints+=Jr*x[:,a].astype(np.int32)*x[:,b].astype(np.int32)
            elif j==jj:ints+=Jc*x[:,a].astype(np.int32)*x[:,b].astype(np.int32)
    pos=((x+1)//2).reshape(-1,m,n)
    K=pos.sum(axis=(1,2))
    energy2=2*ints-h2*(2*K-N)
    low,allowed=optimal(m,n,Jr,Jc,h2)
    is_low=energy2==low
    structural=np.zeros(len(v),dtype=bool)
    for k in allowed:
        qr,tr,qc,tc=balanced(m,n,k)
        rr=pos.sum(axis=2)
        cc=pos.sum(axis=1)
        structural|=((K==k)&np.isin(rr,[qr,qr+1]).all(axis=1)
                     & (rr==qr+1).sum(axis=1).__eq__(tr)
                     &np.isin(cc,[qc,qc+1]).all(axis=1)
                     &(cc==qc+1).sum(axis=1).__eq__(tc))
    assert int(energy2.min())==low,(m,n,Jr,Jc,h2,'energy')
    assert np.array_equal(is_low,structural),(m,n,Jr,Jc,h2,'states')
    return int(is_low.sum()), x, K


def microcanonical_dp(m,n,Jr,Jc):
    opts=[(mask,mask.bit_count()) for mask in range(1<<n)]
    dp={(0,)*n:(0,1)}
    for i in range(m):
        nd={}
        for cols,(cost,count) in dp.items():
            for mask,q in opts:
                new=tuple(cols[j]+((mask>>j)&1) for j in range(n))
                row=2*q-n
                candidate=cost+Jr*(row*row-n)
                old=nd.get(new)
                if old is None or candidate<old[0]:nd[new]=(candidate,count)
                elif candidate==old[0]:nd[new]=(candidate,old[1]+count)
        dp=nd
    best=[None]*(m*n+1)
    cnt=[0]*(m*n+1)
    for cols,(cst,num) in dp.items():
        k=sum(cols)
        energy2=cst+Jc*sum((2*c-m)**2-m for c in cols)
        if best[k] is None or energy2<best[k]:best[k]=energy2;cnt[k]=num
        elif energy2==best[k]:cnt[k]+=num
    for k in range(m*n+1):
        assert best[k]==ex_energy2(m,n,Jr,Jc,0,k),(m,n,k,best[k])
    return cnt


def coefficient_count(m,n,K):
    qr,tr,qc,tc=balanced(m,n,K)
    target=(qc+1,)*tc+(qc,)*(n-tc)
    rows=(qr+1,)*tr+(qr,)*(m-tr)
    dp={(0,)*n:1}
    for r in rows:
        nxt=defaultdict(int)
        for c,ways in dp.items():
            for cols in combinations(range(n),r):
                v=list(c)
                for j in cols:v[j]+=1
                if all(v[j]<=target[j] for j in range(n)):
                    nxt[tuple(v)]+=ways
        dp=nxt
    return comb(m,tr)*comb(n,tc)*dp.get(target,0)


def micro_covariance(m,n,K):
    if m*n>16:return
    _,x,ks=direct(m,n,1,3,0)
    subset=x[ks==K].astype(np.int64)
    # Filter microcanonical minimizers by *direct* edge energy at K.
    r=subset.reshape(-1,m,n).sum(axis=2)
    c=subset.reshape(-1,m,n).sum(axis=1)
    interaction=((r*r-n).sum(axis=1)+3*(c*c-m).sum(axis=1))//2
    subset=subset[interaction==interaction.min()]
    qr,tr,qc,tc=balanced(m,n,K)
    mu=Fraction(2*K-m*n,m*n)
    V=1-mu*mu
    wr=Fraction(4*tr*(m-tr),m*m)
    wc=Fraction(4*tc*(n-tc),n*n)
    cr=(wr-n*V)/(n*(n-1))
    cc=(wc-m*V)/(m*(m-1))
    cd=(V-wr/n-wc/m)/((m-1)*(n-1))
    def cov(a,b):return Fraction(int((subset[:,a]*subset[:,b]).sum()),len(subset))-mu*mu
    assert cov(0,1)==cr,(m,n,K,'row')
    assert cov(0,n)==cc,(m,n,K,'column')
    assert cov(0,n+1)==cd,(m,n,K,'disjoint')
    return len(subset)


def main():
    trials=0
    for m,n in [(2,2),(2,3),(3,3),(3,4),(4,4)]:
        for Jr,Jc in [(1,1),(1,2),(3,2)]:
            for h2 in range(-2*(Jr+Jc)*max(m,n),2*(Jr+Jc)*max(m,n)+1,2):
                direct(m,n,Jr,Jc,h2)
                trials+=1
    print('Independent direct-edge spin-census comparisons:',trials)
    for m,n in [(2,3),(3,4),(3,5),(4,4),(4,5),(5,5)]:
        for Jr,Jc in [(1,1),(1,2)]:
            cnt=microcanonical_dp(m,n,Jr,Jc)
            assert all(x>0 for x in cnt)
            assert cnt[0]==cnt[-1]==1
            for K in range(m*n+1):assert cnt[K]==coefficient_count(m,n,K),(m,n,K,cnt[K])
        print('Complete DP microcanonical and coefficient-count verification:',m,'x',n,'K = 0,...,',m*n)
    n_cov=0
    for m,n in [(2,3),(3,3),(3,4),(4,4)]:
        for k in range(1,m*n):
            micro_covariance(m,n,k)
            n_cov+=1
    print('Exact three-orbit covariance comparisons:',n_cov)
    for m,n in [(2,3),(3,4),(3,5),(4,4),(4,6),(6,6)]:
        b=[0]+[k for k in range(1,m*n) if k%m==0 or k%n==0]+[m*n]
        assert len(b)==m+n-gcd(m,n)+1
        H=[(2*(k//m)-n+1)+2*(2*(k//n)-m+1) for k in b[:-1]]
        assert H==sorted(set(H))
    print('Arithmetic breakpoint/plateau counts: six aspect-ratio checks')
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
