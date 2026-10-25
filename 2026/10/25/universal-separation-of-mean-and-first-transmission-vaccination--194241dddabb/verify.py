#!/usr/bin/env python3
"""Exact rational finite checks for path vaccination risk objectives."""
import itertools
import json
from fractions import Fraction


def f(k, p):
    return sum(((k-d) * p**d for d in range(1,k)), Fraction(0))


def ell(k, p):
    return Fraction(0) if k < 2 else 2*p + (k-2)*(2*p-p*p)


def predicted(n,j,p):
    a,b=j-1,n-j
    return (1+2*(f(a,p)+f(b,p))/(n-1), (ell(a,p)+ell(b,p))/(n-1))


def independent_enumeration(n,j,p):
    vertices=[v for v in range(1,n+1) if v!=j]
    edges=[(v,v+1) for v in range(1,n) if v!=j and v+1!=j]
    m=len(edges)
    mean=Fraction(0); risk=Fraction(0)
    for mask in range(1<<m):
        parent={v:v for v in vertices}
        def find(v):
            while parent[v]!=v:
                v=parent[v]
            return v
        count=0
        for h,(u,v) in enumerate(edges):
            if (mask>>h)&1:
                parent[find(u)]=find(v)
                count+=1
        sizes={v:0 for v in vertices}
        for v in vertices:
            sizes[find(v)]+=1
        cluster_sizes=[t for t in sizes.values() if t]
        weight=p**count*(1-p)**(m-count)
        mean+=weight*sum(t*t for t in cluster_sizes)/(n-1)
        risk+=weight*sum(t for t in cluster_sizes if t>=2)/(n-1)
    return mean,risk


def optima(n,p):
    values=[predicted(n,j,p) for j in range(1,n+1)]
    smallest_mean=min(v[0] for v in values)
    smallest_risk=min(v[1] for v in values)
    return ([j+1 for j,v in enumerate(values) if v[0]==smallest_mean],
            [j+1 for j,v in enumerate(values) if v[1]==smallest_risk])


def main():
    points=[Fraction(1,4),Fraction(1,2),Fraction(3,4)]
    cases=0
    for n in range(2,11):
        for p in points:
            for j in range(1,n+1):
                a=predicted(n,j,p)
                b=independent_enumeration(n,j,p)
                assert a==b,(n,j,p,a,b)
                cases+=1
            a,b=optima(n,p)
            centers=sorted({(n+1)//2,(n+2)//2}) if n>=3 else [1,2]
            tips=[2,n-1] if n>=4 else ([2] if n==3 else [1,2])
            assert a==centers,(n,p,a,centers)
            assert b==sorted(set(tips)),(n,p,b,tips)
    p=Fraction(1,2)
    middle=predicted(5,3,p)
    near=predicted(5,2,p)
    assert middle==(Fraction(3,2),Fraction(1,2))
    assert near==(Fraction(13,8),Fraction(7,16))
    output={
       'checks':'independent bond-state enumeration against closed path formulas and exact minimizers',
       'fractional_probabilities':['1/4','1/2','3/4'],
       'n_min':2,'n_max':10,'vertex_objective_pairs':cases,
       'path5_p_half_middle':{'expected_size':'3/2','probability_at_least_two':'1/2'},
       'path5_p_half_next_to_endpoint':{'expected_size':'13/8','probability_at_least_two':'7/16'},
       'all_checks_passed':True
    }
    print(json.dumps(output,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
