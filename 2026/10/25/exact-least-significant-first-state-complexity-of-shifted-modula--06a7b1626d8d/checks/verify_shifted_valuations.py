#!/usr/bin/env python3
"""Independent finite-state checks for residue-valuations of translated words.
All data here are mathematical input/output, without external dependencies.
"""
from collections import deque

def vq(z,q):
    assert z>0 and q>=2
    a=0
    while z%q==0:
        z//=q;a+=1
    return a

def formula(q,m,c):
    x=c+1;ell=0
    while q**ell<x:ell+=1
    return ell+2*m

def automaton(q,m,c):
    root=('v',c+1,0); que=deque([root]);seen={root};delta={};outputs={}
    while que:
        state=que.popleft()
        typ=state[0]
        if typ=='c':
            outputs[state]=state[1];dest=[state for _ in range(q)]
        else:
            _,s,p=state
            outputs[state]=(p+vq(s,q))%m
            dest=[('v',(s+d)//q,(p+1)%m) if (s+d)%q==0 else ('c',p) for d in range(q)]
        delta[state]=dest
        for target in dest:
            if target not in seen:
                seen.add(target);que.append(target)
    return root,seen,delta,outputs

def min_classes(seen,delta,outputs,q):
    states=list(seen);cl={s:outputs[s] for s in states}
    while True:
        signatures={s:(outputs[s],tuple(cl[delta[s][d]] for d in range(q))) for s in states}
        vals={sig:i for i,sig in enumerate(sorted(set(signatures.values())))}
        new={s:vals[signatures[s]] for s in states}
        if len(set(new.values()))==len(set(cl.values())) and all((cl[a]==cl[b]) == (new[a]==new[b]) for a in states for b in states):
            return len(set(new.values()))
        cl=new

def verify():
    total=0
    for q in range(2,7):
        for m in range(2,6):
            for c in list(range(0,151))+[255,256,257,999,1000,1001,4095,4096,4097]:
                root,seen,delta,outputs=automaton(q,m,c)
                expected=formula(q,m,c)
                assert len(seen)==expected,(q,m,c,len(seen),expected)
                assert min_classes(seen,delta,outputs,q)==expected,(q,m,c)
                # check direct outputs on all short inputs including noncanonical ones
                for n in range(0,64):
                    bits=[];v=n
                    while v:bits.append(v%q);v//=q
                    s=root
                    for d in bits:s=delta[s][d]
                    assert outputs[s]==vq(n+c+1,q)%m,(q,m,c,n)
                total+=1
    print('PASS modular-valuation automata',total,'parameter triples')
    print('PASS structural reachability and independent DFA minimization')
    print('PASS direct numerical outputs for',64*total,'nonnegative arguments')
if __name__=='__main__':verify()
