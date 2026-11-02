"""Reproduce the five-cluster powered-distance calculation and its asymptotics.

Python >=3.10; numpy>=2 for independent full-matrix diagonalization.
Run: python verify_five_cluster.py
"""
from fractions import Fraction
from math import sqrt,log,exp,expm1,isclose
import random
import numpy as np

A=(sqrt(5)-1)/2
B=(sqrt(5)+1)/2
LOG2=log(2)
S_CRIT=exp(-A*LOG2)


def h(p,s):
    # h = A*2**p+s**p-B, stabilized near p=0.
    return A*expm1(p*LOG2)+expm1(p*log(s))


def root(m,s):
    assert m >= 2 and 0 < s <= 2
    def F(p): return m*h(p,s)-exp(p*log(s))
    l=0.0; r=4.0
    assert F(l)<0 and F(r)>0
    for _ in range(100):
        z=(l+r)/2
        if F(z)>0:r=z
        else:l=z
    return (l+r)/2


def limit_root(s):
    assert 0<s<S_CRIT
    l=1e-10;r=4.0
    assert h(l,s)<0<h(r,s)
    for _ in range(100):
        z=(l+r)/2
        if h(z,s)>0:r=z
        else:l=z
    return (l+r)/2


def distance(m,s):
    N=5*m
    D=np.zeros((N,N),dtype=float)
    for x in range(N):
        for y in range(x+1,N):
            i,j=x//m,y//m
            d=s if i==j else min((i-j)%5,(j-i)%5)
            D[x,y]=D[y,x]=d
    return D


def spectral(m,s,p):
    return (m*(A-B*2**p)+(m-1)*s**p,
            m*(-B+A*2**p)+(m-1)*s**p)

# Exact rational decomposition at p=1; direct metric pairs vs block identity.
rng=random.Random(41729)
ct_exact=0
for m in range(2,7):
    for ss in (Fraction(1,4),Fraction(2,3),Fraction(1),Fraction(7,5),Fraction(2)):
        N=5*m
        for _ in range(29):
            x=[rng.randint(-5,5) for _ in range(N-1)];x.append(-sum(x))
            assert sum(x)==0
            Q=Fraction(0)
            for i in range(N):
                for j in range(i+1,N):
                    a,b=i//m,j//m
                    d=ss if a==b else min((a-b)%5,(b-a)%5)
                    Q+=2*Fraction(d)*x[i]*x[j]
            g=[sum(x[k*m:(k+1)*m]) for k in range(5)]
            R=ss*sum(g[k]*g[k]-sum(x[k*m+j]**2 for j in range(m)) for k in range(5))
            R+=sum(2*min((k-l)%5,(l-k)%5)*g[k]*g[l] for k in range(5) for l in range(k+1,5))
            assert Q==R,(m,ss,Q,R)
            ct_exact+=1
print('EXACT_BLOCK_QUADRATIC_DECOMPOSITION_OK',ct_exact)

# Full-matrix independent diagonalization: compare every analytic spectral mode.
ct_eigen=0
for m in range(2,8):
    for s in (0.15,0.5,S_CRIT,0.9,1,1.7,2):
        for p in (0.1,0.5,1,1.3,root(m,s)):
            D=distance(m,s)**p
            eigen=np.linalg.eigvalsh(D)
            e1,e2=spectral(m,s,p)
            e0=(m*(2+2*2**p)+(m-1)*s**p)
            predicted=[-s**p]*(5*(m-1))+[e1]*2+[e2]*2+[e0]
            assert np.max(np.abs(eigen-np.sort(predicted)))<5e-11,(m,s,p,eigen,predicted)
            ct_eigen+=1
print('FULL_MATRIX_EIGENVALUES_OK',ct_eigen)

# Root, sharp strictness/failure and critical Euclidean rank.
ct_boundary=0
for m in (2,3,4,7,11,20):
    for s in (0.03,0.3,0.6,S_CRIT,0.77,1,1.6,2):
        p=root(m,s)
        e1,e2=spectral(m,s,p)
        assert e1 < -0.999999 and abs(e2)<1e-10
        assert spectral(m,s,p*.99)[1]<0
        assert spectral(m,s,p*1.01)[1]>0
        # exactly 2 zero modes on zero-sum space at criticality
        assert abs(e2)<1e-10 and -s**p<0 and e1<0
        ct_boundary+=1
print('SHARP_BOUNDARY_AND_CRITICAL_RANK_OK',ct_boundary)

# Three asymptotic regimes with explicit constants and separate limit checks.
for s in (0.18,0.36):
    pl=limit_root(s)
    v=root(100000,s)
    assert abs(pl-v)<2e-5,(s,pl,v)
    d=A*LOG2*exp(pl*LOG2)+log(s)*exp(pl*log(s))
    c=exp(pl*log(s))/d
    m=100000
    assert abs(m*(v-pl)/c-1)<1.5e-3,(s,c,m*(v-pl))
print('PERSISTENT_NONZERO_EXPONENT_AND_FIRST_CORRECTION_OK')

for m in (10000,100000,1000000):
    p=root(m,S_CRIT)
    assert abs(p*sqrt(m)/(sqrt(2)/LOG2)-1)<0.007,(m,p)
print('CRITICAL_INVERSE_SQUARE_ROOT_BRANCHING_OK')
for s in (0.8,1,1.4,2):
    c=1/(A*LOG2+log(s))
    m=100000
    assert abs(m*root(m,s)/c-1)<1.2e-4,(s,c,m*root(m,s))
print('SUPRACRITICAL_INVERSE_LINEAR_BRANCHING_OK')

# Special unweighted lexicographic blowups: equality to closed radicals.
for m in (2,3,5,10,100,1000):
    p1=log(1+1/(m*A))/LOG2
    p2=log((m*B)/(m*B-1))/LOG2
    assert abs(root(m,1)-p1)<1e-13 and abs(root(m,2)-p2)<1e-13
print('EXACT_GRAPH_BLOWUP_ENDPOINTS_OK')
print('ALL_FIVE_CLUSTER_ROUNDNESS_CHECKS_OK')
