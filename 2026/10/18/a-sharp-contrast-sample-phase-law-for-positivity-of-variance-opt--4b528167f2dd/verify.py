#!/usr/bin/env python3
"""Independent exact-arithmetic tests for a four-row Bernoulli Galerkin model.

Requires only Python 3 standard library. It checks the finite-state laws and
entrywise variance-optimal weights; it does not prove infinite-sample limits.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, sqrt, erf

# Orthonormal columns and independent leverage-1/2 Bernoulli draws.
U = ((Q(1,2),Q(1,2)),(-Q(1,2),-Q(1,2)),(Q(1,2),-Q(1,2)),(-Q(1,2),Q(1,2)))
T = ((Q(1),Q(0)),(Q(0),Q(1)))

def mat(h,l,bits,nu):
    w = (Q(h),Q(h),Q(l),Q(l))
    zero = [[Q(0),Q(0)],[Q(0),Q(0)]]
    yy = [row[:] for row in zero]
    tt = [row[:] for row in zero]
    for j in range(nu):
        for i in range(4):
            for a in range(2):
                for b in range(2):
                    x=Q(2,nu)*bits[4*j+i]*U[i][a]*U[i][b]
                    yy[a][b] += x*w[i]
                    tt[a][b] += x
    beta=Q(h+l,2)
    cb=[[yy[a][b]-beta*(tt[a][b]-T[a][b]) for b in range(2)] for a in range(2)]
    return yy,tt,cb

def spectrum(A):
    # These matrices have equal diagonals and symmetric off-diagonals.
    assert A[0][0]==A[1][1] and A[0][1]==A[1][0]
    return (A[0][0]+A[0][1], A[0][0]-A[0][1])

def probs(kappa,nu,theta):
    total=4**nu  # each independent 2nu-coordinate binomial has 2**(2nu)=4**nu equally weighted bit patterns
    # Invertibility of uncorrected: counts of each pair positive.
    pb=sum(comb(2*nu,k) for k in range(1,2*nu+1))/total
    cbad=sum(comb(2*nu,k) for k in range(2*nu+1)
             if Q(kappa+1,1)+Q(k,nu)*(Q(1)-Q(kappa))<=0)/total
    fbad=sum(comb(2*nu,k) for k in range(2*nu+1)
             if Q(kappa+1,1)+Q(k,nu)*(Q(theta)-Q(kappa-1))<=0)/total
    return Q(pb),Q(cbad),Q(fbad)

checks=0
assert sum(U[i][0]*U[i][0] for i in range(4))==1
assert sum(U[i][1]*U[i][1] for i in range(4))==1
assert sum(U[i][0]*U[i][1] for i in range(4))==0
checks+=3
for h,l,nu,theta in ((4,1,1,Q(1,4)), (3,1,1,Q(1,2)), (7,1,2,Q(1)), (6,2,2,Q(1,2)),(8,1,3,Q(2))):
    counts=[0,0,0,0,0]
    beta=Q(h+l,2)
    avg=(Q(h+l,2),Q(0),Q(0),Q(h+l,2))
    # Enumerating all 4nu independent Bernoulli choices.
    for bits in product((0,1),repeat=4*nu):
        yy,tt,cb=mat(h,l,bits,nu)
        plus=sum(bits[4*j+i] for j in range(nu) for i in (0,1))
        minus=sum(bits[4*j+i] for j in range(nu) for i in (2,3))
        yyp,yym=spectrum(yy)
        ttp,ttm=spectrum(tt)
        cbp,cbm=spectrum(cb)
        assert (yyp,yym)==(Q(h*plus,nu),Q(l*minus,nu));checks+=1
        assert (ttp,ttm)==(Q(plus,nu),Q(minus,nu));checks+=1
        assert (cbp,cbm)==(beta+Q(h-l,2)*Q(plus,nu),beta-Q(h-l,2)*Q(minus,nu));checks+=1
        assert cbp>0;checks+=1
        inv=(plus>0 and minus>0)
        bad=cbm<=0
        fused_bad=(Q(2)*cbm+theta*yym<=0)
        counts[0]+=inv
        counts[1]+=bad
        counts[2]+=inv and bad
        counts[3]+=inv and fused_bad
        counts[4]+=fused_bad
    total=2**(4*nu)
    pi,pb,pf=probs(Q(h,l),nu,theta)
    assert Q(counts[0],total)==pi*pi;checks+=1
    assert Q(counts[1],total)==pb;checks+=1
    assert Q(counts[2],total)==pi*pb;checks+=1
    assert Q(counts[3],total)==pi*pf;checks+=1
    assert Q(counts[4],total)==pf;checks+=1

# Optimal entrywise coefficient follows from exact independent variances.
for a,b in product((0,1),repeat=2):
    squares=[(U[i][a]*U[i][b])**2 for i in range(4)]
    for h,l in ((4,1),(7,2),(3,3)):
        pp=[h,h,l,l]
        beta=sum(Q(pp[i])*squares[i] for i in range(4))/sum(squares)
        assert beta==Q(h+l,2);checks+=1

# Exact Frobenius variance formulas, and variance-ratio ridge threshold.
for nu in range(1,6):
    for h,l in ((4,1),(7,2),(3,3)):
        v0=Q(h*h+l*l,2*nu)
        vb=Q((h-l)**2,4*nu)
        assert vb<=v0/2;checks+=1
        for K in range(2*nu+1):
            pm=Q(comb(2*nu,K),4**nu)
            assert pm>=0;checks+=1

# Independently compute exact Frobenius risk by binomial summation.
for nu in range(1,7):
    pmf=[Q(comb(2*nu,k),4**nu) for k in range(2*nu+1)]
    for h,l in ((5,1),(7,2),(3,3)):
        beta=Q(h+l,2)
        risk0=sum(pmf[k]*Q(h*h+l*l)*(Q(k,nu)-1)**2 for k in range(2*nu+1))
        riskb=sum(pmf[k]*Q((h-l)**2,2)*(Q(k,nu)-1)**2 for k in range(2*nu+1))
        assert risk0==Q(h*h+l*l,2*nu)
        assert riskb==Q((h-l)**2,4*nu)
        checks+=2

# In the single-sketch case the exact conditional bad-fusion probability is one third.
p0,pb,pf=probs(Q(7),1,Q(1))
assert p0==Q(3,4) and pb==Q(1,4) and pf==Q(1,4)
checks+=3

# Normal CDF transition: exact finite binomial tails are close to CLT values.
for nu in (200,1000):
    c=3.0
    kappa=c*sqrt(nu)
    threshold=nu*(kappa+1)/(kappa-1)
    lo=int(threshold) + (0 if threshold==int(threshold) else 1)
    # Stable log-PMF via logarithms to avoid huge intermediate integers.
    import math
    prob=sum(math.exp(math.lgamma(2*nu+1)-math.lgamma(j+1)-math.lgamma(2*nu-j+1)-2*nu*math.log(2)) for j in range(lo,2*nu+1))
    limit=.5*(1-erf((2*sqrt(2)/c)/sqrt(2)))
    assert abs(prob-limit)<.055,(nu,prob,limit)
    checks+=1
print('PASS',checks,'exact structural/enumeration and approximate CLT checks')
