#!/usr/bin/env python3
"""Exact rational jet checks for the local folded-saddle threshold expansion.

The infinite-parameter and stable-foliation theorems are proved analytically in RESULT.md.
This checker verifies formal identities on an extensive rational sample, without
assuming that sample constitutes an exhaustive proof.
"""
from fractions import Fraction as F

def add(x,y,n=4):
    return tuple((x[i] if i<len(x) else 0)+(y[i] if i<len(y) else 0) for i in range(n))

def neg(x): return tuple(-v for v in x)
def sub(x,y): return add(x,neg(y))
def mul(x,y,n=4):
    return tuple(sum(x[j]*y[i-j] for j in range(i+1) if j<len(x) and i-j<len(y)) for i in range(n))
def coeff(x,i): return x[i] if i<len(x) else 0

def check(b):
    a=1-b; c=1+b
    u1=-c/b
    u2=c*(b*b+2*b-1)/b**3
    u3=-c*(b**4+5*b**3+b*b-5*b+2)/b**5
    U=(F(1),u1,u2,u3)
    rr=(F(0),F(1),F(0),F(0))
    aa=(a,); one=(F(1),)
    # Saddle equation (u-a)(u-1)+r*u*(2u-a)=0 through r^3.
    saddle=add(mul(sub(U,aa),sub(U,one)),mul(rr,mul(U,sub(mul((F(2),),U),aa))))
    assert saddle == (0,0,0,0),('saddle',b,saddle)
    p1=F(2)/(b*c)
    p2=F(2)*(1-b)/b**3
    p3=F(2)*(b-1)**2*(b+2)/b**5
    P=(1/c,p1,p2,p3)
    # (2u-a)*phi=1 through cubic order.
    assert mul(sub(mul((F(2),),U),aa),P)==(1,0,0,0)
    # Jacobian entries at saddle to order required by eigen-slope equation.
    fu=neg(mul(sub(U,aa),add(sub(add(one,P),mul((F(2),),mul(P,U))),rr)))
    fphi=mul(sub(U,aa),mul(U,sub(U,one)))
    gu=mul((F(2),),mul(rr,P))
    gphi=mul(rr,sub(mul((F(2),),U),aa))
    m1=-F(2)/b**2
    m2=F(4)*c/b**3
    M=(F(0),m1,m2,F(0))
    # Differentiated invariance at saddle: (fu-gphi)m+fphi*m^2-gu=0.
    eig=sub(add(mul(sub(fu,gphi),M),mul(fphi,mul(M,M))),gu)
    assert coeff(eig,1)==0 and coeff(eig,2)==0,('slope',b,eig)
    # The local stable curve's curvature contributes first at r^4.
    D=sub(add(P,mul(M,sub(one,U))),(1/c,))
    B1=F(2)/(b*c)
    B2=-F(4)/b**2
    B3=F(2)*(4*b**3+7*b*b+1)/b**5
    assert (coeff(D,1),coeff(D,2),coeff(D,3))==(B1,B2,B3),('delta-jet',b,D)
    C1=b*c/2
    C2=b*c**3/2
    C3=c**4*(4*b**3+b*b-1)/(8*b)
    # Compose delta(r(delta)) through degree three.
    R=(F(0),C1,C2,C3)
    comp=add(add(mul((B1,),R),mul((B2,),mul(R,R))),mul((B3,),mul(mul(R,R),R)))
    assert comp==(0,1,0,0),('series inversion',b,comp)
    # f_uu at the undeformed saddle is exactly zero.
    fuu=2*(-a*(1/c)+3*(1/c)*1-(1/c)-0-1)
    assert fuu==0
    return 7

if __name__ == '__main__':
    samples={F(i,j) for j in range(2,31) for i in range(1,j)}
    tests=sum(check(b) for b in sorted(samples))
    print(f'PASS: {tests} rational jet-identity groups for {len(samples)} distinct Allee parameters.')
    print('Scope: formal algebra only. Stable-manifold estimates and all-real claims need the analytic proof.')
