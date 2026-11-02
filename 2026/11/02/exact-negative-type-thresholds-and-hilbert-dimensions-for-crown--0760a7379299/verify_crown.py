#!/usr/bin/env python3
"""Supplementary finite checks for powered crown-graph distance matrices.

This script is numerical corroboration, not a substitute for the proof for all n.
Requires Python 3 with NumPy and SciPy.
"""
import math
from collections import deque
import numpy as np
from scipy.optimize import brentq


def crown_bfs(n):
    """Compute shortest paths using only the edge definition, not the formula."""
    N = 2*n
    adj = [[] for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].append(n+j)
                adj[n+j].append(i)
    d = np.empty((N,N), dtype=int)
    for start in range(N):
        d[start] = -1
        d[start,start]=0
        Q = deque([start])
        while Q:
            u=Q.popleft()
            for v in adj[u]:
                if d[start,v] == -1:
                    d[start,v] = d[start,u]+1
                    Q.append(v)
        assert np.all(d[start] >= 0)
    return d


def predicted_eigenvalues(n,p):
    a,b=2.0**p,3.0**p
    return np.sort(np.array([ (n-1)*(a+1)+b,
                   (n-1)*(a-1)-b ]+
                   [b-a-1]*(n-1) + [1-a-b]*(n-1)))


def endpoint(n):
    if n <=4: return 1.0
    return brentq(lambda p:(n-1)*math.expm1(math.log(2)*p)-math.exp(math.log(3)*p),
                  1.e-12,1.0,xtol=1.e-14)


def selftest():
    assertions=0
    for n in [3,4,5,6,7,8,10,12,16,20]:
        d=crown_bfs(n)
        assert np.all(d.diagonal()==0)
        for i in range(n):
            assert d[i,n+i]==3
            for j in range(n):
                if i!=j:
                    assert d[i,n+j]==1
                    assert d[i,j]==2
        assertions+=1
        pstar=endpoint(n)
        for p in (0, 0.2, 0.5, 0.999, 1, 1.25, pstar, max(1e-5,pstar-0.0001)):
            matrix=d.astype(float)**p if p>0 else (d>0).astype(float)
            found=np.linalg.eigvalsh(matrix)
            expected=predicted_eigenvalues(n,p)
            assert np.max(np.abs(found-expected)) < 1e-10 * (n+1), (n,p,found,expected)
            assertions += 1
            H=np.eye(2*n)-np.ones((2*n,2*n))/(2*n)
            gram=-0.5*H@matrix@H
            eig=np.linalg.eigvalsh(gram)
            if p<=pstar-1.e-6:
                # The sole zero corresponds to translation (all ones).
                assert eig[-2] > 1e-9, (n,p,eig)
                assertions += 1
            if p > pstar+1e-6:
                assert eig[0] < -1e-9, (n,p,eig)
                assertions += 1
        # Endpoint multiplicity is determined by exact block-eigenvalue formulas;
        # floating-point rank is only a supplementary check.
        a,b=2**pstar,3**pstar
        vals=[(n-1)*(a-1)-b] + [b-a-1]*(n-1) + [1-a-b]*(n-1)
        zerocnt=sum(abs(v)<1e-10 for v in vals)
        assert zerocnt == {3:2,4:4}.get(n,1), (n,zerocnt)
        assertions+=1
    for n in [30,50,100,300,1000]:
        N=n-1
        l2=math.log(2); l3=math.log(3)
        approx=1/(l2*N)+(l3/l2**2-1/(2*l2))/N**2
        actual=endpoint(n)
        assert abs(actual-approx)*N**3 < 4, (n,actual,approx)
        assert actual>math.log2(n/(n-1)), n
        assertions+=2
    print('PASS: %d supplementary assertions' % assertions)
    for n in [3,4,5,6,8,10,20,100]:
        print('n=%d, critical exponent=%.12f, critical affine dimension=%d' % (
            n,endpoint(n), 3 if n in (3,4) else 2*n-2))

if __name__=='__main__':
    selftest()
