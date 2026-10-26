#!/usr/bin/env python3
"""Finite exhaustive and constructive checks for minimum faithful module dimensions.
No external packages needed. Run: python3 verify.py
"""
import itertools
import random

def max_matching(edges):
    # Edges are pairs (tail, head); left and right copies are distinct.
    tails=sorted({u for u,v in edges})
    adj={u:sorted({v for a,v in edges if a==u}) for u in tails}
    best=0
    def search(i,used,k):
        nonlocal best
        if i==len(tails):
            best=max(best,k)
            return
        u=tails[i]
        search(i+1,used,k)
        for v in adj[u]:
            if v not in used:
                search(i+1,used|{v},k+1)
    search(0,set(),0)
    return best

def matching_formula(m):
    n=len(m)
    incoming=[any(m[u][v]>0 for u in range(n)) for v in range(n)]
    outgoing=[any(m[v][w]>0 for w in range(n)) for v in range(n)]
    b=sum(i and o for i,o in zip(incoming,outgoing))
    double=[(u,v) for u in range(n) for v in range(n) if m[u][v]==2]
    return n+b+max_matching(double)

def brute_integer(m):
    n=len(m)
    inc=[any(m[u][v] for u in range(n)) for v in range(n)]
    out=[any(m[v][w] for w in range(n)) for v in range(n)]
    baseline=n+sum(inc[v] and out[v] for v in range(n))
    # An optimal representation needs at most 3n dimensions for mult <= 2.
    bounds=[range(1,4) if inc[v] else (0,) for v in range(n)]
    tbounds=[range(1,4) if out[v] else (0,) for v in range(n)]
    best=None; arg=None
    for s in itertools.product(*bounds):
        for t in itertools.product(*tbounds):
            if not all(t[u]*s[v]>=m[u][v] for u in range(n) for v in range(n)):continue
            dimension=sum(max(1,s[v]+t[v]) for v in range(n))
            if best is None or dimension<best: best, arg=dimension,(s,t)
    if best is None:raise Exception('No feasible module')
    assert best>=baseline
    return best,arg

def construct(m,s,t):
    # Returns explicit action matrices on sum_v (S_v + T_v) and their linear independence.
    n=len(m)
    ss=[];ts=[];at=0
    for v in range(n):
        if s[v]+t[v]==0: ss.append([]);ts.append([at]);at+=1
        else:
            ss.append(list(range(at,at+s[v])));at+=s[v]
            ts.append(list(range(at,at+t[v])));at+=t[v]
    N=at
    ids=[];arrows=[]
    for v in range(n):
        D={(i,i):1 for i in ss[v]+ts[v]}
        ids.append(D)
    for u in range(n):
        for v in range(n):
            for i in range(m[u][v]):
                # Arrow basis maps T_u -> S_v
                arrows.append({(ss[v][i//len(ts[u])],ts[u][i%len(ts[u])]):1})
    acts=ids+arrows
    # independent matrices over every field: pairwise disjoint supports in selected coordinates.
    seen={}
    for j,D in enumerate(acts):
        for entry in D:
            if entry in seen and j!=seen[entry]:raise AssertionError('Overlapping coordinate')
            seen[entry]=j
    # products of arrows are literally zero as all target indices lie in S and source in T.
    sset={x for group in ss for x in group}
    tset={x for group in ts for x in group}
    assert not sset.intersection(tset)
    assert all(r in sset and c in tset for D in arrows for r,c in D)
    return N,len(acts)

def run():
    cases=[]
    for entries in itertools.product(range(3),repeat=4):
        cases.append([list(entries[:2]),list(entries[2:])])
    rng=random.Random(129337)
    for n,k in [(3,120),(4,60)]:
        for _ in range(k):
            cases.append([[rng.randrange(3) for _ in range(n)] for __ in range(n)])
    for m in cases:
        exact,(s,t)=brute_integer(m)
        formula=matching_formula(m)
        assert exact==formula,(m,exact,formula)
        dim,num=construct(m,s,t)
        assert dim==exact
        assert num==len(m)+sum(sum(row) for row in m)
    # Test full optimization for multiplicities above two with two-vertex quivers.
    extra=0
    for entries in itertools.product(range(5),repeat=4):
        m=[list(entries[:2]),list(entries[2:])]
        best,(s,t)=brute_integer(m) if max(entries)<=2 else brute_generic(m)
        dim,num=construct(m,s,t)
        assert dim==best and num==2+sum(entries)
        extra+=1
    print('VERIFY_OK_FAITHFUL_MATCHING',len(cases),'max2_quivers',extra,'max4_quivers')

def brute_generic(m):
    n=len(m)
    inc=[any(m[u][v] for u in range(n)) for v in range(n)]
    out=[any(m[v][w] for w in range(n)) for v in range(n)]
    bd=max(1,max(x for row in m for x in row))
    sb=[range(1,bd+1) if inc[v] else (0,) for v in range(n)]
    tb=[range(1,bd+1) if out[v] else (0,) for v in range(n)]
    best=None; arg=None
    for s in itertools.product(*sb):
        for t in itertools.product(*tb):
            if all(t[u]*s[v]>=m[u][v] for u in range(n) for v in range(n)):
                d=sum(max(1,s[v]+t[v]) for v in range(n))
                if best is None or d<best:best,arg=d,(s,t)
    assert arg is not None
    return best,arg

if __name__=='__main__': run()
