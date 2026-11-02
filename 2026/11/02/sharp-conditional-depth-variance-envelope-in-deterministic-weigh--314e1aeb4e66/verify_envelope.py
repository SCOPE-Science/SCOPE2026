#!/usr/bin/env python3
"""Exact finite verification for an innovation-variance envelope."""
from fractions import Fraction as Q
from itertools import product
from math import factorial, log, sqrt
checks=0

def check(b):
 global checks
 assert b
 checks+=1

def law(p):
    # Finite independent-parent model: p[j]=w_j/W_j, j>=2.
    weights=[Q(1)]
    for q in p:
        weights.append(sum(weights)*q/(1-q))
    probs=[]
    for j in range(2,len(weights)+1):
        s=sum(weights[:j-1]); probs.append([w/s for w in weights[:j-1]])
    return probs

def enumerate_v(p):
    probs=law(p)
    v=[Q(0)]*(len(p)+2)
    for choices in product(*(range(j) for j in range(1,len(p)+1))):
        depth=[Q(0)]; prob=Q(1); xis=[]
        for j,par in enumerate(choices, start=2):
            prob*=probs[j-2][par]
            pre_mean=sum(probs[j-2][k]*(1+depth[k]) for k in range(j-1))
            xi=1+depth[par]-pre_mean
            xis.append((j,xi))
            depth.append(1+depth[par])
        for j,xi in xis:
            v[j]+=prob*xi*xi
    return v

def rec(p):
    v=Q(0); out=[v]
    for q in p:
        v=(1-q*q)*v+q*(1-q)
        out.append(v)
    return out

# Independent finite-word enumeration; no infinite conclusion inferred.
for p in [(Q(1,2),Q(1,3),Q(1,4)),(Q(2,5),Q(3,7),Q(4,9)),(Q(1,4),Q(3,4),Q(1,5))]:
    vv=enumerate_v(p)
    rr=rec(p)
    for j in range(2,len(p)+2):
        check(vv[j]==rr[j-2])

# Dynamic programming over a rational grid, followed by exact algebraic check.
vmax=Q(0)
for j in range(2,10):
    opt=Q(1,2*(vmax+1))
    nxt=vmax+Q(1,4*(vmax+1))
    for k in range(1,100):
        p=Q(k,100)
        val=vmax+p-(vmax+1)*p*p
        check(val<=nxt)
        check(nxt-val==(vmax+1)*(p-opt)**2)
    vmax=nxt

# Exact deficit identity and global dominance for nonextremal independent profiles.
for pseq in [(Q(1,3),Q(1,7),Q(2,9),Q(5,8)),(Q(9,10),Q(1,13),Q(2,3),Q(1,5))]:
    v=Q(0); vmax=Q(0); prev_delta=Q(0)
    for p in pseq:
        q=Q(1,2*(v+1))
        nv=v+p-(v+1)*p*p
        nm=vmax+Q(1,4*(vmax+1))
        delta=nm-nv
        expression=(1-Q(1,4*(vmax+1)*(v+1)))*prev_delta+(v+1)*(p-q)**2
        check(delta==expression)
        check(delta>=0)
        v,vmax,prev_delta=nv,nm,delta

# The deterministic asymptotic shape is tested numerically, not treated as proof.
v=0.
for j in range(2,100001):
    v+=1/(4*(v+1))
    if j in (1000,10000,100000):
        target=j/2+log(j)/8
        check(abs((v+1)**2-target)<2.5)
print('exact_assertions_passed=',checks)
print('optimal_v_100001=',format(v,'.12f'))
print('note=finite checks only; asymptotic proof is separate')
