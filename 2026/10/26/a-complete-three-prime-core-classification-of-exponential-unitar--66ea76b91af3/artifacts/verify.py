"""Direct exact-integer checks for a low-support e-unitary perfect classification.

Usage: python3 verify.py
These finite checks corroborate but do not replace the universal proof.
"""
from math import gcd
from itertools import combinations, product


def unitary_exponent_divisors(a):
    return [d for d in range(1, a+1) if a % d == 0 and gcd(d, a // d) == 1]


def local_sum(p,a):
    return sum(pow(p,d) for d in unitary_exponent_divisors(a))


def check_factorization(fac):
    n=1; s=1
    for p,a in fac:
        n*=pow(p,a)
        s*=local_sum(p,a)
    return s==2*n


def sieve_spf(N):
    spf=list(range(N+1))
    for i in range(2,int(N**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,N+1,i):
                if spf[j]==j: spf[j]=i
    return spf


def factor(n,spf):
    f=[]
    while n>1:
        p=spf[n]; a=0
        while n%p==0: n//=p; a+=1
        f.append((p,a))
    return f


def run():
    P=[2,3,5,7,11,13,17,19,23]
    known={36,1800,2700}
    triples_checked=0
    for k in range(1,4):
        for ps in combinations(P,k):
            for aa in product(range(2,14),repeat=k):
                fac=tuple(zip(ps,aa))
                n=1
                for p,a in fac: n*=p**a
                assert check_factorization(fac)==(n in known), (fac,n)
                triples_checked+=1
    lemma_checks=0
    for p in P:
        for a in range(3,301):
            z=local_sum(p,a)
            assert (z-p**a)*p*p<=p**a,(p,a)
            assert (z-p**a)*p*p==p**a if a==3 else (z-p**a)*p*p<p**a
            lemma_checks+=1
    N=500000
    spf=sieve_spf(N)
    observed=set()
    count=0
    for n in range(2,N+1):
        fac=factor(n,spf)
        if check_factorization(fac):
            count+=1
            core=1
            for p,a in fac:
                if a>=2: core*=p**a
            assert core in known, (n,core)
            observed.add(core)
    assert observed==known,observed
    print('VERIFY_OK direct_full_interval_N={} perfect_count={} cores={} exact_powerful_parameter_cases={} local_inequalities_checked={}'.format(N,count,sorted(observed),triples_checked,lemma_checks))


if __name__=='__main__':
    run()
