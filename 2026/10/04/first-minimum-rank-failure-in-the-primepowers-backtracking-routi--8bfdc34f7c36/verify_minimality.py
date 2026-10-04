from functools import lru_cache

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def is_prime_power(n):
    if n < 4: return False
    p=2
    while p*p<=n:
        if is_prime(p):
            v=p*p
            while v<=n:
                if v==n: return True
                v*=p
        p += 1
    return False

def source_dfs(n,max_terms=5,path=()):
    if n==0:
        return path if len(path)>=2 else None
    if len(path)>=max_terms:
        return None
    start=min(n,path[-1] if path else n)
    for m in range(start,3,-1):
        if is_prime_power(m):
            r=source_dfs(n-m,max_terms,path+(m,))
            if r:
                return r
    return None

def pps_upto(N):
    return [n for n in range(4,N+1) if is_prime_power(n)]

def min_rep(n,max_terms=5):
    A=pps_upto(n)
    aset=set(A)
    # exact k-term nonincreasing search, increasing k
    @lru_cache(None)
    def rec(rem,k,maxv):
        if k==0:
            return () if rem==0 else None
        for a in reversed(A):
            if a>maxv or a>rem: continue
            z=rec(rem-a,k-1,a)
            if z is not None:
                return (a,)+z
        return None
    for k in range(2,max_terms+1):
        z=rec(n,k,n)
        if z is not None:
            return z
    return None

for n in range(24,50):
    s=source_dfs(n); m=min_rep(n)
    assert s is not None and m is not None
    assert len(s)==len(m),(n,s,m)
s=source_dfs(50); m=min_rep(50)
assert s==(32,9,9),s
assert m==(25,25),m
assert sum(s)==50 and sum(m)==50
# paper's printed five-term example has a four-term representation
alt=(659**2,5**7,2**7,2**4)
assert alt==(434281,78125,128,16)
assert sum(alt)==512550
assert all(is_prime_power(x) for x in alt)
print('VERIFY_OK first_mismatch=50 source=(32,9,9) minimum=(25,25) alt_512550=',alt)
