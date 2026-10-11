"""Reproducible finite numerical checks for the quadratic mixed norm theorem.

The analytic argument proves the theorem. Random samples here cannot certify
universal inequalities and are included only as sanity checks.
"""
from math import sqrt
from random import Random


def sqnorm(x, t):
    return max(abs(v) for v in x)**2 + t * sum(abs(v) for v in x)**2


def bounds(n, t):
    hi = (1+n*t+sqrt((1+n*t)**2-4*(n-1)*t))/2
    low = min(1/k +t*k for k in range(1,n+1))
    return low, hi


def run():
    rng = Random(2931)
    checks=0
    for n in (3,4,5,8,16,25):
        for t in (0.02, 0.05, 0.1, 1/n, 0.23, 0.5, 1.0, 3.0):
            lo, hi = bounds(n,t)
            k = min(range(1,n+1), key=lambda j: 1/j+t*j)
            xlo = [1/sqrt(k)]*k+[0.0]*(n-k)
            assert abs(sqnorm(xlo,t)-lo) < 2e-12
            # Positive eigenvector of the rank-two matrix
            a = hi/(hi-1)
            xhi = [a] + [1.0]*(n-1)
            L = sqrt(sum(v*v for v in xhi))
            xhi = [v/L for v in xhi]
            assert abs(sqnorm(xhi,t)-hi) < 2e-10, (n,t,sqnorm(xhi,t),hi)
            for _ in range(1500):
                x = [rng.uniform(-1,1) for _ in range(n)]
                L = sqrt(sum(v*v for v in x))
                v = sqnorm([z/L for z in x],t)
                assert lo-1e-10<=v<=hi+1e-10, (n,t,v,lo,hi)
                checks+=1
    for n in (16,100,1000,10000):
        t=1/n
        lo,hi=bounds(n,t)
        value=sqrt(hi/lo)/n**0.25
        print('n=%d tuned_ratio=%.12f limit=%.12f'%(n,value,1/sqrt(2)))
    print('PASS %d deterministic samples and %d analytic extremizer cases'%(checks,6*8))

if __name__=='__main__':
    run()
