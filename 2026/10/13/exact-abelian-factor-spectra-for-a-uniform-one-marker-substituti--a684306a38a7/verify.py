#!/usr/bin/env python3
"""Standalone finite regression checks for exact one-marker abelian spectra."""
import json
from pathlib import Path

C=json.loads(Path('certificate.json').read_text(encoding='utf-8'))

def morph(b,initial_length=100000):
    word='0'
    z='0'*(b-1)+'1'
    o='1'+'0'*(b-1)
    while len(word)<initial_length:
        word=''.join(z if x=='0' else o for x in word)
    return [int(x) for x in word]

def recurrence(b,n):
    vals=[0]*n
    for j in range(1,n):
        q,r=divmod(j,b)
        if r==0: vals[j]=vals[q]
        elif r==b-1: vals[j]=1-vals[q]
        else: vals[j]=0
    return vals

def theoretical(b,n):
    assert b>=2 and n>=1
    q,r=divmod(n,b)
    if b==2:
        return list(range(q-1,q+2)) if r==0 else [q,q+1]
    if q==0:
        return [0,1] if n==1 else [0,1,2]
    if r==0 or r==1:
        return [q-1,q,q+1]
    if r==b-1:
        return [q,q+1,q+2]
    return [q-1,q,q+1,q+2]

symbolic_cases=0
for b in range(2,18):
    w=morph(b,120000)
    rec=recurrence(b,len(w))
    assert w==rec, ('index_recurrence',b)
    P=[0]
    for x in w:P.append(P[-1]+x)
    for p in range(1,1000):
        for s in range(b):
            assert P[b*p+s]==p+(s>0)*w[p], (b,p,s)
    for q in range(0,8):
        for r in range(b):
            n=b*q+r
            if n==0:continue
            seen=set(P[i+n]-P[i] for i in range(0,18000))
            expected=theoretical(b,n)
            assert sorted(seen)==expected,(b,n,sorted(seen),expected)
            for s in range(b):
                t,u=divmod(s+r,b)
                # Direct boundary equation for each starting block.
                for p in (0,1,2,3,4,5,6,25,77,1000):
                    count=P[b*p+s+n]-P[b*p+s]
                    form=q+t+(u>0)*w[p+q+t]-(s>0)*w[p]
                    assert count==form,(b,n,p,s,count,form)
                    symbolic_cases+=1
    for h in range(1,129):
        signs={(w[p],w[p+h]) for p in range(0,6000)}
        assert (0,1) in signs and (1,0) in signs,(b,h)

assert C['parameter_range_tested']==[2,17]
print('VERIFY_OK b=2..17 index_recurrence prefix_weights exact_factor_spectra '
      'n<=7b+b-1 all_lags_h<=128 symbolic_boundary_cases='+str(symbolic_cases))
