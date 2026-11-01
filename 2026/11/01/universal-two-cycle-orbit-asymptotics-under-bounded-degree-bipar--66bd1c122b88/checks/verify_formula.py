#!/usr/bin/env python3
"""Exact two-cycle counts under synchronous parallel chip-firing on dense bipartite graphs."""
from itertools import product
from math import factorial, comb, exp, sqrt, pi

def neighbors(n, deleted):
    return [tuple(n+j for j in range(n) if (i,j) not in deleted) for i in range(n)]+[tuple(i for i in range(n) if (i,j) not in deleted) for j in range(n)]

def count_by_firing(n, deleted):
    nb=neighbors(n, deleted)
    ans=0
    for f in product((0,1),repeat=2*n):
        prod=1
        for v,adj in enumerate(nb):
            prod*=sum(f[w]!=f[v] for w in adj)
        ans+=prod
    assert ans%2==0
    return ans//2

def crown_multinomial(n):
    res=0
    fac=[factorial(i) for i in range(n+1)]
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                i=c+d; j=b+d
                weight=(i*j)**a * ((j-1)*(n-i-1))**b * ((n-j-1)*(i-1))**c * ((n-j)*(n-i))**d
                res+=fac[n]//(fac[a]*fac[b]*fac[c]*fac[d])*weight
    assert res%2==0
    return res//2

def complete_biclique(n):
    total=0
    for i in range(n+1):
        for j in range(n+1):
            total+=comb(n,i)*comb(n,j)*j**(n-i)*(n-j)**i*i**(n-j)*(n-i)**j
    assert total%2==0
    return total//2

if __name__=='__main__':
    for n in range(2,7):
        full=count_by_firing(n,set()) if n<=5 else None
        exact=complete_biclique(n)
        if full is not None: assert exact==full
        if n>=3:
            crown=count_by_firing(n,{(k,k) for k in range(n)}) if n<=5 else None
            from_poly=crown_multinomial(n)
            if crown is not None: assert from_poly==crown
            print('n',n,'K-count',exact,'crown-count',from_poly)
        else: print('n',n,'K-count',exact)
    for n in [10,20,40,80]:
        ck=complete_biclique(n)
        cr=crown_multinomial(n)
        normalized=float(cr/ck)
        normalized2=float(cr/(sqrt(pi*n)/4*(n-1)**(2*n)))
        print('asymptotics n',n,'crown/K',normalized,'target',exp(-2),'degree-normalized factor',normalized2)
    print('PASS exact formula and crown asymptotic diagnostic')
