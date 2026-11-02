#!/usr/bin/env python3
"""Exact finite checks for a uniform Waring-rank construction (not an infinite proof)."""
from math import factorial
import sympy as sp
X,Y,Z,x,y,z,t=sp.symbols('X Y Z x y z t')
q1=Y**2-Z**2; q2=X*Y
Q=sp.Matrix([[0,t/2,0],[t/2,1,0],[0,0,-1]])
assert sp.factor(Q.det())==t**2/4
for d in [5,6,7,8,9,12]:
    n=d+1
    g=sp.expand(((y+z)**n+(-1)**n*(y-z)**n)/2)
    f=sp.expand(n*x**d*z+g)
    assert sp.expand(sp.diff(f,y,2)-sp.diff(f,z,2))==0
    assert sp.expand(sp.diff(f,x,y))==0
    assert sp.expand(sp.diff(f,x,d)-sp.diff(f,z,d))==0
    h=X**d-Z**d
    G=X**(d+1)+Z**(d-1)*q1
    rhs=X*h+(X*Y)*(Y*Z**(d-2))+q1*(Z**(d-1)-X*Z**(d-2))
    assert sp.expand(G-rhs)==0
    # In the Z=1 chart the point equations split into d+1 roots of unity and two points (0,+/-1).
    assert sp.gcd(sp.Poly(X**n-1,X),sp.Poly(n*X**(n-1),X))==1
    assert sp.expand(G.subs({Y:0,Z:1})-(X**n-1))==0
    assert sp.expand(G.subs({X:0,Z:1})-(Y**2-1))==0
    assert sp.expand((Y*q1).subs({X:0,Z:1})-Y*(Y**2-1))==0
    print('CHECK',d,'RANK_CANDIDATE',d+3)
print('VERIFY_OK')
