#!/usr/bin/env python3
import math

def norm(v):
    x,y=v
    return math.hypot(x,y) if x*y >= 0 else abs(x)+abs(y)

def h(t):
    return t**4 + 2*t**3 - 1

lo=math.sqrt(2)-1
hi=1.0
assert h(lo) < 0 < h(hi)
for _ in range(120):
    mid=(lo+hi)/2
    if h(mid) < 0:
        lo=mid
    else:
        hi=mid
tau=(lo+hi)/2
J=2/math.sqrt(1+tau*tau)
a=(1-tau*tau)/(1+tau*tau)
b=2*tau/(1+tau*tau)
x=(1.0,0.0)
y=(a,b)
F=norm((x[0]+y[0],x[1]+y[1]))
G=norm((x[0]-y[0],x[1]-y[1]))
s=J*J
poly=s**4-12*s**3+64*s**2-128*s+64
assert abs(h(tau)) < 2e-15
assert abs(a*a+b*b-1) < 2e-15
assert 0 <= a <= b
assert abs(F-G) < 2e-14
assert abs(F-J) < 2e-14
assert abs(poly) < 2e-12
assert J > math.sqrt(2)
# Diagnostic sampling of the exact branch formulas proved in RESULT.md.
best_axis=0.0
for k in range(200001):
    aa=(1/math.sqrt(2))*k/200000
    bb=math.sqrt(max(0.0,1-aa*aa))
    f=math.sqrt(2*(1+aa))
    g=1-aa+bb
    best_axis=max(best_axis,min(f,g))
assert best_axis <= J + 1e-9
# Euclidean-arc analytic upper bound sqrt(1+q^-2), q in [1,sqrt(2)].
best_arc=0.0
for k in range(1,200000):
    th=(math.pi/2)*k/200000
    q=math.cos(th)+math.sin(th)
    best_arc=max(best_arc,math.sqrt(1+1/(q*q)))
assert best_arc <= math.sqrt(2)+1e-12
# Taxicab-edge exact formulas.
r=1/math.sqrt(2)
best_edge=0.0
for k in range(1,200000):
    u=k/200000
    v=1-u
    xp=(u+r,-v+r)
    xm=(u-r,-v-r)
    best_edge=max(best_edge,min(norm(xp),norm(xm)))
assert best_edge <= math.sqrt(2)+1e-12
print('VERIFY_OK')
print(f'tau={tau:.16f}')
print(f'a0={a:.16f}')
print(f'b0={b:.16f}')
print(f'J_perp={J:.16f}')
print(f'J_squared={s:.16f}')
print(f'axis_sample_max={best_axis:.16f}')
