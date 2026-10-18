#!/usr/bin/env python3
"""Verify fixed-point rotation criteria in the critical cycle bounded-independence complexes."""
import math
from collections import Counter

def rotate(mask, n, m):
    full=(1<<n)-1
    return ((mask<<m)|(mask>>(n-m)))&full

def vertex_orbits(n,m):
    rem=set(range(n)); out=[]
    while rem:
        i=min(rem); orb=[]; j=i
        while j not in orb:
            orb.append(j); rem.remove(j); j=(j+m)%n
        out.append(orb)
    return out

def fixed_by_face_orbits(d,m):
    """A setwise invariant nonempty face contains a whole vertex orbit;
    a single orbit works exactly when it is a face."""
    n=2*d
    even=set(range(0,n,2)); odd=set(range(1,n,2))
    return any(not (even <= set(o) or odd <= set(o)) for o in vertex_orbits(n,m))

def fixed_by_arithmetic(d,m):
    return math.gcd(d,m//2)>1 if m%2==0 else math.gcd(d,m)>1

def predicted(d):
    factors=[p for p in range(2,d+1) if d%p==0 and all(p%k for k in range(2,math.isqrt(p)+1))]
    if len(factors)>1: return 1
    return 4 if factors[0]==2 else factors[0]

count=0
for d in range(3,101):
    n=2*d
    fixed=[]
    for m in range(1,n):
        a=fixed_by_face_orbits(d,m)
        b=fixed_by_arithmetic(d,m)
        assert a==b,(d,m,a,b)
        if a: fixed.append(m)
        count+=1
    order=math.gcd(n,*fixed) if fixed else n
    assert order==predicted(d),(d,order,predicted(d),fixed)
print('VERIFIED: 98 values d=3..100,',count,'nonidentity rotations; orbit-face test agrees with gcd criterion and quotient orders.')
for d in [3,4,5,6,7,8,9,10,12,15,16,25,27,30,64]:
    n=2*d
    fixed=[m for m in range(1,n) if fixed_by_face_orbits(d,m)]
    order=math.gcd(n,*fixed)
    print('d=%-3d fixed_exponents=%-38s quotient_order=%d' % (d,str(fixed[:14])+('...' if len(fixed)>14 else ''),order))
