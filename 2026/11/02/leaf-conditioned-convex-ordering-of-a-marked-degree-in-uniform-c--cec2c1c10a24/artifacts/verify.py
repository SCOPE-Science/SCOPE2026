#!/usr/bin/env python3
"""Exact finite checks for conditional tagged degree under leaf stratification."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

def stirling(maxn):
    s=[[0]*(maxn+1) for _ in range(maxn+1)]
    s[0][0]=1
    for n in range(1,maxn+1):
        for k in range(1,n+1):
            s[n][k]=s[n-1][k-1]+k*s[n-1][k]
    return s

def pmf(n,k,s):
    m=n-2; q=n-k
    if not 1<=q<=m: raise ValueError((n,k))
    ans={0:Fraction(k,n)}
    for j in range(1,m+1):
        if m-j<0:continue
        ans[j]=Fraction(comb(m,j)*s[m-j][q-1],n*s[m][q])
    return ans

def exhaustive(n):
    d={}
    for code in product(range(n), repeat=n-2):
        k=n-len(set(code)); j=code.count(0)
        if (k,j) not in d: d[(k,j)]=0
        d[(k,j)]+=1
    return d

def main():
    s=stirling(35); checks=0
    for n in range(4,9):
        counts=exhaustive(n)
        totals=Counter()
        for (k,j),cnt in counts.items(): totals[k]+=cnt
        for k in range(2,n):
            p=pmf(n,k,s)
            assert sum(p.values())==1
            for j in range(n-1):
                assert p.get(j,0)==Fraction(counts.get((k,j),0),totals[k]);checks+=1
    for n in range(4,34):
        m=n-2
        for k in range(2,n):
            p=pmf(n,k,s)
            assert sum(p.values())==1;checks+=1
            assert sum(Fraction(j)*prob for j,prob in p.items())==Fraction(m,n);checks+=1
            q=n-k
            fm2=sum(Fraction(j*(j-1))*prob for j,prob in p.items())
            assert fm2==Fraction(m*(m-1),n)*Fraction(s[m-1][q],s[m][q]);checks+=1
        for k in range(2,n-1):
            for l in range(k+1,n):
                p=pmf(n,k,s); q=pmf(n,l,s)
                # Compare the two laws by their right tails at every threshold
                tails=[]
                for j in range(1,m+2):
                    delta=sum(q[t]-p[t] for t in range(j,m+1))
                    tails.append(delta)
                assert tails[0]<0;checks+=1
                assert tails[k-1]>0;checks+=1  # threshold j=k, the low leaf stratum cannot reach
                # Exactly one weak sign change from negative to positive.
                assert not any(tails[i]>0 and tails[j]<0 for i in range(len(tails)) for j in range(i+1,len(tails)));checks+=1
                # Convex-order stop-loss inequalities and strictness for thresholds 1 ... l-1.
                for threshold in range(1,m+1):
                    excess=sum(Fraction(max(j-threshold,0))*(q[j]-p[j]) for j in range(0,m+1))
                    assert excess>=0;checks+=1
                    if 1<=threshold<l-1:assert excess>0;checks+=1
                # Likelihood ratio increases for positive values on shared support.
                for i in range(1,k):
                    for j in range(i+1,k):
                        assert q[j]*p[i]>=q[i]*p[j];checks+=1
    print('PASS:',checks,'exact assertions; all finite population enumerations and convex-order checks passed')
if __name__=='__main__':main()
