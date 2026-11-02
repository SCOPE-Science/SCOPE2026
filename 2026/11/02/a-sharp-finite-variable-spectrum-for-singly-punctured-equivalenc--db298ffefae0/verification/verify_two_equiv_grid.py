#!/usr/bin/env python3
"""Finite-variable formula-type fixed point for two labelled equivalence relations.

The program computes the boolean (without counting) k-dimensional refinement of
all assignments jointly across two finite structures. It is a finite corroboration,
not a substitute for the unbounded pebble-game proof.
"""
from itertools import product, combinations

def cells(m,n,punctured):
    return tuple((r,c) for r in range(m) for c in range(n)
                 if not punctured or (r,c)!=(0,0))

def predicted(k, m,n, hole):
    if k==1:return ('one',)
    if k==2:
        if not hole or min(m,n)>=3:return ('generic',)
        return ('puncture-small',m==2,n==2)
    return ('puncture' if hole else 'full',
            min(m-1,k) if hole else min(m,k),
            min(n-1,k) if hole else min(n,k))

def equivalent(spec1,spec2,k):
    models=[cells(*spec1),cells(*spec2)]
    sizes=[len(M) for M in models]
    lengths=[n**k for n in sizes]
    starts=[0,lengths[0]]
    tuples=[list(product(range(n),repeat=k)) for n in sizes]
    old=[]
    for M,ts in zip(models,tuples):
        for t in ts:
            old.append(tuple((t[i]==t[j],M[t[i]][0]==M[t[j]][0],M[t[i]][1]==M[t[j]][1])
                             for i in range(k) for j in range(k)))
    def compress(conditions):
        dic={sig:i for i,sig in enumerate(sorted(set(conditions)))}
        return [dic[sig] for sig in conditions]
    old=compress(old)
    for iteration in range(100):
        signatures=[]
        for M,n,ts,start in zip(models,sizes,tuples,starts):
            powers=[n**(k-i-1) for i in range(k)]
            for ix,t in enumerate(ts):
                updates=[]
                for j in range(k):
                    base=ix-t[j]*powers[j]
                    updates.append(tuple(sorted({old[start+base+w*powers[j]] for w in range(n)})))
                signatures.append((old[start+ix],tuple(updates)))
        new=compress(signatures)
        if len(set(new))==len(set(old)):
            return bool(set(new[:lengths[0]])&set(new[lengths[0]:])),iteration+1
        old=new
    raise AssertionError('refinement did not stabilize')

def main():
    specs=list(product(range(2,5),range(2,5),(False,True)))
    p2=p3=0; rounds2=rounds3=0
    for x,y in combinations(specs,2):
        for k in (2,3):
            e,r=equivalent(x,y,k)
            assert e == (predicted(k,*x)==predicted(k,*y)),(k,x,y,e)
            if k==2:p2+=1;rounds2=max(rounds2,r)
            else:p3+=1;rounds3=max(rounds3,r)
    print('k=2:',p2,'pairs across 18 structures: PASS; maximum rounds',rounds2)
    print('k=3:',p3,'pairs across 18 structures: PASS; maximum rounds',rounds3)
    cutoff3=[((4,2,0),(5,2,0)),((4,2,1),(5,2,1)),
             ((2,4,0),(2,5,0)),((2,4,1),(2,5,1)),
             ((3,4,1),(3,5,1)),((4,3,1),(5,3,1))]
    for x,y in cutoff3:
        e,_=equivalent(x,y,3)
        assert e==(predicted(3,*x)==predicted(3,*y)),(3,x,y,e)
    print('k=3: six threshold comparisons: PASS')
    examples=[((2,2,0),(3,3,0)),((2,2,1),(2,3,1)),
              ((2,3,1),(2,4,1)),((3,3,1),(3,4,1)),
              ((3,4,1),(4,4,1)),((3,3,0),(3,3,1)),
              ((4,4,0),(3,4,0)),((2,4,1),(3,4,1)),
              ((3,3,1),(3,3,1)),((3,4,1),(3,4,1))]
    for x,y in examples:
        e,r=equivalent(x,y,4)
        assert e == (predicted(4,*x)==predicted(4,*y)),(4,x,y,e)
    print('k=4: ten boundary comparisons: PASS')
    print('VERIFIED')
if __name__=='__main__':main()
