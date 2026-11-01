#!/usr/bin/env python3
"""Reproduce the complete-split majority theorem from independent neighborhoods.

This script uses only Python's standard library. No external files are needed.
"""
from math import comb, isqrt


def neighbor_update(state, n):
    # Vertex positions 0..n-1 form a clique; n..2n-1 are independent.
    nxt = 0
    for v in range(2*n):
        if v < n:
            nei = [u for u in range(2*n) if u != v]
        else:
            nei = list(range(n))
        ones = sum((state >> u) & 1 for u in nei)
        z = (ones * 2 > len(nei)) or (
            ones * 2 == len(nei) and bool((state >> v) & 1)
        )
        nxt |= int(z) << v
    return nxt


def population_update(c, s, n):
    t = c+s
    new_c = (n if t > n else 0 if t < n else n-c)
    new_s = (n if 2*c > n else 0 if 2*c < n else s)
    return new_c, new_s


def reference_counts(n):
    period_count = {1:0,2:0}
    max_transient=0
    for c in range(n+1):
        for s in range(n+1):
            weight=comb(n,c)*comb(n,s)
            # An event is periodic if it lies at populations (0,0), (n,n),
            # (0,n), (n,0), or (n/2,n/2) with n even. The last event is
            # microscopic period two although its population profile is fixed.
            period_two = ((c == 0 and s == n) or (c == n and s == 0)
                          or (n%2==0 and c == s == n//2))
            period_one = (c==s==0) or (c==s==n)
            if period_two or period_one:
                depth=0
            else:
                c1,s1=population_update(c,s,n)
                depth=1 if ((c1,s1) in [(0,0),(n,n),(0,n),(n,0)]) else 2
            max_transient=max(max_transient,depth)
            hit = (c+s==n) or (c+s>n and 2*c<n) or (c+s<n and 2*c>n)
            period_count[2]+=weight*int(hit)
            period_count[1]+=weight*int(not hit)
    return period_count,max_transient


def binomial_formula(n):
    Cmid=comb(n,n//2) if n%2==0 else 0
    vort=1+(Cmid**2//2 if n%2==0 else 0)
    A=sum(comb(n,c) for c in range(n+1) if 2*c < n)
    Q=sum(comb(n,c)**2 for c in range(n+1) if 2*c < n)
    B=comb(2*n,n)+A*A-Q
    if n%2:
        assert B == 4**(n-1)+comb(2*n,n)//2
    else:
        assert B == 4**(n-1)-2**(n-1)*Cmid+3*Cmid*Cmid//4+comb(2*n,n)//2
    return vort,B


def exhaustive():
    tested=0
    for n in range(1,10):
        cyc2_states=0; basin=0; largest_depth=0
        refmax=(0 if n==1 else 1 if n==2 else 2)
        for x in range(1 << (2*n)):
            y=neighbor_update(x,n)
            z=neighbor_update(y,n)
            w=neighbor_update(z,n)
            v=neighbor_update(w,n)
            assert v==z, (n,x,'F4!=F2')
            p2 = y != x and z == x
            cyc2_states += p2
            b = w != z
            basin += b
            # Once in x2, p2 is determined by F(x2)!=x2.
            if x == z or x == y:
                depth=0
            elif y == w:
                depth=1
            else:
                depth=2
            largest_depth=max(largest_depth,depth)
            tested+=1
        count,transient=reference_counts(n)
        vort,B=binomial_formula(n)
        assert cyc2_states == 2*vort, (n,cyc2_states,2*vort)
        assert basin == B == count[2], (n,basin,B,count[2])
        assert largest_depth == transient == refmax, (n,largest_depth,transient,refmax)
        print(f'n={n} exhaustive={1<<(2*n)} cycles={vort} basin={B} first_periodic_max={transient}')
    for n in range(10,151):
        _,basin=binomial_formula(n)
        pop,maxdepth=reference_counts(n)
        assert basin == pop[2]
        assert maxdepth == 2
    print(f'SPLIT_MAJORITY_VERIFY_OK exhaustive_states={tested} population_sizes=1..150')


if __name__=='__main__':
    exhaustive()
