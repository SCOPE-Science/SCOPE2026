#!/usr/bin/env python3
"""Independent finite certificates for weight-four binary code puncturing resilience."""
from itertools import combinations
from math import comb, prod


def choose(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def configurations(k):
    for a in range(k+1):
        for b in range(k-a+1):
            for c in range(k-a-b+1):
                d=k-a-b-c
                if sum(z>0 for z in (a,b,c,d)) >= 3:
                    yield (a,b,c,d)


def target_count(v):
    a,b,c,d=v
    return (a*b*(choose(c,2)+choose(d,2)) +
            c*d*(choose(a,2)+choose(b,2)) +
            a*choose(b,3)+b*choose(a,3) +
            c*choose(d,3)+d*choose(c,3))


def triples(v, target):
    return sum(1 for i,j,h in combinations([i for i,num in enumerate(v) for _ in range(num)],3)
               if (i^j^h)==target)


def triple_formula(v,target):
    return choose(v[target],3)+v[target]*sum(choose(v[u],2) for u in range(4) if u!=target) + prod(v[u] for u in range(4) if u!=target)


def parity_inner(x,subset):
    return (x&subset).bit_count()&1


def krawtchouk(k,w):
    return sum((-1)**j*choose(w,j)*choose(k-w,4-j) for j in range(5))


def rank_binary(rows):
    pivots={}
    for row in rows:
        r=row
        while r:
            pivot=r.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=r
                break
            r^=pivots[pivot]
    return len(pivots)


def verify():
    target_expected={6:2,7:6,8:12,9:21}
    for k in range(6,10):
        allv=list(configurations(k))
        values=[target_count(v) for v in allv]
        minval=min(values)
        assert minval == target_expected[k],(k,minval)
        print('BASE',k,'profiles',len(allv),'min',minval)
    for v in configurations(7):
        for target in range(4):
            assert triple_formula(v,target)==triples(v,target)
            assert triples(v,target)>=5,('T_BASE_FAIL',v,target)
    print('TRIPLE_BASE',7,'min',min(triples(v,t) for v in configurations(7) for t in range(4)))
    for k in range(7,23):
        for v in configurations(k):
            for t in range(4):
                assert triple_formula(v,t)>=k-2,(k,v,t)
    print('TRIPLE_RANGE',7,22,'OK')
    for k in range(6,10):
        # Independent Walsh/Krawtchouk count for every independent ordered message pair.
        N=choose(k,4)
        kw=[krawtchouk(k,w) for w in range(k+1)]
        full=(1<<k)-1
        amin=10**12
        for a in range(1,full):
            wa=kw[a.bit_count()]
            for b in range(1,full):
                if b in (a,full^a):
                    continue
                val=(N+wa-kw[b.bit_count()]-kw[(a^b).bit_count()])//4
                assert val>=target_expected[k],('MASK_FAIL',k,a,b,val)
                amin=min(amin,val)
        assert amin==target_expected[k],(k,amin)
        print('MASKS',k,'min',amin)
    witnesses={6:(3,2,0,1),7:(3,3,0,1),8:(3,3,1,1),9:(1,1,0,7),10:(1,1,0,8)}
    for k,v in witnesses.items():
        assert sum(v)==k
        assert target_count(v)==(target_expected[k] if k<10 else choose(k-2,2))
        vectors=[j for j,m in enumerate(v) for _ in range(m)]
        parity_outputs={u:0 for u in range(4)}
        retained=[]
        for comb4 in combinations(range(k),4):
            t=0; mask=0
            for i in comb4:
                t^=vectors[i];mask|=1<<i
            parity_outputs[t]+=1
            if t!=1:
                retained.append(mask)
        assert parity_outputs[2]>0 and parity_outputs[3]>0, (k,parity_outputs)
        assert rank_binary(retained)==k-1,('DIM',k,rank_binary(retained))
        print('WITNESS',k,'counts',parity_outputs,'remaining_rank',rank_binary(retained))
    print('VERIFY_OK')

if __name__=='__main__': verify()
