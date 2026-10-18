#!/usr/bin/env python3
"""Independent finite numerical checks for the discrete heat-semigroup formulas.

Python 3 standard library only. This tests finite identities and asymptotic
consistency; it does not replace proofs of infinite or uniform assertions.
"""
import math
from functools import lru_cache

M = 8192
THETA = tuple(2 * math.pi * j / M for j in range(M))
COS = tuple(math.cos(a) for a in THETA)
TESTS = 0


def check(condition, name):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(name)


@lru_cache(maxsize=200)
def weights(t):
    return tuple(math.exp(2.0 * t * (c - 1.0)) for c in COS)


@lru_cache(maxsize=12000)
def kernel(t, n):
    n = abs(int(n))
    w = weights(float(t))
    return math.fsum(w[j] * math.cos(n * THETA[j]) for j in range(M)) / M


def second(t, n):
    return kernel(t, n - 1) + kernel(t, n + 1) - 2.0 * kernel(t, n)


def candidate(t, m):
    return 4.0 * (kernel(t, m) - kernel(t, m + 1))


def threshold(n):
    left, right = 0.5 * n * n, 0.5 * (n * n + 3)
    check(second(left, n) > 0, 'threshold lower bracket')
    check(second(right, n) < 0, 'threshold upper bracket')
    for _ in range(37):
        mid = (left + right) / 2.0
        if second(mid, n) > 0:
            left = mid
        else:
            right = mid
    return (left + right) / 2.0


def check_heat(t):
    ks = [kernel(t, n) for n in range(0, int(11.0 * math.sqrt(2*t) + 35))]
    check(all(ks[n] > ks[n+1] - 1e-13 for n in range(len(ks)-1)), 'heat radial monotonicity')
    ds = [ks[n-1] + ks[n+1] - 2 * ks[n] for n in range(1,len(ks)-1)]
    check(second(t,0) < 0, 'center negative')
    crosses = [n for n in range(1,len(ds)) if ds[n-1] < -5e-12 and ds[n] > 5e-12]
    # Sign change may occur through a rounded numerical zero.
    negative = [n for n in range(len(ks)-1) if second(t,n)<-1e-10]
    positive = [n for n in range(len(ks)-1) if second(t,n)>1e-10]
    check(bool(negative) and bool(positive), 'both signs occur')
    check(max(negative)<min(positive),'one radial sign transition')
    m=max(range(len(ks)-1),key=lambda j:ks[j]-ks[j+1])
    full = abs(second(t,0))+2 * math.fsum(abs(second(t,n)) for n in range(1,len(ks)-2))
    closed=candidate(t,m)
    check(abs(full-closed)<2e-9+1e-8*closed,'telescoping norm')
    check(all(closed >= candidate(t,n)-5e-12 for n in range(len(ks)-1)), 'finite global max')
    return closed,m


def main():
    check(abs(kernel(0.5,0)-kernel(0.5,-0))<1e-14,'even zero')
    for t in (0.01,0.1,0.7,1.0,2.0,5.0,10.0,25.0,100.0,500.0):
        norm, m = check_heat(t)
        check(0<norm<4.01, 'heat smoothing bound')
        check(m >= 0, 'index')
    last = 0.0
    for n in (1,2,3,4,5,8,10,15,20):
        tn = threshold(n)
        check(tn>last, 'thresholds increasing')
        check(abs((2*tn-n*n)-0.5)<0.2, 'threshold asymptotic enclosure')
        check(abs(second(tn,n))<2e-10, 'threshold root residual')
        last = tn
    C=math.sqrt(2.0/(math.pi*math.e))
    for t in (25.,50.,100.,200.,500.,1000.,3000.,10000.):
        m=max(0,int(math.sqrt(2*t)))
        direct=max(candidate(t,j) for j in range(max(0,m-4),m+5))
        sqrtx=math.sqrt(2*t)
        rho=min(abs(sqrtx-(j+0.5)) for j in range(max(0,m-4),m+5))
        prediction=C/t * (1+(1.0/12.0-rho*rho/2.0)/t)
        check(abs((direct/prediction)-1) < 5/t**1.5, 'second-order oscillatory expansion')
    print('PASS:',TESTS,'finite numerical assertions; no infinite-proof claims')

if __name__=='__main__':main()
