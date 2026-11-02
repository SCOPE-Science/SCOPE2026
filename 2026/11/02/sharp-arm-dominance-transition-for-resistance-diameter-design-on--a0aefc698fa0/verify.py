#!/usr/bin/env python3
"""Standalone numerical and exact-rational checks for spider resistance-diameter design.

Only Python's standard library is used. These tests supplement the written proof;
finite testing is not a proof of its universal quantifiers.
"""
from fractions import Fraction as F
from math import sqrt, isclose
import random


def optimum(arms, B):
    """Each arm is a nonempty list of positive edge-price floats."""
    s = [sum(sqrt(p) for p in arm) for arm in arms]
    c = [v * v for v in s]
    C = sum(c)
    j = max(range(len(arms)), key=lambda k: c[k])
    t = C - c[j]
    if c[j] <= t:
        R = [C / B] * len(arms)
        D = 2 * C / B
    else:
        u = sqrt(t)
        R = [u * (s[j] + u) / B] * len(arms)
        R[j] = s[j] * (s[j] + u) / B
        D = (s[j] + u) ** 2 / B
    w = [[s[i] / (R[i] * sqrt(p)) for p in arm]
         for i, arm in enumerate(arms)]
    return w, D, R


def max_leaf_pair_R(w):
    R = [sum(1/x for x in arm) for arm in w]
    return max(R[i] + R[j] for i in range(len(w)) for j in range(i + 1, len(w)))


def check_exact(s, B):
    """Integer unit-price arms, exact rational test when the complement sum is a square."""
    c = [v*v for v in s]; C=sum(c); j=c.index(max(c)); t=C-c[j]
    # Arm edges each price 1, so s_i equals the number of edges.
    if c[j] <= t:
        R=[F(C,B) for _ in s]
        D=F(2*C,B)
    else:
        u=int(sqrt(t)); assert u*u==t
        R=[F(u*(s[j]+u),B) for _ in s]
        R[j]=F(s[j]*(s[j]+u),B)
        D=F((s[j]+u)**2,B)
    w=[[F(s[i],1)/R[i] for _ in range(s[i])] for i in range(len(s))]
    assert sum((sum(arm) for arm in w), F(0)) == B
    assert max_leaf_pair_R(w)==D
    # For arbitrary positive rational conductances, verify the proved lower bound.
    rng=random.Random(3001+sum(s)+B)
    for trial in range(40):
        raw=[[F(rng.randrange(1,100),rng.randrange(1,30)) for _ in arm] for arm in w]
        scale=F(B,1)/sum((sum(arm) for arm in raw), F(0))
        candidate=[[scale*x for x in arm] for arm in raw]
        assert max_leaf_pair_R(candidate)>=D
    return 1+40


def max_all_vertex_R(w):
    adj=[[]]
    leaves=[]
    for arm in w:
        parent=0
        for weight in arm:
            v=len(adj);adj.append([])
            adj[parent].append((v, 1/weight))
            adj[v].append((parent, 1/weight))
            parent=v
        leaves.append(parent)
    out=0.0
    for source in range(len(adj)):
        stack=[(source,-1,0.0)]
        while stack:
            v,prev,d=stack.pop()
            out=max(out,d)
            for u,weight in adj[v]:
                if u!=prev:stack.append((u,v,d+weight))
    return out


def main():
    checks=0
    for s in ([1,1], [2,2,2], [1,2,3], [5,3,4],
              [6,3,4], [7,3,4], [9,3,4], [2,2,3,3], [3,4,5,6]):
        # balanced examples do not need a square complement; dominant ones do
        C=sum(x*x for x in s);t=C-max(s)**2
        if max(s)**2<=t or int(sqrt(t))**2==t:
            for B in (1,2,5,17): checks+=check_exact(s,B)
    rng=random.Random(7865)
    for i in range(2400):
        m=rng.randrange(2,9)
        arms=[[float(rng.randrange(1,11)**2) for e in range(rng.randrange(1,7))] for _ in range(m)]
        B=float(rng.randrange(1,31))/rng.randrange(1,15)
        w,D,R=optimum(arms,B)
        assert isclose(sum(sum(p*x for p,x in zip(arm,wi))
                           for arm,wi in zip(arms,w)),B,rel_tol=2e-12)
        assert isclose(max_leaf_pair_R(w),D,rel_tol=2e-12)
        checks+=2
        if i<400:
            assert isclose(max_all_vertex_R(w),D,rel_tol=2e-12)
            checks+=1
        # Enumerate independent positive allocations with exact budget, not just scaling the optimizer
        for j in range(3):
            z=[[float(rng.randrange(1,90)) for _ in a] for a in arms]
            cost=sum(sum(p*x for p,x in zip(a,za)) for a,za in zip(arms,z))
            cand=[[B*x/cost for x in za] for za in z]
            assert max_leaf_pair_R(cand)>=D*(1-2e-12)
            checks+=1
    # Key exact boundary and unbalanced illustrations
    assert optimum([[1],[1],[1]],3)[1] == 2
    assert isclose(optimum([[1,1,1,1],[1],[1]],3)[1],(4+sqrt(2))**2/3)
    checks+=2
    print('PASS',checks,'independent equalities and feasible-comparison assertions')


if __name__=='__main__':main()
