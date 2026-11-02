#!/usr/bin/env python3
"""Definition-level exact census for short balanced run-two one-deletion codes.
Python 3.9+; standard library only. Run: python verify_census.py
All maximal cliques, not just greedy candidates, are enumerated.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

LENGTHS = (4, 6, 8, 10)
EXPECTED = {4:(6, 2, 4, 4), 6:(14, 4, 4, 16),
            8:(34, 8, 1, 520), 10:(84, 15, 20, 675239)}

def universe(n):
    # Definition-level generator; no precomputed word tables.
    return tuple(''.join('1' if j in c else '0' for j in range(n))
                 for c in combinations(range(n), n//2)
                 if all(not all(j in c for j in range(i,i+3))
                         and not all(j not in c for j in range(i,i+3))
                         for i in range(n-2)))

def deletions(s):
    return frozenset(s[:i]+s[i+1:] for i in range(len(s)))

def compatibility(words):
    n=len(words); a=[0]*n
    # Direct comparison of the complete deletion shadows for every pair.
    desc=[deletions(w) for w in words]
    for i in range(n):
        for j in range(i+1,n):
            if desc[i].isdisjoint(desc[j]):
                a[i] |= 1<<j
                a[j] |= 1<<i
    return tuple(a)

def check_edges_independently(words, adj):
    # Different graph constructor: create conflict pairs from individual
    # observed length-(n-1) strings instead of pairwise shadow intersections.
    bins={}
    for i,w in enumerate(words):
        for d in deletions(w):bins.setdefault(d,set()).add(i)
    conflicts=set()
    for indices in bins.values():
        for i,j in combinations(sorted(indices),2):conflicts.add((i,j))
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            assert bool(adj[i]&(1<<j))==((i,j) not in conflicts)

def all_maximal_cliques(adj):
    # Bron--Kerbosch with pivot; bit masks represent vertices in P and X.
    # Every call maintains R clique and P,X its common neighbors; pivoting
    # partitions all extensions and visits each maximal clique once.
    n=len(adj); counts=Counter(); largest=0; maxima=[]
    def rec(R,P,X):
        nonlocal largest,maxima
        if not (P or X):
            k=len(R)
            counts[k]+=1
            if k>largest:
                largest=k
                maxima=[]
            if k==largest:
                maxima.append(tuple(sorted(R)))
            return
        choices=P|X
        if choices:
            tmp=choices; pivot=-1; best=-1
            while tmp:
                bit=tmp & -tmp; j=bit.bit_length()-1
                v=(P&adj[j]).bit_count()
                if v>best:best=v; pivot=j
                tmp ^= bit
            branches=P & ~adj[pivot]
        else:branches=P
        while branches:
            bit=branches & -branches; v=bit.bit_length()-1
            rec(R+(v,),P&adj[v],X&adj[v])
            P &= ~bit
            X |= bit
            branches &= ~bit
    rec((),(1<<n)-1,0)
    return largest,counts,tuple(maxima)

def reverse(w):return w[::-1]
def complement(w):return ''.join('0' if x=='1' else '1' for x in w)

def orbits_under_reversal_and_complement(maxima,words):
    index={w:i for i,w in enumerate(words)}
    group=(lambda w:w, reverse, complement, lambda w:complement(reverse(w)))
    todo=set(map(frozenset,maxima)); all_orbits=[]
    while todo:
        C=min(todo,key=lambda c:tuple(sorted(c)))
        orb=set()
        for g in group:
            orb.add(frozenset(index[g(words[i])] for i in C))
        assert orb <= todo
        assert len(orb)<=4
        todo.difference_update(orb)
        all_orbits.append(orb)
    return tuple(sorted(len(O) for O in all_orbits))

def canonical_maxima(maxima,words):
    return sorted([sorted(words[i] for i in C) for C in maxima])

def run():
    data=json.loads((Path(__file__).resolve().parent/'maxima.json').read_text(encoding='utf-8'))
    for n in LENGTHS:
        words=universe(n)
        graph=compatibility(words)
        check_edges_independently(words,graph)
        k,counts,maxima=all_maximal_cliques(graph)
        assert (len(words),k,len(maxima),sum(counts.values()))==EXPECTED[n]
        assert canonical_maxima(maxima,words)==data[str(n)]['all_maxima']
        # Each advertised codebook is definition-level collision-free.
        for C in maxima:
            shadows=[deletions(words[i]) for i in C]
            for a,b in combinations(shadows,2):assert a.isdisjoint(b)
        if n==10:
            assert orbits_under_reversal_and_complement(maxima,words)==(2,2,2,2,2,2,4,4)
            assert data['10']['orbit_sizes']==[2,2,2,2,2,2,4,4]
        elif n==8:
            assert orbits_under_reversal_and_complement(maxima,words)==(1,)
        if n in (8,10):
            pure_classes=[]
            for C in maxima:
                syndromes={sum((i+1)*int(words[j][i]) for i in range(n))%(n//2+1) for j in C}
                if len(syndromes)==1:
                    s=next(iter(syndromes))
                    full_class={j for j,word in enumerate(words)
                                if sum((i+1)*int(bit) for i,bit in enumerate(word))%(n//2+1)==s}
                    assert full_class==set(C)
                    pure_classes.append(s)
            assert sorted(pure_classes)==([3] if n==8 else [3,4])
        print(f'n={n}: admissible={len(words)} max_size={k} maximum_codebooks={len(maxima)} total_maximal_cliques={sum(counts.values())}')
    print('VERIFY_OK')

if __name__=='__main__':run()
