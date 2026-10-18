"""Finite symbolic/diagnostic checks for a weighted-gradient coupled sine map.

All global convergence assertions in the accompanying proof are analytical.
The numerical checks here are deliberately finite and non-exhaustive.
"""
import math
import random
import sympy as s

x,y,a,b,h=s.symbols('x y a b h', real=True, positive=True)
p=s.pi
V=-a*s.cos(2*p*x)/(4*p*p*h)-a*s.cos(2*p*y)/(4*p*p)+b*s.cos(2*p*(y-x))/(4*p*p)
T=s.Matrix([x+a*s.sin(2*p*x)/(2*p)+h*b*s.sin(2*p*(y-x))/(2*p),
             y+a*s.sin(2*p*y)/(2*p)-b*s.sin(2*p*(y-x))/(2*p)])
assert s.simplify(s.Matrix([x,y])+s.diag(h,1)*s.Matrix([s.diff(V,x),s.diff(V,y)])-T)==s.zeros(2,1)
H=s.Matrix([[h*s.diff(V,x,x), s.sqrt(h)*s.diff(V,x,y)],
            [s.sqrt(h)*s.diff(V,y,x),s.diff(V,y,y)]])
v=s.Matrix([s.sqrt(h),-1]); Q=a*s.diag(s.cos(2*p*x),s.cos(2*p*y))-b*s.cos(2*p*(y-x))*(v*v.T)
assert s.simplify(H-Q)==s.zeros(2,2)
J=T.jacobian([x,y]); J0=s.simplify(J.subs({x:s.Rational(1,2),y:s.Rational(1,2)}))
assert s.simplify((s.Symbol('z')*s.eye(2)-J0).det()-(s.Symbol('z')-(1-a))*(s.Symbol('z')-(1-a-(1+h)*b)))==0

rng=random.Random(20261014)
def map_step(X,Y,A,B,H):
    return (X+A*math.sin(2*math.pi*X)/(2*math.pi)+H*B*math.sin(2*math.pi*(Y-X))/(2*math.pi),
            Y+A*math.sin(2*math.pi*Y)/(2*math.pi)-B*math.sin(2*math.pi*(Y-X))/(2*math.pi))
def energy(X,Y,A,B,H):
    return (-A*math.cos(2*math.pi*X)/H-A*math.cos(2*math.pi*Y)+B*math.cos(2*math.pi*(Y-X)))/(4*math.pi**2)
checks=0
for _ in range(180):
    H=rng.uniform(.02,1.0)
    A=rng.uniform(.02,1.8)
    B=(2-A)/(1+H)*rng.uniform(.02,.999)
    L=A+(1+H)*B
    for _ in range(35):
        X,Y=rng.uniform(-10,10),rng.uniform(-10,10)
        XX,YY=map_step(X,Y,A,B,H)
        dv=energy(XX,YY,A,B,H)-energy(X,Y,A,B,H)
        sq=(XX-X)**2/H+(YY-Y)**2
        assert dv>= (1-L/2)*sq-3e-14,(dv,sq,L)
        checks+=1
for _ in range(1000):
    H=rng.uniform(.05,1)
    A=rng.uniform(.05,1.5)
    B=(2-A)/(1+H)
    X,Y=rng.random(),rng.random()
    XX,YY=map_step(X,Y,A,B,H)
    assert energy(XX,YY,A,B,H)>energy(X,Y,A,B,H)-3e-14
    checks+=1
for A,B,H in [(.8,.9,.5),(.6,.95,1.),(1.,.9,.1)]:
    if A+(1+H)*B<=2:continue
    w=math.sqrt(H)
    for e in [1e-3,2e-3,4e-3]:
        X=.5+e*w;Y=.5-e
        XX,YY=map_step(X,Y,A,B,H)
        assert energy(XX,YY,A,B,H)<energy(X,Y,A,B,H),(A,B,H,e)
        checks+=1

# Reconstruct every nontrivial stationary point from the angular formula.
for _ in range(180):
    H=rng.uniform(.05,1)
    A=rng.uniform(.1,1.5)
    B=A/(1+H)*rng.uniform(1.01,1.4)
    C=((A/B)**2-1-H**2)/(2*H)
    if abs(C)>=1:continue
    for t in [math.acos(C),-math.acos(C)]:
        sx=-H*(B/A)*math.sin(t)
        cx=(B/A)*(1+H*C)
        u=math.atan2(sx,cx)
        X=u/(2*math.pi);Y=(u+t)/(2*math.pi)
        XX,YY=map_step(X,Y,A,B,H)
        assert max(abs(XX-X),abs(YY-Y))<1e-12
        checks+=1
print('symbolic identities: 3; finite diagnostics:',checks,'PASS')
