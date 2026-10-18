#!/usr/bin/env python3
"""Independent finite tests of De Morgan congruence support and occupancy identities."""
from itertools import product
from math import factorial, comb
from random import Random

def comp_map(tau, x, n):
    inv=sum(1 << v for v in range(n) if (x >> tau[v]) & 1)
    return ((1 << n)-1) ^ inv

def good_pred(tus, s, n):
    # Exactly no incoming edge to s from outside s.
    return all(((s >> tau[v]) & 1) == 0 for tau in tus for v in range(n) if not ((s >> v) & 1))

def congruence_table(tus,s,n):
    full=(1<<n)-1
    for x in range(full+1):
        for y in range(full+1):
            if ((x^y)&(full^s))==0:
                for tau in tus:
                    if (comp_map(tau,x,n)^comp_map(tau,y,n)) & (full^s):
                        return False
    return True

def zmask(tus,n):
    z=(1<<n)-1
    for tau in tus:
        for u in tau:
            z &= ~(1<<u)
    return z

def check():
    tables=0; tuples=0; bad=0
    for n in (2,3):
        maps=list(product(range(n), repeat=n))
        for r in (1,2):
            for tus in product(maps,repeat=r):
                tuples+=1
                z=zmask(tus,n)
                proper=[]
                for s in range(1<<n):
                    a=good_pred(tus,s,n)
                    b=congruence_table(tus,s,n)
                    assert a==b, ('congruence mismatch',n,r,tus,s)
                    tables+=1
                    if a and s!=(1<<n)-1:proper.append(s)
                target=[s for s in range(1<<n) if s!=(1<<n)-1 and (s&~z)==0]
                if proper != target:
                    bad+=1
            print('ALL_TABLES',n,r,'tuples',len(maps)**r)
    # An exact falling factorial occupancy check from entire function tuples.
    for n,r in [(2,1),(3,1),(3,2)]:
        maps=list(product(range(n),repeat=n))
        zcounts=[zmask(tus,n).bit_count() for tus in product(maps,repeat=r)]
        for k in range(1,n+1):
            empirical=sum(factorial(z)//factorial(z-k) if z>=k else 0 for z in zcounts)
            # (n)_k (1-k/n)^(nr) times n^(nr), as an exact integer.
            predicted=(factorial(n)//factorial(n-k))*(n-k)**(n*r)
            assert empirical==predicted,(n,r,k,empirical,predicted)
        print('OCCUPANCY_EXACT',n,r,'sample_space',len(zcounts))
    rng=Random(321881)
    for n,r in [(12,2),(20,3),(40,4),(80,4)]:
        count_bad=0; trials=160
        for _ in range(trials):
            tus=[tuple(rng.randrange(n) for v in range(n)) for j in range(r)]
            z=zmask(tus,n)
            # For n>20, probe all singleton and random subsets; this is NOT exhaustive.
            trial_masks=range(1<<n) if n<=12 else [0,(1<<n)-1]+[1<<v for v in range(n)]+[rng.getrandbits(n) for i in range(60)]
            if any(good_pred(tus,s,n) and s!=(1<<n)-1 and (s&~z) for s in trial_masks):count_bad+=1
        print('FINITE_SAMPLE',n,r,'bad_trials',count_bad,'out_of',trials)
    print('VERIFY_OK','congruence_tables',tables,'map_tuples',tuples,'finite_bad',bad)

if __name__=='__main__': check()
