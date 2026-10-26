"""Exact finite-field orbit and deck-normalizer cross-checks."""
from itertools import permutations
from collections import Counter

DOUBLE = ((1,0,3,2),(2,3,0,1),(3,2,1,0))

def classes(p):
    reps = {}
    for b in range(1,p):
        for c in range(1,p):
            d = (-1-b-c) % p
            if not d: continue
            a=(1,b,c,d)
            orbit = set()
            for m in range(1,p):
                orbit.add(tuple(sorted(m*x%p for x in a)))
            representative=min(orbit)
            reps[representative]=True
    return sorted(reps)

def lifted_double_permutations(a,p):
    good=[]
    for pi in DOUBLE:
        for m in range(1,p):
            if all(a[pi[i]] == m*a[i]%p for i in range(4)):
                good.append((pi,m))
    return good

def prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**.5)+1))

for p in [3]+[n for n in range(5,42,2) if prime(n)]:
    counts=Counter()
    for rep in classes(p):
        v=len(lifted_double_permutations(rep,p))
        assert v in (0,1,3),(p,rep,v)
        counts[v]+=1
    if p==3:
        assert counts=={3:1}
    else:
        delta=int(p%4==1)
        total=(p*p+6*p+5+12*delta)//24
        assert 24*total==p*p+6*p+5+12*delta
        assert len(classes(p))==total,(p,len(classes(p)),total)
        assert counts[3]==1 and counts[1]==(p-1)//4 and counts[0]==total-1-(p-1)//4,(p,counts)
    print(f'p={p} total={len(classes(p))} normalizer_only_Cp={counts[0]} Dp={counts[1]} Dp_x_C2={counts[3]}')
print('VERIFY_OK orbit_census_and_liftable_Klein_four=all_tested_primes')
