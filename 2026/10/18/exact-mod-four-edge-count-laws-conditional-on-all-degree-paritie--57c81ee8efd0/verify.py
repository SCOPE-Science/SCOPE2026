#!/usr/bin/env python3
"""Exact finite checks of the stated conditional graph edge-mod-four law.
No external dependencies; computations are rational and integer only.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def mul(z,w):
    a,b=z; c,d=w
    return a*c-b*d, a*d+b*c


def power(z,k):
    out=(1,0)
    while k:
        if k&1:out=mul(out,z)
        z=mul(z,z);k>>=1
    return out


def negi_pow(k):
    return ((1,0),(0,-1),(-1,0),(0,1))[k%4]


def kw(n,w,k):
    return sum((-1)**j*comb(w,j)*comb(n-w,k-j)
               for j in range(max(0,k-(n-w)),min(k,w)+1))


def exact_weighted_count(n,w):
    """A+iB = sum_{G:D(G)=d} i^{|E(G)|}, every feasible d of weight w."""
    assert n>=3 and 0<=w<=n and w%2==0
    M=comb(n,2)
    sr=si=0
    for k in range(n+1):
        z=negi_pow(k*(n-k)); K=kw(n,w,k)
        sr+=K*z[0];si+=K*z[1]
    numr,numi=mul(power((1,1),M),(sr,si))
    den=1<<n
    assert numr%den==numi%den==0,(n,w,numr,numi,den)
    return numr//den,numi//den


def predicted_weighted_count(n,w):
    M=comb(n,2)
    if n%2==0:
        if 0<w<n:return (0,0)
        sigma=(-1)**(n//2)
        z=(1, sigma if w==0 else -sigma)
        num=mul(power((1,1),M),z)
        denpow=M+2-n  # weighted count = 2^(n-M-2)*(1+i)^M*(1+i sigma) * 2^(M-n+1)
        # simplifies weighted count = (1+i)^M*(1+/- i sigma)/2
        assert denpow>=0
        assert num[0]%2==0 and num[1]%2==0
        return num[0]//2,num[1]//2
    # odd n: Z=(-1)^(w/2+(n^2-1)/8)*2^(-(M-n+1)/2)*e^(i*pi*M/4)
    # Weighted count = (1+i)^M * S / 2^n, where S=sign*2^((n+1)/2)
    sign=(-1)**(w//2+(n*n-1)//8)
    num=power((1,1),M)
    factor=sign*(1<<((n+1)//2))
    a,b=num[0]*factor,num[1]*factor
    assert a%(1<<n)==0 and b%(1<<n)==0
    return a//(1<<n),b//(1<<n)


def count_by_exhaustive(n):
    edges=list(combinations(range(n),2))
    out=defaultdict(lambda:[0,0,0,0])
    for bitmask in range(1<<len(edges)):
        d=0
        for i,(u,v) in enumerate(edges):
            if bitmask&(1<<i):d^=(1<<u)|(1<<v)
        out[d][bitmask.bit_count()%4]+=1
    return out


def run():
    total=0
    for n in range(3,13):
        M=comb(n,2)
        for w in range(0,n+1,2):
            A=exact_weighted_count(n,w)
            B=predicted_weighted_count(n,w)
            assert A==B,(n,w,A,B)
            assert max(map(abs,A)) <= (1<<(M-n+1))
            total+=1
    for n in range(3,7):
        distributions=count_by_exhaustive(n)
        M=comb(n,2)
        denom=1<<(M-n+1)
        assert len(distributions)==(1<<(n-1))
        for d,counts in distributions.items():
            assert sum(counts)==denom
            w=d.bit_count()
            complex_sum=(counts[0]-counts[2],counts[1]-counts[3])
            assert complex_sum==exact_weighted_count(n,w),(n,d,counts,complex_sum)
            assert counts[0]+counts[2]==counts[1]+counts[3]==denom//2
            if n%2==0 and 0<w<n:
                assert counts==[denom//4]*4
            total+=1
    print(f'OK: {total} independent exact analytic/finite-graph instances; n=3..12 analytic, n=3..6 exhaustive.')

if __name__=='__main__':run()
