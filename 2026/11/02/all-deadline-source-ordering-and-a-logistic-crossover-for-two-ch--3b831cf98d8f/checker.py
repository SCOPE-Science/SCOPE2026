"""Finite exact checks for a two-choice walk on complete bipartite graphs.
No finite check is used as a substitute for the all-order arguments.
Run: python3 checker.py
"""
from fractions import Fraction
from functools import lru_cache
from math import log, e

checks = 0

@lru_cache(None)
def coupon_cdf(m, t):
    if t < 0:
        return Fraction(0)
    dist = [Fraction(1)] + [Fraction(0)] * m
    for _ in range(t):
        nxt = [Fraction(0)] * (m + 1)
        for k, pk in enumerate(dist):
            if not pk:
                continue
            if k == m:
                nxt[k] += pk
                continue
            success = Fraction(m*m-k*k, m*m)
            nxt[k] += pk*(1-success)
            nxt[k+1] += pk*success
        dist = nxt
    return dist[m]

def harmonic(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction(0))

def coupon_mean(m):
    return sum((Fraction(m*m, r*(2*m-r)) for r in range(1,m+1)), Fraction(0))

def exact_optimal_deadline(a,b,deadline, start_A=True):
    # Exhaustive Bellman maximisation on the visited-label state space;
    # unlike the product formula, this allows every possible adaptive choice.
    @lru_cache(None)
    def value(va,vb,side,remaining):
        if va == (1<<a)-1 and vb == (1<<b)-1:
            return Fraction(1)
        if remaining == 0:
            return Fraction(0)
        degree = b if side == 0 else a
        total = Fraction(0)
        for u in range(degree):
            for w in range(degree):
                if side == 0:
                    x = value(va, vb | (1<<u),1,remaining-1)
                    y = value(va, vb | (1<<w),1,remaining-1)
                else:
                    x = value(va | (1<<u), vb,0,remaining-1)
                    y = value(va | (1<<w), vb,0,remaining-1)
                total += max(x,y)
        return total/(degree*degree)
    return value(1,0,0,deadline) if start_A else value(0,1,1,deadline)

def product_deadline(a,b,deadline,start_A=True):
    t = deadline//2
    if start_A:
        return coupon_cdf(a,t+1)*coupon_cdf(b,t+(deadline%2))
    return coupon_cdf(b,t+1)*coupon_cdf(a,t+(deadline%2))

# Exact harmonic evaluation of the one-part coupon mean.
for m in range(1,31):
    assert coupon_mean(m) == Fraction(m,2)*harmonic(2*m-1)+Fraction(1,2)
    checks += 1

# Independent full-state Bellman recursion versus exact two-collector product,
# for both initial sides and every reachable/unreachable short horizon.
for a in range(1,5):
    for b in range(1,5):
        for d in range(0,19):
            for side in (True,False):
                exact = exact_optimal_deadline(a,b,d,side)
                via_collector = product_deadline(a,b,d,side)
                assert exact == via_collector,(a,b,d,side,exact,via_collector)
                checks += 1

# Log-concavity of the exact one-part coupon completion CDF, and its
# reverse-hazard comparison as the number of coupon types grows.
for m in range(1,10):
    for t in range(m,60):
        fprev,fnow,fnext = (coupon_cdf(m,t-1),coupon_cdf(m,t),coupon_cdf(m,t+1))
        assert fnow*fnow >= fprev*fnext
        checks += 1
for a in range(1,10):
    for b in range(1,a):
        for t in range(0,60):
            assert coupon_cdf(a,t+1)*coupon_cdf(b,t) >= coupon_cdf(a,t)*coupon_cdf(b,t+1)
            checks += 1

# The geometric splitting identity in the source-order proof, checked as a
# rational generating-function coefficient identity at sample arguments.
for m in range(1,14):
    for r in range(1,m+1):
        p = Fraction(r*(2*m-r),m*m)
        p2 = Fraction(r*(2*(m+1)-r),(m+1)*(m+1))
        assert 0 < p2 <= p <= 1
        z0 = p2/p
        for k in range(1,16):
            z=[z0]+[z0*(p-p2)*(1-p2)**(j-1) for j in range(1,k+1)]
            convolution=sum(p*(1-p)**(j-1)*z[k-j] for j in range(1,k+1))
            target=p2*(1-p2)**(k-1)
            assert convolution==target,(m,r,k)
            checks += 1

# The centering constant is independently fixed by the harmonic sum.
GAMMA=0.5772156649015329
for m,tol in [(100,0.02),(1000,0.004),(5000,0.001)]:
    value=float(2*coupon_mean(m)/m)-log(m)
    assert abs(value-(log(2)+GAMMA))<tol,(m,value)
    checks+=1

print('PASS:',checks,'exact rational assertions and asymptotic mean diagnostics')
