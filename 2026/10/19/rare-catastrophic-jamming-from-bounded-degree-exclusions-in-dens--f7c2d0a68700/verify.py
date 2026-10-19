"""Finite direct checks for rare-jamming theorem on dense bipartite exclusion graphs.
Requires only Python 3 standard library. Run: python verify.py
"""
from itertools import permutations
from fractions import Fraction
from math import factorial
from collections import Counter
from random import Random

def greedy(n, missing, ordering):
    taken=[]
    for v in ordering:
        if all(not ((u<n) != (v<n) and (min(u,v),max(u,v)-n) not in missing) for u in taken):
            taken.append(v)
    return taken

def exceptional_certificate(n, missing, ordering):
    first=ordering[0]
    a=first if first<n else first-n
    first_left=first<n
    ranks={v:i for i,v in enumerate(ordering)}
    if first_left:
        candidates=[n+j for j in range(n) if (a,j) in missing]
        return any(all(ranks[y]<ranks[i] for i in range(n) if (i,y-n) not in missing)
                   for y in candidates)
    candidates=[i for i in range(n) if (i,a) in missing]
    return any(all(ranks[y]<ranks[n+j] for j in range(n) if (y,j) not in missing)
               for y in candidates)

def exact_check(n, missing):
    spectrum=Counter()
    checks=0
    d=max([0]+[sum((i,j) in missing for j in range(n)) for i in range(n)]+[sum((i,j) in missing for i in range(n)) for j in range(n)])
    for order in permutations(range(2*n)):
        accepted=greedy(n,missing,order)
        cross=bool(any(v<n for v in accepted) and any(v>=n for v in accepted))
        assert cross == exceptional_certificate(n,missing,order), ('cross-event',n,missing,order,accepted)
        if cross:
            assert 2<=len(accepted)<=2*d
        else:
            assert len(accepted)==n
        spectrum[len(accepted)]+=1
        checks+=1
    return checks,spectrum

def main():
    checked=0; graph_count=0
    for bits in range(1<<9):
        H={(i,j) for i in range(3) for j in range(3) if bits>>(3*i+j)&1}
        if max([0]+[sum((i,j) in H for j in range(3)) for i in range(3)]+[sum((i,j) in H for i in range(3)) for j in range(3)])>2:continue
        k,spec=exact_check(3,H);checked+=k;graph_count+=1
        if H=={(0,0),(1,1),(2,2)}:
            assert spec == {2:240,3:480},spec
    for n,H in [(4,set()),(4,{(i,i) for i in range(4)}),
                (4,{(0,0),(0,1),(1,1),(2,2),(3,3)}),
                (4,{(0,0),(0,1),(1,1),(1,2),(2,2),(3,3)}),
                (4,{(i,i) for i in range(4)}|{(i,(i+1)%4) for i in range(4)})]:
        k,spec=exact_check(n,H);checked+=k;graph_count+=1
        if H=={(i,i) for i in range(4)}:assert spec=={2:10080,4:30240},spec
        if H==({(i,i) for i in range(4)}|{(i,(i+1)%4) for i in range(4)}):
            assert spec=={3:21504,4:18816},spec
    rng=Random(20261016)
    for n in (5,10,25):
        H={(i,i) for i in range(n)}
        misses=0; reps=20000
        for _ in range(reps):
            order=list(range(2*n));rng.shuffle(order)
            K=len(greedy(n,H,order));assert K in (2,n)
            misses+=(K==2)
        assert abs(misses/reps-1/n)<0.03,(n,misses)
    print('PASS exact ordered-configurations:',checked)
    print('PASS distinct bounded-degree missing-edge graphs:',graph_count)
    print('PASS exact matching law n=3,4 and exact cycle law n=4; matching stochastic cross-check n=5,10,25')
if __name__=='__main__':main()
