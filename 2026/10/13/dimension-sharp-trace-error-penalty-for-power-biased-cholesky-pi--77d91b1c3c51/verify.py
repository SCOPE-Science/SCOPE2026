#!/usr/bin/env python3
"""Exact arithmetic checks for one-pivot power-biased Cholesky trace risk.

Python 3 standard library only. Finite checks are supplementary to the proof.
"""
from fractions import Fraction as F
from random import Random


def risk(K, q):
    """One-pivot expected residual trace for positive-diagonal PSD K."""
    n = len(K)
    d = [K[i][i] for i in range(n)]
    assert all(x > 0 for x in d)
    weights = [x ** q for x in d]
    den = sum(weights)
    errors = [sum(K[k][k] - K[k][j]*K[j][k]/d[j]
                  for k in range(n)) for j in range(n)]
    assert min(errors) >= 0
    return sum(w * e for w, e in zip(weights, errors)) / den


def two_block(r, s, t):
    """Rank-two matrix diag(t J_r, J_s)."""
    n = r+s
    return [[t if i < r and j < r else
             F(1) if i >= r and j >= r else F(0)
             for j in range(n)] for i in range(n)]


def two_block_risk(r,s,t,q):
    return F(r*s)*t*(t**(q-1)+1)/(r*t**q+s)


def gram(vectors):
    return [[sum(a*b for a,b in zip(v,w)) for w in vectors]
            for v in vectors]


def run():
    checks = 0
    for r in range(1,4):
        for s in range(1,9):
            for t in [F(1,3),F(1),F(3,2),F(2),F(4),F(7)]:
                K=two_block(r,s,t)
                for q in range(1,6):
                    expected=two_block_risk(r,s,t,q)
                    actual=risk(K,q)
                    assert actual == expected,(r,s,t,q,actual,expected)
                    checks += 1
                    if q>1:
                        ratio=actual/risk(K,1)
                        assert ratio**q <= (r+s)**(q-1)
                        checks += 1
    rng=Random(140419)
    for n in range(2,9):
        for trial in range(30):
            vectors=[[F(rng.randint(-3,3)) for k in range(3)] for j in range(n)]
            if any(not any(v) for v in vectors):
                continue
            K=gram(vectors)
            E1=risk(K,1)
            if not E1: # rank one gives no residual trace
                continue
            for q in range(2,6):
                Eq=risk(K,q)
                assert (Eq/E1)**q <= n**(q-1),(n,q,K)
                checks += 1
    # Explicit dimension-17 witness, exact in rational arithmetic.
    K=two_block(1,16,F(4))
    assert risk(K,1)==F(32,5)
    assert risk(K,2)==F(10)
    assert risk(K,2)/risk(K,1)==F(25,16)
    checks += 3
    # A non-degenerate SPD perturbation approaches the rank-two witness.
    Kp=[[K[i][j]+(F(1,100000) if i==j else F(0))
         for j in range(17)] for i in range(17)]
    gap=abs(risk(Kp,2)/risk(Kp,1)-F(25,16))
    assert gap < F(1,100)
    checks += 1
    # Exact optimum for two blocks with squared-diagonal weighting:
    # fixed r,s: max ratio attained at t=sqrt(s/r).
    # For (r,s)=(1,16), t=4 is exact and equals 1/2+n/(4 sqrt(n-1)).
    assert F(25,16) == F(1,2)+F(17,16)
    checks += 1
    print(f"PASS {checks} exact-rational checks; no proof of continuous parameters by enumeration")

if __name__=='__main__':
    run()
