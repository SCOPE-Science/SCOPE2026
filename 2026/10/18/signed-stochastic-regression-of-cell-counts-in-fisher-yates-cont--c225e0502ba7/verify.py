#!/usr/bin/env python3
"""Exact independent finite-size checks for monotone Fisher--Yates cell regression."""
from fractions import Fraction
from itertools import permutations, product
from math import factorial
from collections import defaultdict, Counter


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for x in range(1, n-k+2):
        for z in compositions(n-x,k-1):
            yield (x,)+z


def cumsum(a):
    s=0; out=[]
    for x in a:
        out.append(set(range(s,s+x)))
        s+=x
    return out


def verify_case(rows, cols):
    n=sum(rows)
    assert n==sum(cols)
    A=cumsum(rows); B=cumsum(cols)
    hist=Counter()
    for perm in permutations(range(n)):
        vals=tuple(sum(perm[u] in B[j] for u in A[i]) for i in range(len(A)) for j in range(len(B)))
        hist[vals]+=1
    assert sum(hist.values())==factorial(n)
    m=len(A)*len(B)
    examined=0
    for s in range(m):
        i,j=divmod(s,len(B))
        for t in range(m):
            if s==t: continue
            k,l=divmod(t,len(B))
            freq=defaultdict(Counter)
            for tab,mult in hist.items():
                freq[tab[s]][tab[t]]+=mult
            xs=sorted(freq)
            direction= -1 if i==k or j==l else +1
            for x1,x2 in zip(xs,xs[1:]):
                f1=freq[x1]; f2=freq[x2]
                d1=sum(f1.values()); d2=sum(f2.values())
                for threshold in range(n+1):
                    tail1=Fraction(sum(v for y,v in f1.items() if y>=threshold),d1)
                    tail2=Fraction(sum(v for y,v in f2.items() if y>=threshold),d2)
                    assert direction*(tail2-tail1)>=0,(rows,cols,s,t,x1,x2,threshold,tail1,tail2)
                    examined+=1
            EX=Fraction(sum(x*sum(ct.values()) for x,ct in freq.items()), factorial(n))
            EY=Fraction(sum(y*cnt for ct in freq.values() for y,cnt in ct.items()), factorial(n))
            EXY=Fraction(sum(x*y*cnt for x,ct in freq.items() for y,cnt in ct.items()), factorial(n))
            cov=EXY-EX*EY
            a=rows[i]; c=rows[k]; b=cols[j]; d=cols[l]
            if i==k:
                want=Fraction(-a*(n-a)*b*d,n*n*(n-1))
            elif j==l:
                want=Fraction(-a*c*b*(n-b),n*n*(n-1))
            else:
                want=Fraction(a*c*b*d,n*n*(n-1))
            assert cov==want,(rows,cols,s,t,cov,want)
            examined+=1
    return examined


def main():
    total=0; tested=0
    for n in range(2,7):
        rlist=[];clist=[]
        for k in range(2,min(n,3)+1):
            rlist+=list(compositions(n,k))
            clist+=list(compositions(n,k))
        if n<=5:
            cases=list(product(rlist,clist))
        else:
            cases=[((2,2,2),(2,2,2)),((1,2,3),(3,1,2)),((2,4),(3,3)),((1,1,4),(2,2,2)),((3,3),(1,4,1))]
        for a,b in cases:
            total+=verify_case(a,b)
            tested+=1
    print(f'PASS: {tested} distinct positive-margin pairs; {total} exact rational conditional tail comparisons and covariance identities; all permutations of size <= 6 used for each case.')

if __name__=='__main__': main()
