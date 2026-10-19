#!/usr/bin/env python3
"""Exact checks and reproducible sampling for a tetrahedral edge-bisection ellipse.

Dependency: sympy (exact identities); Python standard library for sampling.
The mathematical infinite-orbit and sharpness assertions are proved separately.
"""
import math
import sympy as sp

x,y=sp.symbols('x y', real=True)
u=sp.Matrix([x,y]); S=sp.Matrix([[4,3],[3,4]])
U=sp.Matrix([[-sp.Rational(3,2),-1],[1,0]])
q=sp.expand((u.T*S*u)[0]); ss=x+y
assert sp.simplify(q-(sp.Rational(7,2)*ss**2+sp.Rational(1,2)*(x-y)**2))==0
assert U.T*S*U==S
D=sp.Matrix([23+4*x+4*y,3+x,3+y,20,20,10])
L01=sp.Matrix([
[sp.Rational(1,4),0,0,0,0,0],
[-sp.Rational(1,4),sp.Rational(1,2),0,sp.Rational(1,2),0,0],
[-sp.Rational(1,4),0,sp.Rational(1,2),0,sp.Rational(1,2),0],
[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
L12=sp.Matrix([
[sp.Rational(1,2),sp.Rational(1,2),0,-sp.Rational(1,4),0,0],
[0,1,0,0,0,0],[0,0,1,0,0,0],
[0,0,0,sp.Rational(1,4),0,0],
[0,0,0,-sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,2)],
[0,0,0,0,0,1]])
D1=sp.simplify(L01*D); D2=sp.simplify(L12*D1)
assert D1==sp.Matrix([x+y+sp.Rational(23,4),-x/2-y+sp.Rational(23,4),-x-y/2+sp.Rational(23,4),20,20,10])
assert D2==sp.Matrix([x/4+sp.Rational(3,4),-x/2-y+sp.Rational(23,4),-x-y/2+sp.Rational(23,4),5,10,10])
M=sp.Matrix([
[-sp.Rational(1,4),sp.Rational(1,2),0,sp.Rational(1,2),0,0],
[-sp.Rational(1,8),sp.Rational(1,8),sp.Rational(1,4),sp.Rational(1,16),sp.Rational(1,8),-sp.Rational(1,8)],
[0,sp.Rational(1,4),0,0,0,0],
[0,0,0,sp.Rational(3,16),-sp.Rational(1,8),sp.Rational(3,8)],
[0,0,0,sp.Rational(1,4),0,0],
[0,0,0,-sp.Rational(1,16),sp.Rational(1,8),sp.Rational(1,8)]])
xnew,ynew=U*u
assert sp.simplify(M*D-sp.Rational(1,4)*D.subs({x:xnew,y:ynew},simultaneous=True))==sp.zeros(6,1)
G=sp.Matrix([[23+4*x+4*y,3+sp.Rational(5,2)*x+2*y,3+2*x+sp.Rational(5,2)*y],
[3+sp.Rational(5,2)*x+2*y,3+x,-2+(x+y)/2],
[3+2*x+sp.Rational(5,2)*y,-2+(x+y)/2,3+y]])
assert sp.simplify(G[:2,:2].det()*4-(240+80*x-(3*x+4*y)**2))==0
assert sp.simplify(G.det()-(25-sp.Rational(35,4)*q))==0
qc=sp.Rational(63,32)
assert sp.simplify(q.subs({x:-sp.Rational(3,8),y:-sp.Rational(3,8)})-qc)==0
assert sp.simplify(D[0].subs({x:-sp.Rational(3,8),y:-sp.Rational(3,8)})-20)==0
assert sp.simplify((sp.Matrix([1,1]).T*S.inv()*sp.Matrix([1,1]))[0]-sp.Rational(2,7))==0

# Independent numerical test of Haar-frequency formula on formal irrational rotations.
theta=math.acos(-0.75)
for eq in (1.5,float(qc),1.975,2.0):
    expected=0.0 if eq<=float(qc) else math.acos(math.sqrt(float(qc)/eq))/math.pi
    count=0
    N=180000
    for k in range(N):
        ang=(0.4321+k*theta)%(2*math.pi)
        sx=math.sqrt(2*eq/7)*math.cos(ang)
        if sx<-.75: count+=1
    observed=count/N
    assert abs(observed-expected)<.0009,(eq,observed,expected)
    print(f'q={eq:.9f} forbidden_frequency={observed:.8f}, formula={expected:.8f}')
print('PASS: exact invariance, bisection stages, Gram minors, critical contact, numerical frequencies')
