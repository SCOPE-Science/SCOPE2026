"""Reproducibility checks for monomial cross-adjoint spectra; finite checks only."""
import math
import numpy as np
from scipy.special import gammaln


def log_norm(k, alpha):
    return 0.5 * (math.lgamma(alpha + 2) + math.lgamma(k + 1) - math.lgamma(k + alpha + 2))


def weight(k, m, n, alpha):
    return math.exp(log_norm(m*k, alpha) + log_norm(n*k, alpha) - 2*log_norm(k, alpha))


def graph(m, n, N):
    e = {n*k: m*k for k in range(1, N//max(m, n)+1)}
    assert len(e) == len(set(e.values()))
    return e


def run():
    count = 0
    for alpha in [-0.6, 0.0, 1.25, 2.75]:
        for m, n in [(2, 3), (3, 2), (2, 4), (4, 2), (6, 10), (10, 6), (2, 2), (3, 3)]:
            c = (m*n)**(-(alpha+1)/2)
            for k in [5000, 20000, 100000]:
                w = weight(k, m, n, alpha)
                assert abs(w/c - 1) < 0.004, (m, n, alpha, k, w, c)
                count += 1
            edges = graph(m,n,10000)
            assert all((j % n == 0 and out % m == 0) for j,out in edges.items())
            count += 1
    for m,n in [(2,3),(3,2),(4,6),(6,4),(6,10),(10,6)]:
        if m % n == 0 or n % m == 0: continue
        N=max(m,n)**4
        edges=graph(m,n,N)
        for v in list(edges)[:150]:
            seen=set()
            cur=v
            while cur in edges:
                assert cur not in seen, (m,n,cur)
                seen.add(cur)
                cur=edges[cur]
            count+=1
    for m,n in [(2,4),(4,2),(3,6),(6,3)]:
        alpha=0
        c=(m*n)**(-0.5)
        for h in [101,103,107]:
            t=max(m,n)//min(m,n)
            if h%t==0:continue
            # One-sided infinite chain has weights approaching a positive constant.
            assert abs(weight(h*t**12,m,n,alpha)/c-1)<0.0001
            count+=1
    print('PASS',count,'deterministic exact graph and floating asymptotic checks; infinity follows from proof')

if __name__=='__main__': run()
