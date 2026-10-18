#!/usr/bin/env python3
"""Independent finite checks for the average shortest-absent-subsequence formula.

Scientific definitions use the fixed alphabet {0,1}, including the empty
word and constant words. This verifies finite consequences; the proof of
all lengths is in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict


def is_subsequence(pattern, text):
    j=0
    for c in text:
        if j<len(pattern) and c==pattern[j]:
            j+=1
    return j==len(pattern)


def direct_sas_count(w):
    for k in range(len(w)+2):
        cnt=0
        for u in product('01', repeat=k):
            if not is_subsequence(u,w):
                cnt+=1
        if cnt:
            return cnt
    raise AssertionError('unreachable')


def greedy_index(w):
    k=0
    first=None
    for c in w:
        if first is None:
            first=c
        elif c!=first:
            k+=1
            first=None
    return k


def recurrence(nmax):
    a=[2,2,8]
    while len(a)<=nmax:
        a.append(a[-1]+3*a[-2]-a[-3])
    return a[:nmax+1]


def three_state_counts(nmax):
    # State: 0=fresh, 1=pending target equal to arch symbol,
    # 2=pending target unequal. h=matched prefix minus arches.
    # Multiply each weighted probability by 4 per step.
    dp={(0,0):1}
    result=[]
    for n in range(nmax+1):
        assert all(h>=0 for (_,h) in dp)
        good=sum(v for (state,h),v in dp.items() if h==0)
        result.append(Fraction(2*good,4**n))
        out=defaultdict(int)
        for (s,h),v in dp.items():
            if s==0:
                out[(1,h+1)]+=v
                out[(2,h+1)]+=v
                out[(2,h)]+=2*v
            elif s==1:
                assert h>=1
                out[(0,h-1)]+=4*v
                out[(1,h+1)]+=v
                out[(2,h+1)]+=v
            else:
                out[(0,h)]+=4*v
                out[(2,h)]+=2*v
        dp=out
    return result


def safe_two_state_counts(nmax):
    # Exact zero-surplus paths; weight 4^n is used for comparison.
    # F->B: z/2, B->B:z/2, B->F:z, F->F:z^2/4.
    f=[Fraction(0)]*(nmax+1)
    b=[Fraction(0)]*(nmax+1)
    for n in range(nmax+1):
        # continuations evaluated backward by remaining length
        # F_n = 1(n=0) + B_{n-1}/2 + F_{n-2}/4
        # B_n = 1(n=0) + B_{n-1}/2 + F_{n-1}
        if n==0:
            f[n]=b[n]=Fraction(1)
        else:
            f[n]=(b[n-1]/2)+(f[n-2]/4 if n>=2 else 0)
            b[n]=(b[n-1]/2)+f[n-1]
    return [2*x for x in f]


def main():
    for n in range(15):
        total=0
        for bits in product('01', repeat=n):
            w=''.join(bits)
            cnt=direct_sas_count(w)
            k=greedy_index(w)
            assert cnt==sum(not is_subsequence(''.join(u),w) for u in product('01',repeat=k+1)), (n,w,cnt,k)
            total+=cnt
        expected=recurrence(n)[-1]
        assert total==expected,(n,total,expected)
    gf=recurrence(100)
    three=three_state_counts(100)
    safe=safe_two_state_counts(100)
    for n in range(101):
        target=Fraction(gf[n],2**n)
        assert target==three[n]==safe[n],(n,target,three[n],safe[n])
    print('ALL_CHECKS_PASS direct_all_words_n=0..14 recurrence_n=0..100 three_state_n=0..100 safe_paths_n=0..100')
    print('TOTALS_n_0_to_15',recurrence(15))

if __name__=='__main__':
    main()
