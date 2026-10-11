#!/usr/bin/env python3
"""Exact scalar algebra and finite reproducibility checks for the quadratic rectangular constant of real L4."""
import math
import random
import sympy as sp
from mpmath import mp

z = sp.symbols('z', real=True)
P = 9*z**4 + 9*z**3 - 12*z**2 - 3*z + 1
R = 9*z**4 - 9*z**3 - 6*z**2 + 9*z + 1
K = 1 + 9*z**2 - 9*z**4
L = 1 + 3*z**2
s = sp.sqrt(z*(1-z**2))
lam = 3*s/(1-3*z**2)
D = 1 + lam**4 + 6*z*lam**2 - 4*s*lam**3
G = (1+lam**2)**2 / D
closed = R**2/(L**2*K)
assert sp.simplify(G - closed) == 0
assert sp.simplify(sp.diff(closed,z) + 18*(3*z**4-6*z**2-1)*R*P/(L**3*(9*z**4-9*z**2-1)**2)) == 0
assert sp.simplify(P.subs(z, sp.sqrt(3)/3) + 2) == 0
assert sp.simplify(sp.diff(P,z).subs(z,sp.sqrt(3)/3) - (6-4*sp.sqrt(3))) == 0
assert sp.diff(P,z).subs(z,0) == -3

mp.dps = 75
u = mp.findroot(lambda x: 9*x**4+9*x**3-12*x**2-3*x+1, (mp.mpf('0.19'),mp.mpf('0.22')))
assert mp.mpf('0.2') < u < mp.mpf('0.21')
su=mp.sqrt(u*(1-u*u))
lam0=3*su/(1-3*u*u)
mu2=(mp.mpf(str(1)) + lam0**2)**mp.mpf('0.5') / (1+lam0**4+6*u*lam0**2-4*su*lam0**3)**mp.mpf('0.25')
a=mp.sqrt((1-u*u)/u)
tplus=(-a+mp.sqrt(a*a+4*u))/2
tminus=(-a-mp.sqrt(a*a+4*u))/2
wp=-tminus/(tplus-tminus)
wm=tplus/(tplus-tminus)
T=lambda j:wp*tplus**j+wm*tminus**j
for j,target in ((0,1),(1,0),(2,u),(3,-su),(4,1)):
    assert abs(T(j)-target) < mp.mpf('1e-68')
assert abs((1+lam0**2)**2 / (1+lam0**4+6*u*lam0**2-4*su*lam0**3) - (mu2**4)) < mp.mpf('1e-65')
assert abs((1+lam0**2)**2 / (1+lam0**4+6*u*lam0**2-4*su*lam0**3) - mp.mpf(str(sp.N(closed.subs(z,str(u)),65)))) < mp.mpf('1e-60')

rng = random.Random(164829)
checks=0
for dimension in (2,3,4,6,9):
    for i in range(420):
        x=[rng.uniform(-1,1) for _ in range(dimension)]
        xnorm=sum(a**4 for a in x)**0.25
        x=[a/xnorm for a in x]
        y=[rng.uniform(-1,1) for _ in range(dimension)]
        ortho=sum(a**3*b for a,b in zip(x,y))
        y=[b-ortho*a for a,b in zip(x,y)]
        ynorm=sum(b**4 for b in y)**0.25
        if ynorm<1e-10:continue
        y=[b/ynorm for b in y]
        assert abs(sum(a**3*b for a,b in zip(x,y))) < 1e-12
        A=sum((a*b)**2 for a,b in zip(x,y))
        B=sum(a*b**3 for a,b in zip(x,y))
        assert B*B <= A*(1-A*A)+1e-10
        for scale in (0.0,0.2,0.5,1.0,float(lam0),2.0,4.0,12.0):
            ratio=((1+scale*scale)**0.5)/(sum((a+scale*b)**4 for a,b in zip(x,y))**0.25)
            assert ratio <= float(mu2) + 1e-11,(dimension,i,ratio)
            checks+=1

print('VERIFY_OK symbolic_identities=3 root_bracket=1 two_atom_moments=5 random_pair_ratios=%d' % checks)
print('u0='+mp.nstr(u,55))
print('lambda0='+mp.nstr(lam0,55))
print('mu2='+mp.nstr(mu2,55))
print('two_ratio='+mp.nstr(tplus,18)+','+mp.nstr(tminus,18))
