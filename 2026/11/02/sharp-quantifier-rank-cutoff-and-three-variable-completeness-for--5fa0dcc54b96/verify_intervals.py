#!/usr/bin/env python3
"""Independent arithmetic checks of the rank-bounded cyclic-arc proof.

The recursive formula F(r,s) tests that an oriented open arc has at least s
points, for 0<=s<=2^r-1. Its recursive evaluation uses a witness splitting
an arc into two shorter arcs. Cap classes are the exact one-step profiles.
"""
from functools import lru_cache

@lru_cache(None)
def formula(r,s,c):
    if s==0:
        return True
    if r==0 or c==0 or s>(1<<r)-1:
        return False
    left=(s-1)//2
    right=s-1-left
    return any(formula(r-1,left,a) and formula(r-1,right,c-1-a)
               for a in range(c))

def profiles(c,threshold):
    return frozenset((min(a,threshold),min(c-1-a,threshold))
                     for a in range(c))

def check():
    nformula=0
    for rank in range(0,7):
        for s in range(0,(1<<rank)):
            for c in range(0,85):
                assert formula(rank,s,c)==(c>=s),(rank,s,c)
                nformula+=1
    print('rank-recursive threshold formula semantic checks:',nformula,'PASS')
    nprofiles=0
    for rank in range(1,7):
        old=(1<<rank)-1
        new=(1<<(rank-1))-1
        base=profiles(old,new)
        # For all c>=old, the achievable truncated split profiles stabilize.
        for c in range(old, 3*old+12):
            assert profiles(c,new)==base,(rank,c)
            nprofiles+=1
        # For all c<old, distinct c have different profiles: arithmetic lower direction.
        seen=set()
        for c in range(old):
            p=profiles(c,new)
            assert p not in seen,(rank,c)
            seen.add(p)
    print('arc split stabilization checks:',nprofiles,'PASS')
    for rank in range(3,9):
        threshold=1<<(rank-1)
        cap=(1<<(rank-2))-1
        for n in range(3,2*threshold+3):
            # Realizable two-arc lower bounds a+b+2 <= n.
            for a in range(cap+1):
                for b in range(cap+1):
                    exists=(n>=a+b+2)
                    brute=any(x>=a and n-2-x>=b for x in range(n-1))
                    assert exists==brute,(rank,n,a,b)
        print(f'rank={rank} distinguishing-size cutoff={threshold} PASS')
    print('VERIFY_INTERVALS_OK')

if __name__=='__main__':
    check()
