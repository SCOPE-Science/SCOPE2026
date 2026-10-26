#!/usr/bin/env python3
"""Finite independent checks for geometric pairwise-distance spacing shifts.
These checks corroborate finite instances, not the unrestricted automorphism theorem.
"""
from itertools import combinations
from math import floor, log


def allowed_positions(support, base):
    return all(j - i in {base**t for t in range(18)}
               for i, j in combinations(support, 2))


def analytic_count(base, n):
    k = 0
    while base**(k+1) <= n:
        k += 1
    if base == 2:
        return (2*k+2)*n-2**(k+2)+4
    return (k+2)*n + 1-(base**(k+1)-1)//(base-1)


def finite_orbit_types(base, maxgap):
    powers=[]
    t=0
    while base**t <= maxgap:
        powers.append(base**t)
        t+=1
    pair_types=[(0,d) for d in powers]
    triple_types=[(0,d,2*d) for d in powers if base == 2 and 2*d <= 2*maxgap]
    return pair_types+triple_types


word_checks=0
for base in range(2,9):
    for n in range(1,15):
        exact=0
        possible={base**k for k in range(16) if base**k<n}
        for mask in range(1<<n):
            supp=[i for i in range(n) if mask>>i&1]
            if all(j-i in possible for i,j in combinations(supp,2)):
                exact+=1
        assert exact==analytic_count(base,n), (base,n,exact,analytic_count(base,n))
        word_checks+=1

# Check complete support normal forms independently over a bounded window.
support_checks=0
for base in range(2,9):
    for n in range(1,15):
        powers={base**k for k in range(16) if base**k<n}
        for mask in range(1<<n):
            supp=[i for i in range(n) if mask>>i&1]
            good=all(j-i in powers for i,j in combinations(supp,2))
            normal=(len(supp)<=1 or
                    (len(supp)==2 and supp[1]-supp[0] in powers) or
                    (base==2 and len(supp)==3 and
                     supp[1]-supp[0]==supp[2]-supp[1] and
                     (supp[1]-supp[0]) in powers))
            assert good==normal,(base,n,supp)
        support_checks+=1

# Independent exact formula at large lengths and continuous scale profiles.
profile_checks=0
for base in range(2,10):
    for n in [base**k+s for k in range(1,9) for s in (0,1,-1) if base**k+s>=1]:
        p=analytic_count(base,n)
        k=0
        while base**(k+1)<=n:k+=1
        t=log(n/base**k)/log(base)
        if base==2:
            delta=p/n-2*log(n)/log(base)
            pred=2-2*t-2**(2-t)+4/n
        else:
            delta=p/n-log(n)/log(base)
            pred=2-t-base**(1-t)/(base-1)+base/((base-1)*n)
        assert abs(delta-pred)<3e-11,(base,n,delta,pred)
        profile_checks+=1

# Orbit stabilizers: no nonempty finite support is shift-periodic.
for base in [2,3,4]:
    types=finite_orbit_types(base,base**5)
    assert len(types)==(12 if base==2 else 6)
    for supp in types:
        for shift in range(-9,10):
            if shift: assert tuple(x+shift for x in supp)!=supp
print(f'VERIFY_OK word_counts={word_checks} normal_forms={support_checks} digital_profiles={profile_checks} and orbit_freeness')
