#!/usr/bin/env python3
"""Exact finite checks for covariance of disjoint richness samples."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json


def fall(a, k):
    z = 1
    for j in range(k):
        z *= (a-j)
    return z


def choose(a, k):
    return comb(a,k) if (a >= 0 and 0 <= k <= a) else 0


def compositions(n, lo=1):
    if n == 0:
        yield ()
    else:
        for a in range(lo, n+1):
            for rest in compositions(n-a,a):
                yield (a,)+rest


def by_formula(abunds, m, n):
    N = sum(abunds)
    if m < 1 or n < 1 or m+n > N:
        raise ValueError('invalid sample sizes')
    mu = [Fraction(choose(N-a,m),choose(N,m)) for a in abunds]
    nu = [Fraction(choose(N-a,n),choose(N,n)) for a in abunds]
    tot = Fraction(0)
    denom = choose(N,m)*choose(N-m,n)
    for i,a in enumerate(abunds):
        for j,b in enumerate(abunds):
            if i == j:
                joint = Fraction(choose(N-a,m+n),choose(N,m+n))
            else:
                numerator = sum(choose(b,u)*choose(N-a-b,m-u)*choose(N-m-b+u,n) for u in range(m+1))
                joint = Fraction(numerator,denom)
            tot += joint-mu[i]*nu[j]
    return tot


def by_pair_formula(abunds):
    N = sum(abunds)
    T2 = sum(fall(a,2) for a in abunds)
    T3 = sum(fall(a,3) for a in abunds)
    return Fraction((4*N-6)*T2*T2-fall(N,2)*(4*T3+2*T2),fall(N,2)*fall(N,4))


def brute(abunds,m,n):
    labels = []
    for i,a in enumerate(abunds):
        labels += [i]*a
    N=len(labels)
    pool=set(range(N))
    Sx=Sy=Sxy=cnt=0
    for A in combinations(range(N),m):
        x=len({labels[i] for i in A})
        for B in combinations(sorted(pool-set(A)),n):
            y=len({labels[i] for i in B})
            Sx += x; Sy += y; Sxy += x*y; cnt += 1
    return Fraction(Sxy*cnt-Sx*Sy,cnt**2)


def main():
    counts=Counter(); first_examples={}
    for N in range(4,9):
        for a in compositions(N):
            exact=by_pair_formula(a)
            assert by_formula(a,2,2)==exact
            assert brute(a,2,2)==exact
            counts['pair_profiles']+=1
            counts['pair_cases_'+str(N)]+=1
            counts['pair_sign_'+str((exact>0)-(exact<0))]+=1
    for N in range(2,8):
        for a in compositions(N):
            for m in range(1,N):
                for n in range(1,N-m+1):
                    assert by_formula(a,m,n)==brute(a,m,n),(a,m,n)
                    counts['general_cases']+=1
    for N in range(4,101):
        for d in range(0,N//2+1):
            a=[2]*d+[1]*(N-2*d)
            C=by_pair_formula(a)
            criterion=0 if d==0 else ((d*(4*N-6)>N*(N-1))-(d*(4*N-6)<N*(N-1)))
            assert (C>0)-(C<0)==criterion
            counts['singleton_doubleton_phase_checks']+=1
    assert by_pair_formula([2,2])==Fraction(2,9)
    assert by_pair_formula([3,1])==Fraction(-1,4)
    assert by_pair_formula([2,1,1])==Fraction(-1,36)
    assert by_pair_formula([2,2,2])==Fraction(2,75)
    assert by_pair_formula([4,1,1])==Fraction(-7,75)
    for N in range(4,101):
        assert by_pair_formula([2]+[1]*(N-2))<0
        assert by_pair_formula([2]*(N//2)+[1]*(N%2))>0
        counts['all_N_positive_negative_witnesses_checked']+=1
    out={'status':'all_exact_checks_passed','counts':dict(sorted(counts.items())),
         'key_cases':{str(tuple(a)):str(by_pair_formula(a)) for a in ((2,2),(3,1),(2,1,1),(2,2,2),(4,1,1))},
         'scope_note':'Finite checks only: formulas for all N,m,n are proved by exact counting in RESULT.md.'}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
