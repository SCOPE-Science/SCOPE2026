"""Exact finite verification of component-size factorial covariance thresholds.

Python standard library only. No finite check replaces the analytic inequality.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def component_counts(n, edges, mask):
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            a, b = root(u), root(v)
            if a != b:
                parent[a] = b
    sizes = Counter(root(v) for v in range(n))
    return Counter(sizes.values())


def connected_probabilities(n, p):
    q = 1-p
    k = [Fraction(0)] * (n+1)
    k[1] = Fraction(1)
    for m in range(2, n+1):
        k[m] = 1 - sum((comb(m-1,j-1) * k[j] * q**(j*(m-j))
                         for j in range(1,m)), Fraction(0))
    return k


def predicted(n, p):
    q = 1-p
    k = connected_probabilities(n,p)
    mu = {a: comb(n,a)*k[a]*q**(a*(n-a)) for a in range(1,n+1)}
    output = {}
    for a in range(1,n+1):
        for b in range(1,n+1):
            r = Fraction(comb(n-a,b),comb(n,b)) if a+b<=n else 0
            output[a,b] = mu[a]*mu[b] * (r*q**(-a*b)-1)
    return mu, output


def brute(n,p):
    edges=list(combinations(range(n),2))
    e=len(edges)
    powers_p = [p**k for k in range(e+1)]
    powers_q = [(1-p)**k for k in range(e+1)]
    mu = {a:Fraction(0) for a in range(1,n+1)}
    mom = {(a,b):Fraction(0) for a in range(1,n+1) for b in range(1,n+1)}
    for mask in range(1<<e):
        num_edges=mask.bit_count()
        weight=powers_p[num_edges]*powers_q[e-num_edges]
        c=component_counts(n,edges,mask)
        for a in range(1,n+1):
            mu[a] += weight*c[a]
            for b in range(1,n+1):
                mom[a,b] += weight*c[a]*(c[b]-(a==b))
    return mu,{ab:v-mu[ab[0]]*mu[ab[1]] for ab,v in mom.items()}


def threshold_ratio(n,a,b):
    return Fraction(comb(n-a,b),comb(n,b))


def threshold_less(n,a,b,c,d):
    r=threshold_ratio(n,a,b)
    s=threshold_ratio(n,c,d)
    return r**(c*d)>s**(a*b)


def verify():
    for n in range(2,7):
        for p in (Fraction(1,5),Fraction(2,5),Fraction(4,5)):
            brute_means,brute_cov=brute(n,p)
            means,cov=predicted(n,p)
            assert brute_means == means, (n,p,'means')
            assert brute_cov == cov, (n,p,'cumulants')
        print('EXHAUSTIVE_SECOND_FACTORIAL_MOMENTS_PASS n=',n)
    for n in range(3,81):
        assert all(threshold_less(n,1,1,a,b) for a in range(1,n+1) for b in range(1,n+1) if a+b<=n and (a,b)!=(1,1))
        assert all(threshold_less(n,a,b,1,n-1) for a in range(1,n+1) for b in range(1,n+1) if a+b<=n and (a,b) not in ((1,n-1),(n-1,1)))
        for s in range(4,n+1):
            for a in range(1,s//2):
                # More imbalanced (a,s-a) has larger threshold than (a+1,s-a-1).
                assert threshold_less(n,a+1,s-a-1,a,s-a), (n,s,a)
    print('EXACT_STRICT_BALANCE_AND_GLOBAL_THRESHOLD_ORDER_PASS n<=80')
    n,p=5,Fraction(13,40)
    _,vals=predicted(n,p)
    assert vals[2,3]>0 and vals[1,4]<0
    br,_=brute(n,p)
    print('COEXISTING_COVARIANCE_SIGNS_PASS n=5 p=13/40')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
