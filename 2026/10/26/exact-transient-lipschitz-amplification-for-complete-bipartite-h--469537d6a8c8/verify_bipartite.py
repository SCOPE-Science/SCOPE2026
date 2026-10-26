#!/usr/bin/env python3
"""Reproduce exact graph-heat Lipschitz constants by independent finite optimal transport.
Requires numpy and scipy. The mathematical proof, including unbounded graph size,
is in RESULT.md rather than this finite test program.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog, minimize_scalar


def formula(a, b, t):
    M, m = max(a, b), min(a, b)
    return (2-2/M)*math.exp(-m*t)-(1-2/M)*math.exp(-(M+m)*t)


def matrix_and_metric(a, b, t):
    n=a+b
    adjacency=np.zeros((n,n))
    adjacency[:a,a:]=1
    adjacency[a:,:a]=1
    laplacian=np.diag(adjacency.sum(axis=1))-adjacency
    transition=expm(-t*laplacian)
    distance=np.full((n,n),2.0)
    distance[adjacency==1]=1.0
    np.fill_diagonal(distance,0.0)
    return transition,distance


def dual_wasserstein(row_difference,distance):
    n=len(row_difference)
    rows=[];bounds=[]
    # Gauge f(vertex 0)=0; every metric constraint is included.
    for i in range(n):
        for j in range(i+1,n):
            q=np.zeros(n-1)
            if i>0: q[i-1]+=1
            if j>0: q[j-1]-=1
            rows.extend((q,-q))
            bounds.extend((distance[i,j],distance[i,j]))
    result=linprog(-row_difference[1:],A_ub=np.array(rows),b_ub=np.array(bounds),
                   bounds=[(None,None)]*(n-1),method='highs')
    if not result.success:
        raise RuntimeError(result.message)
    return -result.fun


def witness(a,b):
    f=np.ones(a+b)
    if a>=b:
        f[:a]=0
        f[0]=2
    else:
        f[a:]=0
        f[a]=2
    return f


def test():
    largest_error=0.0
    count=0
    for a,b in itertools.product(range(1,8),repeat=2):
        for t in (0.,0.0001,0.1,0.7,2.):
            transition,distance=matrix_and_metric(a,b,t)
            difference=transition[0]-transition[a]
            got=dual_wasserstein(difference,distance)
            want=formula(a,b,t)
            largest_error=max(largest_error,abs(got-want))
            assert abs(got-want)<1e-11,(a,b,t,got,want)
            f=witness(a,b)
            assert max(abs(f[i]-f[j])/distance[i,j]
                       for i in range(a+b) for j in range(i+1,a+b)) <= 1+1e-12
            assert abs(abs(difference@f)-want)<1e-11,(a,b,t,'witness')
            count+=1
    for M,m in ((4,1),(5,2),(10,2),(18,5),(100,1)):
        assert M-m>2
        tstar=math.log((M-2)*(M+m)/(2*m*(M-1)))/M
        peak=2*(M-1)/(M+m)*(2*m*(M-1)/((M-2)*(M+m)))**(m/M)
        direct=minimize_scalar(lambda t:-formula(M,m,t),bounds=(0.,max(1.,2*tstar)),
                               method='bounded',options={'xatol':1e-13})
        assert abs(peak+direct.fun)<3e-9,(M,m,peak,-direct.fun)
        assert abs(formula(M,m,tstar)-peak)<1e-12
    print('PASS:',count,'independent LP/heat-matrix cases; max error',format(largest_error,'.3g'))
    print('PASS: all fixed potential tests and five peak-optimization tests')


if __name__=='__main__':
    test()
