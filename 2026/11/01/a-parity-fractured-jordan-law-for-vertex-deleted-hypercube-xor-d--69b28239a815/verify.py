#!/usr/bin/env python3
"""Independent finite-dimensional checks for GF(2^s) XOR dynamics on vertex-deleted hypercubes.
Only coefficients 0 and 1 occur, so GF(2^s) addition is coordinatewise XOR.
"""
import random
from collections import Counter

def rows_for(d):
    N=1<<d
    return [sum(1<<( (u^(1<<k))-1) for k in range(d) if (u^(1<<k))!=0) for u in range(1,N)]

def mul(A,B):
    ans=[]
    for row in A:
        t=0
        while row:
            b=row & -row; idx=b.bit_length()-1
            t^=B[idx]
            row-=b
        ans.append(t)
    return ans

def rank(rows):
    piv={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i]
            else:piv[i]=v;break
    return len(piv)

def action(rows,conf,q):
    o=[]
    for r in rows:
        v=0
        while r:
            a=r&-r;r-=a
            v^=conf[a.bit_length()-1]
        o.append(v)
    return tuple(o)

def classify(rows,conf,q):
    seen={};t=0;cur=tuple(conf)
    while cur not in seen:
        if t>20:raise AssertionError('Exceeded bound')
        seen[cur]=t;cur=action(rows,cur,q);t+=1
    return seen[cur], t-seen[cur]

def run():
    rng=random.Random(606)
    test_ranks=0;countstates=0
    for d in range(2,9):
        A=rows_for(d);N=1<<d;n=N-1
        I=[1<<i for i in range(n)]
        A2=mul(A,A);A3=mul(A2,A)
        if d%2==0:
            assert rank(A)==N//2
            assert rank(A2)==1
            assert all(x==0 for x in A3)
        else:
            assert rank(A)==N-2
            assert A3==A
            assert rank(A2)==N-2
            assert rank([A[i]^I[i] for i in range(n)])==N//2
        test_ranks+=1
        cases=[(2,65536)]
        if d in [2,3]:cases.append((4,65536))
        for q,cap in cases:
            total=q**n
            if total<=cap:
                from itertools import product
                data=list(product(range(q),repeat=n))
            else:
                data=[tuple(rng.randrange(q) for _ in range(n)) for _ in range(500)]
            observed=Counter()
            for s in data:
                t,p=classify(A,s,q);observed[(t,p)]+=1
                assert t<= (3 if d%2==0 else 1)
                assert p in (1,2) if d%2 else p==1
            countstates+=len(data)
            if total<=cap:
                if d%2==0:
                    K=[1,q**(N//2-1),q**(N-2),q**(N-1)]
                    expected={(0,1):K[0],(1,1):K[1]-K[0],(2,1):K[2]-K[1],(3,1):K[3]-K[2]}
                else:
                    f=q**(N//2-1);per=q**(N-2)
                    expected={(0,1):f,(0,2):per-f,(1,1):(q-1)*f,(1,2):(q-1)*(per-f)}
                assert all(observed.get(k,0)==v for k,v in expected.items()),(d,q,observed,expected)
            print(f'd={d}, q={q}, rank(A)={rank(A)}, rank(A^2)={rank(A2)}, states={len(data)}, distributions={dict(sorted(observed.items()))}')
    print(f'PUNCTURED_HYPERCUBE_GF2_RANK_AND_STATE_CHECKS_PASSED: {test_ranks} dimensions, {countstates} states')

if __name__=='__main__':run()
