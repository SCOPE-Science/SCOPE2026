#!/usr/bin/env python3
"""Finite verifier for the universal/private/guardian committee family.

Uses exact integer ordinary-core and Pareto checks and an independent LP
for fractional core+ certificates (SciPy HiGHS; tolerance 1e-8).
The general theorem relies on the supplied analytic proof, not these tests.
"""
from itertools import combinations
from math import comb
import numpy as np
from scipy.optimize import linprog


def instance(k, r):
    m = 1+k*r
    approvals = [frozenset([0] + list(range(1+i*r,1+(i+1)*r))) for i in range(k)]
    approvals.append(frozenset(range(1,m)))  # guardian approves every private, not the common
    return m, approvals


def core_exact(m, approvals, W, k):
    n = len(approvals)
    u = [len(A.intersection(W)) for A in approvals]
    for t in range(1,k+1):
        for T in combinations(range(m),t):
            improving = sum(len(A.intersection(T)) > x for A,x in zip(approvals,u))
            if improving*k >= n*t:
                return False
    return True


def plus_lp(m, approvals, W, k):
    q = len(approvals)/k
    winning=set(W)
    variables=[(i,c) for i,A in enumerate(approvals) for c in W if c in A]
    d=len(variables); A_ub=[];b_ub=[]
    for i,app in enumerate(approvals):
        budget=np.zeros(d+1)
        for j,(v,_) in enumerate(variables):
            if v==i: budget[j]=1
        A_ub.append(budget);b_ub.append(1)
        for j,(v,_) in enumerate(variables):
            if v!=i:continue
            row=budget.copy();row[j]+=1
            A_ub.append(row);b_ub.append(1)
    for c in W:
        row=np.zeros(d+1)
        for j,(i,w) in enumerate(variables):
            if w==c:row[j]=1
        A_ub.append(row);b_ub.append(q)
    for c in range(m):
        if c in winning:continue
        supp={i for i,A in enumerate(approvals) if c in A}
        row=np.zeros(d+1)
        for j,(i,w) in enumerate(variables):
            if i in supp:row[j]=-1
        row[-1]=1
        A_ub.append(row);b_ub.append(q-len(supp))
    objective=np.zeros(d+1);objective[-1]=-1
    res=linprog(objective,A_ub=A_ub,b_ub=b_ub,
        bounds=[(0,None)]*d+[(0,1)],method='highs')
    return bool(res.success and res.x[-1]>1e-8)


def is_pareto_efficient(approvals,W,all_utility):
    my=tuple(len(a.intersection(W)) for a in approvals)
    return not any(all(x>=y for x,y in zip(other,my)) and other!=my for other in all_utility)


def run():
    checked=0
    for k,r in [(3,1),(3,2),(3,3),(4,1),(4,2),(5,1)]:
        m,approvals=instance(k,r)
        Ws=list(combinations(range(m),k))
        all_utility=[tuple(len(A.intersection(W)) for A in approvals) for W in Ws]
        counts=[0,0,0]
        for W in Ws:
            ordinary=core_exact(m,approvals,W,k)
            plus=plus_lp(m,approvals,W,k)
            pe=is_pareto_efficient(approvals,W,all_utility)
            sizes=[len(approvals[i].intersection(W)) for i in range(k)]
            expected_core=0 in W or sum(v>0 for v in sizes)>=k-1
            expected_plus=0 in W
            assert (ordinary,plus,pe)==(expected_core,expected_plus,True), (k,r,W,ordinary,plus,pe,expected_core,expected_plus)
            counts[0]+=ordinary;counts[1]+=plus;counts[2]+=pe
            checked+=1
        expected_plus=comb(k*r,k-1)
        expected_bad=r**k+k*(k-1)*comb(r,2)*r**(k-2)
        assert counts==[expected_plus+expected_bad,expected_plus,comb(m,k)],(k,r,counts)
        print('k=%d r=%d committees=%d core=%d core_plus=%d Pareto_efficient=%d' % (
             k,r,comb(m,k),*counts))
    print('PASS: %d distinct committees; all possible proposals checked and independent LP certificates solved.' % checked)
if __name__=='__main__': run()
