#!/usr/bin/env python3
"""Direct enumeration and cyclic transfer verification for antiprism P3-convexity."""
from collections import Counter
from itertools import combinations
from fractions import Fraction

def graph(n):
    e=[set() for _ in range(2*n)]
    def add(a,b):
        assert a!=b
        e[a].add(b);e[b].add(a)
    for i in range(n):
        add(i,(i+1)%n)
        add(n+i,n+(i+1)%n)
        add(i,n+i)
        add(i,n+(i-1)%n)
    return e

def convex_coeffs(n):
    e=graph(n);v=2*n;cnt=Counter();
    for mask in range(1<<v):
        if all(mask>>i&1 or sum(bool(mask>>j&1) for j in e[i])<=1 for i in range(v)):
            cnt[mask.bit_count()]+=1
    return dict(cnt)

def packing_coeffs(n):
    e=graph(n);v=2*n;cnt=Counter();neigh2=[]
    for i in range(v):
        bad=set(e[i]);bad.add(i)
        for j in e[i]:bad.update(e[j])
        neigh2.append(sum(1<<j for j in bad))
    for mask in range(1<<v):
        if all(not (mask>>i&1) or (mask & neigh2[i]) == (1<<i) for i in range(v)):
            cnt[mask.bit_count()]+=1
    return dict(cnt)

def renewal_counts(max_n):
    # The bivariate rational function Q(t,x)= [2*x*t^3*(3-2t)+x^2*t^5*(5-4t)] / [(1-t)*(1-t-2*x*t^3-x^2*t^5)]
    # Use recurrence (1-t-2xt^3-x^2t^5)Q = numerator/(1-t).
    a=[Counter() for _ in range(max_n+1)]
    for n in range(max_n+1):
        c=Counter()
        if n>=1:c.update(a[n-1])
        if n>=3:
            for k,v in a[n-3].items():c[k+1]+=2*v
        if n>=5:
            for k,v in a[n-5].items():c[k+2]+=v
        # coefficient of numerator/(1-t): 6x t^3 + 2x t^4 + ... (2xt^3(3-2t)/(1-t))
        if n==3:c[1]+=6
        if n>=4:c[1]+=2
        if n==5:c[2]+=5
        if n>=6:c[2]+=1
        a[n]=c
    return a

def test():
    predicted=renewal_counts(13)
    for n in range(3,11):
        p=convex_coeffs(n)
        q=packing_coeffs(n)
        assert p==dict(Counter({0:1,2*n:1})+Counter(q)-Counter({0:1})),(n,p,q)
        expected=dict(predicted[n]);actual={k:v for k,v in q.items() if k>0}
        assert actual==expected,(n,actual,expected)
        assert max(q)==(2*n)//5 if n>=5 else 1,(n,q)
        print(n,dict(sorted(p.items())))
    # Separate direct combinatorial enumeration of cyclic word admissibility for n <= 12.
    for n in range(3,13):
        byword=Counter()
        for wordnum in range(3**n):
            q=wordnum;word=[]
            for _ in range(n):q,r=divmod(q,3);word.append(r)
            inds=[i for i,t in enumerate(word) if t]
            if not inds:continue
            if len(inds)>1:
                ok=True
                for i,j in zip(inds,inds[1:]+inds[:1]):
                    d=(j-i)%n
                    if d<2 or (d==2 and not (word[i]==1 and word[j]==2)):
                        ok=False;break
                if not ok:continue
            byword[len(inds)]+=1
        assert dict(byword)==dict(predicted[n]),(n,byword,predicted[n])
    print('VERIFY_OK; direct exhaustive convexity for n<=10, cyclic word encoding for n<=12')
if __name__=='__main__':test()
