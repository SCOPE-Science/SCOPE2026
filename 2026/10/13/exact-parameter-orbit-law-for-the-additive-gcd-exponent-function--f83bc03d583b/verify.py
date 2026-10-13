from math import gcd, lcm
from itertools import product
from collections import Counter

def phi(n):
    r=n
    p=2
    m=n
    while p*p<=m:
        if m%p==0:
            while m%p==0:m//=p
            r-=r//p
        p+=1
    if m>1:r-=r//m
    return r

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def F(k, exps):
    return sum(gcd(k,e) for e in exps)

def predicted_mean_numer(exps,L):
    # L * sum_i sum_{d|e_i} phi(d)/d, evaluated integrally as (L/e_i)*sum_{k=1}^{e_i} gcd(k,e_i)
    return sum((L//e)*sum(gcd(k,e) for k in range(1,e+1)) for e in exps)

cases=0
parameter_checks=0
max_L=0
for r in range(1,5):
    for exps in product(range(1,9), repeat=r):
        L=1
        for e in exps:L=lcm(L,e)
        max_L=max(max_L,L)
        vals=[F(k,exps) for k in range(1,L+1)]
        # projection to gcd(k,L)
        for k,v in enumerate(vals,1):
            assert v==F(gcd(k,L),exps)
            parameter_checks+=1
        # exact minimum and maximum fibers
        assert min(vals)==r
        assert sum(v==r for v in vals)==phi(L)
        assert max(vals)==sum(exps)
        assert sum(v==sum(exps) for v in vals)==1
        # full divisor-weighted distribution
        actual=Counter(vals)
        pred=Counter()
        for d in divisors(L):
            pred[F(d,exps)] += phi(L//d)
        assert actual==pred
        # exact least positive period: no smaller T works
        for T in divisors(L):
            if T==L:continue
            # sufficient to test one full L-block cyclically
            if all(vals[k-1]==vals[(k-1+T)%L] for k in range(1,L+1)):
                raise AssertionError((exps,L,T))
        # first moment identity
        assert sum(vals)==predicted_mean_numer(exps,L)
        cases+=1
print(f'VERIFY_OK exponent_tuples={cases} parameter_checks={parameter_checks} max_L={max_L} support_max=4 exponent_max=8')
