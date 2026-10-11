#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def connected(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==n

def edmonds_karp(cap, s, t):
    # cap is dict-of-dicts with Fraction capacities
    residual={u:dict(vs) for u,vs in cap.items()}
    for u in list(residual):
        for v in list(residual[u]):
            residual.setdefault(v,{})
            residual[v].setdefault(u,Fraction(0))
    flow=Fraction(0)
    while True:
        parent={s:None}
        q=[s]
        for u in q:
            for v,c in residual.get(u,{}).items():
                if c>0 and v not in parent:
                    parent[v]=u
                    q.append(v)
                    if v==t:
                        break
            if t in parent:
                break
        if t not in parent:
            break
        aug=None
        v=t
        while v!=s:
            u=parent[v]
            c=residual[u][v]
            aug=c if aug is None or c<aug else aug
            v=u
        v=t
        while v!=s:
            u=parent[v]
            residual[u][v]-=aug
            residual[v][u]+=aug
            v=u
        flow+=aug
    return flow

def flow_feasible(ranks, edges):
    n=len(ranks)
    mean=Fraction(sum(ranks),n)
    rr=[Fraction(x)-mean for x in ranks]
    S=sum(x*x for x in rr)
    c=[-x/S for x in rr]
    total=sum(x for x in c if x>0)
    s=n; t=n+1
    cap={i:{} for i in range(n+2)}
    for i,x in enumerate(c):
        if x>0:
            cap[s][i]=x
        elif x<0:
            cap[i][t]=-x
    for u,v in edges:
        cap[u][v]=total
    return edmonds_karp(cap,s,t)==total

def ideal_condition(ranks, edges):
    n=len(ranks)
    mean=Fraction(sum(ranks),n)
    rr=[Fraction(x)-mean for x in ranks]
    for mask in range(1<<n):
        I={i for i in range(n) if (mask>>i)&1}
        # lower ideal: if v is chosen, every immediate predecessor u is chosen
        if all((v not in I or u in I) for u,v in edges):
            if sum(rr[i] for i in I)>0:
                return False
    return True

def sphere_check(ranks, edges):
    n=len(ranks)
    mean=Fraction(sum(ranks),n)
    rr=[Fraction(x)-mean for x in ranks]
    S=sum(x*x for x in rr)
    assert S>0
    c=[-x/S for x in rr]
    R2=Fraction(2)-Fraction(1,S)
    for u,v in edges:
        root=[Fraction(0) for _ in range(n)]
        root[u]=1; root[v]=-1
        d2=sum((root[i]-c[i])**2 for i in range(n))
        assert d2==R2
    return R2

checked=0
for n in range(3,6):
    # Enumerate labeled consecutive rank assignments, fixing vertex 0 at rank 0
    # only to keep runtime small; this still spans all local patterns up to relabeling.
    for h in range(1,n):
        for ranks in product(range(h+1), repeat=n):
            if ranks[0]!=0 or min(ranks)!=0 or max(ranks)!=h:
                continue
            if any(k not in ranks for k in range(h+1)):
                continue
            cand=[(u,v) for u in range(n) for v in range(n)
                  if ranks[v]==ranks[u]+1]
            m=len(cand)
            if m==0 or m>8:
                continue
            for mask in range(1,1<<m):
                edges=[cand[i] for i in range(m) if (mask>>i)&1]
                if not connected(n,edges):
                    continue
                sphere_check(ranks,edges)
                assert ideal_condition(ranks,edges)==flow_feasible(ranks,edges)
                checked+=1

# Explicit failure example: ranks (0,0,1,1,2).
ranks=(0,0,1,1,2)
edges=[(0,2),(0,3),(1,3),(2,4)]
assert connected(5,edges)
assert not ideal_condition(ranks,edges)
assert not flow_feasible(ranks,edges)
R2=sphere_check(ranks,edges)
assert R2==Fraction(23,14)

print(f"VERIFY_OK graded-directed-edge-spheres quivers={checked} failure_example_R2={R2}")
