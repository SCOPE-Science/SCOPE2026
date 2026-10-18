#!/usr/bin/env python3
"""Check exact one-hole fixed-block factor avoidance against an independent automaton BFS."""
from collections import deque, Counter
from itertools import product
from math import gcd

def formula(v):
    k=len(v)
    periods=[s for s in range(1,k) if v[:-s]==v[s:]]
    g=k; cost=0
    for p in periods:
        h=gcd(g,p)
        cost += (g-h)*p
        g=h
    return k+cost+(g-1)*(k+1), periods

def bfs_kmp(v):
    """BFS over actual letters, remembering KMP state, clock residue and all occupied occurrence residues."""
    k=len(v)
    alphabet=sorted(set(v))
    if len(alphabet)==1: alphabet=alphabet+['1' if alphabet[0]=='0' else '0']
    # Alphabet choices exactly binary for the tests, not synthesized from periods.
    alphabet=['0','1']
    start=(0,0,0) # matched proper prefix, number of read chars modulo k, residue mask
    Q=deque([start]); visited={start}; parent={start:None}; label={}
    while Q:
        st=Q.popleft(); s,clock,mask=st
        for a in alphabet:
            z=v[:s]+a
            while z and not v.startswith(z): z=z[1:]
            found=len(z)==k
            if found:
                residue=(clock+1-k)%k  # position where occurrence starts
                nm=mask|(1<<residue)
                z=z[1:]
                while z and not v.startswith(z): z=z[1:]
            else:nm=mask
            ns=(len(z),(clock+1)%k,nm)
            if ns in visited:continue
            parent[ns]=st; label[ns]=a
            if nm==(1<<k)-1:
                out=[];cur=ns
                while parent[cur] is not None:
                    out.append(label[cur]);cur=parent[cur]
                return ''.join(reversed(out)),len(visited)
            visited.add(ns);Q.append(ns)
    raise RuntimeError('unreachable')

def direct_nfa_absence(v):
    """All-path NFA factor test built from fixed-length codewords, independent of KMP alignment criterion."""
    k=len(v)
    code={''.join(w) for w in product('01',repeat=k)}-{v}
    prefixes={''}
    for w in code:prefixes.update(w[:j] for j in range(1,k))
    states=sorted(prefixes)
    ix={p:i for i,p in enumerate(states)}
    trans=[[] for _ in states]
    for p in states:
        for a in '01':
            mask=0
            pa=p+a
            if pa in prefixes:mask|=1<<ix[pa]
            if pa in code:mask|=1<<ix['']
            trans[ix[p]].append(mask)
    full=(1<<len(states))-1
    q=deque([(full,0)]); seen={full}
    while q:
        subset,d=q.popleft()
        for a in range(2):
            ns=0
            for j in range(len(states)):
                if subset>>j&1:ns|=trans[j][a]
            if ns==0:return d+1,len(seen)
            if ns not in seen:
                seen.add(ns);q.append((ns,d+1))
    raise RuntimeError('NFA complete when it must be incomplete')

def run():
    total_kmp=total_nfa=0
    summary=[]
    for k in range(2,9):
        hist=Counter(); checked=0
        for tup in product('01',repeat=k):
            v=''.join(tup)
            f,ps=formula(v)
            w,states=bfs_kmp(v)
            assert len(w)==f,(v,f,len(w))
            assert {i%k for i in range(len(w)-k+1) if w[i:i+k]==v}==set(range(k))
            total_kmp+=1
            if k<=6:
                nd,ns=direct_nfa_absence(v)
                assert nd==f,(v,nd,f)
                total_nfa+=1
            checked+=1;hist[f]+=1
        summary.append((k,checked,sorted(hist.items())))
    witness='010010'
    w,states=bfs_kmp(witness)
    assert len(w)==25
    print('MATCH: period-GCD formula versus letter-by-letter KMP BFS:',total_kmp,'binary holes, lengths 2..8')
    print('MATCH: independent prefix-flower NFA factor BFS:',total_nfa,'binary holes, lengths 2..6')
    print('DISTANCE DISTRIBUTIONS (k, holes, {shortest absent length:count})')
    for k,c,dist in summary:print(k,c,dict(dist))
    print('EXAMPLE v=010010: periods',formula(witness)[1], 'shortest absent length',len(w),'word',w)
    print('EXAMPLE occurrence starts',[i for i in range(len(w)-len(witness)+1) if w[i:i+len(witness)]==witness])
    print('PASS')
if __name__=='__main__':run()
