#!/usr/bin/env python3
"""Direct finite checks of a three-voter, two-option temporal-core theorem."""
from itertools import combinations_with_replacement, product
from random import Random

A,B,AB=1,2,3
ALL_MASKS=[(A,A,A),(A,B,B),(B,A,B),(B,B,A),(AB,A,B),(A,AB,B),(A,B,AB)]

def construct(profile):
    l=len(profile)
    refined=[tuple(A if s==AB else s for s in rnd) for rnd in profile]
    lone=[[] for _ in range(3)]
    ans=[None]*l
    for j,rnd in enumerate(refined):
        if len(set(rnd))==1:
            ans[j]=0 if rnd[0]==A else 1
        else:
            i=next(i for i in range(3) if rnd.count(rnd[i])==1)
            lone[i].append(j)
            ans[j]=1 if rnd[i]==A else 0
    idx=sorted(range(3),key=lambda i:(-len(lone[i]),i))
    c1,c2,c3=(len(lone[i]) for i in idx)
    d=c1+c2+c3
    a=d//3;b=2*d//3;h=d-b
    t=max(0,c1-(d-a)) if c2<=h else c1-h
    assert 0<=t<=c1
    for j in lone[idx[0]][:t]:ans[j]^=1
    base=tuple(sum(bool(r[i]&(1<<ans[j])) for j,r in enumerate(profile)) for i in range(3))
    assert min(base)>=l//3
    assert sum(q>=2*l//3 for q in base)>=2
    return tuple(ans),base

def pareto_completion(profile,base):
    dp={(0,0,0):0}
    for j,r in enumerate(profile):
        ndp={}
        for v,mask in dp.items():
            for choice in (0,1):
                vv=tuple(v[i]+bool(r[i]&(1<<choice)) for i in range(3))
                ndp[vv]=mask|(choice<<j)
        dp=ndp
    cand=[(v,mask) for v,mask in dp.items() if all(v[i]>=base[i] for i in range(3))]
    assert cand
    v,mask=max(cand,key=lambda vm:(sum(vm[0]),vm[0]))
    assert not any(all(w[i]>=v[i] for i in range(3)) and w!=v for w in dp)
    return v,tuple(mask>>j&1 for j in range(len(profile)))

def check_strong_core(profile,vector):
    l=len(profile)
    for S_mask in range(1,8):
        S=[i for i in range(3) if S_mask>>i&1]
        k=l*len(S)//3
        for dev in product((-1,0,1),repeat=l):
            if sum(z!=-1 for z in dev)!=k:continue
            if all(sum(bool(profile[j][i]&(1<<z)) for j,z in enumerate(dev) if z!=-1)>vector[i] for i in S):
                return False,(S,dev)
    return True,None

def run():
    tests=0
    for l in range(1,7):
        for idx in combinations_with_replacement(range(len(ALL_MASKS)),l):
            prof=tuple(ALL_MASKS[z] for z in idx)
            _,base=construct(prof)
            v,_=pareto_completion(prof,base)
            ok,wit=check_strong_core(prof,v)
            if not ok:raise AssertionError(('canonical',l,idx,v,wit))
            tests+=1
        print('canonical horizon',l,'checked',tests,flush=True)
    full_types=list(product((A,B,AB),repeat=3))
    exhaustive=0
    for l in range(1,5):
        for idx in combinations_with_replacement(range(len(full_types)),l):
            prof=tuple(full_types[z] for z in idx)
            _,base=construct(prof)
            v,_=pareto_completion(prof,base)
            ok,wit=check_strong_core(prof,v)
            if not ok:raise AssertionError(('full',l,idx,v,wit))
            exhaustive+=1
        print('full-ballot unordered profiles through horizon',l,'checked',exhaustive,flush=True)
    rng=Random(72517)
    random_checks=0
    for l in (3,4,5,6,7):
        for _ in range(180):
            prof=tuple(tuple(rng.choice((A,B,AB)) for _ in range(3)) for __ in range(l))
            _,base=construct(prof)
            v,_=pareto_completion(prof,base)
            ok,wit=check_strong_core(prof,v)
            if not ok:raise AssertionError(('random',l,prof,v,wit))
            random_checks+=1
    print('PASS structured classes',tests,'exhaustive full-ballot unordered profiles',exhaustive,'random full-ballot profiles',random_checks)
if __name__=='__main__':run()
