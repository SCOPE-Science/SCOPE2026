#!/usr/bin/env python3
"""Finite, independent checks for the Boolean signed-chain incenter theorem.

Requires only Python 3 standard library. These finite checks do not replace
its arbitrary-dimension proof.
"""
import itertools
import math
from fractions import Fraction


def rank_rational(rows, width):
    pivots = {}
    for row in rows:
        v = {i: Fraction(a) for i, a in enumerate(row) if a}
        while v:
            p = min(v)
            if p not in pivots:
                c = v[p]
                pivots[p] = {j: z/c for j,z in v.items()}
                break
            factor = v[p]
            for j,z in pivots[p].items():
                v[j] = v.get(j, 0) - factor*z
                if v[j] == 0:
                    del v[j]
    return len(pivots)


def maximal_chain_vectors(n):
    for order in itertools.permutations(range(n)):
        m = 0
        vec = [0]*(1<<n)
        vec[m] = 1
        for i in order:
            m |= (1<<i)
            vec[m] = 1
        yield vec


def cube_section_vertices(h, a):
    for rest in itertools.product((-1,1), repeat=h-1):
        last=-sum(rest)
        if abs(last) <= 1:
            yield [a*x for x in (*rest,last)]
    # Above enumerates all vertices with the final coordinate free, but some
    # vertices have a different free coordinate. Enumerate all positions.


def all_section_vertices(h,a):
    vertices = set()
    for free in range(h):
        others = [i for i in range(h) if i!=free]
        for signs in itertools.product((-1,1),repeat=h-1):
            q=[0]*h
            for i,s in zip(others,signs):q[i]=s
            q[free]=-sum(signs)
            if abs(q[free])<=1:
                vertices.add(tuple(q))
    return [tuple(a*s for s in q) for q in vertices],len(vertices)


def test(n):
    h=n+1
    N=1<<n
    full=list(maximal_chain_vectors(n))
    assert len(full)==math.factorial(n)
    exact_rank=rank_rational(full,N)
    assert exact_rank==N-n,(n,exact_rank,N-n)
    a=1-math.sqrt((h-1)/h)
    r=1/math.sqrt(h)
    points,nverts=all_section_vertices(h,a)
    if h%2==0:
        expected=math.comb(h,h//2)
    else:
        expected=h*math.comb(h-1,(h-1)//2)
    assert nverts==expected,(n,nverts,expected)
    assert all(abs(sum(t))<1e-10 and max(abs(z) for z in t)<=a+1e-10 for t in points)
    for t in points:
        for s in range(1,h+1):
            for inds in itertools.combinations(range(h),s):
                slack=1-abs(sum(t[k] for k in inds))-r*math.sqrt(s)
                assert slack >= -2e-12,(n,t,s,slack)
                if s==h:
                    assert abs(slack)<2e-12
    # A perturbed rank-constant center (not simply the origin) works.
    p=[0.0]*h
    p[0]=a/3
    p[-1]=-a/3
    assert any(abs(q)>0 for q in p)
    for s in range(1,h+1):
        for inds in itertools.combinations(range(h),s):
            assert abs(sum(p[k] for k in inds)) + r*math.sqrt(s) <=1+2e-12
    return n, N, len(full), exact_rank, nverts


def main():
    rows=[test(n) for n in range(1,7)]
    for line in rows:
        print('n=%d ambient=%d maximal_chains=%d exact_chain_rank=%d incenter_vertices=%d'%line)
    print('VERIFY_OK signed_boolean_chain_incenter n=1..6 exact_matrix_ranks=yes all_section_vertices=yes all_subchain_slacks=yes')

if __name__=='__main__':main()
