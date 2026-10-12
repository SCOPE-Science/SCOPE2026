"""Direct finite checks for bounded-run binary bigram profiles."""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def profile(word):
    return tuple(sum((word[i], word[i+1]) == pair for i in range(len(word)-1))
                 for pair in ((0,0), (0,1), (1,0), (1,1)))


def admissible(word, h):
    run = 1
    for i in range(1, len(word)):
        run = run+1 if word[i] == word[i-1] else 1
        if run > h:
            return False
    return True


def bounded_compositions(r, a, h):
    if r == 0:
        return int(a == 0)
    if a < 0 or a > r*(h-1):
        return 0
    dp = [1] + [0]*a
    for _ in range(r):
        nxt = [0]*(a+1)
        for t, v in enumerate(dp):
            if v:
                for v1 in range(h):
                    if t+v1 <= a:
                        nxt[t+v1] += v
        dp = nxt
    return dp[a]


def class_size(p, h):
    a, u, v, b = p
    if abs(u-v) > 1:
        return 0
    m = min(u,v)
    B = lambda r,k: bounded_compositions(r,k,h)
    if u == v:
        return B(m+1,a)*B(m,b) + B(m,a)*B(m+1,b)
    return B(m+1,a)*B(m+1,b)


def gf_coeff(n, h):
    def H(exp, period):
        if n < exp:
            return 0
        k = (n-exp)//period
        return (k+1)*(n-exp+1) - period*k*(k+1)//2
    return (H(1,2) + 2*H(2,2)
            - 2*H(h+1,h+1) - 4*H(h+2,h+1)
            - H(3,2*h) + 2*H(h+2,2*h) + 2*H(2*h+2,2*h))


def representative(p,h):
    a,u,v,b = p
    if abs(u-v) > 1:
        return None
    m = min(u,v)
    def try_start(start):
        if u==v:
            r0,r1 = ((m+1,m) if start==0 else (m,m+1))
        elif u==v+1 and start==0:
            r0=r1=m+1
        elif v==u+1 and start==1:
            r0=r1=m+1
        else:
            return None
        if not (0<=a<=(h-1)*r0 and 0<=b<=(h-1)*r1):
            return None
        rem={0:a,1:b}
        runs=[]
        for j in range(r0+r1):
            bit=(start+j)%2
            extra=min(h-1,rem[bit]); rem[bit]-=extra
            runs.extend([bit]*(1+extra))
        assert rem == {0:0,1:0}
        return tuple(runs)
    out = try_start(0)
    return out if out is not None else try_start(1)


def unique_formula(n):
    if n==1:return 0
    if n==2:return 4
    return (2*(n%2==0)+4*(n%3==0)+2*(n%4==0)
            +2*(n%3==2)+2*(n%4==2))

c=[48,1,44,33,16,17,60,1,32,33,28,17]
for h in range(1,6):
    for n in range(1,18):
        freq=Counter()
        for w in product((0,1),repeat=n):
            if admissible(w,h):
                freq[profile(w)] += 1
        assert len(freq) == gf_coeff(n,h), (h,n,len(freq),gf_coeff(n,h))
        for p,v in freq.items():
            assert v == class_size(p,h), (h,n,p,v,class_size(p,h))
            w=representative(p,h)
            assert w is not None and len(w)==n and admissible(w,h) and profile(w)==p
        if h==2:
            assert len(freq)==(3*n*n+20*n+c[n%12])//24
            assert sum(v==1 for v in freq.values()) == unique_formula(n)
for h in range(1,21):
    for n in range(1,501):
        z=gf_coeff(n,h)
        assert z>=1
        if h==2:
            assert 24*z==3*n*n+20*n+c[n%12]
print('VERIFY_OK brute_h_1_to_5_n_1_to_17; exact_fibers; canonical_representatives; rational_h_1_to_20_n_1_to_500; h2_quasipolynomial_singletons')
