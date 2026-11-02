"""Reproducible finite-state checks for mean-preserving integer rounding.

This program checks exact finite instances; the asymptotic Gaussian law
requires the analytic martingale argument given in RESULT.md.
Requires only Python 3.10+ standard library.
"""
from fractions import Fraction as F
from math import floor, ceil, sqrt
import random


def frac(a):
    return a - floor(a)


def psi(a):
    r = frac(a)
    return r * (1-r)


def states(theta, q):
    radius = 1 / (1-q)
    return list(range(ceil(theta-radius),floor(theta+radius)+1))


def kernel(theta, q):
    domain = states(theta,q)
    pos = {x:i for i,x in enumerate(domain)}
    p = [[F(0) for _ in domain] for _ in domain]
    for i,x in enumerate(domain):
        y=(1+q)*theta-q*x
        lo=floor(y)
        r=frac(y)
        assert lo in pos
        p[i][pos[lo]] += 1-r
        if r:
            assert lo+1 in pos
            p[i][pos[lo+1]] += r
        assert sum(p[i]) == 1
        assert sum(p[i][j]*domain[j] for j in range(len(domain))) == y
        assert sum(p[i][j]*(domain[j]-y)**2 for j in range(len(domain))) == psi(y)
    return domain,p


def solve_linear(a,b):
    n=len(b)
    t=[row[:] + [z] for row,z in zip(a,b)]
    for col in range(n):
        piv=next(i for i in range(col,n) if t[i][col])
        t[col],t[piv]=t[piv],t[col]
        m=t[col][col]
        t[col]=[v/m for v in t[col]]
        for i in range(n):
            if i==col: continue
            m=t[i][col]
            if m:
                t[i]=[u-m*v for u,v in zip(t[i],t[col])]
    return [row[-1] for row in t]


def stationary(domain,p):
    n=len(domain)
    A=[[p[j][i]-int(i==j) for j in range(n)] for i in range(n)]
    A[-1]=[F(1)]*n
    b=[F(0)]*(n-1)+[F(1)]
    probs=solve_linear(A,b)
    assert all(u>=0 for u in probs)
    assert sum(probs)==1
    assert all(sum(probs[i]*p[i][j] for i in range(n))==probs[j] for j in range(n))
    return probs


def exact_checks():
    tests=0
    for theta in [F(1,5), F(3,10), F(1,2), F(7,10)]:
        for q in [F(1,4),F(1,2),F(2,3),F(3,4),F(9,10)]:
            d,p=kernel(theta,q)
            pi=stationary(d,p)
            mean=sum(w*x for x,w in zip(d,pi))
            var=sum(w*(x-theta)**2 for x,w in zip(d,pi))
            assert mean==theta
            assert (1-q*q)*var==sum(w*psi((1+q)*theta-q*x) for x,w in zip(d,pi))
            assert (1-q*q)*var<=F(1,4)
            assert abs((1-q*q)*var-psi(2*theta))<= (1-q)*sqrt(float(var))+1e-12
            if theta==F(1,2):
                assert var==F(1,4)
                assert all(w==(F(1,2) if x in (0,1) else 0) for x,w in zip(d,pi))
            c1=sum(pi[i]*p[i][j]*(d[i]-theta)*(d[j]-theta)
                   for i in range(len(d)) for j in range(len(d)))
            assert c1==-q*var
            tests+=8
    return tests


def numerical_checks():
    tests=0
    theta=F(3,10)
    c=float(psi(2*theta))
    for q in [F(9,10),F(19,20),F(49,50)]:
        d,p=kernel(theta,q)
        n=len(d)
        pf=[[float(a) for a in row] for row in p]
        z=[0.]*n
        z[d.index(0)]=1.
        # Exactly the finite-state transition kernel, approximate stationary by powers.
        for k in range(15000):
            nz=[0.]*n
            for i in range(n):
                if z[i]:
                    for j in range(n):
                        if pf[i][j]:
                            nz[j]+=z[i]*pf[i][j]
            z=nz
        assert abs(sum(z)-1)<1e-9
        m=sum(t*x for t,x in zip(z,d))
        v=sum(t*(x-float(theta))**2 for t,x in zip(z,d))
        scaled=(1-float(q*q))*v
        assert abs(m-float(theta))<1e-7
        assert abs(scaled-c)<=0.25*sqrt(1-float(q))
        tests+=3
    return tests


if __name__ == '__main__':
    a=exact_checks()
    b=numerical_checks()
    print('PASS: exact-rational instance checks:',a)
    print('PASS: floating-point finite-state checks:',b)
    print('Asymptotic central limit theorem is established analytically, not by these finite tests.')
