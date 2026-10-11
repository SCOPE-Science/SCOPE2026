#!/usr/bin/env python3
import sympy as sp
from itertools import combinations

sqrt = sp.sqrt

def closure(n, edges):
    R=[[False]*n for _ in range(n)]
    for i in range(n):
        R[i][i]=True
    for i,j in edges:
        R[i][j]=True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j]=True
    return tuple(tuple(row) for row in R)

def comparable(R,i,j):
    return R[i][j] or R[j][i]

def chains(R):
    n=len(R)
    out=[]
    for mask in range(1,1<<n):
        C=[i for i in range(n) if (mask>>i)&1]
        if all(comparable(R,i,j) for i,j in combinations(C,2)):
            out.append(tuple(C))
    return out

def maximal_chains(R):
    allc=chains(R)
    aset=[set(c) for c in allc]
    out=[]
    for i,c in enumerate(aset):
        if not any(c<d for d in aset):
            out.append(tuple(sorted(c)))
    return sorted(set(out))

seen=set()
posets=0
nonunique=0
for n in range(1,6):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for mask in range(1<<len(pairs)):
        edges=[pairs[t] for t in range(len(pairs)) if (mask>>t)&1]
        R=closure(n,edges)
        if R in seen:
            continue
        seen.add(R)
        MC=maximal_chains(R)
        h=max(len(C) for C in MC)
        r=1/(sp.Integer(h)+sqrt(h))

        # Candidate center has coordinate-facet clearance r.
        # Verify every maximal-chain normalized clearance is >= r.
        for C in MC:
            k=len(C)
            dist=sp.simplify((1-k*r)/sqrt(k))
            assert sp.simplify(dist-r)>=0

        longest=[set(C) for C in MC if len(C)==h]
        covered=set().union(*longest)
        unique=(len(covered)==n)

        if unique:
            assert all(any(i in C for C in longest) for i in range(n))
        else:
            nonunique += 1
            q=next(i for i in range(n) if i not in covered)
            slacks=[]
            for C in MC:
                if q in C:
                    k=len(C)
                    slack=sp.simplify(1-r*(k+sqrt(k)))
                    assert slack>0
                    slacks.append(slack)
            eps=min(slacks)/2
            # Increasing x_q by eps preserves every radius-r chain clearance.
            for C in MC:
                k=len(C)
                extra=eps if q in C else 0
                lhs=sp.simplify(k*r+extra+r*sqrt(k))
                assert lhs<=1

        posets+=1

print(f"VERIFY_OK chain-polytope-inradius posets={posets} nonunique={nonunique} n<=5 exact=yes")
