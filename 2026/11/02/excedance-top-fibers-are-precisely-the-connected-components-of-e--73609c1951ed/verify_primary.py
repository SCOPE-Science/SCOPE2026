#!/usr/bin/env python3
"""Independent direct enumeration of fixed-excedance adjacent-swap graphs."""
import itertools
import collections
import math

def exc(p): return sum(v>i+1 for i,v in enumerate(p))
def tops(p): return frozenset(v for i,v in enumerate(p) if v>i+1)
def canon(t,n): return tuple(sorted(t)+sorted(set(range(1,n+1))-set(t)))
def legal(p,i): return p[i]!=i+2 and p[i+1]!=i+2

def verify(n):
    ps=list(itertools.permutations(range(1,n+1)))
    idx={p:j for j,p in enumerate(ps)}
    adj=[[] for _ in ps]
    byk=collections.Counter(map(exc,ps)); edgecount=collections.Counter(); iso=collections.Counter()
    for j,p in enumerate(ps):
        for i in range(n-1):
            q=list(p);q[i],q[i+1]=q[i+1],q[i];q=tuple(q)
            stays=exc(p)==exc(q)
            assert stays==legal(p,i),(n,p,i)
            if stays:
                assert tops(p)==tops(q)
                adj[j].append(idx[q])
        if not adj[j]: iso[exc(p)]+=1
        edgecount[exc(p)]+=len(adj[j])
    seen=set(); components=collections.Counter(); sigs=collections.defaultdict(list)
    for j,p in enumerate(ps):
        if j in seen: continue
        todo=[j];seen.add(j);ts=tops(p);k=exc(p)
        while todo:
            a=todo.pop()
            assert tops(ps[a])==ts
            for b in adj[a]:
                if b not in seen: seen.add(b);todo.append(b)
        components[k]+=1;sigs[k].append(ts)
    for k in range(n):
        assert components[k]==math.comb(n-1,k)
        assert iso[k]==1
        assert len(set(sigs[k]))==components[k]
        expected=(n-1)*(byk[k]-byk[k-1]-byk[k] if False else byk[k])/2
        if n>2:
            # Eulerian row of n-1 computed independently.
            prev=collections.Counter(exc(q) for q in itertools.permutations(range(1,n)))
            expected=(n-1)*(byk[k]-prev[k]-prev[k-1])//2
            assert edgecount[k]//2==expected,(n,k,edgecount[k]//2,expected)
    for t in itertools.chain.from_iterable(itertools.combinations(range(2,n+1),k) for k in range(n)):
        c=canon(t,n);assert tops(c)==set(t)
    print('DIRECT_PASS',n,len(ps),sum(components.values()),sum(edgecount.values())//2)

if __name__=='__main__':
    for n in range(2,9):verify(n)

def check_nongeodesic_witness():
    n=5;start=(1,4,3,5,2);goal=(4,2,3,5,1)
    assert tops(start)==tops(goal)=={4,5}
    todo=collections.deque([(start,0)]);seen={start};distance=None
    while todo:
        p,d=todo.popleft()
        if p==goal:distance=d;break
        for i in range(n-1):
            if not legal(p,i):continue
            q=list(p);q[i],q[i+1]=q[i+1],q[i];q=tuple(q)
            if q not in seen:seen.add(q);todo.append((q,d+1))
    inv={v:i for i,v in enumerate(goal)}
    mapped=[inv[v] for v in start]
    unconstrained=sum(mapped[i]>mapped[j] for i in range(n) for j in range(i+1,n))
    assert(distance,unconstrained)==(8,6)
    print('NONGEODESIC_PASS',distance,unconstrained)
check_nongeodesic_witness()
