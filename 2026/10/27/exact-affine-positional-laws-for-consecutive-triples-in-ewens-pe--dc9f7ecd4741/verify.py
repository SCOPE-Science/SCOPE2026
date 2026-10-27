#!/usr/bin/env python3
"""Exact verification of Ewens consecutive-three pattern polynomial identities."""
from itertools import permutations, combinations
from fractions import Fraction
from math import comb, factorial

TYPES=('123','132','213','231','312','321')

def choose(a,k):
    return comb(a,k) if a>=k and k>=0 else 0

def coeffs(n,i,typ):
    b=choose(n-1,3); t=choose(n-2,2); h=n-3; g=n-i-2; j=i-1
    return {
      '123':(b,t,h,1),
      '132':(b-g,t+h,g+1,0),
      '213':(b-j,t+h,j+1,0),
      '231':(b+g,t+1,j,0),
      '312':(b+j,t+1,g,0),
      '321':(b,t+h,1,0)
    }[typ]

def cycles_closed(f):
    seen=set(); found=0
    for x in f:
        if x in seen: continue
        path={}; z=x
        while z in f and z not in path and z not in seen:
            path[z]=True; z=f[z]
        if z in path: found+=1
        seen.update(path)
    return found

def observed_counts(n,i,typ):
    counts=[0,0,0,0]
    rank=[int(x)-1 for x in typ]
    for chosen in combinations(range(1,n+1),3):
        assignment={i+k:chosen[rank[k]] for k in range(3)}
        counts[cycles_closed(assignment)]+=1
    return tuple(counts)

def cycle_number(perm):
    n=len(perm); seen=set(); total=0
    for j in range(n):
        if j in seen: continue
        total+=1; z=j
        while z not in seen:
            seen.add(z); z=perm[z]-1
    return total

def ranktype(vals):
    return ''.join(str(1+sorted(vals).index(z)) for z in vals)

def exhaustive():
    assertions=0
    for n in range(3,12):
        for i in range(1,n-1):
            for typ in TYPES:
                assert observed_counts(n,i,typ)==coeffs(n,i,typ),(n,i,typ,observed_counts(n,i,typ),coeffs(n,i,typ))
                assertions+=1
    for n in range(3,8):
        for theta in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(3)):
            num={(i,t):Fraction(0) for i in range(1,n-1) for t in TYPES}
            den=Fraction(0)
            for pi in permutations(range(1,n+1)):
                weight=theta**cycle_number(pi)
                den+=weight
                for i in range(1,n-1):num[(i,ranktype(pi[i-1:i+2]))]+=weight
            base=(theta+n-3)*(theta+n-2)*(theta+n-1)
            for i in range(1,n-1):
                for t in TYPES:
                    a=coeffs(n,i,t)
                    prob=sum(a[k]*theta**k for k in range(4))/base
                    assert num[(i,t)]/den==prob,(n,i,t,theta)
                    assertions+=1
    # Degree argument: the marked-closed-cycle expression makes each numerator
    # a polynomial of total degree <=3 in u=i-1, v=n-i-2. The ten triangular
    # lattice nodes u+v<=3 uniquely determine such a polynomial. The first
    # test above checks these ten nodes exactly and hence gives an all-n proof.
    print(f'VERIFY_OK {assertions} exact coefficient/joint-law assertions; triangular-polynomial certificate')

if __name__=='__main__': exhaustive()
