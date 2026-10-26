#!/usr/bin/env python3
"""Independent finite checks for one-root colour refinement on odd-cycle powers.
Standard library only. Checks full graphs and independent weighted quotient refinements.
"""
from itertools import product
from math import comb, factorial, prod
from collections import Counter, defaultdict


def partitions_after_rounds(adj, root=0):
    colors = [1 if i == root else 0 for i in range(len(adj))]
    hist = [len(set(colors))]
    snapshots=[colors[:]]
    while True:
        sig = [(colors[i], tuple(sorted(Counter(colors[v] for v in nbr).items())))
               for i, nbr in enumerate(adj)]
        palette = {s: k for k, s in enumerate(sorted(set(sig)))}
        new = [palette[s] for s in sig]
        if len(set(new)) == len(set(colors)):
            break
        colors = new
        hist.append(len(set(colors)))
        snapshots.append(colors[:])
    return colors, hist, snapshots


def fullgraph(n,d):
    V = list(product(range(n), repeat=d))
    idx = {v:i for i,v in enumerate(V)}
    adj = []
    for v in V:
        nbr=[]
        for j in range(d):
            for s in (-1,1):
                z=list(v); z[j]=(z[j]+s)%n
                nbr.append(idx[tuple(z)])
        adj.append(nbr)
    return V,adj


def quotient(n,d):
    r=n//2
    profiles=[v for v in product(range(d+1), repeat=r+1) if sum(v)==d]
    index={p:i for i,p in enumerate(profiles)}
    rows=[]
    for p in profiles:
        counts=Counter()
        for l,num in enumerate(p):
            if not num: continue
            if l==0:
                z=list(p);z[0]-=1;z[1]+=1
                counts[index[tuple(z)]]+=2*num
            else:
                z=list(p);z[l]-=1;z[l-1]+=1
                counts[index[tuple(z)]]+=num
                if l<r:
                    z=list(p);z[l]-=1;z[l+1]+=1
                    counts[index[tuple(z)]]+=num
                else:
                    counts[index[p]]+=num
        rows.append(counts)
    return profiles, rows


def quotient_rounds(profiles, rows):
    root=next(i for i,p in enumerate(profiles) if p[0]==sum(p))
    colors=[1 if i==root else 0 for i in range(len(profiles))]
    hist=[len(set(colors))]
    while True:
        sig=[]
        for i,row in enumerate(rows):
            distribution=Counter()
            for j,m in row.items(): distribution[colors[j]]+=m
            sig.append((colors[i],tuple(sorted(distribution.items()))))
        palette={s:k for k,s in enumerate(sorted(set(sig)))}
        new=[palette[s] for s in sig]
        if len(set(new))==len(set(colors)): break
        colors=new
        hist.append(len(set(colors)))
    return colors,hist


def check_full(n,d):
    V,adj=fullgraph(n,d)
    colors,hist,snapshots=partitions_after_rounds(adj)
    r=n//2
    profile=[]
    for v in V:
        profile.append(tuple(sum(1 for x in v if min(x,n-x)==l) for l in range(r+1)))
    # Test the stronger finite-round statement, not only final orbit equality.
    distances=[sum(min(x,n-x) for x in v) for v in V]
    for t, palette in enumerate(snapshots):
        block=defaultdict(set)
        for i,c in enumerate(palette): block[c].add(i)
        inside={}
        outside=set()
        for c,items in block.items():
            ds={distances[i] for i in items}
            if min(ds)>t:outside.add(c)
            else:
                assert len({profile[i] for i in items})==1,(n,d,t,c)
                assert len(ds)==1 and min(ds)<=t,(n,d,t,c)
                p=profile[next(iter(items))]
                assert p not in inside,(n,d,t,p)
                inside[p]=c
        assert len(outside)<=1,(n,d,t,outside)
        if t<r*d: assert len(outside)==1,(n,d,t)
    cl=defaultdict(set); rev=defaultdict(set)
    for col,p in zip(colors,profile):
        cl[col].add(p);rev[p].add(col)
    assert all(len(s)==1 for s in cl.values())
    assert all(len(s)==1 for s in rev.values())
    assert len(hist)-1==r*d-1,(n,d,hist)
    assert len(hist)==1 or hist[-2]<hist[-1]
    assert len(hist[-1:])==1
    assert len(cl)==comb(d+r,r)
    for p in set(profile):
        size=sum(1 for x in profile if x==p)
        expect=factorial(d)*2**(d-p[0])//prod(factorial(x) for x in p)
        assert size==expect,(n,d,p,size,expect)
    return len(V),len(cl),len(hist)-1


def check_quotient(n,d):
    profiles, rows=quotient(n,d)
    for p,row in zip(profiles,rows):
        assert sum(row.values())==2*d
        # One downward neighbor for every positive coordinate.
        D=sum(i*p_i for i,p_i in enumerate(p))
        expect=d-p[0]
        got=sum(m for q,m in row.items() if sum(i*profiles[q][i] for i in range(len(p)))==D-1)
        assert got==expect,(n,d,p,got,expect)
        # Independently reconstruct the original profile from its multiset
        # of distance-decreasing neighbours (the structural proof's key step).
        down=[(profiles[q],mult) for q,mult in row.items()
              if sum(i*profiles[q][i] for i in range(len(p)))==D-1]
        M=sum(mult for _,mult in down)
        S=[sum(mult*q[i] for q,mult in down) for i in range(len(p))]
        recovered=[d-M]
        if M:
            for i in range(len(p)-1):
                recovered.append(S[i]-(M if i==0 else M-1)*recovered[i])
        else:
            recovered += [0]*(len(p)-1)
        assert tuple(recovered)==p,(n,d,p,recovered)
    colors,hist=quotient_rounds(profiles,rows)
    assert len(hist)-1==n//2*d-1,(n,d,hist)
    assert len(set(colors))==len(profiles),(n,d,hist)
    return len(profiles),len(hist)-1

if __name__=='__main__':
    fullcases=0;verts=0
    for n in range(3,14,2):
        for d in range(1,6):
            if n**d>1600:continue
            v,cl,rounds=check_full(n,d);fullcases+=1;verts+=v
    qc=0;pcs=0
    for n in range(3,24,2):
        for d in range(1,11):
            if comb(d+n//2,n//2)>240: continue
            pc,rounds=check_quotient(n,d);qc+=1;pcs+=pc
    print('FULL_CASES',fullcases,'TOTAL_VERTICES',verts)
    print('QUOTIENT_CASES',qc,'TOTAL_PROFILES',pcs)
    print('ALL_TESTS_PASS')
