#!/usr/bin/env python3
"""Independently compare cycle-endomorphism idempotent counts with path-walk formula."""
from collections import Counter
from itertools import product
from math import comb

def formula(n):
    if n % 2:
        return {n: 1}
    m=n//2
    ans={n:1}
    for k in range(1,m+1):
        length=n-k
        v=[0]*(k+1)
        v[0]=1
        for _ in range(length):
            w=[0]*(k+1)
            for j,num in enumerate(v):
                if j>0:w[j-1]+=num
                if j<k:w[j+1]+=num
            v=w
        ans[k+1]=n*v[k]
    return ans

def reflection(n):
    if n%2:return {n:1}
    m=n//2
    ans={n:1}
    for k in range(1,m+1):
        L=n-k
        s=0
        for j in range(-L,L+1):
            a=m+j*(k+2)
            b=m+1+j*(k+2)
            s+=(comb(L,a) if 0<=a<=L else 0)-(comb(L,b) if 0<=b<=L else 0)
        ans[k+1]=n*s
    return ans

def enumerate_direct(n):
    # Enumerate all graph homomorphisms directly using local edge relations,
    # not path image classification or the adjacency-matrix formula.
    histogram=Counter()
    count_all=0
    for a in range(n):
        for signs in product((-1,1),repeat=n):
            data=[a]
            cur=a
            for step in signs:
                cur=(cur+step)%n
                data.append(cur)
            if cur!=a:continue
            f=tuple(data[:-1])
            count_all+=1
            if all(f[f[i]]==f[i] for i in range(n)):
                histogram[len(set(f))]+=1
    return dict(histogram), count_all

def run():
    for n in range(3,17):
        f=formula(n)
        r=reflection(n)
        b,all_count=enumerate_direct(n)
        if f!=r or f!=b:
            raise AssertionError((n,f,r,b))
        print('n=',n,'endo=',all_count,'idempotent_ranks=',sorted(f.items()),'total=',sum(f.values()))
    print('CHECKER_OK')

if __name__=='__main__':run()
