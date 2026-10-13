#!/usr/bin/env python3
"""Exact small-board checker for power domination and inclusion-minimal sets on rook graphs."""
from itertools import combinations
from math import comb, factorial
from collections import Counter

def stirling(n,k):
    a=[[0]*(k+1) for _ in range(n+1)];a[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):a[i][j]=j*a[i-1][j]+a[i-1][j-1]
    return a[n][k]

def formula_minimal(m,n):
    if m==n:return {m-1:2*m**m-m*m*factorial(m-1)}
    if m>n:return formula_minimal(n,m)
    ans={m-1:m*n**(m-1)}
    total=n*sum(comb(m,a)*factorial(a)*stirling(n-1,a) for a in range(1,m-1))
    if total:ans[n-1]=total
    return ans

def polynomial_by_inclusion_exclusion(m,n):
    result=[comb(m*n,d) for d in range(m*n+1)]
    for a in range(m-1):
        for b in range(n-1):
            covered=[0]*(m*n+1)
            for i in range(a+1):
                for j in range(b+1):
                    cells=(a-i)*(b-j)
                    mult=(-1)**(i+j)*comb(a,i)*comb(b,j)
                    for degree in range(cells+1):
                        covered[degree] += mult*comb(cells,degree)
            mult=comb(m,a)*comb(n,b)
            result=[x-mult*y for x,y in zip(result,covered)]
    return result

def structural_minimal(m,n,s):
    rows={v//n for v in range(m*n) if s>>v&1}
    cols={v%n for v in range(m*n) if s>>v&1}
    a,b,k=len(rows),len(cols),s.bit_count()
    return ((a==m-1 and k==a and b<n-1)
       or (b==n-1 and k==b and a<m-1)
       or (a==m-1 and b==n-1 and k==a==b))

def power(m,n,s):
    if not s:return False
    allv=(1<<(m*n))-1
    nbr=[]
    for i in range(m):
        for j in range(n):
            mask=0
            for p in range(m):
                for q in range(n):
                    if (i,j)!=(p,q) and (i==p or j==q):mask|=1<<(p*n+q)
            nbr.append(mask)
    obs=s
    for v in range(m*n):
        if s>>v&1:obs|=nbr[v]
    while True:
        newer=obs
        for v in range(m*n):
            if obs>>v&1:
                unseen=nbr[v] & (~obs) & allv
                if unseen and unseen&(unseen-1)==0:newer|=unseen
        if newer==obs:break
        obs=newer
    return obs==allv

def main():
    tests=0;members=0;optcounts=0
    cases=[(m,n) for m in range(2,5) for n in range(2,5)]+[(3,5)]
    for m,n in cases:
            nvert=m*n
            correct=[];mincounts=Counter();count_by_weight=Counter()
            for s in range(1,1<<nvert):
                rows={v//n for v in range(nvert) if s>>v&1}
                cols={v%n for v in range(nvert) if s>>v&1}
                expected=len(rows)>=m-1 or len(cols)>=n-1
                found=power(m,n,s)
                assert expected==found,(m,n,s,expected,found)
                tests+=1
                if found:
                    members+=1
                    count_by_weight[s.bit_count()]+=1
                    if all(not power(m,n,s & ~(1<<v)) for v in range(nvert) if s>>v&1):
                        mincounts[s.bit_count()]+=1
                        assert structural_minimal(m,n,s),(m,n,s,'missed minimalist')
                    else:
                        assert not structural_minimal(m,n,s),(m,n,s,'false minimalist')
            theory=formula_minimal(m,n)
            assert mincounts==theory,(m,n,mincounts,theory)
            coefficient_formula=polynomial_by_inclusion_exclusion(m,n)
            coefficient_brute=[count_by_weight[d] for d in range(m*n+1)]
            assert coefficient_formula==coefficient_brute,(m,n,coefficient_formula,coefficient_brute)
            optcounts+=sum(mincounts.values())
            print('TEST',m,n,'minimal',dict(mincounts))
    print('VERIFY_OK','subset_checks',tests,'power_sets',members,'minimal_sets',optcounts,'boards','2..4 plus 3x5','coefficient_cases',len(cases))
if __name__=='__main__':main()
