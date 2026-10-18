#!/usr/bin/env python3
"""Check the involution-rank enumerator in wheel partial-isometry monoids.
Python standard library only. Independent distance-based enumeration of partial
involutions is compared with the partition/run formula, including small wheels.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def parts(n, top=None):
    if n == 0:
        yield ()
        return
    for v in range(min(n, top if top is not None else n), 0, -1):
        for tail in parts(n-v, v):
            yield (v,) + tail


def iwreath(size, multiplicity):
    a = 1 if size == 1 else 2
    return sum(factorial(multiplicity)//(2**t * factorial(t) * factorial(multiplicity-2*t))
               * a**(multiplicity-t) for t in range(multiplicity//2+1))


def rim_formula(n):
    ans=[0]*(n+1)
    ans[0]=1
    ans[n]=n+1+(n%2==0)
    for k in range(1,n):
        for lam in parts(k):
            counts=Counter(lam)
            r=len(lam)
            zeros=n-k
            if zeros<r:
                continue
            numerator=n*factorial(r-1)*comb(zeros-1,r-1)
            denominator=1
            aut_inv=1
            for j,m in counts.items():
                denominator*=factorial(m)
                aut_inv*=iwreath(j,m)
            assert numerator%denominator==0
            ans[k]+=numerator//denominator*aut_inv
    return ans


def wheel_formula(n):
    rim=rim_formula(n)
    ans=[0]*(n+2)
    for k in range(n+2):
        ans[k]=(rim[k] if k<=n else 0)+(rim[k-1] if 1<=k<=n+1 else 0)
    for k,a in [(2,1),(3,2),(4,2)]:
        ans[k]+=n*a
    return ans


def wheel_dist(n,x,y):
    if x==y:return 0
    if x==0 or y==0:return 1
    return 1 if ((x-y)%n in (1,n-1)) else 2


def direct(n):
    # An independent exhaustive classification by permutations of every subset.
    # Generate all partial involutions without referring to cycle run types.
    N=n+1
    cnt=[0]*(N+1)
    def enumerate_involutions(unmatched, assigned, points):
        if not unmatched:
            for i,u in enumerate(points):
                for v in points[i+1:]:
                    if wheel_dist(n,u,v)!=wheel_dist(n,assigned[u],assigned[v]):
                        return
            cnt[len(points)]+=1
            return
        x=unmatched[0]
        assigned[x]=x
        enumerate_involutions(unmatched[1:], assigned, points)
        for i in range(1,len(unmatched)):
            y=unmatched[i]
            assigned[x]=y
            assigned[y]=x
            enumerate_involutions(unmatched[1:i]+unmatched[i+1:], assigned, points)
            del assigned[y]
        del assigned[x]
    for k in range(N+1):
        for S in combinations(range(N),k):
            enumerate_involutions(S,{},S)
    return cnt


def main():
    for n in range(3,10):
        f=wheel_formula(n)
        d=direct(n)
        assert f==d,(n, f, d)
        print('rim',n,rim_formula(n))
        print('wheel',n,f,'total',sum(f))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
