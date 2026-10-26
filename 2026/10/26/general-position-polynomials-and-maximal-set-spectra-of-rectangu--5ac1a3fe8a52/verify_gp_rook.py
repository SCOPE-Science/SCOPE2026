#!/usr/bin/env python3
"""Independent finite tests for general-position sets of rectangular rook graphs."""
from collections import Counter,deque
from functools import lru_cache
from math import comb,factorial

def add(a,b,shift=0,mult=1):
    ans=a.copy()
    for k,v in b.items(): ans[k+shift]=ans.get(k+shift,0)+v*mult
    return {k:v for k,v in ans.items() if v}

@lru_cache(None)
def all_star_forests(p,q):
    if p==0 or q==0: return {0:1}
    z=all_star_forests(p-1,q).copy()
    z=add(z,all_star_forests(p-1,q-1),1,q)
    for k in range(2,q+1): z=add(z,all_star_forests(p-1,q-k),k,comb(q,k))
    for k in range(2,p+1): z=add(z,all_star_forests(p-k,q-1),k,q*comb(p-1,k-1))
    return z

@lru_cache(None)
def covered_star_forests(p,q):
    if p==q==0: return {0:1}
    if p==0 or q==0: return {}
    z={}
    z=add(z,covered_star_forests(p-1,q-1),1,q)
    for k in range(2,q+1): z=add(z,covered_star_forests(p-1,q-k),k,comb(q,k))
    for k in range(2,p+1): z=add(z,covered_star_forests(p-k,q-1),k,q*comb(p-1,k-1))
    return z

@lru_cache(None)
def associated_stirling(n,h):
    if n==0 and h==0: return 1
    if n==0 or h==0 or n<2*h: return 0
    return h*associated_stirling(n-1,h)+(n-1)*associated_stirling(n-2,h-1)

def falling(n,h): return factorial(n)//factorial(n-h)

def maximal_formula(p,q):
    z=covered_star_forests(p,q).copy()
    for h in range(1,min(p-1,q//2)+1):
        z=add(z,{0:1},q,falling(p,h)*associated_stirling(q,h))
    for h in range(1,min(q-1,p//2)+1):
        z=add(z,{0:1},p,falling(q,h)*associated_stirling(p,h))
    return z

def gp_direct(p,q,mask):
    # Every pair of nonadjacent selected cells has precisely two length-2 geodesics.
    cells=[(i,j) for i in range(p) for j in range(q) if (mask>>(i*q+j))&1]
    for a,(i,j) in enumerate(cells):
        for k,l in cells[a+1:]:
            if i!=k and j!=l:
                if mask & (1<<(i*q+l)) or mask & (1<<(k*q+j)):
                    return False
    return True

def star_forest_direct(p,q,mask):
    adj={i:set() for i in range(p+q)}
    for i in range(p):
        for j in range(q):
            if mask>>(i*q+j)&1:
                adj[i].add(p+j); adj[p+j].add(i)
    visited=set()
    for v in range(p+q):
        if v in visited or not adj[v]: continue
        comp=set([v]); todo=[v]; visited.add(v)
        while todo:
            for w in adj[todo.pop()]:
                if w not in visited:
                    visited.add(w); comp.add(w); todo.append(w)
        e=sum(len(adj[w]) for w in comp)//2
        if e!=len(comp)-1 or (e>1 and max(map(lambda w:len(adj[w]),comp))!=e):
            return False
    return True

def maximal_structural(p,q,mask):
    dl=[0]*p; dr=[0]*q
    for i in range(p):
        for j in range(q):
            if mask>>(i*q+j)&1: dl[i]+=1; dr[j]+=1
    zleft=dl.count(0); zright=dr.count(0)
    if not zleft and not zright:return True
    if zleft and zright:return False
    if zleft: return zright==0 and all(d==0 or d>=2 for d in dl) and all(d==1 for d in dr)
    return zleft==0 and all(d==0 or d>=2 for d in dr) and all(d==1 for d in dl)

def check(p,q):
    all_counts=Counter();max_counts=Counter();checked=0
    for mask in range(1<<(p*q)):
        gp=gp_direct(p,q,mask)
        assert gp==star_forest_direct(p,q,mask),(p,q,mask,'star equivalence')
        if gp:
            k=mask.bit_count();all_counts[k]+=1
            maximal=all(not gp_direct(p,q,mask|(1<<v)) for v in range(p*q) if not(mask>>v&1))
            assert maximal==maximal_structural(p,q,mask),(p,q,mask,'maximal equivalence')
            if maximal:max_counts[k]+=1
        checked+=1
    assert dict(all_counts)==all_star_forests(p,q),(p,q,'all polynomial',all_counts,all_star_forests(p,q))
    assert dict(max_counts)==maximal_formula(p,q),(p,q,'maximal polynomial',max_counts,maximal_formula(p,q))
    support=set(max_counts)
    expected={p,q}|{p+q-k for k in range(2,min(p,q)+1)}
    assert support==expected,(p,q,support,expected)
    assert min(support)==min(p,q)
    assert max(support)==p+q-2
    print(f'{p}x{q}: subsets={checked}, GP={sum(all_counts.values())}, maximal={sum(max_counts.values())}, spectrum={sorted(support)}')
    if (p,q) in [(2,5),(3,5),(4,4)]:
        print('  psi=',dict(sorted(all_counts.items())))
        print('  max=',dict(sorted(max_counts.items())))
    return checked

if __name__=='__main__':
    tests=[(2,2),(2,3),(2,4),(2,5),(2,7),(3,3),(3,4),(3,5),(4,4)]
    total=sum(check(p,q) for p,q in tests)
    for p in range(2,9):
        for q in range(p,13):
            a=all_star_forests(p,q)
            m=maximal_formula(p,q)
            assert sum(a.values())>0 and sum(m.values())>0
            assert a.get(1)==p*q and a.get(2)==comb(p*q,2)
            assert a.get(3,0)==comb(p*q,3)-4*comb(p,2)*comb(q,2)
            if p==2:
                assert a=={k:comb(q,k)*2**k for k in range(q+1)} | ({2:comb(q,2)*4+q} if q>=2 else {})
                assert m==({2:q, q:2**q} if q>2 else {2:6})
            elif p>=3 and q>=3:
                assert m[p+q-2]==p*q
            assert {k for k,v in m.items() if v}==({p,q}|{p+q-c for c in range(2,min(p,q)+1)})
    print('total exhaustive masks:',total)
    print('additional integer-recurrence checks: 7 by up to 11 rectangular parameter pairs')
    print('ALL CHECKS PASS')
