#!/usr/bin/env python3
"""Exact enumeration of signed total Roman dominating functions of clique bouquets.
All checks are reproducible using only the Python 3 standard library.
"""
from collections import Counter
from itertools import product
from math import comb, factorial

def windmill_neighbors(m,t):
    size=1+m*t
    ans=[set(range(1,size))]
    for j in range(m):
        vs=set(range(1+j*t,1+(j+1)*t))
        for v in range(t):
            ans.append((vs-{1+j*t+v})|{0})
    return tuple(tuple(sorted(x)) for x in ans)

def feasible(vals,nb):
    return all(sum(vals[u] for u in adj)>=1 and (vals[v]!=-1 or any(vals[u]==2 for u in adj))
               for v,adj in enumerate(nb))

def direct(m,t):
    nb=windmill_neighbors(m,t)
    res=Counter()
    for vals in product((-1,1,2), repeat=1+m*t):
        if feasible(vals,nb): res[sum(vals)]+=1
    return res

def blade_patterns(c,t):
    out=Counter()
    for vals in product((-1,1,2), repeat=t):
        w=sum(vals)
        if any(c+w-x<1 for x in vals): continue
        if c!=2 and -1 in vals and 2 not in vals: continue
        out[(w,2 in vals)]+=1
    return out

def conv(m,t,c):
    B=blade_patterns(c,t)
    dp=Counter({(0,False):1})
    for _ in range(m):
        nxt=Counter()
        for (s,has2),ways in dp.items():
            for (w,b2),count in B.items():
                nxt[(s+w,has2 or b2)]+=ways*count
        dp=nxt
    return Counter({w+c:sum(val for (ss,has2),val in dp.items() if ss==w and ss>=1 and (c!=-1 or has2))
                    for w in set(ss for ss,_ in dp) if w>=1})

def formula(m,t):
    if t%2:
        B=sum(factorial(t)//(factorial((t-1+d)//2)*factorial((t+1-3*d)//2)*factorial(d))
              for d in range(0,(t+1)//3+1,2) if (t+1-3*d)>=0)
        return m+2,B**m
    if t==2:
        p={-2:1,0:2,1:2,2:1,3:2,4:1}
        dp={0:1}
        for _ in range(m):
            nd={}
            for s,a in dp.items():
                for w,b in p.items(): nd[s+w]=nd.get(s+w,0)+a*b
            dp=nd
        return 3,dp[1]
    B=comb(t,t//2)
    A=sum(factorial(t)//(factorial((t-1+d)//2)*factorial((t+1-3*d)//2)*factorial(d))
          for d in range(1,(t+1)//3+1,2) if (t+1-3*d)>=0)
    return 3,m*A*B**(m-1)

if __name__=='__main__':
    total=0
    for m in range(2,9):
        for t in range(2,13):
            counts=Counter()
            for c in (-1,1,2): counts.update(conv(m,t,c))
            assert counts, (m,t)
            w=min(counts)
            assert (w,counts[w])==formula(m,t), (m,t,w,counts[w],formula(m,t))
            total+=1
    print('DP cross-check: 77 parameter pairs through m=8,t=12 passed')
    for m,t in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4)]:
        exact=direct(m,t)
        dynamic=Counter()
        for c in (-1,1,2): dynamic.update(conv(m,t,c))
        assert exact==dynamic, (m,t)
        print(f'Exhaustive: m={m}, t={t}, min_weight={min(exact)}, optimal_count={exact[min(exact)]}, labelings={sum(exact.values())}')
    print('All direct enumerations, independent dynamic enumerations, and formulas agree.')
