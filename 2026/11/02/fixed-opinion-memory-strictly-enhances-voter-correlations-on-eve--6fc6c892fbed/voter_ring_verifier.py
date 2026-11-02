"""Reproducibility checks for voter correlations with fixed-memory and fresh resets.

Pure Python 3, using only its standard library. Exact rational generator
checks are independent of the Green-function derivation.
"""
from fractions import Fraction as Q
from itertools import product
from math import acosh, cosh, exp, sinh, sqrt, tanh


def solve(A, b):
    a = [list(map(Q, row)) + [Q(v)] for row, v in zip(A, b)]
    n = len(a)
    for i in range(n):
        j = next(j for j in range(i, n) if a[j][i])
        a[i], a[j] = a[j], a[i]
        a[i] = [v / a[i][i] for v in a[i]]
        for j in range(n):
            if j != i and a[j][i]:
                c = a[j][i]
                a[j] = [a[j][k] - c*a[i][k] for k in range(n+1)]
    return [a[i][-1] for i in range(n)]


def exact_resolvent(N, r):
    L = [[(1+r if i==j else Q(0))
          - (Q(1,2) if j==(i-1)%N else Q(0))
          - (Q(1,2) if j==(i+1)%N else Q(0))
          for j in range(N)] for i in range(N)]
    e = [Q(i==0) for i in range(N)]
    G = solve(L, e)
    F = [sum(G[k]*G[(n-k)%N] for k in range(N)) for n in range(N)]
    P = [x/G[0] for x in G]
    C = [P[n] + r*r*(F[n]-P[n]*F[0]) for n in range(N)]
    return P,C


def exact_generator(N, r, memory):
    states = list(product((-1,1), repeat=N))
    idx = {x:i for i,x in enumerate(states)}
    Nstates=len(states)
    total=Q(0)
    for xi in states:
        generator = [[Q(0) for _ in range(Nstates)] for _ in range(Nstates)]
        for j,s in enumerate(states):
            for i in range(N):
                rate = Q(s[i]!=s[(i-1)%N],2)+Q(s[i]!=s[(i+1)%N],2)
                if memory:
                    rate += r*Q(s[i]!=xi[i])
                else:
                    rate += r/2
                changed=list(s);changed[i]=-changed[i]
                k=idx[tuple(changed)]
                generator[k][j]+=rate
                generator[j][j]-=rate
        generator[-1]=[Q(1)]*Nstates
        v=[Q(0)]*(Nstates-1)+[Q(1)]
        pi=solve(generator,v)
        total+=sum(pi[j]*s[0]*s[1] for j,s in enumerate(states)) / len(states)
    return total


def continuous(N,r,n):
    a=acosh(1+r)
    sh=sinh(a)
    h=N/2
    z=h-min(n,N-n)
    g=cosh(z*a)/(sh*sinh(h*a))
    p=cosh(z*a)/cosh(h*a)
    delta=r*r*g/sh*(h*tanh(h*a)-z*tanh(z*a))
    return p,p+delta,delta


def checks():
    count=0
    for N in (3,4):
        for r in (Q(1,3),Q(5,7)):
            P,C=exact_resolvent(N,r)
            assert exact_generator(N,r,True)==C[1]
            assert exact_generator(N,r,False)==P[1]
            assert C[0]==P[0]==1
            assert all(C[n]>P[n] for n in range(1,N))
            count+=4
    print('Exact rational generator checks:',count,'PASS')
    count=0
    for N in (3,4,5,8,12,24):
        for r in (0.005,0.3,1.7,10):
            for n in range(1,N):
                p,c,d=continuous(N,r,n)
                assert d>0 and c>p and 0<c<1
                count+=1
    print('All-distance strict ordering checks:',count,'PASS')
    count=0
    for lam in (0.2,2.,10.,30.):
        s=sqrt(lam/2)
        x=0.3
        profile=cosh(sqrt(2*lam)*(0.5-x))/cosh(s)
        wall=s*tanh(s)
        gap=lam/2*(1+2*s/sinh(2*s))
        last=None
        for N in (500,1000,2000):
            r=lam/N**2
            pf,cf,df=continuous(N,r,round(x*N))
            p1,c1,d1=continuous(N,r,1)
            errors=(abs(cf-profile),abs(N*(1-c1)/2-wall),abs(N*N*d1-gap))
            if last is not None:
                assert all(a<b for a,b in zip(errors,last)),(lam,N,errors,last)
            last=errors
            count+=3
    print('Finite-size profile, domain-wall, memory-gap scaling checks:',count,'PASS')

if __name__=='__main__':
    checks()
