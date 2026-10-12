"""Exact finite checks for subset-gcd deficit comparisons and density formulas."""
from math import gcd, lcm, isqrt

N = 1500
mu = [1] * (N + 1)
mu[0] = 0
for p in range(2,N+1):
    if all(p % d for d in range(2,isqrt(p)+1)):
        for k in range(p,N+1,p): mu[k] *= -1
        for k in range(p*p,N+1,p*p): mu[k] = 0

def divs(n):
    return [d for d in range(1,isqrt(n)+1) if n%d==0 for d in (d,n//d)]

def prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))

def rmin(n):
    k=2
    while n%k == 0: k += 1
    return k

def pmin(n):
    return next(p for p in range(2,n+1) if n%p==0 and prime(p))

f=[0]*(N+1)
for n in range(1,N+1):
    f[n]=sum(mu[d]*((1<<(n//d))-1) for d in range(1,n+1) if mu[d])
checks=0
min_lower=999999
for n in range(2,N+1):
    ds=set(divs(n))
    D=sum(f[d] for d in ds)
    Phi=sum(mu[d]*((1<<(n//d))-1) for d in ds)
    A=(1<<n)-D
    B=(1<<n)-Phi
    r=rmin(n); p=pmin(n)
    assert r==next(d for d in range(2,n+2) if n%d), n
    assert prime(r) or (r & (r-1)==0) or any(prime(q) and r==q**a for q in range(2,isqrt(r)+1) for a in range(2,10))
    assert (1<<(n//r))<=A<=(n+1)*(1<<(n//r)),(n,A,r)
    assert (1<<(n//p))<=B<=(n+1)*(1<<(n//p)),(n,B,p)
    if n%2==0:
        assert A*(1<<(n//2))<=B*(n+1)*(1<<(n//3)), n
    else:
        assert A*(n+1)*(1<<(n//3))>=B*(1<<(n//2)), n
    checks+=1


# Fully independent direct subset-gcd enumeration at small sizes.
for n in range(2,17):
    g = [0]*(1<<n)
    direct_D = direct_Phi = 0
    for mask in range(1,1<<n):
        lb = mask & -mask
        elt = lb.bit_length()
        g[mask] = gcd(g[mask ^ lb], elt)
        direct_D += (n % g[mask] == 0)
        direct_Phi += (gcd(g[mask],n) == 1)
    ds = set(divs(n))
    formula_D=sum(f[d] for d in ds)
    formula_Phi=sum(mu[d]*((1<<(n//d))-1) for d in ds)
    assert (direct_D,direct_Phi)==(formula_D,formula_Phi), n

M=200000
l=1
count=0
res=[]
for k in range(2,30):
    old=l;l=lcm(l,k)
    observed=sum(1 for n in range(1,M+1) if rmin(n)==k)
    predicted=M//old-M//l
    assert observed==predicted, (k,observed,predicted)
    if observed: res.append((k,observed,predicted))
    count+=observed
assert count==M, (count,M)

# Exact finite inclusion-exclusion for the least-prime strata.
spf=list(range(M+1))
for p in range(2,isqrt(M)+1):
    if spf[p]==p:
        for v in range(p*p,M+1,p):
            if spf[v]==v: spf[v]=p
for q in (3,5,7,11,13):
    prior=[p for p in range(2,q) if prime(p)]
    predicted=0
    for mask in range(1<<len(prior)):
        t=q
        sign=1
        for j,p in enumerate(prior):
            if mask>>j&1: t*=p; sign=-sign
        predicted+=sign*(M//t)
    observed=sum(1 for n in range(2,M+1) if spf[n]==q)
    assert observed==predicted, (q,observed,predicted)
print('VERIFY_OK', 'exact_subset_counts_n=',N,
      'independent_subset_enumeration_n=',16, 'density_range_n=',M,
      'positive_least_nondivisor_strata=',res, 'covered=',count,
      'least_prime_strata_3_to_13=OK')
