#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations
from math import comb


def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def build_graph(parts):
    cls=[]
    for i,n in enumerate(parts):
        cls += [i]*n
    N=len(cls)
    adj=[0]*N
    for u in range(N):
        for v in range(u+1,N):
            if cls[u] != cls[v]:
                adj[u] |= 1<<v
                adj[v] |= 1<<u
    return cls, adj


def dominates(mask, adj, N):
    for v in range(N):
        if not (mask>>v)&1 and (adj[v] & mask)==0:
            return False
    return True


def has_perfect_matching(mask, adj):
    @lru_cache(None)
    def rec(m):
        if m==0:
            return True
        if m.bit_count() & 1:
            return False
        u=(m & -m).bit_length()-1
        cand=adj[u] & m & ~(1<<u)
        while cand:
            vb=cand & -cand
            v=vb.bit_length()-1
            if rec(m & ~(1<<u) & ~(1<<v)):
                return True
            cand -= vb
        return False
    return rec(mask)


def theorem(mask, cls, parts):
    t=mask.bit_count()
    if t<2 or t%2:
        return False
    q=t//2
    counts=[0]*len(parts)
    for v,c in enumerate(cls):
        if (mask>>v)&1:
            counts[c]+=1
    return max(counts, default=0) <= q


def coeff_formula(parts, q):
    N=sum(parts)
    if 2*q>N:
        return 0
    bad=0
    for n in parts:
        for j in range(q+1, min(n,2*q)+1):
            rem=2*q-j
            if 0<=rem<=N-n:
                bad += comb(n,j)*comb(N-n,rem)
    return comb(N,2*q)-bad


def run():
    graph_types=0
    subset_checks=0
    coeff_checks=0
    for N in range(2,10):
        for parts in integer_partitions(N):
            if len(parts)<2:
                continue
            graph_types += 1
            cls,adj=build_graph(parts)
            brute=[0]*(N+1)
            for mask in range(1<<N):
                actual=dominates(mask,adj,N) and has_perfect_matching(mask,tuple(adj))
                predicted=theorem(mask,cls,parts)
                subset_checks += 1
                if actual != predicted:
                    raise AssertionError((parts,mask,actual,predicted))
                if actual:
                    brute[mask.bit_count()] += 1
            for q in range(1,N//2+1):
                want=coeff_formula(parts,q)
                got=brute[2*q]
                coeff_checks += 1
                if got != want:
                    raise AssertionError((parts,q,got,want))
            for k in range(1,N+1,2):
                if brute[k] != 0:
                    raise AssertionError((parts,'odd',k,brute[k]))
            m=max(parts)
            Q=min(N//2,N-m)
            support=[k for k,c in enumerate(brute) if c]
            expected=list(range(2,2*Q+1,2))
            if support != expected:
                raise AssertionError((parts,'support',support,expected))
            edges=sum(parts[i]*parts[j] for i in range(len(parts)) for j in range(i+1,len(parts)))
            if brute[2] != edges:
                raise AssertionError((parts,'edges',brute[2],edges))
    print(f'VERIFY_OK graph_types={graph_types} subset_checks={subset_checks} coefficient_checks={coeff_checks} max_order=9')

if __name__=='__main__':
    run()
