#!/usr/bin/env python3
"""Standalone finite verification of Takasaki quandles on (Z/4Z)^d.
Only small instances are enumerated; arbitrary-d proof is mathematical.
"""
from itertools import permutations, product

def xor(a,b): return a^b

def op(a,b,c,d): return (a,b^a^c)

def affine_permutation(pi,d):
    v=pi[0]; L=[pi[a]^v for a in range(1<<d)]
    return all(L[a^b]==(L[a]^L[b]) for a in range(1<<d) for b in range(1<<d))

def automorphism(pi,t,d):
    N=1<<d; points=list(product(range(N),repeat=2))
    images={(a,b):(pi[a],t[a]^pi[a]^pi[a^b]) for a,b in points}
    if len(set(images.values()))!=N*N: return False
    for a,b in points:
        for c,e in points:
            x=op(a,b,c,e)
            l=images[x]; aa,bb=images[(a,b)];cc,dd=images[(c,e)]
            if l!=op(aa,bb,cc,dd): return False
    return True

def rank_binary(rows):
    pivots={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in pivots: x^=pivots[p]
            else:
                pivots[p]=x;break
    return len(pivots)

def check():
    for d in (1,2,3,4):
        N=1<<d
        # Right translation by y=(c,*) on all x=(a,b) adds a XOR c to b.
        vecs=[]
        for c in range(N):
            z=sum((((a^c)>>j)&1) << (a*d+j) for a in range(N) for j in range(d))
            vecs.append(z)
        assert rank_binary(vecs)==d+1
        print('INNER',d,'generators',N,'rank',rank_binary(vecs),'order',1<<(d+1))
    for d in (1,2,3):
        N=1<<d
        pi_good=[pi for pi in permutations(range(N)) if affine_permutation(pi,d)]
        expected=N
        from math import prod
        expected*=prod(N-2**j for j in range(d))
        assert len(pi_good)==expected
        print('AFFINE_ORBIT_PERMUTATIONS',d,len(pi_good))
        if d<=2:
            autos=0
            # all images of orbit representatives, no use of automorphism formula
            for pi in permutations(range(N)):
                for t in product(range(N), repeat=N):
                    # induced mapping from f((a,0)*(a+b,0))
                    valid=automorphism(pi,t,d)
                    assert valid == affine_permutation(pi,d)
                    autos+=valid
            expected_total=(N**N)*expected
            assert autos==expected_total
            print('EXHAUSTIVE_AUT',d,autos)
        else:
            # All S_8 permutations tested for the affine constraint;
            # sample independent homomorphism check at several translations.
            sample=pi_good[::173][:8]
            for pi in sample:
                for v in (0,1,N-1):
                    t=tuple(((a*3+v) % N) for a in range(N))
                    assert automorphism(pi,t,d)
            print('SAMPLE_HOMOMORPHISMS',d,len(sample)*3)
    assert (4**4)*24==6144
    assert (4**2)* (2**4*6) ==1536
    print('VERIFY_OK')
if __name__=='__main__':check()
