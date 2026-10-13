#!/usr/bin/env python3
"""Exact-rational cross-checks of weighted star-graph sweep certificates.

No random simulation is used to certify the infinite statements.  This script
compares two distinct finite-state first-step recurrences with closed forms.
"""
from fractions import Fraction as Q
from math import factorial


def binom_real(v, k):
    out = Q(1)
    for i in range(1, k + 1):
        out *= Q(v - (i - 1), i)
    return out


def gss_closed(m, w):
    return (binom_real(w + m, m-1) +
            binom_real(w + m - 1, m-1) - 1)


def rk_closed(m, w):
    p = Q(1)
    for r in range(1, m + 1):
        p *= Q(r, 1) / (Q(r, 1) + w)
    return (m + w) / w * (1 / p - 1)


def gss_dp(m, w):
    """Use linear equations T_j for j selected leaves since the last center."""
    # T_m=0, T_j =1+ (w/(w+m-j))*T_0 + (m-j)/(w+m-j)*T_{j+1}
    # j>=1; T_0=1+T_1 (first leaf forced)
    # Represent T_j=a_j+b_j*T_0 in exact rationals.
    a, b = Q(0), Q(0)
    for j in range(m-1, 0, -1):
        den = w + (m - j)
        a, b = 1 + Q(m-j,1)*a/den, (w + Q(m-j,1)*b)/den
    return (1 + a) / (1-b)


def rk_dp(m, w):
    """Fresh iid row sampling; T_m=0; center resets coverage."""
    a, b = Q(0), Q(0)
    for k in range(m-1, -1, -1):
        # (w+m-k)*T_k=(w+m)+(m-k)*T_{k+1}+w*T_0
        den = w + (m - k)
        a, b = (w + m + Q(m-k,1)*a)/den, (w+Q(m-k,1)*b)/den
    return a/(1-b)


def check_source_transition(m):
    # For center label m, star adjacency: center touches every leaf;
    # each leaf touches only center. Algorithm 3 update is (S union N(i))\{i}.
    S = set(range(m))
    for i in range(m):
        assert i in S
        S = (S | {m}) - {i}
    assert S == {m}
    S = (S | set(range(m))) - {m}
    assert S == set(range(m))


def main():
    count = 0
    weights = [Q(1, 4),Q(1,2),Q(1),Q(3,2),Q(2),Q(5)]
    for m in range(2, 11):
        check_source_transition(m)
        for w in weights:
            a,b=gss_closed(m,w),gss_dp(m,w)
            c,d=rk_closed(m,w),rk_dp(m,w)
            assert a == b,(m,w,a,b)
            assert c == d,(m,w,c,d)
            count += 2
        assert gss_closed(m,Q(1)) == Q(m*m+3*m-2,2)
        assert rk_closed(m,Q(1)) == m*(m+1)
        count += 2
    print('PASS',count,'exact closed-form/recurrence equalities;',
          'source transition states checked for m=2..10.')
    for m,w in [(2,Q(1)),(3,Q(1)),(5,Q(1)),(6,Q(1,2)),(10,Q(2))]:
        print('example',m,w,gss_closed(m,w),rk_closed(m,w))

if __name__ == '__main__':
    main()
