#!/usr/bin/env python3
"""Independent finite checks for radial height-two tree p-negative type.

Requires Python 3.10+, numpy, scipy. Run: python artifacts/check_numeric.py
This is supplementary numerical testing, not an infinite-family proof.
"""
from collections import deque
import math

import numpy as np
from scipy.optimize import brentq


def target(k, m, p):
    a, b, c = (2.0**p, 3.0**p, 4.0**p)
    U = k - (k - 1)*a/2
    V = math.sqrt(m)*((k - 1) + k*a - (k - 1)*b)/2
    W = (m + 1)*a/2 + (k - 1)*m*(a - c/2)
    return np.array([[U, V], [V, W]])


def diff_block(m, p):
    a,b,c=(2.0**p,3.0**p,4.0**p)
    return np.array([[a/2, math.sqrt(m)*(b-1)/2],
                     [math.sqrt(m)*(b-1)/2, (m*c+(1-m)*a)/2]])


def distances(k, m):
    n=1+k+k*m
    edges=[(0, 1+i) for i in range(k)]
    edges += [(1+i, 1+k+i*m+j) for i in range(k) for j in range(m)]
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    D=np.zeros((n,n), dtype=int)
    for i in range(n):
        D[i,:]=-1
        D[i,i]=0
        q=deque([i])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if D[i,v]<0:
                    D[i,v]=D[i,u]+1
                    q.append(v)
        assert min(D[i])>=0
    return D


def gram_from_dist(D,p):
    d0=(D[0,1:].astype(float))**p
    return (d0[:,None]+d0[None,:] - D[1:,1:].astype(float)**p)/2


def critical(k,m):
    if (k,m)==(2,1):
        return 2.0
    bound = 1+math.log2(k/(k-1))
    def f(p):
        return np.linalg.det(target(k,m,p))
    upper=bound-1.0e-7 if k==2 else bound
    assert f(1)>0 and f(upper)<0,(k,m,upper,f(upper))
    return brentq(f,1,upper,xtol=1e-13)


def run():
    comparisons=0; critical_checks=0; spectral_checks=0; limit_checks=0
    for k in range(2,10):
        for m in range(1,9):
            D=distances(k,m)
            threshold=critical(k,m)
            upper=1+math.log2(k/(k-1))
            assert 1<threshold<=upper+1e-12
            for p in (1,1.03,1.15,1.31,1.5,1.8,1.999):
                if p>=2:continue
                G=gram_from_dist(D,p)
                actual=np.linalg.eigvalsh(G)
                predicted=np.concatenate((
                    np.full(k*(m-1),2.0**(p-1)),
                    np.tile(np.linalg.eigvalsh(diff_block(m,p)),k-1),
                    np.linalg.eigvalsh(target(k,m,p))
                ))
                assert np.max(np.abs(np.sort(actual)-np.sort(predicted)))<5e-8,(k,m,p)
                comparisons+=1
                # Independent sign testing below and above the exact threshold.
                if p < threshold-1e-5:
                    assert actual[0]>-2e-8,(k,m,p,threshold,actual[0])
                if p > threshold+1e-5:
                    assert actual[0]<2e-8,(k,m,p,threshold,actual[0])
                spectral_checks+=1
            if (k,m)!=(2,1):
                at=np.linalg.eigvalsh(gram_from_dist(D,threshold))
                assert abs(at[0])<2e-7,(k,m,threshold,at[0])
                assert at[1]>1e-7,(k,m,threshold,at[1])
                critical_checks+=1
            else:
                at=np.linalg.eigvalsh(gram_from_dist(D,2.0))
                assert len(at)==4 and abs(at[0])<1e-7 and abs(at[1])<1e-7 and abs(at[2])<1e-7
                critical_checks+=1
    for k in range(2,9):
        c = (5*k-4)*math.log(2)-3*(k-1)*math.log(3)
        assert c>0
        for m in (100,1000,10000):
            p=critical(k,m)
            assert abs((p-1)*m*c - 1)<.1,(k,m,p,c)
            limit_checks+=1
    assert abs(critical(3,2)-1.4190935098)<1e-6
    assert abs(critical(2,2)-1.5271731077)<1e-6
    print(f"CHECK_OK: {comparisons} full spectral comparisons; {critical_checks} endpoint multiplicity checks; {spectral_checks} phase checks; {limit_checks} asymptotic checks")


if __name__=='__main__':
    run()
