#!/usr/bin/env python3
"""Check finite-prism two-facilitator blocked-state formula independently.
Science-only reproducibility; no external dependencies.
"""
from collections import Counter
from itertools import combinations
from math import comb

def prism_neighbors(n):
    assert n >= 3
    return [set((r*n+(i-1)%n, r*n+(i+1)%n, (1-r)*n+i))
            for r in (0,1) for i in range(n)]

def full_census(n):
    adj=prism_neighbors(n)
    N=2*n; counts=[0]*(N+1)
    for bits in range(1<<N):
        # A spin flip is allowed at vertex v iff >=2 facilitators are its neighbors.
        if all(sum((bits>>u)&1 for u in adj[v]) <= 1 for v in range(N)):
            counts[bits.bit_count()] += 1
    return counts

def cycle_square_independence_poly(m):
    counts=[0]*(m+1)
    for bits in range(1<<m):
        if all(not ((bits>>i)&1 and ((bits>>((i+d)%m))&1))
               for i in range(m) for d in (1,2)):
            counts[bits.bit_count()] += 1
    return counts

def formula_I(m):
    x=[0]*(m+1);x[0]=1
    for k in range(1,m//3+1):
        assert m*comb(m-2*k,k)%(m-2*k)==0
        x[k]=m*comb(m-2*k,k)//(m-2*k)
    return x

def poly_mult(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def main():
    for n in range(3,10):
        coeff=formula_I(2*n) if n%2 else poly_mult(formula_I(n),formula_I(n))
        brute=full_census(n)
        assert coeff[:len(brute)]==brute, (n, coeff, brute)
        print(f'n={n} polynomial_coeffs={list(x for x in coeff if x)} total={sum(coeff)} largest={max(i for i,c in enumerate(coeff) if c)}')
    for m in range(3,14):
        assert cycle_square_independence_poly(m)==formula_I(m),m
    print('PASS: all direct FA constraints, all independent-set enumeration, all formula coefficients')
if __name__=='__main__': main()

# The second independent check uses the actual common-neighbor conflict graph.
# Its cyclic components are read off from alternating-rail diagonals.
def test_conflict_graph(n):
    adj=prism_neighbors(n)
    conflicts={frozenset((u,v)) for u in range(2*n) for v in range(u+1,2*n)
               if adj[u] & adj[v]}
    visited=set(); predicted=set()
    for start in range(2*n):
        if start in visited: continue
        seq=[]; u=start
        while u not in seq:
            seq.append(u);visited.add(u)
            rail,i=divmod(u,n)
            u=(1-rail)*n+(i+1)%n
        assert u==start
        m=len(seq)
        assert m==(2*n if n%2 else n)
        for j in range(m):
            for delta in (1,2):
                predicted.add(frozenset((seq[j],seq[(j+delta)%m])))
    assert conflicts==predicted,(n,len(conflicts),len(predicted),conflicts^predicted)
    return len(visited),len(conflicts)

if __name__=='__main__':
    for n in range(3,51):
        v,e=test_conflict_graph(n)
        assert v==2*n
    print('PASS: exact common-neighbor conflict graph equals cyclic-square components for n=3,...,50')
