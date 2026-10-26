#!/usr/bin/env python3
"""Independent finite check of the exact cyclic OR-neighbor relaxation census."""
from math import comb
import random

def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0

def gap_bounded_polynomial(q, h):
    out=[0]*(q+1)
    out[0]=1
    for k in range(1, q+1):
        compositions=sum((-1)**j*comb(k,j)*choose(q-j*h-1,k-1) for j in range(k+1))
        numerator=q*compositions
        assert numerator%k==0
        out[k]=numerator//k
    return out

def convolution(a, b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def predicted_counts(n, t):
    if n%2:
        return gap_bounded_polynomial(n,t+1)
    p=gap_bounded_polynomial(n//2,t+1)
    return convolution(p,p)

def step(x,n):
    # Directly evaluates the local binary truth table for every cell.
    return sum((int(bool((x>>((i-1)%n)&1) or (x>>((i+1)%n)&1)))<<i) for i in range(n))

def preperiod(x,n):
    seen={}
    z=x
    for t in range(2*n+2):
        if z in seen:
            period=t-seen[z]
            assert period in (1,2)
            return seen[z], period
        seen[z]=t
        z=step(z,n)
    raise AssertionError('No repeat within finite bound')

def gap_preperiod(x,n):
    if x==0: return 0
    d=1 if n%2 else 2
    q=n//d
    maximum=0
    for residue in range(d):
        occupied={j for j in range(q) if (x>>(residue+2*j if d==2 else 2*j%n))&1}
        if occupied:
            v=sorted(occupied)
            gap=max((v[(i+1)%len(v)]-v[i])%q or q for i in range(len(v)))
            maximum=max(maximum,gap-1)
    return maximum

def exhaustive():
    checks=0
    for n in range(3,17):
        hist=[[0]*(n+1) for _ in range(n+1)]
        for x in range(1<<n):
            k=x.bit_count()
            a,period=preperiod(x,n)
            b=gap_preperiod(x,n)
            assert a==b, (n,x,a,b)
            if n%2:
                assert period==1, (n,x,period)
            else:
                even_mask=sum(1<<j for j in range(0,n,2))
                odd_mask=sum(1<<j for j in range(1,n,2))
                period_two=bool(x and not(x&even_mask and x&odd_mask))
                assert period==(2 if period_two else 1), (n,x,period)
            hist[a][k]+=1
            checks+=1
        previous=[0]*(n+1)
        for t in range(n):
            current=predicted_counts(n,t)
            actual=[sum(hist[u][k] for u in range(t+1)) for k in range(n+1)]
            assert current==actual,(n,t,current,actual)
            previous=current
        assert sum(sum(v) for v in hist)==(1<<n)
        M=n-1 if n%2 else n//2-1
        expected=n if n%2 else n*(1<<(n//2))-(n//2)**2
        assert sum(hist[M])==expected,(n,hist[M],expected)
        assert sum(hist[0])==(2 if n%2 else 4)
    return checks

def random_large():
    rng=random.Random(2502026)
    checks=0
    for n in (17,18,19,20,24,31,32,41,48,63,64,101):
        for _ in range(400):
            x=rng.getrandbits(n)
            a,p=preperiod(x,n)
            b=gap_preperiod(x,n)
            assert a==b, (n,x,a,b)
            checks+=1
    return checks

if __name__=='__main__':
    print('VERIFY_OK exhaustive_binary_configurations=',exhaustive(),
          'random_larger_cases=', random_large(),
          'cumulative_fixed_density_histogram=verified')
