#!/usr/bin/env python3
"""Independent direct recovery-pair enumeration for binary punctured-simplex codes."""
from collections import Counter
from itertools import product
import random


def span(vs):
    a={0}
    for x in vs: a |= {v^x for v in tuple(a)}
    return a


def rank(vs):
    row={}
    for x in vs:
        while x:
            p=x.bit_length()-1
            if p in row:x ^= row[p]
            else:row[p]=x;break
    return len(row)


def canonical(k,u,r):
    t=u-r
    assert 0<=r<=u and 2*u+t<=k
    a=[1<<i for i in range(u)]
    b=[1<<(u+i) for i in range(u)]
    c=[1<<(2*u+i) for i in range(t)]
    U=(span(a),span(b),span([a[i]^b[i] for i in range(r)]+c))
    assert len(set.union(*map(set,U))) == 1+3*(2**u-1)
    assert all(len(U[i]&U[j])==1 for i in range(3) for j in range(i+1,3))
    return U


def spectrum_brute(k,U):
    S=set(range(1,2**k))-set.union(*map(set,U))
    hist=Counter()
    for v in S:
        pairs={(min(x,x^v),max(x,x^v)) for x in S if x^v in S}
        # This also checks pair-disjointness (each helper appears once).
        helpers=[x for p in pairs for x in p]
        assert len(helpers)==len(set(helpers))
        hist[len(pairs)]+=1
    return hist, S


def spectrum_pred(k,u,r):
    t=u-r;d=3*u-r
    base=2**(k-1)-1-3*(2**u-1)
    j0=2**k-2**d+2**(2*r)*(2**t-1)**3
    j1=3*2**(2*r)*(2**t-1)**2
    j2=3*2**r*(2**r-1)*(2**t-1)
    j3=(2**r-1)*(2**r-2)
    return Counter({base+j:num for j,num in enumerate((j0,j1,j2,j3)) if num})


def map_GL(k, U, seed):
    rand=random.Random(seed)
    while True:
        b=[rand.randrange(1,2**k) for _ in range(k)]
        if rank(b)==k:break
    def apply(x):
        out=0
        for i,v in enumerate(b):
            if x>>i&1:out^=v
        return out
    return tuple({apply(x) for x in z} for z in U)


def main():
    cases=0
    for u in [2,3]:
        for r in range(u+1):
            for k in range(3*u-r,min(3*u-r+2,10)):
                if 2**(k-1)<=3*(2**u-1):continue
                for seed in (None,0,13):
                    U=canonical(k,u,r)
                    if seed is not None:U=map_GL(k,U,seed)
                    got,S=spectrum_brute(k,U)
                    want=spectrum_pred(k,u,r)
                    assert got==want,(k,u,r,seed,got,want)
                    assert sum(got.values())==2**k-1-3*(2**u-1)
                    cases+=1
                    print(f'PASS k={k} u={u} r={r} seed={seed} n={len(S)} hist={dict(sorted(got.items()))}')
    # Two specific optimal [22,5,10] generator column sets, inequivalent by availability.
    A,_=spectrum_brute(5,canonical(5,2,2))
    B,_=spectrum_brute(5,canonical(5,2,1))
    assert A==Counter({6:16,9:6})
    assert B==Counter({6:4,7:12,8:6})
    assert A!=B
    for r0 in (1,2):
        _,columns=spectrum_brute(5,canonical(5,2,r0))
        weights=[sum((w & v).bit_count()%2 for v in columns) for w in range(1,32)]
        assert min(weights)==10
        assert rank(columns)==5
    print('DISTANCE_EXAMPLES_OK k=5 u=2 r=1,2: [22,5,10]')
    print(f'RECOVERY_SPECTRA_OK {cases} exact tests')

if __name__=='__main__':main()
