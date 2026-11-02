#!/usr/bin/env python3
"""Exhaustive finite checks of canonical caterpillar spines, truncation orbits, and the recycled-parent leaf test."""
from itertools import product,permutations
from math import floor

def edges(b):
    m=len(b);g=[set() for _ in range(m+sum(b))]
    def join(i,j):g[i].add(j);g[j].add(i)
    for i in range(m-1):join(i,i+1)
    p=m
    for i,num in enumerate(b):
        for _ in range(num):join(i,p);p+=1
    return g

def accepted(b):
    return (len(b)==1 and b[0]>=2) or (len(b)>=2 and b[0]>=1 and b[-1]>=1 and all(v>=0 for v in b))

def at_least_k_leaves_recycled(g,spine,k):
    leaves=[x for x in range(len(g)) if len(g[x])==1]
    # choose k-1 witnesses next to spine while it is still named
    from itertools import permutations
    for old in permutations([x for x in g[spine] if x in leaves],k-1):
        # rebind the original 'spine' name to an extra leaf y;
        # a stored name is then rebound to the common parent of y and old[0].
        for extra in leaves:
            if extra in old:continue
            if any(parent in g[extra] and parent in g[old[0]] for parent in range(len(g))):
                return True
    return False

def expected_number(k,m):
    if m==1:return k-1
    return (k*k*(k+1)**(m-2)+k*(k+1)**((m-1)//2))//2

def expected_words(k,m):
    if m==1:return [(v,) for v in range(2,k+1)]
    return list(product(range(1,k+1),*([range(k+1)]*(m-2)),range(1,k+1)))

def main():
    graph_checks=0;local_checks=0; formula_checks=0
    for m in range(1,6):
        for bs in product(*( ([range(2,7)] if m==1 else [range(1,6)]+[range(0,5)]*(m-2)+[range(1,6)]) )):
            if len(bs)+sum(bs)>19:continue
            assert accepted(bs)
            g=edges(bs)
            core={i for i,nbrs in enumerate(g) if len(nbrs)>=2}
            assert core==set(range(m)),(bs,core)
            assert sum(len(x) for x in g)==2*(len(g)-1)
            assert all(len(g[i])==1 for i in range(m,len(g)))
            for i in core:
                leaf_count=sum(len(g[x])==1 for x in g[i])
                assert leaf_count==bs[i]
                for k in (3,4,5):
                    obs=at_least_k_leaves_recycled(g,i,k)
                    exp=bs[i]>=k
                    assert obs==exp,(bs,i,k,obs,exp)
                    local_checks+=1
            graph_checks+=1
    for k in (3,4,5):
        for m in range(1,6):
            words=expected_words(k,m)
            orbits={min(w,w[::-1]) for w in words}
            exp=expected_number(k,m)
            assert len(orbits)==exp,(k,m,len(orbits),exp)
            formula_checks+=1
    print('Canonical caterpillar structure:',graph_checks,'graphs PASS')
    print('Recycled-parent k-leaf test:',local_checks,'point/k configurations PASS')
    print('Burnside orbit counts:',formula_checks,'(k,m) parameter pairs PASS')
    print('STRUCTURAL VERIFICATION PASS')
if __name__=='__main__':main()
