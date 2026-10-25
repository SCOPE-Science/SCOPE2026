#!/usr/bin/env python3
"""Independent finite verification of orbit-diameter and Lefschetz formulas.
Python 3; standard library only. Run: python check_cycle_fixed.py
"""
from itertools import combinations

def cyc(a,n):
    a%=n
    return min(a,n-a)

def orbit_pair_diameter(n,d,i,j):
    m=n//d
    # Differences between one orbit point and the other run over j-i+t*m.
    return max(cyc(j-i+t*m,n) for t in range(d))

def predicted_nonempty(n,d,k,S):
    m=n//d
    if not S:return True
    if d%2==0:
        return k>=n//2
    shift=(d-1)*m//2
    if k<shift:return False
    return all(cyc(i-j,m)<=k-shift for i,j in combinations(S,2))

def actual_nonempty(n,d,k,S):
    m=n//d
    V=[i+t*m for i in S for t in range(d)]
    return all(cyc(i-j,n)<=k for i,j in combinations(V,2))

def inversion_sign(items,pi):
    indexed=[pi(x) for x in items]
    return -1 if sum(x>y for p,x in enumerate(indexed) for y in indexed[p+1:])%2 else 1

def signed_reduced_lefschetz(n,d,k):
    m=n//d
    pi=lambda v:(v+m)%n
    result=-1  # reduced chain degree -1
    for mask in range(1,1<<n):
        S=[i for i in range(n) if mask>>i&1]
        if not all(cyc(i-j,n)<=k for i,j in combinations(S,2)):
            continue
        if {pi(i) for i in S}==set(S):
            result += (-1 if len(S)%2==0 else 1)*inversion_sign(S,pi)
    return result

def fixed_reduced_euler(n,d,k):
    m=n//d
    out=-1
    for mask in range(1,1<<m):
        S=[i for i in range(m) if mask>>i&1]
        if predicted_nonempty(n,d,k,S):
            out += (-1 if len(S)%2==0 else 1)
    return out

def run():
    diam_cases=0
    for n in range(3,101):
        for d in range(1,n+1):
            if n%d:continue
            m=n//d
            for a in range(m):
                for b in range(m):
                    actual=orbit_pair_diameter(n,d,a,b)
                    if d%2:
                        expected=(d-1)*m//2+cyc(a-b,m)
                    else:
                        # The diameter of every orbit itself is n/2.
                        expected=n//2 if a==b else None
                    if expected is not None:
                        assert actual==expected,(n,d,a,b,actual,expected)
                    diam_cases+=1
    subset_cases=0
    for n in range(3,49):
        for d in range(1,n+1):
            if n%d:continue
            m=n//d
            if m>8:continue
            for k in range(n//2+1):
                for mask in range(1,1<<m):
                    S=[i for i in range(m) if mask>>i&1]
                    assert predicted_nonempty(n,d,k,S)==actual_nonempty(n,d,k,S),(n,d,k,S)
                    subset_cases+=1
    trace_cases=0
    for n in range(3,15):
        for d in range(1,n+1):
            if n%d:continue
            for k in range(n//2+1):
                a=signed_reduced_lefschetz(n,d,k)
                b=fixed_reduced_euler(n,d,k)
                assert a==b,(n,d,k,a,b)
                trace_cases+=1
    print('ODD_ROTATION_ORBIT_DIAMETER_FORMULA',diam_cases,'VERIFIED')
    print('FIXED_SIMPLEX_FILTRATION_EQUIVALENCE',subset_cases,'VERIFIED')
    print('SIGNED_LEFSCHETZ_FIXED_EULER',trace_cases,'VERIFIED')

if __name__=='__main__':run()
