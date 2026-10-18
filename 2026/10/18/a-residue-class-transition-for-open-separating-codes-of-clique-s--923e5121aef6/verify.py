#!/usr/bin/env python3
"""Direct finite verification of open-separating domination on full clique subdivisions.
The mathematical conclusions for unbounded orders use the proof, not these tests.
"""
from math import comb, factorial
from collections import Counter
from itertools import combinations


def convolution(a, b):
    c = Counter()
    for i, x in a.items():
        for j, y in b.items():
            c[i + j] += x*y
    return c


def w_poly(n):
    # Inclusion-exclusion over prescribed isolated singleton or edge components.
    res = Counter()
    for j in range(n//2+1):
        for i in range(n-2*j+1):
            rest = n-i-2*j
            fac = factorial(n)//(factorial(i)*factorial(j)*2**j*factorial(rest))
            sgn = (-1)**(i+j)
            for r in range(comb(rest,2)+1):
                res[j+r] += sgn*fac*comb(comb(rest,2),r)
    return Counter({k:v for k,v in res.items() if v})


def formula(n):
    w, prev = w_poly(n), w_poly(n-1)
    out = Counter()
    for k,v in w.items():
        out[n+k] += v
        out[n-1+k] += n*v
    for k,v in prev.items():
        out[n+k] += n*v
        out[n-1+k] += n*(n-1)*v
    return Counter({k:v for k,v in out.items() if v})


def forests_min(n):
    # Count spanning tree forests with floor(n/3) components, each of size >=3.
    q=n//3
    if q==0:return 0
    from functools import lru_cache
    @lru_cache(None)
    def aux(rem, groups):
        if rem==0:return int(groups==0)
        if groups==0:return 0
        v=0
        for s in range(3,rem+1):
            v += comb(rem-1,s-1)*s**(s-2)*aux(rem-s,groups-1)
        return v
    return aux(n,q)


def predicted_min(n):
    q=n//3
    if n%3==0:
        return n*forests_min(n)+n*(n-1)*forests_min(n-1)
    return n*(n-1)*forests_min(n-1)


def check_subsets(n, full=True):
    edges=list(combinations(range(n),2)); m=len(edges); V=n+m
    nb=[0]*V
    for j,(a,b) in enumerate(edges):
        nb[a]|=1<<(n+j); nb[b]|=1<<(n+j)
        nb[n+j]|=(1<<a)|(1<<b)
    tally=Counter(); tally_total=Counter(); tested=0
    flags=[]
    for f in range(1<<m):
        deg=[0]*n
        for j,(a,b) in enumerate(edges):
            if (f>>j)&1:
                deg[a]+=1;deg[b]+=1
        isolates=[v for v in range(n) if deg[v]==0]
        isolated_edge=any(((f>>j)&1) and deg[a]==deg[b]==1 for j,(a,b) in enumerate(edges))
        flags.append((isolates,isolated_edge))
    # n <= 5: all subsets; n=6: all candidates meeting forced original count.
    if full:
        codes=range(1<<V)
    else:
        allowed_A=[(1<<n)-1]+[((1<<n)-1)^(1<<i) for i in range(n)]
        codes=(A|(F<<n) for A in allowed_A for F in range(1<<m))
    for C in codes:
        tested+=1
        sigset=set()
        good=True
        for v in range(V):
            sig=nb[v]&C
            if not sig and not ((C>>v)&1):good=False; break
            if sig in sigset:good=False;break
            sigset.add(sig)
        A=C&((1<<n)-1)
        isolates,isolated_edge=flags[C>>n]
        expected=(A.bit_count()>=n-1 and not isolated_edge and
                  (len(isolates)==0 or (len(isolates)==1 and ((A>>isolates[0])&1))))
        assert good==bool(expected),(n,C,good,expected)
        if good:
            tally[C.bit_count()]+=1
            directly_total=all(nb[v]&C for v in range(V))
            assert directly_total==(len(isolates)==0)
            if directly_total:
                tally_total[C.bit_count()]+=1
    assert tally==formula(n),(n,tally,formula(n))
    w=w_poly(n)
    predicted_total=Counter()
    for k,v in w.items():
        predicted_total[n+k]+=v
        predicted_total[n-1+k]+=n*v
    assert tally_total==predicted_total,(n,tally_total,predicted_total)
    first=min(tally)
    q=n//3
    expected=2*n-1-q-(n%3!=0)
    assert first==expected,(n,first,expected)
    assert tally[first]==predicted_min(n),(n,tally[first],predicted_min(n))
    assert min(tally_total)==2*n-1-n//3
    return tested,sum(tally.values()),first,tally[first],min(tally_total),sum(tally_total.values())


def main():
    for n in range(3,12):
        p=formula(n)
        assert sum(p.values())>0
        assert all(v>0 for v in p.values())
        assert min(p)==2*n-1-n//3-(n%3!=0)
        assert p[min(p)]==predicted_min(n)
        print('SYMBOLIC',n,'min',min(p),'minimum_codes',p[min(p)],'all_codes',sum(p.values()))
    total=0
    for n in range(3,7):
        tested,valid,minimum,optimizers,minimum_total,total_count=check_subsets(n,full=True)
        total+=tested
        print('DIRECT',n,'tested',tested,'valid',valid,'minimum',minimum,'optimizers',optimizers,'OTD_minimum',minimum_total,'OTD_count',total_count)
    print('VERIFICATION_OK','direct_candidates',total,'symbolic_orders',9)

if __name__=='__main__':main()
