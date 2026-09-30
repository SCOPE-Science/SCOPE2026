#!/usr/bin/env python3
from itertools import combinations


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for tail in partitions(n - x, x):
            yield (x,) + tail


def graph(parts):
    labels=[]
    for i,n in enumerate(parts):
        labels += [(i,j) for j in range(n)]
    idx={v:k for k,v in enumerate(labels)}
    V=range(len(labels))
    part=[labels[v][0] for v in V]
    E=[(u,v) for u in V for v in range(u+1,len(labels)) if part[u]!=part[v]]
    return list(V), E, part


def dv(u,v,part):
    if u==v: return 0
    return 2 if part[u]==part[v] else 1


def de(s,e,part):
    return min(dv(s,e[0],part), dv(s,e[1],part))


def resolving(S,V,E,part,mixed=False):
    elems=[('v',v) for v in V] + ([('e',e) for e in E] if mixed else [('e',e) for e in E])
    if not mixed:
        elems=[('e',e) for e in E]
    seen={}
    for kind,obj in elems:
        rep=[]
        for s in S:
            rep.append(dv(s,obj,part) if kind=='v' else de(s,obj,part))
        rep=tuple(rep)
        if rep in seen:
            return False
        seen[rep]=(kind,obj)
    return True


def minimum(parts,mixed=False):
    V,E,part=graph(parts)
    for k in range(len(V)+1):
        for S in combinations(V,k):
            if resolving(S,V,E,part,mixed=mixed):
                return k
    raise AssertionError


def predicted_mixed(parts):
    N=sum(parts); r=len(parts); s=sum(x==1 for x in parts)
    if s>=2:
        return N
    if r==2 and min(parts)>=3:
        return N-2
    return N-1


def predicted_edge_rge3(parts):
    assert len(parts)>=3
    return sum(parts)-1

count=0
for N in range(2,9):
    for parts in partitions(N):
        if len(parts)<2:
            continue
        m=minimum(parts, mixed=True)
        p=predicted_mixed(parts)
        assert m==p, (parts,m,p)
        if len(parts)>=3:
            e=minimum(parts, mixed=False)
            pe=predicted_edge_rge3(parts)
            assert e==pe, (parts,e,pe)
        count+=1
print(f'VERIFIED {count} complete multipartite types of orders 2 through 8')
print('MIXED_FORMULA_OK')
print('EDGE_R_GE_3_CORRECTION_OK')
