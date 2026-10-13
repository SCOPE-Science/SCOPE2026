from fractions import Fraction as F
import sympy as sp

t=sp.symbols('t')
p=[t/2,(1-t)/2,(1-t)/2,t/2]
xs=[0,1,2,3]
mu=sum(p[i]*xs[i] for i in range(4))
EL=EU=EL2=EU2=ELU=0
for i in range(4):
    for j in range(4):
        w=p[i]*p[j]
        lo=min(xs[i],xs[j]); hi=max(xs[i],xs[j])
        EL += w*lo; EU += w*hi
        EL2 += w*lo*lo; EU2 += w*hi*hi; ELU += w*lo*hi
VL=sp.factor(EL2-EL**2)
VU=sp.factor(EU2-EU**2)
C=sp.factor(ELU-EL*EU)
rho=sp.factor(C/sp.sqrt(VL*VU))
# VL=VU and both are positive on [0,1], so replace sqrt(VL*VU) by VL.
assert sp.factor(VL-VU)==0
rho=sp.factor(C/VL)
expected_rho=sp.factor((1+4*t-2*t**2)**2/(3+24*t-12*t**2+16*t**3-4*t**4))
assert sp.factor(rho-expected_rho)==0
D=3+24*t-12*t**2+16*t**3-4*t**4
assert sp.factor(16*VL-D)==0
# delta=(EU-EL)/2
assert sp.factor((EU-EL)/2-(1+4*t-2*t**2)/4)==0
expected_def=4*(2*t-1)**2*(1+12*t-4*t**2)/(11*D)
assert sp.factor(sp.Rational(5,11)-rho-expected_def)==0
# exact rational stress grid
mx=F(0); arg=None
for k in range(101):
    q=F(k,100)
    num=(1+4*q-2*q*q)**2
    den=3+24*q-12*q*q+16*q**3-4*q**4
    r=num/den
    assert r <= F(5,11)
    if r>mx: mx,arg=r,q
assert mx==F(5,11) and arg==F(1,2)
print('VERIFY_OK max=5/11 theta=1/2 grid=101')
