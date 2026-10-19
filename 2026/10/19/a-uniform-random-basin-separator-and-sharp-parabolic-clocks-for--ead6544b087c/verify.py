"""Deterministic consistency diagnostics for a two-map Arnold circle example.

The analytical almost-sure conclusions are proved in the accompanying theorem;
finite simulations are NOT certificates for almost-sure assertions.
"""
import math
import numpy as np
import sympy as sp

y, s, e, mu = sp.symbols('y s e mu', real=True)
h=(1-sp.cos(2*sp.pi*y))/10
c=sp.pi**2/5
checks=0
assert sp.simplify(sp.limit(h/y**2,y,0)-c)==0;checks+=1
assert sp.simplify(h.subs(y,1)-h.subs(y,0))==0;checks+=1
assert sp.simplify(sp.diff((y+h)+(y-h),y)-2)==0;checks+=1
assert sp.simplify(((1+mu)/2)*(y+h)+((1-mu)/2)*(y-h)-y-mu*h)==0;checks+=1
assert sp.simplify(((y+h)+(y-h))/2-y)==0;checks+=1
upper_plus=sp.simplify(1/(y-h)-1/y)
upper_minus=sp.simplify(1/(y+h)-1/y)
lower_plus=sp.simplify(1/(y+h)-1/y)
lower_minus=sp.simplify(1/(y-h)-1/y)
assert sp.simplify(sp.limit(upper_plus,y,0)-c)==0;checks+=1
assert sp.simplify(sp.limit(upper_minus,y,0)+c)==0;checks+=1
assert sp.simplify(sp.limit(lower_plus,y,0)+c)==0;checks+=1
assert sp.simplify(sp.limit(lower_minus,y,0)-c)==0;checks+=1
assert sp.simplify(sp.diff(y+h,y)+sp.diff(y-h,y)-2)==0;checks+=1

def update(x, eps):
    return x + eps*(1-np.cos(2*np.pi*x))/10

xs=np.linspace(0.001,0.999,10001)
for direction in (-1,1):
    ys=update(xs,direction)
    assert np.all(np.diff(ys)>0)
    assert np.all(ys>0) and np.all(ys<1)
    checks+=1

for p in (0.25,0.75):
    drift=2*p-1
    target=0 if drift<0 else 1
    theoretical=5/(math.pi**2*abs(drift))
    for seed in (2,11,73):
        rng=np.random.default_rng(seed)
        signs=np.where(rng.random(30000)<p,1,-1)
        x=0.53
        for eps in signs:
            x+=eps*((1-math.cos(2*math.pi*x))/10)
        scaled=30000*abs(x-target)
        # Loose numerical diagnostic, not the basis of the theorem.
        assert abs(scaled-theoretical)/theoretical<0.30,(p,seed,scaled,theoretical)
        checks+=1

print(f'PASS {checks} symbolic, map-order and seeded numerical diagnostics')
