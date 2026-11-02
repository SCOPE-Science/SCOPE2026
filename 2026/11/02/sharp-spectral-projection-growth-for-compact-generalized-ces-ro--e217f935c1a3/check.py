#!/usr/bin/env python3
"""Finite-section arithmetic checks for a Cesaro spectral-projection identity."""
from fractions import Fraction
from math import comb, lgamma, log, exp, pi, sqrt


def mm(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def verify_section(N,m,t):
    lam=Fraction(1,m+1)
    C=[[t**(n-k)/Fraction(n+1) if k<=n else Fraction(0) for k in range(N)] for n in range(N)]
    v=[Fraction(0) if n<m else Fraction(comb(n,m))*t**(n-m) for n in range(N)]
    w=[Fraction(comb(m,k))*(-t)**(m-k) if k<=m else Fraction(0) for k in range(N)]
    assert sum(v[k]*w[k] for k in range(N)) == 1
    assert [sum(C[n][k]*v[k] for k in range(N)) for n in range(N)] == [lam*z for z in v]
    assert [sum(w[n]*C[n][k] for n in range(N)) for k in range(N)] == [lam*z for z in w]
    P=[[v[n]*w[k] for k in range(N)] for n in range(N)]
    assert mm(P,P)==P
    assert mm(P,C)==mm(C,P)
    exact1=sum(abs(z) for z in v)*max(abs(z) for z in w)
    direct1=max(sum(abs(P[n][k]) for n in range(N)) for k in range(N))
    assert direct1==exact1
    exact_inf=max(abs(z) for z in v)*sum(abs(z) for z in w)
    direct_inf=max(sum(abs(z) for z in row) for row in P)
    assert direct_inf==exact_inf
    return True


def logsumexp(terms):
    ma=max(terms)
    return ma+log(sum(exp(z-ma) for z in terms))


def lognorm(m,t,p):
    from math import inf
    a=[lgamma(m+j+1)-lgamma(m+1)-lgamma(j+1)+j*log(t) for j in range(max(10*m, int(4*m/(1-t)) + 150))]
    b=[lgamma(m+1)-lgamma(k+1)-lgamma(m-k+1)+(m-k)*log(t) for k in range(m+1)]
    q=inf if p==1 else (1 if p==inf else p/(p-1))
    def lp(logvals,r):
        return max(logvals) if r==inf else logsumexp([r*x for x in logvals])/r
    return lp(a,p)+lp(b,q)


def logasym(m,t,p):
    from math import inf
    q=inf if p==1 else (1 if p==inf else p/(p-1))
    invp=0 if p==inf else 1/p
    return m*log((1+t)/(1-t)) + invp*log((1+t)/(1-t))-0.5*log(2*pi*m*t) - (0 if p==inf else log(p)/(2*p)) - (0 if q==inf else log(q)/(2*q))

if __name__=='__main__':
    cases=0
    for N in range(1,9):
        for m in range(N):
            for t in [Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(2,3),Fraction(9,10)]:
                verify_section(N,m,t)
                cases+=1
    print('Exact finite-section rank-one eigenprojection identities passed:',cases)
    for t in [0.2,0.5,0.8]:
        for p in [1,2,3,float('inf')]:
            vals=[round(exp(lognorm(m,t,p)-logasym(m,t,p)),5) for m in [30,80,180]]
            print('Asymptotic ratio',t,p,vals)
            assert 0.8<vals[-1]<1.2
    print('Asymptotic diagnostics passed (not a substitute for proof).')
