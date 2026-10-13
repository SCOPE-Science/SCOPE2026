#!/usr/bin/env python3
"""Exact-rational check of Cesaro quantum mixing on products of cliques."""
from fractions import Fraction
from itertools import product
from functools import reduce
from math import prod,comb
import sympy as sp

def kron(matrices):
    return reduce(sp.kronecker_product, matrices)

def laurent_coefficient(ns):
    weights={0:1}
    for n in ns:
        new={}
        for e, c in weights.items():
            for j, scale in ((0,n-2),(n,1),(-n,1)):
                new[e+j]=new.get(e+j,0)+scale*c
        weights=new
    return sp.Rational(weights.get(0,0),prod(ns))

def sectors(dims):
    P=[]
    for n in dims:
        J=sp.ones(n)/n
        P.append((J,sp.eye(n)-J))
    return P

def construct(dims):
    p=sectors(dims); M=sp.zeros(prod(dims)); predicted=sp.zeros(prod(dims)); spectral={}
    for bits in product((0,1),repeat=len(dims)):
        PP=kron([p[i][bits[i]] for i in range(len(dims))]); lam=laurent_coefficient([dims[i] for i in range(len(dims)) if bits[i]])
        predicted+=lam*PP
        eig=sum(dims[i]-1 if bits[i]==0 else -1 for i in range(len(dims)))
        if eig in spectral:spectral[eig]+=PP
        else:spectral[eig]=PP
    for E in spectral.values():M+=E.multiply_elementwise(E)
    assert M==predicted,(dims,'matrix mismatch')
    N=prod(dims)
    rank = sum(prod(dims[i]-1 for i in range(len(dims)) if bits[i]) for bits in product((0,1),repeat=len(dims)) if laurent_coefficient([dims[i] for i in range(len(dims)) if bits[i]])>0)
    assert M*sp.ones(N,1)==sp.ones(N,1)
    assert (M-M.T)==sp.zeros(N)
    return N,rank

def special_formula(m,n):
    a=2*m*n
    expected=m*n+((m-1)*(n-1) if abs(m-n)==2 else 0)
    N,r=construct((2,m,n))
    assert N==a and r==expected,(m,n,r,expected)
    return N,r

def main():
    profiles=[(2,),(3,),(2,2),(2,3),(2,3,3),(2,3,4),(2,3,5),(2,4,6),(2,2,3),(3,3,3),(2,2,2,3),(3,4,5)]
    entries=0
    for dims in profiles:
        N,rank=construct(dims)
        entries+=N*N
    special=[]
    for m,n in [(3,3),(3,4),(3,5),(4,6)]:
        special.append((m,n,*special_formula(m,n)))
    print('VERIFY_OK exact_profiles=%d exact_entries=%d special=%s'%(len(profiles),entries,special))

if __name__=='__main__':main()
