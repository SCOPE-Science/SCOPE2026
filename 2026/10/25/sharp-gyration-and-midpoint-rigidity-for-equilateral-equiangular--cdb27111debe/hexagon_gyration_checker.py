"""Self-contained reproduction of exact midpoint-gyration identity.
Requires Python 3 standard library only.
"""
import random,math

def d2(a,b): return sum((x-y)**2 for x,y in zip(a,b))
def midpoint(a,b):return tuple((x+y)/2 for x,y in zip(a,b))
def gyr(P):
    c=tuple(sum(p[i] for p in P)/6 for i in range(3))
    return sum(d2(p,c) for p in P)/6

def calc(P):
    C1=sum(d2(P[i],P[(i+1)%6]) for i in range(6))
    C2=sum(d2(P[i],P[(i+2)%6]) for i in range(6))
    M=[midpoint(P[i],P[i+3]) for i in range(3)]
    H=sum(d2(M[i],M[j]) for i in range(3) for j in range(i+1,3))
    assert abs(gyr(P)-((C1+C2)/24-H/18))<1e-11,(gyr(P),C1,C2,H)

rng=random.Random(20261018)
for _ in range(5000):
    P=[tuple(rng.gauss(0,1) for i in range(3)) for j in range(6)]
    calc(P)
print('UNIVERSAL_SIX_POINT_CENTROID_MIDPOINT_IDENTITY_OK 5000')

def chair(theta):
    D2=4*math.sin(theta/2)**2
    r=(1+D2)/4; t=(D2-1)/4
    import numpy as np
    G=np.array([[r,t,-t],[t,r,t],[-t,t,r]])
    ev=np.linalg.eigvalsh(G)
    assert ev.min()>0,ev
    P3=np.linalg.cholesky(G)
    return [tuple(x) for x in [*P3,*(-P3)]]

for j in range(1,100):
    theta=(2*math.pi/3)*j/100
    P=chair(theta)
    for i in range(6):
        assert abs(d2(P[i],P[(i+1)%6])-1)<1e-12
        assert abs(d2(P[i],P[(i+2)%6])-4*math.sin(theta/2)**2)<1e-12
    assert abs(gyr(P)-(math.sin(theta/2)**2+1/4))<1e-12
    calc(P)
print('CHAIR_EQUILATERAL_EQUIANGULAR_SHARPNESS_ALL_SAMPLED_ANGLES_OK 99')

import sympy as sp
z=sp.symbols('z',real=True)
r=(1+z)/4;t=(z-1)/4
G=sp.Matrix([[r,t,-t],[t,r,t],[-t,t,r]])
assert sp.factor(G.det()) == sp.factor(z*z*(3-z)/16)
print('GRAM_POSITIVE_EIGENVALUE_CERTIFICATE_OK',sp.factor(G.charpoly().as_expr()))
print('ALL_HEXAGON_GYRATION_CHECKS_OK')
