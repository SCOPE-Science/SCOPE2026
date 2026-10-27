#!/usr/bin/env python3
"""Independent direct definition / weighted binary-support checks for rook graphs."""
from collections import Counter
from itertools import product
from math import comb


def direct(p,q):
    cells = [(i,j) for i in range(p) for j in range(q)]
    adj = [tuple(k for k,(a,b) in enumerate(cells)
                 if k!=i*q+j and (i==a or j==b)) for i,j in cells]
    weights=Counter()
    minima=[]
    for f in product(range(3), repeat=p*q):
        if not all(sum(f[w]==2 for w in adj[v])==1 if f[v]==0 else any(f[w]>0 for w in adj[v]) for v in range(p*q)):
            continue
        weights[sum(f)]+=1
        if not minima or sum(f)<minima[0][0]: minima=[(sum(f),f)]
        elif sum(f)==minima[0][0]: minima.append((sum(f),f))
    return weights, minima


def structured(p,q):
    n=p*q
    P=Counter()
    for mask in range(1<<n):
        t=mask.bit_count()
        if t==0:
            P[n]+=1
            continue
        row=[0]*p; col=[0]*q
        for k in range(n):
            if mask>>k&1:
                i,j=divmod(k,q); row[i]+=1;col[j]+=1
        r0=sum(x==0 for x in row);r1=sum(x==1 for x in row)
        c0=sum(x==0 for x in col);c1=sum(x==1 for x in col)
        u=r1*c0+r0*c1
        b=n-t-u
        if t==1:
            # At least one formerly optional vertex must be labeled 1.
            for k in range(1,u+1): P[2*t+b+k]+=comb(u,k)
        elif r0==1 and c0==1 and all(a<=1 for a in row) and all(a<=1 for a in col):
            # The only forced-1 corner is isolated unless an optional vertex is positive.
            for k in range(1,u+1): P[2*t+b+k]+=comb(u,k)
        else:
            for k in range(u+1): P[2*t+b+k]+=comb(u,k)
    return P


def optimal_shape(p,q):
    m=min(p,q)
    if p==q==2:return 13
    return q+(p if p==q else 0)


if __name__=='__main__':
    checked=0
    for p,q in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)]:
        D, minima=direct(p,q)
        S=structured(p,q)
        assert D==S,(p,q,D-S,S-D)
        assert minima[0][0]==2*p,(p,q,minima[0][0])
        assert len(minima)==optimal_shape(p,q),(p,q,len(minima),optimal_shape(p,q))
        print('exhaustive',p,q,'ternary',3**(p*q),'polynomial_terms',len(D),'total',sum(D.values()),'opt',len(minima))
        checked+=3**(p*q)
    for p,q in [(4,4),(4,5)]:
        S=structured(p,q)
        assert min(S)==2*p,(p,q,min(S))
        assert S[2*p]==optimal_shape(p,q),(p,q,S[2*p])
        print('binary-support',p,q,'supports',2**(p*q),'polynomial_terms',len(S),'total',sum(S.values()),'opt',S[2*p])
    print('PASS: direct-versus-structural distributions for',checked,'ternary assignments and large-support bound checks')
