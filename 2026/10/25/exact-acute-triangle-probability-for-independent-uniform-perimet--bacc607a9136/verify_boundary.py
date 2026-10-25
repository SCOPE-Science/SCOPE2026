"""Numerical cross-checks of equilateral perimeter acute-triangle integrals.

Run: python verify_boundary.py
The analytic proof is in RESULT.md; numerical integration and finite samples
are checks, not proof of the integral identities.
"""
import math
import random

L = math.log(4.0 / 3.0)
P2 = 4*L - 5.0/6.0
P3 = (27.0/2.0)*L - 3.5
P = (17.0/3.0)*L - 4.0/3.0


def simpson(fun, a, b, n=100000):
    if n % 2: raise ValueError('n even')
    h = (b-a)/n
    s = fun(a)+fun(b)
    for k in range(1,n):
        s += (4 if k % 2 else 2)*fun(a+k*h)
    return s*h/3


def f(t):
    if t == 0: return 0.0
    if t <= 0.5:
        return 1.5*t*t*(1.0+math.log((2-t)/(3*t)))
    return t*(1-0.5*t)


def qx(x):
    if x == 0 or x == 1: return 0.0
    if x <= 0.5:
        return x*(3*(1-x)*math.log((2-x)/(1-x))-1)
    return (1-x)*(3*x*math.log((1+x)/x)-1)


p2_numeric = simpson(f, 0, .5)+simpson(f,.5,1)
q_numeric = simpson(qx,0,.5)+simpson(qx,.5,1)
p3_numeric = 1-3*q_numeric
p_numeric = (2.0/3.0)*p2_numeric+(2.0/9.0)*p3_numeric
for label, calculated, closed in [('two',p2_numeric,P2),('three',p3_numeric,P3),('total',p_numeric,P)]:
    assert abs(calculated-closed)<2e-9, (label,calculated,closed)

rng = random.Random(31072026)
verts = ((0.,0.),(1.,0.),(.5,math.sqrt(3)/2))
N=300000
counts = [0,0,0]
acute = [0,0,0]
for _ in range(N):
    sides = [rng.randrange(3) for _ in range(3)]
    points = []
    for e in sides:
        t = rng.random()
        a,b=verts[e],verts[(e+1)%3]
        points.append((a[0]*(1-t)+b[0]*t,a[1]*(1-t)+b[1]*t))
    k=len(set(sides))-1
    counts[k]+=1
    if k == 0: continue
    dot=[]
    for i in range(3):
        p=points[i]; a=points[(i+1)%3]; b=points[(i+2)%3]
        dot.append((a[0]-p[0])*(b[0]-p[0])+(a[1]-p[1])*(b[1]-p[1]))
    if min(dot)>0: acute[k]+=1
assert abs(sum(acute)/N-P)<0.008
assert abs(acute[1]/counts[1]-P2)<0.012
assert abs(acute[2]/counts[2]-P3)<0.012
print('two-edge exact',repr(P2),'quadrature',repr(p2_numeric),'MC',repr(acute[1]/counts[1]))
print('three-edge exact',repr(P3),'quadrature',repr(p3_numeric),'MC',repr(acute[2]/counts[2]))
print('perimeter exact',repr(P),'quadrature',repr(p_numeric),'MC',repr(sum(acute)/N))
print('degenerate MC',repr(counts[0]/N),'theory',repr(1/9))
