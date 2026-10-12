#!/usr/bin/env python3
from collections import defaultdict

def build(a):
    adj=[set(),set()]
    names={0:"x",1:"y"}
    adj[0].add(1); adj[1].add(0)
    nxt=2
    def arm(center,length,label):
        nonlocal nxt
        prev=center
        for i in range(1,length+1):
            v=nxt; nxt+=1
            adj.append(set()); names[v]=f"{label}{i}"
            adj[prev].add(v); adj[v].add(prev)
            prev=v
    arm(0,a,"A"); arm(0,a,"B"); arm(1,a,"C"); arm(1,a+1,"D")
    return adj,names

def refine(adj, rounds):
    colors=[0]*len(adj)
    parts=[]
    for _ in range(rounds+1):
        g=defaultdict(list)
        for v,c in enumerate(colors): g[c].append(v)
        parts.append(frozenset(frozenset(s) for s in g.values()))
        sig=[(colors[v],tuple(sorted(colors[w] for w in adj[v]))) for v in range(len(adj))]
        mp={}
        colors=[mp.setdefault(s,len(mp)) for s in sig]
    return parts

def mid(a,names):
    inv={name:v for v,name in names.items()}
    classes=[{inv["x"]},{inv["y"]}]
    for i in range(1,a+1):
        classes.append({inv[f"A{i}"],inv[f"B{i}"],inv[f"C{i}"]})
    for j in range(1,a+2):
        classes.append({inv[f"D{j}"]})
    return frozenset(frozenset(s) for s in classes)

def post(a,k,names):
    inv={name:v for v,name in names.items()}
    classes=[{inv["x"]},{inv["y"]}]
    for j in range(1,a+2):
        classes.append({inv[f"D{j}"]})
    for i in range(1,a+1):
        if i<=k:
            classes += [{inv[f"A{i}"],inv[f"B{i}"]},{inv[f"C{i}"]}]
        else:
            classes.append({inv[f"A{i}"],inv[f"B{i}"],inv[f"C{i}"]})
    return frozenset(frozenset(s) for s in classes)

dc=pc=0
for a in range(1,101):
    adj,names=build(a)
    parts=refine(adj,2*a+2)
    s=next(r for r in range(len(parts)-1) if parts[r+1]==parts[r])
    assert s==2*a+1
    dc+=1
    assert parts[a+1]==mid(a,names); pc+=1
    for k in range(1,a+1):
        assert parts[a+1+k]==post(a,k,names); pc+=1
print(f"VERIFY_OK depth_checks={dc} partition_checks={pc} a=1..100")
