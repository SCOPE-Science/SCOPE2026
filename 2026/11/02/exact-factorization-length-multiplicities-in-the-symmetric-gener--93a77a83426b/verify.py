#!/usr/bin/env python3
"""Independent finite check of exact length-multiplicity formula for star triples."""
from collections import Counter
from math import gcd


def generators(a, n):
    return (a*n*(n-1)+1, a*n*(n+1)+1, a*(n+1)*(n+2)+1)


def formula(a, n, m):
    A,B,C=generators(a,n)
    s=2*n+1
    assert (3*a+4)%s==0
    u,v=A//s,C//s
    r=(m*pow(B,-1,s))%s
    N=(m-r*B)//s
    x=(N*pow(u,-1,v))%v
    z=(N-u*x)//v
    out={}
    if z>=0:
        for j in range(z//u+1):
            xx,zz=x+v*j,z-u*j
            ell=r+xx+zz
            out[ell]=1+min(xx//(n+1),zz//n)
    return out


def brute(a,n,m):
    A,B,C=generators(a,n)
    hist=Counter()
    for z in range(m//C+1):
        for y in range((m-z*C)//B+1):
            t=m-z*C-y*B
            if t%A==0:
                hist[t//A+y+z]+=1
    return dict(hist)


def run():
    tests=0
    for a,n,upper,step in [(7,2,1500,1),(6,5,25000,11),(5,9,60000,41),(8,3,24000,23),(15,3,28000,23),(7,12,75000,73)]:
        A,B,C=generators(a,n)
        s=2*n+1
        assert s>1 and (3*a+4)%s==0
        assert A%s==0 and C%s==0 and gcd(A//s,C//s)==1
        assert gcd(B,s)==1 and (n+1)*A+n*C==s*B
        for m in range(0,upper+1,step):
            want=brute(a,n,m)
            got=formula(a,n,m)
            assert got==want, (a,n,m,want,got)
            if len(got)>1:
                assert {v-u for u,v in zip(sorted(got),sorted(got)[1:])}=={2*a}
            tests+=1
    print('PASS: exact factorization-length multiplicities and identities,',tests,'targets')


if __name__=='__main__':
    run()
