#!/usr/bin/env python3
"""Independent finite checks for size and maximality counts in triangular graphs."""
from math import comb, factorial
from itertools import combinations
from collections import Counter
import random


def add_product(out, sub, multiplicity, increment):
    for deg, num in sub.items():
        out[deg + increment] += multiplicity * num


def assemblies(nmax, maximal=False):
    p = [Counter({0: 1})]
    for n in range(1, nmax+1):
        curr=Counter()
        for k in range(1,n+1):
            mult=comb(n-1,k-1)
            if not maximal and k==1:
                add_product(curr,p[n-k],mult,0)
            if k==2:
                add_product(curr,p[n-k],mult,1)
            if k==3:
                if not maximal:
                    add_product(curr,p[n-k],3*mult,2)
                add_product(curr,p[n-k],mult,3)
            if k>=4:
                add_product(curr,p[n-k],k*mult,k-1)
        p.append(curr)
    if maximal:
        for n in range(1,nmax+1):
            if n%3==1:
                q=(n-1)//3
                p[n][3*q] += factorial(n)//(6**q*factorial(q))
    return p


def brute(n):
    edges=list(combinations(range(n),2))
    m=len(edges)
    adjacency=lambda i,j: bool(set(edges[i])&set(edges[j]))
    forbidden=[]
    for a,b,c in combinations(range(m),3):
        if adjacency(a,b)+adjacency(a,c)+adjacency(b,c)==2:
            forbidden.append((1<<a)|(1<<b)|(1<<c))
    valid=bytearray(1<<m)
    gc=Counter()
    for mask in range(1<<m):
        if not any(mask&bad==bad for bad in forbidden):
            valid[mask]=1
            gc[mask.bit_count()]+=1
    mc=Counter()
    for mask in range(1<<m):
        if valid[mask] and all(not valid[mask|(1<<i)] for i in range(m) if not mask&(1<<i)):
            mc[mask.bit_count()]+=1
    return gc,mc,len(forbidden),sum(valid)


def check():
    all_poly=assemblies(6)
    max_poly=assemblies(6,True)
    num=0
    for n in range(2,7):
        a,b,bad,gp=brute(n)
        assert a==all_poly[n], ('all',n,a,all_poly[n])
        assert b==max_poly[n], ('maximal',n,b,max_poly[n])
        num+=gp
        print('board',n,'graph_vertices',comb(n,2),'GP_sets',gp,'maximal',sum(b.values()),'range',min(b),max(b))
    assert all_poly[0]==Counter({0:1}) and max_poly[0]==Counter({0:1})
    assert all_poly[1]==Counter({0:1}) and max_poly[1]==Counter({0:1})
    assert max_poly[4]==Counter({2:3,3:8})
    assert max_poly[6]==Counter({3:15,4:60,5:6,6:10})
    assert max_poly[5]==Counter({4:15})
    # Explicit known extremal GP values and the proven lower-GP cardinality.
    for n in range(3,50):
        p=assemblies(n,True)[n]
        top=n if n%3==0 else n-1
        bottom=(n//2 if n%2==0 else (n+3)//2)
        assert max(p)==top and min(p)==bottom,(n,p,bottom,top)
    print('VERIFY_OK n=2..6 all induced subsets exhaustive, GP_sets_total=',num,'extremal_order_checks=3..49')

if __name__=='__main__':
    check()
