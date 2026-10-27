"""Independent exact and finite-state checks for a two-colour boundary-driven exclusion chain.

Run: python check.py (requires numpy and scipy).
"""
from fractions import Fraction as Q
from itertools import product
from math import acosh, exp, isclose, sinh, cosh
import numpy as np
from scipy.linalg import solve

A, B, U = Q(1), Q(1, 2), Q(1)
T, M, DELTA = Q(1, 2), Q(1, 4), Q(3, 10)
LEFT = (T + DELTA/2 - M)/2, (T + DELTA/2 + M)/2
RIGHT = (T - DELTA/2 + M)/2, (T - DELTA/2 - M)/2
assert LEFT == (Q(1,5),Q(9,20))
assert RIGHT == (Q(3,10),Q(1,20))
assert 0 < A-B and U >= 2*B
z = 3 - 2*np.sqrt(2)
R = (A+B)*DELTA / ((A-B)*M)
assert R == Q(18,5)


def profiles(n):
    L=n+1
    # Direct exact solution of the finite difference boundary-value problem.
    # Difference: M[j+1] - 6 M[j] + M[j-1]=0.
    coef=2+2*U/(A-B)
    matrix=[[Q(0) for _ in range(n)] for _ in range(n)]
    target=[Q(0) for _ in range(n)]
    for j in range(n):
        matrix[j][j]=-coef
        if j>0: matrix[j][j-1]=Q(1)
        else: target[j] += M
        if j<n-1: matrix[j][j+1]=Q(1)
        else: target[j] -= M
    for j in range(n): matrix[j].append(target[j])
    for i in range(n):
        k=next(k for k in range(i,n) if matrix[k][i])
        matrix[i],matrix[k]=matrix[k],matrix[i]
        pivot=matrix[i][i]
        matrix[i]=[v/pivot for v in matrix[i]]
        for k in range(n):
            if k!=i:
                v=matrix[k][i]
                matrix[k]=[x-v*y for x,y in zip(matrix[k],matrix[i])]
    color=[-M]+[matrix[j][-1] for j in range(n)]+[M]
    total=[T+DELTA/2-DELTA*Q(j,L) for j in range(L+1)]
    first=[(t+c)/2 for t,c in zip(total,color)]
    second=[(t-c)/2 for t,c in zip(total,color)]
    currents=[A*(first[j]-first[j+1])+B*(second[j]-second[j+1]) for j in range(L)]
    return first,second,currents

exact3=[Q(1,240),Q(11,240),Q(11,240),Q(1,240)]
exact4=[Q(-7,1025),Q(147,4100),Q(43,1025),Q(147,4100),Q(-7,1025)]
assert profiles(3)[2]==exact3
assert profiles(4)[2]==exact4
checks=2

for n in range(1,61):
    p1,p2,j=profiles(n)
    assert all(0<=x<=1 for x in p1+p2)
    assert all(0<=x+y<=1 for x,y in zip(p1,p2))
    assert all(j[k]==j[-k-1] for k in range(len(j)))
    assert sum(j)==((A+B)*DELTA - 2*(A-B)*M)/2
    assert j[0]==min(j)
    assert all(j[k]>j[0] for k in range(1,len(j)-1)) if n>=2 else True
    F=(n+1)*(1-z)*(1+z**n)/(1-z**(n+1))
    assert (j[0]>0)==(F<float(R))
    checks+=7

# The per-edge jump generators are independently constructed from elementary
# substitution rules, with the neutral state unchanged by colour reversal.
flip={0:0,1:2,2:1}

def stationary_means(n):
    configs=list(product((0,1,2),repeat=n))
    ids={s:i for i,s in enumerate(configs)}
    gen=np.zeros((len(configs),len(configs)))
    reservoirs=(LEFT,RIGHT)
    for idx,s in enumerate(configs):
        def jump(dst,rate):
            if dst!=s and rate:
                gen[idx,ids[dst]]+=float(rate)
        for edge in range(n-1):
            dst=list(s);dst[edge:edge+2]=s[edge+1],s[edge]
            jump(tuple(dst),A)
            dst=list(s);dst[edge:edge+2]=flip[s[edge+1]],flip[s[edge]]
            jump(tuple(dst),B)
        for site,rho in [(0,reservoirs[0]),(n-1,reservoirs[1])]:
            ra,rb=rho;rv=1-ra-rb
            old=s[site]
            if old==0: variants=[(1,A*ra+B*rb),(2,B*ra+A*rb)]
            elif old==1: variants=[(0,(A+B)*rv),(2,B*ra+A*rb)]
            else: variants=[(0,(A+B)*rv),(1,A*ra+B*rb)]
            for new,rate in variants:
                dst=list(s);dst[site]=new
                jump(tuple(dst),rate)
        gen[idx,idx]=-sum(gen[idx,:])
    assert np.max(np.abs(gen.sum(axis=1)))<1e-11
    H=gen.T.copy();H[-1,:]=1
    q=np.zeros(len(configs));q[-1]=1
    dist=solve(H,q,assume_a='gen')
    assert np.min(dist)>-1e-11 and abs(np.sum(dist)-1)<1e-11
    pa=[sum(dist[i] for i,s in enumerate(configs) if s[j]==1) for j in range(n)]
    pb=[sum(dist[i] for i,s in enumerate(configs) if s[j]==2) for j in range(n)]
    return pa,pb

for n in (1,2,3,4):
    pa,pb=stationary_means(n)
    xa,xb,_=profiles(n)
    for j in range(n):
        assert isclose(pa[j],float(xa[j+1]),abs_tol=3e-11)
        assert isclose(pb[j],float(xb[j+1]),abs_tol=3e-11)
        checks+=2

# Analytic cutoff monotonicity and threshold values checked independently.
lam=acosh(1+float(U/(A-B)))
def F_cont(L):
    return 2*L*sinh(lam/2)*cosh(lam*(L-1)/2)/sinh(lam*L/2)
def dlogF(L):
    h=1e-4
    return (np.log(F_cont(L+h))-np.log(F_cont(L-h)))/(2*h)
for L in np.linspace(2,100,1000):
    assert dlogF(L)>0
    checks+=1
assert abs(F_cont(4)-10/3)<1e-12
assert abs(F_cont(5)-170/41)<1e-12
assert F_cont(4)<float(R)<F_cont(5)
checks+=3
print(f'PASS {checks} independent analytic, exact-rational, and stationary-generator checks')
print(f'Cutoff test: F_4={F_cont(4):.12f} < R={float(R):.12f} < F_5={F_cont(5):.12f}')
print('N=3 currents:', ', '.join(map(str,exact3)))
print('N=4 currents:', ', '.join(map(str,exact4)))
