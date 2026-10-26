#!/usr/bin/env python3
"""Exact-arithmetic checks for the four-agent EFX chore phase diagram.

The theorem's nonexistence interval is proved analytically in RESULT.md.
This script verifies the seven symbolic allocation certificates and provides
independent exhaustive checks at three rational points in that interval.
"""
from fractions import Fraction
from itertools import product

# Each of four agent bundles has counts (A, B, C).  All item types are
# indistinguishable within their category.  Agents 1,2 have costs (r,1,7),
# and agents 3,4 have costs (r,7,1), with r>7.
WITNESSES = [
    ([(0,3,1),(0,2,1),(2,0,0),(1,0,3)], Fraction(7), Fraction(13)),
    ([(1,0,1),(0,5,2),(1,0,1),(1,0,1)], Fraction(11), Fraction(19)),
    ([(1,2,0),(0,3,3),(1,0,1),(1,0,1)], Fraction(21), Fraction(23)),
    ([(1,0,1),(0,4,3),(1,1,0),(1,0,1)], Fraction(23), Fraction(25)),
    ([(1,0,0),(0,5,3),(1,0,1),(1,0,1)], Fraction(25), Fraction(38)),
    ([(1,0,0),(0,5,4),(1,0,1),(1,0,0)], Fraction(32), Fraction(39)),
    ([(1,0,0),(0,5,5),(1,0,0),(1,0,0)], Fraction(39), None),
]

def tuple_affine(c, i):
    a,b,d=c
    return a, b+7*d if i<2 else 7*b+d

def threshold_affine(c, i):
    a,b,d = c
    coeff, const = tuple_affine(c, i)
    if b>0 and i<2 or d>0 and i>=2:
        return coeff, const-1
    if d>0 and i<2 or b>0 and i>=2:
        return coeff, const-7
    if a>0:
        return coeff-1, const
    return 0,0

def interval_for_allocation(bundles):
    assert len(bundles)==4
    assert tuple(sum(row[t] for row in bundles) for t in range(3)) == (3,5,5)
    lo,hi=Fraction(7),None
    binding_lo=[];binding_hi=[]
    for i in range(4):
        tcoef,tconst=threshold_affine(bundles[i], i)
        for j in range(4):
            ccoef,cconst=tuple_affine(bundles[j],i)
            dcoef,dconst=tcoef-ccoef,tconst-cconst
            if dcoef==0:
                if dconst>0:return None
            elif dcoef>0:
                b=Fraction(-dconst,dcoef)
                if hi is None or b<hi:hi=b;binding_hi=[(i+1,j+1)]
                elif b==hi:binding_hi.append((i+1,j+1))
            else:
                b=Fraction(dconst,-dcoef)
                if b>lo:lo=b;binding_lo=[(i+1,j+1)]
                elif b==lo:binding_lo.append((i+1,j+1))
    if hi is not None and hi<lo:return None
    return lo,hi,binding_lo,binding_hi

def efx_at(bundles,r):
    for i in range(4):
        a,b=threshold_affine(bundles[i],i)
        for j in range(4):
            aa,bb=tuple_affine(bundles[j],i)
            if a*r+b > aa*r+bb:
                return False
    return True

def comp4(k):
    for a in range(k+1):
        for b in range(k-a+1):
            for c in range(k-a-b+1):
                yield (a,b,c,k-a-b-c)

def exhaustive_no_efx(r):
    count=0
    for aa in comp4(3):
        for bb in comp4(5):
            for cc in comp4(5):
                bundles=tuple((aa[i],bb[i],cc[i]) for i in range(4))
                count+=1
                if efx_at(bundles,r):
                    return False,count,bundles
    return True,count,None

def main():
    for idx,(alloc,expected_lo,expected_hi) in enumerate(WITNESSES,1):
        actual=interval_for_allocation(alloc)
        assert actual is not None
        lo,hi,bindlo,bindhi=actual
        assert (lo,hi)==(expected_lo,expected_hi), (idx,actual)
        assert efx_at(alloc, max(lo,Fraction(8)) if hi is None else (max(lo,Fraction(8))+hi)/2)
        print(f'P{idx}: range r in [{lo}, {hi if hi is not None else "infinity"}], lower_binding={bindlo}, upper_binding={bindhi}')
    assert WITNESSES[0][1] == 7
    assert WITNESSES[0][2]>=WITNESSES[1][1]
    assert WITNESSES[1][2] == 19
    assert WITNESSES[2][1] == 21
    for i in range(2,6):
        assert WITNESSES[i][2] >= WITNESSES[i+1][1]
    assert WITNESSES[-1][2] is None
    for r in [Fraction(39,2), Fraction(20), Fraction(41,2)]:
        valid,count,wit=exhaustive_no_efx(r)
        assert valid,(r,wit)
        assert count==20*56*56
        print(f'No EFX at r={r}: {count} exhaustive type-count allocations checked')
    for r in [Fraction(71,10), Fraction(13), Fraction(19), Fraction(21), Fraction(23), Fraction(25), Fraction(38), Fraction(39), Fraction(100)]:
        assert any(efx_at(w[0],r) for w in WITNESSES)
    print('All exact checks passed. The nonexistence proof for every 19<r<21 is analytic, not inferred from sampling.')

if __name__ == '__main__':
    main()
