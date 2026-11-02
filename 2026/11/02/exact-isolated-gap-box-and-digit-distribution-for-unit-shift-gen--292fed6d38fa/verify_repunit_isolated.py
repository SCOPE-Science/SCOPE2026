"""Exact bounded checks for a base-repunit semigroup isolated-gap theorem.
Run: python3 verify_repunit_isolated.py
Only Python 3 standard library is required. Finite checks do not prove the theorem.
"""
from collections import Counter
from heapq import heappop, heappush
from itertools import product


def rep(b, j):
    return (b**j - 1) // (b-1)


def apery(gens):
    m=gens[0]
    dist=[None]*m
    dist[0]=0
    q=[(0,0)]
    while q:
        w,r=heappop(q)
        if w!=dist[r]:
            continue
        for a in gens[1:]:
            t=(r+a)%m
            ww=w+a
            if dist[t] is None or ww<dist[t]:
                dist[t]=ww
                heappush(q,(ww,t))
    assert all(x is not None for x in dist)
    return dist


def canonical_heights(b,n):
    ls=list(range(b+1))
    for j in range(3,n+1):
        ls=[u+h for h in range(b) for u in ls]+[b]
    return ls


def claim_isolates(b,n):
    m=rep(b,n)
    base=(b-1)*m+b
    return {base+sum(d*(m+rep(b,j-1)) for j,d in enumerate(ds,3))
            for ds in product(range(b),repeat=n-2)}


def main():
    count=0; sum_gaps=0; sum_iso=0; unique_hist=0
    for b in range(2,7):
        for n in range(2,7):
            m=rep(b,n)
            if m>5000:continue
            gens=[m+rep(b,j-1) for j in range(1,n+1)]
            w=apery(gens)
            heights=canonical_heights(b,n)
            assert len(heights)==m
            assert w==[r+m*heights[r] for r in range(m)],(b,n,'Apéry')
            F=max(w)-m
            def member(x):
                return x>=0 and x>=w[x%m]
            observed={x for x in range(1,F+1)
                        if not member(x) and member(x-1) and member(x+1)}
            proposed=claim_isolates(b,n)
            assert observed==proposed,(b,n,sorted(observed^proposed)[:5])
            assert len(observed)==b**(n-2)
            assert min(observed)==(b-1)*m+b
            assert max(observed)==F
            polys=Counter((x//m)-(b-1) for x in observed)
            expected=Counter({0:1})
            for _ in range(n-2):
                expected=Counter({k:sum(expected[k-d] for d in range(b))
                                  for k in range((n-2)*(b-1)+1)})
            assert polys==expected,(b,n,'polynomial')
            count+=1;sum_gaps+=sum(heights);sum_iso+=len(observed);unique_hist+=len(polys)
    print(f'PASS: {count} complete families; {sum_gaps} gaps classified; '
          f'{sum_iso} isolated gaps; {unique_hist} strata checked')

if __name__=='__main__':main()
