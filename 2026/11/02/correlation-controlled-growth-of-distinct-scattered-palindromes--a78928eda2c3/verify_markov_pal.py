#!/usr/bin/env python3
"""Independent finite checks for distinct palindrome subsequences under a binary Markov source.

Usage: python verify_markov_pal.py
"""
from fractions import Fraction as Q
from collections import defaultdict
from math import isclose, sqrt

def formula_coefficients(t, N):
    f=[Q(0) for _ in range(N+1)]
    s=[Q(0) for _ in range(N+1)]
    i=[Q(0) for _ in range(N+1)]
    for j in range(1,N+1):
        f[j]=t*(1-t)**(j-1)
        if j==1: s[j]=1-t
        else: s[j]=t*t*(1-t)**(j-2)
        i[j]=Q(1,2) if j==1 else f[j-1]/2
    def mul(a,b):return [sum((a[k]*b[j-k] for k in range(j+1)),Q(0)) for j in range(N+1)]
    H=[x+y for x,y in zip(mul(s,s),mul(f,f))]
    one_s=s.copy();one_s[0]=1
    R=[2*x for x in mul(i,one_s)]
    inv=[Q(1)]+[Q(0)]*N
    for j in range(1,N+1):inv[j]=sum((H[k]*inv[j-k] for k in range(1,j+1)),Q(0))
    prod=mul(R,inv)
    E=[]; acc=Q(0)
    for z in prod:acc+=z;E.append(acc)
    return E

def actual_pal_count(word):
    # Independent explicit generation of actual distinct scattered strings.
    subs={''}
    for bit in word:
        subs |= {s+bit for s in subs}
    return sum(bool(s) and s==s[::-1] for s in subs)

def exhaustive_aggregates(max_n=12):
    totals=[];num_words=0
    for n in range(max_n+1):
        agg=defaultdict(int)
        if n==0:
            totals.append(agg);continue
        for mask in range(1<<n):
            w=''.join(str((mask>>j)&1) for j in range(n))
            flips=sum(w[j]!=w[j-1] for j in range(1,n))
            agg[flips]+=actual_pal_count(w)
            num_words+=1
        totals.append(agg)
    return totals,num_words

def independent_expectations(totals,t):
    out=[Q(0)]
    for n in range(1,len(totals)):
        out.append(sum((Q(s)*t**k*(1-t)**(n-1-k)/2 for k,s in totals[n].items()),Q(0)))
    return out

def count_by_interval_dp(w):
    n=len(w)
    if n==0:return 0
    dp=[[0]*n for _ in range(n)]
    for i in range(n):dp[i][i]=1
    for k in range(2,n+1):
        for l in range(n-k+1):
            r=l+k-1
            inner=dp[l+1][r-1] if k>=3 else 0
            if w[l]!=w[r]:dp[l][r]=dp[l+1][r]+dp[l][r-1]-inner
            else:
                inner_positions=[j for j in range(l+1,r) if w[j]==w[l]]
                if len(inner_positions)==0:dp[l][r]=2*inner+2
                elif len(inner_positions)==1:dp[l][r]=2*inner+1
                else:
                    a,b=inner_positions[0],inner_positions[-1]
                    dp[l][r]=2*inner-(dp[a+1][b-1] if b>a+1 else 0)
    return dp[0][-1]

def fast_aggregate(n):
    agg=defaultdict(int)
    for mask in range(1<<n):
        w=''.join('1' if (mask>>j)&1 else '0' for j in range(n))
        flips=sum(w[j]!=w[j-1] for j in range(1,n))
        agg[flips]+=count_by_interval_dp(w)
    return agg

def root(t):
    def H(z):
        f=t*z/(1-(1-t)*z)
        s=(1-t)*z+t*z*f
        return s*s+f*f
    a,b=0.,1.
    for _ in range(85):
        mid=(a+b)/2
        if H(mid)>1:b=mid
        else:a=mid
    return (a+b)/2

def main():
    agg,N=exhaustive_aggregates(12)
    cases=[Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]
    for t in cases:
        a=independent_expectations(agg,t)
        f=formula_coefficients(t,12)
        assert a==f,(t,[(i,a[i],f[i]) for i in range(13) if a[i]!=f[i]])
    big=fast_aggregate(15)
    for t in cases:
        a=sum((Q(s)*t**k*(1-t)**(14-k)/2 for k,s in big.items()),Q(0))
        assert a==formula_coefficients(t,15)[15]
    roots=[root(i/100) for i in range(1,101)]
    assert all(a>b for a,b in zip(roots,roots[1:]))
    assert isclose(root(1),sqrt((sqrt(5)-1)/2),abs_tol=1e-14)
    assert isclose(1/root(.5),(1+sqrt(2))/2,abs_tol=1e-14)
    print(f'VERIFY_OK explicit_words={N} explicit_n=1..12 interval_words={1<<15} interval_n=15 probability_cases={len(cases)} coefficient_comparisons={len(cases)*14} monotone_root_grid=100', flush=True)
if __name__=='__main__':main()
