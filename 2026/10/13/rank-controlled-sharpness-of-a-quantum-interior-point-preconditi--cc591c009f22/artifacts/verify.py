#!/usr/bin/env python3
"""Reproduce exact algebra for the integral two-constraint witness."""
from fractions import Fraction as F

A=((1,0,0),(0,1,-1))
b=(1,0)
c=(0,1,1)
for gamma in (F(1,2),F(3,4)):
    assert F(0)<gamma<F(1)
    for mu in (F(1,10),F(1,100),F(1,1000),F(1,10000)):
        x=(F(1),mu,mu)
        y=(-mu,F(0))
        s=(mu,F(1),F(1))
        assert tuple(sum(A[i][j]*x[j] for j in range(3)) for i in range(2))==b
        assert tuple(sum(A[i][j]*y[i] for i in range(2))+s[j] for j in range(3))==c
        assert all(x[i]*s[i]==mu for i in range(3))
        assert x[0]>0 and all(v>0 for v in s)
        # Source Definition 2 threshold, evaluated without radicals.
        threshold2=(F(3)-2*gamma)*mu
        assert x[0]**2>=threshold2 and x[1]**2<threshold2 and x[2]**2<threshold2
        omega=max(x+s)
        assert omega==1
        # A A^T = diag(1,2), so sigma_min(A)^2 = 1.
        h=gamma / omega**2
        D1=mu
        D2inv=mu
        F1=F(1)+D1
        B2=F(1)/F1        # B B^T only at its first diagonal entry.
        H11=B2
        H22=2*D2inv
        Zhat=B2/h + D1
        G11=(B2/h)/Zhat
        Y11=G11+(1-G11)*H11/h
        Y22=H22/h
        assert Y11==(1+mu)/(1+gamma*mu*(1+mu))
        assert Y22==2*mu/gamma
        assert Y11>Y22>0
        kappa=Y11/Y22
        assert kappa==gamma*(1+mu)/(2*mu*(1+gamma*mu*(1+mu)))
        normal1=1/mu
        normal2=2*mu
        assert normal1/normal2 == 1/(2*mu**2)
        if mu==F(1,10000):
            assert abs(float(mu*kappa-gamma/2))<0.00004
# Exactly certified limiting rank-complement coefficient is gamma/2 because
# the nonbasic projected Gram entry is 2 and the prescribed scalar tends to gamma.
print('VERIFY_OK')
