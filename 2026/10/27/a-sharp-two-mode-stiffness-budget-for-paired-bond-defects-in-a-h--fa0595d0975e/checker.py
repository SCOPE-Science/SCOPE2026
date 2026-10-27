#!/usr/bin/env python3
"""Standalone numerical checks for the two-stiff-spring harmonic chain.

Only the Python standard library is required. The infinite resolvent equation
and a separately constructed finite-chain Jacobi matrix are evaluated independently.
Numerical tests are finite checks; the accompanying mathematical proof is essential.
"""
from math import exp, cosh, sqrt


def bs_eigenvalues(d, alpha, beta, t):
    q=exp(-t)
    B=2*q/(1-q)
    F=fd(d,q)
    C=B-F
    s=alpha+beta
    root=sqrt(((alpha-beta)*B/2)**2+alpha*beta*C*C)
    high=s*B/2+root
    low=alpha*beta*F*(B+C)/high
    return (low,high)


def find_roots(d, alpha, beta):
    z=2*alpha*beta*(2*d-1)/(alpha+beta)
    modes=[]
    for i in ([0,1] if z>1 else [1]):
        lo,hi=1e-10,10.0
        for _ in range(100):
            mid=(lo+hi)/2
            if bs_eigenvalues(d,alpha,beta,mid)[i]>1:
                lo=mid
            else:
                hi=mid
        t=(lo+hi)/2
        modes.append(2+2*cosh(t))
    return modes


def finite_chain_matrix(n, d, alpha, beta):
    springs=[1.0]*(n-1)
    j=n//2-1
    springs[j]+=alpha
    springs[j+d]+=beta
    diag=[springs[0]]+[springs[i-1]+springs[i] for i in range(1,n-1)]+[springs[-1]]
    off=[-s for s in springs]
    return diag,off


def below(diag,off,x):
    """Sturm inertia of a real symmetric tridiagonal matrix minus x I."""
    pivot=diag[0]-x
    cnt=int(pivot<0)
    for i,c in enumerate(off):
        if abs(pivot)<1e-14: pivot=-1e-14
        pivot=diag[i+1]-x-c*c/pivot
        cnt+=int(pivot<0)
    return cnt


def top_finite_eigs(n,d,alpha,beta):
    D,E=finite_chain_matrix(n,d,alpha,beta)
    upper=4+2*alpha+2*beta
    eigs=[]
    for target in (n-2,n-1):
        lo,hi=-0.01,upper
        for _ in range(70):
            mid=(lo+hi)/2
            if below(D,E,mid)<=target: lo=mid
            else: hi=mid
        eigs.append((lo+hi)/2)
    return eigs


def fd(d,q):
    return 2*sum(q**j for j in range(1,d))+q**d


def check():
    ntests=0
    for d in [1,2,3,5,8]:
        for a,b in [(0.15,0.15),(0.4,0.7),(1.5,0.8),(0.8,2.1)]:
            theta=2*a*b*(2*d-1)/(a+b)
            modes=find_roots(d,a,b)
            assert len(modes)==1+int(theta>1)
            finite=top_finite_eigs(200,d,a,b)
            for theory,observed in zip(modes,finite[-len(modes):]):
                assert abs(theory-observed)<2e-4, (d,a,b,theory,observed)
                ntests+=1
    for d in [1,2,3,7]:
        crit=1/(2*d-1)
        coeff=(2*d-1)**4/d**4
        for eps in [.002,.0003]:
            a=crit+eps
            lo,hi=0.0,1.0
            for _ in range(95):
                mid=(lo+hi)/2
                if a*fd(d,mid)>1:hi=mid
                else:lo=mid
            q=(hi+lo)/2
            lam=2+q+1/q
            assert abs((lam-4)/eps**2/coeff-1)<.05,(d,eps,lam)
            ntests+=1
    for d in [1,2,5]:
        S=2.8/(2*d-1)
        balanced=find_roots(d,S/2,S/2)
        assert len(balanced)==2
        for p in [.2,.35,.65,.8]:
            a,b=S*p,S*(1-p)
            modes=find_roots(d,a,b)
            if len(modes)==2:
                assert modes[0]<balanced[0]
            assert modes[-1]>balanced[-1]
            ntests+=1
    print(f"PASS: {ntests} numerical comparisons (finite Jacobi/Sturm, edge law, allocation).")

if __name__=='__main__':
    check()
