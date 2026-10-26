#!/usr/bin/env python3
"""Reproduce the ternary cyclic two-gram profile support enumerator."""
from collections import Counter
from itertools import product
from math import comb

def C(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def formula(n):
    # Coefficients of a rational bivariate series, expanded by nonzero arc support.
    ans = Counter({0:3})
    for x in range(1,n//2+1):
        ans[2] += 3*(n-2*x+1)
    # Noncirculating three-symbol Eulerian supports: 2 or 3 reversible pairs.
    for k in (2,3):
        for x in range(k,n//2+1):
            ans[2*k] += (3 if k==2 else 1)*C(x-1,k-1)*C(n-2*x+2,2)
    # Either orientation of a positive full directed triangle; k reverse arcs.
    for t in range(1,n//3+1):
        ans[3] += 2*C(n-3*t+2,2)
        for k in (1,2,3):
            for x in range(k,(n-3*t)//2+1):
                ans[3+k] += 2*C(3,k)*C(x-1,k-1)*C(n-3*t-2*x+2,2)
    return +ans

def direct_words(n):
    profiles=set()
    for word in product(range(3),repeat=n):
        a=[0]*9
        for j in range(n):a[3*word[j]+word[(j+1)%n]]+=1
        profiles.add(tuple(a))
    return Counter(sum(p[3*i+j]>0 for i in range(3) for j in range(3) if i!=j) for p in profiles)

def independent_flow(n):
    # Independent from formula: enumerate every balanced count matrix, filter connected.
    ans=Counter()
    for t in range(-(n//3),n//3+1):
        m=n-3*abs(t)
        for x in range(m//2+1):
            for y in range((m-2*x)//2+1):
                for z in range((m-2*x-2*y)//2+1):
                    rem=m-2*(x+y+z)
                    for a in range(rem+1):
                        for b in range(rem-a+1):
                            c=rem-a-b
                            E=[[0]*3 for _ in range(3)]
                            for i,v in enumerate((a,b,c)): E[i][i]=v
                            for (i,j),v in zip(((0,1),(1,2),(2,0)),(x,y,z)):
                                E[i][j]=v+max(t,0)
                                E[j][i]=v+max(-t,0)
                            active={i for i in range(3) if sum(E[i])}
                            reached={min(active)}
                            while True:
                                nxt=reached | {j for i in reached for j in active if E[i][j] or E[j][i]}
                                if nxt==reached: break
                                reached=nxt
                            if reached!=active: continue
                            s=sum(E[i][j]>0 for i in range(3) for j in range(3) if i!=j)
                            ans[s]+=1
    return +ans

if __name__=='__main__':
    first=[3,6,11,24,48,95,174,306,510,819,1266,1901,2775,3960,5531]
    assert [sum(formula(n).values()) for n in range(1,16)]==first
    for n in range(1,12):
        assert formula(n)==direct_words(n),(n,formula(n),direct_words(n))
    for n in range(1,15):
        assert formula(n)==independent_flow(n),(n,formula(n),independent_flow(n))
    assert set().union(*(set(formula(n)) for n in range(1,20)))=={0,2,3,4,5,6}
    print('TERNARY_SUPPORT_REFINEMENT_PASS direct=1..11 flow=1..14 first15='+repr(first))
