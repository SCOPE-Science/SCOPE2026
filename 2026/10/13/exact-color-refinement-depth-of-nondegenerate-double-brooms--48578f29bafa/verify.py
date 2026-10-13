#!/usr/bin/env python3
from collections import defaultdict

def double_broom(p,q,L):
    # Path vertices 0,...,L are the two star centers and the spine.
    adj=[set() for _ in range(L+1+p+q)]
    for i in range(L):
        adj[i].add(i+1); adj[i+1].add(i)
    z=L+1
    left=[]
    for _ in range(p):
        adj[0].add(z); adj[z].add(0); left.append(z); z+=1
    right=[]
    for _ in range(q):
        adj[L].add(z); adj[z].add(L); right.append(z); z+=1
    return adj,left,right

def partition(colors):
    cells=defaultdict(set)
    for v,c in enumerate(colors): cells[c].add(v)
    return frozenset(frozenset(x) for x in cells.values())

def color_refinement(adj):
    colors=[0]*len(adj)
    old=partition(colors)
    for r in range(len(adj)+3):
        sig=[(colors[v],tuple(sorted(colors[w] for w in adj[v])))
             for v in range(len(adj))]
        names={}
        new=[names.setdefault(s,len(names)) for s in sig]
        newpart=partition(new)
        if newpart==old:
            return r,old
        colors,old=new,newpart
    raise RuntimeError("no stabilization")

def formula(p,q,L):
    if p==q:
        return max(1,L//2)
    return max(2,(L+1)//2)

def orbit_partition(p,q,L,left,right):
    cells=[]
    if p==q:
        cells.append(set(left+right))
        seen=set()
        for i in range(L+1):
            if i in seen: continue
            j=L-i
            cells.append({i,j})
            seen.add(i); seen.add(j)
    else:
        cells.append(set(left)); cells.append(set(right))
        cells.extend([{i} for i in range(L+1)])
    return frozenset(frozenset(x) for x in cells)

depth_checks=orbit_checks=0
for p in range(2,21):
    for q in range(2,21):
        for L in range(1,41):
            adj,left,right=double_broom(p,q,L)
            depth,stable=color_refinement(adj)
            assert depth==formula(p,q,L),(p,q,L,depth,formula(p,q,L))
            assert stable==orbit_partition(p,q,L,left,right),(p,q,L)
            depth_checks+=1
            orbit_checks+=1

print(f"VERIFY_OK depth_checks={depth_checks} orbit_checks={orbit_checks} p,q=2..20 L=1..40")
