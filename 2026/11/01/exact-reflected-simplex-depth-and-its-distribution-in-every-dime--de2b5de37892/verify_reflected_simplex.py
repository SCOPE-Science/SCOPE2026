#!/usr/bin/env python3
"""Independent arithmetic and sampling checks of reflected-simplex depth formulas.
This file uses only the Python standard library; simulations are finite checks."""
from fractions import Fraction as Q
from math import comb, exp, log
from random import Random

RNG=Random(20261031)
checks=0

def cap_mass(z, d):
    """Independent full-subset inclusion-exclusion for Dirichlet(1,...,1)."""
    n=d+1
    total=type(z[0])(0)
    for mask in range(1<<n):
        s=sum((z[j] for j in range(n) if (mask>>j)&1),type(z[0])(0))
        if s<1:
            total+=(-1 if mask.bit_count()%2 else 1)*(1-s)**d
    return total

def two_level(d,a):
    b=(2-a)/d
    return sum((-1)**k*comb(d,k)*(max(type(a)(0),1-k*b)**d-max(type(a)(0),1-a-k*b)**d) for k in range(d+1))

def baseline(d):
    m=d+1;c=Q(2,m)
    return 1-sum((-1)**k*comb(m,k)*max(Q(0),1-k*c)**d for k in range(m+1))

def level_prob(d,u):
    return sum((-1)**k*comb(d+1,k)*max(type(u)(0),1-k*u)**d for k in range(d+2))

for d in range(2,13):
    m=d+1;c=Q(2,m)
    vals=[]
    for j in range(21):
        a=c*j/20;b=(2-a)/d
        f=two_level(d,a)
        direct=cap_mass([a]+[b]*d,d)
        assert f==direct,(d,j,f,direct)
        vals.append(f);checks+=1
    assert vals[0]==0 and all(vals[j]<vals[j+1] for j in range(20));checks+=1
    b=baseline(d)
    assert b==1-level_prob(d,c);checks+=1
    atom=sum((-1)**(k+1)*comb(m,k)*max(Q(0),1-k*c)**d for k in range(1,m+1))
    assert b==atom;checks+=1

# Independently verify the first two explicit depth profiles.
for j in range(101):
    a=Q(j,150)
    if a<=Q(2,3):
        assert two_level(2,a)==2*a-Q(3,2)*a*a
        checks+=1
    a=Q(j,200)
    if a<=Q(1,2):
        assert two_level(3,a)==2*a*(1-a)
        checks+=1
assert baseline(2)==Q(1,3) and baseline(3)==Q(1,2)
assert 1-two_level(3,Q(1,4))==Q(5,8)
checks+=3

# Random Dirichlet point tests against direct cap-volume inclusion-exclusion.
for d in (2,3,4,5):
    m=d+1;c=2/m
    for trial in range(160):
        y=[RNG.expovariate(1) for _ in range(m)]
        s=sum(y); y=[v/s for v in y]
        a=min(max(y),c)
        predicted=two_level(d,a)
        # Search random translations that exclude y; none may exceed predicted value.
        for iteration in range(120):
            z=[RNG.expovariate(1) for _ in range(m)]
            z=[2*w/sum(z) for w in z]
            if any(z[i]<y[i] for i in range(m)):
                actual=cap_mass(z,d)
                assert actual<=predicted+1e-10,(d,y,z,actual,predicted)
                checks+=1
        # Independent Dirichlet Monte Carlo volume estimate for a few configurations.
        if trial<4:
            z=[a]+[(2-a)/d]*d
            hits=0; N=10000
            for _ in range(N):
                v=[RNG.expovariate(1) for _ in range(m)]
                s=sum(v)
                hits+=all(v[j]/s<=z[j] for j in range(m))
            assert abs(hits/N-predicted)<0.027,(d,hits/N,predicted)
            checks+=1

# Demonstrate reflected simplex region and probability-law formula for sample thresholds.
for d in range(2,8):
    c=2/(d+1)
    lower=1-baseline(d)
    center=two_level(d,1/(d+1))
    assert center<lower
    for j in range(1,20):
        u=(1/(d+1))*(1-j/20)+c*(j/20)
        alpha=1-two_level(d,u)
        assert float(baseline(d))<alpha<float(1-center)
        pr=level_prob(d,u)
        assert 0<pr<1
        checks+=1

print('PASS',checks,'exact or independently sampled checks')
