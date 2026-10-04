#!/usr/bin/env python3
from functools import lru_cache
from math import comb, factorial

# Exhaustive rooted non-plane leaf-labelled trees whose internal outdegree is 2 or 3.
# A canonical tree is either ('L', label) or ('N', tuple(sorted(children))).
def set_partitions_k(items, k):
    items=tuple(items)
    n=len(items)
    # restricted-growth strings, fixing first item in block 0, then require all k blocks used
    if k<1 or k>n: return
    a=[0]*n
    def rec(i, mx):
        if i==n:
            if mx==k-1:
                blocks=[[] for _ in range(k)]
                for x,b in zip(items,a): blocks[b].append(x)
                yield tuple(tuple(b) for b in blocks)
            return
        for b in range(min(mx+1,k-1)+1):
            a[i]=b
            yield from rec(i+1,max(mx,b))
    yield from rec(1,0)

def canon_key(t):
    return repr(t)

@lru_cache(None)
def rooted(labels):
    labels=tuple(labels)
    if len(labels)==1:
        return frozenset({('L', labels[0])})
    ans=set()
    for k in (2,3):
        for blocks in set_partitions_k(labels,k):
            pools=[rooted(tuple(b)) for b in blocks]
            for children in __import__('itertools').product(*pools):
                ans.add(('N', tuple(sorted(children,key=canon_key))))
    return frozenset(ans)

def recurrence(N):
    r=[0]*(N+1); r[1]=1
    for n in range(2,N+1):
        s2=sum(comb(n,i)*r[i]*r[n-i] for i in range(1,n))//2
        s3=0
        for i in range(1,n-1):
            for j in range(1,n-i):
                k=n-i-j
                s3 += factorial(n)//(factorial(i)*factorial(j)*factorial(k))*r[i]*r[j]*r[k]
        r[n]=s2+s3//6
    return r

def lagrange(m):
    from fractions import Fraction
    s=Fraction(0,1)
    for j in range((m-1)//2+1):
        i=m-1-2*j
        k=i+j
        s += Fraction(comb(m+k-1,k)*comb(k,j), (2**i)*(6**j))
    return factorial(m-1)*s

# Explicit enumeration versus recurrence through 7 labelled leaves.
r=recurrence(10)
for m in range(1,8):
    e=len(rooted(tuple(range(m))))
    assert e==r[m], (m,e,r[m])
    assert lagrange(m).denominator==1 and lagrange(m).numerator==r[m]

# Unrooted 4-branching D-types on n labelled leaves are rooted types on n-1 labels
# after fixing one leaf and deleting it. Include n=1 separately.
a=[None,1]+[r[n-1] for n in range(2,11)]
expected=[None,1,1,1,4,25,220,2485,34300,559405,10525900]
assert a==expected, (a,expected)

# Check low-arity structural anchors: on four labels there are three binary splits plus one 4-star.
assert a[4]==4
print('VERIFY_OK')
