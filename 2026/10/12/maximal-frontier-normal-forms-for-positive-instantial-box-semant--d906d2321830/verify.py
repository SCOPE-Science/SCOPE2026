#!/usr/bin/env python3
"""Finite up-set neighbourhood operations: exhaustive independent checking.

A poset is a reflexive, antisymmetric, transitive relation on range(n).
All mask subsets of range(n) are represented as integers.
"""
from itertools import product
from collections import defaultdict
from math import prod

def posets(n):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    for options in product(range(3), repeat=len(pairs)):
        R = [(1<<i) for i in range(n)]
        for (i,j),v in zip(pairs, options):
            if v==1: R[i] |= 1<<j
            if v==2: R[j] |= 1<<i
        if all(not (R[i]&(1<<j)) or (R[i]|R[j])==R[i]
               for i in range(n) for j in range(n)):
            yield R

def upsets(R):
    n=len(R); return [A for A in range(1<<n)
                         if all(not(A&(1<<i)) or (R[i]&A)==R[i] for i in range(n))]

def maximal(R,U):
    return sum(1<<i for i in range(len(R)) if (U&(1<<i)) and (R[i]&U)==(1<<i))

def core(R, N):
    bymax=defaultdict(list)
    for U in N:bymax[maximal(R,U)].append(U)
    return frozenset(U for M, B in bymax.items() for U in B
                     if not any(V!=U and (V&U)==V for V in B))

def operation_signature(R, N, args):
    # Direct semantics: NO reference to the core or domination lemma.
    return tuple(any((U&B)==U and all(U&A for A in AA) for U in N)
                 for (B,AA) in args)

def all_args(R):
    ups=upsets(R); return [(B,AA) for k in range(len(R)+1)
               for AA in product(ups,repeat=k) for B in ups]

def antichains(fibre):
    return sum(1 for bits in range(1<<len(fibre)) if all(
       (a&b)!=a and (a&b)!=b
       for i,a in enumerate(fibre) if bits>>i&1
       for j,b in enumerate(fibre) if bits>>j&1 and i<j))

def formula_count(R):
    ups=upsets(R)
    fibre=defaultdict(list)
    for U in ups:fibre[maximal(R,U)].append(U)
    return prod(antichains(f) for f in fibre.values())

def main():
    counters={}
    for n in (1,2,3):
        ps=list(posets(n)); checked=0; families=0
        for R in ps:
            ups=upsets(R); args=all_args(R)
            # Exhaustive every neighbourhood family, every scope upset and
            # every ordered list of up to n witness upsets.
            signatures={}
            reps={}
            for bitset in range(1<<len(ups)):
                N=[u for j,u in enumerate(ups) if bitset>>j&1]
                C=core(R,N)
                sig=operation_signature(R,N,args)
                if sig in signatures:
                    assert signatures[sig]==C, (n,R,N,'different core same function')
                else: signatures[sig]=C
                if C in reps:
                    assert reps[C]==sig, (n,R,N,'same core different function')
                else: reps[C]=sig
                checked+=1; families+=1
            assert len(signatures)==formula_count(R), (n,R,len(signatures),formula_count(R))
        counters[n]=(len(ps),checked)
    for n in (1,2,3,4):
        R=[sum(1<<j for j in range(i,n)) for i in range(n)]
        got=formula_count(R)
        assert got==2*(n+1), (n,got)
    for n in (1,2,3,4):
        R=[1<<i for i in range(n)]
        got=formula_count(R)
        assert got==2**(2**n),(n,got)
    print('VERIFY_OK: exhaustive full ordered-witness semantic comparison',counters)
    print('VERIFY_OK: chain counts n=1..4', [2*(n+1) for n in range(1,5)])
    print('VERIFY_OK: antichain counts n=1..4',[2**(2**n) for n in range(1,5)])
if __name__=='__main__':main()

# Additional direct edge-case tests can be invoked separately below.
def extra():
    for r in range(0,4):
        n=r+1
        R=[(1<<i)|(1<<r) for i in range(r)]+[(1<<r)]
        ups=upsets(R); args=all_args(R)
        observed=set()
        for subset in range(1<<len(ups)):
            N=[U for i,U in enumerate(ups) if subset>>i&1]
            observed.add(operation_signature(R,N,args))
        assert len(observed)==formula_count(R)
        print('star',r,'worlds',n,'upsets',len(ups),'different',len(observed))
    for n in range(1,5):
        R=[1<<i for i in range(n)]; up=upsets(R)
        N=up; Nminus=[x for x in up if x !=(1<<n)-1]
        low=[(B, AA) for k in range(n) for AA in product(up,repeat=k) for B in up]
        assert operation_signature(R,N,low)==operation_signature(R,Nminus,low)
        AA=tuple(1<<i for i in range(n)); B=(1<<n)-1
        assert operation_signature(R,N,[(B,AA)]) != operation_signature(R,Nminus,[(B,AA)])
        print('sharp arity on discrete',n)
if __name__=='__main__': extra()
