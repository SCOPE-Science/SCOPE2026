#!/usr/bin/env python3
"""Exact rational checks for the heterogeneous anti-coordination triangle."""
from fractions import Fraction as Q
from itertools import combinations,product


def utility(g,a,i):
    return (g[i] if a[i] else 1-g[i])*sum(a[i]!=a[j] for j in range(3) if i!=j)


def welfare(g,a):
    return sum(utility(g,a,i) for i in range(3))


def nash(g,a):
    return all(utility(g,a,i)>=utility(g,tuple(1-a[j] if j==i else a[j] for j in range(3)),i) for i in range(3))


def theory(g):
    ix=sorted(range(3),key=lambda i:g[i]);l,m,h=(g[i] for i in ix)
    assert l<m<h and 2*m!=l+h and m!=Q(1,2)
    a=[1,1,1] if 2*m>l+h else [0,0,0]
    a[ix[0] if 2*m>l+h else ix[2]]=0 if 2*m>l+h else 1
    non_nash=(m-Q(1,2))*(2*m-l-h)<0
    return tuple(a),non_nash


def main():
    values=[Q(i,20) for i in range(1,20)]
    cases=0
    for g in product(values,repeat=3):
        if len(set(g))<3:continue
        l,m,h=sorted(g)
        if 2*m==l+h or m==Q(1,2):continue
        predicted,is_bad=theory(g)
        scores={a:welfare(g,a) for a in product((0,1),repeat=3)}
        winners=[a for a in scores if scores[a]==max(scores.values())]
        assert winners==[predicted],(g,winners,predicted)
        assert (not nash(g,predicted))==is_bad,(g,predicted,is_bad)
        cases+=1
    witness=(Q(1,10),Q(2,5),Q(3,5))
    a,is_bad=theory(witness)
    assert a==(0,1,1) and is_bad
    assert welfare(witness,a)==Q(14,5)
    assert utility(witness,a,1)==Q(2,5)
    assert utility(witness,(0,0,1),1)==Q(3,5)
    # In the lower half of the ordered simplex, the failure volume is
    # integral_{0}^{1/2} integral_{0}^{m}(m-l) dl dm = 1/48.
    # Density of ordered triples is 6; reflection gives two equal halves.
    half_simplex_volume=Q(1,48)
    assert 2*6*half_simplex_volume==Q(1,4)
    print(f'PASS {cases} generic rational triples; exact uniform probability 1/4')

if __name__=='__main__':main()
