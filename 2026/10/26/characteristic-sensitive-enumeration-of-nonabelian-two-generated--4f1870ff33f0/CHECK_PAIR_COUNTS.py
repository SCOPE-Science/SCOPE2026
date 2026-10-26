#!/usr/bin/env python3
"""Exhaustive and seeded finite-field checks of the two-generator span in n4."""
from collections import Counter
from itertools import product
from random import Random
import sys

def bracket(x,y,q):
    a,b,c,d,e,f=x; A,B,C,D,E,F=y
    return (0,0,0,(a*B-b*A)%q,(b*C-c*B)%q,(a*E-e*A+d*C-c*D)%q)

def rank_mod(vectors,q):
    basis={};rank=0
    for vec in vectors:
        w=list(vec)
        for piv,b in sorted(basis.items()):
            if w[piv]:
                k=w[piv]
                w=[(z-k*t)%q for z,t in zip(w,b)]
        pos=next((i for i,z in enumerate(w) if z),None)
        if pos is None:continue
        inv=pow(w[pos],-1,q)
        basis[pos]=[(inv*z)%q for z in w]
        rank+=1
    return rank

def class_dim(x,y,q):
    z=bracket(x,y,q)
    u=bracket(x,z,q);v=bracket(y,z,q)
    r=rank_mod([x,y,z,u,v],q)
    cls=3 if any(u) or any(v) else 2 if any(z) else 1 if any(x) or any(y) else 0
    return (r,cls)

def formulas(q,p):
    B=(q*q-1)*(q*q-q);L=q*q+q+1
    H=q+1 if p==2 else 2
    K=L-1-H
    counts={
      0:1,
      1:(q**3-1)*(q+1) + L*(q*q-1)*q**3,
      2:(q**3-1)*(q**3-q) +(q*q-1)*((q**6-q**3)+(L-1)*(q**5-q**3))+B*q**5,
      3:(q*q-1)*(L-1)*(q-1)*q**5 + B*((q-1)*q**5+H*q**6),
      4:K*B*q**6
    }
    assert sum(counts.values())==q**12,(q,counts,sum(counts.values()))
    return counts

def run(q,full=True):
    pred=formulas(q,q)
    if full:
        E=tuple(product(range(q),repeat=6))
        counts=Counter(); classes=Counter()
        for x in E:
            for y in E:
                d,c=class_dim(x,y,q)
                counts[d]+=1;classes[c]+=1
        assert counts==Counter(pred),(q,counts,pred)
        exp3=pred[4]
        assert classes[3]==exp3,(classes,exp3)
        print('EXHAUSTIVE',q,'pairs',q**12,'ranks',dict(sorted(counts.items())),'classes',dict(sorted(classes.items())))
    else:
        rng=Random(314159)
        for _ in range(15000):
            x=tuple(rng.randrange(q) for _ in range(6));y=tuple(rng.randrange(q) for _ in range(6)); z=bracket(x,y,q)
            a,b,c=x[:3];A,B,C=y[:3]
            alpha=(a*B-b*A)%q;beta=(b*C-c*B)%q;tau=(a*C-c*A)%q
            P=rank_mod([x[:3],y[:3]],q)
            cls=class_dim(x,y,q)[1]
            if P==2:
                if not alpha and not beta: assert cls<=2
                else:
                    if q%2==0: target=2 if not tau else 3
                    else:target=2 if not tau and (not alpha or not beta) else 3
                    assert cls==target,(x,y,alpha,beta,tau,cls,target)
        print('RANDOM',q,'15000 span/class cases','pred',pred)
for q in (2,3):run(q)
run(5,False)
print('N4_TWO_GENERATOR_CHECK_OK')
