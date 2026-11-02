#!/usr/bin/env python3
"""Exact rational tests for the sorted-rate clique heat-variation criterion."""
from fractions import Fraction as F
from itertools import permutations, product

def coefficients(n, k):
    return [((n-k) if i <= k else -k)*(2*i-n-1) for i in range(1,n+1)]

def exact_sorted_maximum(rates, k):
    return sum(a*b for a,b in zip(sorted(coefficients(len(rates),k)),sorted(rates)))

def derivative_coefficient(rates, k):
    n=len(rates)
    b=[2*i-n-1 for i in range(1,n+1)]
    return (n-k)*sum(b[i]*rates[i] for i in range(k))-k*sum(b[i]*rates[i] for i in range(k,n))

def main():
    checks=0
    for n in range(2,7):
        for rates in product((1,2,4,13),repeat=n):
            if n==6 and rates[:3]!=(1,2,4):
                continue
            bounds=[exact_sorted_maximum(rates,k) for k in range(1,n)]
            for order in permutations(rates):
                for k in range(1,n):
                    assert derivative_coefficient(order,k)<=bounds[k-1]
                    checks+=1
    assert checks==741152,checks
    assert sorted(coefficients(4,1))==[-9,-3,-1,1]
    assert sorted(coefficients(4,2))==[-6,-6,-2,-2]
    assert sorted(coefficients(4,3))==[-9,-3,-1,1]
    assert [exact_sorted_maximum((1,1,1,13),k) for k in range(1,4)]==[0,-40,0]
    assert [exact_sorted_maximum((1,1,1,14),k) for k in range(1,4)]==[1,-42,1]
    rates=[F(1),F(14),F(1),F(1)]
    values=[F(0),F(1),F(101,100),F(102,100)]
    initial_derivative=sum((2*i-3)*rates[i]*(sum(values)-4*values[i]) for i in range(4))
    assert initial_derivative==F(33,100)
    print('PASS: exact sorted maxima, first threshold and strict witness;',checks,'comparisons')

if __name__=='__main__': main()
