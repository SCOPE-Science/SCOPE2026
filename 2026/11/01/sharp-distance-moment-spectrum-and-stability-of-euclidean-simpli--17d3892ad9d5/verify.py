#!/usr/bin/env python3
"""Independent finite checks for the simplex pair-distance moment spectrum.
Requires only the Python standard library; finite checks do not replace proof.
"""
from fractions import Fraction as F
from math import factorial, comb
from collections import Counter
from itertools import product
import random

rng=random.Random(20261031)
checks=0

def assert_eq(a,b):
    global checks
    assert a==b, (a,b)
    checks+=1

def gram_from_vertices(points):
    n=len(points)
    d=len(points[0])
    centered=[[n*points[i][k]-sum(points[j][k] for j in range(n)) for k in range(d)] for i in range(n)]
    return [[sum(centered[i][k]*centered[j][k] for k in range(d)) for j in range(n)] for i in range(n)]

def invariants(G):
    n=len(G)
    S=sum(G[i][i] for i in range(n))
    T=sum(G[i][j]**2 for i in range(n) for j in range(n))
    H=sum(G[i][i]**2 for i in range(n))
    return S,T,H

def formula(G):
    n=len(G)
    S,T,H=map(F,invariants(G))
    q=n*(n+1)*(n+2)*(n+3)
    mu=2*S/(n*(n+1))
    E4=(S*S+2*T+6*H)/q
    nu=2*E4+2*(S/(n*(n+1)))**2+4*T/(n*n*(n+1)**2)
    return mu,nu,E4

def direct_fourth(G):
    n=len(G)
    total=F(0)
    den=factorial(n+3)//factorial(n-1)
    for ix in product(range(n),repeat=4):
        c=Counter(ix)
        numer=1
        for multiplicity in c.values():
            numer*=factorial(multiplicity)
        total+=F(numer,den)*G[ix[0]][ix[1]]*G[ix[2]][ix[3]]
    return total

def benchmarks(n):
    k=F(n*(n+1)*(n+6),(n-1)*(n+2)*(n+3))
    upper=F(6*n**3,(n-1)*(n+2)*(n+3))
    A=F(2*(n*n+3*n+3),(n+2)*(n+3))
    B=F(3*n*(n+1),(n+2)*(n+3))
    return k,upper,A,B

# Direct Dirichlet enumeration uses a completely independent 4-index sum.
for n in range(4,7):
    for _ in range(9):
        pts=[[rng.randrange(-6,7) for _ in range(n-1)] for _ in range(n)]
        G=gram_from_vertices(pts)
        S,T,H=map(F,invariants(G))
        mu,nu,e4=formula(G)
        assert_eq(e4,direct_fourth(G))
        assert_eq(mu,F(2*S,n*(n+1)))
        base,upper,A,B=benchmarks(n)
        excess=nu/mu**2-base
        decomposition=A*(T-S*S/(n-1))/S**2 + B*(H-S*S/n)/S**2
        assert_eq(excess,decomposition)
        assert 0<=excess and nu/mu**2<upper
        checks+=1
        E=[[F(G[i][j])-S*F(int(i==j),n-1)+S*F(1,n*(n-1)) for j in range(n)] for i in range(n)]
        E2=sum(x*x for row in E for x in row)
        assert_eq(E2,T-S*S/(n-1))
        esq=2*S/(n-1)
        for i in range(n):
            for j in range(i+1,n):
                delta=G[i][i]+G[j][j]-2*G[i][j]
                dev=F(delta,1)/esq-1
                assert dev*dev <= (n-1)**2 *excess/A
                checks+=1

# Exact regular-to-spike Gram interpolation: every interior value in [lower,upper).
for n in range(4,11):
    S=n*(n-1)
    w=[n-1]+[-1]*(n-1)
    G0=[[n*int(i==j)-1 for j in range(n)] for i in range(n)]
    G1=[[w[i]*w[j] for j in range(n)] for i in range(n)]
    lower,upper,A,B=benchmarks(n)
    for t in (F(0),F(1,7),F(1,3),F(1,2),F(5,6),F(1)):
        G=[[(1-t)*G0[i][j]+t*G1[i][j] for j in range(n)] for i in range(n)]
        S0,T,H=map(F,invariants(G))
        assert_eq(S0,F(S))
        mu,nu,_=formula(G)
        assert_eq(nu/mu**2,lower+t*t*(upper-lower))
        if t<1:
            assert nu/mu**2<upper
            checks+=1
        else:
            assert_eq(T,S*S)
            assert_eq(H,F((n*n-3*n+3)*S*S,n*(n-1)))
    # Scalar zero-sum two-level extremal comparison (analytic proof in RESULT.md).
    for k in range(1,n):
        fourth=F(n,k*(n-k))-F(3,n)
        assert fourth<=F(n*n-3*n+3,n*(n-1))
        checks+=1

# Sampled barycentric point-pair distances: independent check of moments.
for n in (4,5):
    pts=[[float((2 if j==i else 0) + (i*j)/11) for j in range(n-1)] for i in range(n)]
    G=gram_from_vertices([[F(x).limit_denominator(1000) for x in p] for p in pts])
    _,nu_exact,_=formula(G)
    scale=n*n  # centered coordinates are n times original centered vertices
    exact=float(nu_exact)/(scale**2)
    total=0.
    R=14000
    for rep in range(R):
        p=[rng.expovariate(1.) for _ in range(n)]
        q=[rng.expovariate(1.) for _ in range(n)]
        ps,qs=sum(p),sum(q)
        u=[z/ps for z in p]
        v=[z/qs for z in q]
        vec=[sum((u[i]-v[i])*pts[i][j] for i in range(n)) for j in range(n-1)]
        total+=sum(z*z for z in vec)**2
    assert abs(total/R-exact)<0.09*exact,(n,total/R,exact)
    checks+=1
print('VERIFY_OK',checks,'exact identities and seeded pair-distance tests')
