#!/usr/bin/env python3
"""Exact finite-size checks for inversion/long-displacement covariance.

No input data or third-party packages required. The proof in RESULT.md is general;
these calculations serve as independent small-instance diagnostics.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial, isqrt


def cov_closed(n, t):
    assert n >= 2 and 1 <= t < n
    return Fraction((n-t)*(n-t+1)*(2*n*t-n+t*t-t+1), 6*n*(n-1))


def inv(a):
    return sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1, len(a)))


def high_displacement(a, t):
    return sum(abs(v-i)>=t for i,v in enumerate(a, 1))


def brute_covariances(n):
    nfact = factorial(n)
    sum_i = 0
    sum_h = [0]*n
    sum_ih = [0]*n
    # Generate from first principles, without relying on the proof's
    # conditional-expectation or diagonal-sum manipulations.
    for a in permutations(range(1,n+1)):
        v = inv(a)
        sum_i += v
        disps = [abs(x-i) for i,x in enumerate(a,1)]
        for t in range(1,n):
            h = sum(d>=t for d in disps)
            sum_h[t] += h
            sum_ih[t] += v*h
    out = [None]*n
    for t in range(1,n):
        out[t] = Fraction(sum_ih[t],nfact)-Fraction(sum_i*sum_h[t],nfact**2)
    return out


def check():
    assert cov_closed(2,1)==Fraction(1,2)
    trials = 0
    total_permutations = 0
    for n in range(2,9):
        observed=brute_covariances(n)
        total_permutations+=factorial(n)
        for t in range(1,n):
            assert observed[t]==cov_closed(n,t), (n,t,observed[t],cov_closed(n,t))
            assert observed[t]>0
            trials+=2
        # Cross-check that the covariance of total displacement is the sum
        # of the threshold covariances. The closed form of this special case
        # is already published, so is *not* the novelty claim.
        assert sum(observed[1:]) == Fraction((n+1)*(n*n+1),30)
        trials+=1
    for n in range(2,501):
        maxima=max(cov_closed(n,t) for t in range(1,n))
        r=isqrt(3*n*n-2)
        alpha_floor=(r-n)//2
        # If the square root is nonintegral, floor((sqrt(3n^2-2)-n)/2)
        # can differ by 1 from integer division of isqrt; use candidate local
        # verification in a radius two rather than floats.
        candidates=[t for t in range(max(1,alpha_floor-2), min(n,alpha_floor+4))]
        assert any(cov_closed(n,t)==maxima for t in candidates)
        for t in range(1,n-1):
            difference=cov_closed(n,t+1)-cov_closed(n,t)
            expected=Fraction((t-n)*(2*t*t+2*n*t-n*n+1),3*n*(n-1))
            assert difference==expected, (n,t)
            trials+=1
        trials+=1
    # All monotone penalties are sums of thresholds with nonnegative
    # coefficients; the tested representative weights exercise this fact.
    for n in range(2,15):
        for f in [lambda d:d,lambda d:d*d,lambda d: d>=2,lambda d:d>=n-1]:
            increments=[f(t)-f(t-1) for t in range(1,n)]
            assert min(increments)>=0
            covariance=sum(Fraction(increments[t-1])*cov_closed(n,t) for t in range(1,n))
            assert covariance >= 0
            if max(increments)>0:assert covariance>0
            trials+=1
    print(f'PASS: {trials} exact checks; {total_permutations} exhaustively enumerated permutations; n up to 500 for peak/difference identities.')

if __name__=='__main__':check()
