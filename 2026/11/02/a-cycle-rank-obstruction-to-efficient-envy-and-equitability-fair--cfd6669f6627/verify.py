#!/usr/bin/env python3
"""Independent finite check of the degree-two binary-goods cycle-rank theorem."""
from itertools import product
from collections import defaultdict

def canonical(n):
    z=[0]*(2*n)
    def rec(k,mx):
        if k==2*n:
            yield tuple((z[2*i],z[2*i+1]) for i in range(n))
            return
        for v in range(mx+2):
            if k%2 and v==z[k-1]:
                continue
            z[k]=v
            yield from rec(k+1,max(mx,v))
    yield from rec(1,0)

def saturation(sides):
    n=len(sides); m=max(max(p) for p in sides)+1
    adj=[list(p) for p in sides]
    inv=[[] for _ in range(m)]
    for i,pp in enumerate(sides):
        for p in pp:inv[p].append(i)
    def match(left, right_n):
        taken=[-1]*right_n
        def augment(u,seen):
            for v in left[u]:
                if v in seen:continue
                seen.add(v)
                if taken[v]<0 or augment(taken[v],seen):
                    taken[v]=u;return True
            return False
        return all(augment(i,set()) for i in range(len(left)))
    return match(adj,m) or match(inv,n)

def component_criterion(sides):
    m=max(max(p) for p in sides)+1
    adj=[[] for _ in range(m)]
    for a,b in sides:
        adj[a].append(b);adj[b].append(a)
    visited=set();tree=False;multiple=False
    for v in range(m):
        if v in visited:continue
        stack=[v];visited.add(v);vertices=0;deg=0
        while stack:
            u=stack.pop();vertices+=1;deg+=len(adj[u])
            for w in adj[u]:
                if w not in visited:visited.add(w);stack.append(w)
        edges=deg//2
        tree |= edges<vertices
        multiple |= edges>vertices
    return not(tree and multiple)

def brute_fair(sides):
    n=len(sides);m=max(max(p) for p in sides)+1
    likers=[[i for i,p in enumerate(sides) if g in p] for g in range(m)]
    for chosen in product(*likers):
        bundles=[set() for _ in range(n)]
        for g,i in enumerate(chosen):bundles[i].add(g)
        own=[sum(g in sides[i] for g in bundles[i]) for i in range(n)]
        eqx=all(own[i]>=own[j]-1 for i in range(n) for j in range(n) for _ in bundles[j])
        if not eqx:continue
        efx=all(own[i]>=sum(g in sides[i] for g in bundles[j] if g!=removed)
                for i in range(n) for j in range(n)
                for removed in bundles[j] if removed in sides[i])
        if efx:return True
    return False

def main():
    counts={}
    for n in (2,3,4):
        k=0;f=0
        for sides in canonical(n):
            k+=1
            expected=component_criterion(sides)
            assert saturation(sides)==expected,(n,sides,'matching')
            assert brute_fair(sides)==expected,(n,sides,'allocation')
            if not expected:f+=1
        counts[n]=(k,f)
    assert counts=={2:(7,0),3:(87,0),4:(1657,16)},counts
    n=5;k=0;f=0
    for sides in canonical(n):
        k+=1;expected=component_criterion(sides)
        assert saturation(sides)==expected,(n,sides)
        if not expected:f+=1
    assert k==43833 and f==1280,(k,f)
    witness=((0,1),(0,1),(0,1),(2,3))
    assert not brute_fair(witness) and not component_criterion(witness)
    simple=((0,1),(0,2),(0,3),(1,2),(1,3),(4,5))
    assert len({frozenset(p) for p in simple})==6 and not brute_fair(simple)
    print('VERIFY_OK n2=7 n3=87 n4=1657 n5_matching=43833 n4_failure=16 n5_failure=1280')
if __name__=='__main__':main()
