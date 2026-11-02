#!/usr/bin/env python3
"""Independent exhaustive check of domination on selected finite Sierpinski products.
No external dependencies, standard Python 3.
"""
from itertools import combinations, product

def predicted(f,n):
    m=len(f)
    a=[f.count(h) for h in range(n)]
    if not all(a):
        return m
    out=m
    for c in range(1,n+1):
        for C in combinations([h for h in range(n) if a[h]>=2],c):
            C=set(C)
            value=c*c + sum(max(a[h],c) for h in range(n) if h not in C)
            out=min(out,value)
    return out

def direct_domination(f,n):
    m=len(f); N=m*n
    closed=[1<<v for v in range(N)]
    for g in range(m):
        for u in range(n):
            for v in range(n):
                closed[g*n+u] |= 1<<(g*n+v)
    for g in range(m):
        for h in range(g+1,m):
            u=g*n+f[h];v=h*n+f[g]
            closed[u]|=1<<v
            closed[v]|=1<<u
    total=(1<<N)-1
    for k in range(m+1):
        for S in combinations(range(N),k):
            cover=0
            for v in S:
                cover|=closed[v]
                if cover==total:break
            if cover==total:return k
    raise AssertionError('dominating set not found')

def count_vectors(m,n):
    for counts in product(range(m+1),repeat=n):
        if sum(counts)==m and tuple(sorted(counts,reverse=True))==counts:
            yield counts

if __name__=='__main__':
    checks=0
    for n,mmax in [(2,9),(3,7),(4,6)]:
        for m in range(2,mmax+1):
            for counts in count_vectors(m,n):
                f=[h for h,count in enumerate(counts) for _ in range(count)]
                value=predicted(f,n)
                actual=direct_domination(f,n)
                assert value==actual,(n,m,counts,value,actual)
                checks+=1
        print('n',n,'success; profiles checked',checks,flush=True)
    print('ALL CHECKED',checks)
