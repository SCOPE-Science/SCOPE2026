#!/usr/bin/env python3
from fractions import Fraction as F

mu=F(751,10000)
lam=F(19,20)
p=F(1,100)
sigma=F(5,26)
rho=F(37,50)
theta=F(1,2)
gI=F(1,6)
muI=F(3521,100000)
gA=F(1,14)

sstar=(lam+mu)/(p+lam+mu)
qstar=p/(p+lam+mu)
assert sstar+qstar==1
assert p*sstar-(lam+mu)*qstar==0
assert p>0

def R0(beta):
    return beta*sstar*sigma/(sigma+mu)*(rho/(gI+muI+mu)+theta*(1-rho)/(gA+mu))

a=sigma+mu
b=gI+muI+mu
c=gA+mu
def det_minus_J(beta):
    return a*b*c-beta*sstar*sigma*(rho*c+theta*(1-rho)*b)

for beta in (F(9,100),F(3,10),F(13,20)):
    assert det_minus_J(beta)==a*b*c*(1-R0(beta))

r1=R0(F(9,100))
r2=R0(F(13,20))
bc=1/R0(F(1,1))
assert r1<1<r2
assert abs(float(r1)-0.22812111744668054)<1e-15
assert abs(float(r2)-1.6475414037815817)<1e-15
assert abs(float(bc)-0.3945272625671579)<1e-15
print("VERIFY_OK")
print("R0_beta_0.09",float(r1))
print("R0_beta_0.65",float(r2))
print("beta_critical",float(bc))
