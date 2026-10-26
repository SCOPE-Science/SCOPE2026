#!/usr/bin/env python3
"""Exact small-size inversion validation for uniform binary-tree automorphism permutations."""
from collections import Counter
from fractions import Fraction
from math import cos, log, sqrt

checks = 0

def verify(cond, label):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(label)

def inversions(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def permutation_group(max_height=4):
    G = [tuple([0])]
    for height in range(1,max_height+1):
        m = len(G[0]); nxt=[]
        for p in G:
            for q in G:
                nxt.append(p + tuple(x+m for x in q))
                nxt.append(tuple(x+m for x in p)+q)
        G=nxt
        yield height,G

def hist_theory(n):
    h=Counter({0:1})
    for j in range(n):
        weight=4**(n-j-1)
        for _ in range(2**j):
            k=Counter()
            for inv,num in h.items():
                k[inv]+=num; k[inv+weight]+=num
            h=k
    return h

for height,G in permutation_group():
    N=2**height
    verify(len(G)==2**(2**height-1),f'group cardinality n={height}')
    verify(len(set(G))==len(G),f'group unique n={height}')
    actual=Counter(map(inversions,G))
    theory=hist_theory(height)
    verify(actual==theory,f'inversion distribution n={height}')
    verify(sum(actual.values())==len(G),f'histogram n={height}')
    verify(min(actual)==0 and max(actual)==N*(N-1)//2,f'inversion endpoints n={height}')
    verify(all(theory[k]==theory[N*(N-1)//2-k] for k in actual),f'symmetry n={height}')
    mean=sum(Fraction(k*v,len(G)) for k,v in actual.items())
    var=sum(Fraction((k-mean)**2*v,len(G)) for k,v in actual.items())
    verify(mean==Fraction(N*(N-1),4),f'expected inversions n={height}')
    verify(var==Fraction(N**4,56)*(1-Fraction(1,8**height)),f'variance n={height}')
    print(f'n={height}; N={N}; group_size={len(G)}; distinct_inversion_counts={len(actual)}; mean={mean}; variance={var}; histogram_matches=True')

# Algebraic series identities for each level, exact rational arithmetic.
for n in range(1,81):
    mean=sum(Fraction(2**j,2*4**(j+1)) for j in range(n))
    var=sum(Fraction(2**j,4*16**(j+1)) for j in range(n))
    verify(mean == Fraction(1,4)*(1-Fraction(1,2**n)),f'mean-series n={n}')
    verify(var == Fraction(1,56)*(1-Fraction(1,8**n)),f'variance-series n={n}')
    verify(sum(Fraction(2**j,4**(j+1)) for j in range(n)) + Fraction(1,2**(n+1)) ==Fraction(1,2),f'tail-coupling n={n}')
    if n <= 32:
        verify(Fraction(1,4**n) <= Fraction(1,2**(n+1)),f'tail-support n={n}')

# Characteristic-function modulus bound: no approximation is offered as proof.
q=cos(0.5); c=-log(q)/4
for t in [4.,5.,7.,12.,16.,30.,50.,99.,1000.,10000.,100000.]:
    m=0
    while 4**(m+1)<=t: m+=1
    j=m-1
    verify(j>=0,f'fourier level {t}')
    arg=t/(2*4**(j+1))
    verify(0.5<=arg<2,f'fourier argument {t}')
    verify(abs(cos(arg))<=q+1e-14,f'fourier factor {t}')
    verify(2**j>sqrt(t)/4-1e-12,f'fourier root scale {t}')
    # Check the selected factor on log scale, avoiding numerical underflow.
    verify(2**j*log(max(abs(cos(arg)),1e-300)) <= -c*sqrt(t)+1e-11, f'fourier bound {t}')

print(f'PASS: {checks} exact-combinatorial / rational-series assertions and numerical Fourier diagnostics.')
