"""Exact independent checks for finite bounded-morphism / factorization theorem.
Pure Python 3, standard library only.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def edge_colourings(z):
    """Proper edge colorings of the labelled K_z with z-1 fixed colour names."""
    edges=list(combinations(range(z),2))
    used=[0]*z
    def rec(i):
        if i==len(edges):
            yield tuple(colours)
            return
        a,b=edges[i]
        for c in range(z-1):
            bit=1<<c
            if used[a]&bit or used[b]&bit:continue
            used[a]|=bit;used[b]|=bit;colours.append(c)
            yield from rec(i+1)
            colours.pop();used[a]^=bit;used[b]^=bit
    colours=[]
    yield from rec(0)


def theorem_count(m, F):
    n=m+1
    return factorial(m)*((n*n)+n+sum(comb(n,z)*F[z]//factorial(z-1)
         for z in range(2,n+1,2)))


def direct_bounded_morphisms(n,m):
    """Independently enumerate every monotone map and test each back condition.
    Target has bottom=0, middles 1..m, top=m+1; no theorem structure used.
    """
    N=1<<n; order=sorted(range(N),key=lambda x:(x.bit_count(),x))
    f=[-1]*N
    ups=[[j for j in range(N) if i&j==i] for i in range(N)]
    pred={x:[x^(1<<i) for i in range(n) if x&(1<<i)] for x in range(N)}
    counts=Counter();tot=0
    def poss(vals):
        if not vals:return [0]
        s=set(vals)
        if m+1 in s:return [m+1]
        s.discard(0)
        if len(s)>=2:return [m+1]
        if len(s)==1:return [next(iter(s)),m+1]
        return list(range(m+2))
    def rec(t):
        nonlocal tot
        if t==N:
            if set(f)!=set(range(m+2)):return
            for x in range(N):
                for y in range(m+2):
                    if f[x]==y or f[x]==0 or y==m+1:
                        if not any(f[q]==y for q in ups[x]):return
            tot+=1
            counts[sum(f[1<<i]==0 for i in range(n))]+=1
            return
        x=order[t]
        opts=([m+1] if x==N-1 else [0] if x==0 else poss([f[v] for v in pred[x]]))
        for v in opts:f[x]=v;rec(t+1)
        f[x]=-1
    rec(0)
    return tot,counts


def classification(m,F):
    n=m+1
    res={0:factorial(m)*n*n,1:factorial(m)*n}
    for z in range(2,n+1,2):
        res[z]=comb(n,z)*factorial(m)//factorial(z-1)*F[z]
    return res

if __name__=='__main__':
    F={z:sum(1 for _ in edge_colourings(z)) for z in (2,4,6)}
    assert F=={2:1,4:6,6:720}, F
    print('PROPER_EDGE_COLOURINGS',F)
    expected={2:30,3:162,4:1080,5:9360}
    for m,answer in expected.items():
        count=theorem_count(m,F)
        assert count==answer,(m,count,answer)
        print('THEOREM',m,'n',m+1,'count',count,'zero_singleton_slices',classification(m,F))
    for n,m in ((2,2),(3,2),(4,3)):
        tot,slices=direct_bounded_morphisms(n,m)
        if n==m:
            assert tot==factorial(m),(n,m,tot)
        else:
            assert tot==expected[m] and dict(slices)==classification(m,F),(n,m,tot,slices)
        print('DIRECT',n,m,tot,dict(sorted(slices.items())))
    print('ALL_TESTS_PASS')
