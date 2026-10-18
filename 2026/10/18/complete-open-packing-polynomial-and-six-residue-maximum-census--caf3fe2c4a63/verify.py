#!/usr/bin/env python3
"""Independent small-instance checks for open packings in circular ladders.

Run with Python 3.9+; uses only the standard library.
"""
from collections import defaultdict
from math import comb


def prism_neighborhoods(n):
    adj = [set() for _ in range(2*n)]
    def add(u,v):
        adj[u].add(v)
        adj[v].add(u)
    for i in range(n):
        add(i,(i+1)%n)
        add(n+i,n+(i+1)%n)
        add(i,n+i)
    return adj


def conflict_edges(adj):
    return {frozenset((i,j)) for i in range(len(adj))
            for j in range(i+1,len(adj)) if adj[i].intersection(adj[j])}


def cyclic_orders(n):
    g = 2 if n%2 == 0 else 1
    orders = []
    for eps in range(g):
        order=[]
        for j in range(n//g):
            order.extend([(eps+2*j)%n, n+(eps+2*j+1)%n])
        orders.append(order)
    return orders


def formula(n):
    def one(length):
        out = [0]*(length+1)
        for s in range(length//3+1):
            out[s] = 1 if s==0 else length*comb(length-2*s,s)//(length-2*s)
        return out
    if n%2: return one(2*n)
    a = one(n)
    return [sum(a[j]*a[k-j] for j in range(max(0,k-n),min(k,n)+1))
            for k in range(2*n+1)]


def direct_count(n):
    N = prism_neighborhoods(n)
    adjacency = [sum(1 << j for j in neighbors) for neighbors in N]
    hist=[0]*(2*n+1)
    for mask in range(1<<(2*n)):
        if all((mask & adjacency[v]).bit_count() <= 1 for v in range(2*n)):
            hist[mask.bit_count()]+=1
    return hist


def transfer_count(n):
    # Derive a second enumerator from cyclic two-bit columns, without
    # using the closed formula or the cycle-square isomorphism.
    def allowed(a,b,c):
        return ((a&c)==0 and (not((b&1) and (c&2)))
                and (not((b&2) and (c&1))))
    hist=[0]*(2*n+1)
    for a in range(4):
        for b in range(4):
            D={(a,b):{a.bit_count()+b.bit_count():1}}
            for _ in range(2,n):
                E=defaultdict(lambda:defaultdict(int))
                for (u,v),weights in D.items():
                    for w in range(4):
                        if allowed(u,v,w):
                            for size,count in weights.items():
                                E[(v,w)][size+w.bit_count()]+=count
                D=E
            for (u,v),weights in D.items():
                if allowed(u,v,a) and allowed(v,a,b):
                    for size,count in weights.items():
                        hist[size]+=count
    return hist


def predicted_maximum(n):
    residue=n%6
    count={0:9,1:n*(2*n+1)//3,2:(n*(n+1)//6)**2,
           3:3,4:n*n,5:2*n}[residue]
    size = 2*(n//3) if n%2==0 else (2*n)//3
    return size,count


def main():
    tested=0
    for n in range(3,11):
        direct=direct_count(n)
        algebra=formula(n)
        assert direct==algebra,(n,'direct-vs-formula',direct,algebra)
        assert direct==transfer_count(n),(n,'direct-vs-transfer')
        tested+=1<<(2*n)
    for n in range(3,41):
        adj=prism_neighborhoods(n)
        actual=conflict_edges(adj)
        orders=cyclic_orders(n)
        assert sorted(u for order in orders for u in order)==list(range(2*n))
        predicted={frozenset((order[i],order[(i+d)%len(order)]))
                   for order in orders for i in range(len(order)) for d in (1,2)}
        assert actual==predicted,(n,'structural graph-isomorphism')
        f=formula(n)
        assert f==transfer_count(n),(n,'transfer-vs-formula')
        best=max(i for i,v in enumerate(f) if v)
        assert (best,f[best])==predicted_maximum(n),(n,'maximum census')
    for n in range(41,151):
        f=formula(n)
        best=max(i for i,v in enumerate(f) if v)
        assert (best,f[best])==predicted_maximum(n)
    print('PASS: direct graph-predicate exhaustive comparisons, n=3..10')
    print('PASS: %d labelled vertex subsets checked' % tested)
    print('PASS: explicit conflict graph equals cycle-square decomposition, n=3..40')
    print('PASS: independent cyclic-column transfer polynomials agree, n=3..40')
    print('PASS: six-residue maximum size and multiplicity formulas, n=3..150')
    print('PASS: all checks complete')

if __name__=='__main__':
    main()
