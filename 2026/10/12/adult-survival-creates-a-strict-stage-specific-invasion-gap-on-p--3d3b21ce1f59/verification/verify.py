#!/usr/bin/env python3
"""Exact-symbolic replay for an adult-survival predator-stage Floquet theorem."""
import sympy as sp
from fractions import Fraction
from math import factorial

H, J, A = sp.symbols('H J A', real=True)
u, sig0 = sp.symbols('u sig0', real=True)

# Strict concavity on exp(u)>sig0>0 (the derivative identity is exact).
phi = sp.log(sp.exp(u)-sig0)
expected_second = -sig0*sp.exp(u)/(sp.exp(u)-sig0)**2
assert sp.simplify(sp.diff(phi,u,2)-expected_second) == 0

# Rational proof 3/2 < log(7) < 2: exp(3/2)<7<exp(2).
x = Fraction(3,2)
partial = sum((x**k)/factorial(k) for k in range(6))
# Tail k>=6 has successive ratios at most x/7.
next_term = x**6/factorial(6)
exp32_upper = partial + next_term/(1-x/Fraction(7))
assert exp32_upper < 7
assert sum((Fraction(2)**k)/factorial(k) for k in range(6)) > 7

L=sp.log(7)
r0=sp.Rational(49,4)
sigma=sp.Rational(1,4)
hlo=r0*L
hhi=2*hlo
rhoJ=1/hlo
rhoA=sp.Rational(3,4)/hlo
F=lambda z: r0*sp.exp(-z/r0)

# Original three-dimensional recurrence: prey, juvenile predator, adult predator.
N=sp.exp(-A)*H
T=sp.Matrix([
 sigma*N+sp.exp(-J)*F(N)*N,
 rhoJ*(1-sp.exp(-J))*F(N)*N,
 rhoA*(1-sp.exp(-A))*H
])
state=(H,J,A)

def exact(v):
 return sp.simplify(v)

for h, target in ((hlo,hhi),(hhi,hlo)):
 y=T.subs({H:h,J:0,A:0}).applyfunc(exact)
 assert y == sp.Matrix([target,0,0])

jac=T.jacobian(state)
lo=jac.subs({H:hlo,J:0,A:0}).applyfunc(exact)
hi=jac.subs({H:hhi,J:0,A:0}).applyfunc(exact)
for matrix in (lo,hi):
 assert all(exact(matrix[i,j])==0 for i in (1,2) for j in range(i))
assert [exact(lo[i,i]) for i in range(3)] == [
 2-sp.Rational(7,4)*L,sp.Rational(7,4),sp.Rational(3,4)]
assert [exact(hi[i,i]) for i in range(3)] == [
 (1-L)/2,sp.Rational(1,2),sp.Rational(3,2)]

# Correct time order, x0=hlo -> x1=hhi -> x2=hlo.
mon=(hi*lo).applyfunc(exact)
prey=(7*L-8)*(L-1)/8
assert exact(mon[0,0]-prey)==0
assert [exact(mon[i,i]) for i in (1,2)] == [sp.Rational(7,8),sp.Rational(9,8)]
# 3/2<L<2 implies 0<prey<3/4 as a monotone product of positive factors.
assert (7*sp.Rational(3,2)-8)>0
assert ((7*sp.Rational(2)-8)*(sp.Rational(2)-1)/8)==sp.Rational(3,4)

# The equilibrium factor is identical for both predator types and >1.
K = r0*sp.log(sp.Rational(49,3))
BJ = exact(rhoJ*(1-sigma)*K)
BA = exact(rhoA*K)
assert exact(BJ-BA)==0
assert 3**3<7**2
assert sp.N(BJ,25)>1
assert sp.N(prey,25)>0 and sp.N(prey,25)<sp.Rational(3,4)

# Exact inequality on this orbit: F(hlo)F(hhi)/(1-sigma)^2 = 7/9.
assert exact(F(hlo))==sp.Rational(7,4)
assert exact(F(hhi))==sp.Rational(1,4)
assert exact(F(hlo)*F(hhi)/(1-sigma)**2)==sp.Rational(7,9)
print('VERIFY_OK')
