"""Reproduce the exact period-two selection threshold and an admissible witness.
Requires Python 3 with SymPy; decimal trajectories only supplement exact tests.
"""
from fractions import Fraction
from math import sqrt
import sympy as sp

A = sp.Rational(16, 5)
r = sp.Rational(37, 10)
e_low, e_high = sp.Rational(1, 4), sp.Rational(1, 2)
s0, s1 = sp.Rational(58, 25), sp.Rational(8, 25)
t0, t1 = sp.Rational(3, 2), sp.Rational(3, 1)
n, x = sp.symbols('n x', real=True)

S = (1 - n)*s0 + n*s1
T = (1 - n)*t0 + n*t1
fC = 2*x + S*(1-x)
fD = T*x + (1-x)
F = sp.cancel(x*fC/(x*fC+(1-x)*fD))
G = sp.expand(r*n*(1-(1-e_high/r)*n)-n*(e_low*x+e_high*(1-x)))
assert sp.simplify(G-n*(A+(e_high-e_low)*x-A*n))==0

low = (21-sp.sqrt(21))/32
high = (21+sp.sqrt(21))/32
g0 = sp.simplify(G.subs(x,0))
assert sp.simplify(g0.subs(n,low)-high)==0
assert sp.simplify(g0.subs(n,high)-low)==0
assert 0 < float(low) < float(high) < 1
mu_low = sp.simplify(S.subs(n,low))
mu_high = sp.simplify(S.subs(n,high))
P = sp.simplify(mu_low*mu_high)
mean = sp.simplify((mu_low+mu_high)/2)
assert P == sp.Rational(37321,40000)
assert mean == sp.Rational(403,400) > 1
assert 0 < mu_low and 0 < mu_high

J = sp.Matrix([F,G]).jacobian(sp.Matrix([x,n]))
J_low = J.subs({x:0,n:low})
J_high = J.subs({x:0,n:high})
M = sp.simplify(J_high*J_low)
assert sp.simplify(M[0,0]-P)==0
assert sp.simplify(M[1,1]-sp.Rational(4,25))==0
assert sp.simplify(M[0,1])==0
assert 0 < P < 1
# The unit square is invariant: G >= 0 on its vertical boundaries,
# and its global maximum on that square is strictly less than one.
max_G = (A+e_high-e_low)**2/(4*A)
assert max_G == sp.Rational(4761,5120) < 1
assert sp.simplify(G.subs(n,1)-(e_high-e_low)*x)==0

# General symbolic two-cycle formula, not inferred from enumeration.
R, C, d = sp.symbols('R C d', real=True, positive=True)
mean_n=(R+1)/(2*R)
Delta=sp.sqrt((R-3)*(R+1))/(2*R)
nlo=mean_n-Delta
nhi=mean_n+Delta
s=lambda z: C-d*z
prod=sp.expand(s(nlo)*s(nhi))
assert sp.simplify(prod - ((C-d*mean_n)**2 - d*d*(R-3)*(R+1)/(4*R*R)))==0

# Supplementary forward trajectories of the full two-dimensional map.
def step(xx, nn):
    sn=float(s0)+(float(s1)-float(s0))*nn
    tn=float(t0)+(float(t1)-float(t0))*nn
    fc=2*xx+sn*(1-xx)
    fd=tn*xx+(1-xx)
    return xx*fc/(xx*fc+(1-xx)*fd), nn*(float(A)+0.25*xx-float(A)*nn)

for ix in range(1,7):
    for j in range(-3,4):
        xx=ix*0.002
        nn=float(low)+j*0.002
        for k in range(900):
            xx,nn=step(xx,nn)
            assert 0<=xx<=1 and 0<=nn<=1
        assert xx<1e-8
        assert min(abs(nn-float(low)),abs(nn-float(high))) < 1e-8

print('Exact resource 2-cycle:', low, high)
print('Transverse multiplier:', P, 'resource multiplier:', sp.Rational(4,25))
print('Mean-game multiplier:', mean, '> 1')
print('Unit-square maximum resource update:',max_G)
print('Validated 42 near-cycle full-map trajectories plus symbolic identities.')
