#!/usr/bin/env python3
"""Independent finite checks of the circular antisquare theorem.
No third-party packages. This is a finite consistency checker, not an infinite proof.
"""
from collections import Counter
from itertools import product
from math import comb

def is_good(w):
    n=len(w)
    # Any longer antisquare in an n-periodic infinite word implies
    # an antisquare whose order is between 2 and n+1.
    for order in range(2,n+2):
        for start in range(n):
            if all(w[(start+j)%n]!=w[(start+j+order)%n] for j in range(order)):
                return False
    return True

def admissible_differences(w):
    n=len(w)
    p=''.join(str(int(w[i]!=w[(i+1)%n])) for i in range(n))
    for f in ('010','101','11111','01110'):
        for i in range(n):
            if ''.join(p[(i+j)%n] for j in range(len(f)))==f:
                return False
    return True

def bivariate_formula(n):
    out=Counter({0:2})
    for r in range(1,n+1):
        for s in range(r+1):
            changes=2*r+2*s
            slack=n-changes-2*r
            if slack < 0:continue
            # n/r * choose(r,s) * number of compositions of zeros into r runs >=2
            num=2*n*comb(r,s)*comb(slack+r-1,r-1)
            assert num%r==0
            out[changes]+=num//r
    return +out

def rational_recurrence(N):
    c=[Counter() for _ in range(N+1)]
    for n in range(1,N+1):
        for shift,delta in ((1,0),(4,2),(6,4)):
            if n>=shift:
                for t,v in c[n-shift].items():c[n][t+delta]+=v
        if n==1:c[n][0]+=2
        if n==4:c[n][2]+=8
        if n==6:c[n][4]+=12
    return c

def trace_check(N, formula):
    states=[''.join(a) for a in product('01',repeat=4)]
    f=('010','101','11111','01110')
    edges=[[] for _ in states]
    for i,s in enumerate(states):
        for bit in '01':
            t=s+bit
            if any(t.endswith(y) for y in f):continue
            edges[i].append((states.index(t[-4:]),int(bit)))
    # Enumerate closed directed walks of length n, with weight = number of 1s.
    hist=[Counter() for _ in range(N+1)]
    for origin in range(len(states)):
        dp=[Counter() for _ in states]
        dp[origin][0]=1
        for n in range(1,N+1):
            nxt=[Counter() for _ in states]
            for i in range(len(states)):
                for j,b in edges[i]:
                    for t,v in dp[i].items():nxt[j][t+b]+=v
            dp=nxt
            for t,v in dp[origin].items():hist[n][t]+=2*v
    for n in range(1,N+1):
        assert hist[n]==formula[n],(n,hist[n],formula[n])
    return N

def main():
    N=120
    series=rational_recurrence(N)
    for n in range(1,N+1):
        assert series[n]==bivariate_formula(n),(n,series[n],bivariate_formula(n))
    tests=0
    for n in range(1,16):
        hist=Counter()
        for bits in product('01',repeat=n):
            w=''.join(bits)
            c=is_good(w)
            a=admissible_differences(w)
            assert c==a,(n,w,c,a)
            if c:hist[sum(w[i]!=w[(i+1)%n] for i in range(n))]+=1
            tests+=1
        assert hist==series[n],(n,hist,series[n])
    trace_check(60,series)
    assert [sum(series[n].values()) for n in range(1,17)]==[2,2,2,10,12,26,30,42,56,92,134,202,288,422,612,906]
    print(f'CYCLIC_ANTISQUARE_PASS exhaustive_n=1..15 test_words={tests} trace_n=1..60 rational_and_formula_n=1..{N}')
if __name__=='__main__':main()
