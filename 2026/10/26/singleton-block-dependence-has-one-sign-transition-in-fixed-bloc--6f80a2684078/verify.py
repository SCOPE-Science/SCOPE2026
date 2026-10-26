#!/usr/bin/env python3
"""Standalone exact checker for uniform set-partition singleton/block-size covariance.
No input files, external packages, random seeds, or network needed.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, log


def stirling(max_n):
    s = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    s[0][0] = 1
    for n in range(1, max_n + 1):
        for k in range(1, n + 1):
            s[n][k] = k * s[n - 1][k] + s[n - 1][k - 1]
    return s


def partitions(n):
    """Generate each set partition exactly once as its restricted-growth word."""
    def rec(word, maxlabel):
        if len(word) == n:
            yield tuple(word)
        else:
            for label in range(maxlabel + 2):
                word.append(label)
                yield from rec(word, max(maxlabel, label))
                word.pop()
    yield from rec([0], 0)


def F(s, b, m):
    return Fraction(m * s[m - 1][b - 1], s[m][b])


def covariance(s, n, k, r):
    count = Fraction(comb(n, r) * s[n-r][k-1], s[n][k])
    return count * (F(s, k-1, n-r) - F(s, k, n))


def test_all():
    st = stirling(320)
    total = 0
    cases = 0
    for n in range(4, 10):
        bins = defaultdict(list)
        for word in partitions(n):
            sizes = [word.count(i) for i in range(max(word)+1)]
            k = len(sizes)
            xs = [sizes.count(r) for r in range(n+1)]
            bins[k].append(xs)
            total += 1
        for k in range(3, n-1):
            z = bins[k]
            assert len(z) == st[n][k]
            mean1 = Fraction(sum(t[1] for t in z), len(z))
            assert mean1 == F(st, k, n)
            vals=[]
            for r in range(2, n-k+2):
                meanr = Fraction(sum(t[r] for t in z), len(z))
                mixed = Fraction(sum(t[1]*t[r] for t in z), len(z))
                observed = mixed-mean1*meanr
                predicted=covariance(st,n,k,r)
                assert observed == predicted, (n,k,r, observed,predicted)
                vals.append(F(st,k-1,n-r)-F(st,k,n))
                cases += 1
            assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))
            assert vals[-1] > 0
        print('EXHAUSTIVE_RGS_PASS',n,'partitions',sum(map(len,bins.values())))
    assert total == sum(sum(st[n][k] for k in range(1,n+1)) for n in range(4,10))
    print('EXHAUSTIVE_COVARIANCE_PASS', cases,'conditional covariance cases')
    for k in range(3, 16):
        for n in range(k+2, 321):
            # Exact decreasing expected singleton counts, including all nearby s.
            assert all(F(st,k-1,m)>F(st,k-1,m+1) for m in range(k-1,n-1))
            seq = [F(st,k-1,n-r)-F(st,k,n) for r in range(2,n-k+2)]
            assert all(a < b for a,b in zip(seq,seq[1:]))
            assert seq[-1] > 0
            # Covariance sign equals the sign of the explicit conditional-mean contrast.
            for r in (2,3,(n-k+3)//2,n-k+1):
                if 2 <= r <= n-k+1:
                    cv=covariance(st,n,k,r)
                    assert (cv>0)-(cv<0) == (seq[r-2]>0)-(seq[r-2]<0)
        rho=1-log(k/(k-1))/log((k-1)/(k-2))
        n=300
        signseq=[F(st,k-1,n-r)-F(st,k,n) for r in range(2,n-k+2)]
        sw=min(r for r in range(2,n-k+2) if signseq[r-2]>=0)
        assert abs(sw/n-rho)<0.05, (k,rho,sw/n)
    assert covariance(st,6,3,3)==0
    assert covariance(st,6,3,2)<0 and covariance(st,6,3,4)>0
    print('EXACT_MONOTONICITY_AND_FIXED_K_THRESHOLD_PASS k=3..15 n<=320')
    print('ZERO_COVARIANCE_EXAMPLE_PASS n=6 k=3 r=3')
    print('VERIFY_OK')

if __name__=='__main__':
    test_all()
