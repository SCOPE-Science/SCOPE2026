#!/usr/bin/env python3
"""Exhaustive checks for the SCOPE run 001 spectral-radius theorem.

Enumerates all labelled simple digraphs with n+2 arcs for n=3,4,5,
with and without loops; filters strongly connected digraphs; computes
adjacency spectral radius; and compares the maximum to the proposed
flower extremizer.
"""
from itertools import combinations
import numpy as np


def strongly_connected(n, edges):
    adj=[[] for _ in range(n)]
    radj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); radj[v].append(u)
    def reach(g):
        seen={0}; stack=[0]
        while stack:
            u=stack.pop()
            for v in g[u]:
                if v not in seen:
                    seen.add(v); stack.append(v)
        return len(seen)==n
    return reach(adj) and reach(radj)


def spectral_radius(n, edges):
    A=np.zeros((n,n),dtype=float)
    for u,v in edges:
        A[u,v]=1.0
    return float(np.max(np.abs(np.linalg.eigvals(A))))


def bisect_root(f, lo=0.0, hi=1.0, iters=100):
    flo=f(lo); fhi=f(hi)
    assert flo*fhi <= 0
    for _ in range(iters):
        mid=(lo+hi)/2
        fm=f(mid)
        if flo*fm <= 0:
            hi=mid; fhi=fm
        else:
            lo=mid; flo=fm
    return (lo+hi)/2


def predicted(n, loops):
    if loops:
        r=bisect_root(lambda x: 1-x-x*x-x**(n-1))
        return 1/r
    if n==3:
        return (1+5**0.5)/2
    r=bisect_root(lambda x: 1-2*x*x-x**(n-2))
    return 1/r


def enumerate_case(n, loops):
    universe=[(i,j) for i in range(n) for j in range(n) if loops or i!=j]
    k=n+2
    best=-1.0; count=0; strong_count=0
    tol=1e-9
    for idxs in combinations(range(len(universe)), k):
        edges=[universe[i] for i in idxs]
        if not strongly_connected(n, edges):
            continue
        strong_count += 1
        rho=spectral_radius(n, edges)
        if rho > best + tol:
            best=rho; count=1
        elif abs(rho-best) <= tol:
            count += 1
    return best, count, strong_count


def main():
    for loops in (True, False):
        print("loops_allowed" if loops else "loopless")
        for n in (3,4,5):
            best,count,strong_count=enumerate_case(n,loops)
            pred=predicted(n,loops)
            print(f"n={n}: max={best:.15f}; predicted={pred:.15f}; "
                  f"labelled_maximizers={count}; strongly_connected={strong_count}; "
                  f"abs_error={abs(best-pred):.3e}")

if __name__ == '__main__':
    main()
