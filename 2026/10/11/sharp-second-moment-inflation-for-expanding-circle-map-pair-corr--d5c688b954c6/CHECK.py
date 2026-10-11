"""Finite exact-arithmetic diagnostics for circular pair correlations of integer expanding maps.

Run with Python 3. No external packages. The infinite limit is proved separately.
"""
from fractions import Fraction as Q
from math import gcd


def fractional_part(q):
    return q - q.numerator // q.denominator


def bernoulli2(x):
    t = fractional_part(x)
    return t*t - t + Q(1, 6)


def covariance_formula(m, n, r):
    d = gcd(m, n)
    a, c = m // d, n // d
    return (bernoulli2((a-c)*r)-bernoulli2((a+c)*r)) / (a*c)


def arcs(m, r):
    out = []
    for k in range(m+1):
        lo, hi = Q(k-r, m), Q(k+r, m)
        lo, hi = max(Q(0),lo), min(Q(1),hi)
        if hi > lo:
            out.append((lo,hi))
    return out


def intersections(a, b):
    p = q = 0
    mass = Q(0)
    while p<len(a) and q<len(b):
        lo=max(a[p][0], b[q][0]);hi=min(a[p][1],b[q][1])
        if hi>lo:mass+=hi-lo
        if a[p][1]<b[q][1]:p+=1
        elif b[q][1]<a[p][1]:q+=1
        else:p+=1;q+=1
    return mass


def variance_formula(base, N, r):
    multipliers = [base**j-base**i for i in range(N) for j in range(i+1,N)]
    total = sum((covariance_formula(m,n,r) for m in multipliers for n in multipliers),Q(0))
    return Q(4,N*N)*total


def variance_partition(base,N,r):
    multipliers=[base**j-base**i for i in range(N) for j in range(i+1,N)]
    endpoints={Q(0),Q(1)}
    for m in multipliers:
        for lo,hi in arcs(m,r):
            endpoints.add(lo);endpoints.add(hi)
    pts=sorted(endpoints)
    mean=Q(0);second=Q(0)
    for left,right in zip(pts,pts[1:]):
        mid=(left+right)/2
        count=sum(min(fractional_part(m*mid),1-fractional_part(m*mid))<r for m in multipliers)
        val=Q(2*count,N)
        mean+=(right-left)*val
        second+=(right-left)*val*val
    return mean,second-mean*mean


def main():
    tested=0
    for m in range(1,8):
        for n in range(1,8):
            for r in (Q(1,9),Q(2,7),Q(1,3)):
                p=intersections(arcs(m,r),arcs(n,r))
                assert p-Q(4)*r*r==covariance_formula(m,n,r), (m,n,r,p)
                tested+=1
    for b,N,s in ((2,3,Q(1)),(2,4,Q(1)),(2,5,Q(1)),
                  (3,3,Q(1)),(3,4,Q(1)),(2,5,Q(2,3))):
        r=s/N
        mean, variance=variance_partition(b,N,r)
        assert mean==Q(2*s*(N-1),N)
        assert variance==variance_formula(b,N,r), (b,N,s,variance)
        tested+=1
    print('PASS',tested,'independent rational finite checks')

if __name__=='__main__':main()
