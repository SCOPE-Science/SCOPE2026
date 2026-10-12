#!/usr/bin/env python3
from math import comb

MAX_N = 8

def book(n):
    # 0=a, 1=b, 2+2*i=x_i, 3+2*i=y_i
    N = 2*n + 2
    adj = [set() for _ in range(N)]
    def add(u,v):
        adj[u].add(v); adj[v].add(u)
    add(0,1)
    for i in range(n):
        x,y = 2+2*i,3+2*i
        add(0,x); add(x,y); add(y,1)
    return adj

def skew_forces(adj, mask):
    N=len(adj)
    black={v for v in range(N) if (mask>>v)&1}
    while True:
        forced=None
        for u in range(N):
            whites=[v for v in adj[u] if v not in black]
            if len(whites)==1:
                forced=whites[0]
                break
        if forced is None:
            return len(black)==N
        black.add(forced)

def predicted(n, mask):
    U={1}|{2+2*i for i in range(n)}
    V={0}|{3+2*i for i in range(n)}
    return any((mask>>u)&1 for u in U) and any((mask>>v)&1 for v in V)

def polynomial_coeffs(n):
    N=2*n+2
    c=[0]*(N+1)
    for i in range(1,n+2):
        for j in range(1,n+2):
            c[i+j]+=comb(n+1,i)*comb(n+1,j)
    return c

def main():
    subset_checks=criterion_checks=coefficient_checks=minimum_checks=0
    for n in range(1,MAX_N+1):
        adj=book(n); N=len(adj)
        got=[0]*(N+1)
        min_size=N+1; min_count=0; max_failed=-1
        for mask in range(1<<N):
            subset_checks+=1
            actual=skew_forces(adj,mask)
            want=predicted(n,mask)
            criterion_checks+=1
            if actual!=want:
                raise AssertionError(('criterion',n,mask,actual,want))
            size=mask.bit_count()
            if actual:
                got[size]+=1
                if size<min_size:
                    min_size,min_count=size,1
                elif size==min_size:
                    min_count+=1
            else:
                max_failed=max(max_failed,size)
        expected=polynomial_coeffs(n)
        for k,(a,b) in enumerate(zip(got,expected)):
            coefficient_checks+=1
            if a!=b:
                raise AssertionError(('coefficient',n,k,a,b))
        minimum_checks+=3
        if min_size!=2:
            raise AssertionError(('minimum',n,min_size))
        if min_count!=(n+1)**2:
            raise AssertionError(('minimum_count',n,min_count))
        if max_failed!=n+1:
            raise AssertionError(('failed_number',n,max_failed))
    print(f'VERIFY_OK n_range=1..{MAX_N} subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order={2*MAX_N+2}')

if __name__=='__main__':
    main()
