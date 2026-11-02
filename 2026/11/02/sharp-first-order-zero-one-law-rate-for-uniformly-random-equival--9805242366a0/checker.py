"""Exact finite tests for rank-bounded logic on uniform equivalence relations.
Python standard library; run: python3 checker.py
"""
from math import comb, factorial, exp

def bell_and_forbidden(N, forbidden):
    a = [0]*(N+1)
    a[0]=1
    for n in range(1,N+1):
        a[n]=sum(comb(n-1,k-1)*a[n-k] for k in range(1,n+1) if k not in forbidden)
    return a

def integer_partitions(n, lo=1):
    if n==0:
        yield ()
    for k in range(lo,n+1):
        for tail in integer_partitions(n-k,k):
            yield (k,)+tail

N=320
Bell=bell_and_forbidden(N,())
for n in range(0,9):
    total=0
    singleton_hist=[0]*(n+1)
    for p in integer_partitions(n):
        count=factorial(n)
        for size in p: count//=factorial(size)
        # Use exact rational expression in one division; repeated integer division is invalid.
        den=1
        for size in p: den*=factorial(size)
        for size in set(p):den*=factorial(p.count(size))
        count=factorial(n)//den
        total+=count
        singleton_hist[p.count(1)]+=count
    assert total==Bell[n]
    no_single=bell_and_forbidden(n,(1,))
    for t in range(n+1):
        predicted=comb(n,t)*no_single[n-t]
        assert singleton_hist[t]==predicted, (n,t)

no_single=bell_and_forbidden(N,(1,))
for n in (80,160,320):
    assert no_single[n]/Bell[n] > 0
    # Poisson saddle approximation: w = W(n) by monotone bisection.
    low,high=0.0,float(n)
    for _ in range(150):
        mid=(low+high)/2
        if mid*exp(mid)<n:low=mid
        else: high=mid
    w=(low+high)/2
    for t in (0,1,2):
        exact=comb(n,t)*no_single[n-t]/Bell[n]
        approx=exp(-w)*w**t/factorial(t)
        assert abs(exact/approx-1)<0.06, (n,t,exact/approx)
    print(f'n={n} w={w:.6f} p(no singleton)={no_single[n]/Bell[n]:.9f} asymptotic ratio={(no_single[n]/Bell[n])/exp(-w):.7f}')

# Witnesses for all quantifier ranks: an E-structure with r-2 singletons
# fails the rank-r sentence asserting r-1 distinct singleton classes.
for r in range(2,10):
    witness=(1,)*(r-2)+(2,)*r
    assert witness.count(1)==r-2
    rich=(1,)*(r-1)+(2,)*r
    assert rich.count(1)==r-1
print('ALL_CHECKS_OK')
