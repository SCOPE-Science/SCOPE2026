#!/usr/bin/env python3
"""Exact finite checks for optimal fair-cube disjoint-occurrence threshold."""
from math import comb, log

count = 0
for n in range(1, 1101):
    N = 1 << n
    c = [comb(n,j) for j in range(n+1)]
    suffix = [0] * (n+2)
    for k in range(n, -1, -1):
        suffix[k] = suffix[k+1] + c[k]
    nums = [suffix[k]**2 - N*(suffix[2*k] if 2*k<=n else 0) for k in range(n+1)]
    k0 = (n+2)//3
    assert nums[k0] == max(nums)
    count += 1
    assert nums.count(nums[k0])==1
    count += 1
    for k in range(n):
        delta = nums[k+1]-nums[k]
        rhs = N*( (c[2*k] if 2*k<=n else 0) + (c[2*k+1] if 2*k+1<=n else 0)) - c[k]*(suffix[k]+suffix[k+1])
        assert delta==rhs
        count+=1
        if k>=1:
            assert (delta>0 if k<k0 else delta<0)
            count+=1
    if n>=4:
        for k in range((n+2)//3+1,n//2):
            a = (n-2*k)*(n-2*k-1)
            den = 2*(2*k+3)*(n-k)
            assert a*6<=den
            count+=1

# Verify the exact three-coin block coupling step for n=3m.
for m in range(1,151):
    n=3*m
    c=[comb(n,j) for j in range(n+1)]
    den=1<<n
    def F(N,j):
        return sum(comb(N,i) for i in range(j,N+1))+sum(comb(N,i) for i in range(j+1,N+1))
    df_numerator=F(n+3,m+1)-8*F(n,m)
    rhs= -c[m+1]+3*c[m]+5*c[m-1]+(c[m-2] if m>=2 else 0)
    assert df_numerator==rhs
    assert rhs>0
    count+=2

# Asymptotic entropy exponent check using a high-precision log-gamma formula
# only as a finite sanity test, not as proof.
from math import lgamma
D=(5/3)*log(2)-log(3)
for n in (150,300,600,900,1100):
    k=(n+2)//3
    # use logsumexp, separately for the rare left and right tails
    def logtail(lo,hi):
        v=[lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)-n*log(2) for j in range(lo,hi+1)]
        t=max(v)
        from math import exp
        return t+log(sum(exp(x-t) for x in v))
    from math import exp
    ell=logtail(0,k-1)
    rrr=logtail(2*k,n) if 2*k<=n else float('-inf')
    lost=2*exp(ell)-exp(2*ell)+exp(rrr)
    assert abs(log(lost)/n+D) < .10
    count+=1

print(f'PASS: {count} exact / corroborating assertions (n=1..1100; symbolic identities evaluated exactly on integer parameters).')
print(f'KL rate: {D:.15f}')
print('The all-n optimizer and exponential limit rely on the written analytical proof, not on these finite tests.')
