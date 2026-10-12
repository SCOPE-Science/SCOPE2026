#!/usr/bin/env python3
"""Exact finite checks for fixed-occupancy, site-equiprobable co-occurrence nulls.

Uses only standard-library integers and Fraction arithmetic. Intended to verify
specific finite cases, not to substitute for the all-parameter proof.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb


def falling(n, r):
    if r > n:
        return 0
    z = 1
    for j in range(r):
        z *= n-j
    return z


def factorial_moment(h, a, b, r):
    return Q(falling(a, r)*falling(b, r), falling(h, r)) if r <= h else Q(0)


def exact_pair_moments(h, a, b):
    k = a+b-1
    m = [factorial_moment(h, a, b, j) for j in range(5)]
    mean = a*b-k*m[1]+m[2]
    second = (a*b)**2+k*(k-2*a*b)*m[1] + (2*a*b+k*k-4*k+2)*m[2] + (4-2*k)*m[3] + m[4]
    return mean, second-mean*mean


def hypergeom(h, a, b):
    return {x: Q(comb(a,x)*comb(h-a,b-x),comb(h,b))
            for x in range(max(0,a+b-h), min(a,b)+1)}


def pair_value(a,b,x):
    return (a-x)*(b-x)


def checks_pair_moments():
    n=0
    for h in range(2,13):
        for a in range(1,h+1):
            for b in range(1,h+1):
                p=hypergeom(h,a,b)
                assert sum(p.values())==1
                m=sum(Q(pair_value(a,b,x))*pr for x,pr in p.items())
                v=sum(Q(pair_value(a,b,x)**2)*pr for x,pr in p.items())-m*m
                assert (m,v)==exact_pair_moments(h,a,b),(h,a,b,m,v,exact_pair_moments(h,a,b))
                assert v>=0
                n+=1
    return n


def enum_row_subsets(h, a):
    return tuple(sum(1<<site for site in t) for t in combinations(range(h),a))


def brute_case(h, degrees):
    s=len(degrees)
    edges=tuple(combinations(range(s),2))
    populations=[enum_row_subsets(h,a) for a in degrees]
    total=1
    for p in populations:total*=len(p)
    sum_c=0
    sum_c2=0
    pair_marginal={e:Counter() for e in edges}
    pair_joint={(e,f):Counter() for e,f in combinations(edges,2)}
    forest_edges=tuple((i,i+1) for i in range(s-1))
    forest_joint=Counter()
    for rows in product(*populations):
        X={e:(rows[e[0]]&rows[e[1]]).bit_count() for e in edges}
        C=sum(pair_value(degrees[i],degrees[j],X[i,j]) for i,j in edges)
        sum_c+=C
        sum_c2+=C*C
        for e in edges:pair_marginal[e][X[e]]+=1
        for (e,f),p in pair_joint.items():p[X[e],X[f]]+=1
        forest_joint[tuple(X[e] for e in forest_edges)]+=1
    observed_mean=Q(sum_c,total*len(edges))
    observed_var=Q(sum_c2,total*len(edges)**2)-observed_mean**2
    expected_mean=sum(exact_pair_moments(h,*[degrees[i] for i in e])[0] for e in edges)/len(edges)
    expected_var=sum(exact_pair_moments(h,*[degrees[i] for i in e])[1] for e in edges)/len(edges)**2
    assert (observed_mean,observed_var)==(expected_mean,expected_var),(h,degrees,observed_mean,observed_var,expected_mean,expected_var)
    # Pairwise independence of ALL overlaps, including pairs sharing a species.
    for (e,f),jj in pair_joint.items():
        for (x,y),count in jj.items():
            assert Q(count,total)==Q(pair_marginal[e][x],total)*Q(pair_marginal[f][y],total)
        # Also test zero-probability joint outcomes if a joint category is absent.
        for x in pair_marginal[e]:
            for y in pair_marginal[f]:
                assert Q(jj[x,y],total)==Q(pair_marginal[e][x],total)*Q(pair_marginal[f][y],total)
    # Forest independence of all overlaps along a path, not merely each pair.
    marginal_f=[pair_marginal[e] for e in forest_edges]
    for tup in product(*(sorted(m) for m in marginal_f)):
        p=Q(1)
        for j,v in enumerate(tup):p*=Q(marginal_f[j][v],total)
        assert Q(forest_joint[tup],total)==p
    return total,observed_mean,observed_var


def triangle_obstruction():
    h=2; degrees=(1,1,1)
    rows=[enum_row_subsets(h,1)]*3
    all_x=[]
    for A,B,C in product(*rows):
        all_x.append(((A&B).bit_count(),(A&C).bit_count(),(B&C).bit_count()))
    assert len(all_x)==8
    assert all(sum(x) in (1,3) for x in all_x)
    assert Q(sum(x==(1,1,1) for x in all_x),8)==Q(1,4)
    # Each overlap marginal is Bernoulli(1/2), so mutual independence would imply 1/8.
    assert Q(1,4)!=Q(1,2)**3
    return 'triangle_joint_111=1/4_not_1/8'


def main():
    pairs=checks_pair_moments()
    cases=((2,(1,1,1)),(3,(1,2,1,2)),(4,(1,2,3,2)),
           (5,(2,3,4)),(5,(1,3,4,2)),(6,(1,2,3,4)))
    totals=[]
    for h, degrees in cases:
        n,m,v=brute_case(h,degrees)
        totals.append(n)
        print('CASE',h,degrees,'matrices',n,'mean',m,'variance',v)
    print('PAIR_CASES',pairs,'MATRICES',sum(totals),triangle_obstruction())
    print('VERIFY_OK')

if __name__=='__main__':
    main()
