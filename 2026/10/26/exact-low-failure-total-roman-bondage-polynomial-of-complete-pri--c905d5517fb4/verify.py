#!/usr/bin/env python3
"""Standalone finite checks of low-deletion total-Roman bondage on clique prisms.
This program does not use the formulas to determine the independently enumerated graph outcomes.
"""
from itertools import combinations, product
from math import comb, factorial

def edges(n):
    E=[]
    for layer in range(2):
        for i in range(n):
            for j in range(i+1,n):
                E.append((layer*n+i,layer*n+j))
    E += [(i,n+i) for i in range(n)]
    return E

def min_trdf(n,retained):
    N=2*n
    neighbor=[0]*N
    for a,b in retained:
        neighbor[a]|=1<<b; neighbor[b]|=1<<a
    if not all(neighbor):return None
    best=N+1
    for f in product((0,1,2),repeat=N):
        w=sum(f)
        if w>=best:continue
        support=sum(1<<v for v in range(N) if f[v])
        two=sum(1<<v for v in range(N) if f[v]==2)
        if all((neighbor[v] & two) if f[v]==0 else (neighbor[v] & support) for v in range(N)):
            best=w
    return best

def dom_edge(n,retained):
    closed=[1<<v for v in range(2*n)]
    for a,b in retained:
        closed[a]|=1<<b;closed[b]|=1<<a
    allones=(1<<(2*n))-1
    return any((closed[a]|closed[b])==allones for a,b in retained)

def destruction_ie(n,k):
    return sum((-1)**j*comb(n,j)*comb((n-j)**2,k) if (n-j)**2>=k else 0
               for j in range(n+1))

def min_number(n):
    if n%2==0:
        r=n//2
        return factorial(n)//factorial(r)
    r=(n-1)//2
    loop=n*factorial(2*r)//factorial(r)
    p3=comb(n,3)*3*2**(r+1)*factorial(2*r-2)//(2**(r-1)*factorial(r-1))
    return loop+p3

def run():
    checked=0
    for n in range(3,7):
        E=edges(n)
        counts=[]
        for k in range(n):
            c=0
            for deleted in combinations(E,k):
                bits=0
                for a,b in deleted:
                    bits|=(1<<(a%n))|(1<<(b%n))
                c+=bits == (1<<n)-1
                checked+=1
            assert c==destruction_ie(n,k),(n,k,c,destruction_ie(n,k))
            counts.append(c)
        b=(n+1)//2
        assert all(not a for a in counts[:b])
        assert counts[b]==min_number(n),(n,counts[b],min_number(n))
        print(f'IE n={n} all_k_below_degree={counts} min_count={counts[b]}')
    # Check actual graph domination, rather than only indexing, independently.
    graph_checked=0
    for n in (3,4):
        E=edges(n)
        assert min_trdf(n,E)==4
        for k in range(n):
            for removed in combinations(E,k):
                present=set(E)-set(removed)
                direct=min_trdf(n,present)
                predicate=dom_edge(n,present)
                assert (direct==4)==predicate,(n,removed,direct,predicate)
                assert (direct>4)==(destruction_predicate(n,removed)),(n,removed,direct)
                graph_checked+=1
        print(f'TRDF exhaustive n={n} tested up to k={n-1}')
    print(f'VERIFY_OK edge_subsets={checked} independent_trdf_instances={graph_checked}')

def destruction_predicate(n,removed):
    hit={v%n for e in removed for v in e}
    return len(hit)==n

if __name__=='__main__':run()
