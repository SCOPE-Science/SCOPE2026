#!/usr/bin/env python3
"""Exact arithmetic checks of the optimal hook/core coefficient congruences.

The analytic proof, not these bounded tests, establishes all parameter values.
"""

def sigma1(N):
    s = [0] * (N + 1)
    for d in range(1, N + 1):
        for k in range(d, N + 1, d):
            s[k] += d
    return s


def euler_power(exponent, degree, sig=None):
    """Coefficients of prod_{j>=1} (1-x^j)^exponent (exact integers)."""
    if sig is None:
        sig = sigma1(degree)
    coeff = [1]
    for n in range(1, degree + 1):
        numerator = -exponent * sum(sig[k] * coeff[n-k] for k in range(1, n+1))
        assert numerator % n == 0
        coeff.append(numerator // n)
    return coeff


def partition_inverse(degree):
    """Coefficients of 1/prod_{j>=1}(1-x^j), via unlimited coin changes."""
    part = [0] * (degree + 1)
    part[0] = 1
    for j in range(1, degree + 1):
        for n in range(j, degree + 1):
            part[n] += part[n-j]
    return part


def quotient_difference(t, degree):
    sig = sigma1(degree)
    full = euler_power(t*t, degree, sig)
    sparse_base = euler_power(t, degree//t, sig)
    sparse = [0] * (degree + 1)
    for k, c in enumerate(sparse_base):
        sparse[k*t] = c
    num = [a-b for a,b in zip(full, sparse)]
    p = partition_inverse(degree)
    ans = [sum(num[j]*p[n-j] for j in range(n+1)) for n in range(degree+1)]
    # Independent product construction checks (finite degree and small t).
    if t <= 9 and degree <= 85:
        arr = [1] + [0]*degree
        for step in range(1, degree+1):
            for _ in range(t*t - 1):
                for k in range(degree, step-1, -1):
                    arr[k] -= arr[k-step]
        assert arr == euler_power(t*t-1, degree, sig)
        rhs = [sum(sparse[k]*p[n-k] for k in range(n+1)) for n in range(degree+1)]
        assert ans == [a-b for a,b in zip(arr,rhs)]
    return ans


def v_p(n,p):
    if n == 0: return 10**9
    e=0
    while n % p == 0:
        n//=p
        e+=1
    return e


def prime_factors(t):
    ans=[]
    original=t
    for p in range(2, t+1):
        if t%p==0:
            q=t
            a=0
            while q%p==0:
                q//=p
                a+=1
            ans.append((p,a,original//(p**a)))
            while t%p==0:t//=p
        if t==1: break
    return ans


def run():
    checks=0
    for p,a in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2),(7,1)]:
        t=p**a
        N=max(65,p**(a-1)+10)
        f=quotient_difference(t,N)
        assert f[0]==0 and f[1]==-t*t
        assert all(v_p(x,p)>=a+1 for x in f)
        first=p**(a-1)
        assert all(v_p(x,p)>=a+2 for x in f[:first])
        assert f[first] % (p**(a+2)) == (-(p**(a+1))) % (p**(a+2))
        checks += N+1
        print(f'prime_power t={t}: exact modulus p^{a+1}, first failure n={first}: OK')
    for t in [6,10,12,15,18,20,21,30]:
        ff=prime_factors(t)
        degree=max(p**(2*a) for p,a,u in ff)
        f=quotient_difference(t,degree)
        assert f[0]==0 and f[1]==-t*t
        for p,a,u in ff:
            start=p**(2*a)
            assert all(n%p==0 for n in f[:start])
            assert f[start]%p == (-u*u)%p
            checks += start + 1
        print(f'non_prime_power t={t}: all first p-failures and gcd 1: OK')
    print(f'VERIFY_OK comparisons={checks}')

if __name__=='__main__':run()
