#!/usr/bin/env python3
"""Standalone checks for exact scattered-pair count languages (no external dependencies)."""
from collections import deque, defaultdict
from itertools import product

def count01(w):
    z=t=0
    for c in w:
        if c=='0': z+=1
        elif c=='1': t+=z
        else: raise ValueError('binary input only')
    return t

def raw(k):
    lim=k+1
    nexts=lambda q,r: ((min(lim,q+1),r),(q,min(lim,r+q)))
    states=[(0,0)]
    ids={(0,0):0}
    d=[]
    for s in states:
        xs=[]
        for y in nexts(*s):
            if y not in ids:
                ids[y]=len(states); states.append(y)
            xs.append(ids[y])
        d.append(tuple(xs))
    return states,d

def minimization(states,trans,k):
    classes=[int(r==k) for q,r in states]
    steps=0
    while True:
        d={};nxt=[]
        for i,(q,r) in enumerate(states):
            key=(r==k, classes[trans[i][0]],classes[trans[i][1]])
            if key not in d:d[key]=len(d)
            nxt.append(d[key])
        steps+=1
        if len(d)==len(set(classes)): return len(d),steps,nxt
        classes=nxt

def canonical(k,q,r):
    if r>k or (r<k and q>k-r):return ('dead',)
    if q==0:return ('start',)
    if r==k:return ('accept_zeros',)
    t=k-r
    if 2*q>t:return ('single_one',t-q)
    return ('double_plus',q,t)

def reachable_model(k):
    return [('start',),('dead',),('accept_zeros',)]+[('single_one',d) for d in range((k-1)//2+1)]+[('double_plus',q,t) for t in range(1,k+1) for q in range(1,t//2+1)]

if __name__=='__main__':
    allstates=0; totals=0; small=0
    for k in range(1,61):
        states,trans=raw(k)
        n,steps,cls=minimization(states,trans,k)
        want=(k*k)//4+(k+1)//2+3
        assert n==want,(k,n,want)
        d=defaultdict(set)
        for s,c in zip(states,cls):d[c].add(canonical(k,*s))
        assert all(len(ss)==1 for ss in d.values()), (k,[(a,b) for a,b in d.items() if len(b)>1][:5])
        assert len({canonical(k,*s) for s in states})==want
        assert len(set(reachable_model(k)))==want
        allstates+=len(states)
        if k<=6:
            for nword in range(12):
                for word in map(''.join,product('01',repeat=nword)):
                    q=word.count('0');r=count01(word)
                    state=states[0];u=0
                    for c in word:
                        u=trans[u][int(c)]
                    assert state==states[0] and states[u]==(min(k+1,q),min(k+1,r))
                    small+=1
        totals+=n
    print(f'VERIFY_OK independent_minimizations=60 raw_reachable_states={allstates} total_minimized_states={totals} direct_binary_words={small} exact_class_correspondence=true')
