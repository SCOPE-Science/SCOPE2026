#!/usr/bin/env python3
"""Finite checks of public-announcement stabilization bounds in S5."""
from __future__ import annotations
import random

# Formulas: (var,index), (not,phi), (and,phi,psi), (or,phi,psi),
# (dia,agent,phi), (true,), (false,).
def neg(a): return ('not',a)
def conj(a,b): return ('and',a,b)
def disj(a,b): return ('or',a,b)
def dia(i,a): return ('dia',i,a)

def eval_at(phi,w,S,classes,values):
    tag=phi[0]
    if tag=='var': return values[w][phi[1]]
    if tag=='true': return True
    if tag=='false': return False
    if tag=='not': return not eval_at(phi[1],w,S,classes,values)
    if tag=='and': return eval_at(phi[1],w,S,classes,values) and eval_at(phi[2],w,S,classes,values)
    if tag=='or': return eval_at(phi[1],w,S,classes,values) or eval_at(phi[2],w,S,classes,values)
    if tag=='dia':
        cls=classes[phi[1]][w]
        return any(eval_at(phi[2],v,S,classes,values) for v in S if classes[phi[1]][v]==cls)
    raise ValueError(tag)

def iterate(phi,n,classes,values):
    S=set(range(n)); history=[frozenset(S)]
    while True:
        T={w for w in S if eval_at(phi,w,S,classes,values)}
        if T==S: break
        S=T
        history.append(frozenset(S))
        if len(history)>n+1: raise AssertionError('Too many updates')
    return history

def theta(value,k):
    result=('true',)
    for i in range(k):
        q=('var',i)
        result=conj(result,q if value & (1<<i) else neg(q))
    return result

def sharp_formula(k):
    # The current valuation type has some larger type still present in its S5 class.
    result=('false',)
    types=[theta(t,k) for t in range(1<<k)]
    for s in range(1<<k):
        for t in range(s+1,1<<k):
            result=disj(result,conj(types[s],dia(0,types[t])))
    return result

def pair_classes(n,agent):
    # a-class pairs (0,1),(2,3),...; b-class pairs (1,2),(3,4),...
    if agent==0: return [i//2 for i in range(n)]
    return [(-1 if i==0 else (i-1)//2) for i in range(n)]

def random_formula(rng,k,depth):
    if depth==0 or rng.randrange(5)==0: return ('var',rng.randrange(k))
    c=rng.randrange(4)
    if c==0:return neg(random_formula(rng,k,depth-1))
    if c==1:return conj(random_formula(rng,k,depth-1),random_formula(rng,k,depth-1))
    if c==2:return disj(random_formula(rng,k,depth-1),random_formula(rng,k,depth-1))
    return dia(0,random_formula(rng,k,depth-1))

def run():
    checks=0
    for k in range(0,6):
        n=1<<k
        phi=sharp_formula(k)
        values=[tuple(bool(w & (1<<i)) for i in range(k)) for w in range(n)]
        classes=[[0]*n]
        hist=iterate(phi,n,classes,values)
        assert len(hist)-1==n,(k,len(hist))
        assert [len(s) for s in hist]==list(range(n,-1,-1))
        checks+=1
    # Test the fixed depth-one, one-letter, two-agent formula on long paths.
    p=('var',0)
    phi=disj(conj(p,dia(0,neg(p))),conj(neg(p),dia(1,p)))
    for n in range(1,161):
        vals=[(i%2==0,) for i in range(n)]
        classes=[pair_classes(n,0),pair_classes(n,1)]
        hist=iterate(phi,n,classes,vals)
        assert hist==[frozenset(range(n-i)) for i in range(n+1)]
        checks+=1
    rng=random.Random(260924006)
    for k in range(1,4):
        for _ in range(950):
            n=rng.randrange(1,32)
            groups=rng.randrange(1,9)
            classes=[[rng.randrange(groups) for _ in range(n)]]
            values=[tuple(bool(rng.randrange(2)) for _ in range(k)) for _ in range(n)]
            formula=random_formula(rng,k,4)
            hist=iterate(formula,n,classes,values)
            assert len(hist)-1<=1<<k,(k,len(hist))
            checks+=1
    print('VERIFY_OK',checks,'models','sharp one-agent k=0..5','two-agent paths 1..160','one-agent random instances 2850')

if __name__=='__main__': run()
