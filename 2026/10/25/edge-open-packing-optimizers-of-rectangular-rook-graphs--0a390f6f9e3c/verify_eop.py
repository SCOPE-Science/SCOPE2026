#!/usr/bin/env python3
"""Independent finite checks for edge-open packing on labeled rook boards.

The implementation uses the graph's original adjacency relation, not the
row-block proof. Run: python verify_eop.py
"""
from itertools import combinations
from collections import Counter
from math import factorial

def graph(p,q):
    vv=tuple((i,j) for i in range(p) for j in range(q))
    es=tuple((a,b) for a,b in combinations(range(len(vv)),2)
             if vv[a][0]==vv[b][0] or vv[a][1]==vv[b][1])
    return vv,es

def conflict_matrix(p,q):
    v,e=graph(p,q)
    es=set(e)
    n=len(e)
    compat=[0]*n
    for i,(a,b) in enumerate(e):
        for j in range(i+1,n):
            c,d=e[j]
            bad=False
            for x in (a,b):
                for y in (c,d):
                    z=tuple(sorted((x,y)))
                    if x!=y and z in es and z != (a,b) and z!=(c,d):
                        bad=True
            if not bad:
                compat[i]|=1<<j
    return compat

def counts(p,q):
    cp=conflict_matrix(p,q)
    number=Counter({0:1})
    def rec(bits,depth):
        while bits:
            last=bits & -bits
            i=last.bit_length()-1
            bits ^= last
            number[depth+1]+=1
            rec(bits&cp[i],depth+1)
    rec((1<<len(cp))-1,0)
    mx=max(number)
    return mx,number[mx],sum(number.values())-1

def predicted(p,q):
    if p>q:p,q=q,p
    assert p>=2
    if p==q and p%2==1:
        l=(p-1)//2
        return p-1,factorial(p)**2//factorial(l) + factorial(p)**2//(4*factorial(l-1))
    k=p
    total=0
    for h in range(p%2,min(p,q-p)+1,2):
        l=(p-h)//2
        total += factorial(p)*factorial(q)//(2**h*factorial(l)*factorial(h)*factorial(q-p-h))
    return k,total

if __name__=='__main__':
    boards=[(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5)]
    total=0
    for p,q in boards:
        obs,ct,tested=counts(p,q)
        exp,ec=predicted(p,q)
        print(f'{p}x{q}: maximum={obs}, maximizing_sets={ct}, inspected_nonempty_EOP={tested}')
        assert (obs,ct)==(exp,ec), (p,q,obs,ct,exp,ec)
        total+=tested
    print(f'PASS: {len(boards)} labeled rook boards, {total} EOP sets enumerated')
