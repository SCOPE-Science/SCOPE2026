#!/usr/bin/env python3
"""Exact checks for the sharp first-collision antitone dependence theorem.

All computations here use rational arithmetic; this finite checker is a
supplement to, not a replacement for, the analytic proof.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def actual_joint(weights):
    p = [Fraction(a, sum(weights)) for a in weights]
    m = len(p)
    out = {(s, r): Fraction(0) for s in range(m) for r in range(1, m-s+1)}
    for k in range(1, m + 1):
        for seq in permutations(range(m), k):
            mass = Fraction(1)
            for i in seq:
                mass *= p[i]
            for s, i in enumerate(seq):
                out[s, k-s] += mass * p[i]
    return out


def collision_polynomial(weights):
    p = [Fraction(a, sum(weights)) for a in weights]
    m = len(p)
    b = []
    for r in range(m):
        b.append(sum((p[i]**2 *
                      sum((__import__('math').prod(p[j] for j in ss)
                           for ss in combinations([j for j in range(m) if j != i], r)),
                     Fraction(0)) for i in range(m)), Fraction(0)))
    q = [factorial(k-1)*b[k-1] for k in range(1, m+1)]
    return b, q


def check(weights):
    m = len(weights)
    actual = actual_joint(weights)
    b, q = collision_polynomial(weights)
    assert sum(k*q[k-1] for k in range(1,m+1)) == 1
    for (s,r),prob in actual.items():
        assert prob == q[s+r-1], ('joint', weights, (s,r),prob,q[s+r-1])
    for k in range(2,m):
        lhs = q[k-1]**2 * (m-k)
        rhs = q[k-2]*q[k] * (m-k+1)
        assert lhs>=rhs, ('Newton bound',weights,k,lhs,rhs)
        assert (lhs==rhs)==(len(set(weights))==1), ('rigidity',weights,k)
    for s in range(m):
      for ss in range(s+1,m):
        for r in range(1,m+1):
          for rr in range(r+1,m+1):
            A=actual.get((s,r),Fraction(0)); B=actual.get((ss,rr),Fraction(0))
            C=actual.get((s,rr),Fraction(0)); D=actual.get((ss,r),Fraction(0))
            assert A*B <= C*D, ('RR2',weights,s,ss,r,rr)
    # strict covariance on the identity transform
    E_s=sum(s*prob for (s,r),prob in actual.items())
    E_r=sum(r*prob for (s,r),prob in actual.items())
    cov=sum(s*r*prob for (s,r),prob in actual.items())-E_s*E_r
    assert cov<0, ('cov',weights,cov)
    return cov


def run():
    total=0
    for m in range(2,7):
        vectors=[[1]*m, list(range(1,m+1)), [2**j for j in range(m)], [5]+[1]*(m-1)]
        if m<=5:
            vectors += [[1]+list(t) for t in __import__('itertools').product(range(1,4),repeat=m-1)]
        for weights in vectors:
            check(weights)
            total+=1
    print(f'PASS: {total} exact-rational probability-vector checks, dimensions 2..6.')
    print('Each check independently enumerates ordered collision paths, verifies')
    print('the coefficient formula and sharp Newton bound, all 2x2 RR2')
    print('inequalities, equality rigidity, and strict negative covariance.')
    print('No finite computation is asserted to prove the universal theorem.')

if __name__=='__main__':run()
