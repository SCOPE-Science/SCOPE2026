#!/usr/bin/env python3
"""Exact finite enumerations for the conditional moments and score-projection law."""
from itertools import combinations
from collections import defaultdict
from fractions import Fraction
from math import comb

def choose3(m):
    return comb(m,3) if m>=3 else 0

checks=0
for n in range(3,7):
    edges=list(combinations(range(n),2))
    patterns=1<<len(edges)
    stats=defaultdict(lambda:[0,0,0])
    frequency=defaultdict(lambda:[0,0])
    sum_cycles=0
    for mask in range(patterns):
        scores=[0]*n
        beats=[[False]*n for _ in range(n)]
        for bit,(u,v) in enumerate(edges):
            if mask & (1<<bit):
                beats[u][v]=True
                scores[u]+=1
            else:
                beats[v][u]=True
                scores[v]+=1
        cycles=sum(int((beats[u][v] and beats[v][w] and beats[w][u]) or
                       (beats[u][w] and beats[w][v] and beats[v][u]))
                   for u,v,w in combinations(range(n),3))
        record=stats[scores[0]]
        record[0]+=1
        record[1]+=cycles
        record[2]+=cycles*cycles
        sum_cycles+=cycles
        for k in range(n):
            observed=sum(s==k for s in scores)
            frequency[k][0]+=observed
            frequency[k][1]+=cycles*observed
    for k in range(n):
        count, summ, sq=stats[k]
        mean=Fraction(summ,count)
        variance=Fraction(sq,count)-mean*mean
        wanted_mean=Fraction(choose3(n-1),4)+Fraction(k*(n-1-k),2)
        wanted_variance=Fraction(3*choose3(n-1),16)+Fraction(k*(n-1-k),4)
        assert mean==wanted_mean,(n,k,'mean',mean,wanted_mean)
        assert variance==wanted_variance,(n,k,'variance',variance,wanted_variance)
        obs_sum,prod_sum=frequency[k]
        covariance=Fraction(prod_sum,patterns)-Fraction(sum_cycles*obs_sum,patterns*patterns)
        pk=Fraction(comb(n-1,k),2**(n-1))
        wanted=-Fraction(n,8)*pk*((2*k-(n-1))**2-(n-1))
        assert covariance==wanted,(n,k,'covariance',covariance,wanted)
        checks+=3
    print(f'n={n}: exhausted {patterns} tournaments; {3*n} rational identities checked')
print(f'PASS: {checks} exact rational identities across n=3,4,5,6')
