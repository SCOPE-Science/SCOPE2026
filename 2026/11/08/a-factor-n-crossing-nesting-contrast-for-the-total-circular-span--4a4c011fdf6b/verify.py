#!/usr/bin/env python3
"""Standalone exact checks for random perfect matching span/crossing/nesting formulas."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def matchings(points):
    if not points:
        yield ()
        return
    a = points[0]
    for r in range(1, len(points)):
        b = points[r]
        rem = points[1:r] + points[r + 1:]
        for rest in matchings(rem):
            yield ((a, b),) + rest


def stats(m):
    n = len(m)
    size = 2*n
    span = sum(min(b-a-1, size-(b-a)-1) for a,b in m)
    cross = 0
    nest = 0
    for (a,b),(c,d) in combinations(m,2):
        if a > c: a,b,c,d = c,d,a,b
        cross += a < c < b < d
        nest += a < c < d < b
    return span, cross, nest


def exact_moments(n):
    sums = [0,0,0]
    sums2 = [0,0,0]
    mixed = [0,0]
    count = 0
    for m in matchings(tuple(range(1,2*n+1))):
        s,c,t = stats(m)
        count += 1
        for i,v in enumerate((s,c,t)):
            sums[i] += v
            sums2[i] += v*v
        mixed[0] += s*c
        mixed[1] += s*t
    means = [Q(v,count) for v in sums]
    vars_ = [Q(v,count)-means[i]**2 for i,v in enumerate(sums2)]
    covs = [Q(v,count)-means[0]*means[i+1] for i,v in enumerate(mixed)]
    return count,means,vars_,covs


def target(n):
    ms = Q(n*(n-1)**2,2*n-1)
    mc = Q(n*(n-1),6)
    vs = Q(2*n*n*(n-1)**2*(n*n-n+1),3*(2*n-3)*(2*n-1)**2)
    vc = Q(n*(n-1)*(n+3),45)
    cx = Q(n**3*(n-1)**2,6*(2*n-3)*(2*n-1))
    ct = Q(-n*n*(n-1)**2,6*(2*n-3)*(2*n-1))
    return [ms,mc,mc],[vs,vc,vc],[cx,ct]


def weighted_conditional(n):
    N=2*n
    W=W2=UX=UN=0
    for a in range(1,N):
        for b in range(a+1,N+1):
            d=b-a
            l=min(d-1,N-d-1)
            W+=l
            W2+=l*l
            UX+=l*(d-1)*(N-d-1)
            UN+=l*(comb(d-1,2)+(a-1)*(N-b))
    assert W == n*(n-1)**2
    assert UX == n*(n-1)**2*(5*n*n-10*n+6)//6
    assert UN == n*(n-2)*(n-1)**2*(4*n-3)//6
    p=Q(1,N-1)
    both=Q(1,(N-1)*(N-3))
    R=(n-1)**2
    E_S2=p*W2 + both*(W*W+W2-2*n*R*R)
    ES=p*W
    vS=E_S2-ES*ES
    EX=Q(n*(n-1),6)
    EY=EX
    # Two equivalent conditional expansions: the n-1 unmarked edges
    # contribute E[X_{n-1}]=(n-1)(n-2)/6.
    constant=Q((n-1)*(n-2),6)
    cX=(constant-EX)*ES + Q(UX,(N-1)*(N-3))
    cN=(constant-EY)*ES + Q(UN,(N-1)*(N-3))
    return vS,cX,cN


def main():
    checks=0
    for n in range(2,8):
        count,me,va,co=exact_moments(n)
        mt,vt,ct=target(n)
        for x,y in zip(me,mt):
            assert x==y,(n,'mean',x,y)
            checks+=1
        for x,y in zip(va,vt):
            assert x==y,(n,'variance',x,y)
            checks+=1
        for x,y in zip(co,ct):
            assert x==y,(n,'covariance',x,y)
            checks+=1
        assert co[0] == -n*co[1]
        checks+=1
        print('enumeration',n,count,'covariances',*co)
    for n in range(2,201):
        v,cx,ct=weighted_conditional(n)
        mt,vt,cts=target(n)
        assert v==vt[0]
        assert cx==cts[0]
        assert ct==cts[1]
        assert cx==-n*ct
        checks+=4
    print('PASS',checks,'exact assertions; exhaustive matching enumeration through seven chords and independent weighted edge sums through 200 chords')

if __name__=='__main__':
    main()
