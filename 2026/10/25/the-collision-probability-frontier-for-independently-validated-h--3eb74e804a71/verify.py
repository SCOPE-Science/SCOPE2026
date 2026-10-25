#!/usr/bin/env python3
"""Exact, finite checks for independent-validation coordinate models."""
from fractions import Fraction as F
from itertools import product
from random import Random


def loss(p, h, x, i):
    return h * x[i] * x[i] / (2 * p[i])


def step(p, h, x, a, i):
    out = list(x)
    out[i] = (1 - a * h / p[i]) * x[i]
    return tuple(out)


def feedback(p, h, x, a, i, j):
    if not x[i]:
        raise ValueError('zero sampled gradient: feedback undefined')
    y = step(p, h, x, a, i)
    return (loss(p,h,y,j) - loss(p,h,x,j)) / ((h * x[i] / p[i])**2)


def protected_step(p, h, x, a, i, j, tie_accept=True):
    y=step(p,h,x,a,i)
    new_loss = loss(p,h,y,j)
    old_loss = loss(p,h,x,j)
    if new_loss<old_loss or (tie_accept and new_loss==old_loss):
        return y
    return x


def distribution_mse(p,h,a,x,k,tie_accept=True):
    dist={tuple(x):F(1)}
    for _ in range(k):
        nd={}
        for state,weight in dist.items():
            for i,j in product(range(len(p)), repeat=2):
                y=protected_step(p,h,state,a,i,j,tie_accept)
                nd[y]=nd.get(y,F(0))+weight*p[i]*p[j]
        dist=nd
        assert sum(dist.values())==1
    return tuple(sum(weight*state[i]**2 for state,weight in dist.items()) for i in range(len(p))), len(dist)


def check_case(p,h):
    d=len(p)
    assert sum(p)==1 and all(t>0 for t in p)
    c=sum(v*v for v in p)
    a=c/h
    x=tuple(F(i+1,2) for i in range(d))
    for trial in (F(0), F(1,10), F(3,7), a, F(2,1)):
        lhs=sum(p[i]*p[j]*feedback(p,h,x,trial,i,j) for i,j in product(range(d),repeat=2))
        rhs=h*trial*trial/2-c*trial
        assert lhs==rhs, (p,trial,lhs,rhs)
    for i in range(d):
        raw_mse = sum(p[j]*step(p,h,x,a,j)[i]**2 for j in range(d))
        raw_rho = 1-2*c + c*c/p[i]
        assert raw_mse == raw_rho*x[i]**2
        gate_mse = sum(p[j]*p[l]*protected_step(p,h,x,a,j,l)[i]**2 for j,l in product(range(d),repeat=2))
        if c < 2*p[i]:
            gate_rho=1-p[i]*(1-(1-c/p[i])**2)
        elif c > 2*p[i]:
            gate_rho=1+p[i]*(1-p[i])*((1-c/p[i])**2-1)
        else:
            gate_rho=1
        assert gate_mse == gate_rho*x[i]**2, (p,i,gate_mse,gate_rho)
        assert (abs(1-c/p[i])<1)==(c<2*p[i])


checks=0
rng=Random(20261023)
for d in range(2,7):
    for _ in range(75):
        ints=[rng.randrange(1,50) for _ in range(d)]
        p=tuple(F(i,sum(ints)) for i in ints)
        check_case(p,F(rng.randrange(1,21),rng.randrange(1,21)))
        checks+=1

p=(F(1,4),F(3,4)); h=F(1); c=F(5,8); a=c
assert sum(t*t for t in p)==c
assert 1-a/p[0] == -F(3,2)
assert 1-2*c + c*c/p[0] == F(21,16)
assert 1+p[0]*(1-p[0])*((1-a/p[0])**2-1) == F(79,64)
for k in range(1,5):
    mse,states=distribution_mse(p,h,a,(F(1),F(1)),k,True)
    assert mse[0] == F(79,64)**k, (k,mse,states)
    assert states <= 4**k

for d in range(2,15):
    # At each rational m below (respectively above) threshold, verify
    # extremal distribution fails (respectively succeeds), for a grid.
    for den in range(d,5*d+1):
        m=F(1,den)
        p=(1-(d-1)*m,)+(m,)*(d-1)
        c=sum(t*t for t in p)
        assert (c<2*m)==(d*(d-1)*m*m-2*d*m+1 < 0)
        checks+=1

print('PASS: 375 exact full-feedback and gate cases,',checks,'total cases; 4 epoch-enumerations and exact collision-threshold grid.')
