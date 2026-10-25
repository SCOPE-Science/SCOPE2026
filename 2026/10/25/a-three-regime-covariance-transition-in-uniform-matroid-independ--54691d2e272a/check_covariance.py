"""Exact finite-rank moment identities for rank-capped unit cubes.
Pure Python standard library. No simulation is used as an infinite proof.
"""
from fractions import Fraction as Q
from math import comb, factorial
from random import Random

def poly_moments(n,k):
    assert 1<=k<=n
    F=A=B=Q(0)
    for j in range(k):
        c=k-j; w=(-1)**j * comb(n,j)
        F+=Q(w*c**n,factorial(n))
        A+=Q(w,factorial(n-1))*(Q(j*c**n,n)+Q(c**(n+1),n+1))
        B+=Q(w,factorial(n-1))*(Q(j*j*c**n,n)+Q(2*j*c**(n+1),n+1)+Q(c**(n+2),n+2))
    return F,A,B

def xmoment(n,k,p):
    m=n-1
    res=Q(0)
    for j in range(k):
        c=k-j
        inner=sum((Q((-1)**l*comb(m,l)*c**(m-l), p+l+1) for l in range(m+1)),Q(0))
        res+=(-1)**j*comb(m,j)*inner
    return res/factorial(m)

def spectra(n,k):
    F,A,B=poly_moments(n,k)
    J0=xmoment(n,k,0)
    assert J0==F,(n,k,F,J0)
    es=A/F
    var=B/F-es**2
    ex=xmoment(n,k,1)/F
    ax=xmoment(n,k,2)/F-ex**2
    parallel=var/n
    transverse=(n*n*ax-var)/(n*(n-1))
    assert transverse>0 and parallel>0,(n,k,transverse,parallel)
    return F,transverse,parallel,ex

def monte(n,k,N=100000,seed=8271):
    rng=Random(seed)
    c=0;s=s2=x=x2=Q(0)
    # simple double precision check of the analytic spectrum on acceptance sampling
    esum=esum2=eone=eone2=0.
    trials=0
    while c<N:
        v=[rng.random() for _ in range(n)]
        trials+=1
        if sum(v)>k:continue
        total=sum(v)
        esum+=total; esum2+=total*total
        eone+=v[0]; eone2+=v[0]*v[0]
        c+=1
    vs=esum2/N-(esum/N)**2
    ax=eone2/N-(eone/N)**2
    return (n*n*ax-vs)/(n*(n-1)),vs/n,trials

if __name__=='__main__':
    tot=0
    for n in range(2,10):
        for k in range(1,n+1):
            F,t,p,mean=spectra(n,k)
            if k==n:
                assert F==1 and t==Q(1,12) and p==Q(1,12)
            if k==1:
                assert F==Q(1,factorial(n))
            tot+=1
    for n,k in [(6,2),(7,3),(8,4)]:
        F,t,p,mean=spectra(n,k)
        tt,pp,trials=monte(n,k,120000,seed=1907+n)
        assert abs(tt-float(t))<0.008 and abs(pp-float(p))<0.008,(n,k,t,tt,p,pp)
        print('CHECK',n,k,'volume',float(F),'transverse',float(t),'parallel',float(p),'sample',tt,pp,'trials',trials)
    print('VERIFY_OK rational_parameter_cases=',tot,'simulation_cases=3')
