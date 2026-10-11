#!/usr/bin/env python3
import sympy as s
import math

t, a = s.symbols("t a", positive=True, real=True)
pi = s.pi

x = t/(pi*s.sin(t))
y = s.cos(t)/4
dx = s.diff(x,t)
dydx = s.simplify(s.diff(y,t)/dx)
g = 2*t*s.cos(2*t)+4*t-3*s.sin(2*t)
h = 1-s.cos(2*t)-t*s.sin(2*t)

target_dydx = pi*s.sin(t)**3/(4*(t*s.cos(t)-s.sin(t)))
assert s.simplify(dydx-target_dydx) == 0

target_der = pi*s.sin(t)**2*g/(8*(t*s.cos(t)-s.sin(t))**2)
assert s.simplify(s.diff(dydx,t)-target_der) == 0
assert s.simplify(s.diff(g,t)-4*h) == 0
assert s.simplify(s.diff(h,t)-(s.sin(2*t)-2*t*s.cos(2*t))) == 0
assert s.simplify(s.diff(h,t,2)-4*t*s.sin(2*t)) == 0

u,n = s.symbols("u n", positive=True, real=True)
xodd = 1/(2*n*s.sin(u))
yodd = s.cos(2*u)/(4*s.cos(u))
xeven = 1/(2*n*s.sin(u))
yeven = s.cos(u)/4
assert s.simplify(xodd-xeven) == 0
assert s.trigsimp(yeven-yodd-s.sin(u)**2/(4*s.cos(u))) == 0

sqrt2=s.sqrt(2)
FQ=(1-a)/(2*sqrt2)+a*sqrt2/8
FB=(1-a)/pi+a/4
astar=2*(sqrt2*pi-4)/(pi*(sqrt2+2)-8)
assert s.simplify((FQ-FB).subs(a,astar)) == 0
assert 0 < float(s.N(astar,30)) < 1

# Regression scan; not part of the proof.
def coords(k):
    th=math.pi/k
    P=2*k*math.sin(th)
    A=k*math.sin(th)*math.cos(th)
    if k%2==0:
        D=2.0
    else:
        D=2*math.cos(th/2)
    return D/P, A/(P*D)

aa=float(s.N(astar,30))
for alpha in [0.0, .1, aa, .5, .9, 1.0]:
    fq=(1-alpha)/(2*math.sqrt(2))+alpha*math.sqrt(2)/8
    fb=(1-alpha)/math.pi+alpha/4
    env=max(fq,fb)
    best=(-1,None)
    for k in range(3,10001):
        xx,yy=coords(k)
        val=(1-alpha)*xx+alpha*yy
        assert val <= env + 1e-12
        if val>best[0]: best=(val,k)
    if alpha <= aa + 1e-14:
        assert best[1] == 4
    else:
        # The finite scan should be improving near its upper endpoint.
        assert best[1] >= 9990

print("VERIFY_OK")
print("alpha_star =", s.N(astar,18))
print("square branch =", s.simplify(FQ))
print("disk branch =", s.simplify(FB))
