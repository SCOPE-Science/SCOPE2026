#!/usr/bin/env python3
"""Independent finite checks for the pendant-coupling average-mixing theorem.

Usage: python3 verify.py   (requires numpy; optional networkx is not needed)
Finite tests corroborate but cannot certify the unrestricted analytic identity.
"""
import numpy as np
from math import isclose


def avg_and_projectors(H):
    eig, V = np.linalg.eigh(H)
    groups = []
    for i, val in enumerate(eig):
        if not groups or abs(val - groups[-1][0]) > 1e-8:
            groups.append([float(val), np.zeros_like(H, dtype=float)])
        groups[-1][1][:] += np.outer(V[:, i], V[:, i])
    M = sum((E * E for _, E in groups), np.zeros_like(H, dtype=float))
    return M, groups


def check(A, g):
    n = len(A)
    S, groups = avg_and_projectors(A)
    T = sum(((t*t/(t*t+4*g*g)) * E*E for t, E in groups),
            np.zeros_like(A))
    predicted = np.block([[(S+T)/2, (S-T)/2], [(S-T)/2, (S+T)/2]])
    lifted = np.block([[A,g*np.eye(n)],[g*np.eye(n),np.zeros_like(A)]])
    observed, _ = avg_and_projectors(lifted)
    err = np.max(np.abs(predicted-observed))
    if err > 3e-9:
        raise AssertionError((n,g,err))
    def rank(X):
        return int(np.linalg.matrix_rank(X, tol=1e-8))
    rs,rt,rc = rank(S),rank(T),rank(observed)
    assert rc==rs+rt
    if abs(np.linalg.det(A))>1e-8:
        assert rc==2*rs
    return err, rc


def path(n):
    A=np.zeros((n,n))
    for i in range(n-1):A[i,i+1]=A[i+1,i]=1
    return A


def clique(n):
    return np.ones((n,n))-np.eye(n)


def cycle(n):
    A=path(n); A[0,-1]=A[-1,0]=1;return A


def main():
    rng=np.random.default_rng(410041)
    cases=[np.zeros((1,1))]
    for n in range(2,10):
        cases.extend([path(n),clique(n)])
        if n>=3: cases.append(cycle(n))
    for n in range(2,8):
        for _ in range(12):
            X=rng.integers(0,2,(n,n));
            A=np.triu(X,1); A=A+A.T
            cases.append(A.astype(float))
    tested=0; maxerr=0
    for A in cases:
        for g in (0.25,1.0,2.75):
            err,_=check(A,g)
            tested+=1;maxerr=max(maxerr,err)
    for n in range(1,17):
        for g in (0.5,1,3):
            _,r=check(path(n),g)
            assert r==n,(n,g,r)
    gaps=0
    for n in range(3,12):
        for g in (0.5,1.0,3.0):
            A=clique(n);H=np.block([[A,g*np.eye(n)],[g*np.eye(n),np.zeros((n,n))]])
            M,_=avg_and_projectors(H)
            least=float(np.linalg.eigvalsh(M)[0])
            expected=(n-2)/(n*(1+4*g*g))
            assert abs(least-expected)<2e-11,(n,g,least,expected)
            gaps+=1
    print('VERIFY_OK numerical_graph_cases=%d path_cases=%d clique_gap_cases=%d max_abs_error=%.3e' %
          (tested,16*3,gaps,maxerr))

if __name__=='__main__':main()
