#!/usr/bin/env python3
"""Independent geometric-smoothness census via Groebner bases over GF(3).
Requires Python 3 and SymPy. No extension-field cutoff is used.
"""
import itertools
from collections import Counter
import sympy as sp
x,y,z=sp.symbols('x y z')
MON=[(a,b,3-a-b) for a in range(4) for b in range(4-a)]
points=set()
for p in itertools.product(range(3),repeat=3):
    if p==(0,0,0):continue
    v=next(c for c in p if c)
    points.add(tuple((a*pow(v,-1,3))%3 for a in p))
points=sorted(points)
lines=[[p for p in points if sum(a*b for a,b in zip(p,coef))%3==0] for coef in points]
def poly(c):return sum(v*x**a*y**b*z**d for v,(a,b,d) in zip(c,MON))
def smooth(F):
    # Affine patch z=1, then the line at infinity z=0 with y=1,
    # then the exceptional projective point (1:0:0).
    f=sp.expand(F.subs(z,1))
    g=sp.groebner([f,sp.diff(f,x),sp.diff(f,y)],x,y,modulus=3)
    if g!=sp.groebner([1],x,y,modulus=3):return False
    h=sp.expand(F.subs({y:1,z:0}))
    g=sp.groebner([h,sp.diff(F,x).subs({y:1,z:0}),
                   sp.diff(F,z).subs({y:1,z:0})],x,modulus=3)
    if g!=sp.groebner([1],x,modulus=3):return False
    p={x:1,y:0,z:0}
    if all(int(t.subs(p))%3==0 for t in [F,sp.diff(F,y),sp.diff(F,z)]):return False
    return True
nblocking=0; nsmooth=0; count_points=Counter()
for code in range(1,3**10):
    n=code;c=[]
    for i in range(10):c.append(n%3);n//=3
    zero=lambda p: sum(v*pow(a,i,3)*pow(b,j,3)*pow(d,k,3) for v,(i,j,k) in zip(c,MON) for a,b,d in [p])%3==0
    if not all(any(zero(p) for p in line) for line in lines):continue
    nblocking+=1
    F=poly(c)
    if smooth(F):
        nsmooth+=1
        count_points[sum(zero(p) for p in points)]+=1
print('nonzero_cubic_forms=',3**10-1)
print('blocking_cubic_forms=',nblocking)
print('smooth_blocking_cubic_forms=',nsmooth)
print('smooth_blocking_point_counts=',dict(sorted(count_points.items())))
assert nblocking==9880 and nsmooth==1872 and count_points==Counter({6:1872})
