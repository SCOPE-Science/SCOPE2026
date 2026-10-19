#!/usr/bin/env python3
"""Exact finite-N checks and independent numerical asymptotic checks for the two-state nonlinear voter model."""
from fractions import Fraction
from math import comb, sqrt, log, erf, ceil, lgamma, exp, fsum

def exact_exit(N, q):
    m = N - 1
    w = [comb(m,j)**(q-1) for j in range(m+1)]
    den=sum(w)
    E=[Fraction(0)]
    running=0
    for j in range(m+1):
        running+=w[j]
        E.append(Fraction(running,den))
    return E

def test():
    checks=0
    assert 1 <= 2
    for N in range(3,40):
        m=N-1
        E2=exact_exit(N,2)
        E3=exact_exit(N,3)
        assert sum(comb(m,j)**2 for j in range(m+1)) == comb(2*m,m); checks+=1
        for q,E in [(2,E2),(3,E3)]:
            for k in range(1,N):
                a=(N-k)*Fraction(k,N-1)**q
                b=k*Fraction(N-k,N-1)**q
                assert a*(E[k+1]-E[k]) == b*(E[k]-E[k-1])
                checks+=1
            assert E[0]==0 and E[N]==1; checks+=1
            for k in range(N+1):
                assert E[N-k] ==1-E[k]; checks+=1
        for k in range(1,N):
            if 2*k<N: assert E3[k] < E2[k]
            if 2*k==N: assert E3[k] == E2[k]
            if 2*k>N: assert E3[k] > E2[k]
            checks+=1
        d=[E3[k]-E2[k] for k in range(N+1)]
        imax=max(range(N+1),key=lambda k:d[k])
        for k in range(imax+1,N):
            assert d[k+1]<=d[k];checks+=1
        for k in range(ceil(N/2),imax):
            assert d[k+1]>=d[k];checks+=1
    sstar=sqrt(log(2))/2
    Phi=lambda z:(1+erf(z/sqrt(2)))/2
    L=Phi(2*sqrt(2)*sstar)-Phi(2*sstar)
    for N in (101,401,1601,6401):
        m=N-1
        # Compute the two distribution functions independently by log-gamma masses, standard library only.
        logB=lgamma(2*m+1)-2*lgamma(m+1)
        p2=[];p3=[]
        for j in range(m+1):
            lc=lgamma(m+1)-lgamma(j+1)-lgamma(m-j+1)
            p2.append(exp(lc-m*log(2)))
            p3.append(exp(2*lc-logB))
        d=[0.0]
        c2=c3=0.0
        for j in range(m+1):
            c2+=p2[j];c3+=p3[j]
            d.append(c3-c2)
        imax=max(range(N+1),key=lambda i:d[i])
        print('N=',N,'kmax=',imax,'(kmax-N/2)/sqrt(N)=',round((imax-N/2)/sqrt(N),7),'max gap=',round(d[imax],10),'limit=',round(L,10))
        assert abs(d[imax]-L)<1.3/sqrt(N)
        checks+=1
    print('checks_passed=',checks)
    print('exact_universal_limit=',L,'s_star=',sstar)

if __name__=='__main__':test()
