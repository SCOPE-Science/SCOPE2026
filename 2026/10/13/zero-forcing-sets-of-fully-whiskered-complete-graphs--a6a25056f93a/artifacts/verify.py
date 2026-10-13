#!/usr/bin/env python3
from itertools import combinations
from math import comb

def graph(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(i+1,n):
            adj[i].add(j); adj[j].add(i)
        adj[i].add(n+i); adj[n+i].add(i)
    return adj

def zero_forces(n, mask):
    adj=graph(n); N=2*n
    black={v for v in range(N) if (mask>>v)&1}
    while True:
        move=None
        for u in tuple(black):
            white=[v for v in adj[u] if v not in black]
            if len(white)==1:
                move=white[0]; break
        if move is None: break
        black.add(move)
    return len(black)==N

def criterion(n, mask):
    empty=0; has_leaf=False
    for i in range(n):
        c=(mask>>i)&1; l=(mask>>(n+i))&1
        if not c and not l: empty+=1
        if l: has_leaf=True
    return empty==0 or (empty==1 and has_leaf)

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def poly_pow(base,n):
    a=[1]
    for _ in range(n): a=poly_mul(a,base)
    return a

def expected_poly(n):
    # (2x+x^2)^n + n*((2x+x^2)^(n-1)-x^(n-1))
    p=poly_pow([0,2,1],n)
    q=poly_pow([0,2,1],n-1)
    if len(p)<2*n+1:p += [0]*(2*n+1-len(p))
    for k,v in enumerate(q): p[k]+=n*v
    p[n-1]-=n
    return p

def main():
    subset_checks=criterion_checks=coefficient_checks=minimum_checks=0
    for n in range(2,9):
        N=2*n; counts=[0]*(N+1)
        for mask in range(1<<N):
            z=zero_forces(n,mask); c=criterion(n,mask)
            subset_checks+=1; criterion_checks+=1
            if z!=c:
                raise AssertionError((n,mask,z,c))
            if z: counts[mask.bit_count()]+=1
        exp=expected_poly(n)
        if counts!=exp:
            raise AssertionError((n,counts,exp))
        coefficient_checks += N+1
        zmin=next(i for i,x in enumerate(counts) if x)
        if zmin!=n-1: raise AssertionError((n,zmin))
        if counts[zmin] != n*((1<<(n-1))-1):
            raise AssertionError((n,counts[zmin]))
        total=sum(counts)
        if total != (n+3)*(3**(n-1))-n:
            raise AssertionError((n,total))
        minimum_checks += 3
    print(f"VERIFY_OK n_range=2..8 subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=16")

if __name__=='__main__': main()
