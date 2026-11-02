#!/usr/bin/env python3
"""Finite checks for the metric structure of two-choice Bernoulli recursive trees.
No simulation is a proof of any asymptotic assertion.
"""
from itertools import product
from collections import Counter
import random

checks=0

def ck(cond,msg='assertion'):
    global checks
    assert cond,msg
    checks+=1

def construct(bits):
    n=len(bits)+2
    p=[0]*(n+1);h=[0]*(n+1);p[2]=1;h[2]=1
    step=[0]*(n+1); step[2]=1
    for i,b in enumerate(bits,3):
        ck(b in (1,2));p[i]=i-b;h[i]=h[p[i]]+1
        step[i]=1 if b==1 else step[i-1]+1
        ck(h[i]-h[i-1] in (0,1),'monotone depth increments')
        ck(h[i]-h[i-1] == (1 if b==1 else 1-(h[i-1]-h[i-2])))
    return p,h,step

def lca(p,a,b):
    ancestors=set()
    while a:
        ancestors.add(a);a=p[a]
    while b not in ancestors:b=p[b]
    return b

def distance(p,h,a,b):
    c=lca(p,a,b);return h[a]+h[b]-2*h[c]

def diameter_bruteforce(p,h):
    n=len(p)-1
    return max(distance(p,h,a,b) for a in range(1,n+1) for b in range(a+1,n+1))

def diameter_linear(p):
    n=len(p)-1;branch=[0]*(n+1);diam=0
    for i in range(n,1,-1):
        u=p[i];diam=max(diam,branch[u]+branch[i]+1)
        branch[u]=max(branch[u],branch[i]+1)
    return diam

# Exhaustive deterministic enumeration, including both pure path and alternating arms.
profiles=0
for n in range(2,15):
    for bits in product((1,2),repeat=n-2):
        p,h,D=construct(bits)
        ck(diameter_bruteforce(p,h)==diameter_linear(p),'diameter algorithms')
        ck(h[-1] == max(h[1:]),'latest height is maximum depth')
        for i in range(2,n+1):
            ck(D[i]==distance(p,h,i,i-1),'adjacent depth formula')
            for j in range(i+1,n+1):
                e=distance(p,h,i,j)-h[j]
                ck(e in (-h[i],D[i]-h[i-1]),'two-crossing distance identity')
                ck(e<=max(-h[i],D[i]-h[i-1]),'local upper bound')
        profiles+=1

# Almost-sure stabilization only explored numerically; this finite check is not a proof.
r=random.Random(20261030)
for prob in (0.2,0.5,0.8):
    for rep in range(25):
        n=1400;bits=[1 if r.random()<prob else 2 for _ in range(n-2)]
        p,h,D=construct(bits)
        diam=diameter_linear(p)
        ck(diam>=h[n])
        ck(max(D)<=diam)
        ck(diam-h[n]<=max(max(-h[i],D[i]-h[i-1]) for i in range(2,n+1)),'finite upper certificate')

print('all assertions passed:',checks,'exhaustive profiles:',profiles,'random trees:',75)
