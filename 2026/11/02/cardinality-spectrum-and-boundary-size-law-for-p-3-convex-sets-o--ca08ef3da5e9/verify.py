#!/usr/bin/env python3
"""Recompute exact P3-convex set enumerators on open two-row strips.
Requires Python 3.10+ and sympy. Run: python3 verify.py
"""
from collections import Counter
from itertools import product
import sympy as sp

z, t = sp.symbols('z t')
STATES = [(a,b) for a in range(4) for b in range(4)]
INDEX = {s:i for i,s in enumerate(STATES)}

def admissible(a,b,c):
    return all((b>>row)&1 or ((a>>row)&1)+((b>>(1-row))&1)+((c>>row)&1) <= 1
               for row in range(2))

T = sp.zeros(16)
for i,(a,b) in enumerate(STATES):
    for c in range(4):
        if admissible(a,b,c):
            T[i,INDEX[b,c]] = z**b.bit_count()

initial = sp.Matrix([[int(a==0) for a,b in STATES]])
final = sp.Matrix([int(b==0) for a,b in STATES])
D = (1-(1+z+z**2)*t+(z**2+z**3)*t**2-(z+z**2)*t**3
     +2*z**3*t**4+z**3*t**5)
N = 1+z*t+(z+z**2-2*z**3)*t**2-3*z**3*t**3-z**3*t**4
Q = (1-z*t+z*t*t)*D
assert sp.cancel((initial*(sp.eye(16)-t*T).inv()*final)[0]-N/D)==0
x=sp.Symbol('lambda')
char=T.charpoly(x).as_expr()
assert sp.cancel(t**16*char.subs(x,1/t)-Q)==0

# The enumerated selections are completely independent of the transfer automaton.
def brute(n):
    adj=[[] for _ in range(2*n)]
    def connect(i,j):
        if j not in adj[i]:adj[i].append(j)
        if i not in adj[j]:adj[j].append(i)
    for i in range(n):
        connect(2*i,2*i+1)
        if i+1<n:
            for row in (0,1): connect(2*i+row,2*(i+1)+row)
    result=Counter()
    for mask in range(1<<(2*n)):
        if all(((mask>>v)&1) or sum((mask>>u)&1 for u in adj[v])<=1
               for v in range(2*n)):
            result[mask.bit_count()]+=1
    return sp.Poly.from_dict({(k,):v for k,v in result.items()},z).as_expr()

def iterations(n):
    out=[sp.Integer(1)]
    row=initial
    for _ in range(n):
        row=row*T
        out.append(sp.expand((row*final)[0]))
    return out

open_polys=iterations(9)
count=0
for n in range(1,9):
    actual=brute(n)
    assert actual==open_polys[n], ('open',n)
    count += (1<<(2*n))
assert [int(p.subs(z,1)) for p in open_polys[:9]]==[1,4,10,21,48,113,261,601,1390]
# All exact transfer formulas are verified symbolically; numerical constants
# are re-evaluated from the displayed algebraic root and implicit derivatives.
r=0.432450402724258
dt=float(sp.diff(D,t).subs({t:r,z:1}))
dz=float(sp.diff(D,z).subs({t:r,z:1}))
a=-dz/dt
b=-float((sp.diff(D,t,2)*a*a+2*sp.diff(D,t,z)*a+sp.diff(D,z,2)).subs({t:r,z:1}))/dt
mu=-a/r
var=-(a+b)/r+(a/r)**2
assert abs(mu-.514909291163714)<1e-12
assert abs(var-.359892854829278)<1e-12
print('VERIFY_OK open_cases=8 examined_subsets=',count,
      'weighted_matrix_identities=2 mu=',round(mu,12), 'variance=',round(var,12))
