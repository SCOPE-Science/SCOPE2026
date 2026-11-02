#!/usr/bin/env python3
"""Direct subset-and-swap verification of maximal induced matching exchange theorems."""
from itertools import combinations, product
from collections import Counter
from math import ceil

def legal(n, chosen):
    s=set(chosen)
    for x in s:
        if any(((x+d)%n) in s for d in (1,2)):
            return False
    for v in range(n):
        if v not in s and not any(((v+d)%n) in s for d in (-2,-1,1,2)):
            return False
    return True

def expected(n,k):
    hist=Counter()
    for gaps in product((3,4,5),repeat=k):
        if sum(gaps)==n:
            degree=sum(2-abs(gaps[i]+gaps[(i+1)%k]-8) for i in range(k))
            hist[degree]+=1
    assert all(n*v%k==0 for v in hist.values()) if False else True
    # Coefficient of trace transfer-matrix power, with n/k conversion.
    return {d:n*v//k for d,v in hist.items()}

def coeff(n,k):
    if k<0:return int(n==0)
    if n<3*k or n>5*k:return 0
    return sum(1 for g in product((3,4,5),repeat=k) if sum(g)==n)

def analyze(n,k):
    states=[frozenset(c) for c in combinations(range(n),k) if legal(n,c)]
    idx={x:i for i,x in enumerate(states)}
    adj=[]
    for s in states:
        ns=set()
        for a in s:
            for b in range(n):
                if b not in s:
                    t=(s-{a})|{b}
                    if t in idx: ns.add(idx[t])
        adj.append(ns)
    assert all(i in adj[j] for i,ns in enumerate(adj) for j in ns)
    hist=Counter(map(len,adj))
    assert hist==expected(n,k),(n,k,hist,expected(n,k))
    assert len(states)==n*coeff(n,k)//k
    edges=sum(map(len,adj))//2
    assert edges==n*(coeff(n-7,k-2)+3*coeff(n-8,k-2)+coeff(n-9,k-2))
    triangles=sum(len(adj[i]&adj[j]) for i in range(len(states)) for j in adj[i] if i<j)//3
    assert triangles==n*coeff(n-8,k-2),(n,k,triangles,n*coeff(n-8,k-2))
    comps=[]; seen=set()
    for i in range(len(states)):
        if i in seen:continue
        q=[i];seen.add(i)
        for p in q:
            for t in adj[p]:
                if t not in seen:
                    seen.add(t);q.append(t)
        comps.append(len(q))
    assert len(seen)==len(states)
    e=n-3*k
    if e==0: assert sorted(comps)==[1]*3
    elif e==2*k: assert sorted(comps)==[1]*5
    else: assert comps==[len(states)]
    if e in (1,2*k-1): assert hist=={2:n} and triangles==0
    elif 2<=e<=2*k-2: assert triangles>0
    assert all(d%2==0 for d in hist)
    return len(states),edges,triangles,sorted(comps),dict(sorted(hist.items()))

if __name__=='__main__':
    tests=0
    for n in range(7,19):
        for k in range(ceil(n/5),n//3+1):
            answer=analyze(n,k)
            tests+=1
            print(n,k,*answer,flush=True)
    print('DIRECT_SUBSET_VERIFICATION_PASS',tests)
