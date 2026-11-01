#!/usr/bin/env python3
"""Exhaustive finite-field checks of line-centered furtherness order-complex barcodes.

Uses explicit prime-field subspaces and direct simplicial boundary reduction.
No topological barcode library or assumed homology theorem is used.
"""
from itertools import product
from collections import Counter
from math import prod


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    numerator = prod(q**(n-i)-1 for i in range(k))
    denominator = prod(q**(i+1)-1 for i in range(k))
    return numerator // denominator


def subspaces(q, n):
    """Enumerate spans by repeatedly adjoining one vector; q must be prime."""
    zero = (0,)*n
    vectors = list(product(range(q), repeat=n))
    found = {frozenset([zero])}
    frontier = [frozenset([zero])]
    while frontier:
        space = frontier.pop()
        for v in vectors:
            if v in space: continue
            enlarged = frozenset(tuple((u[i]+a*v[i]) % q for i in range(n))
                                  for u in space for a in range(q))
            if enlarged not in found:
                found.add(enlarged)
                frontier.append(enlarged)
    return sorted(found, key=lambda x:(len(x),sorted(x)))


def barcode(q,n,p):
    spaces = subspaces(q,n)
    rank=lambda x: next(k for k in range(n+1) if q**k==len(x))
    counts=Counter(map(rank,spaces))
    assert counts == Counter({k:gaussian(n,k,q) for k in range(n+1)})
    B=[sum(gaussian(k,i,q) for i in range(k+1)) for k in range(n+1)]
    L=frozenset((a,)+(0,)*(n-1) for a in range(q)) # first coordinate line
    spaces=[U for U in spaces if len(U)>1]
    weights=[B[rank(U)]-B[rank(U.intersection(L))] for U in spaces]
    # Comparable subspaces have monotone furtherness; independently verify.
    bigger=[[] for _ in spaces]
    for i,U in enumerate(spaces):
        for j,V in enumerate(spaces):
            if U < V:
                assert weights[i] <= weights[j]
                bigger[i].append(j)
    # all strictly increasing chains; no face-size or dimension truncation.
    chains=[]
    def add(c, tail):
        chains.append(tuple(c))
        for j in bigger[tail]: add(c+[j],j)
    for i in range(len(spaces)): add([i],i)
    # Filtration is the maximum vertex value, not the sum of vertex weights.
    chains.sort(key=lambda c:(max(weights[j] for j in c),len(c),c))
    index={c:i for i,c in enumerate(chains)}
    times=[max(weights[j] for j in c) for c in chains]
    # True boundary-matrix persistent reduction over F_p.
    pivots={}
    paired=set()
    zero_columns=set()
    intervals=[]
    for j,c in enumerate(chains):
        if len(c)==1:
            col={}
        else:
            col={index[c[:r]+c[r+1:]]:(-1 if r%2 else 1)%p for r in range(len(c))}
        while col:
            pivot=max(col)
            if pivot not in pivots: break
            other=pivots[pivot]
            scale=col[pivot]*pow(other[pivot],-1,p)%p
            for i,v in other.items():
                new=(col.get(i,0)-scale*v)%p
                if new:col[i]=new
                elif i in col:del col[i]
        if col:
            lo=max(col)
            assert lo not in paired
            pivots[lo]=col
            paired.add(lo)
            if times[lo]<times[j]:
                intervals.append((len(chains[lo])-1,times[lo],times[j]))
        else:
            zero_columns.add(j)
    # Essential classes are zero reduced columns not later killed.
    essential=Counter((len(chains[i])-1,times[i]) for i in zero_columns-paired)
    assert essential == Counter({(0,0):1}), (q,n,p,essential)
    expected=Counter({(0,0,None):1})
    for k in range(1,n):
        expected[(k-1,B[k]-1,B[k+1]-2)]=q**(k*(k+1)//2)*gaussian(n-1,k,q)
    observed=Counter(intervals)
    assert observed == Counter({key:val for key,val in expected.items() if key[2] is not None}), (q,n,p,observed,expected)
    stages=sorted(set([0]+times))
    # The top subspace is the last enumerated subspace, and occurs in a chain.
    assert any(c[-1]==len(spaces)-1 for c in chains)
    return len(spaces),len(chains),len(intervals),len(stages),B,dict(observed)


def main():
    cases=[(2,2),(2,3),(2,4),(3,2),(3,3)]
    total=0
    for q,n in cases:
        checks=[]
        for p in (2,3,5):
            result=barcode(q,n,p)
            checks.append(result)
            total+=1
        assert checks[0] == checks[1] == checks[2]
        num,chains,bars,stages,B,intervals=checks[0]
        print(f'CASE q={q} n={n} subspaces={num} chains={chains} bars={bars} levels={stages} gaussian_B={B} intervals={intervals}')
    print(f'VERIFY_OK cases={len(cases)} field_reductions={total}')

if __name__=='__main__': main()
