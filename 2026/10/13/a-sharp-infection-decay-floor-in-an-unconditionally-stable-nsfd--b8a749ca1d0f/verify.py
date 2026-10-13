#!/usr/bin/env python3
import sympy as sp

R,c,phi,h,mu=sp.symbols("R c phi h mu", positive=True)
lam=(1+c*R*phi)/(1+c*phi)
assert sp.simplify(lam-(R+(1-R)/(1+c*phi)))==0
assert sp.simplify(1-lam-c*phi*(1-R)/(1+c*phi))==0

phis=(sp.exp(mu*h)-1)/mu
lams=sp.simplify(lam.subs(phi,phis))
dl0=sp.simplify(sp.limit((lams-1)/h,h,0))
assert sp.simplify(dl0+c*(1-R))==0

Rw=sp.Rational(1,2)
cw=sp.Rational(3)
hw=sp.log(2)
phiw=sp.simplify(sp.exp(hw)-1)
lamw=sp.simplify((1+cw*Rw*phiw)/(1+cw*phiw))
qw=sp.simplify(sp.exp(-cw*(1-Rw)*hw))
hstar=sp.simplify(-sp.log(Rw)/(cw*(1-Rw)))
assert phiw==1
assert lamw==sp.Rational(5,8)
assert qw==sp.sqrt(2)/4
assert sp.simplify(hw-hstar)>0
assert sp.simplify(Rw-qw)>0
assert sp.simplify(lamw-Rw)>0

rho_w=sp.simplify(-sp.log(lamw)/hw)
assert sp.simplify(rho_w-sp.log(sp.Rational(8,5))/sp.log(2))==0

lamh=sp.simplify((1+cw*Rw*(sp.exp(h)-1))/(1+cw*(sp.exp(h)-1)))
assert sp.limit(lamh,h,sp.oo)==Rw
rhoh=-sp.log(lamh)/h
assert sp.limit(rhoh,h,sp.oo)==0
assert sp.limit(h*rhoh,h,sp.oo)==-sp.log(Rw)

print("VERIFY_OK")
print("R0",Rw)
print("h_star",hstar)
print("h",hw)
print("phi",phiw)
print("NSFD_multiplier",lamw)
print("continuous_multiplier",qw)
print("NSFD_rate",sp.N(rho_w,20))
print("continuous_rate",sp.Rational(3,2))
