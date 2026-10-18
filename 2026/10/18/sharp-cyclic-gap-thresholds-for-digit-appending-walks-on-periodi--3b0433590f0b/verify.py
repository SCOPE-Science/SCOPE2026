#!/usr/bin/env python3
"""Independent finite checks for cyclic-gap digit-appending classification."""
from itertools import combinations
from random import Random


def gap(S,h):
    if not S: return None
    a=sorted(S)
    return max((a[(i+1)%len(a)]-a[i])%h or h for i in range(len(a)))


def cycle(A):
    n=len(A)
    color=[0]*n
    def visit(v):
        color[v]=1
        for w in A[v]:
            if color[w]==1 or (color[w]==0 and visit(w)):
                return True
        color[v]=2
        return False
    return any(color[v]==0 and visit(v) for v in range(n))


def expected_N(u):
    h=len(u)
    candidates=[gap({i for i,x in enumerate(u) if x==a},h) for a in (0,-1)]
    return min((q for q in candidates if q is not None), default=None)


def actual_cycle(u,N,b=2):
    h=len(u)
    edges=[set() for i in range(h)]
    for i in range(h):
        for t in range(1,N+1):
            j=(i+t)%h
            d=u[j]-b**t*u[i]
            if 0<=d<b**t:
                edges[i].add(j)
    return cycle(edges)


def test_all_sets():
    tests=0
    for h in range(1,11):
        for mask0 in range(1<<h):
            remaining=((1<<h)-1)^mask0
            mask1=remaining
            while True:
                u=[0 if mask0>>i&1 else (-1 if mask1>>i&1 else 2) for i in range(h)]
                want=expected_N(u)
                for N in range(1,h+2):
                    found=actual_cycle(u,N)
                    if found!=(want is not None and N>=want):
                        raise AssertionError((h,mask0,mask1,N,want,found))
                    tests+=1
                if mask1==0:break
                mask1=(mask1-1)&remaining
    return tests


def test_random():
    rng=Random(74271)
    tests=0
    for _ in range(13000):
        h=rng.randrange(1,13)
        b=rng.choice((2,3,7,10))
        u=[rng.randrange(-9,10) for i in range(h)]
        want=expected_N(u)
        for N in (1, rng.randrange(1,h+5), h+3):
            found=actual_cycle(u,N,b)
            if found!=(want is not None and N>=want):
                raise AssertionError((h,b,u,N,want,found))
            tests+=1
        U=max(map(abs,u))
        M=1
        while b**M <=4*(U+1): M+=1
        m=M+rng.randrange(0,3*h)
        for t in range(1,min(9,h+4)):
            for k in range(1,min(10,h+5)):
                a=b**m+u[m%h]
                z=b**(m+k)+u[(m+k)%h]
                d=z-b**t*a
                possible=0<=d<b**t
                equivalence=(k==t and 0<=u[(m+t)%h]-b**t*u[m%h]<b**t)
                if possible!=equivalence:
                    raise AssertionError((h,b,u,m,t,k,possible,equivalence))
                tests+=1
    return tests


def main():
    exhaustive=test_all_sets()
    sampled=test_random()
    print('VERIFY_OK subset_graph_comparisons=%s sampled_recurrence_and_graph_checks=%s'%(exhaustive,sampled))

if __name__=='__main__': main()
