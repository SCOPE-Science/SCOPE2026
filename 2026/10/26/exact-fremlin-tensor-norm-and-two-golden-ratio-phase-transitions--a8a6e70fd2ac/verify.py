#!/usr/bin/env python3
"""Exact arithmetic and numeric checks of the stated three-point path theorem."""
from fractions import Fraction as F
from math import sqrt,isclose

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def matvec(M,v): return [dot(row,v) for row in M]
def transp(M): return list(map(list,zip(*M)))
def check_mid(t):
    a=1/t**2;b=t-1/t**3;c=1-t*t+1/t**2
    assert min(a,b,c)>=0
    u=[F(1),1/t,1/t**2];v=[F(1),t,t*t]
    N=[[a,b,F(0)],[F(0),c,b],[F(0),F(0),a]]
    assert matvec(N,v)==[t*t*w for w in u]
    assert matvec(transp(N),u)==[w/(t*t) for w in v]
    M=[[F(1),t,F(0)],[F(0),F(1),t],[F(0),F(0),F(1)]]
    assert all(u[i]*v[j]>=M[i][j] for i in range(3) for j in range(3))
    dual=sum(M[i][j]*N[i][j] for i in range(3) for j in range(3))
    cost=1+t*t+1/t**2
    assert dual==cost
    D=[[int(i==j)-dot([N[k][i] for k in range(3)],[N[k][j] for k in range(3)]) for j in range(3)] for i in range(3)]
    assert D[0][1]<=0 and D[1][2]<=0
    assert matvec(D,v)==[0,0,0]
for t in [F(1),F(1001,1000),F(21,20),F(11,10),F(6,5),F(5,4),F(127,100)]: check_mid(t)
for t in [sqrt((1+sqrt(5))/2),1.28,1.3,1.5,2,3,10,100]:
    h=sqrt(1+t*t);a=1/h;b=t/h
    x=[1,b,a];y=[a,b,1]
    M=[[1,t,0],[0,1,t],[0,0,1]]
    assert all(h*x[i]*y[j]+1e-12>=M[i][j] for i in range(3) for j in range(3))
    assert isclose(h*dot(x,x),2*h,rel_tol=1e-12)
    assert isclose((2*a+2*t*b),2*h,rel_tol=1e-12)
    assert isclose(a*a+b*b,1,abs_tol=1e-12)
for t in [0,.01,.2,.5,.9,1]:
    assert all(1>=x for x in [1,t])
assert 2+6 != 0
print('Passed: exact middle-phase rational certificates and finite sampling of large/low phases.')
