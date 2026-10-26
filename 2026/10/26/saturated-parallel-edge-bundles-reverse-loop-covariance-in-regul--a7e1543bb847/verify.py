#!/usr/bin/env python3
"""Exact matching enumeration for loop / parallel-bundle covariance."""
from fractions import Fraction
from math import comb, factorial

def pairings(indices):
    if not indices:
        yield ()
        return
    first = indices[0]
    for j in range(1,len(indices)):
        mate=indices[j]
        rest=indices[1:j]+indices[j+1:]
        for tail in pairings(rest):
            yield ((first,mate),)+tail

def theory(n,d,r):
    N=n*d
    if N%2 or n<2 or d<2 or r<2 or r>d: raise ValueError
    if n==2 and r==d:
        p=Fraction(factorial(d),1)
        for j in range(d): p/=N-2*j-1
        return -Fraction(n*comb(d,2),N-1)*p
    prod=Fraction(1,1)
    for j in range(r): prod/=N-2*j-1
    B=comb(n,2)*comb(d,r)**2*factorial(r)
    return B*prod*Fraction(r*(2*d-r-1-N*(d-r)),(N-1)*(N-2*r-1))

def direct(n,d,r):
    N=n*d
    Lsum=Psum=LPsum=cnt=0
    for pairs in pairings(tuple(range(N))):
        L=0; mult={}
        for a,b in pairs:
            i,j=a//d,b//d
            if i==j:L+=1
            else:
                ij=tuple(sorted((i,j)))
                mult[ij]=mult.get(ij,0)+1
        P=sum(comb(k,r) for k in mult.values() if k>=r)
        Lsum+=L;Psum+=P;LPsum+=L*P;cnt+=1
    C=Fraction(LPsum,cnt)-Fraction(Lsum*Psum,cnt*cnt)
    return C,cnt

def main():
    total=0
    for n,d in [(2,2),(2,3),(2,4),(2,5),(2,6),
                (3,2),(3,4),(4,2),(4,3),(5,2),(6,2)]:
        N=n*d
        if N>12:continue
        count=None
        for r in range(2,d+1):
            observed,count=direct(n,d,r)
            expected=theory(n,d,r)
            assert observed == expected,(n,d,r,observed,expected)
            expected_sign=(-1 if n==2 or r<d else 1)
            assert observed * expected_sign>0,(n,d,r,observed)
            total+=1
        print(f'EXHAUSTIVE_PASS n={n} d={d} pairings={count}')
    # Spot-check all nonexceptional parameter signs and asymptotic directions
    for n in range(2,50):
        for d in range(2,15):
            if n*d%2:continue
            for r in range(2,d+1):
                c=theory(n,d,r)
                assert (c>0)==(n>=3 and r==d)
    print('PARAMETER_SIGN_PASS n<=49 d<=14')
    print('TOTAL_EXHAUSTIVE_CASES',total)
    print('VERIFY_OK')
if __name__=='__main__':main()
