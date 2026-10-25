#!/usr/bin/env python3
"""Standalone integer verification of finite skyscraper cases and asymptotic diagnostics."""
import itertools
import math

OEIS_A218531 = [1,1,2,6,22,105,675,4872,40614,403704,4342080,50457000,631548456,8484089328,121882518576,1865935562400,30341974222944,522466493255424,9499883854364928,181927524046316544,3713847873452280000,80378118226450517760,1816649795206970760960,42807228653571471429120]

def stirling_row(n):
    row=[1]
    for j in range(n-1):
        nxt=[0]*(len(row)+1)
        for t,v in enumerate(row):
            nxt[t]+=j*v
            nxt[t+1]+=v
        row=nxt
    return row

def count_pairs_from_row(n):
    sr=stirling_row(n)
    f={}
    for t,c in enumerate(sr):
        if not c:
            continue
        for k in range(t+1):
            f[(k+1,t-k+1)]=c*math.comb(t,k)
    assert sum(f.values())==math.factorial(n)
    return f

def brute(n):
    d={}
    for perm in itertools.permutations(range(1,n+1)):
        hi=0; l=0
        for v in perm:
            if v>hi:
                hi=v; l+=1
        hi=0; r=0
        for v in perm[::-1]:
            if v>hi:
                hi=v; r+=1
        d[l,r]=d.get((l,r),0)+1
    return d

def diagnostic(n, cap=128):
    # Distribution of the total extra visibility count is an Ewens(2)
    # cycle count on n-1 objects; exact target has beta-binomial split.
    p=[1.0]
    for m in range(1,n):
        enter=2.0/(m+1)
        nextp=[0.0]*min(cap,len(p)+1)
        for t,x in enumerate(p):
            if t<len(nextp):
                nextp[t]+=x*(1-enter)
            if t+1<len(nextp):
                nextp[t+1]+=x*enter
        p=nextp
    vals=[x*math.comb(t,t//2)/2**t for t,x in enumerate(p)]
    t=max(range(len(vals)),key=lambda k:vals[k])
    return t,2*math.pi*math.log(n)*vals[t]

def main():
    for n in range(2,9):
        assert count_pairs_from_row(n)==brute(n),n
    for n in range(1,25):
        if n==1:
            v=1
        else:
            v=max(count_pairs_from_row(n).values())
        assert v==OEIS_A218531[n-1],(n,v,OEIS_A218531[n-1])
    for n in (100,1000,10000,100000):
        t,ratio=diagnostic(n)
        assert 1<ratio<1.5,(n,ratio)
        print('diagnostic',n,'total_extra_mode',t,'scaled_ratio',format(ratio,'.9f'))
    print('VERIFY_OK brute_n=2..8 exact_OEIS_n=1..24 asymptotic_diagnostics_n=100..100000')

if __name__=='__main__':
    main()
