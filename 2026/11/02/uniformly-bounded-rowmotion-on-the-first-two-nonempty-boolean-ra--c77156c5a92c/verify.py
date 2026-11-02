"""Exact finite checks for rowmotion on the 1-2 rank truncation of the Boolean lattice.

Run: python3 verify.py
The infinite-family proof is in RESULT.md; this program checks finite instances.
"""
from itertools import combinations
from collections import Counter
from math import comb, lcm
import random


def cycle_predictions(n):
    def d(m):
        return sum((-1)**j*comb(m,j)*2**comb(m-j,2) for j in range(m+1))
    def a(m):
        return 2*d(m)-2**comb(m,2)
    two=a(n)//2
    three=1
    five=n
    six=sum(comb(n,m)*a(m) for m in range(4,n))//2
    eight=(sum(comb(n,m)*(2**comb(m,2)-d(m)) for m in range(2,n))-n)//2
    return {2:two,3:three,5:five,6:six,8:eight}


def verify(n):
    E=list(combinations(range(n),2))
    em=[sum(1<<i for i,(u,v) in enumerate(E) if mask&(1<<u) and mask&(1<<v))
        for mask in range(1<<n)]
    incidence=[(1<<u)|(1<<v) for u,v in E]
    ideals=[]
    for a in range(1<<n):
        t=em[a]
        while True:
            ideals.append((a,t))
            if not t:break
            t=(t-1)&em[a]
    idx={state:i for i,state in enumerate(ideals)}
    assert len(idx)==len(ideals)
    succ=[]
    for a,b in ideals:
        newedges=em[a]&~b
        endpoints=0
        t=newedges
        while t:
            lo=t&-t
            endpoints|=incidence[lo.bit_length()-1]
            t^=lo
        newvertices=((1<<n)-1)^a | endpoints
        succ.append(idx[(newvertices,newedges)])
    assert len(set(succ))==len(succ)
    seen=bytearray(len(ideals))
    hist=Counter()
    for i in range(len(ideals)):
        if seen[i]:continue
        j=i; p=0
        while not seen[j]:
            seen[j]=1
            j=succ[j];p+=1
        assert j==i
        hist[p]+=1
    pred=cycle_predictions(n)
    assert dict(hist)=={k:v for k,v in pred.items() if v}
    assert len(ideals)==sum(comb(n,k)*2**comb(k,2) for k in range(n+1))
    order=lcm(*(p for p in hist))
    assert order==(15 if n==3 else 120)
    print(f'CHECK_OK n={n} states={len(ideals)} periods={dict(sorted(hist.items()))} order={order}')


def sampled_long_n(n, samples=100):
    # Independent of the finite-state cycle lookup: verify 120-step identity.
    E=list(combinations(range(n),2))
    vertices=[(1<<u)|(1<<v) for u,v in E]
    rng=random.Random(7000+n)
    for _ in range(samples):
        a=rng.getrandbits(n)
        allowed=[i for i,(u,v) in enumerate(E) if ((a>>u)&1) and ((a>>v)&1)]
        b=0
        for i in allowed:
            if rng.randrange(2): b|=1<<i
        start=(a,b)
        for _ in range(120):
            f=0;endpoints=0
            for i,(u,v) in enumerate(E):
                if ((a>>u)&1) and ((a>>v)&1) and not ((b>>i)&1):
                    f|=1<<i;endpoints|=vertices[i]
            a,b=(((1<<n)-1)^a)|endpoints,f
        assert (a,b)==start
    print(f'SAMPLE_OK n={n} samples={samples} iterations_per_sample=120')

if __name__=='__main__':
    for n in range(3,7):verify(n)
    for n in (8,12,25):sampled_long_n(n,100)
    print('ALL_VERIFY_OK')
