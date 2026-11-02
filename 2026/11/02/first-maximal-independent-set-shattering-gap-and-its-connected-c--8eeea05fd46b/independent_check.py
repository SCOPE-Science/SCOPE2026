#!/usr/bin/env python3
"""Independent maximal-clique complement enumeration and online learning tree test."""
from itertools import combinations, permutations
from functools import lru_cache
from collections import Counter


def indep_via_cliques(n,E):
    edge=set(E)
    # Independent sets of G are cliques in complement(G).
    all_sets=[]
    for sz in range(n+1):
        for C in combinations(range(n),sz):
            if all((min(a,b),max(a,b)) not in edge for a,b in combinations(C,2)):
                all_sets.append(sum(1<<v for v in C))
    return tuple(s for s in all_sets if all(s==t or (s & t)!=s for t in all_sets))


def VCD(n,H):
    best=0
    for mask in range(1<<n):
        k=mask.bit_count()
        if k>best and len({mask&s for s in H})==(1<<k):best=k
    return best


def LDim(n,H):
    @lru_cache(None)
    def can(depth,sub):
        if depth==0:return True
        if len(sub)<(1<<depth):return False
        for v in range(n):
            a=tuple(s for s in sub if s & 1<<v)
            b=tuple(s for s in sub if not s & 1<<v)
            if len(a)>=(1<<(depth-1)) and len(b)>=(1<<(depth-1)) and can(depth-1,a) and can(depth-1,b):
                return True
        return False
    return max(d for d in range(n+1) if can(d,H))


def canonical(n,E):
    pairs=list(combinations(range(n),2));e=set(E)
    return min(tuple(int((min(p[a],p[b]),max(p[a],p[b])) in e) for a,b in pairs) for p in permutations(range(n)))


def main():
    for n in range(1,6):
        edges_all=list(combinations(range(n),2))
        classes=Counter(); n_gap=0
        for code in range(1<<len(edges_all)):
            E=[edges_all[i] for i in range(len(edges_all)) if code>>i&1]
            H=indep_via_cliques(n,E)
            v=VCD(n,H);l=LDim(n,H)
            if l>v:
                assert n==5 and (v,l)==(1,2)
                classes[canonical(n,E)]+=1;n_gap+=1
        if n<=4:assert n_gap==0
        if n==5:assert n_gap==90 and sorted(classes.values())==[30,60]
        print('INDEPENDENT_ORDER',n,'GAPS',n_gap)
    print('INDEPENDENT_FULL_CENSUS_PASS')

if __name__=='__main__':main()
