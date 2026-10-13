#!/usr/bin/env python3
from collections import defaultdict

def formula(a,b):
    if a>b:
        a,b=b,a
    if a==b:
        return a
    if b==a+1:
        return b
    return max(2*a+3, (a+b+2)//2)

def weighted_quotient(a,b,d):
    nodes=[("A",j) for j in range(a+1)]+[("B",j) for j in range(b+1)]
    nbr={}
    for side,h,other in [("A",a,"B"),("B",b,"A")]:
        for j in range(h+1):
            z=[]
            if j==0: z.append((other,0))
            else: z.append((side,j-1))
            if j<h: z += [(side,j+1)]*d
            nbr[(side,j)]=z
    return nodes,nbr

def partition(colors):
    cells=defaultdict(set)
    for v,c in colors.items(): cells[c].add(v)
    return frozenset(frozenset(x) for x in cells.values())

def quotient_depth(a,b,d):
    nodes,nbr=weighted_quotient(a,b,d)
    colors={v:0 for v in nodes}; old=partition(colors)
    for r in range(a+b+10):
        sig={v:(colors[v],tuple(sorted(colors[w] for w in nbr[v]))) for v in nodes}
        names={}; new={v:names.setdefault(sig[v],len(names)) for v in nodes}
        newpart=partition(new)
        if newpart==old: return r,old
        colors,old=new,newpart
    raise RuntimeError

def full_graph(a,b,d):
    adj={0:{1},1:{0}}; meta={0:("A",0),1:("B",0)}
    next_id=2
    for root,side,h in [(0,"A",a),(1,"B",b)]:
        level=[root]
        for depth in range(1,h+1):
            nxt=[]
            for u in level:
                for _ in range(d):
                    v=next_id; next_id+=1
                    adj[v]=set(); adj[u].add(v); adj[v].add(u)
                    meta[v]=(side,depth); nxt.append(v)
            level=nxt
    return adj,meta

def full_cr(a,b,d):
    adj,meta=full_graph(a,b,d)
    colors={v:0 for v in adj}; old=partition(colors)
    for r in range(len(adj)+2):
        sig={v:(colors[v],tuple(sorted(colors[w] for w in adj[v]))) for v in adj}
        names={}; new={v:names.setdefault(sig[v],len(names)) for v in adj}
        newpart=partition(new)
        if newpart==old: return r,old,meta
        colors,old=new,newpart
    raise RuntimeError

def predicted_orbits(a,b,meta):
    cells=defaultdict(set)
    if a==b:
        for v,(s,j) in meta.items(): cells[("eq",j)].add(v)
    elif abs(a-b)==1:
        tall="A" if a>b else "B"
        for v,(s,j) in meta.items():
            cells[("center_dist", j if s==tall else j+1)].add(v)
    else:
        for v,(s,j) in meta.items(): cells[(s,j)].add(v)
    return frozenset(frozenset(x) for x in cells.values())

quotient_checks=0
for d in range(2,6):
    for a in range(1,26):
        for b in range(1,26):
            depth,_=quotient_depth(a,b,d)
            assert depth==formula(a,b),(d,a,b,depth,formula(a,b))
            quotient_checks+=1

full_checks=orbit_checks=0
for d in (2,3):
    for a in range(1,5):
        for b in range(1,5):
            depth,stable,meta=full_cr(a,b,d)
            assert depth==formula(a,b),(d,a,b,depth,formula(a,b))
            assert stable==predicted_orbits(a,b,meta),(d,a,b)
            full_checks+=1; orbit_checks+=1

print("VERIFY_OK "
      f"quotient_depth_checks={quotient_checks} "
      f"full_graph_checks={full_checks} orbit_checks={orbit_checks} "
      "d=2..5 a,b=1..25; full d=2,3 a,b=1..4")
