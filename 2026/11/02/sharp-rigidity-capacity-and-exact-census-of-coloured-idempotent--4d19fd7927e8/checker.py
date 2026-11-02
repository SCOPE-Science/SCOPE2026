#!/usr/bin/env python3
"""Exhaustive checks for colored idempotent unary algebras and rigidity."""
from itertools import product
from collections import Counter
from math import comb

def exhaustive(n,q):
    all_keys=set()
    rigid_keys=set()
    labeled_checked=0
    for f in product(range(n),repeat=n):
        if any(f[f[x]]!=f[x] for x in range(n)):
            continue
        roots=[i for i in range(n) if f[i]==i]
        for color in product(range(q),repeat=n):
            stars=[]
            for root in roots:
                counts=[0]*q
                for x in range(n):
                    if x!=root and f[x]==root:counts[color[x]]+=1
                stars.append((color[root],*counts))
            key=tuple(sorted(stars))
            all_keys.add(key)
            if len(stars)==len(set(stars)) and all(max(star[1:])<=1 for star in stars):
                rigid_keys.add(key)
            labeled_checked+=1
    return len(all_keys),len(rigid_keys),labeled_checked

def unrestricted_counts(q,N):
    arr=[1]+[0]*N
    for size in range(1,N+1):
        choices=q*comb(size+q-2,q-1)
        for _ in range(choices):
            for j in range(size,N+1): arr[j]+=arr[j-size]
    return arr

def rigid_counts(q):
    N=q*2**(q-1)*(q+2)
    arr=[1]+[0]*N
    for j in range(q+1):
        copies=q*comb(q,j)
        for _ in range(copies):
            for n in range(N,j,-1):arr[n]+=arr[n-j-1]
    return arr

def divisor_recurrence(q,N):
    arr=[1]+[0]*N
    b=[0]*(N+1)
    for d in range(1,N+1):
        a=q*comb(d+q-2,q-1)
        for m in range(d,N+1,d): b[m]+=d*a
    for n in range(1,N+1):
        total=sum(b[m]*arr[n-m] for m in range(1,n+1))
        assert total%n==0
        arr[n]=total//n
    return arr

for q,top in [(1,6),(2,5),(4,4)]:
    U=unrestricted_counts(q,20)
    R=rigid_counts(q)
    assert U==divisor_recurrence(q,20)
    assert len(R)==q*2**(q-1)*(q+2)+1
    assert R[0]==R[-1]==1
    assert all(x>0 for x in R)
    assert R==R[::-1]
    for n in range(1,top+1):
        observed_unrestricted,observed_rigid,structures=exhaustive(n,q)
        assert observed_unrestricted==U[n],(q,n,observed_unrestricted,U[n])
        assert observed_rigid==(R[n] if n<len(R) else 0),(q,n,observed_rigid)
        print('q=',q,'n=',n,'labeled=',structures,'unlabeled=',U[n],'rigid=',(R[n] if n<len(R) else 0))
    print('q=',q,'rigidity_cutoff=',len(R)-1,'initial_unlabeled=',U[:9])
# Independent check of the documented 1-colorable-predicate Euler/MacMahon identification.
assert unrestricted_counts(2,8)==[1,2,7,18,47,110,258,568,1237]
assert rigid_counts(1)==[1,1,1,1]
print('ALL_CHECKS_OK')
