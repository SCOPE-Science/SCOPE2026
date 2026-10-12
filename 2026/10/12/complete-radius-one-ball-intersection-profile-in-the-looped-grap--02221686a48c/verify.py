"""Exact finite test of radius-one node-ball intersections (standard library only).

These checks validate small cases; the theorem for arbitrary n and prime powers
is proved in RESULT.md, not inferred from exhaustive samples.
"""
from itertools import combinations
from collections import defaultdict


def expected(n, q, edges, d):
    support = {e for e, v in zip(edges, d) if v}
    cov1 = [i for i in range(n) if all(i in e for e in support)]
    if not support:
        return 1 + n*(q**n-1) - n*(n-1)//2*(q-1), 0
    if cov1:
        if len(support)==1 and next(iter(support))[0] != next(iter(support))[1]:
            return 2*q**n-q,1
        if len(support)==2 and all(a != b for a,b in support) and len(set().union(*[set(e) for e in support]))==3:
            return q**n + 2*(q-1),1
        return q**n,1
    cov2 = [set(S) for S in combinations(range(n),2)
            if all(set(e) & set(S) for e in support)]
    if cov2:
        c=len(cov2)
        h=sum(len(s&t)==1 for s,t in combinations(cov2,2))
        matching=(len(support)==2 and all(a!=b for a,b in support)
                  and len(set().union(*[set(e) for e in support]))==4)
        return 2*q*c-2*h+2*matching,2
    return 0,3


def run(n,q,full=True,samples=0):
    # Genuine finite-field additive group: XOR for q=2,4, sum modulo 3 for q=3.
    assert q in (2,3,4)
    edges=list(combinations(range(n),2))+[(i,i) for i in range(n)]
    m=len(edges); powers=[q**i for i in range(m)]
    balls=set()
    for v in range(n):
        star=[k for k,e in enumerate(edges) if v in e]
        for w in range(q**n):
            balls.add(sum((w//q**a%q)*powers[k] for a,k in enumerate(star)))
    def add(x,y):
        if q==2: return x^y
        if q==4:
            return sum((((x//p)%4)^((y//p)%4))*p for p in powers)
        return sum((((x//p)+(y//p))%3)*p for p in powers)
    if full:
        # In every support pattern choose unit labels; coordinatewise field
        # scaling makes all nonzero labels isometric to that representative.
        masks=range(1<<m)
    else:
        masks=[(0x9e3779b9*i+i*i*14711)%(1<<m) for i in range(samples)]
    shells=defaultdict(int)
    for mask in masks:
        d=[int(bool(mask>>i&1)) for i in range(m)]
        w=sum(d[i]*powers[i] for i in range(m))
        pred,dist=expected(n,q,edges,d)
        actual=sum(add(w,b) in balls for b in balls)
        if pred != actual:
            raise AssertionError((n,q,mask,edges,pred,actual))
        shells[(dist,actual)] += 1
    print('n=%d q=%d patterns=%d B1=%d distance-overlap-profile=%s' %
          (n,q,len(masks),len(balls),sorted(shells.items())))
    return len(masks)

if __name__ == '__main__':
    checks=0
    for n,q,full,samples in [
        (3,2,True,0),(4,2,True,0),(4,3,True,0),(4,4,True,0),
        (5,2,True,0),(5,3,False,200),(6,2,False,400)]:
        checks+=run(n,q,full,samples)
    print('VERIFY_OK',checks)
