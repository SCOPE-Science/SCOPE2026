#!/usr/bin/env python3
"""Independent structural event classification for 3-color CCA on K_n minus a matching.
Verifies the defect-event decomposition against microscopic dynamics.
"""
from itertools import product
from math import comb

def edge_partner(v, k):
    return (v ^ 1) if v < 2*k else -1

def case_by_structure(state, k):
    n=len(state)
    support=set(state)
    if len(support)==1:
        return (0,1)
    if len(support)==2:
        pred=next(c for c in support if (c+1)%3 in support)
        succ=(pred+1)%3
        w=[v for v in range(n) if state[v]==succ]
        if len(w)==1 and edge_partner(w[0],k)>=0 and state[edge_partner(w[0],k)]==pred:
            return (2,1)
        return (1,1)
    blockers=[]
    for j in range(3):
        singleton=[v for v in range(n) if state[v]==j]
        if len(singleton)==1:
            w=singleton[0]
            v=edge_partner(w,k)
            if v>=0 and state[v]==(j-1)%3:
                blockers.append((v,w))
    assert len(blockers)<=1
    if not blockers: return (0,3)
    v,w=blockers[0]
    i=state[v]
    others=[u for u in range(n) if u!=v and state[u]==i]
    if not others:return (2,1)
    if len(others)==1:
        u=others[0];z=edge_partner(u,k)
        if z>=0 and state[z]==(i+2)%3:return (2,3)
    return (1,3)

def independent_update(state,k):
    n=len(state)
    nn=[set(range(n))-{v,edge_partner(v,k)} for v in range(n)]
    return tuple((s+1)%3 if (s+1)%3 in {state[w] for w in nn[v]} else s for v,s in enumerate(state))

def predicted(n,k):
    return {(0,1):3,
            (0,3):3**n-3*2**n+3-6*k*(2**(n-2)-1),
            (1,1):3*2**n-6-6*k,
            (1,3):6*k*(2**(n-2)-2*k),
            (2,1):12*k,
            (2,3):12*k*(k-1)}

def run():
    cases=0;states=0
    for n in range(3,11):
        for k in range(n//2+1):
            if n-k<3:continue
            actual={key:0 for key in predicted(n,k)}
            for a in product(range(3),repeat=n):
                kind=case_by_structure(a,k)
                seq=[a]
                for _ in range(5):seq.append(independent_update(seq[-1],k))
                assert seq[5]==seq[2],(n,k,a,seq)
                d=next(t for t in (0,1,2) if seq[t+3]==seq[t])
                p=1 if seq[d]==seq[d+1] else 3
                assert (d,p)==kind,(n,k,a,(d,p),kind)
                actual[kind]+=1;states+=1
            assert actual==predicted(n,k),(n,k,actual,predicted(n,k))
            cases+=1
            print(f'n={n} k={k} counts={actual}')
    print(f'STRUCTURAL_CLASSIFICATION_OK cases={cases} states={states}')
if __name__=='__main__':run()
