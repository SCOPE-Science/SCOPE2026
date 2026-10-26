"""Exact finite-field rank-process and regenerative extreme-value checks."""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np

def pprod(q,n):
    x=F(1)
    for a in range(1,n+1): x*=1-F(1,q**a)
    return x

def transitions(q,j):
    up=F(1,q**(2*j+1))
    down=(1-F(1,q**j))**2 if j else F(0)
    return down,1-up-down,up

def exact_rank_prob(q,n,j):
    return F(1,q**(j*j))*pprod(q,n)**2/(pprod(q,j)**2*pprod(q,n-j))

checks=0
for q in [2,3,4,5]:
    distrib={0:F(1)}
    for n in range(1,14):
        nxt={j:F(0) for j in range(n+1)}
        for j,v in distrib.items():
            down,hold,up=transitions(q,j)
            if j:nxt[j-1]+=v*down
            nxt[j]+=v*hold
            nxt[j+1]+=v*up
        distrib=nxt
        for j in range(n+1):
            assert distrib[j]==exact_rank_prob(q,n,j),(q,n,j)
            checks+=1
    # Exact gambler's-ruin formula, using the corresponding harmonic recurrence.
    for k in range(2,13):
        s=[F(1)]
        for j in range(1,k):
            down,hold,up=transitions(q,j)
            s.append(s[-1]*down/up)
        r=1/sum(s)
        f=[F(0)] + [sum(s[:j])/sum(s) for j in range(1,k)] + [F(1)]
        for j in range(1,k):
            down,hold,up=transitions(q,j)
            assert f[j]==down*f[j-1]+hold*f[j]+up*f[j+1], (q,k,j)
            checks+=1
        assert f[1]==r

# Algebraic enumeration of the rank of the residual block, F_2 and F_3 cases.
for q in (2,3):
    for j in range(0,4 if q==2 else 3):
        counts={-1:0,0:0,1:0}
        for v in product(range(q),repeat=j):
            for w in product(range(q),repeat=j):
                for a in range(q):
                    if any(v) and any(w): delta=2
                    elif any(v) or any(w) or a: delta=1
                    else: delta=0
                    counts[1-delta]+=1
        down,hold,up=transitions(q,j)
        denom=q**(2*j+1)
        assert (F(counts[-1],denom),F(counts[0],denom),F(counts[1],denom))==(down,hold,up)
        checks+=3

# Rare-event finite-horizon survival via killed Markov matrices.
for q in (2,3):
    pp=math.prod(1-q**(-i) for i in range(1,120))
    for k in (2,3,4):
        if q**(k*k)>2**55:continue
        n=q**(k*k)
        P=np.zeros((k,k),float)
        for j in range(k):
            d,h,u=transitions(q,j)
            if j:P[j,j-1]=float(d)
            P[j,j]=float(h)
            if j+1<k:P[j,j+1]=float(u)
        surv=np.linalg.matrix_power(P,n)[0,:].sum()
        ss=1.0
        sumss=1.0
        for i in range(1,k):
            d,h,u=transitions(q,i)
            ss*=float(d/u)
            sumss+=ss
        rare=1/sumss
        rescaled=rare*q**(k*k-1)*pp*pp
        print(f'q={q} k={k} horizon={n} P(max<k)={surv:.12g} limit={math.exp(-1/pp):.12g} P_hitting={rare:.12g} normalized_hitting={rescaled:.12g}')
print('exact checks:',checks)
