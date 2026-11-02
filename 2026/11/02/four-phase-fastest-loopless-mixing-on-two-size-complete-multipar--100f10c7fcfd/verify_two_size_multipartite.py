#!/usr/bin/env python3
"""Exact-rational checks for loopless fastest mixing on two-size multipartite graphs.

Only Python's standard library is required. Matrix/eigenbasis tests and rational
minimax tests supplement the all-parameter analytic proof; finite tests alone
are not offered as a proof of the infinite family.
"""
from fractions import Fraction as F

assertions = 0
cases = 0


def check(ok, description):
    global assertions
    assertions += 1
    if not ok:
        raise AssertionError(description)


def solution(p, q, a, b):
    """p A-parts of size a, q B-parts of size b; p,q>=2 and a,b>=1."""
    r = F(p*a, q*b)
    if r <= F(1,q):
        x = F(1)
        mu = (1-r)/(q-1)
    elif r <= F(p,q):
        x = F(q,1)/(q-1+q*r)
        mu = 1/(q-1+q*r)
    elif r <= p:
        x = F(p,1)/(p+(p-1)*r)
        mu = r/(p+(p-1)*r)
    else:
        x = 1/r
        mu = (r-1)/(r*(p-1))
    aa=(1-x)/((p-1)*a)
    ab=x/(q*b)
    bb=(1-r*x)/((q-1)*b)
    return x,mu,aa,ab,bb


def scalar_checks(p,q,a,b):
    global cases
    cases += 1
    r=F(p*a,q*b)
    cap=min(F(1), 1/r)
    xa=F(p)/(p+(p-1)*r)
    xb=F(q)/(q-1+q*r)
    x,mu,aa,ab,bb=solution(p,q,a,b)
    check(x==min(cap,max(xa,xb)), 'crossover formula')
    check((xa>=xb)==(a>=b), 'active size comparison')
    check(F(0)<x<=cap, 'admissibility')
    check(min(aa,ab,bb)>=0, 'weight signs')
    check((aa==0)==(p*a<=b), 'A-to-A deletion threshold')
    check((bb==0)==(a>=q*b), 'B-to-B deletion threshold')
    check((p-1)*a*aa+q*b*ab==1, 'A row sum')
    check((q-1)*b*bb+p*a*ab==1, 'B row sum')
    lamA= -a*aa
    lamB= -b*bb
    lamC=1-(1+r)*x
    check(mu==max(abs(lamA),abs(lamB),abs(lamC)), 'exact SLEM')
    for k in range(101):
        z=cap*F(k,100)
        A=(1-z)/(p-1)
        B=(1-r*z)/(q-1)
        D=abs(1-(1+r)*z)
        check(max(A,B,D)>=mu, 'rational grid competitor')


def full_matrix_checks(p,q,a,b):
    x,mu,aa,ab,bb=solution(p,q,a,b)
    sizes=[a]*p+[b]*q
    memberships=[i for i,s in enumerate(sizes) for _ in range(s)]
    N=len(memberships)
    starts=[0]
    for s in sizes: starts.append(starts[-1]+s)
    M=[[F(0)]*N for _ in range(N)]
    for i in range(N):
        u=memberships[i]
        for j in range(N):
            v=memberships[j]
            if u==v: continue
            M[i][j]=aa if u<p and v<p else bb if u>=p and v>=p else ab
    check(all(M[i][i]==0 for i in range(N)), 'zero diagonal')
    check(all(sum(M[i])==1 for i in range(N)), 'stochastic rows')
    check(all(M[i][j]==M[j][i] and M[i][j]>=0 for i in range(N) for j in range(N)), 'symmetric nonnegative')
    def eig(v,lam):
        for i in range(N):
            check(sum(M[i][j]*v[j] for j in range(N))==lam*v[i], 'full eigenvector')
    eig([F(1)]*N,F(1))
    for k in range(1,p):
        v=[F(1) if z==0 else F(-1) if z==k else F(0) for z in memberships]
        eig(v,-a*aa)
    for k in range(p+1,p+q):
        v=[F(1) if z==p else F(-1) if z==k else F(0) for z in memberships]
        eig(v,-b*bb)
    # The A/B macro contrast is orthogonal to the all-ones vector.
    eig([F(q*b) if z<p else F(-p*a) for z in memberships], 1-(p*a+q*b)*ab)
    for cls in range(p+q):
        for j in range(starts[cls]+1,starts[cls+1]):
            v=[F(0)]*N
            v[starts[cls]]=1
            v[j]=-1
            eig(v,F(0))


# Analytic identities/crossover/certificate sampled over an extended grid.
for p in range(2,9):
    for q in range(2,9):
        for a in range(1,11):
            for b in range(1,11):
                scalar_checks(p,q,a,b)
# Full matrices also checked from their independently constructed edge rule.
full_cases=0
for p in range(2,5):
    for q in range(2,5):
        for a in range(1,5):
            for b in range(1,5):
                full_matrix_checks(p,q,a,b)
                full_cases+=1
print('PASS: {} exact rational assertions; {} parameter cases; {} full matrix eigenbasis cases'.format(assertions,cases,full_cases))
