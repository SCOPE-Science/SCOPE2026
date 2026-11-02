#!/usr/bin/env python3
"""Exact finite checks for the two-token complete-bipartite Laplacian theorem."""
from itertools import combinations
from math import comb
import sympy as sp

def direct_laplacian(m,n):
    labels = tuple(range(m+n))
    states = tuple(combinations(labels,2))
    positions = {x:i for i,x in enumerate(states)}
    M=sp.zeros(len(states))
    for pos,pair in enumerate(states):
        for occupied in pair:
            for vacant in labels:
                if vacant in pair or (occupied < m)==(vacant < m):
                    continue
                next_pair=tuple(sorted((set(pair)-{occupied})|{vacant}))
                M[pos,pos]+=1
                M[pos,positions[next_pair]]-=1
    return M

def expected(m,n,z):
    t=m+n
    return sp.expand(z*(z-t)*(z-(2*t-2))*(z-2*n)**(m*(m-3)//2)*(z-2*m)**(n*(n-3)//2)*(z-(t-2))**((m-1)*(n-1)) * ((z-n)*(z-(m+2*n-2)))**(m-1)*((z-m)*(z-(2*m+n-2)))**(n-1))

def trees(m,n):
    t=m+n
    return 4*(2*n)**(m*(m-3)//2)*(2*m)**(n*(n-3)//2)*(t-2)**((m-1)*(n-1))*(n*(m+2*n-2))**(m-1)*(m*(2*m+n-2))**(n-1)

z=sp.Symbol('z')
for m,n in [(3,3),(3,4),(3,5),(4,4),(4,5)]:
    L=direct_laplacian(m,n)
    N=comb(m+n,2)
    assert L.rows==N
    assert L==L.T and all(sum(L.row(i))==0 for i in range(N))
    observed=sp.Poly(L.charpoly(z).as_expr(),z)
    predicted=sp.Poly(expected(m,n,z),z)
    assert observed==predicted,(m,n,'characteristic polynomial mismatch')
    observed_tau=L[:N-1,:N-1].det(method='domain-ge')
    assert observed_tau==trees(m,n),(m,n,'Kirchhoff tree mismatch')
    print(f'EXACT_SPECTRUM_AND_KIRCHHOFF_OK m={m} n={n} states={N} edges={(m+n-2)*m*n} trees={observed_tau}')
print('DIRECT_EXACT_CERTIFICATE_OK')
