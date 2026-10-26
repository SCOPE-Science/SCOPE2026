#!/usr/bin/env python3
"""Standalone exact rational checks for a three-summand point-concentration theorem.

These finite checks validate the displayed arithmetic. General upper bounds
are established by the accompanying written combinatorial proof.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter


def convolution(a,b):
    c=Counter()
    for i,x in a.items():
        for j,y in b.items():c[i+j]+=x*y
    return c


def count_for_light(light_positions,t,s=3):
    d={0:F(1)}
    for z in light_positions:
        p={i:(t if i==z else F(1)) for i in range(3)}
        d=convolution(d,p)
    return d.get(s,F(0))


def check_full_support_center_polynomials():
    # Determine each cubic uniquely by interpolation at 0,1,-1,2.
    unique=set()
    for lights in product(range(3),repeat=3):
        vals=[count_for_light(lights,F(t)) for t in (0,1,-1,2)]
        # p(t)=a+b*t+c*t*t+d*t*t*t
        a=vals[0]
        e=vals[1]-a; f=vals[2]-a
        c=(e+f)/2
        bd=(e-f)/2
        d=(vals[3]-a-2*bd-4*c)/6
        b=bd-d
        coeff=tuple(F(v) for v in (a,b,c,d))
        assert all(count_for_light(lights,F(t))==sum(coeff[i]*F(t)**i for i in range(4)) for t in (0,1,-1,2,3))
        unique.add(coeff)
    expected={
        (3,2,2,0), (2,3,2,0), (2,2,3,0),
        (1,6,0,0), (2,4,0,1), (0,6,0,1),
    }
    assert unique==expected, sorted(unique)
    for coeff in unique:
        for k in range(101):
            t=F(k,100)
            assert sum(coeff[i]*t**i for i in range(4))<=3+2*t+2*t*t
    return len(unique)


def check_additive_counts():
    # Sanity check of N_j ceilings on all subsets of a finite example lattice.
    arr=list(combinations(range(-2,5),3))
    mx={0:0,1:0,2:0,3:0}
    for a,b in product(arr,repeat=2):
        first=Counter(u+v for u in a for v in b)
        for c in arr:
            d=Counter()
            for z,m in first.items():
                for w in c:d[z+w]+=m
            mx[3]=max(mx[3],max(d.values()))
    assert mx[3]==7
    for a,b,c in [({0,1,2},{0,1,2},{0,1,2})]:
        for mask in product((0,1),repeat=3):
            sets=[(u if q else {0,1}) for u,q in zip((a,b,c),mask)]
            m=max(Counter(sum(x) for x in product(*sets)).values())
            mx[sum(mask)]=max(mx[sum(mask)],m)
    assert mx=={0:3,1:4,2:5,3:7}, mx
    return mx


def check_witnesses():
    count=0
    for alpha in [F(1,3), F(7,20),F(3,8),F(2,5),F(9,20),F(1,2)]:
        beta=1-2*alpha
        t=beta/alpha
        lo=7*alpha**3-6*alpha**2+2*alpha
        hi=3*alpha**2*(1-alpha)
        want=(lo if alpha<=F(2,5) else hi)
        p0={0:alpha,1:alpha,2:beta}
        p1={0:beta,1:alpha,2:alpha}
        mixed=convolution(convolution(p1,p1),p0)
        equal=convolution(convolution(p1,p1),p1)
        assert mixed[3]==lo
        assert equal[4]==hi
        assert max(mixed.values())<=want and max(equal.values())<=want
        assert want==alpha**3*max(F(3)+3*t,F(3)+2*t+2*t*t)
        count+=1
    return count

if __name__=='__main__':
    print('VERIFY_OK polynomial_profiles=%d additive_bounds=%s exact_witness_profiles=%d' % (check_full_support_center_polynomials(),check_additive_counts(),check_witnesses()))
