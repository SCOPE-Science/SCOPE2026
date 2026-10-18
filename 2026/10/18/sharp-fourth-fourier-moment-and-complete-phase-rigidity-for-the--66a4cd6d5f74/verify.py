#!/usr/bin/env python3
"""Exact convolution and numerical reproduction of the centered A2 fourth moment."""
from collections import defaultdict
from itertools import combinations
import math
import random
import sympy as sp
S=[(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]
a,b=sp.symbols('a b',real=True)
w=[a]+[b]*6

def fourth(c):
    z=defaultdict(lambda:0)
    for i,s in enumerate(S):
        for j,t in enumerate(S):
            k=(s[0]+t[0],s[1]+t[1]);z[k]+=c[i]*c[j]
    return sum(sp.expand(x*sp.conjugate(x)) for x in z.values())
F=sp.expand(fourth(w))
assert sp.factor(F-(a**4+36*a*a*b*b+48*a*b**3+90*b**4))==0
r=sp.symbols('r',positive=True)
K=(r**4+36*r*r+48*r+90)/(r*r+6)**2
assert sp.simplify(sp.diff(K,r)+24*(2*r**3+6*r*r-3*r-12)/(r*r+6)**3)==0
root=float(sp.nroots(2*r**3+6*r*r-3*r-12)[2])
assert 1.35<root<1.37
S6=S[1:]
T=[(i,j,k) for i,j,k in combinations(range(6),3) if (S6[i][0]+S6[j][0]==S6[k][0] and S6[i][1]+S6[j][1]==S6[k][1]) or (S6[i][0]+S6[k][0]==S6[j][0] and S6[i][1]+S6[k][1]==S6[j][1]) or (S6[j][0]+S6[k][0]==S6[i][0] and S6[j][1]+S6[k][1]==S6[i][1])]
assert len(T)==6
for trial in range(100):
    c=[complex(random.uniform(-2,2),random.uniform(-2,2)) for _ in range(7)]
    conv=defaultdict(complex)
    for i,s in enumerate(S):
        for j,t in enumerate(S):
            conv[(s[0]+t[0],s[1]+t[1])]+=c[i]*c[j]
    fv=sum(abs(z)**2 for z in conv.values())
    mass=sum(abs(z)**2 for z in c)
    assert fv<= (float(K.subs(r,root))+1.e-9)*mass**2
for n in (5,6,7,9):
    c=[root]+[1.]*6
    conv=defaultdict(complex)
    for i,s in enumerate(S):
        for j,t in enumerate(S):
            conv[((s[0]+t[0])%n,(s[1]+t[1])%n)]+=c[i]*c[j]
    sampled=sum(abs(z)**2 for z in conv.values())
    assert abs(sampled-float(F.subs({a:root,b:1})))<1.e-8
print('exact moment polynomial:',F)
print('derivative factorization: verified')
print('root:',format(root,'.15f'))
print('sharp fourth-power constant:',format(float(K.subs(r,root)),'.15f'))
print('six root-addition triples:',T)
print('100 numerical complex-coefficient upper-bound checks: passed')
print('N=5,6,7,9 finite-grid equality convolution checks: passed')
