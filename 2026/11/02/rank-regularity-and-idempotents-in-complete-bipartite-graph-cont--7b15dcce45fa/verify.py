#!/usr/bin/env python3
"""Independent exhaustive verification of rank/regular/idempotent formulas for continuous partial transformations of K_{m,n}."""
import itertools, math, collections
from functools import lru_cache

@lru_cache(None)
def falling(a,b):
    return math.factorial(a)//math.factorial(a-b) if 0<=b<=a else 0

def choose(a,b):
    return math.comb(a,b) if 0<=b<=a else 0

def J(a,k):
    return sum(choose(a,j)*falling(k,j) for j in range(0,k+1))

def F(m,n,k):
    return sum((-1)**(k-j)*choose(k,j)*J(m,j)*J(n,j) for j in range(k+1))

def expected(m,n):
    out={}
    for k in range(m+n+1):
        if k==0:
            out[k]=(1,1,1); continue
        side=(choose(m,k)+choose(n,k))
        pure=side*F(m,n,k)
        reg_pure=side*(falling(m,k)*J(n,k)+falling(n,k)*J(m,k)-falling(m,k)*falling(n,k))
        mixed=sum(choose(m,j)*choose(n,k-j)*(falling(m,j)*falling(n,k-j)+falling(n,j)*falling(m,k-j)) for j in range(1,k))
        out[k]=(pure+mixed,reg_pure+mixed,0)
    # idempotents rank k pure side: S of size k fixed, any partial injection from opposite side into S.
    # mixed image: choose nonempty subsets of both sides, rank k.
    for k in range(1,m+n+1):
        total,regular,_=out[k]
        E=choose(m,k)*J(n,k)+choose(n,k)*J(m,k)
        E+=sum(choose(m,j)*choose(n,k-j) for j in range(1,k))
        out[k]=(total,regular,E)
    return out

def isface(xs,m):
    if len(xs)<=1: return True
    return len(xs)==2 and ((xs[0]<m)!=(xs[1]<m))

def continuous(f,m,n):
    N=m+n
    fibers=[[] for _ in range(N)]
    for x,y in enumerate(f):
        if y!=N: fibers[y].append(x)
    if any(not isface(a,m) for a in fibers): return False
    for x in range(m):
        for y in range(m,N):
            if not isface(fibers[x]+fibers[y],m): return False
    return True

def is_idempotent(f):
    N=len(f)
    return all(f[y]==y for y in f if y!=N)

def is_regular_by_sections(f,m,n):
    N=len(f)
    fibers={t:[] for t in f if t!=N}
    for x,t in enumerate(f):
        if t!=N: fibers[t].append(x)
    support=tuple(sorted(fibers))
    for picks in itertools.product(*(fibers[y] for y in support)):
        section=[N]*N
        for y,x in zip(support,picks): section[y]=x
        if continuous(section,m,n): return True
    return False

def verify(m,n):
    N=m+n; exp=expected(m,n)
    counts=collections.Counter(); regular=collections.Counter(); idem=collections.Counter()
    for f in itertools.product(range(N+1),repeat=N):
        if not continuous(f,m,n): continue
        k=len(set(f)-{N}); counts[k]+=1
        if is_regular_by_sections(f,m,n): regular[k]+=1
        if is_idempotent(f): idem[k]+=1
    got={k:(counts[k],regular[k],idem[k]) for k in range(N+1)}
    assert got==exp,(m,n,got,exp)
    return m,n,sum(counts.values()),sum(regular.values()),sum(idem.values()),got

if __name__=='__main__':
    for m,n in [(2,2),(2,3),(3,2),(3,3)]:
        result=verify(m,n)
        print('PASS',result[:5],result[5])
    print('VERIFY_OK')
