#!/usr/bin/env python3
import math
A0=10.0; A1=0.3; mu=0.1; d1=0.02; alpha=0.4; w1=0.05; d2=0.03; w2=0.2
mu1=mu+d1+alpha+w1; mu2=mu+d2+w2; theta0=0.5; b=0.7
Iimp=alpha*A1/(mu1*mu2); zeta=alpha*(A0+A1)/(mu1*mu2)
def theta(I): return theta0/(1.0+b*I)
def H(I): return alpha*(mu1*mu2*I-alpha*A1)/(mu2*I*(alpha*(A0+A1)-mu1*mu2*I))
def solve(z):
    mu0=mu+z; lo=Iimp*(1+1e-12); hi=zeta*(1-1e-12)
    for _ in range(220):
        mid=(lo+hi)/2
        if theta(mid)-mu0*H(mid)>0: lo=mid
        else: hi=mid
    I=(lo+hi)/2; E=mu2*I/alpha; S=A0/(mu0+theta(I)*E)
    ell=theta(I)*S/mu1; Rcl=theta0*A0/(mu0*mu1)
    rS=A0-theta(I)*S*E-mu0*S
    rE=A1+theta(I)*S*E-mu1*E
    rI=alpha*E-mu2*I
    assert max(abs(rS),abs(rE),abs(rI))<2e-11
    assert I>Iimp and E>A1/mu1
    assert abs(ell-(1-A1/(mu1*E)))<2e-12
    assert 0<ell<Rcl
    if Rcl<1:
        assert I<Iimp/(1-Rcl)
        assert E<(A1/mu1)/(1-Rcl)
    return I,E,S,ell,Rcl
vals=[solve(z) for z in (0.0,1.0,10.0,100.0,1000.0)]
assert all(vals[i+1][0]<vals[i][0] for i in range(len(vals)-1))
theta_imp=theta(Iimp)
coefI=alpha*A0*A1*theta_imp/(mu1*mu1*mu2)
coefE=A0*A1*theta_imp/(mu1*mu1)
I,E,_,ell,_=solve(10000.0); mu0=10000.0+mu
assert abs(mu0*(I-Iimp)-coefI)<0.01
assert abs(mu0*(E-A1/mu1)-coefE)<0.01
assert abs(mu0*ell-A0*theta_imp/mu1)<0.01
print('VERIFY_OK')
print('I_imp',repr(Iimp))
for z,row in zip((0.0,1.0,10.0,100.0,1000.0),vals): print('z',z,'I',repr(row[0]),'ell',repr(row[3]),'Rcl',repr(row[4]))
print('coef_I',repr(coefI),'coef_E',repr(coefE))
