"""Direct finite-instance test of cycle-equivariant idempotent rank law.
No external dependencies; run: python check.py
"""
from collections import Counter
from itertools import product
from math import comb


def cycle_lengths(sigma):
    n=len(sigma); seen=set(); lens=[]
    for i in range(n):
        if i not in seen:
            j=i; k=0
            while j not in seen:
                seen.add(j);j=sigma[j];k+=1
            assert j==i
            lens.append(k)
    return lens


def prediction(n,sigma):
    L=cycle_lengths(sigma);t=len(L); out=Counter()
    for mask in range(1,1<<t):
        J=[j for j in range(t) if mask&(1<<j)]
        for ranks in product(range(1,n+1),repeat=len(J)):
            r={j:rr for j,rr in zip(J,ranks)}
            coeff=1
            for j in J:
                coeff*=comb(n,r[j])*r[j]**(n-r[j])
            for i in range(t):
                if i not in J:
                    coeff*=sum(L[j]*r[j]**n for j in J if L[i]%L[j]==0)
            out[sum(L[j]*r[j] for j in J)]+=coeff
    return +out


def minimum_rank_and_count(n, sigma):
    sizes = Counter(cycle_lengths(sigma))
    minimal = [d for d in sizes if not any(e != d and d % e == 0 for e in sizes)]
    lower = sum(minimal)
    ways = n ** len(minimal)
    for d in minimal:
        ways *= sizes[d] * d ** (sizes[d] - 1)
    for length, multiplicity in sizes.items():
        if length not in minimal:
            ways *= sum(d for d in minimal if length % d == 0) ** multiplicity
    return lower, ways


def brute(n,sigma):
    m=len(sigma); loc=list(product(range(n), repeat=n))
    top=list(product(range(m),repeat=m))
    out=Counter()
    for g in top:
        for F in product(loc,repeat=m):
            # independently construct the actual map on m*n points
            im=[n*g[i]+F[i][a] for i in range(m) for a in range(n)]
            if any(im[im[x]]!=im[x] for x in range(m*n)):
                continue
            if any(im[n*sigma[x//n]+x%n]!=n*sigma[im[x]//n]+im[x]%n for x in range(m*n)):
                continue
            out[len(set(im))]+=1
    return +out


def run():
    tests=[(2,(0,)),(2,(0,1)),(2,(1,0)),(2,(0,1,2)),(2,(1,0,2)),(2,(1,2,0)),
           (2,(0,1,2,3)),(2,(1,0,2,3)),(2,(1,0,3,2)),(2,(1,2,3,0)),
           (3,(0,1)),(3,(1,0)),(3,(0,1,2)),(3,(1,0,2)),(3,(1,2,0))]
    for n,sigma in tests:
        a=brute(n,sigma);b=prediction(n,sigma)
        assert a==b,(n,sigma,a,b)
        low, count = minimum_rank_and_count(n, sigma)
        assert min(a) == low and a[low] == count, (n, sigma, low, count, a)
        print('PASS',n,sigma, 'cycle lengths',cycle_lengths(sigma),'spectrum',dict(sorted(a.items())))
    print('ALL_EXACT_CHECKS_PASSED',len(tests))
if __name__=='__main__':run()
