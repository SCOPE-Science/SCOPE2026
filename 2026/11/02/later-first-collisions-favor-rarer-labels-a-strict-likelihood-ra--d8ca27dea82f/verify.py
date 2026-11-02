#!/usr/bin/env python3
"""Exact rational checks for first-duplicate label/time likelihood-ratio law.

Only standard-library Python is required. Finite checks support (but do not replace)
the analytic all-size proof.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import permutations
from math import factorial

COUNT=0

def check(condition, message):
    global COUNT
    COUNT+=1
    if not condition:
        raise AssertionError(message)

def sym(values, k):
    if k<0 or k>len(values):
        return F(0)
    a=[F(1)]+[F(0)]*k
    for v in values:
        for j in range(k,0,-1):
            a[j]+=v*a[j-1]
    return a[k]

def closed_joint(p):
    m=len(p)
    return {(t,i):factorial(t-1)*p[i]*p[i]*sym([p[j] for j in range(m) if j!=i],t-2)
            for t in range(2,m+2) for i in range(m)}

def independently_enumerated_joint(p):
    m=len(p)
    out=defaultdict(F)
    # Each prefix of distinct draws plus a final draw repeating one prefix type.
    # Distinct ordered prefixes are independently enumerated, no symmetric polynomials used.
    for distinct_count in range(1,m+1):
        for prefix in permutations(range(m),distinct_count):
            prior=F(1)
            for index in prefix:
                prior*=p[index]
            for index in prefix:
                out[(distinct_count+1,index)]+=prior*p[index]
    return out

def run():
    samples=0
    for m in range(2,7):
        vectors=[list(range(1,m+1)),[1]*m,[m]+[1]*(m-1),[1]+[2]*(m-1),list(range(m,0,-1))]
        for integer_weights in vectors:
            p=tuple(F(v,sum(integer_weights)) for v in integer_weights)
            C=closed_joint(p)
            E=independently_enumerated_joint(p)
            check(sum(C.values())==1,(m,p,'normalization'))
            for t in range(2,m+2):
                check(sum(C[t,i] for i in range(m))>0,(m,t,'positive time'))
                for i in range(m):
                    check(C[t,i]==E[t,i],(m,p,t,i,'independent enumeration'))
            for i in range(m):
                check(C[2,i]/sum(C[2,j] for j in range(m))==p[i]**2/sum(x*x for x in p),(m,i,'early endpoint'))
                check(C[m+1,i]/sum(C[m+1,j] for j in range(m))==p[i],(m,i,'late endpoint'))
            for i in range(m):
                for j in range(m):
                    if p[i]>p[j]:
                        for t in range(2,m+1):
                            check(C[t,i]*C[t+1,j]>C[t+1,i]*C[t,j],(m,p,i,j,t,'strict odds'))
                    elif p[i]==p[j]:
                        for t in range(2,m+1):
                            check(C[t,i]*C[t+1,j]==C[t+1,i]*C[t,j],(m,p,i,j,t,'tie odds'))
            # Conditional expected probability of collision label is strictly decreasing
            conditional_means=[]
            for t in range(2,m+2):
                wt=sum(C[t,i] for i in range(m))
                conditional_means.append(sum(p[i]*C[t,i] for i in range(m))/wt)
            for u,v in zip(conditional_means,conditional_means[1:]):
                check((u>v) if len(set(p))>1 else (u==v),(m,p,'conditional mean'))
            times={t:sum(C[t,i] for i in range(m)) for t in range(2,m+2)}
            et=sum(t*times[t] for t in times)
            ej=sum(p[i]*C[t,i] for t in times for i in range(m))
            etj=sum(t*p[i]*C[t,i] for t in times for i in range(m))
            check((etj<et*ej) if len(set(p))>1 else (etj==et*ej),(m,p,'covariance'))
            samples+=1
    print(f'PASS: {COUNT:,} exact rational assertions across {samples} probability vectors, with independent prefix enumeration.')

if __name__=='__main__':
    run()
