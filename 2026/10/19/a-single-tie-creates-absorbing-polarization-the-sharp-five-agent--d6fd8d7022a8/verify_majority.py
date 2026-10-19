"""Exact finite-graph verifier for binary tie-retaining asynchronous majority updates.
Standalone Python 3, standard library only; deterministic and no external data files.
"""
from itertools import combinations, permutations
from fractions import Fraction
from functools import lru_cache
from math import comb


def edge_pairs(n):
    return list(combinations(range(n), 2))


def conn(n, es):
    seen = {0}
    while True:
        reach = seen | {v for u,v in es if u in seen} | {u for u,v in es if v in seen}
        if reach == seen: return len(seen) == n
        seen = reach


def stable_states(n, es):
    adj = [0]*n
    for u,v in es:
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    stable = []
    for s in range(1, (1<<n)-1):
        if all(2*(adj[v] & (s if not(s>>v & 1) else ((1<<n)-1)^s)).bit_count() <= adj[v].bit_count() for v in range(n)):
            stable.append(s)
    return stable


def canon_pair(n, es, add):
    def transform(per):
        re = tuple(sorted(tuple(sorted((per[u],per[v]))) for u,v in es))
        a = tuple(sorted((per[add[0]],per[add[1]])))
        return re, a
    return min(transform(p) for p in permutations(range(n)))


def absorption(n, es):
    adj = [0]*n
    for u,v in es:
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    @lru_cache(None)
    def f(s):
        flips = [v for v in range(n) if 2*(adj[v] & (s if not(s>>v&1) else ((1<<n)-1)^s)).bit_count() > adj[v].bit_count()]
        if not flips:
            return Fraction(s not in (0,(1<<n)-1)), Fraction(0)
        vals = [f(s^(1<<v)) for v in flips]
        return (sum((a for a,b in vals),Fraction(0))/len(flips),
                Fraction(n,len(flips))+sum((b for a,b in vals),Fraction(0))/len(flips))
    vals = [f(s) for s in range(1<<n)]
    return sum((p for p,t in vals),Fraction(0))/(1<<n), sum((t for p,t in vals),Fraction(0))/(1<<n)


def main():
    for n in range(2,6):
        pairs=edge_pairs(n); kinds={}; total=0; connected=0
        for em in range(1<<len(pairs)):
            es=frozenset(e for i,e in enumerate(pairs) if em>>i&1)
            if not conn(n,es): continue
            connected+=1
            if stable_states(n,es): continue
            for add in pairs:
                if add in es:continue
                new_es=es|{add}
                if not stable_states(n,new_es):continue
                total+=1
                key=canon_pair(n,es,add)
                kinds[key]=kinds.get(key,0)+1
        print('n',n,'connected_labelled_graphs',connected,'creation_labelled_pairs',total,'marked_isomorphism_classes',len(kinds))
        for (edges,added),count in sorted(kinds.items()):
            pre_p,pre_t=absorption(n,edges)
            post_p,post_t=absorption(n,edges+(added,))
            print('  G',edges,'added',added,'labelled_count',count,'p_before',pre_p,'p_after',post_p,'mean_attempts_before',pre_t,'after',post_t)
    # Independent aggregation for exact absorption probabilities; recurrence includes all inert update attempts.
    for n in range(5,15):
        es = [(0,i) for i in range(1,n)] + [(1,2)]
        if n <= 10:
            prob,_=absorption(n,es)
            print('star+edge n=',n,'p=',prob,'approx=',float(prob))
    print('verification_complete')

if __name__=='__main__':main()
