#!/usr/bin/env python3
"""Finite coefficient checks of a sharp hook-length/core-series congruence.

No finite bound is claimed to prove the all-coefficient theorem.
Uses only Python's standard library and integer arithmetic.
"""
from math import gcd


def prime_factors(n):
    fac = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            fac[d] = a
        d += 1
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    return fac


def divisor_sums(N):
    s = [0] * (N + 1)
    for d in range(1, N + 1):
        for k in range(d, N + 1, d):
            s[k] += d
    return s


def coefficient_pair(t, N):
    """Independent Euler-logarithmic-derivative recurrences for F and C."""
    sigma = divisor_sums(N)
    f = [1] + [0] * N
    c = [1] + [0] * N
    for n in range(1, N + 1):
        rf = -(t*t - 1) * sum(sigma[k]*f[n-k] for k in range(1, n+1))
        rc = sum((sigma[k] - (t*t * sigma[k//t] if k % t == 0 else 0)) * c[n-k]
                 for k in range(1, n+1))
        assert rf % n == 0 and rc % n == 0, (t,n)
        f[n] = rf // n
        c[n] = rc // n
    return f, c


def mul(a,b,N):
    out=[0]*(N+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:N+1-i]):
                out[i+j] += x*y
    return out


def direct_products(t,N):
    """Build both products by coefficient convolution, independent of derivative recurrences."""
    # (1-x^k)^(t*t-1), product over k.
    f=[1]+[0]*N
    from math import comb
    for k in range(1,N+1):
        B=[0]*(N+1)
        for j in range(min(t*t-1,N//k)+1):
            B[j*k]=(-1)**j*comb(t*t-1,j)
        f=mul(f,B,N)
    # C = [prod_k (1-x^(tk))^t]*[prod_k (1-x^k)^(-1)]
    c=[1]+[0]*N
    for k in range(1,N+1):
        if t*k<=N:
            B=[0]*(N+1)
            for j in range(min(t,N//(t*k))+1):
                B[j*t*k]=(-1)**j*comb(t,j)
            c=mul(c,B,N)
    # multiply by the ordinary partition series built via 1/(1-x^k).
    for k in range(1,N+1):
        for n in range(k,N+1):
            c[n]+=c[n-k]
    return f,c


def main():
    t_count=0
    coefficient_checks=0
    first_failure_checks=0
    for t in range(2,41):
        fac=prime_factors(t)
        witness=max((p**(2*a) for p,a in fac.items()), default=0) if len(fac)>1 else t//next(iter(fac))
        N=max(witness+10, 24)
        f,c=coefficient_pair(t,N)
        delta=[x-y for x,y in zip(f,c)]
        assert delta[0]==0 and delta[1]==-t*t
        g=0
        for z in delta:
            g=gcd(g,z)
        if len(fac)==1:
            p,a=next(iter(fac.items()))
            n0=p**(a-1)
            modulus=p**(a+1)
            assert all(v%modulus==0 for v in delta)
            assert all(delta[n]%(p**(a+2))==0 for n in range(n0))
            assert delta[n0]%(p**(a+2))==(-p**(a+1))%(p**(a+2))
            assert g==modulus, (t,g,modulus)
            first_failure_checks += 1
        else:
            assert g==1, (t,g)
            for p,a in fac.items():
                m=t//(p**a)
                n0=p**(2*a)
                assert all(delta[n]%p==0 for n in range(n0)), (t,p,n0)
                assert delta[n0]%p==(-m*m)%p, (t,p,n0)
                first_failure_checks += 1
        t_count += 1
        coefficient_checks += N+1
    comparisons = 0
    for t in range(2,8):
        n=18
        assert coefficient_pair(t,n)==direct_products(t,n),t
        comparisons+=(n+1)*2
    print(f'VERIFY_OK parameters={t_count} coefficients={coefficient_checks} '
          f'first_failure_checks={first_failure_checks} direct_product_coefficient_comparisons={comparisons} '
          f'prime_power_examples=(2,3,4,8,9,16,25,27,32)')

if __name__=='__main__':
    main()
