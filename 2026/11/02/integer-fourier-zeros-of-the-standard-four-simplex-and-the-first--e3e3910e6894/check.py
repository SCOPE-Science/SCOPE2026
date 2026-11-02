#!/usr/bin/env python3
"""Exact rational verification of integer-frequency simplex Fourier-zero rule."""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import factorial

def add(A,B,alpha=Fraction(1)):
    n=max(len(A),len(B))
    return [(A[i] if i<len(A) else 0)+alpha*(B[i] if i<len(B) else 0) for i in range(n)]

def confluent_poly(nodes):
    a=sorted(nodes)
    n=len(a)
    tab=[[None]*n for _ in range(n)]
    for i in range(n): tab[i][i]=[Fraction(1)]
    for s in range(1,n):
        for i in range(n-s):
            j=i+s
            if a[i]==a[j]:
                tab[i][j]=[Fraction(0)]*s+[Fraction(1,factorial(s))]
            else:
                tab[i][j]=[v/Fraction(a[j]-a[i]) for v in add(tab[i+1][j],tab[i][j-1],Fraction(-1))]
    return tab[0][n-1]

def classified(nodes):
    cs=Counter(nodes)
    if len(cs)==len(nodes): return True
    if len(nodes)==5 and sorted(cs.values())==[1,2,2]:
        c=next(k for k,v in cs.items() if v==1)
        a,b=(k for k,v in cs.items() if v==2)
        return 2*c==a+b
    return False

def main():
    counts={}
    for d in range(1,5):
        seen=0; zeros=0; exceptions=0
        for k in product(range(-3,4),repeat=d):
            nodes=(0,*k)
            pp=confluent_poly(nodes)
            got=all(v==0 for v in pp)
            predicted=classified(nodes)
            assert got==predicted,(d,k,pp,got,predicted)
            assert not pp or pp[0]==0 or d==0, (d,k,pp)
            seen+=1; zeros+=got
            if d==4 and got and len(set(nodes))==3: exceptions+=1
        counts[d]=(seen,zeros,exceptions)
    for d,val in counts.items():print('d',d,'tested, zeros, arithmetic exceptions =',val)
    for nodes in ([0,0,1,2,2],[0,1,1,-1,-1],[0,0,1,2,3]):
        print('nodes',nodes,'divided-difference polynomial',confluent_poly(nodes))
    print('EXACT_CHECK_PASS')
if __name__=='__main__':main()
