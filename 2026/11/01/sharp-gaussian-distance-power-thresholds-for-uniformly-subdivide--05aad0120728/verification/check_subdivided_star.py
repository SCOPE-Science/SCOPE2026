#!/usr/bin/env python3
"""Reproduce the subdivided-star Gaussian power threshold checks.

Requires only Python 3 standard library. Numerical checks complement the analytic proof.
"""
import math

L2 = math.log(2.0)

def data(m, p):
    v = 2.0 ** p
    t = math.sqrt(v)
    u = v / 2.0
    w = 3.0 ** p
    a = m - (m - 1) * u
    b = u - (m - 1) * (w - 1.0 - v) / 2.0
    diagonal = ((1.0, u), (u, v))
    off = ((1.0-u, (1.0+v-w)/2.0), ((1.0+v-w)/2.0, v-v*v/2.0))
    q = tuple(tuple(diagonal[i][j] - off[i][j] for j in range(2)) for i in range(2))
    pblock = ((a,b),(b,v*a))
    return diagonal,off,q,pblock,t*a+b

def eig2(M):
    a,b=M[0]
    _,d=M[1]
    h=math.hypot(a-d,2*b)
    return ((a+d-h)/2.0,(a+d+h)/2.0)

def critical(m):
    if m<=2:
        return 2.0
    upper=math.log2(2.0*m/(m-1))
    lo,hi=1.0,upper
    for _ in range(72):
        mid=(lo+hi)/2
        if data(m,mid)[4]>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def distance(x,y):
    # A vertex is (arm, depth), with arm -1 for the central root.
    if x==y:return 0.0
    if x[0]==-1:return float(y[1])
    if y[0]==-1:return float(x[1])
    if x[0]==y[0]:return float(abs(x[1]-y[1]))
    return float(x[1]+y[1])

def gram(m,p):
    nodes=[(i,j) for i in range(m) for j in (1,2)]
    return [[(a[1]**p+b[1]**p-distance(a,b)**p)/2 for b in nodes] for a in nodes]

def analytic_gram(m,p):
    D,O,*_=data(m,p)
    return [[(D if i//2==j//2 else O)[i%2][j%2]
            for j in range(2*m)] for i in range(2*m)]

checks=0
for m in range(2,18):
    root=critical(m)
    if m==2:
        assert abs(root-2)<1e-13
        checks+=1
    else:
        assert 1<root<math.log2(2*m/(m-1))<2
        assert abs(data(m,root)[4])<2e-10
        Q,P,*_=data(m,root)[2:]
        assert eig2(Q)[0]>0.1
        assert abs(eig2(P)[0])<4e-10
        assert eig2(P)[1]>0
        t=2**(root/2)
        assert abs(P[0][0]*t+P[0][1])<3e-10
        assert abs(P[1][0]*t+P[1][1])<3e-10
        star=math.log2(2*m/(m-1))
        assert eig2(data(m,star)[3])[0]<-1e-7
        assert eig2(data(m,(root+star)/2)[3])[0]<-1e-7
        assert eig2(data(m,1+(root-1)/2)[3])[0]>0
        checks+=10
    for p in (1.0,1.07,1.3,1.6,1.95,2.0):
        G=gram(m,p)
        A=analytic_gram(m,p)
        assert max(abs(G[i][j]-A[i][j])
                   for i in range(2*m) for j in range(2*m))<8e-13
        checks+=1
        D,O,Q,P,_=data(m,p)
        # Exact S_m block diagonalization of a constant-diagonal/off-diagonal array.
        assert abs(sum(G[0][j] for j in range(0,2*m,2))-P[0][0])<1e-11
        assert abs(G[0][0]-G[0][2]-Q[0][0])<1e-11
        checks+=2
for m in (20,30,100,500,1000,3000,10000):
    c=(1+math.sqrt(2))/(math.sqrt(2)*L2+(3*math.log(3)-2*L2)/2)
    root=critical(m)
    if m>=1000:
        assert abs(m*(root-1)-c)<0.007
        checks+=1
assert critical(3)>critical(4)>critical(5)>critical(6)>critical(7)
checks+=1
print('PASS:',checks,'deterministic assertions; one-dimensional threshold, full basepoint Gram blocks,')
print('endpoint null directions, star comparison, strict rank loss and large-arm constant.')
print('critical_exponents:',[(m,round(critical(m),12)) for m in (2,3,4,5,8,16,100)])
print('asymptotic_constant:',format(c,'.12f'))
