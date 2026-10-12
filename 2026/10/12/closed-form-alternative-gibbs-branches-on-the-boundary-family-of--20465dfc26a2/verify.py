#!/usr/bin/env python3
from fractions import Fraction
import math

# Exact rational replay of the source I_3 equations on reciprocal branches.
exact_cases=0
for k in range(4,22,2):
    m=k//2+1
    for z in (Fraction(3,2),Fraction(2,1),Fraction(5,2)):
        t=1/z
        lam=(z*z+1)**k/(z**(k//2)*(z+1)**k)
        den=z+t
        rhs1=lam*((1+z)/den)**m*((1+t)/den)**(k-m)
        rhs2=lam*((1+t)/den)**m*((1+z)/den)**(k-m)
        assert rhs1==z,(k,z,rhs1)
        assert rhs2==t,(k,z,rhs2)
        u=z+t
        assert lam**2 == (u**(2*k))/((u+2)**k)
        exact_cases+=1

# Numerical replay of the explicit radical inverse.
radical_cases=0
max_res=0.0
for k in (4,6,8,12,20):
    for lam in (1.01,1.2,2.0,10.0):
        s=lam**(2.0/k)
        u=(s+math.sqrt(s*s+8*s))/2.0
        zp=(u+math.sqrt(u*u-4.0))/2.0
        zm=1.0/zp
        recon=u**k/(u+2.0)**(k/2.0)
        max_res=max(max_res,abs(recon/lam-1.0),abs(zp+zm-u),abs(zp*zm-1.0))
        radical_cases+=1
assert max_res < 2e-12,max_res
print(f"VERIFY_OK exact_cases={exact_cases} radical_cases={radical_cases} max_residual={max_res:.3e}")
