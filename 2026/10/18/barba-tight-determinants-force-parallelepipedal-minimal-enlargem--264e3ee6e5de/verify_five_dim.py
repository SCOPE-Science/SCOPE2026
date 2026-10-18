"""Exact rational checks for an explicit Barba-tight five-dimensional example.

These checks are finite corroboration of the separate analytic proof.
"""
from fractions import Fraction as F
from itertools import product

n=5
A=[[1-2*(i==j) for j in range(n)] for i in range(n)]
V=[[F(A[i][j],4)-F(1,12) for j in range(n)] for i in range(n)]
for i,j in product(range(n),repeat=2):
    assert sum(F(A[k][i])*F(A[k][j]) for k in range(n)) == (5 if i==j else 1)
    assert sum(F(A[k][i])*V[k][j] for k in range(n)) == (1 if i==j else 0)
for a,b in product([F(-3),F(-1),F(0),F(1),F(2),F(5,3)],repeat=2):
    actual=sum(abs(a*V[k][0]+b*V[k][1]) for k in range(n))
    exact=abs(a+b)/2+(abs(2*a-4*b)+abs(4*a-2*b))/12
    assert actual==exact,(a,b,actual,exact)
for q in (3,5,7,9,11,13):
    n=(q*q+1)//2
    assert 2*n-1==q*q and n%4==1
    Npp=(n+1+2*q)//4
    Nmm=(n+1-2*q)//4
    k=(n-1)//4
    assert Npp+Nmm+2*k==n
    u=F(q-1,q*(n-1)); w=F(q+1,q*(n-1))
    assert Npp*u+Nmm*w==F(1,2)
    assert k*u==F(q-1,4*q) and k*w==F(q+1,4*q)
    g0=(F(1,2),F(1,2))
    g1=(F(q-1,4*q),-F(q+1,4*q))
    g2=(-F(q+1,4*q),F(q-1,4*q))
    det=lambda x,y:x[0]*y[1]-x[1]*y[0]
    assert [abs(det(g0,g1)),abs(det(g0,g2)),abs(det(g1,g2))] == [F(1,4),F(1,4),F(1,4*q)]
print('PASS: exact dimension-five Barba example, pair norm, and parametric algebra')
