#!/usr/bin/env python3
"""Reproduce exact one-outbreak, two-sentinel path probabilities.
No external packages are required. Run: python3 verify.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb

def formula_n_times(n,i,j,p):
    a,b,c=i,j-i,n-1-j
    return (2+sum(p**r for r in range(1,a+1))
            +sum(p**r for r in range(1,c+1))
            +sum(p**r+p**(b-r)-p**b for r in range(1,b)))

def brute_n_times(n,i,j,p):
    total=Fraction(0)
    for edge_mask in range(1 << (n-1)):
        e=edge_mask.bit_count()
        weight=p**e*(1-p)**(n-1-e)
        for source in range(n):
            # Exact connected component of the source among open path edges.
            left=right=source
            while left>0 and (edge_mask & (1 << (left-1))):left-=1
            while right<n-1 and (edge_mask & (1 << right)):right+=1
            if (left<=i<=right) or (left<=j<=right):total+=weight
    return total

def g(n,p):
    return p**(n-3)*(n-1-(n-2)*p)

def check():
    runs=0
    for n in range(2,10):
        for p in (Fraction(1,4), Fraction(1,2), Fraction(3,4)):
            values={}
            for i,j in combinations(range(n),2):
                a=formula_n_times(n,i,j,p)
                b=brute_n_times(n,i,j,p)
                assert a==b,(n,p,i,j,a,b)
                values[i,j]=a
                runs+=1
            if n>=4:
                ep=values[0,n-1]
                assert (all(ep>=v for v in values.values())) == (g(n,p)>=1),(n,p,g(n,p))
                if g(n,p)>1:
                    assert [pair for pair,v in values.items() if v==ep]==[(0,n-1)]
                if g(n,p)==1:
                    assert {pair for pair,v in values.items() if v==ep}=={(0,n-1),(0,n-2),(1,n-1)}
            else:
                assert values[0,n-1]==max(values.values())
    # Nontrivial intermediate positions and exact four-vertex crossover.
    n=4
    assert formula_n_times(n,0,3,Fraction(1,4))==Fraction(83,32)
    assert formula_n_times(n,0,2,Fraction(1,4))==Fraction(43,16)
    assert formula_n_times(n,0,3,Fraction(3,4))==Fraction(121,32)
    assert formula_n_times(n,0,2,Fraction(3,4))==Fraction(59,16)
    assert g(4,Fraction(1,2))==1
    # Exact adjacent-step exchange identity on all placements and parameters.
    for n in range(3,20):
      for p in (Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(4,5)):
       for i,j in combinations(range(n),2):
        if i>0:
         diff=formula_n_times(n,i-1,j,p)-formula_n_times(n,i,j,p)
         assert diff==p**(j-i)*(1+(j-i)*(1-p))-p**i
        if j<n-1:
         diff=formula_n_times(n,i,j+1,p)-formula_n_times(n,i,j,p)
         assert diff==p**(j-i)*(1+(j-i)*(1-p))-p**(n-1-j)
    print(f'PASS: {runs} exact percolation enumerations, all threshold comparisons, exchange identities.')

if __name__=='__main__':check()
