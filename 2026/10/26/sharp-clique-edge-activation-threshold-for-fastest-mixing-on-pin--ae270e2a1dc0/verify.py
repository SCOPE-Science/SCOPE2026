"""Reproducible mathematical checks for optimal weighted pineapple diffusion.

Requires Python 3 and NumPy. This is finite verification supporting an analytic proof;
it is not an exhaustive argument for all graph sizes or weight assignments.
"""
import math
import random
import numpy as np


def graph_laplacian(n, m, a, b, c):
    N = n + m
    L = np.zeros((N, N))
    edges = []
    for i in range(1, n):
        edges.append((0, i, a))
    for i in range(1, n):
        for j in range(i + 1, n):
            edges.append((i, j, b))
    for i in range(n, N):
        edges.append((0, i, c))
    for i, j, w in edges:
        L[i, j] -= w
        L[j, i] -= w
        L[i, i] += w
        L[j, j] += w
    return L


def coefficients(n, m):
    s = math.sqrt(n*(n-1)/2)
    if m < s:
        q = m*(n-1)/s
        a = (m + 1 + q)/(n+m)
        b = (1-a)/(n-1)
        c = (n+s)/(n+m)
        D = n+m-1 - (s-m)**2/(n+m)
    else:
        a,b,c = 1.,0.,1.
        D = n+m-1.
    return a,b,c,D


def spectral(n,m,a,b,c):
    d = n-1
    trace = n*a+(m+1)*c
    disc = trace*trace-4*(n+m)*a*c
    low = (trace-math.sqrt(max(disc,0)))/2
    high = (trace+math.sqrt(max(disc,0)))/2
    return sorted([0.,low, high]+[c]*(m-1)+[a+d*b]*(n-2))


def budget(n,m,a,b,c):
    d=n-1
    return d*a+d*(d-1)/2*b+m*c


def check():
    checks=0
    for n in range(3,19):
        for m in range(2,17):
            a,b,c,D=coefficients(n,m)
            assert b>=-2e-14 and a>0 and c>0
            assert abs(budget(n,m,a,b,c)-D)<3e-12
            assert abs(np.linalg.eigvalsh(graph_laplacian(n,m,a,b,c))[1]-1)<2e-11
            assert abs(spectral(n,m,a,b,c)[1]-1)<2e-11
            if m<math.sqrt(n*(n-1)/2):
                assert b>0 and a<1 and c>1 and D<n+m-1
            else:
                assert b==0 and D==n+m-1
            checks+=4
    rng=random.Random(271828)
    for n in range(3,12):
        for m in range(2,9):
            a,b,c,D=coefficients(n,m)
            for j in range(13):
                # Nonexchangeable conductances; support all graph edges.
                L=np.zeros((n+m,n+m))
                ws=[]; endpoints=[]
                for i in range(1,n): endpoints.append((0,i))
                for i in range(1,n):
                    for k in range(i+1,n): endpoints.append((i,k))
                for i in range(n,n+m):endpoints.append((0,i))
                for i,k in endpoints:
                    w=math.exp(rng.uniform(-4,4));ws.append(w)
                scale=D/sum(ws)
                for (i,k),w in zip(endpoints,ws):
                    w*=scale
                    L[i,i]+=w;L[k,k]+=w;L[i,k]-=w;L[k,i]-=w
                lam=np.linalg.eigvalsh(L)[1]
                assert lam<=1+1e-9,(n,m,lam)
                checks+=1
    # The exact degeneracy where m^2=n(n-1)/2 holds at n=9,m=6.
    assert coefficients(9,6)[1]==0.
    print(f'PASS {checks} finite structural/spectrum/budget/asymmetric comparisons')

if __name__=='__main__': check()
