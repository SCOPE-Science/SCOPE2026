#!/usr/bin/env python3
"""Exact small-instance checks and constructive witnesses for clique-path burning."""
from functools import lru_cache
from itertools import product
from math import isqrt


def predicted(m, n):
    assert m >= 3 and n >= 1
    if m >= 4:
        q = isqrt(n)
        return 1 + q + (q*q < n)
    if n == 1:
        return 2
    q = isqrt(n-1)
    return 1 + max(2, q+(q*q < n-1))


def witness(m, k):
    """Return sources keyed by final-time radius, col zero indexed, row zero indexed."""
    assert k >= 2
    centers = {}
    if m >= 4 or k == 2:
        x = 0
        for r in range(1, k):
            centers[r] = (x + r-1, 0)
            x += 2*r-1
        centers[0] = (0, 0)
        return x, centers
    centers[2] = (1, 0)  # fully covers columns 0,1,2; spike at 3 in row 0
    centers[1] = (4, 1)  # fully covers column 4; spike at 3 in row 1
    centers[0] = (3, 2)  # completes column 3
    x = 5
    for r in range(3, k):
        centers[r] = (x+r-1, 0)
        x += 2*r-1
    return x, centers


def iscovered(m,n,centers):
    return all(any(abs(j-c)+(a != row) <= r
                   for r,(c,a) in centers.items())
               for j in range(n) for row in range(m))


def exact(m,n,k):
    full=(1<<(m*n))-1
    layers=[]
    for r in range(k-1,-1,-1):
        masks=set()
        for j in range(n):
            for a in range(m):
                bits=0
                for q in range(n):
                    for b in range(m):
                        if abs(q-j)+(a!=b)<=r:
                            bits|=1<<(q*m+b)
                masks.add(bits)
        layers.append(tuple(masks))
    @lru_cache(None)
    def rec(i,bits):
        if bits==full: return True
        if i==len(layers): return False
        return any(rec(i+1,bits | block) for block in layers[i])
    return rec(0,0)


def overlap_certificate(n, positions):
    intervals=[]
    for r,c in enumerate(positions,1):
        intervals.append(set(range(max(0,c-r+1),min(n,c+r))))
    U=set().union(*intervals)
    W=sum(map(len,intervals))-len(U)
    R=0
    for x in set(range(n))-U:
        a=sum(bool(I) and max(I)==x-1 for I in intervals)
        b=sum(bool(I) and min(I)==x+1 for I in intervals)
        R+=max(0,a-1)+max(0,b-1)
    return R<=W


def main():
    ns=0
    for m in (3,4,5,8):
        for k in range(2,61):
            N, centers=witness(m,k)
            assert N==(k-1)**2+(m==3 and k>=3)
            assert iscovered(m,N,centers), (m,k,N)
            for n in {1,N,max(1,N//2),max(1,N-1)}:
                clipped={r:(min(c,n-1),a) for r,(c,a) in centers.items()}
                assert iscovered(m,n,clipped),(m,k,n)
            ns+=1
    exact_count=0
    for m,maxn in ((3,12),(4,10),(5,8)):
        for n in range(1,maxn+1):
            want=predicted(m,n)
            assert exact(m,n,want),(m,n,want,'upper')
            if want>1:
                assert not exact(m,n,want-1),(m,n,want,'lower')
            exact_count+=1
    interval_cases=0
    for n,k in ((6,3),(7,4),(8,4)):
        for positions in product(range(n),repeat=k-1):
            assert overlap_certificate(n,positions),(n,k,positions)
            interval_cases+=1
    print('VERIFY_OK',ns,'constructive infinite-family witness samples;',exact_count,
          'independent exact burning instances;',interval_cases,'endpoint-budget instances')
if __name__=='__main__':main()
