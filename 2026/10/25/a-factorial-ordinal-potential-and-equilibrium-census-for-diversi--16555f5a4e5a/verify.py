#!/usr/bin/env python3
"""Exact integer tests of a diversity-jump potential and equilibrium census.

Usage: python check_bipartite_multivac.py
Vertices are labelled: the first A belong to one independent part, the next B
belong to the other. 0 denotes empty and positive integers denote agent types.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial


def utility(state, vertex, A):
    typ = state[vertex]
    if not typ:
        raise ValueError('Utility requested for an empty site')
    other = state[A:] if vertex < A else state[:A]
    live = sum(t != 0 for t in other)
    return Fraction(sum(t != 0 and t != typ for t in other), live) if live else Fraction(0)


def potential(state, A, num_types):
    Q = len(state) + 1  # Greater than the number of occupants.
    def h(t):
        return Q if t == 0 else factorial(t - 1)
    answer = Fraction(1)
    for side in (state[:A], state[A:]):
        live = sum(bool(t) for t in side)
        term = Fraction(1, h(live))
        for typ in range(1, num_types + 1):
            term *= h(sum(t == typ for t in side))
        answer *= term
    return answer


def cross_moves(state, A):
    for u,typ in enumerate(state):
        if not typ:
            continue
        for v,tv in enumerate(state):
            if tv or (u < A) == (v < A):
                continue
            changed=list(state)
            changed[u]=0
            changed[v]=typ
            changed=tuple(changed)
            if utility(changed,v,A)>utility(state,u,A):
                yield changed


def equilibrium_polynomial(A,B,q):
    N=A+B; n=N-q
    C=lambda u,v:comb(u,v) if 0<=v<=u else 0
    P={}
    def add(degree,value):
        P[degree]=P.get(degree,0)+value
    add(0,C(N,q));add(n,C(N,q))
    for full,other in ((A,B),(B,A)):
        ways=C(other,q)
        if not ways:
            continue
        for t in range(other-q+1):
            z=ways*C(other-q,t)
            add(t,z);add(full+t,z)
        add(0,-ways);add(n,-ways)
    for qa in range(1,A):
        qb=q-qa
        if not (1<=qb<B):
            continue
        v=C(A,qa)*C(B,qb)
        add(A-qa,v);add(B-qb,v)
    return {k:v for k,v in P.items() if v}


def test():
    configurations=0
    profitable_moves=0
    checked_polynomials=0
    tested_three_type=0
    for A in range(2,6):
        for B in range(2,6):
            N=A+B
            actual_by_q={}
            for state in product(range(3), repeat=N):
                q=state.count(0)
                if not 1<=q<=N-2:
                    continue
                configurations+=1
                phi=potential(state,A,2)
                any_move=False
                for nxt in cross_moves(state,A):
                    any_move=True
                    profitable_moves+=1
                    assert potential(nxt,A,2)>phi,(A,B,state,nxt)
                if not any_move:
                    k=state.count(1)
                    q_data=actual_by_q.setdefault(q,{})
                    q_data[k]=q_data.get(k,0)+1
            for q,actual in actual_by_q.items():
                expected=equilibrium_polynomial(A,B,q)
                assert actual==expected,(A,B,q,actual,expected)
                checked_polynomials+=1
    # Arbitrarily many types are covered analytically; test three and four types.
    for A,B,num_types in ((2,3,3),(3,3,3),(2,4,3),(3,3,4)):
        for state in product(range(num_types+1),repeat=A+B):
            if not 1<=state.count(0)<=A+B-2:
                continue
            tested_three_type+=1
            phi=potential(state,A,num_types)
            for nxt in cross_moves(state,A):
                profitable_moves+=1
                assert potential(nxt,A,num_types)>phi,(A,B,num_types,state,nxt)
    print('PASS',configurations,'two-color configurations;',checked_polynomials,'exact equilibrium polynomials;',tested_three_type,'three/four-color configurations;',profitable_moves,'strict moves')

if __name__=='__main__':
    test()
