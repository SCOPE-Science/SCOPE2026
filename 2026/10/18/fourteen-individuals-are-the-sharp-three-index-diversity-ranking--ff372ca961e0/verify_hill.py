#!/usr/bin/env python3
"""Exact verification of finite abundance-profile diversity cutoff.

No third-party modules, network connection, or external data are required.
"""
from itertools import combinations
from math import comb


def partitions_desc(n, largest=None):
    """All positive integer partitions in nonincreasing order."""
    if n == 0:
        yield ()
        return
    if largest is None:
        largest = n
    for k in range(min(n, largest), 0, -1):
        for rem in partitions_desc(n-k, k):
            yield (k,) + rem


def hist_partitions(n):
    """Independent construction by multiplicities for parts 1,2,...,n."""
    hist = [0]*(n+1)
    def visit(part, remaining):
        if part == n+1:
            if remaining == 0:
                yield tuple(v for v in range(n,0,-1) for _ in range(hist[v]))
            return
        for count in range(remaining//part+1):
            hist[part] = count
            yield from visit(part+1, remaining-count*part)
        hist[part] = 0
    yield from visit(1,n)


def square_sum(profile):
    return sum(a*a for a in profile)


def paradox(A,B):
    """A has less richness, greater Hill-2, less Hill-infinity."""
    return (len(A)<len(B) and max(A)>max(B)
            and square_sum(A)<square_sum(B))


def lower_square(N,r,x):
    if r<2 or N-x<r-1 or N-x>(r-1)*x:
        return None
    t,u=divmod(N-x,r-1)
    if t<1 or (u and t+1>x):
        return None
    return x*x+(r-1-u)*t*t+u*(t+1)*(t+1)


def upper_square(N,s,c):
    if s<1 or c<1 or N<s or N>s*c:
        return None
    if c==1:
        return N
    full, extra=divmod(N-s,c-1)
    # Full entries at c, possibly one partial entry, the rest singleton.
    if extra:
        return full*c*c+(1+extra)**2+(s-full-1)
    return full*c*c+(s-full)


def envelope_candidates(bound=14):
    found=[]
    for N in range(1,bound+1):
        for r in range(2,N):
            for x in range(2,N-r+2):
                low=lower_square(N,r,x)
                if low is None:
                    continue
                c=x-1
                s=max(r+1,(N+c-1)//c)
                high=upper_square(N,s,c)
                if high is not None and low<high:
                    found.append((N,r,x,s,low,high))
    return found


def run():
    count=0
    qualifying=[]
    pcounts=[]
    for N in range(1,15):
        P=list(partitions_desc(N))
        Q=list(hist_partitions(N))
        assert len(P)==len(set(P))==len(Q)==len(set(Q))
        assert set(P)==set(Q)
        assert all(sum(p)==N and all(a>0 for a in p) for p in P)
        pcounts.append(len(P))
        for A,B in combinations(P,2):
            count+=1
            if paradox(A,B):
                qualifying.append((N,A,B))
            if paradox(B,A):
                qualifying.append((N,B,A))
    assert pcounts==[1,2,3,5,7,11,15,22,30,42,56,77,101,135]
    assert count==20283
    assert qualifying==[(14,(6,2,2,2,2),(5,5,1,1,1,1))]
    expected_envelopes=[(14,5,6,6,52,54)]
    assert envelope_candidates(14)==expected_envelopes
    # Directly test both extremal envelopes, including when s > r+1.
    for N in range(3,15):
        P=list(partitions_desc(N))
        for r in range(2,N):
            for x in range(2,N-r+2):
                allowed_A=[p for p in P if len(p)==r and p[0]==x]
                if not allowed_A:
                    continue
                low=lower_square(N,r,x)
                assert min(map(square_sum,allowed_A))==low
                c=x-1
                s=max(r+1,(N+c-1)//c)
                allowed_B=[p for p in P if len(p)>=r+1 and p[0]<=c]
                high=upper_square(N,s,c)
                if allowed_B:
                    assert max(map(square_sum,allowed_B))==high
                else:
                    assert high is None
    A=(6,2,2,2,2)
    B=(5,5,1,1,1,1)
    assert sum(A)==sum(B)==14
    assert (len(A),len(B))==(5,6)
    assert (square_sum(A),square_sum(B))==(52,54)
    assert (max(A),max(B))==(6,5)
    # Thus (D0,D2,Dinf) is (5,49/13,7/3) vs (6,98/27,14/5).
    assert 49*27 > 98*13
    assert 7*5 < 14*3
    # Strict convexity of squares plus parity yields uniqueness at N=14.
    assert all(square_sum(p)%2 == sum(p)%2 for p in partitions_desc(14))
    print('PASS: two independent enumeration methods,',count,'unordered pairs, N=1..14')
    print('PASS: unique reversed triple:', qualifying)
    print('PASS: sharp envelope candidates:',expected_envelopes)
    print('PASS: extremal square-sum bounds independently verified for N<=14')
    print('PASS: exact diversity contrasts D0, D2, D_infinity and parity')


if __name__=='__main__':
    run()
